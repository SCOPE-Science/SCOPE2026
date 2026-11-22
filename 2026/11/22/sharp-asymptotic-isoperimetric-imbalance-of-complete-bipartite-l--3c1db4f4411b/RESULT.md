# Sharp asymptotic isoperimetric imbalance of complete-bipartite Laplacian simplices

## Finding
For positive integers \(p,q\), write \(N=p+q\ge3\) and \(d=N-1\). Let \(L\) be the unweighted graph Laplacian of \(K_{p,q}\), and let
\[
P_{p,q}=\operatorname{conv}\{Le_i:1\le i\le N\}\subset\mathbf1^\perp\subset\mathbb R^N.
\]
Denote its **intrinsic Euclidean** \(d\)-volume by \(V_{p,q}\), its \((d-1)\)-dimensional facet-area sum by \(S_{p,q}\), and the scale-invariant isoperimetric quotient by \(I_{p,q}=S_{p,q}/V_{p,q}^{(d-1)/d}\). Put \(a=p/N\), \(b=q/N\). The exact volume and surface-area formulas are
\[
\boxed{V_{p,q}=\frac{N^{3/2}p^{q-1}q^{p-1}}{(N-1)!},}
\]
\[
\boxed{\frac{S_{p,q}}{dV_{p,q}}=
\frac pq\sqrt{1-\frac{1+b+b^2}{N}}+
\frac qp\sqrt{1-\frac{1+a+a^2}{N}}.}
\]
The first \(p\) facets each have area \(dV_{p,q}q^{-1}\sqrt{1-(1+b+b^2)/N}\); the remaining \(q\) facets each have area \(dV_{p,q}p^{-1}\sqrt{1-(1+a+a^2)/N}\).

Define, for \(0<a\le1/2\),
\[
H(a)=\left(\frac{a}{1-a}+\frac{1-a}{a}\right)a^{1-a}(1-a)^a,
\qquad H(0)=1.
\]
Then **uniformly over all integers** \(1\le p\le N/2\),
\[
\boxed{\frac{I_{p,N-p}}{N-1}=eH(p/N)\,[1+O(N^{-1})].}
\]
There is a **unique** \(a_*\in(0,1/2)\) maximizing \(H\): writing \(r_*=a_*/(1-a_*)\), it is the unique solution in \((0,\sqrt2-1)\) of
\[
\boxed{-\log r_*=\frac{2(1-r_*^2)}{1+r_*^2}.}
\]
Numerically \(r_*=0.1473406467610953\ldots\), \(a_*=0.1284192686601256\ldots\), and \(eH(a_*)=3.09551449198038\ldots\). Consequently, for any maximizing integer bipartition \(p_N\le N-p_N\),
\[
\boxed{\frac{p_N}{N}\longrightarrow a_*,\qquad
\max_{1\le p\le N/2}\frac{I_{p,N-p}}{N-1}\longrightarrow eH(a_*).}
\]
The balanced, and also the vanishing-small-shore, regimes have limit \(e\). Thus the asymptotic maximizing shore proportion is neither balanced nor star-like. The sharp limiting maximal quotient is larger than the balanced limit by the factor \(H(a_*)=1.13877614144784\ldots\).

## Assumptions and scope
The graphs are finite, simple, unweighted, complete bipartite, with \(p,q\ge1\); \(N\ge3\). The simplex uses **all columns** of the graph Laplacian and the inherited metric of the sum-zero hyperplane, not a column-deleted integer-lattice realization. Surface area means the Euclidean sum of its \(N\) facet areas. The asymptotic claim concerns \(N\to\infty\) and all integer bipartitions, with symmetry used to restrict to \(p\le q\). Uniqueness is claimed for the **continuous limiting proportion**, not for the finite-\(N\) integer maximizing pair. The implicit constants in the displayed uniform error are independent of \(p\) and \(N\).

