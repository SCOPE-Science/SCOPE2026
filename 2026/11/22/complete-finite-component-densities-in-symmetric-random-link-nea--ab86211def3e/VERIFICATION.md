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

# Reproduction and limits

Run `python3 VERIFY.py` in the directory containing that file. No dependencies beyond Python's standard library are required. The actual saved execution yielded `VERIFY_OK 121 assertions`.

The script independently enumerates every strict edge ordering for complete graphs with two, three, and four labelled vertices. It compares exact expected counts by component size with a rational-arithmetic Markov recurrence that conditions on the number of previously unseen vertices. It verifies exact total vertex mass and the known total-component expectation through twenty-two vertices. Deterministic Simpson quadrature and a float recurrence at 350 and 700 vertices check convergence for sizes two through eight and numerical normalization of the proposed density.

The finite enumeration checks precisely the enumerated sizes only. The finite recurrence, numerical quadrature, and agreement with asymptotic values do not by themselves prove the limit. The all-size argument rests on the exact exponential-clock Markov jump rates, bounded quadratic variation, finite-time Grönwall convergence, the two-ancestor pure-birth solution, and an explicit late-vertex bound, all proved in `RESULT.md`. No external or independent mathematical validation has been performed.
