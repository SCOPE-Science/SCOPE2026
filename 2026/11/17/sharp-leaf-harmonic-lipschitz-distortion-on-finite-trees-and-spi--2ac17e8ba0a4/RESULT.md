# Sharp leaf-harmonic Lipschitz distortion on finite trees and spiders

## Finding

Let \(T=(V,E)\) be any finite unweighted tree with at least two vertices and leaf set \(B\). Let \(H_T\) be the real linear Dirichlet extension operator: it copies boundary data at the leaves and is graph-harmonic at every other vertex. Equip real functions modulo constants on \(B\) and \(V\) with their graph-distance Lipschitz seminorms. Its sharp operator norm admits the finite cut formula
\[
\|H_T\|_{\mathrm{Lip}(B)\to\mathrm{Lip}(V)}
=\max_{uv\in E}\sum_{e\in E}
\left|\sum_{b\in B\cap C_e}(\mu_u(b)-\mu_v(b))\right|,
\]
where \(C_e\) is either component of \(T\setminus e\), and \(\mu_v\) is the leaf-hitting distribution of simple random walk started at \(v\). This operator is nonexpansive **if and only if** \(T\) is a path.

For a spider with \(m\ge3\) arms of positive integer lengths \(L_1,\ldots,L_m\), the exact norm simplifies to
\[
\boxed{\|H_T\|=1+\frac{m-2}{L_{\min}\sum_{i=1}^m L_i^{-1}}.}
\]
The nonconstant norming boundary data are precisely \(f(b_j)=c+\varepsilon\,d_T(b_i,b_j)\), where \(\varepsilon\ne0\) and \(b_i\) is a leaf on a shortest arm (with the natural normalization when taking the operator-norm supremum).

Among spiders with exactly \(n\ge4\) vertices and exactly \(3\le m\le n-1\) arms, the norm is largest precisely when one arm has length one and the other \(m-1\) lengths differ by at most one. Writing \(n-2=q(m-1)+r\), \(0\le r<m-1\), its maximum is
\[
\boxed{\Lambda_{n,m}=1+\frac{m-2}{1+(m-1-r)/q+r/(q+1)}.}
\]
The maximum \(\Lambda_n=\max_{3\le m\le n-1}\Lambda_{n,m}\) over all \(n\)-vertex spiders obeys
\[
\boxed{\lim_{n\to\infty}\frac{\Lambda_n}{\sqrt n}=\frac12,\qquad
\Lambda_n<1+\frac{\sqrt{n-2}}2.}
\]
Thus a *fixed, linear, energy-minimizing* extension rule can have unbounded Lipschitz distortion despite the existence of nonlinear norm-preserving extensions of the same data.

## Assumptions and scope

Every graph is a finite, simple, connected, unweighted tree. Leaf means degree one; for the one-edge tree both endpoints are leaves. For a vertex subset \(S\), let
\[
\operatorname{Lip}_S(f)=\max_{x\ne y\in S}\frac{|f(x)-f(y)|}{d_T(x,y)}.
\]
For \(S=V\) this is equivalent to maximizing absolute differences across individual edges. The domain and codomain are real functions modulo additive constants. For every \(f:B\to\mathbb R\), \(H_T f\) is the unique extension with \(H_T f(v)=\deg(v)^{-1}\sum_{w\sim v}H_T f(w)\) at each non-leaf. This is ordinary unweighted Dirichlet energy minimization. Its harmonic measures \(\mu_v\) are probability vectors on \(B\), with \(\mu_b=\delta_b\) for \(b\in B\).

A spider has one central vertex of degree \(m\ge3\) and \(m\) internally vertex-disjoint paths from the center to its leaves, of lengths \(L_i\ge1\). It has \(1+\sum_i L_i\) vertices.

## Proof

