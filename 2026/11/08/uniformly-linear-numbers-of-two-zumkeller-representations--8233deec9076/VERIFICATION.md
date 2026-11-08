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

# Reproducibility checks

Run `python3 check.py` using Python 3 and only its standard library. The source defines and checks exactly 44 odd residue-pairs (88 seeds) and 6 even seeds. For each candidate seed \(s\), it enumerates the complete divisor set and verifies whether \(\sigma(s)/2-s\) is obtainable by distinct proper divisors, using an exhaustive bitset subset-sum dynamic program. This is a finite proof check, not a heuristic sample.

The checker independently verifies all arithmetic relations between each residue pair: \(u_i\equiv v_i\equiv 2i-1\pmod{88}\) and \(11\nmid(v_i-u_i)/88\). It checks the endpoints of constructed representations at 964 even and 2,951 odd sample totals, including direct Zumkeller testing for small samples. Its expected output is included in `check_output.txt`.

Universal quantification over arbitrarily large target integers is supplied by the symbolic coprime-multiplier and residue-count arguments in `RESULT.md`, not by the sample range. No exact asymptotic constant, independent audit or external certification is claimed.
