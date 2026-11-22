# Sharp endpoint recovery constants for odd-degree profiles of bipartite spanning trees

## Finding
Let \(m,n\ge2\). For every spanning tree \(T\) of the labelled complete bipartite graph \(K_{m,n}\), define its *odd-degree profile* \(\partial_2 T\in\mathbb F_2^{m+n}\) by putting a one at a vertex precisely when its degree in \(T\) is odd. Let
\[
f_{m,n}(z)=\#\{T:\partial_2 T=z\},\qquad (C_{m,n}g)(z)=\sum_{w\in\mathbb F_2^{m+n}}f_{m,n}(w)g(z+w).
\]
For \(d\ge2\) write
\[
\Phi(d)=\begin{cases}1,&d\text{ odd},\\1+\binom{2r}{r}\bigl(2^{-r}-2^{1-2r}\bigr),&d=2r.\end{cases}
\]
Let \(W_{m,n}=\operatorname{ran} C_{m,n}\). The **exact, unrestricted sharp endpoint projection constants** are
\[
\boxed{\min_{Q^2=Q,\ \operatorname{ran}Q=W_{m,n}}\|Q\|_{\ell^1\to\ell^1}
=\min_{Q^2=Q,\ \operatorname{ran}Q=W_{m,n}}\|Q\|_{\ell^\infty\to\ell^\infty}
=\Phi(m)\Phi(n).}
\]
Both minima are taken over **all** real or complex linear projections, with no assumption of translation invariance. This exact evaluated product, as attached to vertex-degree parity observations of bipartite spanning trees, is the primary assertion. For both even shore sizes growing,
\[
\Phi(m)\Phi(n)\sim\frac{2}{\pi}\frac{2^{(m+n)/2}}{\sqrt{mn}},
\]
although the recoverable Fourier fraction tends to one.

For completeness the Walsh multiplier at a character having \(a\) negative signs on the first shore and \(b\) on the second is
\[
\Lambda_{m,n}(a,b)=(-1)^{a+b}(m-2a)^{n-1}(n-2b)^{m-1}.
\]
Thus the *previously implied* Fourier-support classification gives
\[
\operatorname{rank}C_{m,n}=\Bigl(2^m-\mathbf1_{2\mid m}\binom{m}{m/2}\Bigr)
\Bigl(2^n-\mathbf1_{2\mid n}\binom{n}{n/2}\Bigr),
\]
with the indicator contribution taken as zero when the corresponding size is odd. The least nonzero absolute multiplier is \(d_m^{n-1}d_n^{m-1}\), with \(d_s=1\) for odd \(s\) and \(d_s=2\) for even \(s\); the largest is \(m^{n-1}n^{m-1}\). Neither the degree-enumerator formula nor the general Fourier-projection optimality principle is claimed as new.

## Assumptions and scope
The graph is simple, labelled, and has two nonempty parts of cardinalities \(m,n\ge2\). Each spanning tree is counted once; distinct trees can have the same degree-parity profile and are then counted with multiplicity. Convolution is unnormalized on the group \(\mathbb F_2^{m+n}\). Walsh transforms use \(\widehat f(s)=\sum_z f(z)(-1)^{s\cdot z}\); inverse transforms divide by \(2^{m+n}\). The range is a subspace of all real or complex functions on the whole Boolean cube, not only on realizable degree-parity profiles. Endpoint norms use counting \(\ell^1\) and maximum \(\ell^\infty\). The result does not concern the different edge-incidence convolution on \(\mathbb F_2^{mn}\).

