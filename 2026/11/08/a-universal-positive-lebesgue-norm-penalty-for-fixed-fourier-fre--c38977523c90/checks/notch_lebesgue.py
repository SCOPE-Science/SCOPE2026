#!/usr/bin/env python3
"""Independent finite numerical sanity checks for punctured Dirichlet-kernel norms.

No enumeration here proves the asymptotic theorem; see the analytic proof.
"""
import math
import cmath

PI = math.pi
TARGET = 0.5 - 4.0 * math.log(2.0) / (PI * PI)

def midpoint_integral(fun, a, b, intervals):
    dx = (b-a)/intervals
    return dx * sum(fun(a + (i+0.5)*dx) for i in range(intervals))

def norm_gap(n, missing, multiplier=128):
    cells=multiplier*(2*n+1)
    def difference(t):
        numerator = math.sin((n+0.5)*t)
        den = math.sin(t/2.0)
        d = numerator / den
        h = sum(cmath.exp(1j*k*t) for k in missing)
        return abs(d-h)-abs(d)
    return midpoint_integral(difference, -PI, PI, cells)/(2*PI)

def angular_average_central(t):
    return (2.0/PI)*(t/2.0-math.tan(t/4.0))

def run():
    assert 0.21 < TARGET < 0.23
    average = midpoint_integral(angular_average_central, 0.0, PI, 20000)/PI
    assert abs(average-TARGET) < 1.0e-9, (average,TARGET)
    gaps=[]
    for n in (80,320,1280):
        gap=norm_gap(n,(0,))
        assert 0.0 < gap < TARGET
        assert abs(gap-TARGET) < 0.015
        gaps.append((n,gap))
    assert gaps[0][1] < gaps[1][1] < gaps[2][1]
    assert abs(gaps[-1][1]-TARGET) < 0.0005
    # A genuinely complex one-sided deletion: a finite test of an asserted general case.
    complex_gap=norm_gap(320,(1,))
    assert complex_gap > 0.0
    # Fourier synthesis identity for the kernel at a sample point.
    x=0.27182
    for n in (2,5,9):
        direct=math.sin((n+0.5)*x)/math.sin(x/2.0)
        fourier=sum(cmath.exp(1j*k*x) for k in range(-n,n+1))
        assert abs(fourier-direct)<1.e-12
    print('PUNCTURED_LEBESGUE_CHECK_PASS central_limit=%.12f n_tests=%d complex_gap=%.9f' % (TARGET,len(gaps),complex_gap))
    for n,v in gaps:
        print('n=%d central_norm_gap=%.12f abs_error=%.8f' % (n,v,abs(v-TARGET)))

if __name__ == '__main__':
    run()
