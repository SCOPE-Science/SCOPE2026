# Independent mathematical audit

## correctness

PASS

Each column of the signed K_{3,n} edge matrix maps two-to-one onto one of four row-pair sign patterns. Summing the signed product over two columns and three row pairs yields W=1/2(S1²+S2²+S3²-3n); Hadamard orthogonality reduces it to 2 sum t_a² - n(n+3)/2. The multinomial count times 2^n accounts for every original signing and implies rank/nullity by character diagonalization. Zeros require three squares S1²+S2²+S3²=3n. The inverse Hadamard map to integer nonnegative counts forces n odd to be 1 mod8, and n even to be 0 mod8. Conversely Legendre’s three-square theorem plus congruence sign choices and Cauchy–Schwarz nonnegativity produce counts for every permitted n; the n=8 case has the explicit witness (1,1,2). The three-square obstruction 4^a(8b+7) is cited as classical, not rediscovered. Independent complete enumeration of 2^(3n) signings for n=2,3,4 matched every predicted Walsh level; no finite enumeration proves the all-n criterion.

## originality

PASS

Goodall’s graphical harmonic-analysis framework provides generic character/Fourier methods but does not give this exact arithmetic cancellation set. Pirzada–Shamsher–Bhat study eigenvalues of *signed adjacency matrices* on bipartite graphs, not the scalar sum of four-cycle sign products across arbitrary signings and its XOR convolution. Classical Legendre three-square theorem supplies the arithmetic input, not the graph-theoretic Fourier classification. The exact all-signing 4-cycle Walsh-zero set and multiplicity distribution have not been established as corollaries of inspected sources. Broader graph character-polynomial literature remains a plausible unindexed prior formulation.

## value

PASS

All 4-cycles form the natural minimum cycle orbit of K_{3,n}; invertibility of their group-convolution operator is a sharply posed invariant. The exact spectrum and a nonperiodic dimension obstruction with n=8 zero but n=80 zero-free give an unexpected graph-to-number-theory connection for every n, beyond a small computational table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
