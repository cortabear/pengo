//@version=5
indicator("cbx.sessions", overlay = true)

// Default Values
overNightPostMarket = "0000-0400"
preMarket = "0400-0930"
openMarket = "0930-1600"
postMarket = "1600-2000"
overNightPreMarket = "1800-2359"

timeInRange(tf, session) =>
    time(tf, session) != 0

sessionColor = if timeframe.isseconds or timeframe.isintraday
    switch
        timeInRange(timeframe.period, overNightPostMarket) => color.rgb(76, 127, 181, 95)
        timeInRange(timeframe.period, preMarket) => color.rgb(76, 127, 181, 90)
        timeInRange(timeframe.period, openMarket) => color.rgb(76, 127, 181, 85)
        timeInRange(timeframe.period, postMarket) => color.rgb(76, 127, 181, 75)
        timeInRange(timeframe.period, overNightPreMarket) => color.rgb(76, 127, 181, 95)
        => color(na)

bgcolor(sessionColor)