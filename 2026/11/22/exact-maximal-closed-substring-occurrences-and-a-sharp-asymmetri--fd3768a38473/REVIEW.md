# Scientific review

## Correctness (C): PASS

The final claim treats every five-positive-tuple \(a,b,c,d,e\) and counts maximal **occurrences** rather than distinct values. The proof classifies factors by zero through four run transitions and rules out all other closed borders. It then checks both available single-symbol extensions, gives seven disjoint endpoint families, and sums them to the exact formula. Integer inequalities on the three zero-run lengths and the two one-run lengths yield the sharp all-length maximum; explicit positive tuples attain both extrema. The verifier independently compares predicted and literal endpoint sets for 7776 full cube cases, 2000 seeded cases, and all fixed-length extrema at lengths 5–42. Finite checks corroborate, not establish, the universal proof. Critical overlapping border occurrences are included in the oracle.

## Originality (O): PASS within the searched and inspected literature

Umezaki–Shibata–Nakashima–Inenaga (2026, arXiv:2607.02838v1) give general run-length-encoded maximal closed substring algorithms and structural lemmas; the full accessible paper does not assert an explicit five-variable symbolic enumeration or fixed-length sharp extremum. Fischer–Köppl (2026, arXiv:2610.38114v1) give output-sensitive algorithms for arbitrary strings, without the five-run symbolic theorem. The published four-run endpoint theorem concerns only four runs, while the five-run closed-factor classification concerns distinct factor **strings**, not maximal occurrence intervals. The symmetric five-run specialization covers only equal outer zero and equal one runs; its maximum, obtained by restricting the all-parameter law, is strictly smaller at lengths congruent to one modulo three. General-purpose procedures can evaluate any given word, but do not logically supply the displayed closed formula plus optimization without the new classification argument. See the structured originality checks in AUDIT.json.

## Mathematical value (V): PASS

Maximal closed substring occurrences are output objects in contemporary compressed string-indexing algorithms. The exact symbolic five-parameter output size and complete endpoint list reveal which run configurations create or suppress maximality. The sharp all-length maximum and the asymmetric residue-one improvement are natural extremal facts not obtained by recomputing the distinct-factor count or by a purely routine parameter substitution. The result gives a reproducible test family for output-size analyses, while making no claim of an improvement to the generic algorithm's complexity.

## Boundaries and risk

Scope is strictly binary, linear, and five-run. The cited general compressed enumeration paper supplies meaningful competing coverage; an unindexed prior explicit five-run calculation is possible. The accessible main paper was inspected rather than relying only on an abstract; independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
