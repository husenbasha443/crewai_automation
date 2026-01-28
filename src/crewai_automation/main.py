from crewai_automation.crew import CrewaiAutomation

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Perform a comprehensive static analysis on this enterprise backend system and identify critical risks'
    }

    try:
        CrewaiAutomation().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")