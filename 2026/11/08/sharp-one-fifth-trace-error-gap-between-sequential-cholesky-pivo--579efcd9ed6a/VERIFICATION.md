---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For real positive-definite 3x3 correlation A with w_ij=1-A_ij² and T_i=sum_{j!=i}w_ij, sequential RPCholesky picks first pivot uniformly and second proportionally to w_ij; 2-DPP unordered pair probability is w_ij/W. Schur complement says two-pivot residual trace det(A)/w_ij. Thus E_R=(2det(A)/3)sum 1/T_i and E_D=3det(A)/W. AM–HM gives ratio>=1 with equality precisely equal absolute correlations. Since sqrt(w_ij) is Frobenius distance between rank-one projectors divided by sqrt2, the triple satisfies triangle inequality. Ratio increases under shifting squared mass from smallest to largest side until a degenerate triangle; at a=b+c its exact factored gap to 6/5 is 2(t-1)^2(t+2)^2(2t+1)^2/[45(t²+1)(t²+2t+2)(2t²+2t+1)]. Strictness for positive-definite Gram triples and jittered nearly collinear unit vectors prove the supremum is 6/5 but unattained. Independent rational checks include equal-correlations and near-boundary ratios; finite tests are not substituted for proof.

## originality

PASS

PASS best-of-knowledge: Chen–Epperly–Tropp–Webber and DPP/Nyström literature supply residual-diagonal pivot law and determinant sampling, but the inspected earlier papers do not derive the exact 3x3 correlation-restricted two-pivot dominance, iff equality condition, and sharp 6/5 supremum. Resultary returned distinct rank-one-spike orientation and one-pivot comparisons but not a stronger theorem which implies this entire correlation class; it includes the identical current result. General approximation expectation bounds do not determine the sharp relative constant or equality.

## value

PASS

PASS: this is the smallest nontrivial (n=3, two selected pivots) exact comparison of adaptive versus determinantal kernel sampling on a natural normalized correlation matrix class. The sharp inequality, equality geometries, singular limiting factor 6/5, and counterexample outside equal diagonals locate a meaningful algorithmic boundary, useful independently of larger asymptotic guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
