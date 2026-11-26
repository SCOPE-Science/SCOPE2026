# Sharp negative-type thresholds and balancing for diameter-three tree metrics

## Finding

Let \(T_{m,n}\) be the unweighted double-star tree with two adjacent hubs, \(m\ge 1\) pendant leaves at one hub and \(n\ge 1\) at the other. The family \(T_{m,n}\) comprises all finite trees of diameter exactly three. For \(p\ge0\), say that the metric \(d\) has \(p\)-negative type if

\[
\sum_{x,y\in T_{m,n}}c_xc_y d(x,y)^p\le0
\quad\text{whenever}\quad \sum_xc_x=0,
\]

with strict negative type when equality forces all coefficients to vanish. Distances between distinct vertices are positive, and diagonal entries are taken to be zero also when \(p=0\).

For \(m+n>2\), put \(s=\log_2 3\). There exists exactly one number \(q_{m,n}\) in the interval

\[
2<q_{m,n}<2+\frac{2}{\max\{m,n\}}
\]

solving

\[
q_{m,n}\sqrt{\left(2+\frac2m-q_{m,n}\right)
\left(2+\frac2n-q_{m,n}\right)}
=2q_{m,n}^{\,s}-2-q_{m,n}^{\,2}.
\]

The supremal negative-type exponent is exactly \(\wp(T_{m,n})=\log_2q_{m,n}\). The metric has strict \(p\)-negative type for \(0\le p<\wp\), nonstrict \(p\)-negative type at \(p=\wp\), and fails \(p\)-negative type for \(p>\wp\). At the endpoint, the zero-sum distance quadratic form has a one-dimensional kernel. Therefore, the minimum affine Hilbert dimension for an isometric embedding of \((T_{m,n},d^{\wp/2})\) is \(m+n\); it is \(m+n+1\) for every strictly smaller positive exponent.

The exceptional tree \(T_{1,1}\) is the four-vertex path and has \(\wp(T_{1,1})=2\), with a one-dimensional Euclidean embedding at its endpoint.

For each fixed \(S=m+n\ge3\), the critical exponent is strictly increasing with the product \(mn\). Thus its **minimum** occurs at \(\{m,n\}=\{1,S-1\}\), and its **maximum** at the most balanced partition \(\{m,n\}=\{\lfloor S/2\rfloor,\lceil S/2\rceil\}\). If \(m=n=k\), the endpoint equation simplifies to

\[
3^{\wp(T_{k,k})}-\left(1+\frac1k\right)2^{\wp(T_{k,k})}=1,
\]

and, as \(k\to\infty\),

\[
\wp(T_{k,k})=1+\frac{2}{(3\log3-2\log2)k}+O(k^{-2}).
\]

For the two partitions of four leaves, \(\wp(T_{1,3})\simeq1.4079824968\) while \(\wp(T_{2,2})\simeq1.5165843743\).

## Assumptions and scope

The graph is finite, connected, simple and unweighted. Every leaf is incident to exactly one of the two adjacent hubs, and \(m,n\) are positive integers. The metric is shortest-path graph distance. Coefficients in the negative-type condition are real. The same theorem covers the corresponding generalized-roundness invariant by the established equivalence of generalized roundness and negative type. The symbol \(q=2^p\) is only an auxiliary positive real variable, and \(s=\log_2 3\), so \(3^p=q^s\).

## Proof

**1. Exact zero-sum decomposition.** Denote the two leaf classes by \(A\) and \(B\). For a zero-total-mass real vector \(c\), set \(a=\sum_{i\in A}c_i\), \(b=\sum_{j\in B}c_j\) and decompose the leaves as \(c_i=a/m+\xi_i\), \(c_j=b/n+\eta_j\), where \(\sum_i\xi_i=\sum_j\eta_j=0\). Put the coefficients on the first and second hubs equal to \(z-a\) and \(-z-b\), respectively. Every zero-sum vector has precisely this representation.

