
# highlightEntries  
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