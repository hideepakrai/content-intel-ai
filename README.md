content-intel-ai/
│
├── app/
│   ├── main.py
│   ├── gpt_engine.py
│   ├── processor.py
│   ├── url_handler.py         ← NEW: Fetch & clean URL
│   ├── agent_saver.py         ← NEW: Save/load agent configs
│   ├── exporter.py            ← Future: PDF/Excel output
│   ├── prompt_templates.py    ← Custom prompt per domain/role
│   ├── task_flow.py
│   └── version_tracker.py
│
├── versions/
│   ├── task_flow.json
│   └── version_log.csv
│
├── uploads/                   ← Local storage of uploaded files
├── projects/                  ← Save per-project info
├── agents/                    ← Saved agent configs
├── outputs/                   ← Exported summaries
├── .env
├── requirements.txt
└── README.md

