# CORTA.BOX Indicator v1.0.7

## Overview

The **CORTA.BOX** indicator is a technical analysis tool developed for TradingView using Pine Script v5. This indicator helps traders identify potential trading opportunities based on gap analysis and price re-entry within a specified range. It highlights gaps in price action and marks potential entry points based on defined conditions, enhancing decision-making for traders.

## Features

- Detects bullish and bearish gaps based on price action.
- Provides visual markings for gap zones.
- Highlights potential entry points when price re-enters gaps.
- Allows customization of key parameters for tailored analysis.
- Implements volume filtering for increased accuracy.
- Suggests risk management levels (stop loss and take profit) based on gap size.

## Installation

1. Open TradingView.
2. Navigate to the Pine Script editor.
3. Copy and paste the entire code of the CORTA.BOX indicator into the editor.
4. Click on the **Add to Chart** button to apply the indicator to your chart.

## Parameters

The following parameters can be customized:

- **Minimum Gap Size (Ticks)**: 
  - **Type**: Integer
  - **Default**: 2
  - Sets the minimum size of gaps in ticks for detection.

- **Show Gap Zones**: 
  - **Type**: Boolean
  - **Default**: true
  - Displays gap zones on the chart.

- **Highlight Potential Entries**: 
  - **Type**: Boolean
  - **Default**: true
  - Highlights potential entry points when price re-enters a gap.

- **Use Volume Filter**: 
  - **Type**: Boolean
  - **Default**: true
  - Enables filtering of gaps based on minimum volume requirements.

- **Minimum Volume for Valid Gaps**: 
  - **Type**: Integer
  - **Default**: 1000
  - Sets the minimum volume for gaps to be considered valid.

- **Session Start Time (ET)**: 
  - **Type**: Time
  - **Default**: 08:30
  - Defines the start time for session analysis.

- **Session End Time (ET)**: 
  - **Type**: Time
  - **Default**: 15:30
  - Defines the end time for session analysis.

- **Time Filter (Only during U.S. Session)**: 
  - **Type**: Boolean
  - **Default**: true
  - Limits analysis to the specified session time.

- **Risk-Reward Ratio**: 
  - **Type**: Float
  - **Default**: 1.5
  - Sets the risk-reward ratio for determining profit targets.

- **Stop Loss Multiplier for Gap Size**: 
  - **Type**: Float
  - **Default**: 0.5
  - Multiplier used to calculate stop loss levels based on gap size.

## How It Works

1. **Gap Detection**: 
   - The script identifies bullish and bearish gaps based on price action between three consecutive candles.
   - A bullish gap is detected when the low of the previous candle is above the high of the current candle, and the gap size meets the defined threshold.
   - A bearish gap is detected when the high of the previous candle is below the low of the current candle, again subject to the defined gap size.

2. **Volume Filtering**: 
   - The script checks whether the trading volume meets the minimum volume requirement for the gaps to be considered valid.

3. **Re-entry Check**: 
   - The script checks if the price re-enters the gap zone within three subsequent candles.
   - If re-entry occurs, the gap zones are visually marked on the chart.

4. **Entry Highlighting**: 
   - Potential entry points are highlighted if the price crosses back into the gap zone.

5. **Risk Management**: 
   - Calculates stop loss and take profit levels based on the gap size and user-defined ratios.
   - Displays these levels visually on the chart.

6. **Alerts**: 
   - The script can trigger alerts when potential entry points are detected, assisting traders in real-time decision-making.

## Notes

- Ensure that the chart's timezone is set to Eastern Time (ET) to match the session times defined in the input parameters.
- Adjust parameters based on individual trading strategies and market conditions.
- This indicator is designed for educational and informational purposes and should be used in conjunction with other analysis methods.

## License

This code is provided for personal use and educational purposes. Redistribution or modification without consent is prohibited.
