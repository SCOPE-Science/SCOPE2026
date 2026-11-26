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

The affine image of an equilateral triangle gives the Steiner ellipses; their squared-axis ratio is the eigenvalue ratio of the centered scatter matrix S. Its trace and determinant are Σ/3 and 4A_T²/3, and the circumradius-one area identity gives K=√3 ℓ12ℓ23ℓ31/Σ=2R/(1+R²). In particular K≤√3 d/2 for shortest chord d, so continuity through collisions after setting K=0 there rules them out as an additional near-circular locus. Equality K=1 means isotropic scatter, hence an equilateral triangle. Expanding the trace-free entry at the two labelled equilateral points gives eigenvalue contrast (2/3)√(u²+v²−uv)+O(u²+v²). With e²=2Q/(1+Q), both t²-scaled domains converge within a fixed bounded set to the indicated ellipse of area 9π/(8√3). The uniform angle density and two configurations give 3√3/(16π); convergence of the indicators off the ellipse boundary proves the marked TV result. Conversely K≥√3 d/6 by the triangle inequality, so R<η implies a shortest angular gap of size O(η). Assign the mark by the shortest pair (ties have probability zero). For a fixed scaled signed gap and third angle away from coincidence, R/η tends to √3 |Δ/η|/4 and the marked pair is uniquely shortest. In these coordinates the indicator vanishes outside a fixed compact scaled-gap strip; dominated convergence on this strip times the two angle circles gives L1 convergence, since the exceptional collision and window-boundary sets have measure zero. Each pair contributes 4/(π√3), with pair labels uniform by exchangeability; normalization gives independent uniform limiting gap and angles. Overall rotation in the circular regime is exactly uniform and independent. The substitution η=√(2t−t²) gives the flat eccentricity constant 4√6/π and widens the scaled gap interval by √2.

## originality

PASS

The supported distinct claim is the pair of sharp eccentricity tails and the marked conditional TV limits under iid circle-boundary sampling. The Steiner geometry and circle-triangle shape law are premises. No inspected independent theorem gives these asymptotics for this statistic; the closest indexed rare-shape laws use a different statistic or a different, non-equivalent sampling mechanism. The identical Resultary copy is not a separate finding.

## value

PASS

This is the extreme shape law for a canonical affine ellipse in a basic random cyclic polygon. The distinct powers, exact constants and marked limits distinguish concentration near two isolated equilateral shapes from three families of pair collisions with an unconditioned third-angle limit. The marks give information absent from a tail exponent alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
