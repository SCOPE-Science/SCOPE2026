# Sharp two-input energy stability and activation jumps for fractional maximal averaging on cliques

## Finding
For an unweighted complete graph with \(n\ge2\) vertices and \(0<\alpha<1\), let \(M_\alpha\) be the centered fractional Hardy–Littlewood maximal operator using counting measure. Write
\[
 c=n^{\alpha-1},\qquad
 K=\left\lceil c^{-1}\right\rceil-1,
 \qquad
 V_2(h)=\left(\sum_{1\le i<j\le n}|h_i-h_j|^2\right)^{1/2}.
\]
Then the **exact optimal two-input Euclidean-to-edge-variation bound**, for all complex vertex signals \(f,g\), is
\[
 \boxed{\;V_2(M_\alpha f-M_\alpha g)\le L_{n,\alpha}\|f-g\|_2,\quad
 L_{n,\alpha}^2=\max\left\{
 \max_{1\le k\le K}(n-k)\bigl[1+k c(nc-2)\bigr],\;
 n\mathbf1_{\{K\ge2\}}\right\}.\;}
\]
The bound is attained by distinct strictly positive real vertex signals for every admissible \(n,\alpha\). At \(c=1/2\) and \(n\ge3\), a strict downward jump of the sharp **squared** modulus occurs in all dimensions except \(n=5\):
\[
 \lim_{c\uparrow1/2}L_n(c)^2
 =\max\left\{n,\frac{n(n-1)}4,\frac{(n-2)^2}2\right\},
 \qquad L_n(1/2)^2=\frac{n(n-1)}4.
\]
For \(n=5\) the two values agree. In particular, at \(n=6\) they are \(8\) and \(15/2\), respectively. These are moduli for **differences of two nonlinear outputs** relative to a vertex Euclidean difference; they are not one-input graph-variation constants.

## Assumptions and scope
The graph is the simple undirected clique \(K_n\), each undirected edge is counted once, and vertex \(\ell^2\) is unnormalized. The fractional maximal function uses all distinct centered graph-distance balls; on a clique these are the singleton and the whole vertex set. Thus for arbitrary complex signals
\[
 (M_\alpha f)_i=\max\left\{|f_i|,\;c\sum_{j=1}^n|f_j|\right\}.
\]
The parameter lies strictly between \(0\) and \(1\), so \(1/n<c<1\), and \(K\) is a positive integer at most \(n-1\). The convention \(\mathbf1_{\{K\ge2\}}=0\) when \(K=1\) is used. For fixed \(n\) and \(c\), the constant is the supremum over all distinct complex input pairs; it is achieved on the positive real cone.

## Proof
**1. Reduction to a piecewise-linear nonnegative map.** Define \(T_c:[0,\infty)^n\to\mathbb R^n\) by \((T_cx)_i=\max\{x_i,c\sum_jx_j\}\). Since \(M_\alpha f=T_c(|f|)\) and \(\||f|-|g|\|_2\le\|f-g\|_2\) coordinatewise, it is enough to compute the global Euclidean-to-\(V_2\) Lipschitz modulus of \(T_c\) on the positive cone. Equality examples within that cone prove sharpness for the full complex domain.

**2. Feasible activation masks.** On an open cell, put \(S=\{i:x_i>c\sum_jx_j\}\) and \(k=|S|\). If \(k\ge1\), summing these strict inequalities yields \(kc<1\). Conversely, whenever \(1\le k\le K\), prescribe \(x_i=1\) on a chosen \(k\)-set and \(x_j=\varepsilon>0\) outside it. Taking \(\varepsilon\) sufficiently small makes precisely those \(k\) sites active, with both inequalities strict. The cell with \(k=0\) exists as \(nc>1\). Consequently, **the exact possible sizes of open-cell active sets are** \(0,1,\ldots,K\); there are no other open-cell masks.

**3. Jacobian and orthogonal modes.** On the cell corresponding to \(S\), the linear derivative \(J_S\) has row \(e_i^\top\) for \(i\in S\), and row \(c\mathbf1^\top\) for \(i\notin S\). Let \(\bar h_S=k^{-1}\sum_{i\in S}h_i\). Directly expanding complete-graph edge energy gives
\[
 V_2(J_Sh)^2=n\sum_{i\in S}|h_i-\bar h_S|^2
 +k(n-k)\left|\bar h_S-c\sum_{j=1}^nh_j\right|^2.
\]
For \(k=0\), the image is constant and has zero edge energy. For \(k\ge1\), set
\[
 u_i=\begin{cases}k^{-1}-c,&i\in S,\\-c,&i\notin S.\end{cases}
 \qquad \|u\|_2^2=k^{-1}-2c+nc^2.
\]
The active-site contrast space \(\{h:\operatorname{supp}h\subseteq S,\ \sum_{i\in S}h_i=0\}\) has dimension \(k-1\) and squared singular value \(n\) when \(k\ge2\). It is orthogonal to \(u\). The remaining nonzero squared singular value is the rank-one value
\[
 k(n-k)\|u\|_2^2
 =(n-k)\bigl[1+k c(nc-2)\bigr].
\]
The inactive contrasts and the remaining orthogonal two-level direction lie in the kernel. Hence the squared derivative norm is this latter value when \(k=1\), and its maximum with \(n\) when \(k\ge2\).

