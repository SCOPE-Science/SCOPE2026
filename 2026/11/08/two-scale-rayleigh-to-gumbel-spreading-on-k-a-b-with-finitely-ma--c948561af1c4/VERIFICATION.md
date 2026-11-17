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

Splitting rate-one caller Poisson processes into directed edges gives independent undirected contact clocks of rate 1/a+1/b. Thus leaf/hub birth rates are h(b−l)c_b and (a−h)lc_b. On the s=√b·t scale the scaled leaf coordinate has drift h/a with vanishing quadratic variation and the hub jump intensity approaches (a−h)y/a; the finite-jump PDMP is uniquely constructed from integrated hazards and all hubs activate almost surely by finite scaled time. The first extra-hub time is the minimum of b independent two-stage Exp(c_b)+Exp((a−1)c_b) waits, with quadratic small-t cdf and Rayleigh scaling. Once hubs activate by o_P(1) time, b−o_P(b) leaves have independent Exp(1+a/b) residual clocks; conditional extreme-value limits give Gumbel independent of the early path. Rechecked exact birth rates and hypoexponential survival formulas for a=2,3,5 and b=1,4,20. Finite checks corroborate but do not prove J1 joint convergence.

## originality

PASS

PASS only for the early √b activation PDMP, exact first-extra-hub distribution/Rayleigh law, and its joint independence from the late Gumbel. A prior fixed-width biclique theorem already established standard Gumbel completion from a hub seed, so that component is not new and cannot separately support originality. Read exact prior proof and compared identical per-edge rate/state model, not merely a title.

## value

PASS

The first random activation of an initially tiny fixed hub set and its complete finite-jump PDMP are a distinct, motivated epidemic phase preceding known Gumbel flooding; the exact Rayleigh hazard and joint separation provide useful distributional information not implied by a terminal cover time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
