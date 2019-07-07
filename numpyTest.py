numpy.random.normal(loc=0.0,scale=1.0,size=10);
#loc is the mean value
#scale is the standard deviation
#size is the data shape


numpy.fft.irfft(re+1j*im)
#The input is expected to be in the form returned by rfft, 
#i.e. the real zero-frequency term followed by the complex positive frequency terms in order of increasing frequency. 
#Since the discrete Fourier Transform of real input is Hermitian-symmetric, 
#the negative frequency terms are taken to be the complex conjugates of the corresponding positive frequency terms.
