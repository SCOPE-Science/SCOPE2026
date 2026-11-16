# Parity jump in the sharp range-projection norms of \(K_{2,n}\) spanning-tree convolution

## Finding
Let \(n\ge 2\), let \(H_n=\mathbb F_2^{E(K_{2,n})}\cong\mathbb F_2^{2n}\), and let \(f_n\) be the indicator of the edge-incidence vectors of spanning trees of \(K_{2,n}\). Use the **unnormalized** Walsh transform
\[
\widehat f_n(\omega)=\sum_{x\in H_n}f_n(x)(-1)^{\omega\cdot x}.
\]
Let \(\Omega_n=\{\omega\in H_n:\widehat f_n(\omega)\ne0\}\), and let \(\Pi_n\) be the (translation-invariant) Fourier projection with multiplier \(\mathbf1_{\Omega_n}\). Then
\[
|\Omega_n|=(n+1)2^n-\mathbf1_{2\mid n}\binom{n}{n/2}.
\]
The exact sharp endpoint operator norms are
\[
\boxed{\ \|\Pi_n\|_{\ell^1(H_n)\to\ell^1(H_n)}=\|\Pi_n\|_{\ell^\infty(H_n)\to\ell^\infty(H_n)}=\begin{cases}
\dfrac{(n+1)\binom{n}{(n-1)/2}}{2^n},& n\text{ odd},\\[2mm]
\dfrac{\binom{n}{n/2}(n+2^{n/2})}{2^n}-\left(\dfrac{\binom{n}{n/2}}{2^n}\right)^2,& n\text{ even}.
\end{cases}\ }
\]
The underlying multiplier support and singular-value distribution were established in earlier work; they are recalled below as inputs and are **not claimed as new here**. The new result is the exact norm of the projection onto that support, including its parity jump. In particular, along odd and even dimensions respectively,
\[
\|\Pi_n\|\sim \sqrt{\frac{2n}{\pi}},\qquad
\|\Pi_n\|\sim 2^{n/2}\sqrt{\frac{2}{\pi n}}.
\]
Thus the sharp endpoint amplification grows polynomially for odd \(n\) and exponentially for even \(n\), despite both frequency supports occupying exponentially small fractions of \(H_n\).

For clarity about the underlying previously known support, the nonzero singular values of unnormalized convolution \(C_n:g\mapsto f_n*g\) can be described as follows. At frequencies where the two edge signs differ in exactly one column, the absolute multiplier equals \(2^{n-1}\), occurring \(n2^n\) times. At frequencies where both edge signs agree in every column, the absolute multipliers are \(2^{n-1}|n-2j|\), with multiplicity \(\binom nj\) for each \(0\le j\le n\), excluding the zero level when \(n\) is even. All other multipliers vanish. Consequently, the smallest positive singular value is \(2^{n-1}\), the largest is \(n2^{n-1}\), and \(\|C_n^\dagger\|_{2\to2}=2^{1-n}\); the condition number on the nonzero spectral subspace is \(n\). Here \(C_n^\dagger\) is the Moore--Penrose pseudoinverse.

## Assumptions and scope
For the bipartition \(\{u_0,u_1\}\sqcup\{v_1,\ldots,v_n\}\), index the two edges incident to \(v_i\) by \((0,i)\) and \((1,i)\). A Fourier frequency has signs \(s_i=(-1)^{\omega_{0i}}\) and \(t_i=(-1)^{\omega_{1i}}\), each in \(\{\pm1\}\). The counting measure on \(H_n\) is unnormalized. The projection \(\Pi_n\) is **onto the nonvanishing spectrum of the tree indicator**, equivalently onto the range of its convolution operator; it is not the Fourier projection whose frequency set is the set of spanning-tree vectors itself. All claims hold for every integer \(n\ge2\), without unproved genericity assumptions. The convention \(\|\Pi_n\|\) in asymptotic formulas refers to either equal endpoint norm.

