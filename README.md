# [Ai assistant - using MCP server]

[Brief one-line description of your project.]

---

## Overview


This project enables browser automation using the Model Context Protocol (MCP). It connects LLMs to external tools like Playwright, DuckDuckGo, and Airbnb, allowing for real-time web interaction, data extraction, and workflow automation.]

---

## Architecture

![Architecture Diagram](architecture-diagram.png)  -![Untitled Diagram drawio](https://github.com/user-attachments/assets/06ebca27-8a0f-4d96-8ff7-812a8d95381e)

_The diagram above illustrates the system architecture. The main components are:_
- **Host (Cursor IDE):** Orchestrates user input, LLM responses, and tool invocation.
- **LLM (Groq via LangChain):** Processes user queries and generates actions or responses.
- **MCP Servers:** Provide access to external tools (Playwright for browser automation, DuckDuckGo for search, Airbnb for listings, etc.).
- **User:** Interacts with the system via the host application.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/sohailayan/mcp-uses.git
    cd 
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    # or for Node.js servers
    npm install
    ```

3. **Set up environment variables:**  
   Create a `.env` file and add your keys (e.g., `GROQ_API_KEY`).

---

## Usage

1. **Start the MCP servers:**
    - Example for Playwright:
      ```
      npx @playwright/mcp@latest
      ```
    - Example for DuckDuckGo:
      ```
      npx duckduckgo-mcp-server
      ```
    - [Add commands for other servers as needed]

2. **Run the main chat application:**
    ```
    python main.py
    ```

3. **Interact:**  
   Type your queries (e.g., "Go to https://www.imdb.com/chart/top and list the top 10 movies.") and the agent will process them using the connected tools.

---

## Configuration

- **MCP Servers:**  
  Configure your MCP servers in `browser_mcp.json` as shown below:
{
"mcpServers": {
"playwright": {
"command": "npx",
"args": ["@playwright/mcp@latest"]
},
"duckduckgo-search": {
"command": "npx",
"args": ["duckduckgo-mcp-server"]
},
"airbnb": {
"command": "npx",
"args": ["@openbnb/mcp-server-airbnb", "--ignore-robots-txt"]
}
}
}

text

- **Environment Variables:**  
Add your API keys and secrets to the `.env` file.

---

## Contributing

Contributions are welcome!  
- Fork this repository
- Create a new branch (`git checkout -b feature/your-feature`)
- Commit your changes
- Open a pull request

---


## Contact

For questions or support, open an issue or email [abbasayan4167@gmail.com].

---
