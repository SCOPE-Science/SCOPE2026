#!/usr/bin/env python3
from fractions import Fraction as F

a=F(37,2)
b=F(19,2)
c=F(1)
d=F(1)
e=F(1)
f=F(2)
alpha=F(2)
beta=F(1)

H=d*e/(f-d)
P=((a-b*H)*(beta+H)*(e+H)-alpha*(e+H))/(c*(beta+H))

assert H == 1
assert P == 16
assert alpha < a*beta
assert alpha < (a-b*H)*(beta+H)
assert max(beta,H) < a/b < beta+H

host_exponent = a-b*H-alpha/(beta+H)-c*P/(e+H)
pred_exponent = f*H/(e+H)-d
assert host_exponent == 0
assert pred_exponent == 0

j11 = 1-b*H+alpha*H/(beta+H)**2+c*H*P/(e+H)**2
j12 = -c*H/(e+H)
j21 = e*f*P/(e+H)**2
j22 = F(1)

assert (j11,j12,j21,j22) == (F(-4),F(-1,2),F(8),F(1))

T = j11+j22
D = j11*j22-j12*j21
assert T == -3
assert D == 0

# Characteristic polynomial lambda^2 - T lambda + D = lambda(lambda+3).
assert (T,D) == (F(-3),F(0))

source_printed_source = (D > 1 and abs(T) < D+1) or (abs(T) > D+1)
source_printed_saddle = 0 < abs(T)+D+1 < 2*abs(T)
corrected_saddle = abs(T) > abs(D+1)
corrected_source = abs(D) > 1 and abs(T) < abs(D+1)

assert source_printed_source
assert source_printed_saddle
assert corrected_saddle
assert not corrected_source

eigs = [F(0),F(-3)]
assert abs(eigs[0]) < 1 < abs(eigs[1])

print("VERIFY_OK")
print("Hstar", H)
print("Pstar", P)
print("J", [[j11,j12],[j21,j22]])
print("T", T)
print("D", D)
print("multipliers", eigs)
print("source_printed_source", source_printed_source)
print("source_printed_saddle", source_printed_saddle)
print("corrected_saddle", corrected_saddle)
print("corrected_source", corrected_source)
