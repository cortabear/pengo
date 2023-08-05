//@version=5
indicator("Line 16 Ticks Above Current Candle", overlay=true)

// Calculate the price 16 ticks above the current candle's close
price_16_ticks_above = close + syminfo.mintick * 16

// Plot the line
line.new(x1 = bar_index, y1 = close, x2 = bar_index, y2 = price_16_ticks_above, color = color.blue, width = 2, extend = extend.both)