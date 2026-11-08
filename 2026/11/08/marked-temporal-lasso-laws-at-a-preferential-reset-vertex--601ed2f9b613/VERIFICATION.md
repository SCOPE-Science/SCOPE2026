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

# Reproducibility and scope
The embedded `checker.py` uses only the Python standard library. Run `python checker.py`. Its separate exhaustive exploration compares the finite joint \(Q_n(t,j)\) cells against direct enumeration of all functions on at most five vertices, and separately checks the exact joint two-color mark generating function by enumerating functions and valuations. It prints `BIASED_FUNCTIONAL_FRAME_ORBIT_CHECKS_OK` on success. The critical limit follows from a factorial-product local asymptotic and the uniformity of all positive \(j\) cells; the supercritical limit follows by a hub-collision coupling with non-hub collision probability \(O((np_n^2)^{-1})\). The computational tests alone do not establish either infinite limit. Scientific literature comparison and priority risk are detailed in the review; independent validation has not occurred.
