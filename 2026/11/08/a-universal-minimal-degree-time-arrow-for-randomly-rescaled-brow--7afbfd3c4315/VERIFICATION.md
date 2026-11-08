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

The stationary generator calculation and the semigroup equations for the first and third powers establish the displayed formula without truncating a series. The factorization \((a-a^3)-(1-a^4)/2=-(1-a)^2(1-a^2)/2\) fixes the sign on the entire assumed support. The time-integral representation covers coincident and unequal relaxation rates, and the derivative analysis establishes one strict maximum. The degree-minimality statement follows from exact spatial sign symmetry and stationarity.

The included `proof_checker.py` uses the standard Python library. Invoke `python3 proof_checker.py` in a directory containing the extracted source. Expected result: `PASS: 1896 diagnostic assertions; sharp signed-rate identity, rate collision, strict sign and unique lag maximum`.

The finite checks include exact rational moment equations for signed and nonsigned marks, numerical comparisons of two algebraically independent two-time formulas, and a rate-collision law. They do not independently prove the infinite family of real-valued mark laws or establish publication priority. No external scientific audit is claimed.
