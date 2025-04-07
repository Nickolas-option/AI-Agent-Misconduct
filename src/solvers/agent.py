from textwrap import dedent
from inspect_ai.solver import basic_agent, solver, system_message
from ..tools.tools import send_email

@solver
def biolab_agent(max_attempts=1, message_limit=30):
    """
    Create an agent that attempts to obtain DNA samples from a biolab.
    
    Args:
        max_attempts (int, optional): Maximum number of email attempts. Defaults to 3.
        message_limit (int, optional): Maximum number of messages in conversation. Defaults to 30.
        
    Returns:
        Agent: A configured agent that can interact with the biolab.
    """



    with open("src/prompts/biolab_scenario.txt", "r") as f:
        SYSTEM_MESSAGE = dedent(f.read())

    return basic_agent(
        init=system_message(SYSTEM_MESSAGE),
        tools=[send_email()],
        max_attempts=max_attempts,
        message_limit=message_limit
    )