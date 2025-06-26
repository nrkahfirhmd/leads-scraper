from pydantic import BaseModel
from typing import List, Optional, Union

class NeglectSignals(BaseModel):
    footer_year: Optional[str]
    last_blog_post: Optional[str]
    
class ScrapeResult(BaseModel):
    url: str
    tech_stack: List[str]
    neglect_signals: NeglectSignals
    stability_signals: List[str]
    growth_signals: List[str]
    fit_score: Optional[int] = None
    deal_memo: Optional[str] = None
    outreach_email: Optional[str] = None
    error: Optional[str] = None
    
class ScrapeRequest(BaseModel):
    urls: List[str]
    
class AnalyzeRequest(BaseModel):
    urls: List[str]

class GenerateSingleRequest(BaseModel):
    data: ScrapeResult