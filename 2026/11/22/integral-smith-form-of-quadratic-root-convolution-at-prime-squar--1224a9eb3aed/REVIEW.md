# Review: integral Smith form of prime-square quadratic-root convolution

## Correctness — PASS
The claim is an all-odd-prime theorem. The finite-field quadratic-character correlation establishes the prime-level determinant, while a group-algebra coefficient computation establishes its characteristic-prime rank and thus every prime-level invariant. The square-root fiber identity holds exactly at prime squares, and an integral coset basis gives a block decomposition. A unit block over \(\mathbb Z_{(p)}\) reduces the remaining part to \(p^2K_p\). The determinant excludes other torsion primes, so this proves the complete integral formula. The separately executable checker passed 46,351 exact assertions, with direct Smith forms at \(p=3,5\). The proof does not extrapolate those computations.

## Originality — PASS, with historical-priority risk
The earliest contextual source inspected was Williams' 2014 catalog of named circulant-graph Smith forms. Chandler–Sin–Xiang's 2014 prime-field Paley result studies a different additive group and adjacency operator; Telloni–Williams' polynomial-circulant result studies Smith forms over a polynomial ring; Long–Pigno–Pinner evaluates character Gauss/Jacobi sums rather than integral square-root convolution. Actual published-index searches for square-root-count circulants, cyclic square-map convolutions and Gauss-sum Smith exponents returned no statement of this prime-square invariant-factor law. Related square-class Fourier-support and Ramanujan-sum Smith results concern different operators. No search establishes absolute novelty; an unlocated general integral convolution theorem remains a residual risk.

## Mathematical value — PASS
The quadratic-root-count operator is canonical from the congruence \(x^2=b-a\), and prime-square modulus is the first odd-prime depth with singular nonunit square fibers. Its Fourier spectrum by itself gives a determinant, not its complete integral cokernel. The theorem identifies every invariant-factor multiplicity and a uniform maximal torsion exponent \(p^4\), revealing the role of both Hensel lifting and non-split integral coset structure. The scope is an infinite family of naturally defined integral matrices, not an arbitrary finite slice or recomputation of a known table.

## Closest sources and limitations
- Williams (2014), https://repository.essex.ac.uk/8578/ : finite list of named circulant graph adjacency matrices, not this quadratic-root multiplicity matrix.
- Chandler–Sin–Xiang (2014), https://arxiv.org/abs/1401.8260 : Smith and critical groups of Paley graphs over finite fields, not the cyclic ring of order \(p^2\).
- Telloni–Williams (2014), https://repository.essex.ac.uk/9703/ : Smith forms of particular polynomial circulants over \(\mathbb Q[\lambda]\), not integral Smith factors for the present arithmetic kernel.
- Long–Pigno–Pinner (2014), https://arxiv.org/abs/1410.6179 : evaluation of Gauss/Jacobi sums, not invariant factors.

The result does not cover depths above two or characteristic two. Priority is best-knowledge only, subject to further expert historical review.

Self-review: passed. Independent audit: not yet performed.
