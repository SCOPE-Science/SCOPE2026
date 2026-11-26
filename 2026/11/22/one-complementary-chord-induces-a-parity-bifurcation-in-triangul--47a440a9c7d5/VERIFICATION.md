---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Over characteristic two, A₀=HᵀH and HHᵀ=(n mod 2)I+J give the unedited identity A₀²=(n mod 2)A₀. Keeping the two chord coordinates u,v prescribed still permits every incidence vector t with coordinate sum zero: the other edge columns are the incidence columns of a connected graph. The perturbed image is Hᵀt+ve+uf, and a nonzero cut vector cannot be supported on just the two chord coordinates (a nontrivial label class forces at least n−1 nonzero coordinates). Constants are in the incidence hyperplane exactly for even n; the respective ranks follow. In the odd case the reduced update has fourth power identity. Fixing one iterate requires u=v=0 and both chord incidence forms a=b=0; fixing two requires a=b and u+v=a. The two forms are independent when there is a fifth ground point. This gives dimensions n−3,n−1,n+1 at iterates 1,2,4, hence the stated orbit counts by subtraction. In the even case the span of A₀e+f and A₀f+e is the third image and the map swaps those independent vectors; it is thus exactly the recurrent subspace. The second image has rank four from the two independent cuts and free input forms at n≥6, but rank two at n=4 because the cuts agree and a=b. These ranks determine all entrance times by counting the inverse image of the recurrent subspace. At the settling time, every recurrent state has q^(N−r) preimages, proving each basin formula. The odd settling bound is sharp since N>n+1, and the even bounds are sharp by the last rank drop. Fresh reconstruction of power ranks, fixed-space dimensions, and polynomial identities for n=4,…,12 using dense adjacency matrices and elimination over F₂ agrees with the theorem; rank identities extend to F_(2^f), and the proof independently treats the whole field family. Replay cd /workspace && python3 review-evidence/reproduce.py 2; output review-evidence/2.txt. Frozen checks were inspected, not executed: the binary enumeration checks individual basins; the F₄ loop actually asserts only entry-layer totals, not separate per-orbit basin assertions.

## originality

PASS

The supported distinct part is the rank, recurrence and entry-filtration classification for a nonadjacent-pair addition in T(n) over characteristic two, including the n=4 exception. Neither the unedited Johnson results nor the previously adjacent-pair deletion covers this perturbation.

## value

PASS

A single missing-line-graph-edge insertion creates qualitatively different periods in the two natural parity classes, and a sharp transient hierarchy with one small-order exception. The exact global basins quantify the response to the edit. This is a motivated, all-order sensitivity classification, rather than merely the routine Fitting argument or an isolated rank calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
