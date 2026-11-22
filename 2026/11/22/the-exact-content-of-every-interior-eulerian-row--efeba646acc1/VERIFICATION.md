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

The theorem is reconstructed from the Eulerian series identity, mod-two Lucas criterion, the explicit first interior coefficient, and the exact second and fourth cumulants of the descent distribution. Under the hypothesis that an odd prime divides every nonendpoint coefficient, evaluation at one forces \(p>n\). Consequently the use of moment identities and rational formal series modulo \(p\) is legal. Comparing to the endpoint-only two-point distribution forces \(3n\equiv1\pmod p\) and \(5(n-1)^2\equiv1\pmod p\), hence \(p=11\), which is incompatible with \(5\le n<p\). This supplies an infinite proof independently of any search or software.

Run `python3 check_eulerian.py` with Python 3 standard library. It checks Eulerian recurrence rows through \(n=240\), inclusion-exclusion coefficients through \(n=48\), and exact first, second, and fourth cumulant identities through \(n=20\), reporting 1,462 exact assertions. Tests are finite and diagnostic, not certificates of the all-index statement.

Checks do not establish priority in literature unavailable in full text. The published finite table of row gcds is not an infinite proof. Independent audit has not been performed.
