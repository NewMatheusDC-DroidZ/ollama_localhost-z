lightweight, responsive, and local-first web interface designed to interact with Ollama Models Locally. This project provides a clean, Gemini-inspired aesthetic that works seamlessly across Desktop and Mobile (Termux) environments.
Key Features
 * Dynamic Model Discovery: Automatically fetches and lists all locally installed models upon connection.
 * File Context Management: Attach text-based files (code, logs, notes) to your prompts. Files are visualized as removable chips and interactive bubbles within the chat.
 * Complete Markdown Support: Renders headers, bold text, lists, and tables using marked.js.
 * Smart Code Blocks: Syntax-aware blocks with a copy button that automatically strips language identifiers for clean pasting.
 * Persistent Sessions: Chat history and server configurations are saved to the browser's localStorage.
 * Responsive Design: Optimized for mobile viewports using dynamic height units to prevent keyboard overlap.
Installation and Setup
1. Configure Ollama (Required)
By default, browsers block requests to local APIs due to CORS policies. You must start Ollama with allowed origins to enable the web interface.
Windows (PowerShell):
$env:OLLAMA_ORIGINS="*"; ollama serve

Linux / macOS / Termux:
OLLAMA_ORIGINS="*" ollama serve

2. Launching the Interface
Desktop Environment:
 * Save the index.html file to your computer.
 * Open the file directly in any modern web browser (Chrome, Firefox, Edge).
 * Enter your Base URL (default is http://127.0.0.1:11434) and select your model to start.
Termux (Android):
 * Install Python if not already present: pkg install python.
 * Navigate to the directory containing index.html.
 * Start a local server:
   python -m http.server 8080

 * Access the UI via your mobile browser at: http://localhost:8080.
Handling Attachments
The interface handles files as supplementary context:
 * Click the "+" icon to select files.
 * Files appear as blue chips above the input bar.
 * Click the "×" on a chip to remove the file before sending.
 * Once sent, files appear as interactive blocks in the chat history. Clicking them allows you to view the raw content in a new tab.
Technical Specifications
 * Frontend: Vanilla JavaScript, CSS3 (Variables & Flexbox), HTML5.
 * Dependencies: marked.js (loaded via CDN) for Markdown processing.
 * Data Handling: Zero external tracking. All data remains within your local network and browser storage.
