# OVERNIGHT HIGH AND LOW
# The ability to display an indication on the overnight session's highest price as well as the session's lowest price.
# 1800-2359 == '..yesterday at 6:00PM to 11:59PM
# 0000-0400 == '..today at 12:00AM to 4:00AM

// @version=5
indicator("cbx.overnight.high", overlay=true)

// Default Values
overNightPreMarket = time(timeframe.period, "1800-2359")
overNightPostMarket = time(timeframe.period, "0000-0400")

bgcolor(overNightPreMarket ? color.new(color.blue, 90) : na)
bgcolor(overNightPostMarket ? color.new(color.blue, 90) : na)

string higherTimeFramePeriod = "1D"
float previousHigh = request.security(syminfo.tickerid, higherTimeFramePeriod, high[barstate.isconfirmed ? 0 : 1])




plot(previousHigh, color=color.red)