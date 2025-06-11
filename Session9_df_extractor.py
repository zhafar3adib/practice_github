import os
import pandas as pd
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import GoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

class Person(BaseModel):
  name: str = Field(description="Name of the person")
  age: int = Field(description="Age of the person")
  city: str = Field(description="City where the person lives")
  favorite_sport: str = Field(description="Favorite sport of the person")

def main():
  model = GoogleGenerativeAI(model="gemini-1.5-flash")
  parser = JsonOutputParser(pydantic_object=Person)

  prompt_template = (
    "Please extract the following query into a structured data according"
    " to: {input_str}. Please extract both the set of attributes: name, age, city, favorite_sport for"
    " each person. If some attributes are not specified, put a Null type in it."
  )

  input_str = """My name is John and I am 25 years old. I live in 
          New York and I like to play basketball. His name is 
          Mike and he is 30 years old. He lives in San Francisco 
          and he likes to play baseball. Sarah is 20 years old 
          and she lives in Los Angeles. She likes to play tennis.
          Her name is Mary and she is 35 years old. 
          She lives in Chicago."""
  
  prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["input_str"]
  )

  prompt_and_model = prompt | model
  output = prompt_and_model.invoke({"input_str": input_str})
  result = parser.invoke(output)
  print(result)

if __name__=="__main__":
  main()