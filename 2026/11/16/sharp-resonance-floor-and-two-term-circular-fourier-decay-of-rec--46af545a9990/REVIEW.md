# Self-review

## Correctness

**PASS.** The rectangle Fourier transform factorizes exactly. Two controlled endpoint expansions recover the leading axis contribution and the oscillatory Fresnel boundary-layer correction; a fixed interior arc contributes only \(O(R^{-4})\). The key nonstandard step is uniform-in-phase dominated convergence after scaling the endpoint by \(R^{-1/2}\), combined with averaging a nonstationary sine-square at frequency \(\asymp\sqrt R\). It yields an honest little-o remainder for arbitrary real radii. The exact liminf uses positivity of the leading coefficient and infinitely many simultaneous rational/continued-fraction approximations for the reverse inequality. Direct numerical quadrature is a supplementary sanity check, not an infinite proof.

## Originality

**PASS relative to inspected primary evidence, with historical-priority risk.** The 1997 polyhedra paper gives a square Fourier formula and order bounds; the 1998 planar convex-body paper gives enhanced square decay estimates along integer radii, but its relevant Lemma 3.12(ii) is one-sided and supplies no limiting constant. The 2003 theorem and the November 2026 motivating paper concern universal decay bounds rather than an exact rectangle-specific two-term expansion. The prior research-index searches uncovered geometric Fourier-zero, spherical harmonic and finite Fourier rectangle findings, but no equivalent all-radius formula or sharp arbitrary-aspect-ratio liminf. Related older diffraction literature remains a stated residual risk.

## Mathematical value

**PASS.** The known sharper-than-generic square decay along resonant radii motivates computing its *sharp nonzero coefficient*; the answer is not a generic \(R^{-3}\) estimate, a numerical fit, or a merely rescaled special square. The theorem addresses all rectangles, including irrational aspect ratios whose axes cannot resonate exactly, and distinguishes the universal oscillatory \(R^{-3}\) profile from the strictly positive \(R^{-7/2}\) resonance floor. It supplies a complete sharp asymptotic invariant for a natural convex Fourier-transform model.

## Closest literature and remaining limitations

The main comparisons are Brandolini–Colzani–Travaglini (1997), Brandolini–Rigoli–Travaglini (1998, Lemma 3.12), Brandolini–Hofmann–Iosevich (2003), and Iosevich–Merlo–Mourgoglou (2026, Theorem 1.1). Earlier optical/diffraction equivalents and uninspected translated literature could overlap. The theorem is parameterwise, planar, and not a general polygonal or higher-dimensional statement.

Self-review: passed. Independent audit: not yet performed.
