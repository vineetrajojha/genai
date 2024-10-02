import openai

# Set up the OpenAI API client
openai.api_key = 'your-api-key'

# Function to generate health analysis
def generate_health_analysis(product_name, calories, fat, sugar, sodium):
    prompt = f"Provide a health analysis for a product called {product_name} with {calories} calories, {fat}g fat, {sugar}g sugar, and {sodium}mg sodium."
    
    response = openai.Completion.create(
      model="gpt-3.5-turbo",
      prompt=prompt,
      max_tokens=150
    )
    
    return response['choices'][0]['text']

# Example usage
product_name = "Chocolate Bar"
calories = 500
fat = 30
sugar = 40
sodium = 10

analysis = generate_health_analysis(product_name, calories, fat, sugar, sodium)
print(analysis)
