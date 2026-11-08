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

# Verification of the finding

The underlying assertion is proved for every integer \(m\ge3\) by the phase-interval characterization, cyclic transfer identity, isolated-run extremal argument, and polynomial reciprocity in `RESULT.md`. The two attached Python scripts implement finite, independently structured cross-checks; they are not a substitute for the unrestricted mathematical proof.

Run `python3 check_direct.py` to enumerate, for each \(m=3,4,5,6\), all bounded state vectors \(0\le x_v\le2d_v-1\), test the actual map twice and compare the resulting chip-mass counts with independent phase-interval counting. This tests exactly 649296 states and produces `check_direct.out`.

Run `python3 check_transfer.py` to compare two polynomial implementations (a four-state transfer trace difference and a direct binary cyclic-word product), for all integer rim sizes \(3\le m\le12\). The test checks exact coefficient arrays, support, endpoints, reflection symmetry and totals and produces `check_transfer.out`.

Both tests were performed using their actual source paths before packaging, with successful outputs captured in the attached text files. Neither test asserts exhaustivity for larger rim lengths. The proof covers that range algebraically, without dependence on test extrapolation. No independent audit has been performed.
