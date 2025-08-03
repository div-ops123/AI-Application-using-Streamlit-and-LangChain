# LangChain-Powered Graph RAG Chatbot

Install the driver
```bash
pip install -r requirements.txt
```

Create a file `.streamlit/secrets.toml` to keep secret

Designing Graph Schema (Nodes + Relationships)
This is the most important part: turning our CSV columns into graph shapes.


## 🎯 Goal-Driven Graph Design

Our chatbot needs to:

* Answer flexible questions like:

  * “Who scored for Nigeria in 2013?”
  * “What was the result of Brazil vs Argentina in 2004?”
  * “Which matches went to penalties?”
* Support **semantic search** (via LangChain RAG) and **precise Cypher queries**

---

## 🧱 Graph Schema:

#### 🟦 Nodes

* `(:Team {name})`
* `(:Player {name})`
* `(:Match {date, home_score, away_score, tournament, city, country, neutral})`

#### 🔗 Relationships

* `(Team)-[:PLAYED_HOME]->(Match)`
* `(Team)-[:PLAYED_AWAY]->(Match)`
* `(Player)-[:SCORED_IN {minute, own_goal, penalty}]->(Match)`
* `(Player)-[:SCORED_FOR]->(Team)`
* `(Team)-[:WON_SHOOTOUT]->(Match)`
* `(Team)-[:FIRST_SHOOTER_IN]->(Match)`

---

### ✅ Why This Schema Works for Our Chatbot

* Keeps things clean and fast to query
* Makes natural Cypher questions easier (ex: “Who scored in Nigeria’s 2-1 win over Ghana?”)
* Fits LangChain GraphRAG pipelines well (graph → retriever → context → LLM)

---

### 🟦 `:Team {name}`

* Comes from **`results.csv`**, **`goalscorers.csv`**, and **`shootouts.csv`**
* You’ll extract team names from:

  * `results.csv`:

    * `home_team`
    * `away_team`
  * `goalscorers.csv`:

    * `team`
  * `shootouts.csv`:

    * `home_team`
    * `away_team`
    * `winner`
    * `first_shooter`

So you’ll collect all unique team names from those columns to create `(:Team {name})` nodes.

---

### 🟨 `:Player {name}`

* Comes only from **`goalscorers.csv`**
* You’ll extract player names from:

  * `scorer` column

### `(:Match {date, home_score, away_score, tournament, city, country, neutral})`
* Comes only from `results.csv`
* Properties from all columns
