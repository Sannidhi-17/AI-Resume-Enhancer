from model import LLMModel
from prompts import SUMMARY_PROMPT, ENHANCE_BULLET_PROMPT, TAILOR_PROMPT
from utils import pdf_to_text, split_sections, split_experience_bullets

## If any open source model wants to use
# llm = LLMModel()

## If chatGroq API wants to use
import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage

## Set API Key
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
os.environ['GROQ_API_KEY'] = GROQ_API_KEY
llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.7)


# def summarize_resume(text):
#     prompt = SUMMARY_PROMPT.format(section=text)
#     response = llm.generate(prompt)
#     return response['response']
    
## CHATGROQ API
def summarize_resume(text):
    print("----- Inside the summarize_resume function -----")
    prompt = SUMMARY_PROMPT.format(section=text)
    response = llm.generate([[HumanMessage(content=prompt)]])
    return response.generations[0][0].text


# def enhance_bullets(bullets, context=""):
#     enhanced = []
#     for b in bullets:
#         prompt = ENHANCE_BULLET_PROMPT.format(bullet=b, context=context)
#         enhanced_b = llm.generate(prompt)
#         enhanced.append(enhanced_b.strip())
#     return enhanced
    
## CHATGROQ API 
def enhance_bullets(bullets, context=""):
    enhanced = []
    for bullet in bullets:
        prompt = ENHANCE_BULLET_PROMPT.format(bullet=bullet, context=context)
        response = llm.generate([[HumanMessage(content=prompt)]])  # <-- pass string directly
        enhanced.append(response.generations[0][0].text)
    return enhanced


# def tailor_bullets(enhanced_bullets, job_description):
#     tailored = []
#     for b in enhanced_bullets:
#         prompt = TAILOR_PROMPT.format(bullet=b, jd=job_description)
#         tailored_b = llm.generate(prompt)
#         tailored.append(tailored_b.strip())
#     return tailored
## CHATGROQ API 
def tailor_bullets(enhanced_bullets, job_description):
    tailored = []
    for b in enhanced_bullets:
        prompt = TAILOR_PROMPT.format(bullet=b, jd=job_description)
        tailored_b = llm.generate([[HumanMessage(content=prompt)]])
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
