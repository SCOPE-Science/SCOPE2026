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

`python3 verify_singer13.py` was executed against the packaged source. It reconstructed the thirteen line translates of the Singer difference set and independently checked the finite-field model, every point pair on precisely one line, the \((13,78,234)\) face vector, and the free rotation cell-orbit counts \((1,6,18)\). It regenerated all eighteen ordered attaching words, verified that each of the five named generator eliminations uses a two-cell with unit occurrence of the eliminated generator, and computed eight trivial words and five degree-thirteen remaining maps. The exact recorded run ends `VERIFY_OK` in `verification_output.txt`.

The boundary matrix reconstructed from the quotient attaching words was also reduced by exact integer arithmetic, yielding Smith factors \((1,1,1,1,1,13)\). This is an independent homology cross-check; the stronger homotopy type relies on the explicit two-cell cancellations and nullhomotopies. The universal-cover deck-module calculation follows from the lifted Moore CW chain complex and its regular sphere orbits. No larger field orders or external independent validation were checked.
