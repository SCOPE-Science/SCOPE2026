#!/usr/bin/env python3
"""Independent numerical diagnostics for the intrinsic distance and eccentricity formulas.
No finite mesh is used as proof of an all-point maximum.
"""
import math

def d2max_t(c, y, z):
    a=abs(y-z); b=abs(y+z)
    t=max(0.0,min(c,(c*c+b*b-a*a)/(2*c)))
    return max(min(a*a,c*c+b*b),min(c*c+a*a,b*b),min(t*t+a*a,(c-t)**2+b*b))

def predicted(c,h,y):
    a=c*c/(2*h)
    b=(h+math.sqrt(h*h+8*c*c))/8
    if h<=c or y<=a:
        return (c*c+h*h)/4+(1+h*h/(c*c))*y*y
    if y<=b:
        return c*c+(h/2-y)**2
    return c*c+(y-c*c/(4*y))**2

def radius(c,h):
    if h<=7*c/math.sqrt(15):
        return math.sqrt(c*c+h*h)/2
    return math.sqrt(c*c+(3*h-math.sqrt(h*h+8*c*c))**2/64)

if __name__=='__main__':
    count=0
    for c in (0.8,1.0,1.7):
        for ratio in (0.33,0.9,1.0,1.01,1.25,1.65,7/math.sqrt(15),2.2,3.5,9.0):
            h=c*ratio
            for j in range(41):
                y=h*j/80
                exact=predicted(c,h,y)
                brute=max(d2max_t(c,y,h*k/2000) for k in range(1001))
                assert brute<=exact+1e-9, (c,h,y,exact,brute)
                assert exact-brute<.004*h*h, (c,h,y,exact,brute)
                count+=1
            vals=[predicted(c,h,h*j/2000) for j in range(1001)]
            assert abs(math.sqrt(min(vals))-radius(c,h))<.002*c+.0005*h
            diameter=(c*c+h*h)/(2*max(c,h))
            assert abs(math.sqrt(max(vals))-diameter)<.004*c+.001*h
    print('PASS',count,'pointwise grid cases and 30 center/diameter profiles')
