"""Fallback success-criterion unsatisfiability certificate.
Fallback criterion (exact): explicit a_i (i<6), b_j (j<6), c_{k,l} (k,l<3) in
(Q,<,+,P) with phi1(x;y1):=(y1<x), phi2(x;y2):=P(x-y2) such that rows are
mutually indiscernible, EACH (k,l)-branch Gamma_{k,l} is consistent, and
off-branch conjunctions are inconsistent.

This script certifies the criterion is UNSATISFIABLE, using only the phi1 row:
Gamma_{k,l} contains phi1(x,a_k) and ¬phi1(x,a_{k'}) for k'!=k, i.e. requires
a_k < c <= a_{k'}. For fixed k!=k' (same l), branches (k,l),(k',l) jointly force
a_k < a_{k'} AND a_{k'} < a_k. Hence no a-vector works — over ALL weak order
types on the a's (exhausted here for the 3-branch core; the pairwise argument
covers any length >= 2, hence length 6).

Result: binary check on the logged L-array = FAIL (array does not exist).
This is a PROVED non-existence (obstruction), not a timeout.
"""
import itertools

def branch_feasible(a, k, n):
    """Gamma_{k} consistency requires a_k < c <= a_i for all i!=k (rationals)."""
    lo = a[k]
    hi = min(a[i] for i in range(n) if i != k)
    return lo < hi

unsat_count = 0
total = 0
# check all weak order types on 3 params (values 0,1,2 cover all comparisons)
for a in itertools.product([0, 1, 2], repeat=3):
    total += 1
    # fallback needs ALL THREE branches (k=0,1,2, same l) consistent
    feas = [branch_feasible(a, k, 3) for k in range(3)]
    if all(feas):
        print("SAT WITNESS (would revive fallback):", a)
    else:
        unsat_count += 1
print(f"order-types: {total}, types where >=1 branch infeasible: {unsat_count}")
assert unsat_count == total
print("FALLBACK_CRITERION_UNSAT: no a-vector admits all (k,l)-branches; exact fallback cannot be completed")