**1. Exact tree cut identity.** Fix any edge \(uv\) of \(T\), and put \(\nu(b)=\mu_u(b)-\mu_v(b)\). Its mass on \(B\) sums to zero. The corresponding output edge difference is the linear functional \(\sum_{b\in B}\nu(b)f(b)\). Root the tree arbitrarily. For every edge \(e\), let \(C_e\) be its descendant component. Every unit-Lipschitz leaf datum extends to a unit-Lipschitz function on all vertices (for example by the minimum-of-distance-cones formula). For any such extension \(F\), discrete summation along root-to-leaf paths gives
\[
\sum_{b\in B}\nu(b)F(b)
=\sum_{e\in E}\nu(B\cap C_e)\bigl(F(\operatorname{child}(e))-F(\operatorname{parent}(e))\bigr).
\]
The absolute value is at most \(\sum_e|\nu(B\cap C_e)|\). Conversely, choose the root-to-child increments of \(F\) to be \(\operatorname{sgn}\nu(B\cap C_e)\), choosing any increment in \([-1,1]\) for a zero cut mass. A tree has no cycle constraints, so this defines a unit-Lipschitz \(F\) and its restriction to \(B\) attains that bound. The absolute cut value is independent of which component is selected because \(\nu(B)=0\). Finally maximize over output edges to obtain the formula. This is the tree transport identity proved directly, rather than an appeal to an unverified infinite-dimensional duality.

**2. Nonexpansivity is rigid.** For a path, the leaf set consists of its two endpoints and the harmonic extension is their affine interpolation, hence has exact norm one. Conversely, suppose \(T\) has a vertex of degree at least three. Fix any leaf \(a\) and define \(g(v)=d_T(a,v)\); the boundary datum \(g|_B\) has Lipschitz seminorm one. Every non-leaf \(v\) has one neighbor closer to \(a\) and \(\deg(v)-1\) farther away, so
\[
(Lg)(v)=\deg(v)g(v)-\sum_{w\sim v}g(w)=2-\deg(v)\le0.
\]
Let \(w=H_T(g|_B)-g\). Then \(w=0\) on the leaves and \(Lw=\deg-2\ge0\) on the interior, strictly at a branch. The maximum principle and connectivity of the non-leaf induced subtree imply \(w(v)>0\) at **every** interior vertex: a zero minimum would propagate through all interior vertices and contradict the strict source. In particular if \(v\) is the neighbor of \(a\), then \(H_Tg(v)-H_Tg(a)=1+w(v)>1\). Thus the operator norm is strictly greater than one for every non-path tree.

**3. Spider norm and all extremizers.** Let \(x_i=f(b_i)\), and set \(S=\sum_{i=1}^mL_i^{-1}\). Harmonicity along each arm is affine, and harmonicity at the central vertex yields the voltage \(c_0=S^{-1}\sum_i x_i/L_i\). Every edge of arm \(i\) has gradient magnitude \(|x_i-c_0|/L_i\). If \(\operatorname{Lip}_B(f)\le1\), then
\[
\frac{|x_i-c_0|}{L_i}
\le\frac1{L_iS}\sum_{j\ne i}\frac{|x_i-x_j|}{L_j}
\le\frac1{L_iS}\sum_{j\ne i}\frac{L_i+L_j}{L_j}
=1+\frac{m-2}{L_iS}.
\]
The maximum occurs at a minimum length \(L_i=L_{\min}\). It is attained by \(x_j=d_T(b_i,b_j)\), since for \(j,k\ne i\), the difference of these distances is \(|L_j-L_k|\le L_j+L_k\). For \(m\ge3\), each coefficient \(1/L_j\) above is strictly positive, so equality forces all \(x_j-x_i\) to attain \(\varepsilon(L_i+L_j)\) with the same sign \(\varepsilon\). This proves the stated complete extremizer classification up to scaling and constants.

**4. Fixed-order extremizers and square-root asymptotics.** Fix \(n,m\) with \(n\ge m+1\), and let \(\ell=L_{\min}\). The denominator of the amplification correction can be written \(\ell\sum_i L_i^{-1}=1+\ell\sum_{j\ne i}L_j^{-1}\). If \(\ell>1\), shortening the chosen arm to length one and adding the released \(\ell-1\) edges to any other arm strictly decreases this denominator while preserving \(n,m\). Hence a maximizer has a unit arm. With that arm fixed, the other \(m-1\) lengths sum to \(n-2\), and the strictly convex function \(x\mapsto1/x\) proves that their sum of reciprocals is minimized precisely when they differ by at most one. Writing the quotient and remainder as in the finding gives \(\Lambda_{n,m}\) and its complete list of extremal spiders (up to permuting arms).

