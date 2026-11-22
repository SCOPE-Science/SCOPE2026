# Quadratic Fourier protection and the first nontrivial nullspace of staircase rook placements

## Finding
Let \(E_n=\{(i,j):1\le i<j\le n\}\) and let \(\mathcal R_n\subseteq \mathbb F_2^{E_n}\) be the incidence vectors of all nonattacking rook placements on the staircase board \(E_n\), including the empty placement. Counting convolution by \(1_{\mathcal R_n}\) on \(G_n=\mathbb F_2^{E_n}\) has the following properties.

1. **Quadratic protection:** for every integer \(n\ge3\), every Walsh multiplier of frequency support size at most two is nonzero. At \(n=3,4\), some such coefficients are negative; at every \(n\ge5\), they are strictly positive.
2. **Infinite parity-protected orders:** whenever \(n\not\equiv2\pmod3\), the full convolution operator is invertible.
3. **First nontrivial failure:** at \(n=5\), exactly \(162\) of the \(2^{10}=1024\) Walsh multipliers vanish. Hence the convolution rank is \(862\) and nullity is \(162\). The zero frequencies have support-size distribution \(\{3:10,4:12,5:42,6:48,7:33,8:14,9:3\}\); in particular exactly ten cubic multipliers vanish and none of lower degree. Thus \(n=5\) is the first singular order among \(n\ge3\).
4. **Uniform finite-band stability:** for every integer \(d\ge0\) and every \(S\subseteq E_n\) with \(|S|\le d\),
\[
1-\frac{2d B_{n-1}}{B_n}\le\frac{W_n(S)}{B_n}\le1,
\]
where \(B_n\) is the number of set partitions of \([n]\). For fixed \(d\), the lower bound tends to one as \(n\to\infty\).

These assertions do not classify all singular orders or all Fourier zeros at larger orders.

## Assumptions and scope
For a set partition \(\pi\) of \([n]=\{1,\ldots,n\}\), write each block in increasing order and join its consecutive elements by an arc \((i,j)\). Denote the set of arcs by \(A(\pi)\subseteq E_n\). Each vertex participates in at most one outgoing and one incoming arc, and each directed chain is strictly increasing. Consequently, the map \(\pi\mapsto A(\pi)\) bijects set partitions with rook placements in \(E_n\): no two arcs share a first coordinate or share a second coordinate, and every such placement decomposes uniquely into increasing directed chains. In particular, \(|\mathcal R_n|=B_n\).

For every \(S\subseteq E_n\) define the unnormalized Walsh multiplier
\[
W_n(S)=\sum_{\pi\vdash[n]}(-1)^{|S\cap A(\pi)|}.
\]
This is an integer. Since Walsh characters form a basis for functions on \(G_n\), the convolution rank is the number of subsets \(S\subseteq E_n\) with \(W_n(S)\ne0\). The operator and claim concern counting convolution (no averaging), ordinary real or complex scalars, and every integer \(n\ge2\), with the quadratic protection statement restricted to \(n\ge3\).

