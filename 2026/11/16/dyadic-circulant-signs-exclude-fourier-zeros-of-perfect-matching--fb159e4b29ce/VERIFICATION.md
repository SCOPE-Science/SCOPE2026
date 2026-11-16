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

# Reproducibility checks

Execute `python3 checker.py` with standard Python 3. It computes signed circulant permanents by exact subset dynamic programming for all sign patterns up to global sign reversal at orders \(n=2,4,8\), and checks four deliberately nonidentical patterns at \(n=16\). The observed marker was `CIRCULANT_SIGN_PERMANENT_EXACT_PASS cases= 142`. The checker explicitly verifies congruence modulo \(2^n\), oddness after dividing by \(2^{n-1}\), and the balanced first-row cancellation of the unrestricted perfect-matching Walsh transform.

The mathematical argument covers every \(n=2^k\) with \(k\ge1\), independently of these finite experiments. The complete proof is in `RESULT.md`. Full-text historical-priority checks remain incomplete for Sburlati's 2017 congruence paper. No independently performed mathematical audit is claimed.
