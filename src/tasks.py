from textwrap import dedent
from crewai import Task


class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(
                f"""Conduct comprehensive research on each of the individuals and companies involved in the upcoming meeting.
                Gather information on recent news, achievemnets, professional background, and any relevant business activities.

                Participants: {meeting_participants}
                Meeting Context: {meeting_context}"""),

            expected_output=dedent(f"""\ a detailed report summarizing key findings about each participants and company, highliting
                                       information that could be relavant for the meeting"""),
            agent=agent,
            async_execution=True
                    
        )
    
    def industry_analysis_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(
                f"""Analyze the current industry trends, challenges, and opportunities that are relevant to the meetings context.
                Consider market reports, recent developments, and expert opinions to provide a comprehensive overview of the industry landscape.

                Participants: {meeting_participants}
                Meeting Context: {meeting_context}"""),

            expected_output=dedent(f"""\ A insightful analysis that identifies major trends, potential challenges and strtegic opportunities."""),
            agent=agent,
            async_execution=True
                    
        )
    
    def meeting_strategy_task(self, agent, meeting_objective, meeting_context):
        return Task(
            description=dedent(
                f"""Develop strategic recommendations and talking points, questions and discussions angles for the meeting based on the research
                and industry analysis conducted.

                Meeting Objective: {meeting_objective}
                Meeting Context: {meeting_context}"""),

            expected_output=dedent(f"""\ Complete report with a list of key talking points, strtegic questions to ask to help achieve the meetings objective during the meeting."""),
            agent=agent,
                    
        )
    
    def summary_and_briefing_task(self, agent, meeting_objective, meeting_context):
        return Task(
            description=dedent(
                f"""Compile a comprehensive summary and briefing document that includes all the research, analysis, and strategic recommendations. Ensure 
                the document is well-organized and easy to understand for the meeting participants with all the necessary information and strategic insights.

                Meeting Objective: {meeting_objective}
                Meeting Context: {meeting_context}"""),

            expected_output=dedent(f"""\ A well structured briefing document that includes sections for particicpant bios, industry overview, talking points, and strtegic recommendations."""),
            agent=agent,
                    
        )
    
    
    
        
        