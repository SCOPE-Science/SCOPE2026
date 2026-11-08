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

# Verification and reproducibility

Run `python3 verify_oct_orlicz.py` in a Python 3 standard-library environment. It runs 5,000 exact rational checks of the four-factor product and elementary symmetric inequalities, followed by bisection of the one-variable boundary equations. On execution it printed `PASS 5000 exact rational Euler-factor comparisons; radii: 1.4738091812419376 1.5446294937642024`. The original proof also includes a symbolic coefficient expansion, and the full theorem for all real unit directions follows analytically from its polynomial identity, inequalities, and Euler product.

The directly computed boundary weights are \(\sqrt3/2\) square units of area and \(1/\sqrt3\) of support height on each of the eight facets; their product is \(1/2\). The numerical bisections verify the stated values to roughly twelve decimal places but cannot prove strict global optimality. That comes solely from the proof in RESULT.md. The equality cases include all signed permutations of the coordinate axes and all eight body diagonals; zero radius is deliberately excluded from uniqueness. The low-radius inequality is restricted to \(0<r\le2\), and no conclusion about the polyhedral covariogram limit follows from the source's smooth theorem.

No independent mathematical audit has been performed.
