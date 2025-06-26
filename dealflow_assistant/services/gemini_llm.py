import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def get_fit_score(data):
    prompt =  f"""
        You are an M&A analyst. Evaluate this business based on web signals.

        Return a single number from 1 to 10 that represents how good of a fit this business is for acquisition (10 = very attractive, 1 = poor target).

        Web signals:
        - Tech Stack: {data['tech_stack']}
        - Neglect Signals: {data['neglect_signals']}
        - Stability Signals: {data['stability_signals']}
        - Growth Signals: {data['growth_signals']}

        Respond with only a single number between 1 and 10.
    """
    
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    return response.text.strip()

def get_deal_memo(data):
    prompt =  f"""
        You are an M&A analyst. Based on the following web signals from a company, generate a 2–4 sentence investment memo explaining whether this company could be a good acquisition opportunity. Mention any signs of neglect, stability, or growth, and justify your opinion.

        Here is the data:
        - URL: {data['url']}
        - Tech Stack: {data.get('tech_stack')}
        - Neglect Signals: {data.get('neglect_signals')}
        - Stability Signals: {data.get('stability_signals')}
        - Growth Signals: {data.get('growth_signals')}
        - Fit Score: {data.get('fit_score')}

        Output:
    """
    
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    
    return response.text.strip()

def get_outreach_email(data):
    prompt =  f"""
        You are a search fund associate who identifies and reaches out to small business owners about potential acquisitions.

        Based on the following web data, write a short, authentic outreach email. Keep it professional, warm, and non-pushy. The email should be 4-6 sentences. Do not sell anything — the goal is to start a conversation.

        Company Info:
        - URL: {data['url']}
        - Tech Stack: {data.get('tech_stack')}
        - Neglect Signals: {data.get('neglect_signals')}
        - Stability Signals: {data.get('stability_signals')}
        - Growth Signals: {data.get('growth_signals')}
        - Fit Score: {data.get('fit_score')}
        - Deal Memo: {data.get('deal_memo')}

        Output just the email body (no subject line or extra text).
    """
    
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    
    return response.text.strip()