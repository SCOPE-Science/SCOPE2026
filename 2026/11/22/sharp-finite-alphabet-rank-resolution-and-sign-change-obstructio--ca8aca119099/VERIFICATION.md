---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The common observation tie label must be retained across comparisons. The transform z=a_j+p_j U sends each reference to an independent uniform point, so the conditional rank is Binomial(m,z). Bernstein polynomials span degrees 0 through m; equality of rank laws is exactly orthogonality of the density difference, constant on each alphabet interval, to those polynomials. For d<=min(K,m+1), the minor on the first d rows and any d ordered columns is an expectation of a strictly positive Vandermonde; hence rank=min(K,m+1), with the constant row imposing mass conservation. Positivity of p gives a relative neighborhood in the resulting affine space. For a nonzero null vector with at most m sign changes, put a simple root at each boundary separating opposite nonzero sign blocks; the polynomial can be signed to have a strictly positive integral against the density difference, a contradiction. Alternating cofactors on any m+2 columns give equality in the bound when 1<=m<=K-2. For equal masses the alternating binomial difference annihilates lower degrees and acts on j^(K-1) by (-1)^(K-1)(K-1)!. Multiplying by the Bernstein polynomial leading coefficient gives the displayed sign and amplitude, and squaring gives the Pearson expression by Vandermonde convolution. This includes K=2 (no positive reference count below the threshold), and the K=5 amplitude is 2/3125. The joint-sample indistinguishability inference uses independent observations as well as independently generated references/ties (the ordinary repeated-sampling model for p and q); equal rank marginals alone do not imply the same joint law for dependent observations. The theorem is not a finite-sample power guarantee. The frozen checker was inspected, not run; python3 /workspace/independent_checks.py 1 independently counts ranks by the multinomial numbers below/equal/above each symbol with uniform position among ties, and checks K=2..8 and an irregular K=4 example exactly.

## originality

PASS

The prior exact rank law, eventual consistency, and the classical positivity and moment techniques are not new. The supported distinct claim is their finite fixed-order classification for every positive K-letter null, including the sharp obstruction and exact first-visible response. No inspected result gives that combination or a dominating theorem subsuming the claim. This is a best-of-knowledge assessment.

## value

PASS

The resampling budget is intrinsic to this goodness-of-fit procedure. Below K-1 some strictly positive alternatives are invisible even with arbitrarily many independent observations; at or above that budget this type of nonidentifiability disappears. The null-space dimension, sharp ordered sign obstruction, and explicit first-visible law quantify which alternatives can cause this failure and how weak the first signal can be, without claiming a power guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
