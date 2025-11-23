# Agent Explanation Video - 

# Google ADK Agent Samples

Welcome to the README file for Website builder agent which will be using Google Agent Development Kit (ADK). This is designed to provide practical, powerful and creative agents formation using the ADK framework.

The goal of this repository is to showcase multi-agent systems. 

---

## 🌱 Available Agent Projects

### Research-Driven Website Builder (`research_website_builder`)

*   **Architecture:** Multi-Agent, Sequential + Parallel Orchestration
*   **Description:** An advanced system that combines intelligent research capabilities with parallel processing. Takes a simple topic input and transforms it into a comprehensive research report webpage through a 6-agent pipeline: `Questions Generator` -> `5 Parallel Research Agents` -> `Query Generator` -> `Requirements Writer` -> `Designer` -> `Code Writer`.
*   **Best for:** Google search integration, research-driven development, and complex multi-agent orchestration with both sequential and parallel patterns.
---

## 🚀 General Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SumitSabu/Research_Driven_Website_Builder_Agent
```

### 2. Set Up Your API Key

To use the agents, you need a Google API key.

1.  Navigate into the specific project folder you want to run 
2.  Create a file named `.env` in that directory.
3.  Add your API key to the `.env` file:

```env
GOOGLE_API_KEY=your-google-api-key
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

You can get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

### 3. Set Up the Python Environment

Each project should be run in its own virtual environment to manage dependencies.

```bash
# Navigate to the project you want to run
cd path/to/specific_agent_project

# Create and activate a virtual environment using uv
uv venv
.venv\Scripts\activate.bat  #On Windows, 
source .venv/bin/activate  #On Mac 

# Install the project's dependencies
uv sync --all-groups
```

---

## 🤖 Running an Agent

After completing the setup for a specific project, you can run its agent(s) using the ADK web interface.

1.  Make sure you are in the project's root directory in your terminal.
2.  Launch the ADK web server:

```bash

# For the intelligent research-driven website builder 
cd Research_driven_website_builder_agent/
adk web ./agents
```

3.  Open your browser and go to `http://localhost:8000`.
4.  Select the desired agent from the dropdown menu and start interacting with it!
5.  Ideally open root_website_builder agent and provide a topic to that agent.


---# Research_Driven_Website_Builder_Agent
