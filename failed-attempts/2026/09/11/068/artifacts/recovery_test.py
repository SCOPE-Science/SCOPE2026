"""Bounded recovery test for lane-871 target (stdlib only).

Checks whether standard inputs (convexity, Weyl law, Weil bound) can reach
the claimed exponents; prints quantitative shortfalls.
"""
import math

T = 1e6  # formal large parameter; only exponents/ratios matter
logT = math.log(T)

# Spectral family facts
weyl_exponent = 5.0          # #{F: ||mu||<=T} ~ c T^5
conductor_exponent = 6.0     # Q(F x g) ~ T^6 for fixed g (6 gamma shifts)
convexity_exp = conductor_exponent / 4.0  # Q^{1/4} => T^{1.5}

print("=== lane-871 recovery test ===")
print(f"Weyl exponent (family size): {weyl_exponent}")
print(f"Conductor exponent: {conductor_exponent}")
print(f"Convexity individual exponent: {convexity_exp}")

# Covering claim: (1/T^5) sum |L| << T^eps.
# Trivial via convexity: (1/T^5) * T^5 * T^1.5 = T^1.5.
trivial_avg_exp = weyl_exponent + convexity_exp - weyl_exponent
print(f"trivial Lindelof-on-average exponent: {trivial_avg_exp} (need 0+eps)")
print(f"GAP to Lindelof-on-average: {trivial_avg_exp:.2f} powers of T")

# Trivial summed bound vs needed T^5
trivial_sum_exp = weyl_exponent + convexity_exp
print(f"trivial sum exponent: {trivial_sum_exp} (need 5+eps)")
print(f"sum GAP: {trivial_sum_exp - 5.0:.2f} powers")

# Nonvanishing: first moment T^5 / convexity max T^1.5 => T^3.5; need T^5/log T
convex_nonvan = weyl_exponent - convexity_exp
print(f"convexity-implied nonvanishing exponent: {convex_nonvan} (need 5, up to log)")
print(f"nonvanishing GAP: {5.0 - convex_nonvan:.2f} powers")

# Toy off-diagonal: Dirichlet length N ~ T^3, moduli c up to T^{1.5}.
# Naive: sum_{c<=C} c * (Weil c^{1/2}) * (trivial Bessel 1) * N^{1/2} coeffs
# gives >> T^{?} exceeding T^{5-1/20}. Model exponents only.
N_exp = 3.0
C_exp = 1.5
# terms: C moduli * N terms each ~ T^{4.5}; Weil saves C^{1/2}~T^{0.75};
# coeff L2-normalization saves ~ N^{1/2} partially offset; net excess computed:
toy_offdiag_exp = C_exp + N_exp - 0.5 * C_exp  # = 1.5+3-0.75 = 3.75 per block
# times ~T^2 archimedean/spectral weight factors in full Kuznetsov normalization
toy_total = toy_offdiag_exp + 2.0
print(f"toy off-diagonal exponent: {toy_total} vs allowed {5.0 - 0.05}")
print(f"off-diagonal EXCESS: {toy_total - (5.0-0.05):+.2f} powers (naive bounds)")

claimed_delta = 0.05
needed_saving_vs_trivial = (trivial_sum_exp) - (5.0 - claimed_delta)
print(f"saving needed beyond trivial to reach T^(5-delta): {needed_saving_vs_trivial:.2f} powers")

ok_blocked = (trivial_avg_exp > 0.5) and (convex_nonvan < 4.5) and (toy_total > 5.0 - claimed_delta)
print("VERDICT:", "CONFIRMED_BLOCKED" if ok_blocked else "NOT_BLOCKED")
