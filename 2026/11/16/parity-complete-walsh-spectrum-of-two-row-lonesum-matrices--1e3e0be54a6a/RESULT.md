# Parity-complete Walsh spectrum of two-row lonesum matrices

## Finding
Let \(n\ge2\) and let \(L_n\) be the set of binary \(2\times n\) lonesum matrices: matrices uniquely determined by their row sums and column sums. Identify them with a subset of the additive group \(G_n=(\mathbb F_2)^{2n}\). For any frequency \(b\in G_n\), let \(c_{ab}(b)\) count its columns equal to \((a,b)\in\{0,1\}^2\) (the two uses of the letter \(b\) are distinguished by context). Define the **unnormalized** Walsh transform
\[
W_n(b)=\sum_{X\in L_n}(-1)^{\langle b,X\rangle},\qquad
\langle b,X\rangle=\sum_{i=1}^2\sum_{j=1}^n b_{ij}X_{ij}\pmod2.
\]
Then every coefficient is given exactly by
\[
\boxed{W_n(b)=3^{c_{00}(b)}\left((-1)^{c_{01}(b)}+(-1)^{c_{10}(b)}\right)
-2^n\mathbf 1_{\{c_{01}(b)=c_{10}(b)=0\}}.}
\]
Consequently,
\[
\boxed{W_n(b)\ne0\quad\Longleftrightarrow\quad\sum_{i,j}b_{ij}\equiv0\pmod2,}
\qquad
\boxed{\min_{W_n(b)\ne0}|W_n(b)|=2.}
\]
All \(2^{2n-1}\) even-weight frequencies survive and all \(2^{2n-1}\) odd-weight frequencies vanish. Thus the unnormalized convolution operator
\[
(C_nf)(x)=\sum_{y\in G_n}\mathbf 1_{L_n}(y)f(x-y)
\]
has rank and nullity both equal to \(2^{2n-1}\), sharp nonzero \(\ell^2\) singular-value gap \(2\), and Moore–Penrose inverse norm \(\|C_n^\dagger\|_{2\to2}=1/2\). Its positive spectral condition number is
\[
\boxed{\kappa_2^+(C_n)=3^n-2^{n-1}.}
\]
The orthogonal projection onto its range is precisely
\[
(P_nf)(x)=\tfrac12\big(f(x)+f(x+\mathbf1)\big),
\]
where \(\mathbf1\) is the all-ones vector, and has the smallest possible norm \(1\) among projections onto this range on both \(\ell^1(G_n)\) and \(\ell^\infty(G_n)\).

## Assumptions and scope
Rows, columns, and binary entries are labeled. A binary matrix is lonesum precisely when it has no two columns equal to \(01\) and \(10\) in either order; equivalently it has neither of the two \(2\times2\) permutation matrices as a submatrix. This is the classical Ryser forbidden-configuration criterion. In the graph-theoretic interpretation, each binary entry encodes the orientation of an edge of \(K_{2,n}\), and the same condition means that the orientation is acyclic: any directed cycle of a complete bipartite orientation contains a directed four-cycle. The coefficient normalization throughout is unnormalized, with the Fourier eigenvalues of \(C_n\) exactly \(W_n(b)\).

The exceptional one-column boundary is **not** included in the theorem: \(L_1=G_1\), so \(W_1(00)=4\) and its other three coefficients vanish. All operator statements concern complex functions with counting-measure \(\ell^p\) norms on \(G_n\); no probability or normalized-convolution factors are implicit.

## Proof
**1. Product-cylinder decomposition.** The forbidden-configuration description gives \(L_n=A_n\cup B_n\), where \(A_n\) is the Cartesian product of the three permitted column types \(00,01,11\), and \(B_n\) is the product of \(00,10,11\). Their intersection is the product of \(00,11\). Character sums over Cartesian products factor into products of their one-column character sums.

For a frequency column \(u\in\{00,01,10,11\}\), the one-column sums for \(A_n,B_n,A_n\cap B_n\), respectively, are
\[
\begin{array}{c|cccc}
u&00&01&10&11\\\hline
A&3&-1&1&1\\
B&3&1&-1&1\\
A\cap B&2&0&0&2
\end{array}.
\]
Inclusion–exclusion yields the boxed coefficient formula. In particular, the zero-frequency coefficient is \(W_n(0)=|L_n|=2\cdot3^n-2^n\), agreeing with the classical unweighted count.

**2. No extra zeros.** Put \(r=c_{01}(b)+c_{10}(b)\). The parity of the total Hamming weight of \(b\) is the parity of \(r\). If \(r\) is odd then \(c_{01}\) and \(c_{10}\) have opposite parity; the two signed terms cancel, and the intersection correction is zero. If \(r\ge2\) is even then those two parities agree and \(W_n(b)=\pm2\cdot3^{c_{00}(b)}\ne0\). If \(r=0\) then \(W_n(b)=2\cdot3^{c_{00}(b)}-2^n\). This cannot vanish for \(n\ge2\), since equality would require the power of three \(3^{c_{00}(b)}\) to equal the positive power of two \(2^{n-1}\); their prime factorizations are incompatible. This exhausts all frequencies.

