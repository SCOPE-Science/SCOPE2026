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

The invariant-state proof in `RESULT.md` supplies the all-parameter assertion. The standalone checks implement the original bit-level closed-neighborhood update without using the abstract grid translation for the actual successor.

Run `python3 check_symbolic.py`. The program checks every announced invariant state and expected successor for all integer parameters from 2 through 70, totaling 126,730 explicit successor checks. It also checks that the predicted transition map traverses the complete invariant set in exactly the stipulated least period. Reproduction output is `symbolic_output.txt`.

Compile `exhaustive_cycles.cpp` using a C++17 compiler with `-O3` and run the resulting executable. This independently computes complete finite functional-graph censuses on both graph versions for parameters 2, 3, 4, and 5, examining at most 4,194,304 binary configurations per graph; it confirms one primitive orbit of the theorem's length for each. Reproduction output is `exhaustive_output.txt`.

The checks neither establish exhaustive uniqueness for unbounded parameters nor substitute for the proof of the uniform symbolic transition table. Numerical checks end at parameter 70 for the first program and at parameter 5 for the second. No independent mathematical audit is claimed.
