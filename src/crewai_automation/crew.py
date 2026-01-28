from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class CrewaiAutomation():
    """CrewaiAutomation crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def code_ingestion_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['code_ingestion_agent'], 
            verbose=True
        )

    @agent
    def bug_detection_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['bug_detection_agent'], 
            verbose=True
        )


    @agent
    def validation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['validation_agent'], 
            verbose=True
        )


    @task
    def code_ingestion_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_ingestion_task'], 
        )

    @task
    def bug_detection_task(self) -> Task:
        return Task(
            config=self.tasks_config['bug_detection_task'], 
        )


    @task
    def validation_task(self) -> Task:
        return Task(
            config=self.tasks_config['validation_task'], 
            output_file='report.md'
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiAutomation crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
