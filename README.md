# AI Posts generator

This repository contains a project that works with LangChain and LangServe.

## Prerequisites

- Python (version 3.11.3 or higher)
- virtualenv

## Setup

1. Clone this repository:
   ```
   git clone git@github.com:lucasayb/ai-posts-generator.git
   cd ai-posts-generator
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on the `.env.example` file:
   ```
   cp .env.example .env
   ```
   Then, edit the `.env` file to include your specific configurations.

5. Place your PDF file inside the `documents/` folder.

## Running the Application

To run the LangServe application, execute:

```
python main.py
```

You can run it in dev mode too:

```
fastapi dev main.py  
```