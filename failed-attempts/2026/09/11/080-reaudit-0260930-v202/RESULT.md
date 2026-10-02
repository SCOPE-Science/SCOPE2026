# One-step real relative Caporaso–Harris recursion off the F2 (−2)-section: signed count 8 vs complex 12 for profile (2)_moving in class E+4F

## Context

The Hirzebruch surface F2 = P(O ⊕ O(2)) has its rigid (−2)-section E. Let B=E+2F be the disjoint section. Complex relative floor-diagram and degeneration methods on Hirzebruch surfaces are established. This record concerns one fixed real-signed profile. The open literature checked in the independent audit did not yield this exact fixed-profile ledger, but that non-detection is not used as a priority claim or as evidence for a general new recursion theorem.

## Definitions

Work in genus 0 with primary insertions. Fix β=E+4F=B+2F, so β·B=4 and β·E=2. Impose four fixed weight-1 contacts on B. On E, profile C is one moving contact of weight 2.

Use the stated floor-diagram conventions. Complex multiplicity is mult_C(D)=∏w(e) over compact edges in this census. Refined multiplicity is mult_q(D)=∏[w(e)]_q, where [m]_q=(q^{m/2}-q^{-m/2})/(q^{1/2}-q^{-1/2}). Its q=-1 specialization gives the edge factor

w* = 0 for even w, and w* = (-1)^((w-1)/2) for odd w.

## Result

For profile C there are exactly 10 labelled diagrams. Grouped by white position p∈{0,1} and compact-edge weight w∈{1,2}:

- (0,1): 4 diagrams, complex 4, signed 4;
- (0,2): 1 diagram, complex 2, signed 0;
- (1,1): 4 diagrams, complex 4, signed 4;
- (1,2): 1 diagram, complex 2, signed 0.

Therefore N_C^C=12 and N_C^R=8. The refined total is 2q^{-1/2}+8+2q^{1/2}=8+2[2]_q, giving 12 at q=1 and 8 at q=-1.

Supporting ledgers, not part of the theorem, are: fixed (2): 1/1/1; fixed (1,1): 1/1/1; moving (1,1): 180 diagrams, 288 complex, 104 signed; mixed (1 fixed + 1 moving): 22 diagrams, 30 complex, 14 signed. In the mixed ledger a weight-3 compact edge contributes +3 complex but -1 at q=-1, consistent with the corrected odd edge factor above.

## Proof / evidence

For profile C the relative dimension gives two vertices. With four left weight-1 ends and one moving right weight-2 end, the divergence equations give w=L0-2 when the white vertex is first and w=2-L1 when it is second, so w≤2. Thus the enumeration cap 8 cannot truncate this profile.

The archived `artifacts/ledger.json` reports `ndiag=10`, `complex=12`, `signed=8`, and refined coefficients `{-0.5:2, 0.0:8, 0.5:2}` for C. Since [1]_{-1}=1 and [2]_{-1}=0, the signed total is 4+0+4+0=8.

## Limitations

This is one fixed profile in class E+4F with B-side (1^4), genus 0 and primary insertions. It does not establish a general real Caporaso–Harris recursion, higher-genus or descendant theory, or a priority claim. The q=-1 interpretation is tied to the refined floor-diagram convention used here.

## Reproducibility

The archived `artifacts/enumerate_f2.py` and `artifacts/ledger.json` contain the five-profile census and the exact C totals.

## References

- R. Cavalieri, P. Johnson, H. Markwig, D. Ranganathan, Counting curves on Hirzebruch surfaces: tropical geometry and the Fock space, arXiv:1706.05401.
- P. Bousseau, Refined floor diagrams from higher genera and lambda classes, arXiv:1904.10311.
- I. Itenberg, V. Kharlamov, E. Shustin, Caporaso–Harris type formula for Welschinger invariants of real toric Del Pezzo surfaces, arXiv:math/0608549.