## Proof
**Parity protection.** Write \(T_n(x)=\sum_k \left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}x^k\), the Touchard polynomial. The Stirling recurrence gives \(T_{n+1}=x(T_n+T_n')\). Over \(\mathbb F_2[x]\), every second derivative vanishes. Applying the recurrence twice and evaluating at \(x=1\) gives \(T_{n+2}(1)=T_n'(1)\) and \(T_{n+1}(1)=T_n(1)+T_n'(1)\) modulo two. Thus \(B_{n+2}\equiv B_{n+1}+B_n\pmod2\). Starting from \(B_0=B_1=1\), the parities repeat \(1,1,0\). Since every summand in \(W_n(S)\) equals \(1\) modulo two, \(W_n(S)\equiv B_n\pmod2\), so the entire spectrum is nonzero when \(n\not\equiv2\pmod3\).

**A uniform band bound.** For a cell \(e=(i,j)\), let \(N_e\) count the partitions whose arc set contains \(e\). Deleting \(j\) from its block, then relabelling the remaining ordered vertices, injects these partitions into partitions of \(n-1\) vertices: the inverse inserts \(j\) into the block containing \(i\), so \(N_e\le B_{n-1}\). The number of partitions with an odd number of arcs from \(S\) is at most \(\sum_{e\in S}N_e\). Therefore
\[
 B_n-2|S|B_{n-1}\le W_n(S)\le B_n.
\]
Dobiński's moment formula \(B_n=e^{-1}\sum_{k\ge0}k^n/k!\) and Cauchy--Schwarz imply that \(B_n/B_{n-1}\) is nondecreasing for \(n\ge1\). Since \(B_6=203\) and \(B_7=877>4B_6\), every multiplier of degree at most two is strictly positive for \(n\ge7\). The ratio in fact diverges: otherwise the moments would be bounded above by \(M^n\) for some fixed \(M\), contradicting the fixed term \(k^n/(e k!)\) with any fixed integer \(k>M\). This also proves the fixed-degree asymptotic bound.

**The finite boundary.** For \(3\le n\le6\), direct exact enumeration of all set partitions and an integer Walsh--Hadamard transform gives the following minima over frequencies of degree exactly \(d\):

| \(n\) | \(d=0\) | \(d=1\) | \(d=2\) |
|---:|---:|---:|---:|
| 3 | 5 | 1 | -1 |
| 4 | 15 | 5 | -1 |
| 5 | 52 | 22 | 2 |
| 6 | 203 | 99 | 25 |

None is zero. At \(n=5\), the exhaustive 1024-entry integer transform has the zero multiplicities stated above. For a transparent cubic witness take \(S=\{(1,3),(2,3),(1,4)\}\). Among the \(52\) partitions, precisely \(23\) contain no marked arc, \(26\) contain one, \(3\) contain two, and none contain three, giving \(W_5(S)=23-26+3=0\). Thus rank equals \(1024-162=862\). The cardinality distribution and rank are finite exhaustive statements, certified by two independent algorithms in `verify.py`.

## Verification
Run `python3 verify.py` with Python 3, standard library only. One implementation constructs restricted-growth set partitions and their consecutive-block arcs, populates the full Boolean indicator, and performs the exact integer Walsh--Hadamard transform. The other implementation uses a separate memoized rook-placement recursion, deciding for each right endpoint whether to place no rook or a rook in an unused earlier row. Every one of the 1024 Fourier coefficients for \(n=5\) agrees between the implementations. The checker also verifies exact full spectra through \(n=6\), the zero-degree histogram at \(n=5\), the degree-at-most-two minima for \(n=3,4,5,6\), and independent rook-recursion comparisons for every degree-at-most-two character at \(n=6\). The supplied run reports 35,011 exact coefficient checks. Infinite statements rest on the preceding algebraic proof, not the finite checker.

## Relationship to prior work
Classical rook theory, Stirling numbers, and the staircase board's correspondence with set partitions predate this result. Varvak's 2004 paper explains staircase rook numbers and their normal-ordering interpretation; Mitchell's 2004 Ferrers-board paper develops the univariate factorization and inverse problem. These sources provide the underlying enumerative objects, not the frequency-by-frequency signed Fourier rank and first quadratic-versus-cubic threshold. The ordinary univariate rook polynomial cannot by itself distinguish which particular cells are assigned negative signs. A separately indexed all-matchings spectrum for a complete rectangular board concerns a different support set, and its overall signed histogram does not imply the staircase-board spectrum.

## Limitations
The complete nullity \(162\) is proved only for \(n=5\). No converse to the parity-protection sufficient condition is asserted for all \(n\equiv2\pmod3\). No all-size higher-degree zero census, sharp singular conditioning, or stability against nonuniform weighting is claimed. The originality comparison is bounded by inspected archival literature and indexed claims; an obscure multivariate rook-weight specialization may predate the character-resolved formulation.

## References
1. Anna Varvak, *Rook numbers and the normal ordering problem*, arXiv:math/0402376, first posted 2004-02-23, https://arxiv.org/abs/math/0402376.
2. Abigail G. Mitchell, *The inverse rook problem on Ferrers boards*, arXiv:math/0407007, first posted 2004-07-01, https://arxiv.org/abs/math/0407007.
3. B. K. Miceli and J. Remmel, *Augmented Rook Boards and General Product Formulas*, Electronic Journal of Combinatorics 15 (2008), R85, https://doi.org/10.37236/809.
