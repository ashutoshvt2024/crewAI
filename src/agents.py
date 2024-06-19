from textwrap import dedent
from crewai import Agent

from tools import ExaSearchToolset

class MeetingPrepAgents():
    def research_agent(self):
        return Agent(
            role="Research Specialist",
            goal=dedent(""" Conduct a thorough research on the people and companies involved in the meeting"""),
            tools=ExaSearchToolset.tools(),
            backstory=dedent("""\ 
                             As a research specialist, your role is to gather and analyze information about 
                             the participants and companies involved in the upcoming meeting."""),

            verbose=True              

        )
    def industry_analysis_agent(self):
      return Agent(
        role='Industry Analyst',
        goal='Analyze the current industry trends, challenges, and opportunities',
        tools=ExaSearchToolset.tools(),
        backstory=dedent("""\
            As an Industry Analyst, your analysis will identify key trends,
            challenges facing the industry, and potential opportunities that
            could be leveraged during the meeting for strategic advantage."""),
        verbose=True
      )
    
    def meeting_strategy_agent(self):
      return Agent(
        role='Meeting Strategy Advisor',
        goal='Develop talking points, questions, and strategic angles for the meeting',
        backstory=dedent("""\
            As a Strategy Advisor, your expertise will guide the development of
            talking points, insightful questions, and strategic angles
            to ensure the meeting's objectives are achieved."""),
        verbose=True
      )
    
    def summary_and_briefing_agent(self): 
      return Agent(
        role='Briefing Coordinator',
        goal='Compile all gathered information into a concise, informative briefing document',
        backstory=dedent("""\
            As the Briefing Coordinator, your role is to consolidate the research,
            analysis, and strategic insights."""),
        verbose=True
      )