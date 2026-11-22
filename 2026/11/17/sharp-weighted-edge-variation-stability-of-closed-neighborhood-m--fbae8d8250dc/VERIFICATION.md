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

Translation equivariance reduces weighted star-edge variation to a weighted l1 seminorm on k leaf-to-hub differences. The filter outputs center median(0,x_1,...,x_k) and leaf values (x_i)/2 relative to the hub, so quotient map is F_i=x_i/2-median(0,x_1,...,x_k). On each strict order chamber, median gradient is a leaf selector, half of two leaf selectors, or zero; weighted induced l1 column sums give k=1 zero, k even W/w_min−1/2, and k odd (W−w_min)/(2w_min). Continuous piecewise linearity yields the same global pair bound along every segment, and minimum-weight leaf strict-order perturbations attain the column extremum. This establishes equal-weight and nonexpansivity classifications, including k=3 and k=1. A new exact rational implementation independently enumerated 2616 order chambers under three weight profiles per k<=5 and checked true attaining input pairs; this is finite corroboration only.

## originality

PASS

Classical median smoothing theorems and Little–Jones 2011 address the variation of one filtered signal along a path, not a two-input difference on a branching star. Resultary full published finite-path two-input theorem and finite-tree majority filter theorem have different graph, endpoint/tie convention and objective and do not imply the weighted closed-neighborhood star coefficient. No matching formula with odd/even number of leaves and w_min was found. The 1994 Restrepo–Chacon manuscript remains a specific residual-access priority risk: author-uploaded full-text entry did not permit content retrieval, and authorized institutional access reported VPN disconnected. It alone does not defeat best-of-knowledge originality.

## value

PASS

A natural branching graph median smoothener has a fully classified sharp perturbation stability modulus for every leaf count and every positive variation-weight profile. The striking parity jump and unique three-leaf nonexpansive exception explain why one-input smoothing fails to imply robustness to data perturbations. Exact attaining pairs and the minimum-weight dependence make the formula operationally meaningful, well beyond a tiny isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
