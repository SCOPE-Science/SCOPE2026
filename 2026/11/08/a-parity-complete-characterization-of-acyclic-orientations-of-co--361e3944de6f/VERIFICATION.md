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

## Reproduction
Run `python3 artifacts/verify.py` using Python 3 (standard library only). The script independently enumerates every directed orientation of \(K_{m,n}\) for \(1\le m,n\le4\), tests directed acyclicity using Kahn elimination, builds the exact set of achieved indegree-parity signatures and compares it with the proposed necessary-and-sufficient condition. It then constructs and validates witnesses for 4,032 canonical parity-count profiles with \(1\le m,n\le12\). Within each part, permutations of vertex names preserve feasibility, so checking one canonical target for each profile is appropriate to this secondary test.

## Observed results
`ALL_ORIENTATIONS_AND_PARITIES_OK` was emitted for all sixteen small part-size pairs; the corresponding counts by rows \(m=1,2,3,4\) were \((2,4,8,16)\), \((4,7,16,31)\), \((8,16,32,64)\), and \((16,31,64,127)\). The run additionally emitted `ALL_PARITY_COUNT_PROFILES_CONSTRUCTIVE_OK 4032 profiles, m,n=1..12` and `VERIFY_OK`.

## Verification limits
The exhaustive edge-orientation search only covers at most sixteen edges. The larger witness tests cover all parity-count profiles in a bounded parameter range but do not prove the unrestricted result. The unrestricted classification follows from the safe-source lemma and induction in `RESULT.md`. Independent audit has not been performed.
