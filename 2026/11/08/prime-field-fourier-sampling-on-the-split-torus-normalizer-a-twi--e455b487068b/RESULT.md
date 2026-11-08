# Prime-field Fourier sampling on the split-torus normalizer: a twisted-Kloosterman singular spectrum

## Finding
Fix a prime \(p\), a nontrivial additive character \(\psi:\mathbb F_p\to\mathbb C^\times\), and the following subset of \(\operatorname{SL}_2(\mathbb F_p)\):
\[
T=\left\{\begin{pmatrix}t&0\\0&t^{-1}\end{pmatrix}:t\in\mathbb F_p^\times\right\},\quad
W=\left\{\begin{pmatrix}0&t\\-t^{-1}&0\end{pmatrix}:t\in\mathbb F_p^\times\right\},\quad S=T\sqcup W.
\]
For odd \(p\), \(S\) is the rational split-torus normalizer, of cardinality \(2(p-1)\). Define the **unnormalized** square ambient-additive Fourier sampling matrix
\[
\mathcal H_{X,Y}=\psi\!\left(\sum_{i,j=1}^2 X_{ij}Y_{ij}\right),\qquad X,Y\in S.
\]
Put \(h=p-1\), and, for every multiplicative character \(\chi\) of \(\mathbb F_p^\times\), set
\[
K_\chi=\sum_{t\in\mathbb F_p^\times}\chi(t)\psi(t+t^{-1}).
\]
Here \(\mathbf1\) denotes the trivial multiplicative character. The **complete singular-value multiset**, including repetitions, is
\[
\boxed{\bigl\{|K_{\mathbf1}+h|,\ |K_{\mathbf1}-h|\bigr\}\ \sqcup\!\bigsqcup_{\chi\ne\mathbf1}\bigl\{|K_\chi|,|K_\chi|\bigr\}.}
\]
For **every odd prime**, all these values are strictly positive, hence \(\mathcal H\) is invertible. More precisely, with the displayed ordering of \(T,W\) and identical parameter order in each, the determinant is
\[
\det\mathcal H=(K_{\mathbf1}^2-h^2)\prod_{\chi\ne\mathbf1}K_\chi^2\ne0.
\]
At \(p=2\), the same explicitly defined set has two elements, \(\mathcal H\) is the all-ones \(2\times2\) matrix, and the singular-value multiset is \(\{2,0\}\).

As a quantitative consequence of the classical twisted-Kloosterman estimate \(|K_\chi|\le2\sqrt p\), the two distinguished singular values are strictly larger than every other singular value whenever \(p\ge19\); they lie between \(p-1-2\sqrt p\) and \(p-1+2\sqrt p\). For every odd prime, the unnormalized Euclidean condition number is at least \((p-1)/(2\sqrt p)\). Neither estimate asserts an upper bound on the condition number.

## Assumptions and scope
There are no assumptions on the particular nontrivial additive character: every such character is \(\psi_b(x)=\exp(2\pi i b x/p)\) for a uniquely determined \(b\in\mathbb F_p^\times\). The singular values are given by the twisted sums for that character; they need not be independent of \(b\). The pairing is the **entrywise dot product** on the ambient four-dimensional vector space, not the Fourier transform of the nonabelian group \(\operatorname{SL}_2(\mathbb F_p)\). The prime-field restriction is essential for the nonvanishing argument. No statement is made about extension fields or arbitrary subsets of the determinant-one locus.

## Proof
**1. Exact block reduction.** Order both indices with the matrices in \(T\) followed by those in \(W\), each indexed by \(t\in\mathbb F_p^\times\). Two diagonal matrices with parameters \(t,u\), and likewise two antidiagonal matrices with those parameters, have ambient dot product \(tu+(tu)^{-1}\). A diagonal and an antidiagonal matrix have dot product zero. Consequently
\[
\mathcal H=\begin{pmatrix}A&J\\J&A\end{pmatrix},\qquad
A_{t,u}=\psi(tu+(tu)^{-1}),\quad J=\mathbf1_h\mathbf1_h^{\mathsf T}.
\]
This identity is also valid at \(p=2\).

**2. Multiplicative-character singular decomposition.** The normalized vectors \(v_\chi(t)=h^{-1/2}\chi(t)\) form an orthonormal basis of \(\mathbb C^{\mathbb F_p^\times}\). Substituting \(z=tu\) gives
\[
A v_\chi=K_\chi v_{\chi^{-1}}.
\]
Thus \(A\) is the product of a diagonal multiplier and the unitary permutation of characters by inversion. On the constant vector, \(A\) has eigenvalue \(K_{\mathbf1}\) and \(J\) has eigenvalue \(h\). On every nontrivial character vector, \(J\) vanishes. Applying the unitary change of basis \((x,y)\mapsto 2^{-1/2}(x+y,x-y)\) to the two copies turns \(\mathcal H\) into \((A+J)\oplus(A-J)\). This yields precisely the singular-value multiset stated above. The same character inversion has determinant \(\pm1\) on the nontrivial-character space in each summand, so multiplying the two determinants cancels its sign and gives the displayed determinant factorization.