For \(q=2^p\) and \(r=3^p\), direct expansion using distances \(1\), \(2\), and \(3\) gives the exact identity

\[
\begin{aligned}
\mathcal Q_p(c)&:=\sum_{x,y}c_xc_y d(x,y)^p\\
&=-q\left(\sum_i\xi_i^2+\sum_j\eta_j^2\right)
-2\left(z-\frac{(2-q)(a-b)}2\right)^2\\
&\quad-\frac12\left[q A_m(q)a^2-2F(q)ab+qA_n(q)b^2\right],
\end{aligned}
\]

where

\[
A_m(q)=2+\frac2m-q,\qquad
A_n(q)=2+\frac2n-q,\qquad
F(q)=2q^{s}-2-q^2.
\]

Consequently \(p\)-negative type is exactly the positive-semidefiniteness condition for the real symmetric matrix

\[
H(q)=\begin{pmatrix}qA_m(q)&-F(q)\\-F(q)&qA_n(q)\end{pmatrix}.
\]

Indeed, the other square and fluctuation terms are nonpositive, and they can be made zero for arbitrary \((a,b)\) by choosing \(\xi=\eta=0\) and the indicated minimizing \(z\). In particular, this is a necessary and sufficient reduction, not merely a sufficient estimate.

**2. A unique first crossing.** For \(2\le q<q_c:=2+2/\max\{m,n\}\), the two diagonal terms in \(H(q)\) are positive. Also \(F(2)=0\) and \(F\) is strictly increasing on \([2,3]\). To verify the latter without a numerical estimate, write \(s=\log_2 3\). The integer inequalities \(3^{12}>2^{19}\) and \((19/12)^{12}>3^5\) yield

\[
s>\frac{19}{12}>3^{5/12}>3^{2-s}.
\]

