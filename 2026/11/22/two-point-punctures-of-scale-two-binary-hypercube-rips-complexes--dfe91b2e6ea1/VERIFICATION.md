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

The standalone `verify_morse.py` uses only the Python 3.9+ standard library. Place `morse_cases.json.gz` in the same directory and execute `python3 verify_morse.py`. The output must match `EXPECTED.txt` byte-for-byte (allowing the shell's normal line endings). The compressed certificate contains every free-face pairing and every critical maximal facet for all 18 pair-distance representatives. The checker independently enumerates all cliques by lexicographic Hamming-distance tests, constructs codimension-one incidences, verifies unique-coface freeness and maximality at each step, and requires no live faces to remain. It checks exactly one critical vertex plus the claimed dimension-two or dimension-three cells. Total audited face occurrences: 48,578.

A free-face pair is an elementary collapse, and removal of a critical maximal facet records one Morse cell. The resulting peeling is an acyclic discrete-Morse matching: a cyclic gradient path would contradict the earliest face pairing's freeness at its removal. The certified CW model has one zero-cell and only one positive critical dimension, hence the homotopy wedge claim follows integrally without relying on mod-two Betti data. Finite exhaustive certificates make no claim outside the checked range \(3\le n\le6\).

The compressed certificate is data, not trusted code. This verification is not independent third-party mathematical validation.
