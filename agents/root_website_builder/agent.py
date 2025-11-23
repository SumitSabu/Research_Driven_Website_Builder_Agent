"""
File: agents/root_website_builder/agent.py
Purpose: Defines the Website builder agent. This agent acts as an orchestrator, guide for all the other agents.

This is the entry point agent in the website building pipeline that:
1. Receives a Topic from user
2. Provide that topic to questions generator agent, which generates 5 questions, related to the topic.
3. This is a sequential agent that executes the sub agents in the provided order
"""

# Import required system modules for path manipulation
import os  # Operating system interface for file paths
import sys  # System-specific parameters and functions

# Import the SequentialAgent class from Google ADK (Agent Development Kit)
from google.adk.agents import SequentialAgent

# Add the project root directory to Python path so we can import utility modules
# This allows importing from the utils directory two levels up from current file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))


# Import utility function to load instruction files from text files
from utils.file_loader import load_file  # Helper to read instruction text files


from agents.questions_generator.agent import questions_generator_agent
from agents.questions_researcher.agent import questions_researcher_agent
from agents.query_generator.agent import query_generator_agent
from agents.requirements_writer.agent import requirements_writer_agent
from agents.designer.agent import designer_agent
from agents.code_writer.agent import code_writer_agent

# Create the Website Builder Agent instance
root_agent = SequentialAgent(
    # Agent identifier - unique name for this agent in the system
    name="root_website_builder_agent",
    sub_agents=[
        questions_generator_agent,
        questions_researcher_agent,
        query_generator_agent,
        requirements_writer_agent,
        designer_agent,
        code_writer_agent
    ],
    
    # Load agent description from external text file
    # Provides a brief summary of this agent's technical business analyst role
    description=load_file("agents/root_website_builder/description.txt")
)