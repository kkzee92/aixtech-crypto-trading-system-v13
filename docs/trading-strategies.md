# Enhanced Trading Strategies by Asset Class (v13)

All strategies are multi-factor, regime-aware, and return structured signals with confidence and size_pct. Position sizing is volatility-scaled. Enhanced with Supertrend-style proxies, better multi-TF consistency, and options/liquidity proxies.

## Majors (BTC, ETH)
Hybrid trend (EMA 50/200 + volume confirmation + Supertrend proxy) + mean reversion (RSI + Stochastic) with funding rate adjustment, on-chain activity proxy, multi-TF alignment, and volatility scaling. Regime filter (trend/range/stress) suppresses or reduces signals in stress. Adaptive confidence based on multi-timeframe alignment proxy.

## Large Alts
Relative strength vs BTC + MACD histogram + Supertrend + volume confirmation + BTC regime filter. Reduced size when BTC is stressed. Correlation filter vs majors.

## DeFi
Protocol metrics (TVL change 7d, fee revenue change) + price/RSI + on-chain activity + liquidity depth proxy. Exit on fundamental deterioration or high volatility. Yield farming / LP opportunity signals.

## Stablecoins
Peg premium arbitrage and yield differential signals. Very low directional risk; size based on deviation magnitude. Enhanced with cross-stable correlation.

## High Volatility
Strict filters: extreme volume spike + moderate ATR + regime check + Supertrend confirmation. Tiny position sizes only; higher anomaly threshold.

## Options / Derivatives Proxies
Implied vol vs realized vol, skew proxies, funding-based carry. Stand aside in high stress or extreme IV.

See `src/crypto_trading/strategies.py` for implementation details. All research/paper only.
