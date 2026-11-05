# Architecture Overview (v13)

Modular design:
- Data layer: synthetic candles and features by default.
- Strategy layer: asset-class specific multi-factor adaptive signals with Supertrend proxies and options support.
- Risk layer: volatility scaling, regime filters, anomaly veto.
- Security layer: redaction, DLP, hash-chained audits, encryption helpers.
- CLI for demo and backtest simulation.

Inspired by AI-agent harness for safe development.
