---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The regeneration identity pi_r=r delta_0 sum_k s^k P^k gives a normalized invariant distribution and uniqueness by TV contraction with factor s per step. Reversibility yields G_s(0,n)=m_n G_s(n,0); the strong Markov property along successive lower-site first hits factors the latter as G_s(0,0) times the product of the w_j. The reversible weight product has m_n proportional asymptotically to n^(−2 epsilon) and p_n tends to 1/2; divergent edge resistances on the positive half-line (2 epsilon > −1 in the stated range) give almost-sure lower hits. Each w_j rises strictly and continuously from zero to one, and the first two target constants lie strictly between those endpoints. At r_1, the exact site-one balance pi(1)=s[pi(0)/2+(2+epsilon)pi(2)/4] yields pi(2)/pi(1)=2(2−s)/(s(2+epsilon))>1. Thus r_2>r_1, and continuity preserves pi(2)>pi(0) immediately to the right of r_1. Positive summable masses and strict separation from site one guarantee an attained outer maximum on each side. Each adjacent ratio is strictly decreasing in r, so equalities are countable; in the claimed window there are in fact only finitely many potentially tied pairs since w_n≤s≤1−r_1 and m_n/m_(n−1) tends to one. A plateau of four positive sites would force 1=s[1−epsilon/(j²−1)] at two distinct interior sites j≥2, impossible; this also justifies the qualitative 'short plateau' wording. An independent recurrence evaluated with outward rounding and tail bounds 0≤w_501≤1 encloses r_1 near 0.00740343587959632569 and r_2 near 0.03099729756312700554 within widths below 8e−31, confirming the quoted decimals. Replay: python3 /tmp/opencode/ordinal3_threshold_check.py. The submitted uncertified tail approximation and mass-losing finite-window propagation were inspected, not run; they are diagnostics, not interval certificates or infinite-chain proofs.

## originality

PASS

The same-chain hitting transforms are prior and mathematically very close, as are modal shifts for continuum diffusions. The surviving claim is the pair of exact stationary neighboring-site thresholds, their strict order for all weakly outward biases, and the consequent open coexistence interval for a single lattice reset site. The inspected sources do not give this combined stationary shape claim. The implication is short but not a direct identification with an existing first-passage optimization threshold.

## value

PASS

Local attraction caused by resetting and outward displacement of the stationary mass are not mutually exclusive. This example gives a strict central peak and two side peaks for an open interval across the entire stated outward-bias regime, not just a tuned numerical profile. The exact neighboring-site comparisons isolate the mechanism and give a region where the reset-site peak is lower than outer mass, while leaving the full inventory of extrema explicitly open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
