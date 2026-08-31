import streamlit as st

from src.orchestrator import MultiAgentOrchestrator


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="Multi-Agent AI Research System",
    page_icon="🤖",
    layout="wide"
)


# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "orchestrator" not in st.session_state:

    st.session_state.orchestrator = (
        MultiAgentOrchestrator()
    )


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title(
    "🤖 Multi-Agent AI Research & Task Automation System"
)


st.markdown(
    "An agentic AI system where multiple specialized agents "
    "collaborate to plan, analyze, summarize, and generate "
    "structured research reports."
)


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.header(
    "🧠 AI Agent Architecture"
)


st.sidebar.info(
    """
    1. Task Planner Agent

    2. Research Agent

    3. Analysis Agent

    4. Summarization Agent

    5. Report Generation Agent
    """
)


# -------------------------------------------------
# SYSTEM ARCHITECTURE
# -------------------------------------------------

st.subheader(
    "⚙️ Multi-Agent Workflow"
)


st.code(
    """
User Query
    ↓
Task Planner Agent
    ↓
Research Agent
    ↓
Analysis Agent
    ↓
Summarization Agent
    ↓
Report Generation Agent
    ↓
Final Structured Report
    """,
    language="text"
)


# -------------------------------------------------
# USER INPUT
# -------------------------------------------------

st.divider()


st.header(
    "🔍 Submit Research Task"
)


user_query = st.text_area(

    "Enter a research topic or task",

    placeholder=(
        "Example: Analyze the impact of artificial intelligence "
        "on cybersecurity and identify key opportunities and risks."
    ),

    height=150
)


# -------------------------------------------------
# RUN AGENTS
# -------------------------------------------------

if st.button(
    "🚀 Run Multi-Agent System"
):

    if user_query.strip() == "":

        st.warning(
            "Please enter a research topic."
        )

    else:

        with st.spinner(

            "AI agents are collaborating on your task..."
        ):

            results = (

                st.session_state.orchestrator
                .run_workflow(
                    user_query
                )
            )


        st.success(
            "Multi-agent workflow completed successfully!"
        )


        # -----------------------------------------
        # TASK PLAN
        # -----------------------------------------

        st.divider()


        st.subheader(
            "🧩 Task Planner Agent"
        )


        st.write(

            results[
                "plan"
            ]
        )


        # -----------------------------------------
        # RESEARCH
        # -----------------------------------------

        st.subheader(
            "🔎 Research Agent"
        )


        st.write(

            results[
                "research"
            ]
        )


        # -----------------------------------------
        # ANALYSIS
        # -----------------------------------------

        st.subheader(
            "📊 Analysis Agent"
        )


        st.write(

            results[
                "analysis"
            ]
        )


        # -----------------------------------------
        # SUMMARY
        # -----------------------------------------

        st.subheader(
            "📝 Summarization Agent"
        )


        st.write(

            results[
                "summary"
            ]
        )


        # -----------------------------------------
        # FINAL REPORT
        # -----------------------------------------

        st.divider()


        st.header(
            "📄 Final AI Report"
        )


        st.success(

            results[
                "report"
            ]
        )


# -------------------------------------------------
# SYSTEM INFORMATION
# -------------------------------------------------

st.divider()


st.header(
    "📊 System Information"
)


col1, col2, col3 = st.columns(3)


col1.metric(
    "AI Architecture",
    "Multi-Agent"
)


col2.metric(
    "Specialized Agents",
    "5"
)


col3.metric(
    "Workflow",
    "Sequential"
)


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()


st.caption(
    "Multi-Agent AI Research & Task Automation System | "
    "Python • Agentic AI • NLP • Task Planning • "
    "AI Orchestration"
)
