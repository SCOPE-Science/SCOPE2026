---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With α=2πk/5, actual arclength conservation gives the first-order endpoint shift −∫_θ^{θ+α}f. Projecting the varied difference vector onto the unperturbed unit chord contributes sin(α/2)(f(θ)+f(θ+α)) plus cos(α/2) times that endpoint shift; hence the stated Fourier symbol, killing ±1, and Parseval apply on the gauge slice. Exact fifth-root values give the strict lowest entries at n=7 for k=1 and n=6 for k=2. For n≥8 or n≥7 respectively, |cos(nα/2)|≥cos(2π/5), giving the displayed strict tails by sin(2π/5)>7/8 and >6/7. For the nonlinear estimate, write the speed as 1+f+E with |E|≤C(f′)² and ∥E∥₁≤C∥f∥₂∥f″∥₂ by periodic integration by parts. Inverting the positive speed primitive gives the shift uniformly O(∥f∥₂) and its error relative to −∫f uniformly O(∥f∥C²∥f∥₂). The radial shift error is bounded by ∥f′∥∞ times the shift, and the chord-norm Taylor error has the same relative L² bound because the unperturbed chord is nonzero. Angular mean subtraction is an orthogonal contraction. The curvature numerator stays positive for small C² norm; the pure real extremal frequencies show first-order sharpness, without an assertion about finite-amplitude equality.

## originality

PASS

The distinct result is the sharp pentagonal L² estimate for the variable chord profile, including exact optimal first-order constants and their different equality frequencies, with a relative C²-to-L² remainder. Neither qualitative pentagonal rigidity nor the underlying linearized symbol is distinct. The symbol already occurs in equivalent form in a related tangent-angle record, and its numerator occurs in the linearized equation for equal chords in the primary pentagonal paper.

## value

PASS

This measures the smallest detectable departure from equal chords in a natural pair of arclength sampling schemes. The two fractions both give global qualitative uniqueness, but have genuinely different slow modes and sharp local recovery factors. The exact leading constants and relative nonlinear error quantify that difference for perturbed curves, rather than merely repeating a no-kernel result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
