"""
File: agents/root_website_builder/__init__.py
Purpose: Package initialization file for the root_website_builder_agent module.
         This file makes the root_website_builder directory a Python package and
         imports the main agent module to make it accessible when the package is imported.

This allows other modules to import the root_website_builder_agent using:
from agents.root_website_builder import agent
or
from agents.root_website_builder.agent import root_website_builder_agent
"""

# Import the agent module from the current package
# This makes all agent definitions available when the package is imported
from . import agent # Imports agent.py from the same directory