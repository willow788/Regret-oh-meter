from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

app = FastAPI(title="REGRET-O-METER", version="1.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#optional sarcasm inducing words
sarcasm_inducing_words = ["great idea", "yeah right", "sure", "totally", "of course 🙄", "amazing 🙃", "hell yeah"]

#self blamig phrases
self_blaming_phrases = [
    "I should have", "I could have", "If only I had", 
    "It's my fault", "I messed up", "I regret", 
    "I wish I had", "I shouldn't have"
]

#self blaming words
self_blaming_words = [
    "stupid", "idiot", "dumb", "foolish", 
    "lazy", "careless", "reckless"
]   

#emoji scoring your ass
emoji_scores = {
    "😞": 2,
    "😔": 2,
    "😢": 3,
    "😭": 4,
    "😡": 3,
    "😠": 3,
    "😩": 2,
    "😖": 2,
    "😣": 2,
    "😤": 2,
    "🙄": 1,
    "😕": 1
}

class TextInput(BaseModel):
    text: str
    #means it will take a string input with key 'text'

@app.post("/analyze")
def analyze_text(input: TextInput):
    lines = input.text.split('\n')
    regrets = [] # list to hold regret scores for each line

    for line in lines:
        score = 0
        
        # Sentiment analysis using negative keywords
        negative_words = ["bad", "terrible", "awful", "horrible", "worst", "hate", "regret", "mistake", "wrong", "failed", "disaster"]
        if any(word in line.lower() for word in negative_words):
            score += 300
        

        #keywords indicating self-blame
        if any(word in line.lower()  for word in ["oops", "shouldn't", "why", "ugh", "forgot"]):
           score += 200


        #sacrasm inducing phrases
        if any(phrase in line.lower() for phrase in sarcasm_inducing_words):
            score += 150


        #sarcasm detecting words
        if any(word in line.lower() for word in sarcasm_inducing_words):
            score +=250


        #self blaming phrases
        if any(word in line.lower() for word in self_blaming_words):
            score += 200

        #emoji detection
        for emoji , emoji_score in emoji_scores.items():
            if emoji in line:
                score += emoji_score


        regrets.append({'line': line, 'regret_score': score})

    if regrets:
        top_regret = max(regrets, key= lambda x: x['regret_score'])
        average_screwups = sum(r['regret_score'] for r in regrets) / len(regrets)

    else:
        top_regret = {'line': '', 'regret_score': 0}
        average_screwups = 0

    

    #comments by ai 
    comments =[
        "Legendary chaos detected.",
        "Mildly questionable choices today.",
        "Smooth operator, zero regrets."
        
        
    ]

    if average_screwups >75:
        ai_comment = comments[0]
    
    elif average_screwups >40:
        ai_comment = comments[1]
    else:
        ai_comment = comments[2]


    return{
        "regret_score": average_screwups,
        "top_regret": top_regret,
        "comment": ai_comment
    }
