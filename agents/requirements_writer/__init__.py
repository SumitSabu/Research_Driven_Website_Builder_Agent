"""
File: agents/requirements_writer/__init__.py
Purpose: Package initialization file for the requirements_writer agent module.
         This file makes the requirements_writer directory a Python package and
         imports the main agent module to make it accessible when the package is imported.

This allows other modules to import the requirements_writer_agent using:
from agents.requirements_writer import agent
or
from agents.requirements_writer.agent import requirements_writer_agent
"""

# Import the agent module from the current package
# This makes all agent definitions available when the package is imported
from . import agent # Imports agent.py from the same directory