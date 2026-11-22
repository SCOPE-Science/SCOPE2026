---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python verify.py` with the Python standard library. The script uses exact `fractions.Fraction` arithmetic and exhaustively lists the \(\binom{20}{2}=190\) equally likely peer pairs in the finite example. It verifies that 100 and 36 pairs, respectively, make the focal player pivotal on the two sides of the risk threshold, that the exact marginal payoff is \(bp_\pm r-c\), and that its two zero crossings are \(3/10\) and \(5/6\).

The script computes all three signed risk-integral segments, confirming \(E_-=E_+=b/95\), \(H=b/380\), flexible gain \(b/76\), best upper-tail gain \(b/380\), and their difference \(b/95\). The supplementary 1001-point cutoff grid only checks consistency; the complete optimization over continuum cutoffs is proved analytically in `RESULT.md` by differentiating the upper-tail integral and considering its two maxima. All symbolic formulae for the general finite-population theorem follow from the pivotal-event indicator and sign changes of affine pieces, independent of the finite witness.

No formal theorem-prover or independent external scientific audit was performed. The result does not establish population equilibrium, global welfare or evolutionary fixation. The source paper's original adaptive strategy is a restricted policy class; our optimization explicitly enlarges that policy class while keeping incumbent behavior fixed.
