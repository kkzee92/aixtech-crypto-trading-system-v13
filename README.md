# AIxTech Crypto Trading System v13

> Enhanced paper-only automated cryptocurrency trading information system with further refined multi-factor adaptive strategies per asset class, advanced regime detection with volatility forecasting proxies, and strengthened zero-trust cyber and data security architecture. Inspired by zeekiankok92/aixtech-agent-harness-demo.

**Disclaimer:** Research and educational purposes only. No live order execution, no withdrawal permissions, no financial advice. Cryptocurrency trading involves substantial risk of loss. This system uses synthetic data by default and is designed for backtesting and simulation only.

## Overview
Builds on previous versions (v12) and the AI coding-agent harness from [zeekiankok92/aixtech-agent-harness-demo](https://github.com/zeekiankok92/aixtech-agent-harness-demo). Features:

- Asset-class specific strategies: Majors (BTC/ETH), Large Alts, DeFi, Stablecoins, High-Volatility, Options/Derivatives proxies, with enhanced multi-factor signals (EMA, RSI, MACD, Supertrend proxy, volume, on-chain, funding)
- Advanced regime-aware filtering with volatility forecasting proxies and adaptive position sizing
- On-chain and funding rate proxies integrated into signal generation
- Advanced risk gates: position limits, drawdown controls, correlation awareness, anomaly detection
- Strengthened zero-trust security: expanded secret redaction (including mnemonics, private keys, API keys), hash-chained audits with timestamps, input validation, encryption helpers, enhanced threat model and DLP
- Synthetic data mode by default for CI and safe agent development
- CI gates inspired by the harness (lint, tests, secret scan)

## Quick Start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m crypto_trading demo
```

## Architecture
See [docs/architecture.md](docs/architecture.md).

## Strategies
See [docs/trading-strategies.md](docs/trading-strategies.md).

## Security
See [SECURITY.md](SECURITY.md) and [docs/security-architecture.md](docs/security-architecture.md).

## Licence
MIT
