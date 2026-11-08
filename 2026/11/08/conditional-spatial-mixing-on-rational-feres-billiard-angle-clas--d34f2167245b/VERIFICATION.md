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

# Verification notes

The analytic proof uses the four explicit Feres transition branches and their positive intervals. The graph is enumerated for arbitrary \(N\) by symbolic indices, not by computational enumeration. Edgewise detailed balance supplies the explicit stationary weights. The two positive length-two return loops have displacements \(4\theta+4\alpha\) and \(8\alpha\), respectively, and their phase conflict excludes spectral radius one for every fixed nonzero Fourier mode if \(\theta/\pi\) is irrational. This is the infinite-parameter argument.

The standalone `angles_check.py` is reproducible with Python 3 and NumPy. Run `python angles_check.py`. It checks graph state counts and degrees, probability normalization, reversible sine weights, a single cycle with \(N-2\) vertices after leaf removal, the odd/even period, and Fourier spectral radii for modes \(k=1,2,3,4\) for \(7\le N\le16\), at \(\theta=(\sqrt2/3)\alpha\). These finite checks passed; additional finite tests over \(7\le N\le30\) and other interior angles also passed when performed. They do not prove uniformity or the all-parameter claims.

A single point-source angle law yields finite supported boundary distributions at each finite time. Thus no convergence in total variation is claimed or established. The exact arithmetic obstruction for rational \(\theta/\pi\) is an elementary finite-subgroup argument. No independent mathematical audit has been conducted.
