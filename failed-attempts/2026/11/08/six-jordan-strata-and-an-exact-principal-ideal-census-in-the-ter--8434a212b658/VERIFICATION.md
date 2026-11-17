---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Frobenius gives f³=0 in A=k[x,y]/(x³,y³). If f has nonzero linear part, local automorphism yields three Jordan 3-blocks. At quadratic leading order the degree-one-to-three map has determinant b²−ac, giving rank four or three, and f²=(b²−ac)x²y². Higher layers have ranks two, one, zero. Counting the nonzero discriminant cone over F_q gives every polynomial. Since each nonzero r-dimensional principal ideal has (q−1)q^{r−1} generators, the asserted principal-ideal counts follow. Independent q=3 rank census arithmetic gives 1,2,24,216,486,5832 by ranks and ideal counts 1,1,4,12,9,12 (39 proper; 40 total).

## originality

FAIL

Two earlier exact published theorems already supply every nontrivial Jordan rank/type multiplicity and the six smooth geometric strata for precisely k[C3×C3] in characteristic 3. Principal ideal counts are then forced by dividing each known rank multiplicity by the standard local Nakayama generator count, so the displayed total is a mechanical corollary.

## value

FAIL

A principal-ideal count is a natural ring invariant, but here the only nominally extra quantity is deterministically obtained by dividing an already published complete rank-fiber table by an elementary Nakayama unit-orbit factor. Repackaging the earlier Jordan and geometric census is not a separate substantive unknown exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
