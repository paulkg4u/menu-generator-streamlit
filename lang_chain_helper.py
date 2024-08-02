
from langchain_community.llms.ollama import Ollama
from langchain.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain.chains.sequential import SequentialChain
from langchain.chains.llm import LLMChain
llm = Ollama(model='llama3')


def get_restaurant_name(cuisine: str):

    prompt_template_name = PromptTemplate(template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this. Only one name please. dont add any extra text",
                                          input_variables=["cuisine"])

    # name_chain = (prompt_template_name | llm)
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,
                          output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        template="Suggest some menu items for  {restaurant_name} restaurant. Return it as comma seperated list. Just give the items list only. dont add any extra text",
        input_variables=["restaurant_name"],
        output_parser=StrOutputParser()
    )

    # food_items_chain = (prompt_template_items | llm)
    food_items_chain = LLMChain(
        llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(chains=[name_chain, food_items_chain], verbose=True, input_variables=[
                            "cuisine"], output_variables=["restaurant_name", "menu_items"])
    response = chain.invoke(cuisine)
    print(response)
    return response
