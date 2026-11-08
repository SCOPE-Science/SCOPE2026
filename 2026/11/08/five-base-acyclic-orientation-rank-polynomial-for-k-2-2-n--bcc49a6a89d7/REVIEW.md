# Review of the five-base acyclic-orientation polynomial

## Correctness — PASS
For complete multipartite graphs, source peeling produces a unique sequence of nonempty monochromatic blocks with no repeated adjacent part label. Specializing to \(K_{2,2,n}\), there are exactly 14 two-part skeletons. The labeling multiplicities, inversion exponents, mandatory gaps, and exponential generating function are proved in the result. A direct, exact standard-library reduction of all 14 skeletons produces the five claimed polynomial bases, so every coefficient for all \(n\ge1\) follows by exponential generating-function extraction. Independent graph-edge enumeration through \(n=4\) and source-block recursion through \(n=12\) agree. No infinite conclusion depends on finite extrapolation.

## Originality — PASS (provisional historical priority)
The complete arXiv HTML of Mühlherr–Poullot was inspected at its acyclic-polynomial definitions, complete-tripartite examples, and appendix. It introduces the invariant but does not state the complete five-base formula. The Carballosa–Khera–Reyes multipartite theorem counts orientations without their edge-reversal ranks. The closest published signed-algebra result gives evaluations at \(t=-1\), and its broader signed consequences are explicitly not claimed as new. The OEIS tripartite table records unsigned values. No covering full-rank result appeared in the actual equivalent-formulation and historical-comparison searches. Possible unindexed inversion-polynomial literature remains a risk.

## Mathematical value — PASS
The complete coefficient distribution answers a natural refined-enumeration question arising from the 2026 acyclic-polynomial program, not merely a numerical specialization. A closed expression using only five fixed polynomial bases works at arbitrary graph size and yields the full symmetric edge-disagreement profile of a nontrivial tripartite family. It also connects to an existing unsigned tripartite census and a signed-Hamiltonicity investigation, with the scope of genuinely new content carefully distinguished.

## Limitations and nearest literature
Only \(K_{2,2,n}\) under the stated part-ordered reference is classified, not every reference orientation or part-size vector. The formula alone does not establish Hamiltonicity. A general source-block encoding is known, and a broader signed evaluation algebra pre-exists; the distinct novelty assertion is specifically about the five-base full polynomial. Historical priority and the proof have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
