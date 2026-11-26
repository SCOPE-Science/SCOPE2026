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

FAIL

Material model mismatch: Ferrari arXiv:2607.11422v1 Eq. (9) uses 2^(−ℓ)c_ℓ^J multiplying (1−z)^(ℓ+1). With Theorem 3.1's c_2^2=2/3 at J=2, the coefficient of (1−z)^3 is 1/6, not 2/3. This makes the headline classification false for the named optimized scheme, not just a notation issue. For the actual denominator x+5/3−(5/2)z+z²−z³/6 the derivative is −[(z−2)²+1]/2. At x=3/5>141/250 it has a real root s in (1,2), since the denominator is positive at 1 and negative at 2; Vieta gives |Z|²−s²=15−6s>0. The positive real residue therefore dominates, and the genuine optimized scheme has eventually strictly positive weights there, contradicting the stated oscillation. Equal moduli actually occur at s=5/2, x=15/16. For the *displayed* polynomial in the frozen source, the mathematical pole proof does work: P' is strictly negative on the real axis, Vieta gives |Z|²−R²=6−15R/4, and the crossing occurs at R=8/5. The real pole is simple with positive expansion constant; a dominating nonreal pair has both signs on recurring subsequences by density for irrational angle or zero mean and positive mean square for a nondegenerate periodic orbit. At equality the ratio 4|C_Z|²/C_R² reduces to 2/(1+cos θ)=128/107, and rational 2cos θ=43/32 rules out roots of unity. Thus both signs occur infinitely often for that formula at the crossing. Independent exact multinomial extraction of [z⁶] from (60/163)Σ[(240z−150z²+40z³)/163]^m gives −1843765644000/3057125241215467 at x=11/20, also for the displayed polynomial only. BDF2 has positive coefficients up to and including its double real pole case at x=1/2. Read VERIFICATION.md and verify.py without executing the uploaded script: its finite computations check the displayed polynomial, not the citation/normalization and not the infinite claim.

## originality

FAIL

No distinct valid finding for the named optimal scheme is established by the frozen record. For the correctly normalized Ferrari problem, same-day Resultary 0667c094ef1b already supplies the exact pole crossover and an exact finite-lag obstruction below it; the tail classification follows directly from those pole data. The algebra for the differently normalized polynomial is not a duplicate of that catalog record, but it cannot substantiate a new Ferrari result.

## value

FAIL

The eventual-versus-all-lag question is motivated for the actual optimized scheme. The frozen polynomial's cubic coefficient instead arises from dropping the normalization factor; no independent reason to study this specific coefficient is established. Correcting it would replace the stated boundary and example, with the normalized problem's crossover and finite-lag distinction already supplied or directly implied by the catalog evidence. The valid algebra for the mismatched polynomial is not a valuable surviving optimized-scheme claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
