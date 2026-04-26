import sys
import math

def calculate(expression):
    # Create a safe dictionary mapping math functions
    safe_dict = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    safe_dict['abs'] = abs
    safe_dict['math'] = math  # Allow the script to recognize the word "math."
    
    try:
        # Use an empty dictionary {} for __builtins__ to secure the eval function properly
        result = eval(expression, {"__builtins__": {}}, safe_dict)
        return result
    except Exception as e:
        return f"Error evaluating expression: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a mathematical expression.")
        sys.exit(1)
        
    expr = sys.argv[1]
    print(f"**Expression Calculated:** `{expr}`\n**Precise Result:** `{calculate(expr)}`")