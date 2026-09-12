# Verify Vinh threshold: for m=n=N, Vinh I <= N^2/p + sqrt(p) N implies I <= 2 N^{13/9} when N >= p^{9/8} and N <= p^{3/2}.
# Check exponents algebraically + numeric spot checks.
from fractions import Fraction
# exponent check: N^2/p <= N^{13/9} iff N^{5/9} <= p. Since N <= p^{3/2}: N^{5/9} <= p^{15/18}=p^{5/6} <= p. OK.
# p^{1/2}N <= N^{13/9} iff p^{1/2} <= N^{4/9} iff N >= p^{9/8}. OK by assumption.
import random, math
for p in [101, 1009, 10007]:
    for N in [int(p**1.125), int(p**1.3), int(p**1.5)]:
        vinh = N*N/p + math.sqrt(p)*N
        target = 2*N**(13/9)
        assert vinh <= target, (p,N,vinh,target)
        print(f"p={p} N={N}: Vinh={vinh:.3e} target13/9={target:.3e} OK")
print("Vinh reduction VERIFIED")
