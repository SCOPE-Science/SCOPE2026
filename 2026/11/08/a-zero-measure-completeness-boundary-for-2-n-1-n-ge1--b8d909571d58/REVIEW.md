# Scientific review: a zero-measure completeness boundary

## Correctness — PASS

The claimed sequence, parameter domain, subset-sum definition, and gap intervals are explicit. For \(\alpha\ge2/3\), the first term exceeds one. For \(1/2<\alpha<2/3\), the earliest excess above the binary-power baseline isolates a permanently missing integer. For \(\alpha=2^{-k}\), the terms after initial zeros form the binary basis. The exact gap identity follows from the sum \(\sum_{j=1}^n(2^j+1)-(2^{n+1}+1)=n-3\). The metric step is justified by an actual second-moment proof: orthogonal lacunary exponentials, a square-index subsequence, Borel--Cantelli, interpolation, and Weyl's criterion. Therefore for almost every \(\alpha\in(0,1/2)\) the gap length divided by \(n\) converges to \(1/2-\alpha>0\). The proof covers every boundary it claims, and the exact-arithmetic finite checker is corroboration rather than a replacement for the metric proof.

## Originality — PASS, qualified

The closest full primary text is Wu--Ma, *A note on a problem of Ma and Chen* (arXiv:2610.38288v1, 2026-10-28). Its Theorems 1.1 and 1.2 assert the existence of a suitable scaling when the growth ratio is at most two; the paper also recalls Ma--Chen's positive-measure statement under a fixed ratio bound \(\gamma<2\). The present claim does not challenge that existence theorem: it supplies a specific strictly subdoubling sequence for which the successful set nevertheless has measure zero and computes the asymptotic size of consecutive missing-integer gaps for almost every small scaling. The proofs in the primary text establish existence by nested intervals, not the measure-zero or typical-gap conclusions. Brown's subset-sum test, binary expansions, and metric equidistribution are pre-existing tools, not novelty claims. The publisher abstract of Ma--Chen (Acta Arith. 203, 2022) was inspected and has no exact near-doubling example; its full primary text could not be retrieved by the available noninteractive routes. Searches for the exact sequence, equivalent formulations, and stronger or broader results did not yield a covering theorem. The residual risk is historical work not indexed or in the inaccessible 2022 full text. No claim of certified historical priority is made.

## Mathematical value — PASS

The question is structurally motivated by two consecutive threshold theorems in the same literature: positive measure is guaranteed under a fixed growth bound strictly below two, while existence survives the boundary bound two. Merely making the inequality strict at each index still does not preserve positive measure. The explicit family \(2^n+1\) is a canonical minimal perturbation of binary powers: its growth is strictly below doubling, yet approaches doubling. The quantified almost-everywhere run of excluded subset-sum values explains the failure rather than merely recording a zero-measure set. Infinitely many explicitly complete scalings preserve the essential existence side of the dichotomy. The theorem does not classify all valid scalings or all near-doubling sequences; that limitation does not diminish this motivated sharp counterexample.

## Closest sources and limitations

- B.-L. Wu and W.-X. Ma, *A note on a problem of Ma and Chen*, arXiv:2610.38288v1 (full text inspected): existence for all sequences bounded by doubling, but no claim about the measure-zero outcome or typical gaps for the specified sequence.
- W.-X. Ma and Y.-G. Chen, *Hegyvári's theorem on complete sequences, II*, Acta Arith. 203 (2022), 307–318, doi:10.4064/aa210811-30-3 (official publisher abstract inspected, full text unavailable): subcritical existence and its relation to positive measure.
- Distinct-index subset-sum gap necessity is classical, supplied as Brown's Lemma 2.1 in Wu--Ma; the metric doubling-map argument and its application to the near-doubling example are explicitly proved in RESULT.md.
- Historical priority remains qualified, and no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
