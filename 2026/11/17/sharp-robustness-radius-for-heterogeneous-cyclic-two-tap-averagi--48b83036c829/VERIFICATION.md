---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For each nontrivial binary cut S with k members and r cyclic runs, homogeneous two-tap averaging has exactly 2 min(theta,1-theta) r^2 Gini deficit. Sitewise perturbations change only 2r boundary outputs. Convex maximization over the box reduces to signs, with perturbation contribution <=2 epsilon[r^2+(2k-n)d-d^2] <=2 epsilon r^2(n-2); the r=1 case and r>=2 use |2k-n|<=n-2r. Layer cake extends the cut estimate to arbitrary real f with the osc(f) factor. A singleton cut and opposite perturbations at two adjacent output rows make the defect exactly 2[mu-(n-2)epsilon], turning negative just above mu/(n-2). Direct rational exhaustive checks independently verified all cuts and parameter-cube vertices for n=4,5,6 and theta=1/4,1/2,3/4 at critical radius; these are finite validations of an algebraic all-n proof.

## originality

PASS

Existing homogeneous cyclic cut-deficit theorem is an essential special case but does not supply the exact independently heterogeneous coefficient cube radius and minimax oscillation defect. General Dobrushin/Hopf oscillation theory concerns a different seminorm and has no strict contraction for n>=4 here. Comparison at actual statements/implications favors a new robust stability boundary, qualified by broad Gini-inequality literature.

## value

PASS

The dimension-dependent sharp uncertainty threshold answers a natural stability question for spatially heterogeneous local averages, including the exact boundary and a two-coordinate adversarial witness. It is an independently useful perturbation theorem beyond the unperturbed contraction law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
