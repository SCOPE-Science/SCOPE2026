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

# Reproduction and limits

The central infinite argument uses the exact Legendre differential equation, the exact generating function for Legendre polynomials, the resulting \(O(\log(n+1)/n)\) bound on an oscillatory integral, and the classical fixed-interior-angle asymptotic (DLMF §18.15). Every omitted constant in the proof is independent of degree for each fixed \(0<c<\pi\). No finite coefficient enumeration substitutes for the infinite asymptotic argument.

To reproduce selected finite checks, execute `python verify_numeric.py` using Python's standard library. The script compares the integral defining \(I_n(c)\) against the exact integration-by-parts expression for selected degrees and cutoffs, and confirms both coefficient signs for selected degrees. It reports 21 supplementary assertions passing on a standard Python numerical environment. These tests are illustrative, not a proof of universal positive definiteness or infinitely many negative coefficients.

The argument does not determine any least negative harmonic degree, a uniform endpoint asymptotic as the cutoff varies, or independent confirmation of mathematical priority. No independent audit has been performed.
