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

# Reproduction of the finite certificates

`verify/transfer.py` builds the seven allowed vertical columns, constructs the weighted adjacency matrix, checks the claimed bivariate determinant identity symbolically over integer polynomials, factors the unweighted characteristic polynomial and verifies counts through circumference twelve. It checks the rational root bracket and computes the asymptotic occupied-site fraction by differentiation of the exact determinant. Run with `python verify/transfer.py` using SymPy.

`verify/brute.cpp` independently constructs every three-symbol labelled configuration on width-two periodic strips of horizontal circumference three through seven, evolves eastbound cars simultaneously and then northbound cars simultaneously, and checks the resulting frozen count, mixed-species count and vacancy-containing count. Compile with `g++ -std=c++17 -O2 -Wall -Wextra verify/brute.cpp -o brute` and execute `./brute`.

`verify/transfer_output.txt` and `verify/brute_output.txt` contain the output of the supplied programs on the checked version of the package. The finite exhaustive checks corroborate the definition and numerical coefficients. The all-circumference and limiting statements depend on the mathematical transfer bijection, the formal determinant identity and the explicitly derived Perron-root argument, not on extrapolation from these samples.

The BML rule is taken with periodic boundaries and an east substep followed by a north substep. All calculations use exact symbolic arithmetic except the clearly labelled approximations to the cubic root and limiting vacancy fraction. No externally performed independent audit is asserted.
