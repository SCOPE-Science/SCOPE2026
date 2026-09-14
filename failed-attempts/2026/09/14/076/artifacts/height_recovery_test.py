"""Recovery test: why the standard height machinery cannot force the linear bound.

Let N = max(|p1|,|q1|,|p2|,|q2|), t = trace of a core curve, a = t-2 (algebraic
integer, nonzero for hyperbolic filling). Neumann-Zagier at the GEOMETRIC
embedding: |a|_geom ~ C/N^2. Norm(a) in Z \\ {0}, so |Norm| >= 1, hence some
Galois conjugate satisfies log|a|_sigma >= 2 log N - C'. Therefore the absolute
logarithmic Weil height satisfies the LOWER bound h(a) >= (2 log N - C')/d
where d = [Q(a):Q] <= const * [K:Q].

Dobrowolski's unconditional theorem is ALSO a lower bound:
h(a) >= D(d) = (1/4)(log log d / log d)^3 / d.

Two lower bounds on the same quantity can never exclude any degree: for every
fixed N and every d, both inequalities are simultaneously satisfiable (take
h = max of the two right-hand sides). We verify this formally below, and
contrast with the fantasy scenario: if one GRANTED a global UPPER bound
h(a) <= C log N / N^2 (controlling ALL conjugates, i.e. all non-geometric
points of the Dehn-filling variety -- exactly what Neumann-Zagier does NOT
give), Dobrowolski would force d >= ~N^2/polylog, proving the target. The
missing upper bound is the precise blocker.
"""
import math

def D(d):
    l = math.log(d)
    ll = math.log(l)
    return 0.25 * (ll / l) ** 3 / d if ll > 0 else float("inf")

print("Part 1: lower+lower never excludes any degree.")
print("For each (N, d): LB_norm = (2logN-C)/d, LB_dob = D(d);")
print("joint satisfiability is automatic since h may be taken large.")
ok = True
for N in [100, 1000, 10**6]:
    for d in [2, 10, 1000, 10**6]:
        lb1 = (2 * math.log(N) - 1.0) / d
        lb2 = D(d)
        feasible_h = max(lb1, lb2, 1e-12)
        # An upper bound would need feasible_h <= UB; with no UB, always satisfiable.
        assert feasible_h >= lb1 and feasible_h >= lb2
print("  -> confirmed: no degree d is excluded for any N. Height-norm route gives nothing.")

print("\nPart 2: fantasy upper bound WOULD suffice (hence it is the exact missing input).")
for N in [100, 1000, 5000]:
    UB = math.log(N) / N ** 2  # granted, not available
    # degrees excluded = {d : D(d) > UB}; find smallest surviving d
    d = 4
    while D(d) > UB:
        d += 1
    print(f"  N={N:>5d}  granted UB={UB:.2e}  Dobrowolski forces d >= {d} "
          f"(target needs d >= N/c = {N}/c)")
print("  -> with a global height upper bound there would be slack to spare;")
print("     without it (reality: non-geometric conjugates uncontrolled) nothing is forced.")
