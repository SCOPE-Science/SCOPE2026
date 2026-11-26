---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a nonconstant binary quasinecklace the defining tie-break is automatic: each longest zero run is followed by 1, and the word ends with 1. Remove its initial 0^ℓ1; splitting the remaining suffix at ones gives exactly the (possibly empty) composition of n−ℓ−1 with parts at most ℓ+1. Adding the two constants proves the exact formula, including n=1. A nonempty suffix contributes x_{n,ℓ}=n2^(−ℓ−2) times the fair-bit probability of no ℓ+1 consecutive zeros with the final bit fixed at 1. For r=ℓ+1, two starts of 10^r within distance r are incompatible; separate starts are independent. Counting separated h-tuples gives binomial(M−r(h−1),h)2^(−h(r+1)), M=t−r−1, and Bonferroni gives exp(−x) at a fixed phase and offset. The initial boundary-run event is O(2^−r). In the lower tail disjoint blocks of 2^(r+2) bits each have probability >1/2 of an internal occurrence by the stated second-moment bound; this gives an exponentially summable tail in x. The upper tail is geometric in ℓ−floor(log₂ n). Burnside gives N₂(n)~2^n/n; the phase approximation holds over all n by compactness of the phase circle and the uniform tail estimates. The profile extends holomorphically to |Im θ|<π/(2 ln 2) by local uniform convergence, proving real analyticity. Unfolding the periodization gives the stated gamma coefficients and |c₁|≈7.13011726×10⁻⁶; hence many phase subsequences and no scalar ratio limit. Independently counted maximal circular zero-run starts over every binary word at lengths 2–11 (python -B /workspace/independent_checks.py 4). That finite check tests the counting equivalence, not the asymptotic.

## originality

FAIL

The exact count is equivalent to earlier fixed-content enumeration summed over content. More decisively, the nonconstant unrestricted overhead law is a corollary of Bender–Canfield–Gao's published asymptotic distribution of the multiplicity of the maximum part of a uniform composition. The correspondence between quasinecklaces and maximal cyclic zero runs also appears in the earlier exact-content Resultary record. The transfer from fixed terminal bit to circular fair bits and from fixed-multiplicity probabilities to the first moment needs a tail check, supplied below. This is mathematical coverage, not a conclusion from a similarly titled result or an attempted but inaccessible source.

## value

FAIL

The quasinecklace interpretation is natural and the ratio is useful as a candidate-count estimate, but the claimed invariant is already determined by the older maximum-part multiplicity asymptotic and known rotation characterization. The boundary bias is asymptotically negligible and the tail estimate is a standard finite-pattern bound. No new remainder order, dependence law, or algorithmic cost result survives this prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
