"""Determine exact Kuo-type recurrence by fitting S_n monomials, then verify corner-weight story.
R table (n>=2): R_0=1+a^2, R_1=2a^2, R_2=(1+a^2)/a^2, R_3=2a^2.
Check: does R_n factor as (corner weight products)? For Kuo condensation on Aztec_n:
  Z_n * Z_{n-2}^{corners-removed} = ... Standard Kuo for Aztec (uniform): Z_n Z_{n-2} = 2 Z_{n-1}^2.
General weights (Kuo 2004, or Ciucu): the factor 2 = sum of two complementary corner matchings = ac+bd (urban renewal cell factor).
For two-periodic: the four corner 2x2 blocks cycle through the 4 phases of the weight pattern as n grows.
The urban-renewal cell factor is Delta = ac+bd where a,b,c,d are the 4 edge weights around the face.
In CJ convention each face has edges of weights: two a's? Let's compute: face centers (2i+1,2j+1)... 
Actually rather than reverse-engineer corners, PROVE recurrence via urban renewal counting:
  One shuffle step: Z_n(a,b) = (factor)^n * Z_{n-1}(a',b')? For uniform: Z_n = 2^n Z_{n-1} (factor 2^n: n^2 cells each giving factor 2, divided by gauge 2^{n(n-1)}: 2^{n^2}/2^{n(n-1)} = 2^n ✓).
For two-periodic with 4-periodic shuffle orbit, four consecutive steps give:
  Z_n = c_n Z_{n-1}, Z_{n-1} = c_{n-1} Z_{n-2}, ... with c_n 4-periodic → S_n = c_n/c_{n-1} 4-periodic.
Let's extract c_n = Z_n/Z_{n-1} from data and identify monomials.
"""
import math
from kasteleyn import logZ
for a in [0.3, 0.7]:
    print(f"--- a={a} ---")
    lz={n:logZ(n,a) for n in range(0,13)}; lz[0]=0.0
    for n in range(1,13):
        c=math.exp(lz[n]-lz[n-1])
        print(f"  n={n} (mod4={n%4}): Z_n/Z_{{n-1}} = {c:.10f}")
