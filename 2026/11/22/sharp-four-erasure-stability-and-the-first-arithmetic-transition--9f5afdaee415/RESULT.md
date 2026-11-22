# Sharp four-erasure stability and the first arithmetic transition for the coordinate–Fourier frame

## Finding

For every integer \(N\ge5\), let \(\omega_N=e^{2\pi i/N}\), and let \(F_N\) be the unitary discrete Fourier matrix, \((F_N)_{a,b}=N^{-1/2}\omega_N^{ab}\) for \(a,b\in\mathbb Z/N\mathbb Z\). Form the equal-norm, twice-redundant frame \(\Phi_N=[I_N\;F_N]\) in \(\mathbb C^N\). For a set \(E\) of labelled frame columns, write \(S_E=\sum_{v\notin E}vv^*\) for the *retained* frame operator, and \(A_N(k)=\min_{|E|=k}\lambda_{\min}(S_E)\).

The sharp worst-case lower bounds for one through four deletions are
\[
\boxed{\begin{aligned}
A_N(1)&=1,\\
A_N(2)&=1-N^{-1/2},\\
A_N(3)&=1-\sqrt{2/N},\\
A_N(4)&=\begin{cases}
1-\dfrac{2\cos(\pi/(2N))}{\sqrt N},&N\text{ prime},\\[3pt]
1-\dfrac2{\sqrt N},&N\text{ composite}.
\end{cases}
\end{aligned}}
\]
Every bound is attained and strictly positive. For every deletion set of at most four columns, \(\lambda_{\max}(S_E)=2\). Accordingly the sharp worst-case condition number of the retained **analysis** matrix after \(k\) erasures is \(\sqrt{2/A_N(k)}\).

The first three optimal values are independent of the factorization of \(N\), whereas the fourth detects compositeness. At four erasures, **every** worst mask deletes exactly two coordinate-basis columns indexed \(a\ne b\) and exactly two Fourier-basis columns indexed \(c\ne d\). Its indices satisfy
\[
\boxed{(a-b)(c-d)\equiv\begin{cases}
\pm1\pmod N,&N\text{ prime},\\
0\pmod N,&N\text{ composite}.
\end{cases}}
\]
The number of unordered, labelled four-erasure masks attaining the sharp worst bound is
\[
\boxed{K_N=\begin{cases}
\dfrac{N^2(N-1)}2,&N\text{ prime},\\[4pt]
\dfrac{N^2}{4}\displaystyle\sum_{h=1}^{N-1}(\gcd(h,N)-1),&N\text{ composite}.
\end{cases}}
\]
These are literal counts of four-element subsets of the \(2N\) labelled frame vectors.

Moreover, the **complete retained-frame spectrum** for any two-plus-two erasure mask is determined by its difference product \(t=(a-b)(c-d)\pmod N\): set
\[
\sigma_\pm(t)=\sqrt{\frac{2\pm2|\cos(\pi t/N)|}{N}}.
\]
Then the \(N\) eigenvalues of \(S_E\), counted with multiplicity, are
\[
\boxed{\left\{1-\sigma_+(t),\,1+\sigma_+(t),\,1-\sigma_-(t),\,1+\sigma_-(t),\,\underbrace{2,\ldots,2}_{N-4}\right\}.}
\]
Here \(t\) may be any integer representative of its residue, since the absolute cosine is well defined modulo \(N\).

At the sharp dimension boundary, \(N=4\), four erasures may destroy spanning (for example, erase coordinate indices \(0,2\) and Fourier indices \(0,2\)); hence \(N=5\) is the smallest dimension with unconditional recovery after four erasures.

## Assumptions and scope

All vectors have Euclidean norm one and the analysis map consists of inner products with the retained vectors. The two bases are labelled separately, even though one or more vectors might be projectively related in small dimensions. An erasure deletes one specified frame column. The bound is worst-case over all subsets of the given size; it does not average over erasures, optimize the signal prior or change the reconstruction operator. All spectral claims are for the complex Hilbert space \(\mathbb C^N\) and the standard Hermitian inner product. Prime and composite refer to positive integer \(N\ge5\); the dimension-four boundary is a separate assertion.

## Proof

