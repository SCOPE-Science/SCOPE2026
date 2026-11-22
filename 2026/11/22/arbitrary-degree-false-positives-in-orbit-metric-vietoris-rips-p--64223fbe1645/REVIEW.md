# Scientific review — higher-degree phantom orbit-metric homology

## Correctness (PASS)
The metric is valid since all nonzero distances are 1 or 2. The cyclic group acts isometrically. A three-color triangle in the cover would force the inconsistent sheet increments \(s,s+1,s+2\) and \(s,s+1\) on its first and last vertices, so the scale-one source complex is exactly a graph and the action is free on its realization. Edge and vertex orbit counts identify the genuine quotient as connected \(K_{2,\ldots,2}\), with \(2q(q-2)+1\) circles; the quotient-distance flag complex is the join of \(q\) zero-spheres and is a \((q-1)\)-sphere. At the final scale the Borel space is \(BC_m\), not a point. An explicit lifted triangle loop has monodromy one, proving the surjectivity needed for the degree-one persistence map. The standard cyclic-group resolution establishes all coefficient-field cases. The included executable enumerator passed seven finite pairs and is a check, not a substitute for proof.

## Originality (PASS, residual risk)
The motivating September 2026 FGP paper explicitly provides only a degree-one one-sided guarantee and leaves the higher-degree case unsettled. Its stated distinction between orbit-distance flag complexes and genuine geometric quotients does not imply this all-degree false-positive family, nor the exact all-field barcodes. Adams–Heim–Peterson's small-scale quotient-Rips comparison assumes a diameter-action lifting property violated by the construction; its projective examples do not classify this family. Adams and coauthors' 2024 persistent Borel-equivariant cohomology treats continuous circle actions instead. Relevant semantic searches across research records, primary-source text, aliases (cyclic voltage covers, flag completions, quotient metric, Borel and equivariant Rips) and local claim history identified no equivalent theorem. The generic idea of lifting obstructions is classical; priority of an identical counterexample in unindexed work cannot be excluded.

## Value (PASS)
A sharp mathematical gap is whether the published practical orbit-distance algorithm can fabricate positive-dimensional features under free symmetry in degrees at least two. For every such degree, the construction gives a field-independent spurious persistent sphere, even though the corresponding categorical space has no homology in that dimension at the same scale. The fully computed barcodes explain both the misclassification and the effect of group cohomological torsion at the final stage. This is a family-wide, motivated obstruction, not a single arbitrary small-instance computation.

## Closest sources and limitations
- S. Alsulami, *Filtered groupoid persistence*, DOI https://doi.org/10.3934/math.20261180, especially the practical-algorithm comparison and explicit higher-degree caveat.
- H. Adams, M. Heim and C. Peterson, *Metric Thickenings and Group Actions*, DOI https://doi.org/10.1142/S1793525320500569, and M. Heim's 2020 thesis, especially Chapter 3, the diameter-action lifting criterion and Chapter 4's sharpness example.
- H. Adams, E. Lagoda, M. Moy, N. Sadovek and A. De Saha, *Persistent equivariant cohomology*, https://arxiv.org/abs/2408.17331.

The theorem concerns an intentionally constructed two-distance metric and establishes failure of a universal higher-degree bound, not failure for every geometric point-cloud model. It does not certify priority against inaccessible or unindexed work. Group homology and joins of zero-spheres are classical ingredients. Independent mathematical validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.
