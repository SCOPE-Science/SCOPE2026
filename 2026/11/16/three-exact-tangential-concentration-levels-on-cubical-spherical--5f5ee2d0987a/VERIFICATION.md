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

For probability sphere S^{d−1} and single positive coordinate-maximal cell C_d, gradients G_i=e_i−x_i x and rotations K_ij=x_i e_j−x_j e_i form full orthogonal normalized vector tangent system of dimension d(d+1)/2. Signed-permutation invariance and moments s_d=E(max_i |X_i|), t_d=E(max_i|X_i|²) give a direct sum of one scalar λ0=(1−t_d)/(2(d−1)) of multiplicity 1+C(d−1,2) and d−1 identical 2×2 real symmetric blocks with a=(d−2+t_d)/(2(d−1)^2), b=(1+(d−2)t_d)/(4(d−1)), c=s_d/(2√(2(d−1))). Strict λ−<λ0<λ+ follows from identity (d−1)s_d−(dt_d−1)=E[(1−M)(dM+1)]>0 and determinant sign. Gaussian radius independence gives explicit univariate erf integrals. Normal Gaussian maximum tail estimates and variance→0 imply λ+~log(d)/(2d), λ0~1/(2d), λ−~1/(4d log d), sharp ratio ~2(log d)^2. Independently integrated moments and checked trace, eigenvalue ordering and d=2,3,4,6,100 numerical values, including d3 0.004813332/0.074778517/0.420408150; finite checks corroborate the analytical proof.

## originality

PASS

The general vector Slepian framework of Plattner–Simons and Michel–Plattner–Seibert covers construction of concentration matrices but does not evaluate a single signed coordinate-dominant cubical cell in every dimension or determine three ordered blocks and Gaussian-max edge asymptotics. A closely relevant published Resultary theorem concerns the identical cubical cell but the scalar pure degree-two harmonic space and a four-branch spectrum; its same leading condition-number growth does not determine the vector tangent spectrum. Best-of-knowledge novelty of exact tangent mixed first moments and full-dimensional formula survives.

## value

PASS

The cubical signed-coordinate cells are natural equal-measure domains from cubed-sphere geometry. The exact tangent first-order gradient/rotation spectral decomposition, strict ordering, dimension-dependent condition numbers, and sharp Gaussian-max growth provide a self-contained structural solution to observing a natural vector harmonic space; neither trivial restatement nor arbitrary small sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
