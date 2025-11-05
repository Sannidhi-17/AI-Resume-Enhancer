from model import LLMModel
from prompts import SUMMARY_PROMPT, ENHANCE_BULLET_PROMPT, TAILOR_PROMPT
from utils import pdf_to_text, split_sections, split_experience_bullets

llm = LLMModel()

def summarize_resume(text):
    prompt = SUMMARY_PROMPT.format(section=text)
    response = llm.generate(prompt)
    return response['response']

def enhance_bullets(bullets, context=""):
    enhanced = []
    for b in bullets:
        prompt = ENHANCE_BULLET_PROMPT.format(bullet=b, context=context)
        enhanced_b = llm.generate(prompt)
        enhanced.append(enhanced_b.strip())
    return enhanced

def tailor_bullets(enhanced_bullets, job_description):
    tailored = []
    for b in enhanced_bullets:
        prompt = TAILOR_PROMPT.format(bullet=b, jd=job_description)
        tailored_b = llm.generate(prompt)
        tailored.append(tailored_b.strip())
    return tailored

def run_pipeline_from_pdf(pdf_path, job_description=None):
    text = pdf_to_text(pdf_path)
    sections = split_sections(text)
    experience_text = sections.get("experience", sections.get("full", ""))
    bullets = split_experience_bullets(experience_text)

    enhanced = enhance_bullets(bullets, context="")
    tailored = tailor_bullets(enhanced, job_description) if job_description else enhanced

    summary = summarize_resume(text)
    return {"summary": summary, "bullets": tailored}
