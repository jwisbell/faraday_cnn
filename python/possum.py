import numpy as np

class possum:
	"""
	Class for creating spectra
	"""

	def __init__(self):
		self.__c   = 2.99e+08 	# speed of light in m/s
		self.__mhz = 1.0e+06

	def _createPOSSUMspectrum(self):
		band1 = self._createFrequency(700.,1000.,nchan=300)
		band2 = self._createFrequency(1000.,1300.,nchan=300)
		band3 = self._createFrequency(1500.,1800.,nchan=300)
		self.nu = np.concatenate((band1,band2[1:],band3))


	def _createFrequency(self, numin=700., numax=1800., nchan=100.):
		"""
		Creates an array of evenly spaced frequencies
		numin and numax are in [MHz]

		To call:
			_createFrequency(numin, numax, nchan)

		Parameters:
			numin
			numax

		Postcondition:
		"""

		# ======================================
		#	Convert MHz to Hz
		# ======================================
		numax = numax * self.__mhz
		numin = numin * self.__mhz

		# ======================================
		#	Generate an evenly spaced grid
		#	of frequencies and store the array
		# ======================================
		return np.arange(nchan)*(numax-numin)/(nchan-1) + numin

		

	def _createNspec(self, flux, depth, chi):
		"""
		Function for generating N faraday spectra
		and merging

		To call:
			createNspec(flux, depth, chi)

		Parameters:
			flux 		[float, array]
			depth
			chi			[float, array]
		"""
		nu    = np.asmatrix(self.nu)
		flux  = np.asmatrix(flux).T
		chi   = np.asmatrix(chi).T
		depth = np.asmatrix(depth).T

		P = flux.T * np.exp(2*1j * (chi + depth * np.square(self.__c / nu)))
		P /= P.max()

		self.Polarization_ = np.ravel(P)
		
	def _addNoise(self, sigma):
		pass

flux = np.array([1, 0.5, 0.3])
depth = np.array([-10, 10, 3])
chi = np.array([0.0, 0.5, 0.2])


spec = possum()
spec._createPOSSUMspectrum()
spec._createNspec(flux, depth, chi)
