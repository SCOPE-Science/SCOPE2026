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

For any selected distinct pair α,β the normalized Fourier projection has pointwise convolution sum with kernel (α+β)/N and exact supremum norm equal to its absolute kernel sum. The quotient β/α takes the q-th roots uniformly, q odd and dividing N. Using the centered representatives j=−(q−1)/2,…,(q−1)/2, the mean of 2 cos(πj/q) is 2/[q sin(π/(2q))]. Since sin(t)−t cos(t)>0 for t in (0,π/2), this norm decreases strictly with q, and the largest possible norm occurs at the smallest prime divisor p; a character of order p exists in the dual. For the phase witness on the cyclic order-p image, the same centered representatives give h(j)=exp(πij/p), so its k-th coefficient is sin(π(1−2k)/2)/[p sin(π(1−2k)/(2p))]. The two residues k=0,1 both give the same positive coefficient and uniquely minimize the denominator magnitude. Pullback has zero coefficients off the cyclic character subgroup. Hence the greedy projection really selects the sharp pair, independently of ties, and its value at zero is the proposed bound. Conversely equality at a maximizing point forces q=p and equality in each term of the convolution estimate. No kernel entry vanishes in odd order, so f has constant modulus and is proportional to the conjugate translated kernel phase; expanding it gives precisely the stated modulation and translation. Those operations and scalar multiplication preserve greedy selection and equality. This also covers p=3, groups not cyclic, and inputs with Fourier support smaller than two for the bound.

## originality

PASS

The root-of-unity average, its odd-order behavior, and the resulting optimal fixed two-character kernel norm are already covered by available two-point or two-frequency formulas. The supported distinct claim is the nonlinear magnitude-ranked operator: exact attainment with a strict selection gap, followed by classification of every equality input on all odd finite abelian groups. No inspected stronger result makes that selection or classification automatic.

## value

PASS

The first nontrivial greedy rank is a natural norm-growth question for magnitude rearrangements, not a randomly chosen finite slice. Compatibility of linear norm attainment with the nonlinear selector is a real constraint. The sharp constant for every odd finite group and the strict-gap equality classification give a benchmark for further ranked projections and identify the precise dependence on the smallest prime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
