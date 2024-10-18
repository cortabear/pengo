# gapSizeTicks   
Adjust this to set the minimum size for gaps in ticks. For a more conservative approach, increase the value, or decrease it for more aggressive gap detection.  

```js
gapSizeTicks = input.int(2, title="Minimum Gap Size (Ticks)", minval=1)  
```
**Type**: Integer  
**Default Value**: 2  
**Range**: >= 1  
  
**Description**  
The gapSizeTicks parameter defines the minimum size of a gap required for the indicator to consider it valid. The size of the gap is measured in ticks, where a tick is the smallest possible price increment or decrement for the asset. The number entered for this parameter determines the threshold used to detect gaps in price levels between bars (candles).

A gap is considered bullish if the low of a previous candle (A) is greater than the high of a current candle (C), with the difference being greater than or equal to the specified gap size.
Conversely, a gap is bearish if the high of a previous candle (A) is less than the low of a current candle (C), and the difference exceeds the set gap size.

**Technical Explanation**  
When detecting a gap, the script calculates the difference between the relevant high and low prices of two candles. If the difference exceeds the product of gapSizeTicks and the minimum tick size (syminfo.mintick), the gap is flagged.

**Usage Example**  
If the gapSizeTicks is set to 2, the gap must be at least two ticks wide before the script considers it valid for further analysis.  

