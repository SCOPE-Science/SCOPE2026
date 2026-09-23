# Independent three-axis audit — 2026-09-23

Source: `2026/09/08/029` in `SCOPE-Science/SCOPE2026`; audited source-tree SHA `5925d46d2bd51a5266030fb2a418a63eab443dbf`; `RESULT.md` blob `2351e75e4cefeea228830a29a8d2d56ae9db8ec0`.

## Claim checked
The record claims that every three-dimensional reflexive lattice polytope of normalized volume at most 12 has volume in exactly `{4,6,8,10,12}`, that every value occurs, that the consecutive-gap maximum is 2, and that every such polytope has `h*=(1,V/2-1,V/2-1,1)`.

## Correctness — passed
The core argument was rederived independently. Triangulating a reflexive 3-polytope from the unique interior origin expresses normalized volume as the sum of normalized facet areas because every facet is at lattice distance one. Pick's theorem makes each normalized facet area congruent to its boundary-lattice-point count mod 2; summing facet boundary counts counts every boundary edge lattice segment twice, hence the total normalized volume is even. A 3-polytope has at least four facets and every lattice facet has normalized area at least one, giving `V>=4`. Thus `V<=12` forces `V in {4,6,8,10,12}`. The five stated witnesses are standard reflexive simplex/bipyramid/crosspolytope constructions and realize those volumes. Hibi's reflexivity criterion gives palindromic degree-3 `h*`; with `h*_0=h*_3=1` and `sum h*_i=V`, one gets exactly `(1,V/2-1,V/2-1,1)`. No correctness defect was found.

## Originality — limited / not independently established as a new result
Kreuzer–Skarke already completely classified the 4319 three-dimensional reflexive polytopes, and the public Kreuzer–Skarke data expose that complete inventory. Hibi's palindromicity theorem is standard. Targeted searches did not locate this exact five-value sentence as a standalone theorem, but the record's result is a short corollary of established reflexive-polytope facts plus five elementary witnesses rather than a new classification theorem. Relevant sources: M. Kreuzer and H. Skarke, *Classification of Reflexive Polyhedra in Three Dimensions*, arXiv:hep-th/9805190; T. Hibi, *Dual polytopes of rational convex polytopes*, Combinatorica 12 (1992), 237–240.

## Scientific value — failed
After subtracting known theory, the surviving contribution is only the tiny cutoff `V<=12`, the arithmetic observation that the allowed even values are 4 through 12, and explicit elementary witnesses. It supplies no new classification, enumeration, structural theorem, algorithm, or difficult extremal phenomenon. The gap statistic is forced immediately once the five values are written down, and the `h*` table is a direct specialization of Hibi palindromicity. Under the audit standard, this is a routine corollary/repackaging rather than a sufficiently substantive scientific finding.

## Repair attempt
A bounded repair cannot create a worthwhile new theorem without changing the record's identity: one would need a genuinely nontrivial classification statistic, a new volume regime, a new structural constraint, or a reusable algorithm beyond the stated cutoff. Therefore the record is rejected on scientific-value grounds while its mathematical statements remain usable as elementary observations.

## Search/access notes
Queries included “reflexive 3-polytope even normalized volume”, “reflexive 3-polytopes volume 4 6 8 10 12”, “Hibi reflexive polytope h-vector palindromic theorem”, and “4319 reflexive polyhedra three dimensions Kreuzer Skarke”. The Kreuzer–Skarke paper is openly available on arXiv and International Press; Hibi's theorem is restated in later open literature. No inaccessible source was decisive.

This is an independent AI audit, not a human/expert attestation and not a Lean verification.
