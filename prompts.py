SUMMARY_PROMPT = """
You are a professional resume writer.
Given this resume section, produce a 2-sentence professional summary
highlighting strengths and role fit.

Resume Text: {section}

Professional Summary:
"""

ENHANCE_BULLET_PROMPT = """
You are a resume optimization assistant. Transform the following resume bullet point
into a concise, action-oriented statement that highlights measurable impact.

Original bullet: {bullet}
Context (role/company/time): {context}

Enhanced bullet:
"""

TAILOR_PROMPT = """
You are a resume tailoring assistant.
Given an enhanced bullet and a job description, modify the bullet to better match
the job description’s required skills and keywords, without fabricating details.

Bullet: {bullet}
Job Description: {jd}

Tailored bullet:
"""
