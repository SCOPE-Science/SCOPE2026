# Scientific review: smooth minimum-degree filling curves on a split quadric

## Correctness — PASS

The theorem is exactly quantified over all bidegree-\((4,3)\) sections of \(\mathcal O(4,3)\) on \(\mathbb P^1\times\mathbb P^1\) over \(\mathbb F_2\) that vanish on all nine rational points. The nine evaluation constraints have rank nine, leaving \(2048\) binary sections. The 2047 nonzero sections form 99 orbits under the 36 ruling-preserving automorphisms. A Gröbner-basis Jacobian test in all four affine charts identifies four smooth orbits with sizes \(6,18,36,6\); direct lexicographic elimination on all 2047 forms independently yields 66 smooth equations. Smoothness implies geometric irreducibility, and the adjunction genus is six. Computation of the four stabilizers, point counts through degree six, and all Weil coefficients is exact, with a second finite-field implementation agreeing on every point count.

The findings do not claim to classify abstract isomorphism classes or stabilizers in the full abstract automorphism group, and pairwise nonisogeny is asserted only over the base field. The finite certificate and reproducible programs substantiate this bounded exhaustive theorem; no extrapolation is used.

## Originality — PASS with residual historical-priority risk

Homma and Kim, arXiv:2203.11595 (March 22, 2022), determine the minimum bidegree and construct a particular smooth filling curve; they do not enumerate the smooth bidegree-\((4,3)\) locus or its arithmetic classes. Their explicit form has coefficient mask `429846` and is included in the size-18 class of the present theorem. The later Ahammed–Campbell–Moon preprint, arXiv:2512.02796 (December 2025), studies smoothness criteria and computer counts for other field sizes and gives no classification of the exceptional \(\mathbb F_2\) bidegree-\((4,3)\) locus. The plane-filling work of Asgarli and Ghioca, arXiv:2307.03072 (July 2023), addresses \(\mathbb P^2\) rather than the split quadric. Searches of accessible research records and historical claims found no covering count, orbit classification or four Weil polynomials. An unindexed earlier classification remains a real priority risk; absence from searches is not a proof of novelty.

## Mathematical value — PASS

The degree-seven split-quadric filling problem is an explicitly motivated extremal small-field case: earlier research establishes existence but not the full smooth locus. The exact enumeration replaces a single example by the entire natural parameter space, distinguishes four genuine projective-geometric types through their ruling-preserving stabilizers, and shows that each type has a different Jacobian isogeny class. The four Weil polynomials are arithmetically substantive invariants, not merely restatements of orbit sizes. These facts can support comparison of minimum-degree filling constructions and finite-field moduli in higher degree or characteristic.

## Sources and limitations

Primary comparisons: Homma–Kim, *Filling curves for \(\mathbb P^1\times\mathbb P^1\)*, arXiv:2203.11595 (especially Sections 2, 4); Ahammed–Campbell–Moon, *Minimal algebraic space filling curves on the product of projective lines*, arXiv:2512.02796 (Sections 3–5). Context: Asgarli–Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072. The exact proof relies on executable Gröbner elimination and finite-field counts, not an entirely handwritten orbit table. Potential older finite-geometry classifications outside indexed sources remain possible.

Self-review: passed. Independent audit: not yet performed.
