---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: W selects one special Q basis index (j(n),n) with j(n)=ceil log2 n for each v_n and bijects the nonspecial indices to u_m; the weights squared produce n2^-j*(1/n)=2^-j or 2^-j*1. V writes n=2^j(2k-1), maps all u_m to odd row-zero coordinates, odd v_n to even row-zero, and v_n at j>=1 to (j,k); the squared weights produce P exactly. All weights are positive <=1, so both maps are contractive, injective and have dense range. P is a compact perturbation of the infinite projection onto the u-sector, whose invertible congruences have a uniform positive Calkin spectral gap; Q has essential positive spectrum 2^-j accumulating at zero, contradicting two-sided invertible comparability. Independent exact basis-index and rational-weight checks passed over >8000 indices. The proof, not finite tests, establishes density and spectral obstruction.

## originality

PASS

PASS (qualified): the paper naming this very pair and posing its dense-range status as a question was located. No earlier source found supplies these two explicit inverse-direction diagonal-permutation pullbacks. General Douglas factorization and operator-range results are relevant but do not visibly specify these congruences. The original preprint full text, including the revised 6 Nov 2026 version, could not be inspected; this is a material residual priority risk, not an automatic failure.

## value

PASS

PASS: the construction resolves a named exact operator-range comparison problem and separates dense-range from invertible comparison for injective noncompact frame operators with nonclosed range. These are natural spectral configurations, and the two explicit dense-range congruences are useful beyond a small parameter check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
