"""
File: agents/questions_generator/__init__.py
Purpose: Package initialization file for the questions_generator agent module.
         This file makes the question_generator directory a Python package and
         imports the main agent module to make it accessible when the package is imported.

This allows other modules to import the questions_generator_agent using:
from agents.questions_generator import agent
or
from agents.questions_generator.agent import questions_generator_agent
"""

# Import the agent module from the current package
# This makes the questions_generator_agent definition available when the package is imported
from . import agent