# Exact Fourier range and sharp endpoint recovery for seven-point singleton-free partitions

## Finding

Let \(E=\{(i,j):1\le i<j\le7\}\), and let \(\mathcal P\) be the set of partitions of \([7]\) in which **every block contains at least two elements**. Encode each block \(b_1<\cdots<b_r\) by its consecutive arcs \((b_1,b_2),\ldots,(b_{r-1},b_r)\), and denote the resulting incidence vector by \(a(\pi)\in\mathbb F_2^E\). Let \(f\) be the indicator of these vectors on \(G=\mathbb F_2^E\), and define unnormalized counting convolution \(T_fh(x)=\sum_{y\in G}f(y)h(x-y)\).

There are exactly **162** distinct codewords. Exactly **157,808** of the \(2^{21}=2,097,152\) Walsh eigenvalues of \(T_f\) vanish, hence
\[
\operatorname{rank}T_f=1,939,344,\qquad \operatorname{nullity}T_f=157,808.
\]
The least nonzero absolute eigenvalue is **2**, the largest is **162**, and the nonzero spectral condition number is **81**. The first vanishing Walsh characters have edge-support weight **3**; there are exactly **19** of these, and no vanishing characters of weight at most two.

Let \(V=\operatorname{ran}T_f\), viewed inside \(\ell^p(G;\mathbb C)\) or \(\ell^p(G;\mathbb R)\), and let \(Q\) range over all linear projections onto \(V\), without any translation-invariance assumption. Both endpoint projection problems have the exact solution
\[
\min_{Q^2=Q,\operatorname{ran}Q=V}\|Q\|_{\ell^1\to\ell^1}
=\min_{Q^2=Q,\operatorname{ran}Q=V}\|Q\|_{\ell^\infty\to\ell^\infty}
=\frac{9,328,235}{65,536}.
\]
The unique translation-invariant range projection has a kernel supported at exactly **521,828** elements of \(G\). These assertions are exact finite classifications, not asymptotic statements.

## Assumptions and scope

The vertex labels are fixed, and arcs mean *consecutive members within a block*, not every pair in the same block. The Walsh characters are \(\chi_s(x)=(-1)^{\sum_{e\in E}s_ex_e}\) for \(s,x\in G\); no Fourier normalization is used for convolution multipliers. The sign sum is
\[
W(s)=\sum_{\pi\in\mathcal P}(-1)^{\langle s,a(\pi)\rangle}.
\]
The convolution has eigenvalues \(W(s)\). The dimension and rank refer to the full Boolean cube on all 21 arcs, not the 162-dimensional codebook alone. In each block, the arcs form an increasing path; two different partitions have different paths and therefore different incidence words.

## Proof

**Combinatorial reduction.** List the 21 possible pairs in order of increasing second endpoint, and then increasing first endpoint. Recursively add each label either as a singleton new block or to an existing block; discard any final partition containing a singleton. This generates every set partition exactly once. A second enumeration chooses nonattacking rooks in the strictly upper-triangular board of cells \((i,j)\) with \(i<j\), permitting each \(i\) at most one outgoing arc and each \(j\) at most one incoming arc, and requiring each vertex to be incident to at least one chosen arc. An increasing directed graph with indegrees and outdegrees at most one decomposes uniquely into increasing paths, so this second description is equivalent to the first; the two independent exhaustive enumerations yield exactly the same 162 masks.

**Complete signed enumeration.** Initialize the integer array \(F(x)=1\) at the 162 codewords and zero otherwise, over all \(2^{21}\) edge masks. For each bit \(e\), replace every pair \((u,v)\) differing only in bit \(e\) by \((u+v,u-v)\). By induction on the number of processed coordinates, the final array equals \(W(s)\) at every \(s\in G\). The exact integer output has 157,808 zero entries and minimum positive magnitude two. Its squared entries sum to \(2^{21}\cdot162\), as required by Walsh–Plancherel. The zero counts by Hamming weight \(0,1,\dots,21\) are respectively

