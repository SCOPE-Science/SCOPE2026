---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For α>0, finitely supported u∈V,v∈W permit u+n^−α F^n v∈V with n^α B^n(u+n^−αF^n v)=v for all large n, giving mixing; a separated-block norm-convergent series gives one universal vector. α<=0 forces n^αB^n x→0. If n<m are visits to the ε-ball about e_0, first coordinate at m gives m^α|x_m|>1−ε while coordinate m−n of the earlier shifted vector gives n^α|x_m|<ε, hence m/n>((1−ε)/ε)^(1/α). This bounds visits on every interval of length N logarithmically. Sparse coordinates x_{ceil(q^j)}=a ceil(q^j)^−α yield the exact c0 lower bound as q decreases to that ratio, and ℓp geometric tail with a=1 gives αp/log(1+ε^−p). The upper c0 bound matches, and both ℓp bounds have same ε→0 coefficient α. Verified the c0 geometric witness inequalities independently for sampled α=.8, ε=.15 and all checked j; finite diagnostics do not prove universal statements. Mixed return-time floor/ceiling limits and strict open-ball inequalities were handled correctly.

## originality

FAIL

Decisive stronger-coverage reduction: the full previously published exact ℓp theorem covers every finite p with D_{p,alpha}(eps)=alpha*p/log(1+(eps^{-p/(p-1)}-1)^(p-1)) for p>1. For any ℓp vector, every ℓp return to the eps ball is also a c0 return because ||.||infty<=||.||p; hence C_c0(eps)>=D_{p,alpha}(eps) for all p. For fixed eps<1/2, letting p→infinity yields the submitted c0 constant alpha/log((1-eps)/eps) as an immediate lower bound. The elementary coordinate comparison at successive c0 returns gives the matching upper bound m/n>((1-eps)/eps)^(1/alpha); it is a textbook one-coordinate packing observation. Thus even the purported surviving c0 exact invariant is a corollary of stronger earlier results plus routine endpoint comparison. The ℓp bounds and sharp small-radius limit are already weaker than the same exact earlier formula. Mixing of polynomially rescaled backward shifts follows from the standard separated-block construction, while frequent-universality obstruction is previously known. No independently original mathematical final claim survives.

## value

FAIL

Dense versus sparse return-frequency behavior is mathematically motivated, but the proposed new c0 endpoint numerical coefficient follows by p→∞ from the already published exact finite-p logarithmic return-frequency theorem, using the norm inclusion ℓp⊂c0 and the one-coordinate upper packing argument. The submitted ℓp bounds are weaker than known exact formulas. Standard block mixing and the qualitative frequent-universality obstruction add no substantive independently valuable new theorem; correctness and a convenient c0 presentation do not confer scientific novelty/value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