**1. Orthogonal-basis reduction.** Because the identity and Fourier columns are independently orthonormal bases,
\[
\Phi_N\Phi_N^*=2I_N.
\]
If \(U_E\) collects the \(k\) erased columns, the retained operator is
\[
S_E=2I_N-U_EU_E^*.
\]
For \(k\le4<N\), the nonzero eigenvalues of \(U_EU_E^*\) and \(U_E^*U_E\) agree, and \(U_EU_E^*\) has a zero eigenvalue. Thus \(\lambda_{\max}(S_E)=2\) and
\[
\lambda_{\min}(S_E)=2-\lambda_{\max}(U_E^*U_E).
\]
Suppose \(r\) deleted vectors come from the coordinate basis and \(s=k-r\) from the Fourier basis. Their erased Gram matrix is
\[
G_E=\begin{pmatrix}I_r&C\\ C^*&I_s\end{pmatrix},\qquad
C=(N^{-1/2}\omega_N^{ab})_{a\in R,b\in T},
\]
where \(R,T\) are the selected coordinate and Fourier indices. If \(\tau_j\) are the singular values of \(C\), the nonunit eigenvalues of \(G_E\) are \(1\pm\tau_j\). The remaining \(|r-s|\) eigenvalues are one (and if either subset is empty, all eigenvalues equal one). This follows by applying singular-value decomposition to the off-diagonal block; there is no assumption of a general-position or full-spark minor.

**2. The first three erasure sizes.** For \(k=1\), \(\lambda_{\max}(G_E)=1\). For \(k=2\), splitting the deletions one from each basis gives \(C\) of modulus \(N^{-1/2}\); this is worse than putting both in one orthonormal basis. For \(k=3\), the worst split is one-plus-two (or two-plus-one); the cross block is a row or column of two entries of modulus \(N^{-1/2}\) and hence has norm \(\sqrt{2/N}\). All these patterns are attainable for every \(N\), proving the first three values. In particular, no arithmetic property of the Fourier phases is visible to these ranks.

**3. Four erasures and the exact spectral formula.** The four possible split types, up to swapping the bases, are four-plus-zero, three-plus-one, and two-plus-two. Their respective largest erased-Gram eigenvalues are \(1\), \(1+\sqrt{3/N}\), and \(1+\|C\|_{\mathrm{op}}\). For two-plus-two deletions, multiply rows and columns of the cross block by unit complex phases to obtain
\[
C\sim\frac1{\sqrt N}\begin{pmatrix}1&1\\1&\omega_N^t\end{pmatrix},\qquad
 t=(a-b)(c-d)\pmod N.
\]
The two eigenvalues of \(CC^*\) are
\[
\frac{2\pm|1+\omega_N^t|}{N}
=\frac{2\pm2|\cos(\pi t/N)|}{N}.
\]
This establishes the displayed complete spectrum. It also shows \(\|C\|_{\mathrm{op}}\le 2/\sqrt N\).

If \(N\) is composite, choose nonzero proper factors \(u,v\) with \(uv=N\), and choose the within-basis index differences equal to \(u,v\). Their product is zero modulo \(N\), so \(\|C\|_{\mathrm{op}}=2/\sqrt N\). Conversely, equality in the modulus bound requires \(\omega_N^t=1\), or \(t\equiv0\pmod N\). If \(N=p\ge5\) is prime, both index differences are nonzero, so \(t\not\equiv0\). The greatest attainable \(|\cos(\pi t/p)|\) over nonzero residues occurs exactly at \(t=1\) and \(t=-1\), and is \(\cos(\pi/p)\). Every nonzero product can be realized, yielding \(\|C\|_{\mathrm{op}}=2\cos(\pi/(2p))/\sqrt p\). Since \(2\cos(\pi/(2N))>\sqrt3\) for every \(N\ge5\), the two-plus-two case strictly dominates the three-plus-one and four-plus-zero cases both for prime and composite dimensions. This proves the fourth bound, all equality patterns, and positivity: the prime case has \(2\cos(\pi/(2p))<\sqrt p\) for \(p\ge5\), while the composite case starts at \(N\ge6\), where \(2<\sqrt N\).

**4. Exact counts of worst masks.** For a prime \(p\), fix any unordered coordinate pair \(\{a,b\}\). The Fourier differences realizing \(t=\pm1\) have absolute residue \(\pm(a-b)^{-1}\). There are exactly \(p\) unordered Fourier pairs with that difference. Therefore there are \(\binom p2p=p^2(p-1)/2\) masks.

For composite \(N\), temporarily order the coordinate and Fourier pairs. For a nonzero ordered coordinate difference \(h=a-b\), there are \(N\) choices of its starting index. The congruence \(h(c-d)\equiv0\pmod N\) has exactly \(\gcd(h,N)-1\) **nonzero** Fourier differences, each with \(N\) ordered starting indices. Thus the number of ordered pair-pairs is \(N^2\sum_{h=1}^{N-1}(\gcd(h,N)-1)\). Each four-erasure mask has exactly four such orderings, proving the composite count. Both formulas are valid integers, and the classification is exhaustive.

