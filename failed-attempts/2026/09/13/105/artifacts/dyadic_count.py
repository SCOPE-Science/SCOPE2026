"""Dyadic scale accounting for AP_N: per-scale counts and Lovett-Meka thresholds.
Shows where log factors enter any size-only chaining.
"""
N=1024
import math
# Scales by length L=2^k. Count sets with length in [L,2L): for each d, #APs of length~L is ~ N (choices of a) but limited.
# Exact count: sum_d (N - (L-1)d)_+ approx.
def count_scale(N,L):
    c=0
    for d in range(1,N):
        v=N-(L-1)*d
        if v>0:
            c+=v  # approx # with length >=L; difference gives [L,2L)
    c2=0
    for d in range(1,N):
        v=N-(2*L-1)*d
        if v>0:
            c2+=v
    return c-c2

print(f"N={N}")
tot=0
for k in range(0,11):
    L=2**k
    if L>N: break
    m=count_scale(N,L)
    tot+=m
    # Lovett-Meka per-set threshold t ~ sqrt(L * log(m)) for sets of size ~L (restricted size <=L)
    # Actually generic: t_s = C sqrt(|S| log(m/|S|))? use simplified sqrt(L*log(m+2))
    t=(L*math.log(m+2))**0.5 if m>0 else 0
    print(f"L={L:4d} m_k={m:8d} sqrt(L*log m)={t:8.1f} N^1/4={N**0.25:.1f} ratio={t/N**0.25:.2f}")
print("total",tot)
# Uniform target C N^1/4
print()
print("Conclusion: for L~N (small-d scale), t~sqrt(N log N) >> N^1/4 by factor (N^1/4 sqrt(log N)).")
print("For L~sqrt(N), t~N^1/4 sqrt(log N): unavoidable sqrt(log) lift in size-only bound.")
print("Chaining across ~log N scales adds another sqrt/sum factor unless joint structure used.")
