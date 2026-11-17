---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Weyl diagonalization makes 25 singular values of complete lifting exactly √5|Ag(k,ℓ)|, so κ=1/min|Ag| and σmax=√5. Every 3-subset of Z5 is affine-equivalent to {0,1,2}. At lag 2 the minimum is uw; at lag1 the five equally-spaced phases guarantee minℓ|u+w e^{iδ−2πiℓ/5}|² ≤u²+w²−2uw cos(π/5), with equality precisely fifth-root phase curvature. Setting s=uw, t=v², the completed-square bound μ≤min{s,(1−φs)/2}≤α=(5−√5)/10 is sharp iff s=t=α and indicated endpoint squared magnitudes. The remaining zero-lag Fourier coefficients have squared moduli 1, √5/5, (3√5−5)/10, all >α², so no overlooked obstruction. Two-site ambiguity lacks some lag rows. Direct real/complex Gram numerical reconstruction confirms κ=(5+√5)/2 for explicit equalizers, but global optimality comes from inequality.

## originality

PASS

PASS best of knowledge: Weyl and nonzero ambiguity criteria and lower support threshold are already known; unlike those general papers, this gives exact best conditioning and every complex-amplitude, support, phase equality case under 25 full Gabor shifts on Z5. The computed invariant is a natural minimax quantity, not a known table restatement.

## value

PASS

PASS: This determines an exact, physically motivated, minimum-support five-cycle Gabor measurement conditioning invariant and classifies all complex optimal masks, including the nontrivial asymmetric magnitudes and phase curvature. The finite natural design result is independently useful; no claim of a complete higher-prime census or downstream general theorem is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
