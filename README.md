# ⚽ LangChain-Powered Graph RAG Chatbot

An intelligent chatbot that understands football like a fan and reasons like a graph. Built with LangChain, Neo4j AuraDB, and Streamlit.

---

## 🚀 Quick Start

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.streamlit/secrets.toml` file to store our Neo4j Aura credentials:

```toml
NEO4J_URI = "neo4j+s://<your-instance>.databases.neo4j.io"
NEO4J_USER = "<your-username>"
NEO4J_PASSWORD = "<your-password>"
OPENROUTER_API_KEY = "your-api-key"
```

Run:
```bash
streamlit run app.py
```

---

## 🧠 Our Goal: A RAG Chatbot That Knows Football

We designed this system to:

* Answer natural questions like:

  * “Who scored for Nigeria in 2013?”
  * “Which World Cup finals ended in shootouts?”
  * “What was the result of Brazil vs Argentina in 2004?”
* Use LangChain's **Graph RAG pipeline**: Cypher → context → LLM → answer
* Combine symbolic reasoning (graph) with semantic reasoning (LLM)

---

## 🧱 Our Graph Schema

We built a clean, fast, and queryable schema based on football match data:

### 🟦 Nodes

| Label     | Description                 |
| --------- | --------------------------- |
| `:Team`   | Football teams              |
| `:Player` | Goal scorers                |
| `:Match`  | Individual football matches |

Match node properties include:

* `date`, `home_score`, `away_score`, `tournament`, `city`, `country`, `neutral`

---

### 🔗 Relationships

| Relationship                            | Meaning                          |
| --------------------------------------- | -------------------------------- |
| `(:Team)-[:PLAYED_HOME]->(:Match)`      | Home team                        |
| `(:Team)-[:PLAYED_AWAY]->(:Match)`      | Away team                        |
| `(:Player)-[:SCORED_FOR]->(:Team)`      | Who the player scored for        |
| `(:Player)-[:SCORED_IN]->(:Match)`      | Which match the goal happened in |
| `(:Team)-[:WON_SHOOTOUT]->(:Match)`     | Team won the shootout            |
| `(:Team)-[:FIRST_SHOOTER_IN]->(:Match)` | Team kicked first in shootout    |

All relationships are meaningful to end-users — optimized for chat queries.

---

## 🗂️ Our Data Sources

We used three Kaggle CSVs:

| File              | Description                     |
| ----------------- | ------------------------------- |
| `results.csv`     | Full-time match results         |
| `goalscorers.csv` | Player-level goal data          |
| `shootouts.csv`   | Matches that ended in penalties |

---

## 🔍 Design Choices That Make It Work

* 🧠 Goal-driven schema — designed backwards from real questions
* ⚡ Fast ingestion — batches 100k+ relationships smoothly
* ✅ RAG-ready — fits LangChain’s GraphCypherQAChain pipeline
* 🤝 Graph-first design — fits LangChain's Graph Cypher QA chain perfectly

---
