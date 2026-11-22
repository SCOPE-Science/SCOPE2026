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

The exact checker constructs a caterpillar with independently defined vertex distances and generates every general-position face by rejecting selected geodesically collinear triples. Every collapse pair is checked against every current coface and is accepted only when the proposed free face has exactly its designated upper coface. The checker verifies the remaining graph is connected and its cycle rank matches the closed formula.

Command: `python3 verify_caterpillar_collapse.py`. Captured stdout is `verification_output.txt`. The benchmark run verified 373 profiles, 60,300 initial simplices and 23,078 exact free-face removal pairs. The tests are exhaustive only inside their stated profile bounds; the proof in RESULT.md supplies the infinite-family argument. No independent external audit has occurred.
