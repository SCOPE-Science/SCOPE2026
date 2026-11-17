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

For k>=3, all squares mod 2^k split disjointly into odd squares congruent 1 mod8 (2^{k-3} classes) and 4Q_{k-2}; the kth Fourier transform consequently repeats depth k-2 away from eight frequencies a divisible by 2^{k-3}. At these eight, the inherited transform is c_k=s_{k-2} for even u and d_k=s_{k-4}-2^{k-5} for odd u (zero at k4), and adding h_k times an eighth-root phase yields exactly the displayed radical two-step increment. Endpoint convolution norms equal the L1 kernel norm by point-mass/phase extremizers. For k>=5, c/h=1/3+a/(3h), d/h=-1/6+a/(3h) with a=4 or5; two-Lipschitz of each modulus difference bounds |Delta_k-C| by 80/(3*2^k). Parity subsequences give two absolutely convergent offsets and tail 80/(9*2^k). Independent direct radix-2 FFT of all squares k1..10 matches recurrence, Parseval and asymptotic C=0.7670312695942494. Thus all-depth proof is mathematical rather than computational extrapolation.

## originality

PASS

Best-of-knowledge originality: established general criteria and overlapping special cases are explicitly credited. Fresh exact finite/arithmetic or spectral classification not mathematically implied by inspected broader statements. Inaccessible plausible primary sources are retained as risks, not falsely described as read.

## value

PASS

Complete quadratic residues including nonunit squares form a natural nested spectral set on dyadic cyclic groups. The exact endpoint projection norm, explicit all-depth radical recurrence and genuinely distinct parity offsets supply precise operator-theoretic invariants where counting squares alone is insufficient. This shows unbounded linear norm growth with a sharp algebraic slope, unlike unit-square projection behavior; nontrivial arithmetic structure, not a routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
