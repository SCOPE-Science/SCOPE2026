---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For iid uniform q-ary input, every adjacent inequality bit is independent Bernoulli(p=(q-1)/q), because each bit pattern has q(q-1)^k realizations. Distinct disjoint effective swaps correspond bijectively to path independent sets. A run of t active edges contributes F_(t+2). Complete 1^t0 geometric cycles have length t+1 and log reward log F_(t+2), yielding the displayed renewal LLN/CLT with finite exponential moments, and a geometrically bounded final cycle. The paired-matching 3-state transfer yields E B_n^2=h^T M_p^(n-1)e; P_p(lambda^2)=lambda*p*(p-1)<0 ensures positive Perron growth gap. Independently enumerated all Bernoulli patterns q=2,3,4,N=0..8, reproducing first and second moment recurrence. Exact boundary n=1 gives moments 1; fixed q>=2 and natural logarithms only.

## originality

FAIL

A published SCOPE finding dated 2026-11-02 already states exactly the full final theorem: same random disjoint-swap ball, all-length second-moment GF, same cubic/spectral gap, same renewal log strong law, identical Gaussian variance series. The Nov 8 claim is mathematically covered, not merely title-similar. No independent original remainder after excluding the already-known deterministic sphere formula and mean.

## value

FAIL

The calculation is useful for information-theoretic sphere concentration, but it is an exact recomputation of a fully published all-parameter theorem. Correctness and reproducibility alone do not constitute a new valuable mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
