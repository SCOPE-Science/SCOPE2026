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

# Verification and scope

The analytically proved statement is the joint weak limit of a scaled time until the first strict longest-gap decrease, the original parent rank of the replacement longest gap, and the scaled size of that decrease. The model is a unit circle with an i.i.d. uniform point sequence.

The critical ingredients have explicit proofs in `RESULT.md`: (i) normalized independent exponentials represent all initial gaps; (ii) thinning a rate-one spatial Poisson process supplies independent original-gap first-hit clocks; (iii) the discrete waiting count differs negligibly from the corresponding Poisson time at scale \((\log n)/n\); (iv) the first cut of each damaged top-ranked gap rules it out as the next leader with probability tending to one, provided some other top rank survives; (v) the probability that the first \(m\) ranks after the leader are all hit tends to \(1/m\), making truncation valid; (vi) independent exponential order gaps give the exact conditional drop distribution.

Run `python3 checker.py` in the directory containing this file. This checker uses only the standard Python library, checks the rank mass telescoping identities, verifies a truncated-mixture series with a rigorous remainder bound, checks conditional exponential-max CDF identities, and simulates actual forward insertion into initial circular gaps while tracking the original parents and all fragments. Its fixed-seed execution passed **113739** assertions; direct finite-sample simulations illustrate slow convergence but are not used to prove an infinite theorem.

The result does not supply convergence rates or convergence of finite-sample means, does not analyze nonuniform locations or higher dimensions, and makes no claim to have checked every historical paper. Self-review is reported; no independent audit has yet been performed.
