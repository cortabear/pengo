# Corta.Box  

## Documentation  
1. Parameters for Customization  
    1. [gapSizeTicks](assets/documentation/gap.size.ticks.md)  
    1. [showGaps](assets/documentation/show.gaps.md)  
    1. [gapSizeTicks](assets/documentation/highlight.entries.md)  



Configure your box to store trade log in your Google drive.  


## Parameters for Customization  
  

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

