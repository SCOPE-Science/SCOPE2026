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

The analytical calculation is entirely contained in `RESULT.md`, steps 1–6. The checker `checker.py` verifies the symbolic derivative factor identity and tests high-precision boundary values and representative interior evaluations. Run it with Python 3, SymPy and mpmath installed. It does not enumerate all real parameters; the proof's global minimization handles those quantifiers.

The first public source date is the publisher's 18 April 2023 online publication date. The paper's submission or revision date was not used as a first-public date. Source comparison covered Proposition 7 and surrounding original article and separately indexed related copulas. A 2024 related source's abstract was accessible; its complete text could not be inspected, so possible historical overlap remains a stated limitation. No independent audit was performed.
