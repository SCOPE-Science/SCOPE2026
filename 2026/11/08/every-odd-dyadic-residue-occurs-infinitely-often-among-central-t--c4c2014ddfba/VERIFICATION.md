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

All central trinomial T_n are odd because T_n=Σ_j binom(n,2j)binom(2j,j) and binom(2j,j) is even for j≥1. Let P(x)=x^-1+1+x. Coefficientwise Frobenius P^{2^s}≡P(x^{2^s}) mod2 plus repeated squaring yields P^{2^r}≡P(x^{2^s})^{2^{r−s}} mod2^{r−s+1}. Choosing s=r−k+1 (r≥k) makes all nonzero exponents of size less than 2^s vanish mod 2^k and gives T_{2^r+m}≡T_{2^r}T_m mod2^k for 0≤m<2^s. Taking s=1 gives T_{2^r}≡T_{2^{r−1}} mod2^r; hence L=lim_r T_{2^r}∈Z₂ exists and L≡T₄=19≡3 mod8. L mod2^k has order 2^{k−2} by LTE, covering the 1/3 mod8 odd classes; T₃=7 multiplies into the remaining 5/7 mod8 coset. Arbitrarily separated dyadic-index blocks realize T_b L^t mod2^k, b∈{0,3}, and can be varied infinitely while retaining the class. Independent recurrence computations reproduced all odd residue images modulo 2^k for k≤8 and bounded block congruences; these are diagnostics. The arbitrary-k proof is constructive.

## originality

PASS

Best-of-knowledge new claim identifies the full 2-adic output closure and infinite representation of each odd unit class for the ordinary central trinomial sequence. Earlier Noe (2006) proves parity/prime-divisibility, OEIS Gauss congruences imply only 2-adic stabilization, Nov2 generalized-trinomial findings give valuations/low unit corrections, and adjacent mod-eight laws cover only a fixed modulus. None of the inspected complete relevant statements contains the separated-block product realization and full all-level odd-class surjectivity.

## value

PASS

Determining the complete p-adic image and infinite multiplicity of every value is a natural exact invariant of a classical combinatorial sequence, substantially stronger than parity and a single-modulus census. The block-separation mechanism is a reusable arithmetic proof device; no asymptotic density is needed for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
