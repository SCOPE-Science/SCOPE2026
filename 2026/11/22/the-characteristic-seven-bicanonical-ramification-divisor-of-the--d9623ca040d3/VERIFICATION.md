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

The exact characteristic-seven computation was run with Python 3 and SymPy using only rational functions over \(\mathbb F_7(x)\). The verified identities are
\[a_3^2-a_2a_4=5x^2/(1+x^4)^4,\quad\Delta_5=\Delta_6=0,\quad\Delta_7=x^3(x^{24}-1)/(1+x^4)^{14}.\]
The scripts emit `FERMAT7_WRONSKIAN_SYMBOLIC_OK` and `FERMAT7_ARITHMETIC_COUNTS_OK`. The second checks the two separately defined support strata: eight plus zero rational points over \(\mathbb F_7\), eighty plus twelve over \(\mathbb F_{49}\). Their weighted sum is \(116\). Independent full curve-point enumeration over both fields gives \(8\) and \(92\), agreeing with the divisor support; the latter also attains the Hasse–Weil upper bound.

The formal-series determinant and the global ramification degree, not the finite enumeration alone, establish the full geometric divisor. No proof of an analogous statement outside characteristic seven is attempted. The inaccessible older primary paper and the absence of independent external review limit historical-priority and external-certification claims.
