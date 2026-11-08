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

# Exact verification and limits

Run `python3 verify.py` using Python 3 standard library. A successful execution prints `VERIFY_OK` and the exact counters described below.

The checker independently constructs the minimal zero-sum residue atom patterns, uses recursive vector factorization over all admissible \((a,b,c)\) with total weight at most \(24\), and compares the possible length sets to the four-threshold decision rule: \(735\) distinct profiles pass. It separately factors every positive integer \(\equiv1\pmod {10}\) and at most \(200000\) by exact integer divisibility, obtaining \(19999\) nonidentity elements, with first unequal-length instance \(75411\) and length set \(\{2,3\}\). The exact identity \(81\cdot931=21\cdot21\cdot171=75411\) and the four prime-product lower bounds are checked.

The code's finite cutoff does not prove the statement for all parameters. The unrestricted argument is the six-pattern zero-sum classification plus the length equation, parity, necessity/sufficiency relations and prime-minimum inequalities in `RESULT.md`. None of these steps relies on numerical extrapolation or on results from an unexecuted certificate.
