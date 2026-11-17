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

`certificate.py` is complete and standalone. Execute `python3 certificate.py` in the same directory; `certificate_output.txt` records the observed output. It enumerates the determinant-one projective group independently from all square-determinant matrices; compares the resulting permutation sets; verifies every cell, every incidence, and integral boundary squared; then performs exact unimodular cancellations in descending degrees. The resulting zero differential has generator counts \((1,0,0,30,5,0)\), with one connected degree-zero generator. Modular elimination over primes \(2,3,5,7\) and the Euler-characteristic check provide separate consistency checks, not a proof of torsionfreeness.

The relevant chain lemma and the selection and clearing of unit pivots are written in `RESULT.md` and implemented directly in `certificate.py`. There are no sample-only or random verification stages, omitted cells, runtime-dependent external input files, or delegated numerical assumptions. The public scientific assertion is restricted to the exact finite group action and its integral homology, two-connectivity, and non-shellability. Independently reproduced mathematics is not claimed.
