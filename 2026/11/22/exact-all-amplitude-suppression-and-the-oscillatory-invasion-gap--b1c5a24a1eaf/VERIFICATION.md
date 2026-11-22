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

The proof is analytic. Reconstruct its key computations directly: differentiate \(H=\delta(N-\log N)+D-\log D\); integrate \((\log D)'\) to obtain \(\langle N\rangle_T=1\); differentiate \(z=B_vh/y-1\) to obtain the Riccati equation; and integrate to obtain the stated variance identity. The equality case at \(\kappa=g\) must use the separate compact-state invariant-set argument and is not claimed exponential.

For an independent numerical diagnostic, install NumPy and SciPy and run `python3 verify_vector_cycle.py`. The script checks six ecological amplitudes, a two-by-two monodromy crossing, the exact Riccati mean-square balance at its crossing, and agreement with the quadratic small-amplitude coefficient \(3/22\) at \(g=3/2\), \(\delta=2\). Finite-precision checks cannot prove the all-amplitude theorem, the monotonic crossing or the global nonlinear result. Numerical tolerances are explicit in the script.

Scientific review passed on correctness, bounded originality and value. No external or independent validation was performed.