**5. Boundary \(N=4\).** Deleting \(\{e_0,e_2,F_0,F_2\}\) yields \(t=(0-2)(0-2)\equiv0\pmod4\), so \(\|C\|_{\mathrm{op}}=1\) and \(\lambda_{\min}(S_E)=0\). For \(N=2\) or \(N=3\), four deletions leave fewer than \(N\) vectors and hence cannot preserve spanning; for \(N=1\) there are fewer than four available labelled vectors. This completes the asserted dimension threshold.

## Verification

Run `python CHECK.py` with Python 3 and NumPy. It constructs the actual frame \([I_N\ F_N]\), enumerates every erasure subset of sizes one through four for each \(5\le N\le13\), diagonalizes the true erased Gram matrices, and checks the four analytical minima, the exact counts of maximizing four-erasure masks, and the primary two-plus-two spectrum. This explicitly exercises prime and composite dimensions, including several prime powers and even composite orders. The checker uses floating-point eigenvalues with a stated tolerance; the universally quantified proof is the exact argument above and is not inferred from finitely many tests.

## Relationship to prior work

Salanevich and Strachan (2025) prove general erasure robustness bounds for Gabor and mutually unbiased-basis frames, including dimension-uniform sufficient guarantees, without an exact all-modulus four-erasure minimum, complete extremizer count, or first prime/composite transition for this twice-redundant coordinate–Fourier frame. Fickus and Mixon (2012) introduce numerical erasure robustness and develop bounds for families of frames; the group-theoretic extension by Fickus, Jasper, Mixon and Peterson (2012) estimates worst subframe singular values but does not state the present specific classification. The elementary singular-value decomposition of two projections and the Fourier-minor identity themselves are standard, not claimed as new. The contribution is their global all-order optimization across **every** four-deletion mask, the sharp arithmetic equality condition and exact mask incidence, together with the proof that four is the first deletion size revealing this distinction.

A separate published harmonic-frame theorem on two-character cyclic frames concerns deleting sample vectors from a two-dimensional Fourier-row system, not deleting vectors from the union of two full orthonormal bases in dimension \(N\). The published three-erasure Alltop theorem concerns a full prime-dimensional Gabor orbit of \(N^2\) vectors rather than this pair of bases. A published weighted four-erasure theorem treats half-dimensional skew-conference equiangular frames, whose Gram structure and weights differ. Their statements do not imply the present formula by setting a parameter, taking a dual, or passing to a subframe. Larson and Scholze (2015) also study reconstruction by bridging erased coefficients for general unions of two bases. The accessible abstract does not state an exact coordinate–Fourier four-erasure minimum or equality census, but the full book chapter was unavailable and has not been ruled out as covering an equivalent formulation. An unindexed reformulation via restricted norms of order-two Fourier minors remains a possible priority risk.

## Limitations

The result is about exactly this pair of unweighted orthonormal bases and deletion sizes at most four, not all pairs of mutually unbiased bases or arbitrary Gabor or Fourier designs. The full two-plus-two spectrum does not give a classification of higher-cardinality erasure masks. Counts depend on labelled columns. The minimum is a deterministic linear-reconstruction stability invariant, not a probabilistic noise estimate. The mathematical proof is exact, whereas the supplementary checker uses floating-point arithmetic. Broad prior coverage through a general Fourier-minor extremal theorem cannot be categorically excluded. Independent mathematical validation has not been performed.

## References

1. P. Salanevich and N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, first public version 2025-09-01, arXiv:2509.01325, https://arxiv.org/abs/2509.01325.
2. M. Fickus and D. G. Mixon, *Numerically erasure-robust frames*, 2012, arXiv:1202.4525, https://arxiv.org/abs/1202.4525.
3. M. Fickus, J. Jasper, D. G. Mixon and J. D. Peterson, *Group-theoretic constructions of erasure-robust frames*, 2012, arXiv:1210.0139, https://arxiv.org/abs/1210.0139.
4. *Exact adversarial-erasure spectra for two-character cyclic harmonic frames*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-adversarial-erasure-spectra-for-two-character-cyclic-harmo--e1e03f96b6f0.
5. *Sharp three-erasure stability of Alltop Gabor frames*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-three-erasure-stability-of-alltop-gabor-frames--ede488cf192e.
6. *Weighted four-erasure spectra and majorization rigidity for skew-conference frames*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-weighted-four-erasure-spectra-and-majorization-rigidity-for-skew--b7efda2e8893.
7. D. Larson and S. Scholze, *Bridging Erasures and the Infrastructure of Frames*, Excursions in Harmonic Analysis, Vol. 4 (2015), DOI:10.1007/978-3-319-20188-7_2 (abstract inspected, full chapter unavailable).
