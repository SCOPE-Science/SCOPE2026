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

# Reproducibility

Execute `python chord11_checker.py` with Python 3 and no third-party dependencies. The complete checker reconstructs Machin-formula rational interval bounds for \(\pi\), Taylor bounds for \(\sin\) and \(\cos\), and all cyclic support sets. The output must include `Certificate PASS`, 3674 essential quadrilaterals, 11 redundant four-normal configurations, 330 bounded triangles and exactly 11 winners. The lowest rigorous excess for other essential quadrilaterals is above 0.008.

The geometric reduction from arbitrary chord-parallel enclosing polygons to support-line triples/quads, the positive-spanning normal criterion and the support-area identity are explained in RESULT.md. The finite verifier certifies numerical comparisons only; it does not replace these geometric steps or prove priority in the literature. No independent audit is claimed.
