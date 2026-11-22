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

The classical transfer-current determinantal identity Cov(X_e,X_f)=P_ee delta_ef-P_ef^2 with P=B^T (BB^T)^+ B reduces covariance to circulant Green-current kernels. Laplacian eigenvalue 3-2cos(pi k/n)-(-1)^k separates odd massive antiperiodic sector O_d from even cycle sector. The exact O,H,T formulas generate rim/rim, chord/chord and cross covariances and diagonalize under Fourier transform into scalar odd modes and the stated Hermitian 2x2 blocks. All fixed-size spanning trees have 2n-1 edges; exchange along overlapping four-cycles connects all edge costs, giving one-dimensional covariance kernel, not inferred merely from finite eigenvalues. In the uniform n->infinity nonzero even modes the limiting block has eigenvalues A=1/(2sqrt3), L(theta)=3a(theta)-A, with L>=0 and a unique quadratic zero at theta=0. The finite correction (1/2n)diag(1,0) acts on the lower eigenvector with rim weight p(theta)>=2/3, yielding min 1/(3n)+O(n^-2); all other modes remain bounded and max tends to A. I independently built actual oriented incidence matrices and pseudoinverse currents for n=3,4,6,9,20; the explicit covariance differs by <4e-16 and exactly one eigenvalue vanishes. A separate 2n FFT computation for n=64..1024 showed n lambda_min approaching 1/3 and max approaching 1/(2sqrt3). These are finite corroborations; the proof requires the uniform symbol error O(n alpha^n) and spectral perturbation.

## originality

PASS

Transfer currents, graph Laplacian pseudoinverses and tree enumeration are classical; Azimi–Farrokhi explicitly compute Möbius ladder Laplacian inverse, resistance and tree numbers. Those inputs do not assert the full edge covariance Fourier spectrum or the first-order small eigenvalue induced by a finite-size topological correction; compared published SCOPE squared-cycle and wheel results concern distinct graphs and constants. Historical structure-factor literature still presents residual priority risk.

## value

PASS

Uniform spanning-tree edge observability is a natural Fourier-covariance invariant of a canonical 3-regular nonplanar twisted cycle family. The exact 3n spectrum and sharp linear condition coefficient distinguish a meaningful topological finite-size near-null mode from wheel and squared-cycle behavior and provide a reusable exact benchmark. It is not just the known tree count or resistances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