## Proof
**1. Signed tree enumerator.** In any spanning tree of \(K_{2,n}\), exactly one vertex \(v_j\) is incident to both bipartition vertices \(u_0,u_1\), while every other \(v_i\) has degree one. Indeed, all \(v_i\) must have degree at least one and the total number of edges is \(n+1\); two degree-two columns would form a four-cycle. Conversely, every such choice yields a spanning tree. It follows that
\[
W_n(s,t):=\widehat f_n(\omega)=\sum_{j=1}^n s_jt_j\prod_{i\ne j}(s_i+t_i).
\]
Let \(k=|\{i:s_i\ne t_i\}|\). If \(k\ge2\), every summand vanishes. If \(k=1\) with unique index \(j\), then
\[
W_n(s,t)=-2^{n-1}\prod_{i\ne j}s_i.
\]
If \(k=0\), then
\[
W_n(s,s)=2^{n-1}\left(\prod_{i=1}^ns_i\right)\left(\sum_{i=1}^ns_i\right).
\]
These known multiplier formulas are rederived here only to identify the precise frequency set whose **different projection norm** is evaluated. For each fixed disagreement subset the \(n\) initial signs are arbitrary. For odd \(n\), no agreeing-sign frequency is zero; for even \(n\), exactly \(\binom{n}{n/2}\) agreeing-sign frequencies have balanced signs. This proves the rank, nonzero singular-value, and pseudoinverse claims.