## Proof
**1. Degree-weighted input and its exact support.** Introduce commuting variables \(x_1,\ldots,x_m\) and \(y_1,\ldots,y_n\). The weighted bipartite spanning-tree identity is
\[
\sum_{T}\prod_{i=1}^{m}x_i^{\deg_T(i)-1}\prod_{j=1}^{n}y_j^{\deg_T(j)-1}
=\left(\sum_i x_i\right)^{n-1}\left(\sum_j y_j\right)^{m-1}.
\]
This is the graph case of the degree-weighted colorful-complex enumeration, and also follows from the weighted matrix-tree theorem using edge weights \(x_i y_j\). For clarity: the weighted Laplacian has diagonal blocks \((\sum_jy_j)\operatorname{diag}(x_i)\) and \((\sum_ix_i)\operatorname{diag}(y_j)\) and off-diagonal block \(-xy^{\mathsf T}\). A cofactor followed by the matrix determinant lemma produces \((\prod_i x_i)(\prod_j y_j)(\sum_i x_i)^{n-1}(\sum_jy_j)^{m-1}\). Removing the product of one variable per vertex gives the displayed identity. This polynomial identity extends to arbitrary signs by specialization.

Assign \(x_i=-1\) precisely on the first-shore Walsh support, and similarly for \(y_j\). Since \((-1)^{\deg_T(v)}=(-1)^{\deg_T(v)-1}(-1)\) when \(v\) is chosen, the Walsh sum over the odd-degree profiles is the displayed \(\Lambda_{m,n}(a,b)\). Its zeros are exactly the characters with \(a=m/2\) when \(m\) is even, or \(b=n/2\) when \(n\) is even. All other characters survive. Distinct shore frequencies are independent, proving the tensor-product range and rank formula.

**2. Sharpness among unrestricted projections.** For a finite abelian group, average any projection onto a translation-invariant Fourier subspace over all conjugations by group translations. Each conjugate remains a projection onto that subspace and its \(\ell^1\) or \(\ell^\infty\) norm does not increase under averaging. The average commutes with translations and hence is a Fourier multiplier. A projection onto the prescribed range must act as one at every retained character and zero at every excluded character. Therefore the average is the unique canonical Fourier projection \(P_{m,n}\), so \(\|P_{m,n}\|\le\|Q\|\) for every competing projection. Conversely \(P_{m,n}\) itself is admissible, proving global minimality.

**3. One-shore kernel.** If \(d\) is odd, its frequency support contains every character, and the projection is the identity, norm one. Suppose \(d=2r\) with \(r\ge1\). The one-shore projection excludes exactly the middle Walsh layer. Its convolution kernel is
\[
p_d(z)=\mathbf1_{z=0}-2^{-d}K_r(|z|;d),\qquad
K_r(t;d)=\sum_{j=0}^r(-1)^j\binom tj\binom{d-t}{r-j}.
\]
For \(0\le t\le d\), Krawtchouk duality gives
\[
\binom dt K_r(t;d)=\binom dr K_t(r;d),\quad
\sum_{t=0}^{2r}K_t(r;2r)u^t=(1-u)^r(1+u)^r=(1-u^2)^r.
\]
It follows that \(K_r(t;2r)=0\) for odd \(t\), and
\[
\sum_{t=0}^{2r}\binom{2r}t|K_r(t;2r)|=\binom{2r}r\sum_{j=0}^r\binom rj=\binom{2r}r2^r.
\]
At the zero group element \(p_d(0)=1-2^{-d}\binom d{d/2}>0\), so subtracting its excluded absolute contribution one more time yields
\[
\|p_d\|_{\ell^1}=1-2\frac{\binom{2r}r}{2^{2r}}+\frac{\binom{2r}r2^r}{2^{2r}}=\Phi(2r).
\]
For convolution, both endpoint operator norms equal the sum of absolute values of its kernel: the upper estimate is triangle inequality and equality is attained by an appropriate sign test function.

**4. Factorization and asymptotic.** Because retained frequency supports factor across the two shores, their canonical projection is the tensor product of the one-shore projections, and its convolution kernel is \(p_m\otimes p_n\). The kernel absolute sum factors exactly: \(\|p_m\otimes p_n\|_1=\|p_m\|_1\|p_n\|_1=\Phi(m)\Phi(n)\). This proves the sharp product theorem. For even \(d=2r\to\infty\), Stirling's formula gives \(\binom{2r}r\sim2^{2r}/\sqrt{\pi r}\), hence \(\Phi(d)\sim2^{d/2}\sqrt{2/(\pi d)}\). Multiplying yields the claimed leading constant. The retained fraction \((1-\binom m{m/2}/2^m)(1-\binom n{n/2}/2^n)\to1\) along even shores, so the instability occurs despite asymptotically negligible relative nullity.

