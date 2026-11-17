---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For T adjacency of K_{a,b}, one-body energies are ±sqrt(ab),0 and only zero two-body energy admits bosonic collision-diagonal-free eigenvectors. In symmetric matrix blocks (P,M,Q), TX+XT=0 and vanishing diagonals require double-centering of M and constant opposite row sums in P,Q. Unsigned vertex-edge incidence kernels have rank m for m>=3 but rank 1 for m=2, and an orthogonal mixed phi adds one dimension; their projector adds exactly and yields the boxed dimension and diagonal capture laws. Every other eigenmode decays under arbitrary strictly positive losses. Independent exact rank and Krylov computations checked (a,b)=(2,2),(2,3),(2,4),(3,3),(3,4),(4,4), with e.g. K_{2,4} dark rank 6, AB loss 5/8, AA loss 2/5; finite tests only corroborate the proof.

## originality

PASS

The 2026-10-12 equal-speed distinguishable-walker theorem implies the bosonic capture laws and dimension for a,b>=3 through symmetric-state projection; these facts alone are NOT original. The new complete treatment of the sharp a=2 or b=2 rank exceptions, and a uniform explicit orthogonal projector through unsigned incidence kernels and one mixed rank-one vector, were not established by that theorem, which excludes 2-vertex parts. Searches of related bosonic multipartite and path results did not reveal an equivalent all-a,b >=2 classification. Best-of-knowledge originality only.

## value

PASS

The two-vertex side is a natural, singular boundary where the unsigned incidence rank changes and an extra protected boson mode appears, with a discontinuous capture formula. The all-size explicit projector and exception classification provide a precise invariant needed for collision-loss quantum transport. The previously implied >=3 capture and dimension formulas are credited; the sharp rank-2 exception and complete projector remain nontrivial and scientifically useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
