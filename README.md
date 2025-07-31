# 🧠 AI Coding Agent (Claude Code Clone)

A toy AI coding assistant inspired by tools like **Claude Code** and **Cursor**, built using **Google's free Gemini API**. This CLI-based agent accepts coding tasks and intelligently chooses from a set of predefined tools to solve problems within a Python codebase.

> "fix my calculator app, it's not starting correctly"
> 💡 The agent scans files, reads content, writes updates, and executes Python scripts — all powered by LLM reasoning.

---

## 🚀 Features

* 🗨️ Accepts natural language coding requests via the command line
* 🛠️ Dynamically calls predefined functions like:

  * `get_files_info` – List files in a directory
  * `get_file_content` – Read a file's content
  * `write_file` – Overwrite a file
  * `run_python_file` – Run a Python script with arguments
* 🔁 Loops intelligently until the task is complete (or fails gracefully)
* 🔗 Built on **Gemini API** with structured function calling

---

## 🧪 Example Usage

```bash
uv run main.py "fix my calculator app, it's not starting correctly"
```
