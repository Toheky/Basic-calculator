from math import * 
from extractors import * 

def evaluate(user_text, active):
    '''Evaluate the expression pass like input.'''
    if "Σ(" in user_text:
        user_text = extract_summa(user_text)
    if "lcm(" in user_text:
        user_text = extract_lcm(user_text)
    if "τ" in user_text:
        user_text = user_text.replace("τ", "tau")
    if "π" in user_text:
        user_text = user_text.replace("π", "pi")
    if "√" in user_text:
        user_text = extract_sqrt(user_text)
    if "!" in user_text:
        user_text = extract_fact(user_text)
    if "cos(" in user_text or "sin(" in user_text or "tan(" in user_text:
        if active < 0:
            user_text = extract(user_text, active)
        else:
            user_text = extract(user_text, active)
    return eval(user_text)
 