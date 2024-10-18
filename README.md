# Corta.Box
Configure your box to store trade log in your Google drive.  


## Parameters for Customization  
By adjusting these parameters, traders can tailor the behavior of the Corta Box indicator to suit their personal strategies and chart preferences.  

### gapSizeTicks   
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


### showGaps   
Turn on or off the visual representation of gap zones on the chart. Keep it on for better visual clarity of gap regions.  

```js
showGaps = input.bool(true, title="Show Gap Zones")
```
**Type**: Boolean (True/False) 
**Default Value**: TRUE   
  
**Description**  
The showGaps parameter controls whether gap zones are visually represented on the chart. When set to true, the script paints a box over detected gap zones. These boxes visually indicate regions where the price has experienced a gap, helping traders quickly identify potential opportunities for entry or exit.  
- When a bullish gap is identified, a green box is drawn between the high of the current candle and the low of the prior candle.  
- For a bearish gap, a red box is drawn between the high of the prior candle and the low of the current candle.  

**Technical Explanation**  
If showGaps is set to true, the script will execute the box.new function to create a box over the gap zone. The box extends horizontally over the relevant candles and is color-coded based on the type of gap (green for bullish, red for bearish).

**Usage Example**  
Set showGaps to false if you prefer not to display gap zones on the chart and only want to identify potential entry points.  


### highlightEntries  
Turn on or off the marking of potential entries when the price re-enters the gap zone. Use this feature to identify possible entry points when gaps are filled.  
 
```js
highlightEntries = input.bool(true, title="Highlight Potential Entries")  
```
**Type**: Boolean (True/False) 
**Default Value**: TRUE   
  
**Description**  
The highlightEntries parameter controls whether potential entry points are marked on the chart when the price re-enters a gap zone. This feature highlights moments when the price revisits the gap area, which is often considered a critical point for trading decisions.  
- A green label will be placed if the price enters a bullish gap zone (i.e., if the price closes inside the gap between the prior low and the current high).  
- A red label will be placed if the price enters a bearish gap zone (i.e., if the price closes inside the gap between the prior high and the current low).  

**Technical Explanation**  
When highlightEntries is enabled, the script evaluates whether the price has re-entered a previously identified gap within a specified window of time (typically 3 candles after the gap is detected). If the condition is met, a label (upward or downward) is drawn on the chart at the point of entry.

**Usage Example**  
Set highlightEntries to true to monitor key moments when price re-enters the gap zone, providing potential trading signals. Setting it to false disables this behavior, which is useful if you only want to track the gap zones without focusing on entries.    







```js
gapSizeTicks = input.int(2, title="Minimum Gap Size (Ticks)", minval=1)


```







```js
tickSize = syminfo.mintick
```

```js
var float aHigh = na
var float aLow = na
var float bHigh = na
var float bLow = na
var float cHigh = na
var float cLow = na
```

```js
var bool reenteredGap = false
```











### IF Bar Index is less than or equal to 2   
  
```js
bullishGap = (aLow > cHigh) and (aLow - cHigh) >= gapSizeTicks * tickSize
bearishGap = (aHigh < cLow) and (cLow - aHigh) >= gapSizeTicks * tickSize
```

```js
reenteredGap := false  // Reset reenteredGap for each new gap
```

#### IF Bullish GAP  
```js
for i = 1 to 3
    // Check if price enters the bullish gap zone within 3 candles
    if close[i] > cHigh and close[i] < aLow
        reenteredGap := true
```
#### IF Bearish GAP  
```js
for i = 1 to 3
    // Check if price enters the bearish gap zone within 3 candles
    if close[i] < aHigh and close[i] > cLow
        reenteredGap := true
```

#### IF [ SHOW GAPS ], [RE-ENTER GAP] and BULLISH/BEARISH GAP  
```js  

if bullishGap
    // Bullish gap zone
    box.new(
        left=bar_index[2],
        top=cHigh, 
        right=bar_index[0], 
        bottom=aLow, 
        border_color=color.green, 
        bgcolor=color.new(color.green, 90), 
        border_width=1
    )

if bearishGap
    // Bearish gap zone
    box.new(
        left=bar_index[2], 
        top=aHigh, 
        right=bar_index[0], 
        bottom=cLow, 
        border_color=color.red, 
        bgcolor=color.new(color.red, 90), 
        border_width=1
    )  

```

#### IF [ HIGHLIGHT ENTRIES ]  
```js  

if bullishGap and close < aLow and close > cHigh
    label.new(
        bar_index, 
        close, 
        text="Entry", 
        style=label.style_label_down, 
        color=color.green, 
    )

if bearishGap and close > aHigh and close < cLow
    label.new(
        bar_index, 
        close, 
        text="Entry", 
        style=label.style_label_up, 
        color=color.red, 
        textcolor=color.white, 
        size=size.large
    )  

```

