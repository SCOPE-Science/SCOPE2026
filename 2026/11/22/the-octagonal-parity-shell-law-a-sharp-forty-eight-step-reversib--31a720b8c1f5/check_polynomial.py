#!/usr/bin/env python3
"""Independent polynomial-ring check of the wave clock and fixed-space exponents.
Ring = F2[X]/(X^9+X^7); multiplication matrix uses no shell graph data.
"""
P = (1 << 9) | (1 << 7)
DEG = 9

def rem(a):
    while a.bit_length() > DEG:
        a ^= P << (a.bit_length()-DEG-1)
    return a

def mul(a,b):
    v=0
    while b:
        if b&1:v ^= a
        a <<=1;b>>=1
    return rem(v)

# Fibonacci/Chebyshev recurrence for a second-order reversible wave.
u=[0,1]
for t in range(2,49+2):u.append(mul(2,u[-1]) ^ u[-2])
# T^t = [[u[t+1],u[t]],[u[t],u[t-1]]]
assert (u[49],u[48],u[47]) == (1,0,1)
assert (u[25],u[24],u[23]) != (1,0,1)
assert (u[17],u[16],u[15]) != (1,0,1)

# Instead of similarity/Jordan theory, build the two-level polynomial module
# directly and eliminate column vectors of (T^t-I) over F2.
def rank(columns):
    pivots={}
    for c in columns:
        while c:
            i=c.bit_length()-1
            if i in pivots:c ^= pivots[i]
            else:pivots[i]=c;break
    return len(pivots)

def ker_wave(t):
    x,y,z=u[t+1]^1,u[t],u[t-1]^1
    col=[]
    for i in range(DEG):
        col.append(mul(x,1<<i) | (mul(y,1<<i)<<DEG))
    for i in range(DEG):
        col.append(mul(y,1<<i) | (mul(z,1<<i)<<DEG))
    return 18-rank(col)

def ker_poly(polypower):
    return DEG-rank([mul(polypower,1<<i) for i in range(DEG)])

def pow_ring(a,k):
    v=1
    while k:
        if k&1:v=mul(v,a)
        a=mul(a,a);k>>=1
    return v

for t in [1,2,3,4,6,8,12,16,24,48]:
    a=t;n=0
    while a%2==0:n+=1;a//=2
    result0=ker_poly(2) if n==0 else 2*ker_poly(pow_ring(2,1<<(n-1)))
    result1=2*ker_poly(pow_ring(3,1<<n)) if t%3==0 else 0
    assert ker_wave(t)==result0+result1,(t,ker_wave(t),result0+result1)
print('Characteristic-two quotient polynomial:',bin(P))
print('Exact wave order:',48)
print('Kernel dimensions at divisors:', {t:ker_wave(t) for t in [1,2,3,4,6,8,12,16,24,48]})
print('PASS')
