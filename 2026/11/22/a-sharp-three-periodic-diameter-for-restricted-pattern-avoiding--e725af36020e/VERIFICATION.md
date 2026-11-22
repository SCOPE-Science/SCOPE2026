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

# Verification record

The self-contained proof is in `RESULT.md`. All-length validity rests on (1) the inversion-code characterization, (2) the exact legal adjacent-flip criterion, (3) a pathwise lower bound counting forced shared-one coordinates and a matching two-sweep construction, and (4) a three-position packing upper bound with an explicit saturating endpoint pair. The external 2022 source supplies the inversion-code characterization, while the edge, distance and diameter proofs are spelled out in `RESULT.md`.

The package contains `verify.py`, a standard-library Python checker. From the directory containing the extracted files, run `python3 verify.py`. It enumerates ordinary-pattern-avoiding permutations and their legal swap edges independently of the binary code for \(2\le n\le8\); it then enumerates all \(111\)-free binary states for \(1\le m\le10\), compares every breadth-first-search distance with the forced-coordinate expression and checks the exact diameter formula. The recorded successful execution ended with `ALL TESTS PASSED`; direct permutation counts were \(2,4,7,13,24,44,81\) and bit-model counts \(2,4,7,13,24,44,81,149,274,504\). These finite tests cannot replace the proof for all lengths.

The proof does not address other pattern classes or longer forbidden-run diameters. The literature-priority conclusion remains subject to an unindexed equivalent and the inaccessible complete text of a related broader-graph finding. Independent mathematical audit is not performed.
