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

# Reproducibility and checks

`verify.py` uses only the Python standard library. Execute `python3 verify.py` from the directory containing the result; the observed successful output was `VERIFY_OK 10603 exact assertions`.

The checker enumerates every function \([4]\to[4]\) and \([5]\to[5]\), and directly enumerates all \(n!\) simultaneous relabelings for each. It additionally uses a fixed pseudorandom seed to select maps on six, seven, and eight vertices and compares the position-resolved probabilities as exact rationals. It independently calculates observed probabilities and predicted motif formulas. Bounded enumeration is supporting evidence, not an infinite proof; the proof in `RESULT.md` covers all \(n\ge4\). The first public posting date recorded for the literature source Leckey–Wormald is 2018-03-07.

An independent mathematical audit has not been performed. Historical originality remains qualified by the possibility of an earlier universal labeling theorem; the known permutation-only peak results are explicitly credited.
