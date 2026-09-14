"""Structural necessity check: why the target cannot be closed by pure theory here.

Formalizes the paper's own statement of the residual problem (BOSW 2023,
arXiv:2206.15188v2, p.2): 'To resolve Conjecture 1.3, we need to eliminate
the possibility of excluded minors with 14 or 15 elements. One strategy would
be ... reducing the bound of 15. Another strategy would be to narrow the space
for a computer search.'

Theorem 1.1 gives |E(M)| <= 15 for any excluded minor M (both 2- and
3-regular). The residual undecided sizes are therefore exactly {14, 15}:
  sizes 0..13: covered by the computer search in [2]/[5] (per p.2: search
    'uncovers all excluded minors for this class up to size 13');
  size >= 16: excluded by Theorem 1.1.
So the target is equivalent to: exhaustive H5-excluded-minor enumeration at
n in {14, 15} returns exactly the 33-conjecture members of those sizes and
nothing else.

This script checks the logical structure: residual = {14,15}, and records
that neither a bound improvement (needs new fragile-structure theorems) nor
an enumeration (needs H5 splice search at n=14,15) is available in-session.
"""
bound = 15
done_by_search = set(range(0, 14))   # sizes settled by search up to 13
residual = {n for n in range(0, bound + 1)} - done_by_search
print(f"bound: |E(M)| <= {bound}")
print(f"settled sizes: 0..13; residual sizes: {sorted(residual)}")
assert residual == {14, 15}, residual
strategies = ["reduce bound below 14 (new structure theory)", "H5 splice search at n=14,15"]
print("paper-sanctioned strategies:", strategies)
print("in-session availability: neither (see search_gap.py + WORKLOG)")
print("OK: residual structure confirmed")
