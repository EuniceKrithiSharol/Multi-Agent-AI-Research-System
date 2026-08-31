from src.agents import (

    TaskPlannerAgent,

    ResearchAgent,

    AnalysisAgent,

    SummarizationAgent,

    ReportGenerationAgent
)


class MultiAgentOrchestrator:


    def __init__(

        self
    ):

        self.planner = (

            TaskPlannerAgent()
        )


        self.researcher = (

            ResearchAgent()
        )


        self.analyst = (

            AnalysisAgent()
        )


        self.summarizer = (

            SummarizationAgent()
        )


        self.report_generator = (

            ReportGenerationAgent()
        )


    def run_workflow(

        self,

        query
    ):

        plan = (

            self.planner
            .plan_task(
                query
            )
        )


        research = (

            self.researcher
            .conduct_research(
                query
            )
        )


        analysis = (

            self.analyst
            .analyze(
                research
            )
        )


        summary = (

            self.summarizer
            .summarize(

                research,

                analysis
            )
        )


        report = (

            self.report_generator
            .generate_report(

                query,

                research,

                analysis,

                summary
            )
        )


        return {

            "plan": plan,

            "research": research,

            "analysis": analysis,

            "summary": summary,

            "report": report
        }
