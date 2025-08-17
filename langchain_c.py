from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secert_key import openai_key

import os
os.environ['OPENAI_API_KEY'] = openai_key

llm = OpenAI(temperature=0.7)



def generate_restaurant_name_and_items(cuisine):
    # chain 1: restaurant Name
    prompt_template_name = PromptTemplate(
input_variables = ['cuisine'],
template = "I want to open a restaurant for {cuisine} food. suggest a fancy name for this."
)
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

   # chain 2: Menu items
    prompt_template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = " suggest some menu items for {restaurant_name}. Return it as a comma seperated list"
        )
    
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
        )
    
    response = chain({'cuisine': cuisine})

    return response

if __name__ =="__main__":
    print(generate_restaurant_name_and_items("Italian"))