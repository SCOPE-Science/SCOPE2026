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

The theorem follows from algebraically exact finite chamber enumeration plus spherical excess for all generic directions. Run `python3 verify_dodecahedron.py`; no external packages are used. The checker covers 20 distinct vertex coordinate tuples, 30 edges of squared length 16 in the chosen normalization, 10 antipodal vertex axes, all 90 crossings of axis-orthogonal great circles, and all 92 positive-area sign chambers. Each chamber is classified by its section-crossed-edge count, spherical corner count, and the full exact corner-angle cosine multiset. The expected positive confirmation lines are `DODECAHEDRON_EXACT_ARRANGEMENT_OK`, `DODECAHEDRON_EXACT_SECTION_TYPES_OK`, and `DODECAHEDRON_EXACT_ANGLE_SIGNATURES_OK`.

The formulas \(\Omega=2\pi-\sum\arccos\langle w_i,w_j\rangle\) and \(\Pr(N=k)=m_k\Omega_k/(4\pi)\) convert exact finite geometry to the continuum probability theorem. A separate edgewise angle-separation identity recovers \(\mathbb E[N]=30\arccos(\sqrt5/3)/\pi\), agreeing with the distribution. Floating-point decimals and Monte Carlo corroboration are not used as proof of any all-direction assertion.

Limitations: exceptional viewing directions have measure zero and are not classified. The exact checker is a reproducible finite mathematical certificate, not independent external certification. An independent audit has not been performed.
