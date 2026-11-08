# Scientific assessment

## Correctness: PASS
The essential degree-sum lemma is an exact translation of disjointness in \(KG(n,2)\): a vertex \(uv\notin D\) has exactly \(|D|-d(u)-d(v)\) selected neighbors. Applying the bound \(2\) at size \(k+2\) rules out a candidate of smaller size. Applying the bound \(3\) at size \(k+3\) yields only a triangle and disjoint matching or, uniquely when \(k=3\), a complete four-vertex selected graph. Both converses are checked. The tuple distinction is tested at selected Kneser vertices, where the \(K_4\) candidate supplies only one selected open neighbor and two selected closed-neighborhood vertices. The accompanying verifier exhaustively checks all subsets at the two relevant sizes for \(k=2,3\). The infinite claim relies on the proof, not these finite experiments.

## Originality: PASS, subject to external priority review
The stronger previously established statements are not attributed to the new result. Cornet and Torres (arXiv:2308.15603, Theorem 20, following paragraph) already determine **all** minimum \(k\)-tuple dominating sets at \(n=2k+3\) as triangle-plus-matching families. Brešar, Cornet, Dravec and Henning (arXiv:2312.15464, Proposition 9) already prove equality of all three minimum **numbers** and supply this construction. The precise additional theorem classifies every ordinary \(k\)-domination minimizer and identifies the unique \(k=3\) non-tuple \(K_4\) family. Searches for equivalent structural descriptions and the exceptional configuration found no directly covering assertion. The incidence-degree method and prior tuple classification are acknowledged, and an unindexed equivalent account remains possible.

## Mathematical value: PASS
Equality of three extremal cardinalities does not imply that their minimizers coincide. The natural first boundary below the matching threshold, \(n=2(k+2)-1\), supports an infinite rigidity theorem: ordinary \(k\)-domination has no additional minimizers except one explicitly classified six-edge type at \(k=3\). The exceptional class consists of exactly \(126\) of the \(1386\) ordinary minima at this parameter and disappears completely from the stronger two variants. This resolves a motivated structural gap left by the prior scalar boundary theorem, not an arbitrary finite graph computation. Its contribution is a complete boundary classification rather than a new general scalar bound.

## Limits and relevant literature
The theorem does not cover other Kneser parameters, nonoptimal sets or other graph families. It uses the established triangle-plus-matching classification and cardinality threshold as context, while proving the new ordinary-minimizer classification independently. Publication priority is not independently certified; further specialized-literature review could find an equivalent theorem.

Cornet and Torres, *\(k\)-tuple domination on Kneser graphs*, arXiv:2308.15603, Sections 3–4, especially Theorem 20 and its paragraph after the proof; Brešar et al., *\(k\)-Domination invariants on Kneser graphs*, arXiv:2312.15464, Section 3, especially Remark 6, Theorem 7 and Proposition 9.

Self-review: passed. Independent audit: not yet performed.
