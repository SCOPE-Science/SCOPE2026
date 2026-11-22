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

# Mathematical verification

The derivation can be checked by substituting the Klein-disk side equation into hyperbolic polar area and evaluating the inverse-sine primitive. This gives the exact area normalizer \((n-2)\pi\) without external numerical inputs. The conditional cusp-mark density integrates to one because \(\int_0^1(z^{-1/2}-1)\,dz=1\), and the many-side limit integrates to one because \(\int_{-1}^1(\pi\sqrt{1-u^2})^{-1}du=1\). Those two identities are the normalization premises for the total-variation limits.

Reproduce the independent numerical diagnostics using Python 3's standard library:

`python3 checks/check_radial.py`

Observed result: `ALL_CHECKS_PASSED; max_direct_quadrature_error=4.05e-12`. The script independently integrates the endpoint-singular polar region, checks branch matching, fixed-polygon rare-distance coefficients and centered large-polygon survival laws. The complete mathematical proof is in RESULT.md. Numerical tests do not establish infinite asymptotics, originality, or independent certification.