## Proof
**1. Full dimension and the exact volume.** A connected graph Laplacian has kernel \(\operatorname{span}\{\mathbf1\}\) and rank \(N-1\), so its \(N\) columns form an affinely independent \((N-1)\)-simplex in \(\mathbf1^\perp\). The nonzero eigenvalues of the Laplacian of \(K_{p,q}\) are \(q\) with multiplicity \(p-1\), \(p\) with multiplicity \(q-1\), and \(N\) with multiplicity one. The regular simplex \(\operatorname{conv}\{e_i\}\) has intrinsic \((N-1)\)-volume \(\sqrt N/(N-1)!\); the Laplacian acts on \(\mathbf1^\perp\) with absolute determinant \(Np^{q-1}q^{p-1}\). Multiplying gives the stated \(V_{p,q}\), including \(p=1\) or \(q=1\).

**2. Metric facet areas.** Let \(Q=L^\dagger\). Since \(QL=I-\mathbf1\mathbf1^\mathsf T/N\), the vector \(Qe_i\) has inner product \(1-1/N\) with the opposite vertex \(Le_i\) and \(-1/N\) with each vertex in its opposite facet. It therefore points inward and is perpendicular to that facet. The simplex altitude to that facet is \(1/\|Qe_i\|\) (the inner-product difference is exactly one); the facet area is \(dV_{p,q}\|Qe_i\|\).

For the first shore, orthogonally decompose \(\mathbf1^\perp\) into contrasts within the first shore, contrasts within the second, and the line of blockwise constants. Their Laplacian eigenvalues are respectively \(q,p,N\). The diagonal entries of their orthogonal projectors, on the first shore, are \(1-1/p\), \(0\), and \(q/(pN)\); on the second they are \(0\), \(1-1/q\), and \(p/(qN)\). Thus
\[
\|Qe_i\|^2=\begin{cases}
\displaystyle\frac{p-1}{pq^2}+\frac{q}{pN^3}=\frac1{q^2}\left(1-\frac{1+b+b^2}{N}\right),&i\text{ in the first shore},\\[6pt]
\displaystyle\frac{q-1}{qp^2}+\frac{p}{qN^3}=\frac1{p^2}\left(1-\frac{1+a+a^2}{N}\right),&i\text{ in the second shore}.
\end{cases}
\]
The square roots are positive for \(N\ge3\); summing the \(p+q\) facet areas proves the exact formula.

**3. Uniform scaling limit, including highly unbalanced shores.** Write \(b=1-a\). Since \(1\le 1+a+a^2\le 3\), and similarly for \(b\), the square-root factors in the area expression equal \(1+O(N^{-1})\) **uniformly** in \(a\). Both coefficients outside the roots are positive, so their weighted sum has the same uniform relative error.

Stirling's expansion, uniformly in \(N\), gives
\[
\log V_{p,q}=N-\tfrac12\log(2\pi)+(q-1)\log a+(p-1)\log b+O(N^{-1}).
\]
Subtract \((N-1)[1+b\log a+a\log b]\). The remainder is \(1-\tfrac12\log(2\pi)-a\log a-b\log b+O(N^{-1})\), bounded independently of \(a\in[1/N,1/2]\) because \(x\log x\) extends continuously to zero. Dividing by \(N-1\), then exponentiating, yields
\[
V_{p,q}^{1/d}=e\,a^b b^a[1+O(N^{-1})]
\]
uniformly. Combining this with \(I_{p,q}/d=V_{p,q}^{1/d}S_{p,q}/(dV_{p,q})\) proves the asserted uniform limit. As \(a\downarrow0\), \(a^b b^a(a/b+b/a)\to1\); hence \(H\) is continuous on \([0,1/2]\) and \(H(0)=H(1/2)=1\).

