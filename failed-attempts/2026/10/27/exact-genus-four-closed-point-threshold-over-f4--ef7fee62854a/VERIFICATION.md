---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Aubry–Herbaut–Monaldi Proposition 2.2 gives the stated upper bound: 2*sqrt(2)<1+sqrt(8)<4 ensures the ceiling is 4. Independently, for r>=4 the proper-divisor contribution to N_r is at most the sum of N_d for 1<=d<=floor(r/2). Hasse–Weil gives N_d<=(21/4)*4^d for d>=1, so this sum is at most 7*2^r, and r*B_r>=4^r+1-15*2^r>0. For the example the pole of order 9 precludes an Artin–Schreier coboundary even over the algebraic closure. Infinity is totally ramified with a single rational point above it; its different exponent 10 gives genus 4. In F_4, x^9 is 0 or 1 and has absolute trace zero. In F_64, every x^9 lies in the subfield F_8 and likewise has trace zero because the subfield extension has degree 2. Omega has trace one in both fields, since the degree F_64/F_4 is odd. The affine equation is smooth and has no affine points in either field by the trace criterion for y^2+y, hence N_1=N_3=1 and B_3=(N_3-N_1)/3=0. This establishes the threshold exactly.

## originality

FAIL

A distinct indexed record gives the identical universal threshold, the identical explicit genus-four Artin–Schreier witness over F_4 and the same absence of degree-three points, and it determines additional closed-point counts and the zeta numerator. The later displayed catalogue date does not establish earlier public priority, duplication lineage, or the chronological order of discovery. This is a verdict of substantiated equivalent coverage in available results. The older DS table is exact at the candidate Weil-polynomial level but is not itself evidence of a previously exhibited equation.

## value

FAIL

A natural genus-four sharp threshold and explicit extremal witness would be valuable if the obstructing curve were not already known. The available exact result supplies both, with the same model and additional zeta data. Neither the finite confirmation of its traces nor the direct use of the published upper bound leaves a distinct exact fact or materially new argument to preserve as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
