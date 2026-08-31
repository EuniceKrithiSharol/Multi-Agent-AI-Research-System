from src.agents import (

    TaskPlannerAgent,

    ResearchAgent,

    AnalysisAgent
)


def test_task_planner():

    agent = (

        TaskPlannerAgent()
    )


    result = agent.plan_task(

        "Artificial Intelligence"
    )


    assert "Task" in result


def test_research_agent():

    agent = (

        ResearchAgent()
    )


    result = agent.conduct_research(

        "Artificial Intelligence"
    )


    assert len(

        result

    ) > 0


def test_analysis_agent():

    agent = (

        AnalysisAgent()
    )


    result = agent.analyze(

        "Research output"
    )


    assert len(

        result

    ) > 0