**3. Nonvanishing of every twisted sum for odd primes.** Let \(E=\mathbb Q(\mu_{p-1})\), the cyclotomic field containing every value of any multiplicative character \(\chi\), and write \(\zeta_p=\exp(2\pi i/p)\). Because \(\gcd(p,p-1)=1\), the cyclotomic polynomial \(\Phi_p(Z)=1+Z+\dots+Z^{p-1}\) remains irreducible over \(E\) (the standard coprime-conductor cyclotomic-field disjointness theorem). Define
\[
c_s=\sum_{\substack{t\in\mathbb F_p^\times\\t+t^{-1}=s}}\chi(t)\in E,\qquad s\in\mathbb F_p.
\]
Then \(K_\chi=\sum_s c_s\zeta_p^{bs}\). Were this zero, irreducibility of \(\Phi_p\) would force all \(p\) coefficients \(c_s\) to be equal, since the polynomial of degree at most \(p-1\) with these coefficients must be an \(E\)-multiple of \(\Phi_p\). But \(t+t^{-1}=2\) has only the solution \(t=1\), and therefore \(c_2=1\). On the other hand the map \(t\mapsto t+t^{-1}\) identifies \(t\) and \(t^{-1}\), so its image has at most \((p+1)/2<p\) values: some coefficient is zero. This contradiction applies to **every** multiplicative character, trivial or nontrivial, proving \(K_\chi\ne0\).

**4. Nonvanishing of the two exceptional factors.** Suppose \(K_{\mathbf1}=\pm h\). As a sum of \(h\) complex numbers of absolute value one, equality in the triangle inequality would require every summand \(\psi(t+t^{-1})\) to equal the corresponding real sign \(\pm1\). For \(t=1\), that summand equals \(\zeta_p^{2b}\), which is neither \(+1\) nor \(-1\) when \(p\) is odd and \(b\ne0\). Thus neither exceptional factor can vanish. In characteristic two, the single parameter \(t=1\) has \(t+t^{-1}=0\), making every entry of \(\mathcal H\) equal to one and giving singular values \(2,0\).

**5. Optional spectral separation.** The established classical Kloosterman bound \(|K_\chi|\le2\sqrt p\) applies to the twisted and untwisted sums. Hence the two exceptional singular values are at least \(p-1-2\sqrt p\), and all nonexceptional ones at most \(2\sqrt p\). The strict inequality \(p-1>4\sqrt p\) holds for every prime \(p\ge19\). The condition-number lower bound follows because the maximum of \(|K_{\mathbf1}\pm(p-1)|\) is at least \(p-1\), whereas at least one nontrivial-character singular value exists and is at most \(2\sqrt p\).

## Verification
A standalone numerical checker constructs the ambient-dot-product matrix directly for every prime \(p\in\{2,3,5,7,11,13,17,19\}\), for two choices of additive character where available. It independently constructs the block matrix and twisted character sums, and compares the entire numerical singular-value multiset with direct singular-value decomposition. The checker prints `NORMALIZER_FOURIER_PASS`; its highest observed discrepancy is less than \(10^{-12}\). These are finite cross-checks. Steps 1–4 above give the all-prime proof and its boundary case. The script `check_normalizer.py` uses Python and NumPy and has no other input files.

## Relationship to prior work
Classical twisted Kloosterman sums and their Weil bounds are well established; they are **not** claimed new. Keith Conrad, *On Weil's Proof of the Bound for Kloosterman Sums*, especially the section on twisted sums, provides the necessary character-sum bound for arbitrary finite fields. Kelmer's *Distribution of twisted Kloosterman sums modulo prime powers* (arXiv:0801.4162, first public 2008-01-27) studies a related arithmetic family, not a two-coset ambient Fourier sampling operator. Li and Hu, *Gauss sums over some matrix groups* (arXiv:1105.4513), calculate ambient Fourier coefficients for full general and special linear groups; their object has all group elements in the summation, rather than a square principal operator on this torus normalizer.

An earlier published four-level coordinate Fourier frame result on determinant-one matrices treats only constant and one-coordinate characters restricted to the **entire** determinant-one locus, rather than all ambient Fourier frequencies indexed by the normalizer. A separate result on full determinant-one self-Fourier injectivity for prime fields concerns the larger matrix and does not imply the invertibility of an arbitrary principal submatrix. The contribution here is the exact normalizer singular spectrum and its all-prime nonsingularity, including the exceptional characteristic-two collapse. A more general earlier twisted-Kloosterman diagonalization could still imply this result; historical priority is not certified.

## Limitations
The result proves only complex **linear** Fourier reconstruction from complete samples indexed by this finite normalizer; it does not imply phaseless reconstruction or a uniform inverse-condition-number upper bound. It does not address extension fields. Exact magnitude formulae retain finite twisted Kloosterman sums, and no closed elementary expression for each magnitude is asserted. Finite computations do not establish the general statement; no independent mathematical audit has been performed.

## References
1. D. Kelmer, *Distribution of twisted Kloosterman sums modulo prime powers*, arXiv:0801.4162, first submitted 2008-01-27. https://arxiv.org/abs/0801.4162
2. Y. Li and S. Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513, first submitted 2011-05-23. https://arxiv.org/html/1105.4513v1
3. K. Conrad, *On Weil's Proof of the Bound for Kloosterman Sums*, especially Section 4 on twisted sums. https://kconrad.math.uconn.edu/articles/kloosterman.pdf
4. Published Fourier-frame result, *Four-level Fourier frame spectrum on determinant-one matrices over finite fields*. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-four-level-fourier-frame-spectrum-on-determinant-one-matrices-ov--a9ad8796111d
