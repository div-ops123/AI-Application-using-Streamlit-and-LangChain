# Phase 1: Project Setup + Load Secrets

import streamlit as st
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI


# Load secrets from .streamlit/secrets.toml
NEO4J_URI = st.secrets["NEO4J_URI"]
NEO4J_USER = st.secrets["NEO4J_USER"]
NEO4J_PASSWORD = st.secrets["NEO4J_PASSWORD"]

# Phase 2: Connect to AuraDB + test a Cypher query
graph = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USER,
    password=NEO4J_PASSWORD
)

# Test the connection with a basic Cypher query
st.set_page_config(page_title="Graph RAG Football Chatbot")
try:
    num_nodes = graph.query("MATCH (n) RETURN count(n) AS node_count")[0]["node_count"]
    st.success(f"✅ Connected to AuraDB! Total nodes: {num_nodes}")
except Exception as e:
    st.error(f"❌ Failed to connect to Neo4j: {e}")


# Phase 3: Setup LLM + GraphCypherQAChain

# Load secret
openrouter_api_key = st.secrets["OPENROUTER_API_KEY"]

# Use DeepSeek R1 0528 via OpenRouter
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",  # OpenRouter base URL
    api_key=openrouter_api_key,
    model="deepseek/deepseek-r1-0528:free"
)

# Create the GraphCypherQAChain. lets the LLM auto-generate Cypher from user questions
chain = GraphCypherQAChain.from_llm(
    llm=llm,
    graph=graph,
    verbose=True,  # shows the generated Cypher query for debuging
    show_intermediate_steps=True,
    allow_dangerous_requests=True
)


# Phase 4: Build the Streamlit UI for the chatbot
st.title("⚽ Graph RAG Football Chatbot")
st.markdown("Ask me anything about international football matches from 1872 to 2025.")

# Input box
user_question = st.text_input("Enter your question:")

# Submit button
if st.button("Ask"):
    if user_question:
        try:
            # Run the GraphCypherQAChain
            with st.spinner("Generating answer... please wait ⏳"):
                result = chain.invoke({"query": user_question})  # safer than run()
            
            st.success("Done!")

            # Show answer
            st.markdown("**Answer:**")
            st.write(result["result"])

        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a question.")
