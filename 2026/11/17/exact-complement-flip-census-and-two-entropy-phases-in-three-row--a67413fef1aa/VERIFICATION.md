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

# Verification

The claim concerns configurations \(x\) satisfying \(F_n(x)=\overline x\) on labelled three-row tori of circumference \(n\ge3\). The supplied exact finite-state certificate is the characteristic polynomial of the fully specified sixteen-state weighted transfer matrix. The matrix identity, local reduction, and trace formula together establish the all-circumference theorem. Direct enumeration is only a separate finite cross-check.

## Exact algebraic check

Run `python3 transfer_verify.py` with Python's standard library. It constructs \(T\) from the triple-weight rule, calculates the first sixteen exact integer traces, reconstructs every coefficient of \(\det(tI-T)\) using Newton identities, compares with the displayed factorization, and tests the resulting power-sum formula through circumference twenty. The recorded output ends `ALL_CHECKS_PASS`.

## Independently implemented update check

Compile and run `c++ -std=c++17 -O3 -Wall -Wextra direct_verify.cpp -o direct_verify && ./direct_verify`. The program enumerates all binary configurations on each \(3\times n\) torus for \(n=3,4,5,6,7\), applies the complete original eight-neighbor update, and verifies the all-flip count, the triple-window condition and the return after two steps. The recorded output ends `ALL_CHECKS_PASS`.

## Limits

The finite direct checks cover circumferences three through seven; they are not a proof about larger circumferences. The exact characteristic-polynomial certificate supplies the all-size step, based on the mathematical transfer equivalence. Neither program checks historical novelty or supplies independent external validation. The result does not count all period-two states or initial-state attraction basins.
