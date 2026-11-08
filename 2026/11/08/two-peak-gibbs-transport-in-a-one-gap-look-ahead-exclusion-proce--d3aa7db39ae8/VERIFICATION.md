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

# Verification record

Run `python3 verify_gap_flux.py` with Python 3 and no dependencies. Expected final line: `ALL_CHECKS_PASSED`.

The program independently constructs the derivative numerator from the rational Gibbs current, checks the exact polynomial coefficient list, computes the Möbius-transformed polynomial coefficient signs and three Descartes sign changes, and evaluates the four rational sign brackets. It also enumerates all compositions with three or four labelled particles and 7–12 holes, checking weighted balance for both jump directions at jump length two. The 24 finite-state direction/batch cases support but do not establish stationarity on every ring.

For general jump length, the proof uses the finite-range Gibbs pairwise-balance identity, canonical-to-grand-canonical equivalence, and a strict-variance monotonicity argument for density. The all-jump-length two-peak conclusion follows from C1 convergence on compact fugacity intervals on either side of the critical scale and strict derivative sign changes; the verifier does not extrapolate the finite witness to an infinite theorem. The three-root classification relies on Descartes' rule and exact rational values, not numerical root finding.

The supplied code is the entire reproducibility dependency. Numerical extrema and densities quoted in the result are illustrative, not proof data. Independent verification has not been performed.
