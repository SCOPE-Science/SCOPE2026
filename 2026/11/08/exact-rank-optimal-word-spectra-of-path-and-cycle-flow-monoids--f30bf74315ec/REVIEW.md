# Scientific review: rank-optimal edge-collapse word spectra

## Correctness — PASS

The exact source and target conventions agree with the flow-monoid definition of Assem–Derets–Nehaniv (arXiv:2608.24239, Definition 2.1). The critical equivalence is an elementwise rank drop: \(\tau_{ab}\) removes \(a\) from the current image exactly when both \(a,b\) are present. It forces each source to be used once and every arrow to point forward in the removal order; these facts establish a rooted-forest/linear-extension bijection without assuming an unproved normal form. Root choices for an \(\ell\)-vertex path are counted by two-chain shuffles. The multinomial theorem handles path forests, and a marked-cut argument handles cycles with the factor \(n/k\), including \(k=1\). The empty word, one-vertex path and triangle-cycle boundaries are explicit. Direct transformation enumeration for ten graph sizes and independent subset-DP enumeration for 22 graph sizes agree with all closed formulas; 65 ratio checks also passed. Finite tests corroborate but do not substitute for the infinite argument.

## Originality — qualified PASS

The 2026 paper gives the generators, constant-map reachability and the known \(n-1\) reset threshold, but not word multiplicities or the uniform path/cycle ratio. Cameron et al. (2016/2017) study shortest **lengths of particular transformations** rather than the aggregate number of minimum-length rank-loss words across all transformations. East–Gadouleau–Mitchell (2019) study structural and Green-type properties of the same arc-generated semigroups. Search comparisons in published mathematical records found related shortest-reset-word enumerations for different sparse automata, including a Wielandt-type family, not for the flow semigroup of paths or cycles. The object, alphabet, quantifiers and word-versus-element distinction prevent those results from implying the new formula as stated. Historical priority remains qualified because equivalent formulations under sequential graph contraction, pruning orders or automata reset-word enumerators may have escaped the searched literature.

## Mathematical value — PASS

Multiplicity of minimum-rank-loss factorizations is a natural enumerative complexity invariant of an explicitly generated finite monoid. The formulas solve all possible target ranks in two infinite, basic graph families, not just an arbitrary parameter slice. Their sharp rank-by-rank ratio \(n/(n-m)\) records the effect of closing one edge into a cycle; root-refined reset counts provide a further structural check. Both value and limitations are specific: the result counts labeled **words**, not distinct maps, and does not assert a classification for general graphs.

## Principal sources and residual risks

Primary sources: Assem–Derets–Nehaniv, arXiv:2608.24239 (2026-08-25); Cameron–Castillo-Ramirez–Gadouleau–Mitchell, DOI 10.1007/s10801-016-0703-9 (first online 2016); East–Gadouleau–Mitchell, DOI 10.5802/alco.56 (2019). The first source is the recent motivation. Earlier shortest-word enumerations elsewhere are the main novelty risk. Characterization of all minimal rank-loss words of arbitrary connected graphs is not claimed.

Self-review: passed. Independent audit: not yet performed.
