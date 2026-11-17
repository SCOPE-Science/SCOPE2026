---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

For infinite-volume continuous-time SEP started at a step and reset by iid Pareto waiting times with support τ≥t0, no-reset mean current is j0(a)=e^(−2a)I0(2a), J0(a)=∫0^a j0~sqrt(a/π). Renewal measure U gives exact transforms Dhat(s)=[(q j0)^hat]/[s(1−ψhat)] and Nhat(s)=[(q J0)^hat]/(1−ψhat), where q is the Pareto survival function. At α=1/2 the numerator is logarithmic and denominator ~sqrt(πt0)s^(1/2), giving D~π^(−3/2)sqrt(t)log(t/t0). At α=1 the integrable current reward G(t0) and infinite-mean renewal denominator yield D~G(t0)t/(t0 log(t/t0)). At α=3/2 finite mean μ=3t0 and h=qJ0~t0^(3/2)/(sqrtπ a) give N~sqrt(t0)log(t/t0)/(3sqrtπ) by the renewal-density limit and convolution splitting, not by falsely asserting net-current monotonicity. The proof separates finite-time renewal and large-t asymptotics and matches normalization of one hop per direction.

## originality

PASS

Mishra–Basu (2022) developed the exact SEP renewal transforms and off-critical power-law regimes; their actual full text Section 5 distinguishes α<1/2, 1/2<α<1, α>1 and Section 6 distinguishes α<1,1<α<3/2,α>3/2, without stating sharp logarithmic boundary terms and their constants. The three marginal limits require boundary-specific slowly varying Tauberian and finite-mean renewal-density arguments, so they are not valid by simply substituting a marginal parameter into an off-critical amplitude. Resultary searches found no earlier same-model critical log laws. Best-of-knowledge PASS is qualified by closely related standard renewal results from which the terms may be derivable.

## value

PASS

Sharp logarithmic boundary laws fill three naturally missing transition points of an established resetting-transport phase diagram. Their distinct sqrt(t)log(t), t/log(t), and log(t) scalings and exact amplitudes correct misleading pure-power extrapolations, and the renewal-density treatment avoids a genuine nonmonotonicity pitfall for net current.

The dated certificate retains the supplied scientific assessment, sources and limitations.
