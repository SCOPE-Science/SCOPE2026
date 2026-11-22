---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. The four-state pair transition B bijects closed length-n walks to uniformly sampled labeled cyclic binary words avoiding 000 and 111; no necklace quotient is taken. Complement symmetry splits B into the Fibonacci even block E=[[0,1],[1,1]] and the period-three odd block O=[[0,1],[-1,-1]], and the spin insertion swaps sectors. Thus Z_n=L_n+2cos(2*pi*n/3), the explicit H_r lag formula and Fourier/circulant eigenvalues follow exactly. n=3 has three positive eigenvalues; n=4 has one zero constant mode. For all n>=5, the explicit rotatable admissible single-coordinate flip witnesses force every coefficient of a hypothetical constant linear spin form to vanish, so covariance is positive definite. Perron/subdominant transfer eigenvalues yield uniform O(n phi^-n) Fourier convergence to S(theta)=(2/sqrt(5))/(1+sqrt(5)cos(theta)+2cos²(theta)); minimizing its positive quadratic denominator gives unique minimum theta=0, two maximizing frequencies cos(theta)=-sqrt(5)/4, and ratio 8+8sqrt(5)/3. Independently enumerated all admissible labeled words for n=3..12; exact word counts, lag covariances and ranks agreed. Enumeration is corroboration, not the all-n proof.

## originality

PASS

Best-of-knowledge PASS on distinct scientific statement/implication comparisons and primary evidence, with explicit source-access and index limitations. Cyclic binary run-two Fourier covariance with isolated n=4 null mode

## value

PASS

PASS. Uniform finite circular two-run constrained words are a canonical finite-state model in homopolymer-limited coding. Their covariance rank determines coordinate identifiability, with an unusual single length-four defect, while their precise Fourier eigenvalues measure reconstruction conditioning for every length. It is a natural complete spectral classification, not just an asymptotic transfer-matrix exercise; infinite stationary PSD methodology is explicitly prior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
