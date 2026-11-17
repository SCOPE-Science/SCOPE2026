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

The exact finite-target result of Amit et al. is explicitly prior: coordinate covering T_r=b_r+dG_r with independent geometric-tail G_r and P(G_r>k)=kappa_r 2^-k, 1/2<=kappa_r<1. Distinct coordinate phase residues of b_r imply a unique anchor s for the max B. Conditional on B, the exact CDF is the product over active r of 1-kappa_r 2^-floor((z+h_r)/d). For any receding targets, finite coordinate count allows subsequence extraction with s constant, each offset h_r fixed or infinite, each surviving kappa convergent in [1/2,1]; terms at infinite offset disappear. Conversely, strict superincreasing coordinate weights order all binary subset sums by binary rank; choosing the threshold to be the subset sum of any upper-half rank R realizes every m and any dyadic kappa=R/2^m. Simultaneously choose m_r=M+(s-r-h_r)/d, valid by offset congruence, and let M grow; every parameter tuple is attained, including kappa=1 via ranks 2^m-1. Dyadic interior tuples repeat exactly for infinitely many increasing targets. Independent code checked 5,876,911 cumulative exact rank and weak-law construction assertions, without treating bounded tests as infinite proof.

## originality

PASS

Amit et al. Random Fibonacci Tilings arXiv:2611.08317 (published Nov 5 2026) gives the finite target law (Theorems 3.1, 3.4, 4.3) and proves tightness in §5.3, but its conclusion poses the classification of subsequential centered limits rather than solving joint parameter attainability. The submitted theorem supplies that necessary-and-sufficient parameter space, simultaneous construction of all phase/rank options, boundary values and exact infinitely repeated dyadic laws. Originality is best-knowledge with the risk that strong readers may view parts of its construction as implicit in the finite law.

## value

PASS

Theorem answers a concrete open limit-classification question identified in the primary tiling paper. It replaces tightness and absence of one universal limit with exact full attainable weak-limit family for every fixed dimension; offsets and rank parameters jointly identify the entire stochastic asymptotic behavior, and exact dyadic repetition is nontrivial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
