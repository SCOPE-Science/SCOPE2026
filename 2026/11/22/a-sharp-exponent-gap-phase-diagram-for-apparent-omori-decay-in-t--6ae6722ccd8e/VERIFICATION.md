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

The actual embedded `checker.py` was run with Python 3 standard library only and returned `PASS 3668 assertions`. It checks the exact rational critical ratio, polynomial factorization, numerical derivative identity and a finite set of phase classifications. No external solver is necessary.

The proof in `RESULT.md` verifies the general claim for every \(A,B,c>0\) and \(0<p<q\). Its crucial infinite step is that the stationary-time equation is bijective to \(\kappa(u)=k\), whose derivative has at most one positive zero. The finite checker is a consistency test and not a substitute for that argument.

The two extremes and their threshold concern the local *log-time* exponent of a deterministic composite event rate; they do not claim an exact finite-sample inference rule or actual earthquake forecasting. No independent audit has been performed.
