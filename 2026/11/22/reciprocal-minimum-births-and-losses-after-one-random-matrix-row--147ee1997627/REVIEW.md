# Review of reciprocal-minimum births and losses under one-row deletion

## Correctness

**PASS.** The model assumes independent atomless entries and deletes one fixed row; strict monotone exponentialization preserves all comparisons. A loss is necessarily unique. Conditioning on a column's surviving minimum gives the exact birth expectation; splitting the mixed loss–birth moment into equal-column and unequal-column cases gives the verified two-term formula. Both identities agree with exhaustive rank enumeration for matrix orders two and three. For the joint limit, scaled old-row values and surviving-column minima form a Poisson process with intensity \(dx\,e^{-y}dy\); the competing-row tests become conditionally independent marks on bounded windows, and a uniform exponential tail controls truncation. The generating function, covariance and conditional means then follow by integration. The finite checker is supplemental, not an infinite proof.

## Originality

**PASS, with historical-priority qualification.** The 2010 regular-minimality article counts the event of complete reciprocity, whereas the 2011 article characterizes the marginal number of violations in one matrix. Even complete one-time marginal distributions of both original and reduced matrices do not specify the joint law of arrivals and losses under the natural coupling. The 1999 bipartite nearest-neighbor graph paper discusses matching and connectivity in its available abstract; no direct one-row-deletion joint theorem was located. Full-text priority comparisons could not be completed for the 1999 and 2011 articles; neither abstract establishes a covering theorem, but these remain specific risks. Searches for deletion-induced reciprocal-minimum transitions, the Poisson quarter law and equivalent matching-stability statements found no directly covering primary source. The previous result concerning independent cellwise refresh is a different coupling and does not imply a deterministic row-removal law.

## Value

**PASS.** Reciprocal minima represent local two-sided matching in random cost and dissimilarity arrays. Removal of one participant is a natural operation, and the conditional birth intensities differ by a factor of eleven in the limit: \(11/24\) versus \(1/24\), despite an unconditional Poisson quarter of arrivals. This reveals substantive dependence that would be invisible to marginal counting formulas, and provides exact stability and uncertainty calibration for local reciprocal assignments. The exact finite covariance, distribution-free joint limit and explicit deletion-count change are useful as mathematical structural results without needing an additional downstream theorem.

## Sources and limitations

The inspected full text of Trendtel, Ünlü and Dzhafarov (2010), https://doi.org/10.3389/fpsyg.2010.00211, develops regular-minimality enumeration without a row-deletion joint law. Dzhafarov, Ünlü, Trendtel and Colonius (2011), https://doi.org/10.1016/j.jmp.2010.12.002, has a directly relevant one-matrix count distribution but only its abstract and bibliographic material were accessible. Pittel and Weishaar (1999), https://doi.org/10.1002/(SICI)1098-2418(199910/12)15:3/4%3C279::AID-RSA6%3E3.0.CO;2-J, has related bipartite nearest-neighbor objects; only the abstract and bibliographic information could be inspected. Historical completeness is therefore not claimed. No quantitative error estimate or generalization to dependent entries is established.

Self-review: passed. Independent audit: not yet performed.
