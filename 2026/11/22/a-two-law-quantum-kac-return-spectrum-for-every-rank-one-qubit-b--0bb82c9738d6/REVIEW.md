# Scientific review: two-law quantum Kac return spectrum

## Correctness — PASS

For every \(m\geq0\), rank calculation with \(Q_m=(\bigvee_{j=1}^{m}\alpha^j(p))^\perp\) gives \(\operatorname{rank}(t_{m+1})=2g_{m+1}-g_{m+2}\), with \(g_L\) the common annihilator dimension for \(L\) adjacent-site qubits. This identity holds for noncommuting projections. Invertible local tensor gauge maps entangled covectors to adjacent antisymmetric constraints and yields \(g_L=L+1\). Independent product covectors yield the forbidden-pattern dimension \(L+1\), while parallel-product covectors yield Fibonacci dimension \(F_{L+2}\). The resulting exact masses normalize to one and have means \(4\) and variances \(4\) or \(20\). The source's operator definitions and boundary indices were checked in Section 3, and 71 supplementary finite assertions passed. The finite checks do not certify the infinite argument.

## Originality — PASS (with residual bibliographic risk)

The primary paper arXiv:2611.16972v1 supplies the return construction and Kac mean identity; its directly inspected Section 3 does not treat this explicit spin-chain spectral law. The independently inspected arXiv:0903.1904 already proves the generic \(L+1\) constraint-kernel count, but not the exceptional complete two-law first-return classification or its discontinuous variance. The separate 2016 open-quantum-systems recurrence framework employs repeated measurements, so its return observable is not the same one. Equivalences and broader coverage were sought using searches for noncommutative Kac return distributions, two-qubit rank-one projections, adjacent quantum satisfiability constraints, Fibonacci chains, and spin shifts; no decisive covering statement was found. An older, stronger chain-counting theorem combined with the source's return construction could indirectly subsume the result, so literature priority is not independently certified.

## Mathematical value — PASS

The source framework fixes only the first moment. The new complete classification shows that the first moment misses a universal spectral dichotomy for *all* two-qubit rank-one constraints. It pinpoints the precise exceptional geometric locus, gives both entire distributions, and proves a norm-input discontinuity from a first-return mass changing by one-half. These statements are substantive observables of a new operator-algebraic construction, not a restatement of its mean identity or a single finite example.

## Scope and limitations

Only the tracial qubit Bernoulli shift, adjacent two-site rank-one projections and the source-defined projection-lattice return operator are treated. No claim about repeated-measurement detection is made. The numerical checker is supplementary; no independent audit or exhaustive bibliographic certification was performed.

Self-review: passed. Independent audit: not yet performed.
