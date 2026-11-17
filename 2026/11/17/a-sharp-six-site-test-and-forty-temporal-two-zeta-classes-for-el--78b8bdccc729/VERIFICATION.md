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

# Verification protocol and boundaries

The exact proof constructs two de Bruijn-type transfer graphs with four and sixteen vertices, respectively. Its all-length conclusions follow from the closed-walk bijection and from an exact strong-component test on the sixteen-state graph, **not** from extrapolating the six-site experimental search. A marked edge in a directed cycle is equivalent to a primitive temporal two-cycle, even when the shortest marked cycle is longer than the smallest observed witness.

Run `python3 verify_scc.py` to check all 256 rule decisions and the sharp witness distribution using only the Python standard library. Run `python3 verify_zeta.py` with SymPy installed to check all 256 exact characteristic polynomials and separately compare fixed-point and two-step traces with direct state updates at every spatial length one through nine. The reference outputs are `verify_scc.out` and `verify_zeta.out`.

The accompanying `rule_table.csv` has 256 data rows in Wolfram rule order. Polynomial coefficients are listed in increasing powers of the formal variable, separated by semicolons; an absent primitive two-cycle is recorded as `none`. The full classification remains computationally reproducible and has not undergone an independent mathematical audit or third-party certification.
