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

All three accompanying source files are standalone, with no data downloads or unavailable artefacts needed.

- `g++ -O2 -std=c++17 verify_direct.cpp -o direct && ./direct 16` verifies every Walsh frequency, the complete signed spectrum and exact nullity for each length from one to sixteen.
- `python3 verify_independent.py` independently enumerates intervals and verifies all frequencies through length ten, then evaluates the binomial-Krawtchouk endpoint formula for the first three resonances.
- `g++ -O2 -std=c++17 verify_projection.cpp -o projection && ./projection` independently applies inverse integer Walsh transforms to the spectral projector and checks endpoint norms at three exceptional lengths.

Observed verified values are the nullities \(4,84,8008\), ranks \(4,172,24760\), and endpoint norms \(1,25/4,131177/2048\) at \(n=3,8,15\), respectively. The all-length statement is proved symbolically in RESULT.md; finite experiments alone would not certify it.
