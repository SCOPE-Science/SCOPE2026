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

Absorption before the next reversal has probability at least exp(−ℓ) after each reversal, yielding a geometric tail for N and analytic count cumulants at z=1. In distance units λ/v the first-step generator gives f'_+=f_+−zf_- and f'_-=zf_+−f_-, with one absorbing value at each outgoing velocity. The transfer matrix squares to (1−z²)I; its (1,1) coefficient A_q=cosh(qw)+sinh(qw)/w gives the right numerator. Applying the transfer first from the left endpoint and then across the remaining h gives the other numerator z sinh(hw)/w, with common denominator A_ℓ. Both event probabilities are positive for 0<s<1 and parity agrees with the outgoing direction. In the difference of conditional count cumulant generators, the normalized common denominator cancels. Expanding the log of the residual left/right ratio at z=e^θ, y=1−e^(2θ), verifies both rational formulas, including the deterministic +1 contribution to Δ_m but not to Δ_V. Their increasing q-parts have strictly positive derivatives (the numerators are 2q(q²+3q+3) and 4q³(q³+6q²+15q+15)); their decreasing h-parts enter with minus signs. The left limits are 1−ℓ²/3 and −2(ℓ⁴+15ℓ²)/45, and the right limits are strictly positive. This gives exactly the asserted threshold domains, including no interior mean zero at ℓ=√3. With u=q+1 the differences become (u²−h²+2/u)/3 and 2[(u²−h²)(u²+h²+15)−20u−6/u+10/u²]/45. Substitution of the mean zero gives −(4/15)(4u+6/u−1/u²)<0. The small-ℓ variance gap divided by 2ℓ²/3 converges uniformly to 3s²−(1−s)². For large ℓ let M=ℓ+1 and d=u−h, so s=1/2−1/(2ℓ)+d/(2ℓ). Evaluate at d=c/M²: the scaled mean equation tends to c+4, and the scaled variance equation to c/2−10, with errors O(M^−2) uniformly for bounded c. Bracketing and the nonzero limiting slopes yield the coefficients −2, 10 and hence 12 in the three stated ℓ^−3 expansions with at least the claimed error. Section 1 of python /workspace/review_reproduction.py replays the cumulant identities and verifies the numerical example (0.2886751345948129, 0.4155475052942946) at ℓ=3. Finite checks are not the proof, and none of these arguments classifies elapsed-time variance or sticky/reactive endpoints.

## originality

PASS

The balance of evidence supports the paired interior mean/variance threshold theorem, not novelty of standard telegraph transforms, the classical splitting law, or the one-sided or boundary-start marked counts. The strongest inspected same-day record has exactly the right-exit boundary law and the same transfer method. Primary one-sided marked passage laws can in fact be combined to give interior two-sided PGFs. Neither of those facts establishes the global two-root comparisons and their different rates of appearance by parameter substitution.

## value

PASS

Exit side is a natural conditioning event for a finite-speed searcher, and the reorientation burden is distinct from elapsed time. The result establishes that the two conditional rankings disagree on a computable spatial region, even though they compare the same two count laws, and explains how the region changes with persistence. At high reversal rates the disagreement is confined to a cubic-width layer; at weak rates the variance ordering alone still switches. The value is the full exact comparison and scale, not another calculation of splitting probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
