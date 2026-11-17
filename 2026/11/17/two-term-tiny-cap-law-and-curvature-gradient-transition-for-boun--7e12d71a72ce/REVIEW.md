# Scientific review

## Correctness — PASS
For a positively curved \(C^8\) oval, the exact tangent-determinant double integral produces a uniform local cap-area expansion. Uniform inversion and the exact endpoint-to-signed-midpoint Jacobian yield the two probability coefficients, including the \(t\)-term \(2(2\pi-J)/(5P^2)\). The curvature-radius harmonic family closes for all \(m\ge2\); its gradient integral is exactly \(2\pi m^2((1-\varepsilon^2)^{-1/2}-1)\). The conditional gap representation and Scheffé's lemma establish total-variation convergence. The arclength-labelled inverse follows from the turning-angle theorem. A separate Green-theorem and quadrature checker gives `SMOOTH_CAP_AREA_CHECKS_OK`. The exact circle case and dimensional scaling were checked. No finite numerical test is treated as a proof.

## Originality — PASS (best-knowledge, provisional priority)
The closest source family addresses random hulls from interior points (Bárány–Fodor–Vígh, 2009; Pardon, 2010), deterministic affine equal-area polygons (Craizer–Teixeira–da Silva, 2011), and invariant-line chord lengths in polygons (Bäsel, 2012). A published three-point rare-triangle-area law has exponent \(2/3\), not the present two-point cap exponent \(1/3\). A published smooth short-chord distance expansion involves \(\int\kappa^4\) and \(\int(\kappa')^2\), but not this cap area correction \(\int(\kappa')^2/\kappa^3\). A known polygonal smaller-cut distribution has an atom and positive \(t\log(1/t)\) regime. These do not imply the new exact second coefficient, the harmonic sign threshold, or the marked inverse law. Potential equivalent forms in older unindexed integral geometry remain a priority risk. Ren's 2014 random-line paper was available only in abstract.

## Mathematical value — PASS
Random chords that cut extremely small fragments are important in stochastic convexity, boundary sampling and geometric reconstruction. The result provides a two-term, shape-sensitive law, a sharp circle extremum, a sign-changing first correction under explicit smooth perturbations, and a location-mark inverse determination of the entire arclength-labelled curvature. These are natural exact geometric invariants, not merely a numerical constant or a substitution in an existing chord-length formula.

## Scope and limitations
All assertions concern fixed \(C^8\) strictly positively curved compact plane convex bodies and independent uniform boundary-arclength samples. Error constants need not be uniform as the curvature oscillates. The inverse requires arclength-labelled locations, not a scalar probability alone. A mathematical priority and correctness audit independent of this review has not yet been performed.

Self-review: passed. Independent audit: not yet performed.
