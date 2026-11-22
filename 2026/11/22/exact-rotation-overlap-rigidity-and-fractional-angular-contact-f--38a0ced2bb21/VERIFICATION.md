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

# Verification of the rotated Lamé-region intersection theorem

The mathematical proof is self-contained in `RESULT.md`. The standalone artifact `CHECK.py` runs with Python 3 and its standard library only:

```sh
python CHECK.py
```

For the recorded calculation it printed:

```text
PASS 163 diagnostics
astroid right-angle-period overlap minimum 0.845064236407054
astroid small-angle correction 2.267857889810772
```

The script forms the two-dimensional polar-overlap integral directly as a midpoint sum and independently forms the crossing-split formula as a combination of one-dimensional midpoint integrals. It tests five exponents (including a nonconvex astroid exponent, the diamond, and two strictly convex noncircular cases), seven angles, the symmetries, strictly decreasing grids, and the elementary astroid antiderivative. It also checks small-angle ratios at moderate powers where finite-precision quadrature is well-conditioned. All tests are finite numerical diagnostics, not a substitute for the proof for every exponent and angle.

The crucial non-numerical checks are (a) radial squared function \(f_p\) and fourfold period, (b) exact crossings of cyclic symmetric decreases, (c) derivative sign for strictly decreasing \(f_p\), (d) integration of the cusp expansion to obtain the \(2^{2-p}/[p(p+1)]\) coefficient, and (e) the astroid substitution \(u=(\tan t)^{1/3}\). The theorem's \(O_p(\eta^4)\) remainder is local to a smooth interior angular point; the near-alignment remainder is only pointwise in \(p\). No external certification is asserted.
