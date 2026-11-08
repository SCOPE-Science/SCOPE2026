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

## Reproducible calculation

Run `python verify.py` using Python 3 with no third-party dependencies. The program enumerates every independent-bond state for finite cycles of orders four to ten at specified exact rational probabilities. It checks the strict separation-difference identity using direct connected-component enumeration and compares four-cycle first and second moments using a separate symbolic polynomial expansion. On the supplied script it reports `PASS 67 exact checks`.

## Scope of mathematical evidence

The proof of the cycle-wide comparison uses two-edge interval counting and exact two-arc connectivity. The proof of the four-cycle variance transition uses a two-open-bond component-size classification, an explicit polynomial, and strict monotonicity. No finite test is used as a substitute for an assertion over all cycle orders or over a continuum of probabilities. The calculation assumes independent undirected bonds and a uniformly selected initial case. Other epidemic timing mechanisms or correlated transmissions are outside scope.
