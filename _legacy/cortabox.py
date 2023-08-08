//@version=5
indicator("cb.box", overlay = true)

// Default Values
string higherTimeFramePeriod = "1D"
float previousHigh = request.security(syminfo.tickerid, higherTimeFramePeriod, high[barstate.isconfirmed ? 0 : 1])
var chartIs60MinOrLess = timeframe.isseconds or (timeframe.isintraday and timeframe.multiplier <=60)

// Function returns `true` when the bar's time is
timeInRange(tf, session) =>
    time(tf, session) != 0

sessionColor = if chartIs60MinOrLess
    switch
        timeInRange(timeframe.period, "0400-0930") => color.rgb(76, 127, 181, 90)
        timeInRange(timeframe.period, "0930-1600") => color.rgb(76, 127, 181, 85)
        timeInRange(timeframe.period, "1600-2000") => color.rgb(76, 127, 181, 75)
        => color(na)

bgcolor(sessionColor)
plot(previousHigh, color=color.red)