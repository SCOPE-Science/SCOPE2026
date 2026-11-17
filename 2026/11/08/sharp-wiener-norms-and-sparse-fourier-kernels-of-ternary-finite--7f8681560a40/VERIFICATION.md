---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Finite-field Gauss summation gives |S_r|=q²+εq and isotropic dual-level count q². Fourier inversion in b proves the exact Salié identity Σ_{t≠0}η(t)ψ(at+b/t)=η(a)GΣ_{v²=4ab}ψ(v). Completing quadratic squares yields F_r(ξ≠0)=qεΣ_{v²=rQ*(ξ)}ψ(v). For nonsquare level the sum vanishes; for square level it is a pair of cosines, never zero in odd characteristic. Multiplicities and the trace fiber sum give ||P||_{1→1}=||P||_{∞→∞}=(q+ε)C_p/p+(1−ε)/q−(1−ε)/q²; point masses and sign-alignment attain the two endpoint operator norms. Traceless Hermitian 2x2 idempotents are the ε=−1 nonzero shell, and the extra scalar axis repeats each kernel coefficient q times. Independent complete direct DFT enumeration at q=3,5,7 over prime fields for both ε sectors agreed to floating tolerance with exact shell and Fourier-zero counts, including q=3 values 16/9 and 8/3; no inference from finite data to all q.

## originality

PASS

Best of knowledge: Gauss/Salié transforms and finite-field extension estimates are standard, but the complete sharp endpoint absolute-Fourier norm for every nondegenerate three-variable nonzero shell, its exact two-class dependence on characteristic, and the Hermitian projector specialization are not implied by the inspected extension estimates. Other published finite-ring/support and Veronese records use distinct frequency sets.

## value

PASS

The ℓ1 norm of a natural finite-field quadratic-shell Fourier idempotent and its Hermitian orbit specialization are exact intrinsic harmonic-analysis invariants; all odd prime powers, exact zero support, and both sharp endpoint operator norms provide useful data for finite harmonic/spectral analysis rather than a textbook exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