Every nonzero multiplier is an even integer. To realize the value \(2\), take two frequency columns of type \(01\) and all remaining columns of type \(11\), yielding \(c_{00}=0,c_{01}=2,c_{10}=0\). Thus the least positive multiplier magnitude is exactly \(2\), not merely bounded below by \(2\).

**3. Operator consequences.** Walsh characters form an orthogonal basis of complex functions on \(G_n\), and unnormalized convolution by \(\mathbf1_{L_n}\) is diagonal in that basis with eigenvalues \(W_n(b)\). The support classification gives the rank/nullity and the inverse norm \(1/2\). The triangle inequality gives \(|W_n(b)|\le W_n(0)=2\cdot3^n-2^n\); equality holds at frequency zero. Combining with the attained gap \(2\) proves the stated positive condition number.

Translation by \(\mathbf1\) multiplies the Walsh character at \(b\) by \((-1)^{\sum b_{ij}}\). Therefore averaging the identity and this translation has multiplier \(1\) exactly on the even-weight frequencies, hence is the orthogonal projection onto the range of \(C_n\). The averaging map has \(\ell^1\)- and \(\ell^\infty\)-norm at most \(1\), and any nonzero idempotent projection on a normed space has norm at least \(1\). These are the optimal endpoint projection norms.

## Verification
Run `python3 verify_lonesum_walsh.py` using the separate standalone checker supplied with this result. All arithmetic is exact integer arithmetic. It enumerates every binary matrix and every Walsh coefficient for \(1\le n\le8\), a total of \(87{,}380\) coefficient comparisons, checks the complete signed-multiplier distribution, and independently compares the forbidden-pattern test with a topological-sort test of acyclicity of the oriented \(K_{2,n}\) for \(1\le n\le5\). It also tests a selection of frequencies at larger lengths \(9,10,15,31,50,100\). Expected final output:

```text
LONESUM_WALSH_EXACT_PASS n=1..8; 87380 exact Walsh coefficients; graph cycle checks n<=5
```

The finite checks corroborate but do not establish the unrestricted theorem; the proof is the product-cylinder computation and the prime-factorization argument above.

## Relationship to prior work
The classical binary forbidden-submatrix criterion, staircase construction, and poly-Bernoulli count appear in Kim–Krotov–Lee (2011), especially Section 2, and the count and acyclic-orientation interpretation appear in Cameron–Glass–Rekvényi–Schumacher (2014), Sections 2–3. Their results include the unweighted specialization \(W_n(0)=2\cdot3^n-2^n\); these do not themselves state the nonzero Fourier support, sharp spectral gap, range characterization, or operator conditioning. The present statement is an all-character refinement, not a new claim about the classical counting formula or about Ryser's criterion.

The published theorem *A parity-complete characterization of acyclic orientations of complete bipartite graphs* concerns attainable prescribed **vertex indegree-parity signatures**, a different map from arbitrary signs on **edge-incidence coordinates**. Neither its existence criterion nor its counts of attainable vertex signatures imply the Fourier coefficient formula above. Published results on Fourier projection norms for spanning-tree edge-incidence vectors of \(K_{2,n}\) likewise use a different subset of the same Boolean edge space and do not imply this statement.

## Limitations
The theorem covers exactly binary two-row lonesum matrices, or all acyclic orientations of \(K_{2,n}\), for \(n\ge2\). It does not claim zero-freeness beyond reversal symmetry for larger first-part sizes, for \(q\)-ary lonesum matrices, or for arbitrary bipartite graphs. The formula gives every coefficient but does not separately simplify the number of distinct *signed* values at arbitrary length. Historical priority is based on bounded full-text and indexed-literature comparisons; an unlocated equivalent weighted forbidden-submatrix identity remains possible. No independent mathematical validation is claimed.

## References
1. H. K. Kim, D. S. Krotov, J. Y. Lee, *Poly-Bernoulli numbers and lonesum matrices*, arXiv:1103.4884v1, 2011-03-25, https://arxiv.org/html/1103.4884v1.
2. P. J. Cameron, C. A. Glass, K. Rekvényi, R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, arXiv:1412.3685v1, 2014-12-11, https://arxiv.org/abs/1412.3685.
3. D. B. West, *Acyclic orientations of complete bipartite graphs*, Discrete Mathematics 138 (1995), 393–396, DOI:10.1016/0012-365X(94)00222-5 (enumeration background; full text not separately relied upon).
4. *A parity-complete characterization of acyclic orientations of complete bipartite graphs*, published research record, 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-parity-complete-characterization-of-acyclic-orientations-of-co--361e3944de6f/RESULT.md.
