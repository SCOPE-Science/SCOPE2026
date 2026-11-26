---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The four weighted PAV branches give a continuous piecewise-linear center coordinate. On each chamber the two off-center coefficients are bounded by A=a/(a+b) and C=c/(b+c). In edge-difference coordinates input edge j sends the signed packet (gamma_j,1-gamma_j-alpha_{j+1},alpha_{j+1}) to consecutive edges, giving its absolute sum as max(1,2(gamma_j+alpha_{j+1})-1). The uniform column bound and integration over the affine pieces yield the two-input bound; for a segment contained in faces one can also approximate by generic segments and use continuity. Since the quotient for cyclic differences is constrained by zero total sum, a single column does not prove sharpness. The two downward edges in the eight-site witness both have strict left/right pair activity in the relevant rows for small perturbations; the input jumps are +1 and -1 and the two maximal packets have disjoint supports. This reaches equality for every positive weight triple and n>=8, including b^2=ac. The upper bound on ordinary shorter cycles is not a claim of sharpness there. Independent exact-rational checks (256 local comparisons with the minimizing feasible partition, 400 upper-bound checks on lengths 3–7, 12 witness equalities at lengths 8, 9 and 12) used /workspace/branches/7236e76f-ada5-45b2-8eb6-ebd56ce641c4/verify_weighted_pav_independently.py; the supplied checker was inspected but not run.

## originality

PASS

The local projection formula and column-norm technique are standard; the covered contribution is the exact two-input constant and its finite realization for the particular overlapping-window operator. Best-of-knowledge assessment only.

## value

PASS

For a natural composition of overlapping shape-constrained fits, the result separates variation contraction of perturbations from exact amplification, and determines the optimal uniform gain including actual finite equality examples. Neither the familiar stability of global least-squares projections nor a one-signal TVD test answers that robustness question. The result is restricted to length-three windows, stationary positive weights and ordinary cycles of at least eight sites for sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
