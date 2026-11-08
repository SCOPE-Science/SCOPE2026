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

# Verification of the three-band phase-coherence theorem

The proof uses exact Fubini expansion of the centered time-limiting form, a two-small-packet limit to force each sinc sign, a connectedness argument to make the template bandwise constant, and simultaneous integer-lobe inequalities. In dimensionless parameters, adjacent bands require \(k+\delta\le x\le k+1-\delta\); outer-band sign balance requires \(2(x-k)+\delta\le1\). Their intersection is nonempty precisely when \(\delta\le1/3\). The endpoint \(x=\delta\) with \(k=0\) is excluded by strict band separation.

Run `python checks/three_band_phase.py` from the package root with Python 3 and NumPy. A successful run prints `THREE_BAND_PHASE_DIAGRAM_PASS 20000` and `THREE_BAND_NUMERICS_PASS`. The 20,000 numerical parameter comparisons and sampled quadratic forms are consistency checks only; they are not an exhaustive certificate of a continuum problem. The proof supplies the required infinite-dimensional quantifiers.

The analysis covers centered time windows, exactly three equal-length equally spaced disjoint Fourier intervals, and a template which is independent of the prescribed nonnegative Fourier magnitude. It does not establish a best phase for every individual magnitude outside coherence windows, nor an optimal numerical coercivity coefficient. No independent mathematical review has been performed.
