---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Reproducing the finite checks

Run `python3 verify_wagner.py` with Python 3.10 or later. The program generates admissible simplices by direct degree counts and checks the full automorphism group by enumerating all vertex permutations. It verifies a complete directed Hasse sorting and the critical masks for the nonequivariant discrete Morse calculation. For each automorphism it sums alternating contributions on all unions of its edge cycles which form faces, and verifies the reduced-homology character. Sorting all 1696 Hasse vertices certifies the matching, not an equivariant Morse equivalence.

Observed checks: 52 facets of dimension six and seven of dimension seven; critical masks 1 and 2646, 847 pairs; graph automorphism order 16. The chain alternating contributions in degrees 0 through 7 are `(0,0,0,1,0,0,0,1)` for `r` and `(2,4,-8,-7,12,6,-6,-1)` for `s`. The augmentation gives the reduced Lefschetz number 1 in each case, so the degree-five sign is −1 in each case. The program does not calculate integral homology of geometric quotients. The rational quotient statement in `RESULT.md` is deduced by averaging, not by numerical inference.
