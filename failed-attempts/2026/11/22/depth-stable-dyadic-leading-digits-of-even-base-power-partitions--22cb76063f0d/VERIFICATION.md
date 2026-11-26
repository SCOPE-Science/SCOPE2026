---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The ordinary uncoloured partition series satisfies B(q)=B(q^m)/(1−q). Write G_r(q)=sum_{n≥1} b_m(m^r n−1)q^n. The recurrence for B gives G₁=qB/(1−q) and extraction gives G_r=B A_r with A₁=q/(1−q) and A_{r+1}=U_m(A_r/(1−q)). For a_r(x) the polynomial coefficient sequence of A_r, a₂(x)=mx and a_{r+1}(x)=sum_{j=1}^{mx}a_r(j). The normalization h_r=2^{r−2}a_r/m^{r−1} has h₂=x and is iterated by T_m f=(2/m)sum_{j=1}^{mx}f(j). In the monomial basis the Faulhaber coefficient of x^t in T_m x^k is 2m^{t−1} binom(k,t−1)B_{k+1−t}/t with the B₁ sign convention for sums starting at 1. Since 2B_j is dyadically integral, its coefficient valuation is ≥(t−1)a−ν₂(t)≥0. The Bernoulli bound also follows from vanishing of odd B_j beyond B₁ and the Bernoulli recursion at even j, which divides by the odd j+1. As T_m x=x+mx², h_r≡x modulo 2^a coefficientwise. Substituting in G_r and removing the odd factor (m/2^a)^{r−1} mod 2 gives the stated convolution and integer divisibility at every r≥2. At n=1 the convolution is b_m(0)=1, so the exponent is attained, including for m=2 and for all even non-prime-power bases. No finite checker run is needed to justify the infinite claim. The originality failure is not a counterexample to this proof.

## originality

FAIL

The full normalized parity claim, not just the universal divisor, is a direct consequence of Rødseth–Sellers' published kernel identities and coefficient bounds (2001). Passing to one bit above their published divisibility bound leaves only the adjacent-kernel term in Lemma 2, whose coefficient after normalization is odd by the recurrence in its proof and Eq. (10). This yields the entire claimed convolution for all even m, all r≥2 and all multipliers n, including the all-ones exact valuation. The alternative Bernoulli-operator proof is valid, but its theorem as stated in the Finding is already covered by that prior machinery.

## value

FAIL

The index progression and the sharpness question are well motivated. But the exact invariant offered as the contribution is a routine one-bit refinement of the existing published triangular recurrence, with no distinct valuation case left outside that implication. The Bernoulli proof is an alternative explanation of the same Finding; the record does not establish an independently needed new theorem or a new use of the method beyond its parity and sharpness claim. No narrower surviving claim from this Finding is supplied as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
