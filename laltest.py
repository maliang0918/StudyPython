import lal
import lalsimulation

psd = lal.CreateReal8FrequencySeries(None,lal.LIGOTimeGPS(0),0.0,df,lal.HertzUnit,N // 2 + 1)
