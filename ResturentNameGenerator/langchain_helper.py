from langchain_openai import OpenAI
from secrete_key import openapi_key
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.schema.runnable import RunnableSequence

import os

from sympy.physics.units import temperature

os.environ["OPENAI_API_KEY"] = openapi_key
llm = OpenAI(temperature=0.5)




def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate( input_variables = ['cuisine'],
                                           template = "I want to have some {cuisine} restaurant names"
                                          )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")


    prompt_template_items = PromptTemplate( input_variables = ['restaurant_name'], flush=True,
                                            template = """suggest menu items for {restaurant_name}. return it as comma separated string""",
                                         )
    items_chain = LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")

    chain = SequentialChain(chains= [name_chain,items_chain],
                            input_variables= ['cuisine'],
                            output_variables= ['restaurant_name',"menu_items"]
                           )
    response = chain.invoke({'cuisine' : cuisine})

    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Thai"))