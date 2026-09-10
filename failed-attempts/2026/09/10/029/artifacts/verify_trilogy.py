"""Verification of the sparse-large-entry trilogy at critical truncation T*=N^{34/81}.

Pure-probability statements about i.i.d. standardized symmetric Pareto-4.5
variables (x_m=sqrt(5)/3, c0=x_m^4.5). Asserts exact constants and N0 values:
  T1: P(#bad > 3 N^{1/9}) <= N^{-1}, N>=2          (Chernoff, exact MGF)
  T2: P((1/N^2) sum x_i^2 1_bad > N^{-5/9}) <= N^{-1}, N>=22   (3rd moment)
  T3: P((1/N^{3/2}) sum |x_i| 1_bad > N^{-5/9}) <= N^{-1}, N>=4 (3rd moment)
plus the m=2 near-miss for T2 (exponent -80/81 vs needed -1).
"""
import math
import sys

XM = math.sqrt(5.0) / 3.0
C0 = XM ** 4.5
TAU_STAR = 34.0 / 81.0
W = -5.0 / 9.0  # window exponent

print(f"c0 = {C0:.12f}")
assert abs(C0 - 0.266462969559) < 1e-9

# ---- tail-integral constants: E[|x|^k 1_{|x|>T}] = Ck * T^{k-4.5}, Ck = 4.5*c0/|k-4.5|
def Ck(k):
    return 4.5 * C0 / abs(k - 4.5)

C_EY, C_EY2, C_EY3 = Ck(2), Ck(4), Ck(6)   # 1.8c0, 9c0, 3c0
C_EZ, C_EZ3 = Ck(1), Ck(3)                  # (9/7)c0, 3c0
print(f"E[Y]={C_EY:.8f}T^-2.5 E[Y^2]={C_EY2:.8f}T^-0.5 E[Y^3]={C_EY3:.8f}T^+1.5")
print(f"E[Z]={C_EZ:.8f}T^-3.5 E[Z^3]={C_EZ3:.8f}T^-1.5")
assert abs(C_EY - 1.8 * C0) < 1e-12 and abs(C_EY2 - 9 * C0) < 1e-12
assert abs(C_EY3 - 3 * C0) < 1e-12 and abs(C_EZ - (9.0 / 7.0) * C0) < 1e-12

# ---- T1: Chernoff. mu = c0 N^{1/9}; threshold 3 N^{1/9}; 1+delta = 3/c0
one_plus_delta = 3.0 / C0
rate = one_plus_delta * math.log(one_plus_delta) - (one_plus_delta - 1.0)
K1 = rate * C0  # P <= exp(-K1 N^{1/9})
print(f"T1: 1+delta={one_plus_delta:.6f} K1={K1:.6f}")
assert abs(K1 - 4.5291) < 1e-3
# need K1*y - 9*ln(y) >= 0 for y=N^{1/9}>=2^{1/9}; min of g at y=9/K1
y_min = 9.0 / K1
g_min = K1 * y_min - 9.0 * math.log(y_min)
print(f"T1: min margin {g_min:.6f} at y={y_min:.4f} (need >0)")
assert y_min >= 2.0 ** (1.0 / 9.0) and g_min > 2.5
# spot-check the final inequality K1*N^{1/9} >= ln(N) for a grid incl. N=2
for N in [2, 3, 4, 5, 10, 100, 10**6, 10**18]:
    assert K1 * N ** (1.0 / 9.0) >= math.log(N), N
print("T1_OK: P(#bad > 3N^{1/9}) <= N^{-1} for all N>=2")

# ---- T2: E[(sum Y)^3] <= A2 N^{231/81}; threshold^3 = N^{351/81}
A2 = C_EY3 + 3 * C_EY2 * C_EY + C_EY ** 3
print(f"T2: A2={A2:.6f} (need N^{{39/81}} >= A2)")
N0_T2 = 22
assert N0_T2 ** (39.0 / 81.0) >= A2 and (N0_T2 - 1) ** (39.0 / 81.0) < A2
print(f"T2_OK: N0=22 sharp for this majorant; P <= {A2:.4f} N^(-120/81) <= N^-1")
# m=2 near-miss: E[(sumY)^2] <= B2 N^{154/81} vs threshold^2=N^{234/81} -> N^{-80/81}
B2 = C_EY2 + C_EY ** 2
gap_exp = (154.0 - 234.0) / 81.0
print(f"T2 m=2: ratio <= {B2:.5f} N^({gap_exp:.5f}); needed N^-1: MISSES by N^{1/81}")
assert abs(gap_exp - (-80.0 / 81.0)) < 1e-12 and B2 < 2.63

# ---- T3: E[(sum Z)^3] <= A3 N^{129/81}; threshold^3 = (N^{17/18})^3 = N^{229.5/81}
A3 = C_EZ3 + 3 * C_EY * C_EZ + C_EZ ** 3
print(f"T3: A3={A3:.6f} (need N^{{19.5/81}} >= A3)")
N0_T3 = 4
assert N0_T3 ** (19.5 / 81.0) >= A3 and (N0_T3 - 1) ** (19.5 / 81.0) < A3
print(f"T3_OK: N0=4 sharp for this majorant; P <= {A3:.4f} N^(-100.5/81) <= N^-1")

# ---- criticality: count binds (34/81 > 24.4/81 > 18/81)
tau_count = (2.0 - 1.0 / 9.0) / 4.5
tau_quad = (5.0 / 9.0) / 2.5
tau_first = (0.5 + 5.0 / 9.0) / 3.5
print(f"tau_count={tau_count:.6f}=34/81 tau_quad={tau_quad:.6f} tau_first={tau_first:.6f}")
assert abs(tau_count - 34.0 / 81.0) < 1e-12
assert tau_count > tau_first > tau_quad

print("TRILOGY_OK")
sys.exit(0)
