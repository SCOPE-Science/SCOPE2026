"""Reproducibility checks for radial periodic Gaussian localization spectra.

Uses only the Python standard library; numeric checks are illustrative rather
than substitutes for the analytic proof.
"""
import cmath
import math

COUNT = 0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def eigenvalue_by_cells(period, width, order):
    # Gamma(order+1,1) mass in the union of radial intervals.
    def survival(t):
        # Used at orders <= 12 to avoid subtraction of close near-unity CDFs.
        return math.exp(-t) * sum(t**j / math.factorial(j) for j in range(order+1))
    upper = max(60., order+55.)
    total = 0.
    for n in range(int(upper/period)+1):
        a=n*period
        total += survival(a)-survival(a+width)
    return total

def exact_top(period,width):
    return -math.expm1(-width)/(-math.expm1(-period))

def fourier_eigenvalue(period,width,order,harmonics=1500):
    answer=width/period
    for n in range(1,harmonics+1):
        z=2j*math.pi*n/period
        aperture=(cmath.exp(1j*math.pi*n*width/period)
                  *math.sin(math.pi*n*width/period)/(math.pi*n))
        answer+=2*(aperture*(1+z)**(-order-1)).real
    return answer

def main():
    for period in (0.5, 1., 2., 3.5):
        rho=1/math.sqrt(1+(2*math.pi/period)**2)
        for width in (0.12*period, 0.38*period, 0.67*period, 0.91*period):
            top=exact_top(period,width)
            uniform=width/period
            lb=math.exp(-period)/(-math.expm1(-period)) * (period*top-width)
            check(top>uniform, 'top exceeds essential spectrum')
            check(lb>0, 'positive gap lower bound')
            check(abs(eigenvalue_by_cells(period,width,0)-top)<1e-12,'top gamma integral')
            for k in range(1,12):
                direct=eigenvalue_by_cells(period,width,k)
                fourier=fourier_eigenvalue(period,width,k)
                check(abs(direct-fourier)<3e-10,'cell/Fourier agreement')
                check(top-direct>=lb-2e-11,'uniform positive spectral gap')
                check(direct<top,'unique top')
            for k in (5,7,10):
                theta=math.atan(2*math.pi/period)
                leading=(2/math.pi)*math.sin(math.pi*width/period) * rho**(k+1)*math.cos((k+1)*theta-math.pi*width/period)
                residual=fourier_eigenvalue(period,width,k)-width/period-leading
                rho2=1/math.sqrt(1+(4*math.pi/period)**2)
                # Easy explicit upper bound on the omitted higher harmonics.
                series=sum((1/(math.pi*n))*(1+(2*math.pi*n/period)**2)**(-(k+1)/2) for n in range(2,200))
                check(abs(residual)<=2*series+3e-14,'first harmonic with rigorous tail bound')
    print('PERIODIC_GAUSSIAN_COMB_CHECKS_PASS',COUNT)

if __name__=='__main__':
    main()
