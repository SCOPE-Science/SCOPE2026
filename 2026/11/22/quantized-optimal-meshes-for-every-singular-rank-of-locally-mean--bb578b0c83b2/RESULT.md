# Quantized optimal meshes for every singular rank of locally mean-corrected Volterra integration

## Finding

Let \(J:L^2(0,1)\to L^2(0,1)\) be the Volterra integration operator, \((Jf)(x)=\int_0^x f(t)\,dt\). Fix an integer \(N\ge1\), and any partition \(0=x_0<x_1<\cdots<x_N=1\) with cell lengths \(h_j=x_j-x_{j-1}>0\). Let \(P\) be the orthogonal projection onto functions constant on each cell, and \(T_{\boldsymbol h}=J(I-P)\). Then its complete nonzero singular multiset, including multiplicities, is

\[
\left\{\frac{h_j}{\pi m}: j=1,\ldots,N,\ m=1,2,\ldots\right\}.
\]

For **every** integer \(k\ge1\), there is an attained sharp mesh-design law

\[
\boxed{\ \min_{h_j>0,\ \sum_{j=1}^N h_j=1}s_k(T_{\boldsymbol h})=\frac{1}{\pi(N+k-1)}\ }.
\]

**All** minimizing ordered meshes are exactly

\[
\boxed{\ h_j=\frac{a_j}{N+k-1},\quad a_j\in\mathbb Z_{\ge1},\quad \sum_{j=1}^{N}a_j=N+k-1.\ }
\]

There are \(\binom{N+k-2}{N-1}\) such ordered minimizing length vectors. Uniform lengths are optimal for rank \(k\) if and only if \(k\equiv1\pmod N\); thus, for every \(N\ge2\), the optimal second-rank mesh has exactly one cell of length \(2/(N+1)\), with the other \(N-1\) cells of length \(1/(N+1)\). It reduces \(s_2\) from the uniform value \(1/(\pi N)\) to \(1/[\pi(N+1)]\), although it increases the operator norm.

For every real \(p>1\), the exact Schatten identity is

\[
\|T_{\boldsymbol h}\|_{\mathcal S_p}^p
=\frac{\zeta(p)}{\pi^p}\sum_{j=1}^N h_j^p,
\]

with unique mesh minimizer \(h_1=\cdots=h_N=1/N\). No such operator belongs to \(\mathcal S_p\) for \(0<p\le1\). This provides an exact contrast between individual singular-rank design and every global Schatten criterion.

## Assumptions and scope

All Hilbert spaces are the usual real or complex, unweighted Lebesgue \(L^2(0,1)\). The number of cells \(N\) and target singular rank \(k\) are arbitrary fixed positive integers. Every mesh cell has strictly positive length and the cells fill \([0,1]\). The projection \(P\) removes the **local** cell mean, not the global mean or a polynomial on the full interval. Singular numbers are listed in nonincreasing order with multiplicity, equivalently \(s_k(T)=\inf_{\operatorname{rank}R<k}\|T-R\|\). There are infinitely many positive singular values for every such mesh, so all ranks exist.

## Proof

**1. Complete orthogonal decomposition.** Denote the cells by \(I_j=(x_{j-1},x_j)\). For every \(g=(I-P)f\), the integral over each cell vanishes. Consequently the cumulative integral of \(g\) is zero at *every* cell endpoint. For \(x\in I_j\),

\[
(T_{\boldsymbol h}f)(x)=\int_{x_{j-1}}^x (f(t)-h_j^{-1}\!\int_{I_j}f)\,dt.
\]

Thus, relative to the orthogonal decomposition \(L^2(0,1)=\bigoplus_j L^2(I_j)\), the operator is the direct sum of one-cell operators \(S_{h_j}g(x)=\int_0^x(g(t)-h_j^{-1}\int_0^{h_j}g)\,dt\). On the cell of length \(h\), the constant function is in the kernel; the normalized cosines \(e_m(x)=\sqrt{2/h}\cos(m\pi x/h)\), \(m\ge1\), form an orthonormal basis of the zero-mean subspace. Each is mapped to \((h/(m\pi))\sqrt{2/h}\sin(m\pi x/h)\). These normalized sines are an orthonormal basis of the output \(L^2(0,h)\). This is a complete singular-value decomposition with singular values \(h/(m\pi)\). Direct summation over cells proves the multiset formula, compactness and its precise multiplicities.

**2. Rank counting lower bound.** Fix \(k\ge1\), an arbitrary mesh, and any \(t\ge s_k(T_{\boldsymbol h})>0\). Set

\[
q_j=\#\{m\in\mathbb N:h_j/(m\pi)>t\}
=\left\lceil\frac{h_j}{\pi t}\right\rceil-1.
\]

Only at most \(k-1\) singular values are strictly larger than \(t\), so \(\sum_j q_j\le k-1\). By the ceiling definition, \(h_j\le\pi t(q_j+1)\). Summing these inequalities gives

\[
1=\sum_jh_j\le\pi t\sum_j(q_j+1)\le\pi t(N+k-1).
\]

Taking \(t=s_k(T_{\boldsymbol h})\) proves the universal lower bound \(s_k\ge1/[\pi(N+k-1)]\), including repeated singular values at the threshold.

