---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Unitary Fourier analysis pairs k and k+N/2 under alternate-vertex restriction, giving orthogonal blocks Q_δ=1/sqrt2[[1,1],[e^{-(2-δ)t},e^{-(2+δ)t}]], δ=2|cos(2πk/N)|; no hidden normalization factor appears for counting-measure norms. The Gram trace and determinant for sqrt2 Q are T=2+2q cosh(2δt), D=2q(cosh(2δt)-1), q=e^{-4t}, and T′=D′>0. Their eigenvalues straddle 1, so both branches grow with δ; min δ=0 iff 4|N, otherwise 2sin(π/N), while max δ=2. The resulting exact A_N and B_N follow by quadratic roots. A_N/d_N²→h(t)=t²/(1+e^{4t}) compact-uniformly, and Rayleigh upper envelope A_N/d_N²<=t²e^{-2t} excludes maximizers at t→0 or infinity. The unique positive maximizer solves 2τ=1+e^{-4τ}, and N d_N→2π gives the constant. Independently rebuilt full complex cycle heat matrices for N=4..20 (even) and five t values, verifying 45 exact Gram extrema within 2e-12. Universal and limit assertions rely on proof not tests.

## originality

PASS

Operator-frame existence and bandlimited-flow observability sources give general criteria and Fourier blind spots but do not state the exact finite even-cycle half-sensor two-time Gram extrema, the modulo-four obstruction, or best-delay limit. A published Resultary result on the infinite integer lattice optimizes a spectral-notch two-time frame and has different domain and scaling; another on a cycle uses two sensors and only the first three Fourier modes. Those do not imply the full-spectrum half-sensor bound by specialization. Specific literature with other normalizations may be overlooked; best-of-knowledge only.

## value

PASS

Sharp recovery stability for fixed sparse sensors is a mathematically motivated experimental-design invariant. The exact parity phase boundary, upper/lower sharp bounds, and a universal time-optimal scaling resolve the full finite-cycle family with nontrivial Fourier alias analysis and a controlled optimizing limit, not a table or a routine frame-existence restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
