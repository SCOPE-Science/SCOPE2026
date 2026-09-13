import numpy as np
# Formalize linearization check + derive Dyson polynomial reduced system symbolically with sympy
import sympy as sp
# Check Schur complement by hand algebra:
# L = [ [-z, s1, s1, s2],[s1,-1,0,0],[0,0,-1,s2? ...
# Use block: L = [[-z, u^T],[v, -I3]] with u^T=[s1,s1,s2], v=[s1,0,0? ...
# Our construction: M0+M1 s1+M2 s2 =
# row0: -z, s1, s1, s2
# row1: s1, -1, 0, 0
# row2: 0, 0, -1, 0
# row3: -s2, 0, 0, -1
# Schur S = -z - u^T(-I)^{-1} v = -z + u.v with u=(s1,s1,s2), v=(s1,0,-s2)
# u.v = s1^2 - s2^2. Missing s1 s2 term! Check: row2 col3? Add s1 in (2,3)?
# Indeed with L23 = s1: u stays [s1,s1,s2]? Let's recompute.
# General: D=-I3, Schur = -z - [row0'] D^{-1} [col0'] = -z + sum_j L0j*L j0.
# L01 L10 = s1^2. L02 L20 = s1*0=0. L03 L30 = s2*(-s2)=-s2^2.
# So Schur = -z + s1^2 - s2^2. The s1*s2 cross term is missing.
# To include s1 s2 need L02*L20 etc. with s-dependent D entries.
# Standard trick: put s1 in D block: e.g. D23 = s1? Then D^{-1} mixes.
# Let's solve: want Schur = -z + s1^2 - s2^2 + s1 s2.
# Take D = [[-1, s1, 0],[s1? ...]] hmm.
# Option: add auxiliary variable w = s2 - s1? Alternative: enlarge to 5x5 with explicit product.
# Simplest correct: 5x5 linearization with entries only linear:
# variables: y0=r-z(scalar eq), y1=s1, y2=s2, y3=s1*s2? Actually products linearized via new vars:
# eqs: y1=s1; y2=s2; y3 = s1*y2 (=s1 s2); y4 = s1*y1 - s2*y2 + y3 ... let's build linear system L [1, y1,y2,y3]^T = 0 style.
# Standard form: L = K0 \otimes 1 + K1 \otimes s1 + K2 \otimes s2 with L*[1;y]=[-r+z... wait.
# Let vector v=(1, a=s1, b=s2, c=s1 s2). Equations:
#  (i) -z*1 + s1*a - s2*b + c - r? Hmm r appears...
#  Better: L(z,r?) Actually linearization of polynomial P(s1,s2)-z with P=s1^2-s2^2+s1s2:
#  L = [[-z, s1, -s2, 1],[s1,-1,0,0],[s2,0,-1,0],[0,s1? ...]]
# Schur with D=-I2 for first two aux + coupling for c:
# Let L = [ [-z, s1, -s2, 1], [s1,-1,0,0], [s2,0,-1,0], [0, s2?...]]
# c should equal s1 b: equation c - s1 b = 0 -> row3: [0, 0, -s1, 1]? but -s1 nonlinear coefficient ok (linear in s1): L30=0,L31=0,L32=-s1? that's K1 entry, L33=1.
# Then Schur of full 4x4: eliminate a,b,c.
# a=s1, b=s2, c=s1 b=s1 s2. Row0: -z + s1 a - s2 b + c = -z+s1^2-s2^2+s1s2. 
# Matrix:
# L00=-z, L01=s1, L02=-s2, L03=1
# L10=s1, L11=-1, L12=0, L13=0
# L20=s2, L21=0, L22=-1, L23=0
# L30=0, L31=0, L32=-s1?? wait equation c - s1*b: L32 = -s1 (coeff of b), L33=1. But L32 multiplies b: yes -s1*b + c. Good.
# Check selfadjointness: L01=s1=L10 ok. L02=-s2, L20=s2: NOT selfadjoint (sign). Fix by scaling: use L02=s2, L20=s2 and row0 term -s2 b via... need L02=-s2 but selfadjoint requires L02=L20. Alternative: L02=s2, L20=s2, and flip sign in D? Use D22=+1? Then b=-s2? Let's redo with signs:
# Want row0 contribution -s2*b with symmetric L02=L20=s2? Then Schur term = -L02 D22^{-1} L20. With D22=-1: +s2^2. Wrong sign. With D22=+1: -s2^2. Good: set L22=+1? But then L22=+1 means equation ... b = -s2? Let's verify: row2: s2*1 + 1*b = 0 -> b=-s2. Then row0: L02*b = s2*(-s2)=-s2^2. 
# Similarly a: L01=L10=s1, L11=-1: a=s1, contrib +s1^2. Good.
# c-equation: c - s1 b = c - s1(-s2) = c + s1 s2. Row0 has +c so total = s1^2 - s2^2 + c = s1^2-s2^2+s1s2? c=s1 b=-s1 s2. Then +c = -s1s2. Wrong sign. Flip row0 L03=-1: then -c=+s1s2. Good.
# Final selfadjoint L:
# L00=-z; L01=L10=s1; L02=L20=s2; L03=L30=-1; L11=-1; L22=+1; L12=L21=0; L13=L31=0; L23=L32=0?; row3: c-s1 b: L31=0? L32=-s1 (coeff of b linear in s1), L33? c coeff 1? But selfadjoint needs L23=L32=-s1, but L23 multiplies c in row2: row2 becomes s2 + b - s1 c =0, corrupting b. So 4x4 selfadjoint insufficient; need 5x5 or non-selfadjoint.
# Standard remedy: use non-selfadjoint linearization then hermitize (double size). Our earlier M1,M2 pencil was WRONG (missed cross term) — must fix!
# Let's build correct (possibly non-selfadjoint) 4x4:
# L00=-z,L01=s1,L02=-s2,L03=1; L10=s1,L11=-1; L20=s2,L22=-1; L32=-s1,L33=1; rest 0.
# Check selfadjoint: L02=-s2 vs L20=+s2. Non-selfadjoint but that's fine: Hermitization doubles to 8x8 anyway.
# Verify Schur: a=s1,b=s2,c=s1 b. row0: -z+s1^2-s2^2+s1s2. Correct.
print("linearization analysis: earlier 4x4 pencil MISSED s1*s2 term (Schur = -z+s1^2-s2^2 only). Must redo with corrected 4x4 non-selfadjoint L above.")
print("Corrected L(z) = M0 + M1 s1 + M2 s2 with:")
print("M0 = diag(-z,-1,-1,1)? Let's decompose:")
print("L00=-z; L03=1,L30=0; L32=-s1; L02=-s2,L20=s2.")
print("M0: (0,0)=-z,(1,1)=-1,(2,2)=-1,(3,3)=1,(0,3)=1")
print("M1: (0,1),(1,0),(3,2)=-1")
print("M2: (0,2)=-1,(2,0)=1")
