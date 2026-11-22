---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Read complete fixed-tree RESULT.md and actual check.py tree entry. Han-Henk-Xue Proposition 2.1 supplies primitive normal projections; direct support-function evaluation gives D(z)=b(M-m)/2+|b(M+m)/2-sum a_i z_i|. Every integer normal of range>=2 has D>=b whereas every nonempty subset indicator has D=max(a(S),b-a(S))<b. Thus all minimizers must have range exactly one, so are ± indicators, proving the exact formula over unbounded integer normals. The construction a_i=2w_i, a_last=2W+1, b=6W+2 is polynomial in binary input and target b/2 iff original PARTITION holds; dynamic programming is pseudo-polynomial. Equal-coordinate optimum and centroid parity follow from ka=b/2. Independently checked three rational small instances by exhaustive primitive vectors in [-2,2]^n; finite box was not used as proof.

## originality

PASS

Best-of-knowledge PASS for origin-translation dependence of the right-simplex first packing minimum and its exact lattice-normal rigidity and weak NP-completeness. Han-Henk-Xue 2026 Proposition 2.1 gives a general 1D lattice-projection identity and Theorem 1.3 calculates the centroid-centered simplex, but neither evaluates all positive barycentric translations nor establishes subset-sum hardness. The older difference-body minima are translation invariant. Resultary matching records did not show a broader translated-first-minimum solution.

## value

PASS

PASS: Origin-dependent packing minimum varies nontrivially even for a single simplex shape; its exact subset-discrepancy formula, full extremal directions and variable-dimensional weak NP-completeness exhibit a natural geometry/complexity connection with pseudo-polynomial solvability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
