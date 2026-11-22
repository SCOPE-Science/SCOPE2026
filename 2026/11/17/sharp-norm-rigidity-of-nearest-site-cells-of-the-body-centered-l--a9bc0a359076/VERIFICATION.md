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

For every coordinate chamber x_i∈[0,1/2], the nearest representative in each coset is 0 or (1/2)1, reducing all p comparisons to sums of x_i^p versus (1/2-x_i)^p. Weighted Manhattan cost difference D1=Σw(2x_i−1/2) and weighted squared Euclidean difference D2=Σw(x_i−1/4) satisfy exact D1=2D2, so have identical sign and ties; reflecting chambers gives the stated weighted origin cell. IMPORTANT FOUND A NONFATAL ARITHMETIC TYPO IN SOURCE RESULT.md §Proof 2: it incorrectly displays D2=(1/2)Σwx_i−(1/8)Σw and claims D1=4D2; correct is D2=Σwx_i−(1/4)Σw and D1=2D2. This does not change conclusion, equality or proof method, but MUST be corrected before publication; no complete replacement file prepared in this run. For d=1,2 strict odd monotonicity of g_p(u) proves sign of sum coincides with linear comparison, including max norm. In d>=3, (t,t,−2t) has zero linear comparison but 2g_p(t)−g_p(2t) has nonzero cubic term except p=1,2; slight shift yields strict open mismatch. For infinity explicit (0.3,0.3,0.151) has Manhattan choose half and max choose integer; exact rational p=3 likewise. Independently checked weighted identity in dimensions 1,2,3,5,10 and strict rational witness. Finite tests corroborate all-dimension analytic argument.

## originality

PASS

Classical Euclidean BCC truncated-octahedral cell is prior. Deza–Dutour Sikirić arXiv:1401.0040 and Blömer–Kohn arXiv:1512.00720 primary PDF full mathematical material was actually inspected: broad general polyhedral/arbitrary-norm Voronoi algorithms, not an explicit labeled all-dimensional weighted l1/l2 equality and sharp all-p if-and-only-if classification. The 2026 regular-octahedron lattice covering result concerns optimal covering density, a different invariant. Resultary nearest-cell distribution and BCC covering profile records concern one metric rather than cross-norm site identity. Material unindexed worked examples still priority risk.

## value

PASS

Norm-robust nearest-site assignments across a natural infinite two-coset BCC/checkerboard lattice are a geometric property distinct from mere covering density; sharp dimension/exponent dichotomy and strict open disagreement show when changing metric changes nearest-site coding, including all common weights. General all-d classification and positive-volume counterexamples are motivated and not a tiny arbitrary computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
