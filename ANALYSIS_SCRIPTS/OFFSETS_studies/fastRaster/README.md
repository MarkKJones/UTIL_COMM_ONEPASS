------------------------------------------------
   Leaf Variables Definitions on THcRaster.cxx
------------------------------------------------

H.raster.*
The four signals measured by the fADC are: XA, XB, YA, YB
In the examples below, only one is used.

Leaf Name                  hcana variable                                                                      Description
"frxaRawAdc":         FRXA_rawadc = pulseIntRaw                                          The fADC reads in (x,y) raster components in raw ADC units channels. 
"frxa_adc":           fXA_ADC =  FRXA_rawadc-fFrXA_ADC_zero_offset                       Offset corrected raw raster ADC 
"fr_xa":              fXA_pos = (fXA_ADC/fFrXA_ADCperCM)*(fFrCalMom/fgpbeam)             Raster converted from channels to cm. (The y component is multiplied by -1,)
""


"IPM3H07A.XRAW"       Raw beam pos. from BPMs                                            Read from EPICS                                         



Parameters (name in param file)
fFrXA_ADCperCM (gfrxa_adc_zero_offset) :  offset parameter value obtained from the gbeam.param. This parameter
                                          is determined by taking the average of the min/max "frxaRawAdc" leaf ADC channels      

fFrXA_ADCperCM (gfrxa_adcpercm)  : conversion factor of ADC Channels per cm, given raster size (Found in gbeam.param)
fFrCalMom (gfr_cal_mom)          : spectrometer momentum set on gbeam.param
fgpbeam (gpbeam)                 : Beam energy found in standard.kinematics

