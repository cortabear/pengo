# showGaps   
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

