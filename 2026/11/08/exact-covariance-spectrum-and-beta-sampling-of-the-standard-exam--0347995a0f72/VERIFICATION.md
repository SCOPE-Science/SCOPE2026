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

For the standard-example order polytope n>=2, conditioning on the largest two lower coordinates produces V~Beta(n-1,n+2), U=V+(1-V)Z with Z~Beta(1,n), correct n(n-1) pair normalization, and independent interval-uniform remaining coordinates. Integrating beta-polynomial factors yields all multivariate monomial moments. Simultaneous permutation and level-complement symmetry reduce covariance to S,C,M,N; recomputing all four eigenmode rational functions symbolically from those entries reproduces stated lambda_0±, lambda_1± and the strictly positive difference N-M=(n²+4n+8)/(8n(n+1)²(2n+1)). At n=2 the two independent chains explain zero off-diagonal cross-chain covariances. Determinant and factorial volume asymptotics imply L²→1/12; independent local symbolic checks for n=2..7 corroborate but do not prove the general disintegration. The source checker.py is an n=2,3,4 triangulation test, not a proof for arbitrary n.

## originality

PASS

Exact-object prior linear-extension count determines volume, but not the full conditional beta sampler, evaluated covariance spectrum or unmatched-minus-matched covariance gap. Resultary comparison covers rooted-forest and complete two-level posets only; neither contains the standard-example missing-matching relations for n≥4. No directly dominating evaluated continuous-volume moment spectrum was located. Best-of-knowledge PASS with substantial residual risk of older threshold-digraph conditional moment formulas.

## value

PASS

The standard example is a canonical extremal poset-dimension family. A uniform-volume exact sampler for all degrees and a complete evaluated covariance spectrum with a universal strict matched/unmatched gap and isotropic limit are natural analytic invariants; the known volume formula alone does not supply these. Not an arbitrary numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
