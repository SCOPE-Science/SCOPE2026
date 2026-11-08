# Review: exact inverse-valence phase diagram

## Correctness — PASS

The proof explicitly parametrizes all quadrant branches by nonnegative input magnitudes and solves four independent two-by-two linear systems. For \(c\ne a\) the image cone inequalities are necessary and sufficient and the determinant factors are nonzero. The positive-ray fan rotates its cyclic order exactly at \(c=a\). For \(c<a\) its four sectors partition the whole plane; for \(c>a\) overlapping sectors have the claimed multiplicities, with duplicate axis solutions merged precisely at the ray boundaries. At equality, two quadrant images collapse, yielding exactly the described infinite fibers. Direct formula verification includes every output boundary and strict inequality. The rational checker returns `VERIFY_OK checks=11617`; it corroborates, rather than proves, the universal result.

## Originality — PASS within the investigated literature

Tikjha's arXiv:2607.13519v1 supplies the map, the four linear branches, and the degenerate \(c=a\) case, concentrating on attracting cycles and bifurcations. The full accessible preprint was inspected through its conclusion and appendices; the present exact all-target multiplicity stratification and fourfold sector are not stated. Gardini–Tikjha (2020) contains a zero/two inverse count for a *different two-quadrant* map, not the four-branch map here. Poggiolini–Spadini (2013, 2018) provide generic homeomorphism criteria and therefore cover the orientation-preserving/reversing one-to-one subcase in principle. They are acknowledged; the valued new conclusion is the **simultaneous full classification of two-, three-, four- and continuum-valent fibers**, not the known general invertibility criterion. Specific earlier computations of the exact four-partition valence table remain a priority risk.

## Value — PASS

The preimage multiplicity, its critical rays, and the invertible-to-folded transition are natural topological invariants for the published noninvertible system: they determine where distinct backwards orbit branches are possible and separate generic loss of surjectivity from singular collapse. A fourfold inverse region is genuinely absent in the source's two-branch predecessor. The exact global partition is a finite but **complete natural classification** of all targets and all positive parameter ratios, rather than an arbitrary finite sample or simple restatement of local determinant vanishing. It furnishes a structural foundation for future studies of backward invariant sets and basin boundaries, while making no unsupported theorem about those objects.

## Sources and limitations

Closest references: Tikjha, arXiv:2607.13519v1 (full accessible original); Gardini–Tikjha, Chaos Solitons & Fractals 137 (2020) 109813 (full accessible original, different map); Poggiolini–Spadini (2013, 2018), general planar invertibility criteria (2018 abstract and available introduction inspected, full text access restricted). A published record on five-valued harmonic Landau shears was also compared by its abstract and pertains to a different analytic map. No assertion of broad literature uniqueness or independent proof certification is made. Parameter signs outside the positive quadrant are not covered.

Self-review: passed. Independent audit: not yet performed.
