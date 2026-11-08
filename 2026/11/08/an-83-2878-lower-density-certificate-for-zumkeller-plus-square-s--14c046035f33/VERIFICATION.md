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

Run `python3 verify.py` with the standard Python library (no external packages). The checker enumerates square-root difference residues modulo the squares of the ten odd primes, rechecks each two-prime Zumkeller factor using exact subset sums, and calculates the CRT density using `fractions.Fraction`. It counts all new mixed-support residue classes on the full period \(44100\), finding \(6804\) classes in the mixed event, \(3780\) overlapping the original \(p=3\) event, and \(3024\) additional classes, which is exactly \(12/175\). The combined bound is \(2768772438842683346/3324339686048415489\). See `verification_output.txt` for the executed result.

The proof supplies a positive CRT square witness for every represented residue class once \(N>236421376\); no bounded enumeration is presented as a proof of an asymptotic statement. The combined periodic certificate is not the full set of Zumkeller-plus-square sums. No external or independent mathematical audit is claimed.
