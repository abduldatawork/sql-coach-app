import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os

# ===== SET UP THE UI ======
st.title("AI-Powered SQL Feedback Agent")
st.write("Get instant, expert feedback on your SQL query solutions.")

# Get API Key from Streamlit Secrets
openai_api_key = st.secrets.get("OPENAI_API_KEY")

if not openai_api_key:
    st.error("OpenAI API key not found in Streamlit secrets. Please add it to your Streamlit secrets.")
    st.stop()

# ====== DEFINE THE LOGIC (Our chain) ======
@st.cache_resource
def get_sql_feedback_chain():
    prompt_template = """
    You are an expert Senior SQL Developer acting as a helpful technical interviewer. 
    Your goal is to give constructive, actionable feedback to a candidate.

    Here is the SQL question they were asked:
    ---
    {question}
    ---

    Here is the candidate's submitted solution:
    ---
    {user_solution}
    ---

    Here is the optimal solution for reference:
    ---
    {optimal_solution}
    ---

    Please provice feedback on the candidate's solution by following this exact format:

    **1. Correctness:**
    (Is the query logically correct? Does it return the expected result? If not, what's wrong?)

    **2. Efficiency:**
    (Is the query efficient? Does it use appropriate JOINs? Does it avoid unnecessary subqueries? Compare it to the optimal solution.)
    
    **3. Readability & Style:**
    (Is the code well-formatted? Is it easy to understand? Are standard SQL conventions like capitalization used?)
    
    **4. Overall Recommendation:**
    (A one-sentence summary and a suggestion for improvement.)
    """

    sql_prompt = ChatPromptTemplate.from_template(prompt_template)

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=openai_api_key)
    output_parser = StrOutputParser()
    
    return sql_prompt | llm | output_parser

sql_feedback_chain = get_sql_feedback_chain()

# ====== CREATE THE INPUT FIELDS ======
st.subheader("The SQL Problem")
question = st.text_area(
    "Paste the question here:",
    "e.g., Find the name of the department with the highest number of employees."
)

st.subheader("Your SQL Solution")
user_solution = st.text_area(
    "Paste your query here:",
    "e.g., SELECT MAX(employees) FROM departements;"
)

st.subheader("The Optimal Solution")
optimal_solution = st.text_area(
    "Paste the ideal answer here:",
    "e.g., SELECT d.department_name FROM departments d JOIN employees e ON d.department_id = e.department_id GROUP BY d.department_name ORDER BY COUNT(e.employee_id) DESC LIMIT 1;"
)

# ====== RUN THE CHAIN ======
if st.button("Get Feedback"):
    if not question or not user_solution or not optimal_solution:
        st.error("Please fill in all fields.")
    else:
        with st.spinner("The AI Coach is thinking..."):
            # Create the input dictionary
            input_data = {
                "question": question,
                "user_solution": user_solution,
                "optimal_solution": optimal_solution,
            }
            
            # Run the chain
            feedback = sql_feedback_chain.invoke(input_data)
            
            # Display the feedback
            st.subheader("AI Coach's Feedback:")
            st.markdown(feedback)                   # Use markdown to render the bolding, etc.