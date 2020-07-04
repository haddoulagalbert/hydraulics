
from math import log10, sqrt

'''
Cálculo do diâmetro de um tubo circular
Equações de Darcy-Weisbach e de Colebrook-White
'''

def calc_diameter(discharge, headLoss, roughness, viscosity=10**-6, precision=4, arbitrary_diameter = 1, g = 9.81):
	
	k = roughness
	v = viscosity
	Q = discharge
	J = headLoss
	p = precision
	
	_D = arbitrary_diameter
	
	dif = 1
	i=0
	
	while dif != 0:
		
		D = ( 0.7267 * Q**0.4 / (J*g)**0.2 ) * ( -log10(0.27 * k / _D + 1.7748 * v / sqrt( (J*g) * _D**3 ) ) )** -0.4
		dif = (round(D,p) - round(_D, p))
		
		print ('D'+str(i+1), ':', round(D, p), 'D'+str(i), ':', round(_D, p), 'Dif:', dif)
		
		_D = D
		i+=1
	
	return round(D, p)

'''
Cálculo da perda de carga unitária em um tubo circular
Equações de Darcy-Weisbach e de Colebrook-White
'''

def calc_headLoss(discharge, diameter, roughness, viscosity=10**-6, precision=3, arbitrary_headLoss = 1, g = 9.81):
	
	k = roughness
	v = viscosity
	Q = discharge
	D = diameter
	p = precision
	_J = arbitrary_headLoss
	
	dif = 1
	i=0
	
	while dif != 0:
		J = ( 0.2026 * Q**2 / (D**5 * g) ) * ( -log10( 0.27 * k / D + 1.7748 * v / sqrt( D**3 * g * _J)))**-2
		
		dif = (round(J,p) - round(_J, p))
		
		print ('J'+str(i+1), ':', round(J, p), 'J'+str(i), ':', round(_J, p), 'Dif:', dif)
		
		_J = J
		i+=1
	
	return round(J, p)

'''
Cálculo da vazão em um tubo circular
Equações de Darcy-Weisbach e de Colebrook-White
'''

def calc_discharge(headLoss, diameter, roughness, viscosity=10**-6, precision=3, g = 9.81):
	
	k = roughness
	v = viscosity
	J = headLoss
	D = diameter
	p = precision
	
	Q = -2.2214 * sqrt(J*g*D**3) * log10(0.27 * k/D + 1.7748 * v / sqrt(J*g*D**3))
	
	return round(Q,p)
	