`[0, 0, 0, 19, 227, 997, 3079, 7304, 13883, 21423, 26413, 27570, 23576, 17005, 9864, 4506, 1575, 340, 27, 0, 0, 0]`.

A direct witness is the three-arc support \(s=\{(1,2),(1,3),(3,4)\}\). The numbers of admissible partitions using exactly \(0,1,2,3\) of these arcs are \(51,81,30,0\), yielding \(W(s)=51-81+30=0\). The verifier enumerates all 19 weight-three vanishing masks; no assertion of higher-order structural orbit classification is needed for the rank result.

**Sharp endpoint projection.** Let \(I(s)=1\) when \(W(s)\ne0\), and zero otherwise. Fourier diagonalization shows that the unique translation-invariant projection onto \(V\) is the multiplier \(I\). Its unnormalized kernel numerator is the integral Walsh transform \(K(g)=\sum_{s\in G}I(s)\chi_s(g)\), so its convolution kernel is \(K(g)/2^{21}\). An exact second Walsh butterfly yields
\[
\sum_{g\in G}|K(g)|=298,503,520,
\qquad |\{g:K(g)\ne0\}|=521,828.
\]
Thus its endpoint norms both equal \(298,503,520/2^{21}=9,328,235/65,536\). For any (not necessarily invariant) projection \(Q\) onto \(V\), average the conjugates \(\tau_gQ\tau_g^{-1}\) over all translations \(g\). Translations preserve \(V\), so the average is a translation-invariant projection onto \(V\), and its endpoint norm does not exceed \(\|Q\|\). The unique such projection is the cutoff \(I\). Hence the displayed norm is the global minimum. The same reasoning applies over real and complex scalars.

## Verification

Run `python3 verify.py` with NumPy installed. The standalone program generates the 162 constrained partitions and checks them against a separate nonattacking-rook enumeration, executes the complete integer Walsh transform for orders three through seven, verifies the n=7 signed-zero counts by degree, signed example by direct parity counting, Plancherel checks, and exact Fourier-inverse projection kernel computation. It checks all 2,097,152 character values implicitly via an exact integer butterfly, not floating point or sampling. Its final line is `PASS`. The computed small-order pairs (partition count, Fourier nullity) are \((1,0),(4,24),(11,0),(41,0),(162,157808)\) for orders three through seven.

## Relationship to prior work

Bóna and Mező (2007, arXiv:0705.2734v1) study exactly the singleton-free partition family through block-count polynomials, real-rootedness, asymptotics, and arithmetic counts; these established enumerative results are background, not the signed incidence-spectrum result. Wachs and White (1991) give the broader set-partition and rook-statistic framework. Bloom and Elizalde (2012) use arc diagrams to study restricted matching and partition patterns. The checked arguments do not determine the 21-coordinate signed Walsh zeros or the optimal endpoint projection norm here. Prior results for **all** set partitions, noncrossing/nonnesting partitions, and pair co-block indicators use different families or frequency encodings; their Fourier ranks do not imply the present constrained 162-codeword spectrum.

## Limitations

The complete rank, nullity and norm are proved by a finite exhaustive integer computation with a standalone reproducible verifier; they are not a symbolic closed formula for general \(n\). No independent mathematical audit is claimed. Unindexed equivalent finite calculations remain a priority risk. The norm describes projections onto the recoverable Fourier range, not the norm of an inverse of the singular convolution on the full space. The nonzero condition number is the ratio of maximal to minimal **nonzero** eigenvalue magnitudes.

## References

- M. Bóna and I. Mező, *Real Zeros and Partitions without singleton blocks*, arXiv:0705.2734v1, first posted 2007-05-18. https://arxiv.org/abs/0705.2734
- M. L. Wachs and D. White, *p,q-Stirling Numbers and Set Partition Statistics*, Journal of Combinatorial Theory, Series A 56 (1991), 27–46.
- J. Bloom and S. Elizalde, *Pattern Avoidance in Matchings and Partitions*, arXiv:1211.3442v1 (2012). https://arxiv.org/abs/1211.3442