## Verification
The standalone `check.py` uses independent brute-force enumeration of all edge subsets of tree size, a union-find acyclicity test, direct odd-degree profile counting, and an independent integer Walsh--Hadamard transform for each of the six cases \((m,n)=(2,2),(2,3),(3,3),(2,4),(3,4),(4,4)\). It compares every direct multiplier with the signed degree formula, checks the exact rank, and verifies the exact rational projection norm computed by inverse Walsh transformation. It also verifies Krawtchouk duality identities for every even shore size between two and sixteen. Running `python3 check.py` prints `PASS: 672 integer/rational assertions`. These finite tests are corroboration, not a substitute for the all-size algebraic proof.

## Relationship to prior work
Aalipour, Duval, Kook, Lee, and Martin established weighted enumeration formulas for complete colorful complexes including complete bipartite graphs. Their Theorem 1.2 supplies the degree-weighted enumerator used here. The result of Ge and Yu treats odd spanning-tree counts for complete bipartite graphs and supplies a closely related direct degree-enumerator calculation; it does **not**, in the inspected text, calculate an endpoint projection constant for the full degree-parity profile convolution. These degree-enumerator consequences, including the displayed Walsh multiplier and its support, are not originality claims.

Defant, Galicer, Mansilla, Mastyło, and Muro establish the general minimal-projection formula for arbitrary finite Boolean Fourier frequency sets, which subsumes the translation-averaging step. Their theorem does not explicitly evaluate the middle-layer complement projection for this bipartite-tree observable or the exact product \(\Phi(m)\Phi(n)\); the finite closed evaluation and its stability consequences are what is asserted here. Published tree-incidence results for \(K_{2,n}\) and \(K_{4,4}\) use **edge variables**, rather than **vertex odd-degree variables**, and their Fourier support and endpoint constants do not imply this result without an additional change of observable and its Fourier-analysis calculation. An exact radius-three Hamming-ball convolution result concerns a different odd-dimensional missing layer, not this two-shore even-dimensional tensor structure. This is a bounded source comparison, not an exhaustive historical priority certificate.

## Limitations
The exact formula concerns complete bipartite graphs with both shores of size at least two; nothing is asserted about general graphs. The signed multiplier and its spectral support are included as necessary known inputs and not claimed original. The proof uses classical Krawtchouk identities and a known general projection minimization principle; the originality and value being asserted are the exact evaluated product for the natural vertex parity information-recovery problem and its sharply exponential endpoint instability. A hidden historical identity or unindexed equivalent formula remains a priority risk. There is no independent validation.

## References
1. G. Aalipour, A. M. Duval, W. Kook, K.-J. Lee, and J. L. Martin, *A weighted cellular matrix-tree theorem, with applications to complete colorful and cubical complexes*, arXiv:1510.00033 (first public 2015-09-30), especially Theorem 1.2 and Section 4. https://arxiv.org/abs/1510.00033
2. J. Ge and Y. Yu, *The bipartite analogue of a classical spanning tree enumeration formula, Boolean functions, and their applications to counting odd spanning trees*, arXiv:2602.13750 (first public 2026-02-14), especially Theorem 3.2 and Section 4. https://arxiv.org/abs/2602.13750
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, and S. Muro, *Asymptotic insights for projection, Gordon--Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233 (first public 2023-02-01), especially Theorem 3.1. https://arxiv.org/abs/2302.00233
4. P. Feinsilver and R. Schott, *Krawtchouk transforms and convolutions*, arXiv:1409.4715 (first public 2014-09-16), for classical Fourier/Krawtchouk background. https://arxiv.org/abs/1409.4715