**4. Global bound and attainment.** Every segment in the positive cone meets finitely many affine cells unless it lies in a boundary hyperplane; a generic small perturbation of its endpoints resolves that case. On each cell, the preceding derivative norm bounds the \(V_2\) length of the output change by that norm times the Euclidean length of the input segment. The triangle inequality over the subsegments and continuity give a global constant equal to the maximum over all feasible cell derivatives. For the reverse inequality, fix an open cell whose derivative has maximal norm, take its strictly positive interior point supplied in Step 2, and add a sufficiently small nonzero multiple of a real norming singular vector. Both inputs remain strictly inside the same cell, so their output difference is **exactly** their Jacobian image and attains the sharp ratio. This proves the boxed formula for all \(n\), \(\alpha\) and complex input pairs.

**5. Jump at the two-site activation threshold.** If \(c=1/2\), the condition \(kc<1\) allows only \(k=1\) among nonzero masks; therefore the squared modulus is \((n-1)(1-1+n/4)=n(n-1)/4\). As \(c\uparrow1/2\) from below, the only nonzero mask sizes are \(1,2\) sufficiently near the endpoint. Their limiting rank-one values are \(n(n-1)/4\) and \((n-2)^2/2\), and the two-active-site contrast mode has value \(n\). Comparing these three expressions shows strict loss at the endpoint for \(n=3,4\) and every \(n\ge6\), but equality for \(n=5\). For completeness, at \(n=2\) the parameter \(c=1/2\) is outside the stated open interval.

## Verification
`CHECKER.py` uses only Python's standard library. Execute `python3 CHECKER.py`. It reconstructs every feasible branch Jacobian and its complete-edge Gram matrix with exact rational arithmetic for 214 parameter/mask cases, compares them to the active-contrast-plus-rank-one decomposition entrywise, checks local singular-vector equality witnesses, and tests 14,400 deterministic real pairs (including signed values passed through absolute value) plus 1,500 genuinely complex-input pairs. It also verifies the endpoint jump in 18 dimensions. Finite testing is supplementary: Steps 1–5 prove the all-dimensional statements, and the code neither purports to sample every parameter nor to certify historical novelty.

## Relationship to prior work
F. Liu, Y. Lian and Y. Wang (arXiv:2611.15377v1, Section 4 and Theorem 1.5) establish sharp **one-input** fractional graph-variation inequalities and use the same clique maximal-function formula, but their numerator involves one maximal output and their denominator is the input edge variation. González-Riquelme and Madrid (arXiv:2005.03146v3, Theorems 3 and 4) prove qualitative graph-BV continuity and sharp strong vertex \(\ell^2\) norms of individual maximal outputs, not an exact two-input Euclidean-to-edge quadratic stability modulus. The more recent Lu–Zhao analysis (arXiv:2611.24189v1, first public November 18, 2026) also addresses one-input graph variation and hence does not imply the present two-input formula. A published complete-graph two-input theorem for ordinary maximal averaging identifies a sharp **total-variation-to-total-variation** modulus when \(\alpha=0\); its input/output norm and parameter differ, and its value does not imply the present energy-to-variation law for \(0<\alpha<1\). The present active-mask feasibility threshold, spectral formula and dimension-specific jumps are not stated in those inspected materials.

## Limitations
This statement concerns complete graphs with counting measure, the Euclidean vertex input norm and the unnormalized quadratic edge-output seminorm, with \(0<\alpha<1\). It does not determine constants for other graph geometries or exponent pairs. The sharp constant is discontinuous as a *global* perturbation modulus at some activation thresholds despite pointwise continuity of the underlying maximal map in the parameter. Because distinct positive interior pairs already attain the supremum, no limiting or distributional interpretation is needed. An unindexed equivalent result or a stronger unpublished theorem cannot be excluded by the literature search. Independent mathematical verification has not been performed.

## References
1. F. Liu, Y. Lian and Y. Wang, *Sharp \(L^p\) and variation inequalities for maximal operators on finite connected graphs*, arXiv:2611.15377v1 (first public 2026-11-11), Theorem 1.5 and Section 4. https://arxiv.org/abs/2611.15377
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v3 (preprint first public 2020-05-06), Theorems 3 and 4. https://arxiv.org/abs/2005.03146
3. C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1 (first public 2026-03-12). https://arxiv.org/abs/2603.12462
4. S. Lu and F. Zhao, *Variational Estimates for the Fractional Maximal Operator on Finite Graphs*, arXiv:2611.24189v1 (first public 2026-11-18; later contextual comparison only). https://arxiv.org/abs/2611.24189
5. *Sharp two-input graph-variation modulus of the centered maximal operator on complete graphs* (public 2026 research record): https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-two-input-graph-variation-modulus-of-the-centered-maximal--1a9c9a4ca51f
