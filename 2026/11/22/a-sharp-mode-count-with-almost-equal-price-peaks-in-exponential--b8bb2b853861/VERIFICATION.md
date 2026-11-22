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

# Verification details

The standalone `verify.py` uses Python 3's standard library and checks the exponential mixture with \(L=400\) for segment counts \(n=1,\ldots,8\). It verifies opposite derivative signs at the two endpoints of each predicted peak window, refines the positive-to-negative crossing by bisection, checks peak-height brackets and the dimension-independent near-equal ratio, and evaluates 1,200 additional randomly generated mixtures by a sampled derivative grid. One local invocation returned `PASS 1693 finite numerical assertions`.

Run `python3 verify.py` alongside `RESULT.md` to reproduce the finite checks. The samples do not establish a universal upper bound, absence of undetected derivative zeros or infinite-parameter assertions. These are justified by the written exponential-polynomial zero-count proof and analytic derivative sign/height estimates in the proof. The code does not provide independent verification or empirical validation. Double-precision root locations and revenue values have numerical error; they are explanatory examples only.
