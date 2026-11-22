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

The theoretical proof is given in `RESULT.md`; the following reproducible checks are finite confirmations and are not used as a replacement for the all-order proof.

Run `g++ -std=c++17 -O3 verify_exhaustive.cpp -o verify_exhaustive && ./verify_exhaustive` to enumerate proper unlabelled partitions and test both color-code predicates. This checks orders two through six and reports counts 4, 17, 74, 307, 1200, including the smaller order two outside the theorem's connected-graph scope; it also confirms that the locating and neighbor-locating predicates agree on all proper partitions inspected. At order six, 61,375 proper partitions are considered.

Run `python3 verify_constructive.py` to generate the normal-form optimum partitions without color-name multiplicity, directly check properness and neighborhood signatures and compare with the symbolic count through order eight. The counts through order eight are 4, 17, 74, 307, 1200, 4461, 15958. The independent code constructions agree with the general formula.

Neither program checks all positive integers. The earlier sources establish general definitions and upper bounds but no independent audit or final publication-priority clearance is asserted here.
