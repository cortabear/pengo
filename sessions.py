//@version=5
indicator("cbx.sessions", overlay = true)

// Function returns `true` when the bar's time is
timeInRange(tf, session) =>
    time(tf, session) != 0
    
var chartIs60MinOrLess = timeframe.isseconds or (timeframe.isintraday and timeframe.multiplier <=60)

sessionColor = if chartIs60MinOrLess
    switch
        timeInRange(timeframe.period, "0400-0930") => color.rgb(76, 127, 181, 95)
        timeInRange(timeframe.period, "0930-1600") => color.rgb(76, 127, 181, 85)
        timeInRange(timeframe.period, "1600-2000") => color.rgb(76, 127, 181, 75)
        => color(na)

bgcolor(sessionColor)