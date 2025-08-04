import nbformat
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import warnings
import os

warnings.filterwarnings("ignore")


key2 = os.getenv("HFAPIKEY")



llm_model = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id="deepseek-ai/deepseek-V3",
        task="text-generation",
        huggingfacehub_api_token=key2,
        temperature=0.1, 
        max_new_tokens=512 # Adjust as needed for feedback length
    )
)

# template de evaluacion
evaluation_template = """
Eres un profesor experimentado y objetivo en la materia de {materia}.
Tu tarea es evaluar la solución de un estudiante a un problema de examen y proporcionar feedback.

---
**Examen:**
{problems}

**Solución del estudiante:**
{student_solution}
---

**Criterios de Evaluación:**
1.  **Corrección:** ¿La solución es matemáticamente y conceptualmente correcta?
2.  **Claridad:** ¿La explicación es clara y fácil de entender?
3.  **Completitud:** ¿La solución aborda todos los aspectos de la pregunta?
4.  **Justificación:** ¿Se proporcionan los pasos o el razonamiento adecuado?

Por favor, evalúa la solución del estudiante y proporciona:
1.  Un **porcentaje de resolución** para cada problema específico (un número del 0 al 100).
2.  **Feedback constructivo** breve, explicando por qué se otorgó ese porcentaje y qué se podría mejorar.
3.  **No incluyas ejemplos de código o soluciones correctas en tu feedback.** Enfócate solo en la evaluación de la respuesta del estudiante.

Formato de salida deseado para cada problema i:
Problema [i]
Porcentaje de Resolución: [X]%
Feedback: [Tu feedback detallado aquí]
-----
Problema [i+1]
Porcentaje de Resolución: [X]%
Feedback: [Tu feedback detallado aquí]
"""

evaluation_prompt = PromptTemplate(
    template=evaluation_template,
    input_variables=["materia", "problems", "student_solution"]
)

evaluation_chain = LLMChain(llm=llm_model, prompt=evaluation_prompt)

def evaluate_notebook(problems, solutions, materia):

        try:
            response = evaluation_chain.invoke({
                "materia": materia,
                "problems": problems,
                "student_solution": solutions
            })
 
            llm_output = response.get('text', '').strip()
            return llm_output

        except Exception as e:
            print(f"Error al evaluar : {e}")
            return None
            


if __name__ == "__main__":
    problems_file = "problemas.ipynb"
    respuestas_file = "respuestas_sudentA.ipynb"
    nb_problemas = nbformat.read(problems_file, as_version=4)
    nb_respuestas = nbformat.read(respuestas_file, as_version=4)
    student_name = (respuestas_file.split(".")[0]).split("_")[1]
    curso = "Metodos Numericos"
    print(f"\n--- Preparando para evaluar a {student_name}")
    results = evaluate_notebook(nb_problemas, nb_respuestas, curso)

    print("\n--- Resumen de Evaluación ---")
    print(results)