**2. Fourier kernel for the full radius-one disagreement support.** Parametrize \(t_i=s_ic_i\). Let \(\Omega'_n\) comprise all sign pairs for which at most one \(c_i\) is negative. For a test point \((u,v)\in\mathbb F_2^n\times\mathbb F_2^n\), set
\[
K'_n(u,v)=\sum_{\omega\in\Omega'_n}(-1)^{\omega\cdot(u,v)}.
\]
Summation over the independent signs \(s_i\) gives
\[
K'_n(u,v)=2^n\mathbf1_{u=v}\left(n+1-2|v|\right),
\]
where \(|v|\) is Hamming weight. Indeed, the sum in the disagreement variables is \(1+\sum_i(-1)^{v_i}\). For odd \(n\), \(\Omega_n=\Omega'_n\).

**3. The balanced-shell correction in even dimension.** Set \(n=2m\), \(C=\binom{2m}{m}\). The actual support \(\Omega_n\) omits from \(\Omega'_n\) precisely the \(C\) agreeing-sign frequencies with \(\sum_i s_i=0\). Their Fourier kernel at \((u,v)\) depends only on \(r=|u+v|\):
\[
B_r=\sum_{\substack{s\in\{\pm1\}^{2m}\\\sum_i s_i=0}}\prod_{i=1}^{2m}s_i^{u_i+v_i}.
\]
Summing first over balanced sign vectors and then over coordinate subsets gives the exact polynomial identity
\[
\sum_{r=0}^{2m}\binom{2m}{r}B_r z^r
=\binom{2m}{m}(1-z^2)^m.
\]
Thus \(B_r=0\) for odd \(r\), while
\[
\binom{2m}{2j}|B_{2j}|=C\binom mj\quad(0\le j\le m).
\]
Hence the actual unnormalized projection kernel is
\[
K_n(u,v)=2^n\mathbf1_{u=v}(n+1-2|v|)-B_{|u+v|}.
\]
For \(u\ne v\), its absolute-value sum over all \((u,v)\) is
\[
2^n\sum_{r=1}^{n}\binom nr|B_r|=2^n C(2^m-1).
\]
For \(u=v\), \(B_0=C\) and \(0<C<2^n\). Because \(n+1-2|v|\) is an odd integer, subtracting \(C\) cannot change its sign. The elementary binomial identities
\[
\sum_{j=0}^n\binom nj|n+1-2j|=(n+1)\binom n{\lfloor n/2\rfloor},
\qquad
\sum_{j=0}^{2m}\binom{2m}{j}\operatorname{sgn}(2m+1-2j)=C
\]
therefore give the diagonal absolute-value sum \(2^n(n+1)C-C^2\). The first identity follows by splitting the binomial sum at \(\lfloor n/2\rfloor\), using \(j\binom nj=n\binom{n-1}{j-1}\), and applying binomial symmetry. The second is simply the central-binomial excess of the lower half over the upper half.

**4. Sharp norm and asymptotics.** The convolution kernel of \(\Pi_n\) is \(2^{-2n}K_n\). By the triangle inequality and testing a sign function on the kernel, its exact \(\ell^1\) and \(\ell^\infty\) norms both equal \(2^{-2n}\sum_{u,v}|K_n(u,v)|\). In odd dimension only the \(2^n\) diagonal entries in step 2 contribute, yielding the odd formula by the first binomial identity. In even dimension the diagonal and off-diagonal sums from step 3 yield
\[
2^{-2n}\left(2^n C(n+2^m)-C^2\right)
=\frac{C(n+2^{n/2})}{2^n}-\frac{C^2}{2^{2n}}.
\]
Stirling's central-binomial estimate \(\binom n{\lfloor n/2\rfloor}/2^n\sim\sqrt{2/(\pi n)}\) gives the two asymptotic regimes. All equalities are exact prior to taking limits.

## Verification
The standalone `check.py` exhaustively enumerates spanning trees as acyclic connected edge subsets (rather than using the degree-pattern proof), calculates the entire unnormalized Walsh transform by an integer butterfly algorithm, and compares all multipliers with the signed-tree expression and its closed cases for \(2\le n\le8\). For those dimensions it independently computes the projection kernel and both exact norm formulas, as rational numbers. Balanced-shell coefficients are also checked directly through even dimension 50. Run `python3 check.py` with standard Python 3; success ends with `K2N_TREE_SUPPORT_EXACT_CHECKS_PASS`. Finite checks corroborate but are not a proof of the all-dimensional statement.

## Relationship to prior work
Weighted spanning-tree enumerators of complete bipartite and complete colorful complexes are classical. Aalipour–Duval–Kook–Lee–Martin (2015, Theorem 1.2 and Section 4) give a **degree-weighted** multipartite tree enumerator, not an all-independent-edge-sign Walsh support or a norm of the projection onto that support. Liu–Huang (2010, pp. 289–300) study rooted complete-bipartite forests; their enumerative formulas do not classify edge-sign cancellations. Dong–Ge (2021, Sections 1 and 3–5) count trees containing a prescribed forest, which can be used in inclusion–exclusion to evaluate particular signed sums; the inspected statements do not provide the support geometry or its sharp endpoint projection norm.

The distinction between a Fourier projection **indexed by spanning-tree vectors** and the projection onto the **nonzero transform support** is essential. An earlier exact result for **this same** \(K_{2,n}\) family already determines all Walsh multipliers, zero sets, ranks, and the norm of the projection indexed by spanning-tree vectors; **none of those results is claimed as original here**. The new assertion is the exact sharp norm of the **range projection** \(\Pi_n\), which is a different operator, and its polynomial-versus-exponential parity transition. The known support classification is necessary input, but does not by itself evaluate the absolute kernel summation required for this norm. Existing \(K_{3,n}\) tree-incidence projections are likewise distinct.

## Limitations
The claim addresses the thin complete-bipartite family \(K_{2,n}\) for \(n\ge2\), not arbitrary \(K_{m,n}\). The endpoint theorem concerns the range projection, not the size of the inverse on \(\ell^1\) or \(\ell^\infty\). The range-projection norm formula is proved mathematically here but not independently validated. The previously known exact Walsh support and convolution rank are explicitly excluded from the novelty assertion. Historical priority for the **new norm formula** is based on bounded comparisons, not an exhaustive search; an older equivalent norm formula for the punctured radius-one support remains possible. A general fixed-forest enumeration could lead to this claim after additional explicit calculation, but the examined sources do not state the endpoint projection norm.

## References
1. G. Aalipour, A. M. Duval, W. Kook, K.-J. Lee, J. L. Martin, *A weighted cellular matrix-tree theorem, with applications to complete colorful and cubical complexes* (first arXiv release 2015-09-30), arXiv:1510.00033, especially Section 4. https://arxiv.org/abs/1510.00033
2. B. Liu, F. Huang, *Enumeration for no-trivial spanning forests of complete bipartite graphs*, Ars Combinatoria 97 (2010), 289–300, especially pp. 289, 291, 294, 297, 299. https://combinatorialpress.com/ars-articles/volume-097-ars-articles/enumeration-for-no-trivial-spanning-forests-of-complete-bipartite-graphs/
3. F. Dong, J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest* (first arXiv release 2021-03-09), arXiv:2103.05294, Sections 1, 3–5. https://arxiv.org/abs/2103.05294