**3. Equality and all minimizers.** Put \(D=N+k-1\) and \(t_*=1/(\pi D)\). Every positive integer composition \(D=a_1+\cdots+a_N\) gives lengths \(h_j=a_j/D\). Then \(q_j=a_j-1\) singular values on that cell are strictly greater than \(t_*\), and their total is \(D-N=k-1\). At least \(N\) singular values equal \(t_*\), one for each cell; hence \(s_k=t_*\). Conversely, if \(s_k=t_*\), the two preceding summed inequalities have the same endpoint \(1\). They therefore force \(\sum_jq_j=k-1\) **and** equality in each individual \(h_j\le(q_j+1)/D\). Thus \(h_j=(q_j+1)/D\), with positive integer numerators summing to \(D\). This proves necessity, sufficiency and the number of ordered compositions \(\binom{D-1}{N-1}\).

For a uniform mesh the singular values \(1/(\pi Nm)\) each occur with multiplicity \(N\); hence \(s_k=1/[\pi N\lceil k/N\rceil]\). Equality with the optimal value holds precisely when \(N\lceil k/N\rceil=N+k-1\), equivalently \(k\equiv1\pmod N\). The second-rank example follows by taking compositions of \(N+1\) into \(N\) positive parts.

**4. Exact Schatten contrast.** For any fixed mesh and \(p>0\), the sum of the \(p\)-th powers of singular values equals

\[
\sum_{j=1}^N\sum_{m=1}^{\infty}\left(\frac{h_j}{\pi m}\right)^p.
\]

It diverges for \(p\le1\); for \(p>1\) the separable series is \(\zeta(p)\pi^{-p}\sum_j h_j^p\). Strict convexity of \(u\mapsto u^p\), followed by Jensen's inequality at the fixed total length, proves \(\sum_jh_j^p\ge N^{1-p}\), with equality only when every cell is of length \(1/N\). In particular, \(\|T_{\boldsymbol h}\|_{\mathcal S_2}^2=\sum_j h_j^2/6\). This finishes all claims.

## Verification

The standalone \(\texttt{check_spectrum.py}\) uses exact rational arithmetic to enumerate positive compositions, compare the \(k\)-th singular value of each finite tested mesh against the universal threshold, check the strict-value counting formula, and verify equality rigidity on sampled rational meshes. It reports **55,907 exact assertions passed** when run with standard Python 3. The checks include all positive integer compositions for \(1\le N\le5\), \(1\le k\le8\), additional rational partitions, and the two-cell second-rank contrast. These finite checks corroborate the statements; the analytical proof establishes all meshes and all ranks. To reproduce, run \(\texttt{python check_spectrum.py}\). The numerical value of \(\pi\) is not used in the exact comparisons: the code orders the rational quantities \(\pi s_k\).

## Relationship to prior work

Edmunds and Lang (2015, arXiv:1504.02515v1) study approximation and other \(s\)-numbers for Sobolev embeddings and a second-order Volterra-type integral operator, and explicitly note the classical exact first-derivative Dirichlet embedding values on a single interval. Lyubich and Tsedenbayar (2010) derive boundary-value formulations and singular values for polynomials of the unrestricted classical Volterra operator. Neither inspected primary text gives a cellwise-mean-corrected first-order Volterra singular multiset or optimizes its **every indexed singular value** over arbitrary positive meshes. Boykov and Tynda (2013, arXiv:1306.2904v1) construct width-optimal local splines for weakly singular Volterra equations, with error **orders** in different function classes rather than an exact indexed operator-singular mesh law.

The closely relevant published study *Exact Sobolev widths from discontinuous affine splines and a sharp mesh law* analyzes the \(H^1\)-to-\(L^2\) error of **cellwise affine projection**, not integration after **cellwise constant** projection; its sharp global first-derivative bound is \(\max_j h_j/(2\pi)\) and is not an all-index spectral mesh optimization. An earlier study of global Legendre moment-annihilated Volterra integration addresses a single global polynomial projector rather than local means and does not imply the direct-sum spectrum or integer-mesh equality set. The spectral calculation uses standard cosine/sine and Dirichlet eigenfunction methods; novelty is claimed narrowly for the combined every-rank mesh optimization and its exact rigidity/tradeoff, not for these classical ingredients.

## Limitations

The result is for unweighted \(L^2\), ordinary first-order Volterra integration, orthogonal **cellwise constant** projection and a finite number of strictly positive intervals. It does not cover continuous spline projections, weighted kernels, higher-order antiderivatives, or optimizing simultaneous vector objectives. Earlier unindexed equivalent statements in classical spectral-partition literature may exist; no independent mathematical validation has been performed. The finite checker is not an infinite proof.

## References

- D. E. Edmunds and J. Lang, *Asymptotic formulae for s-numbers of a Sobolev embedding and a Volterra type operator*, arXiv:1504.02515v1, first posted 9 April 2015. https://arxiv.org/abs/1504.02515
- Y. Lyubich and D. Tsedenbayar, *The norms and singular numbers of polynomials of the classical Volterra operator in \(L^2(0,1)\)*, Studia Mathematica 199 (2010), 171–184. https://doi.org/10.4064/sm199-2-3
- I. V. Boykov and A. N. Tynda, *Numerical Methods of Optimal Accuracy for Weakly Singular Volterra Integral Equations*, arXiv:1306.2904v1, first posted 12 June 2013. https://arxiv.org/abs/1306.2904
- *Exact Sobolev widths from discontinuous affine splines and a sharp mesh law*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-sobolev-widths-from-discontinuous-affine-splines-and-a-sha--620798593d20
