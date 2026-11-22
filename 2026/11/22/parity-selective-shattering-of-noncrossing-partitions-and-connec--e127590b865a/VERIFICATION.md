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

# Reproduction and scope

Execute `python3 verify_matching_parity.py` using a standard Python 3 installation. The script directly constructs all noncrossing set partitions for \(n=4,6,8\) from restricted-growth words, filters them by block-count parity, independently enumerates all perfect matchings, and directly calculates all traces. It compares observed shattering to the connected crossing-graph criterion, and independently checks the complete three-query face count at six points. Exact expected output is provided in `verification_output.txt`. The final marker is `MATCHING_PARITY_PROOF_FINITE_CHECKS_PASS`.

All reported finite checks were executed from the packaged checker path. They corroborate the theorem, but cannot prove its universal quantifiers. The all-size proof relies on the planar positive-closure lemma, the adjacent-block parity switch, and the spanning-tree/path shattering bounds in `RESULT.md`. No independent mathematical audit has been performed.