Thus \(F'(q)=2q^{s-1}(s-q^{2-s})>0\) for \(2\le q\le3\), because \(2-s>0\).

Set \(g(q)=q\sqrt{A_m(q)A_n(q)}\). Its logarithmic derivative is

\[
\frac{g'(q)}{g(q)}=\frac1q-\frac12\left(\frac1{A_m(q)}+\frac1{A_n(q)}\right)
\le\frac12-\frac{m+n}{4}<0
\]

when \(m+n>2\). At \(q=2\) one has \(g(2)>F(2)=0\), while at \(q=q_c\le3\) one has \(g(q_c)=0<F(q_c)\). Hence there is a unique \(q_{m,n}\) with \(g(q)=F(q)\). The determinant \(\det H(q)=g(q)^2-F(q)^2\) is positive before and negative immediately after this crossing. This proves strict negative type from \(p=1\) up to but not including \(\log_2 q_{m,n}\), and nonstrict negative type at the crossing. The classical strict-nesting and interval properties of negative type extend these assertions down to \(p=0\) and rule out any return of negative type at larger exponents. At equality \(H(q)\) has rank one, whereas the other squares are strictly negative away from their equality subspaces. Therefore the full zero-sum quadratic form has exactly one null direction.

By Schoenberg's Hilbert embedding characterization, the centered Gram matrix for the squared metric \(d^p\) is minus one-half of the centered distance matrix. Its rank is the minimum affine Hilbert embedding dimension, giving \(m+n\) at the unique critical eigenvalue and \(m+n+1\) below it. When \(m=n=1\), the four vertices lie on a straight line at consecutive integers, so the endpoint is exactly \(p=2\), with no larger negative-type exponent.

**3. Strict balancing at a fixed number of leaves.** Put \(S=m+n\ge3\) and \(t=q-2\). The exact identity

\[
A_m(q)A_n(q)=t^2+\frac{4-2St}{mn}
\]

makes the product \(mn\) the only parameter that can vary when \(S\) is fixed. At \(q_0=2+2/S\), the left side in the defining crossing equation is \(g(q_0)=2q_0/S>2/S\). Convexity of \(u\mapsto u^p\) for \(p=\log_2q_0>1\), applied to the midpoint \(3=(2+4)/2\), gives

\[
F(q_0)=2\cdot3^p-2-q_0^2<q_0-2=\frac2S.
\]

Thus every crossing satisfies \(q_{m,n}>q_0\), so \(t>2/S\). In this range \(4-2St<0\), making \(A_mA_n\), and hence \(g\), strictly increase with the product \(mn\) wherever defined. Since \(F\) increases and \(g\) decreases with \(q\), the crossing must occur strictly later when \(mn\) increases. Among positive integer partitions of a fixed sum, the unique minimizer of the product (up to order) is \(1,S-1\), while the maximum is the balanced partition. This proves the balancing conclusion.

**4. Equal-blade asymptotics.** For \(m=n=k\), the crossing equation becomes \(q(2+2/k-q)=2q^{s}-2-q^2\), equivalently \(3^p-(1+1/k)2^p=1\). At \(k^{-1}=0\), \(p=1\) is a simple root, with derivative \(3\log3-2\log2>0\). The implicit-function theorem yields the stated expansion.

## Verification

The standalone file `checker.py` constructs each full shortest-path distance matrix independently, computes the zero-sum quadratic form on a basis, and compares its eigenvalue signs against the defining equation. It additionally checks the complete square identity with random real coefficients, exact balancing direction across positive partitions, and the equal-blade asymptotic coefficient. All 1845 supplementary numerical assertions passed. The supplementary finite experiments are not a proof of the statements for all positive integer parameters; the preceding algebraic arguments establish their infinite-family scope. Run with a Python installation containing NumPy using `python checker.py`.

## Relationship to prior work

Negative type and Hilbert snowflake embeddings are classical; the equivalence and strict exponent nesting are used rather than claimed. Sánchez (2011) gives a general finite-metric distance-matrix criterion and computes complete bipartite graph examples. Caffarelli, Doust and Weston (2010) derive bounds and tree examples, and emphasize the difficulty of exact generalized-roundness values on finite trees. Levy-Moore, Nichols and Weston (2016) study comparisons of generalized roundness for metric spaces, including tree-like geometry. Robertson (2023) develops negative-type and bi-Lipschitz embedding theory and computes complete bipartite and Hamming examples. The present claimed new statement is the explicit all-parameter double-star threshold, its unique critical rank loss, and the strict balancing law; it is not the general matrix method, the graph-tree lower bound, or the classical negative-type/Hilbert equivalence.

## Limitations

The result concerns finite, unweighted diameter-three trees only; it does not solve arbitrary diameter-four or weighted trees, give the exact distortion of non-Hilbert-embeddable snowflakes, or supply independent historical priority confirmation. The defining root is exact but transcendental in general; no elementary closed form is claimed beyond the balanced reduction. A general finite-metric determinant criterion can algorithmically imply a threshold after potentially substantial case analysis, but does not by itself constitute this specific all-parameter scalar formula or balancing theorem. An unlocated alternative derivation in older negative-type or tree-generalized-roundness literature remains possible. No independent mathematical audit has been performed.

## References

1. Gavin Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, first posted September 27, 2023, arXiv:2309.16070, https://arxiv.org/abs/2309.16070.
2. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, first posted August 2, 2011, arXiv:1108.0451, https://arxiv.org/abs/1108.0451.
3. Elena Caffarelli, Ian Doust and Anthony Weston, *Metric trees of generalized roundness one*, first posted August 20, 2010, arXiv:1008.3418, https://arxiv.org/abs/1008.3418.
4. J. Levy-Moore, K. Nichols and A. Weston, *Comparing the generalized roundness of metric spaces*, first posted August 2016, arXiv:1608.03699, https://arxiv.org/abs/1608.03699.
5. I. J. Schoenberg, *Metric spaces and positive definite functions*, Trans. Amer. Math. Soc. 44 (1938), 522–536.
