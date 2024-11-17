# PENGO v.1.0.1 Indicator Documentation  

### Overview  
The **PENGO v.1.0.1** indicator is designed to detect price gaps between candles on a chart and visualize them as zones, aiding traders in identifying potential trading opportunities. The indicator allows users to highlight bullish and bearish gaps of a specified size and provides visual cues for potential entry points when the price re-enters these zones.  

### Features  
1. **Gap Detection:** Identifies gaps between candles that meet a user-defined minimum size (in ticks).  
2. **Zone Visualization:** Highlights the gap zones directly on the chart for better visual analysis.  
3. **Potential Entry Markers:** Marks possible entry points when the price re-enters the detected gap zones.  

---

### Inputs  
- **`Minimum Size (Ticks)` (`pengoSize`):**  
  - Defines the minimum size of the gap to detect, measured in ticks.  
  - Default: `2`  
  - Minimum value: `1`  

- **`Show Zones` (`showPengo`):**  
  - Toggles the visualization of gap zones on the chart.  
  - Default: `true`  

- **`Highlight Potential Entries` (`pengoEntries`):**  
  - Toggles the display of labels indicating potential entry points.  
  - Default: `true`  

---

### Logic  

#### **Gap Detection**  
The script evaluates three consecutive bars:  
- **A** (2 bars ago), **B** (1 bar ago), and **C** (current bar).  

Gaps are identified when:  
1. **Bullish Gap:** The low of bar A is higher than the high of bar C by at least the specified `Minimum Size (Ticks)`.  
2. **Bearish Gap:** The high of bar A is lower than the low of bar C by at least the specified `Minimum Size (Ticks)`.  

#### **Zone Visualization**  
- If a gap is detected and `Show Zones` is enabled, the script draws a rectangle (`box.new`) spanning the gap zone:  
  - **Bullish Gap Zone:** Rectangle from bar A's low to bar C's high.  
  - **Bearish Gap Zone:** Rectangle from bar A's high to bar C's low.  
- Colors and transparency are configurable in the script for better visual distinction.

#### **Entry Highlighting**  
- If `Highlight Potential Entries` is enabled, the script checks whether the current price (`close`) re-enters a detected gap zone.  
- Entry conditions:  
  - **Bullish Gap:** The `close` is between bar A's low and bar C's high.  
  - **Bearish Gap:** The `close` is between bar A's high and bar C's low.  
- If a condition is met, a label (`label.new`) is displayed:  
  - **Bullish Entry Marker:** Green label with a downward arrow.  
  - **Bearish Entry Marker:** Red label with an upward arrow.  

---

### Visualization  
1. **Gap Zones:**  
   - **Bullish Gaps:** Highlighted with a semi-transparent rectangle (default: white with 90% transparency).  
   - **Bearish Gaps:** Highlighted similarly, but differentiated by context.  

2. **Entry Labels:**  
   - Displayed above/below bars with color-coded markers to indicate bullish or bearish opportunities.

---

### Code Structure  

#### Variables  
- **Static Variables (`var`):** Persistent across executions for efficiency.  
  - `aHigh`, `aLow`, `bHigh`, `bLow`, `cHigh`, `cLow`: Hold the high/low values of the three bars being evaluated.  
  - Colors and border settings for zone visualization.  

#### Inputs  
Defined at the beginning of the script for user customization.  

#### Logic Implementation  
- **Bar Analysis:**  
  - Logic for comparing the high/low values of bars A, B, and C is implemented in a conditional block.  
- **Gap Detection:**  
  - Conditions for bullish and bearish gaps based on user-defined `Minimum Size (Ticks)`.  
- **Visualization and Labeling:**  
  - Separate logic for drawing zones and placing entry labels.  

---

### Use Cases  
- **Gap Analysis:** Detect price inefficiencies between candles for potential trade setups.  
- **Zone Trading:** Use visualized zones to plan trades or set alerts.  
- **Entry Confirmation:** Highlight price action re-entering the gap zones for additional trade validation.

---

### Notes  
1. **Performance:** The use of `var` ensures minimal computational overhead.  
2. **Compatibility:** Designed for use on charts with tick precision. Ensure the `Minimum Size` aligns with the tick size of the asset being analyzed.  
3. **Customization:** Developers can easily modify zone colors, transparency, and other visualization parameters.  

---

### Example Usage  
For a chart with a tick size of `0.01`, setting `Minimum Size (Ticks)` to `5` will detect gaps of `0.05` or greater. Enable `Show Zones` to visualize these gaps and `Highlight Potential Entries` to get entry markers.

This indicator is particularly effective for identifying gap trading opportunities in assets such as the **30-Year Treasury Bond Futures (ZB)**.  

---  
This documentation equips developers to implement, customize, and enhance the PENGO v.1.0.1 indicator for their trading strategies.