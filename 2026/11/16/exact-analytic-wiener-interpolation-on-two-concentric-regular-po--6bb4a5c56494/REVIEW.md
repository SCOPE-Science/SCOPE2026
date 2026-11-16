# Scientific review: exact two-ring Wiener interpolation

## Correctness

PASS. For \(0<u<v<1\), the explicit trinomials satisfy both interpolation equations, and each minimizes the norm by a dual exponential certificate \(h_j=\lambda u^j+\mu v^j\). Its upper bound follows from the integer minimum of the candidate costs, while the lower bound follows for *every* integer from the one-turning-point derivative of \(h(t)\). This establishes the result against arbitrary infinite complex coefficient sequences, not just polynomials or finite test cases. Strict contraction under rotational projection excludes non-invariant minimizers. The same dual certificate classifies all equality cases; a one-valley derivative proves adjacent ties and the transition law. The asymptotics follow from the unique small stationary root. Exact rational consistency checks pass, but are not used as an all-degree proof.

## Originality

PASS, with historical-priority caveat. Abakumov–Chalendar–Poltoratski (2026, arXiv:2611.02159v1, §§1.3, 3.1 and 4) give abstract moment duality and infinite polygon criteria, but no explicit two-radius endpoint norm, all-minimizer classification, or degree-transition law. Cheng–Mashreghi–Ross (2018, arXiv:1802.04646v2, §6) frame general \(\ell_A^p\) extremal problems for \(1<p<\infty\), excluding the \(p=1\) equality geometry solved here. The nearby 2020 Wiener-interpolation study by El-Fallah–Kellay concerns subsets of the *boundary* circle rather than these interior two-ring constraints; only its abstract was accessible. Semantic search of public mathematical results found no equivalent completed classification, but absence from a search is not proof of first discovery. Unchecked classical \(\ell^1\) Chebyshev/exponential-moment literature is a residual risk.

## Mathematical value

PASS. The paper motivating the problem treats norm-minimizing functions with prescribed zeros as a natural ingredient of coefficient-space zero-set theory. Even for two interior radial levels, abstract duality leaves a genuine continuous/sequence optimization, and the optimal polynomial degree can be arbitrarily large. The new result supplies its exact value, all extremizers, explicit first phase boundary, and a logarithmic degree-divergence law. This is a full classification of a canonical two-level finite-node case rather than an arbitrary numerical slice.

## Scope and limits

The constraints are vanishing at *at least* the two polygon sets. This does not classify any extra zeros; the result does not extend to arbitrary rotations of the rings, unequal cardinalities, or \(p>1\). The exact proof is self-contained and independent of the finite rational checker. Historical priority and independent mathematical audit remain open.

Self-review: passed. Independent audit: not yet performed.
