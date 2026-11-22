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

For a closed rectifiable arclength S² two-design, the H¹ constant-speed F=√3 γ has zero mean, covariance I₃ and |F|²≡3. Orthogonal Fourier projection F=F₁+F₂+R with a+b+c=3 and first/second band covariance ranks ≤2 yields ε=3(L/2π)²−6≥3(2−a)+5c. The fourth-harmonic amplitude of |F₂|² is λ₁(K)−λ₂(K)≥b−2(2−a)≥1−ε/3 by the two-plane trace/eigenvalue principle for U+K+H=I; |F|²≡3 forces that harmonic to be canceled by 2(F₁+F₂)·R+|R|², so amplitude ≤4√(3c)+2c≤4√(3ε/5)+2ε/5. Hence 1≤11ε/15+4√(3ε/5), giving ε≥(1245−180√47)/121 and L≥2π√((1971−180√47)/363)=8.9527209263…; the strict excess over 2π√2 is a genuine uniform positive gap. Eigenvalue inequality and Fourier constants were checked against actual RESULT.md and verify.py. This argument treats every admissible H¹ arclength parameterization, not a finite family or smooth-only subclass.

## originality

PASS

The identified King–Mixon primary theorem gives only 2π√2 on S² at strength two; it does not imply a strictly positive uniform gap of ~0.066955. The new Fourier fourth-harmonic obstruction is a distinct quantitative geometric ingredient. No stronger or equivalent prior theorem was established by the searches, but the closest paper full text was not accessible, so this is a best-of-knowledge PASS with an explicit material historical-priority risk.

## value

PASS

This is not an arbitrary ~0.75% numerical improvement: the prior spectral lower bound was a possibly approached infimum in the unsolved shortest S² two-design curve problem. The proof identifies a structural fourth-harmonic obstruction and proves a uniform nonattainment margin. That rules out sequences of exact designs converging to the spectral value. The independent fact is useful even without an optimal length or minimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
