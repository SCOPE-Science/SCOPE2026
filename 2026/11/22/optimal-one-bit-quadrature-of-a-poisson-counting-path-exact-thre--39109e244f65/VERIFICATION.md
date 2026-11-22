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

# Verification

Execute `python3 verify.py` with the Python standard library (Python 3.10 or newer). The verifier independently builds finite Poisson probability tables, evaluates Bayes conditional-means directly and via the closed covariance formula, and searches a 200-point grid of times over rates \(\lambda\in\{1,3,10,30,100,250\}\). The actual execution completed with **1,182 finite consistency checks passing**. At the two largest rates, the maximizing grid time is close to \(2/3\) and the captured fraction is close to \(16/(9\pi)\).

The test is neither an exhaustive proof of the integer-threshold optimum for unbounded counts nor a proof of the large-intensity limit. The displayed analytical proof establishes those statements by nearest-neighbor encoding, uniform tail bounds, a sharp normal inequality, and stability of optimal two-level quantization under Wasserstein-two convergence. There is no independent audit or external mathematical certification.