**4. Uniqueness of the sharp limiting maximizer.** Set \(r=a/(1-a)\). Direct simplification gives
\[
H(a)=\frac{1+r^2}{1+r}\,r^{-r/(1+r)}.
\]
For \(0<r<1\),
\[
\frac{d}{dr}\log H=\frac{g(r)}{(1+r)^2},\qquad
g(r)=-\log r-\frac{2(1-r^2)}{1+r^2},\qquad
g'(r)=-\frac{r^4-6r^2+1}{r(1+r^2)^2}.
\]
The sign of \(g'\) changes exactly once, at \(r=\sqrt2-1\): it is negative before and positive afterward. Also \(g(0+)=+\infty\), \(g(1/2)=\log2-6/5<0\), and \(g(1)=0\). Therefore \(g\) has exactly one zero \(r_*\in(0,\sqrt2-1)\); \(H\) strictly increases before that zero and strictly decreases after it, up to the endpoint. Since \(H(0)=H(1)=1\) in the \(r\)-parameterization, this critical point is the unique global maximum.

**5. Integer-maximizer convergence.** Let \(p_N\) be any maximizer for given \(N\). The compactness of \([0,1/2]\) gives a convergent subsequence of \(p_N/N\); the uniform approximation forces every subsequential limit to maximize \(H\) because a sequence of admissible integers may approximate every \(a\in[0,1/2]\). Uniqueness from step 4 forces that limit to be \(a_*\). Thus the full sequence converges and the maximum values have the claimed limit. Numerical constants are evaluations of the unique defining equation, not substitutes for the exact characterization.

## Verification
The accompanying `check.py` builds each complete-bipartite graph Laplacian independently, evaluates all vertex-difference Gram determinants and facet determinants, and compares them with the asserted formulas in 44 cases across dimensions \(2\) through \(9\) (\(3\le N\le10\)), including boundary stars and balanced graphs. Its error threshold is relative \(2\times10^{-9}\). A separate stable-log-gamma calculation checks discrete maximizers at \(N=100,200,400,800,1600,3200\), approaching the analytic limiting proportion. Run `python check.py` with Python 3 and NumPy. These finite computations are diagnostic only; the displayed exact algebra and uniform asymptotic argument prove the all-dimensional statement.

## Relationship to prior work
Braun and Meyer introduced the full-column Laplacian simplex and investigated its lattice structure, reflexivity and Ehrhart data [1]. Their definition and full-rank graph argument are inputs; the result here is the **intrinsic Euclidean surface-to-volume optimization** across different complete-bipartite graphs, not a claim about new lattice invariants. Devriendt's graph-simplex/effective-resistance treatment [2] studies a related but different canonical realization, and does not imply this metric optimization. Previously published results on complete-bipartite Laplacian simplices establish a minimum-enclosing-ball contact transition [3] and a logarithmic normal-cone probability crossover near balanced shores [4], whereas a general reconstruction theorem uses Laplacian pseudoinverse facet normals to recover graph weights from dihedral angles [5]. Those results neither evaluate the surface-to-volume quotient above nor identify its unique unbalanced asymptotic optimizer. The elementary altitude identity and graph spectra are not claimed as independently novel.

## Limitations
The theorem is specific to unweighted complete-bipartite graphs and the full-column orthogonal Euclidean embedding; it need not survive a nonisometric lattice-coordinate change or edge weighting. It determines the limiting optimal shore proportion and sharp limiting quotient, not the exact integer optimizer for each finite order or higher-order corrections. An unindexed equivalent surface-optimization treatment is a residual historical-priority risk; an independent mathematical audit has not been performed.

## References
1. B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085v1, public 2017-06-21, https://arxiv.org/abs/1706.07085; particularly the full-column definition and graph-Laplacian simplex construction.
2. K. Devriendt, *Effective resistance is more than distance: Laplacians, Simplices and the Schur complement*, arXiv:2010.04521, https://arxiv.org/abs/2010.04521.
3. *Sharp vertex-contact transition for complete-bipartite Laplacian simplices*, public research record `ac6d13296de7` (2026), minimum enclosing sphere and contact classification.
4. *A logarithmic normal-cone crossover in near-regular Laplacian simplices*, public research record `63fef57c7866` (2026), angular probabilities and random widths.
5. *Angular recognition and weighted-graph reconstruction for Laplacian-column simplices*, public research record `49d3b46853da` (2026), inverse problem from dihedral angles.
