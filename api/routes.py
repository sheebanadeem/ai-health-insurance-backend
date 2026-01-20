from fastapi import APIRouter, UploadFile, File, Form
from agents.policy_parser import policy_parser_agent
from services.pdf_loader import load_pdf_text

router = APIRouter()


@router.post("/analyze")
async def analyze_policy(
    policy_pdf: UploadFile = File(...),
    question: str = Form(...)
):
    try:
        policy_text = load_pdf_text(policy_pdf)

        if not policy_text.strip():
            return {"error": "PDF text extraction failed"}

        result = await policy_parser_agent.run(
            f"""
            POLICY DOCUMENT:
            {policy_text}

            USER QUESTION:
            {question}
            """
        )

        return {
            "answer": result.output
        }

    except Exception as e:
        return {"error": str(e)}