For the asymptotics put \(Q=n-2\), \(s=m-1\). The reciprocal arithmetic--harmonic mean bound gives \(\sum_{j\ne i}L_j^{-1}\ge s^2/Q\), and hence
\[
\Lambda_{n,m}-1\le \frac{Q(s-1)}{Q+s^2}<\frac{\sqrt Q}{2},
\]
by \(Q+s^2\ge2s\sqrt Q\). For the reverse asymptotic, choose \(s=\lfloor\sqrt Q\rfloor\), one arm of length one, and the other \(s\) arms as evenly balanced as integers permit. Their common size is \(\sqrt Q+O(1)\), hence the reciprocal sum is \(1+o(1)\) and the resulting amplification correction is \((1/2+o(1))\sqrt Q\). Therefore \(\Lambda_n/\sqrt n\to1/2\). No claim is made about the exact maximizing leaf count for each \(n\), beyond its explicit finite maximization formula.

## Verification

The standalone standard-library Python program `check_harmonic_extension.py` implements exact rational Gaussian elimination of Dirichlet systems and independently enumerates all extreme signed tree-edge gradients to obtain norms. It also compares harmonic-measure cut sums with these extreme-point norms on non-spider trees, and exhaustively checks every positive-integer spider-arm composition for \(4\le n\le12\) at fixed leaf count. Run `python3 check_harmonic_extension.py`. A successful run reports `ALL_HARMONIC_EXTENSION_DIAGNOSTICS_PASSED`. These finite computations corroborate the analytic identities; they cannot prove claims for all trees or all sizes.

## Relationship to prior work

Naor--Sheffield (public preprint dated 2010-05-14, arXiv:1005.2535) prove existence of norm-preserving absolutely minimal extensions into tree targets; their finite-graph results use infinity-harmonic, rather than mean-value harmonic, extensions. This does **not** imply that the particular energy-minimizing linear operator studied here has norm one. Espínola--Nicolae (public preprint dated 2014-11-25, arXiv:1502.06842) study continuous selections of norm-preserving extensions; these are not fixed leaf-harmonic operators. Fefferman--Klartag (arXiv:2301.13792) analyze \(W^{1,p}\) tree extensions for finite \(1<p<\infty\) on radially symmetric binary trees, with norm defined by a Sobolev trace minimum, rather than the graph-distance Lipschitz norm used here. Abodayeh--Anandam (2005) establish Dirichlet solvability and Green formulas on trees, the classical potential-theoretic inputs; accessible excerpts were not sufficient to exclude an implicit antecedent for this exact norm calculation. Standard tree transport duality supplies the cut decomposition, but it does not by itself supply the spider formula, rigid nonexpansivity classification or the \(\sqrt n/2\) sharp worst-spider growth.

## Limitations

The result concerns simple random-walk harmonic extension from *all leaves*, with unweighted unit edges and real scalar data. Boundary subsets other than the leaves, weighted conductances, complex or vector-valued data, and general graph cycles are not covered. The all-tree cut formula is an exact finite algorithmic expression, not a closed form in graph degrees. The \(\sqrt n/2\) law is for the worst *spider* of a given vertex order, not the worst arbitrary tree. Exact bibliographic priority is not independently certified; in particular the complete older tree Dirichlet literature has not been exhaustively inspected.

## References

1. A. Naor and S. Sheffield, *Absolutely minimal Lipschitz extension of tree-valued mappings*, arXiv:1005.2535v1 (2010-05-14), https://arxiv.org/pdf/1005.2535.
2. R. Espínola and A. Nicolae, *Continuous Selections of Lipschitz Extensions in Metric Spaces*, arXiv:1502.06842v1 (public version dated 2014-11-25), https://arxiv.org/pdf/1502.06842.
3. C. Fefferman and B. Klartag, *Linear extension operators for Sobolev spaces on radially-symmetric binary trees*, arXiv:2301.13792, https://arxiv.org/pdf/2301.13792.
4. K. Abodayeh and V. Anandam, *Dirichlet problem and Green's formulas on trees*, Hiroshima Math. J. 35 (2005), 413–424, https://doi.org/10.32917/hmj/1150998320.
