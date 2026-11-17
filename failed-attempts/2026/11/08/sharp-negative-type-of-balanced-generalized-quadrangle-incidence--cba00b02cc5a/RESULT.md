# Sharp negative type of balanced generalized-quadrangle incidence metrics

## Finding
Let \(\mathcal Q\) be **any finite generalized quadrangle of order \((q,q)\)** with integer \(q\ge2\). Let \(\Gamma\) be its point–line incidence graph, \(d\) its shortest-path distance, and \(\mathcal D_p=(d(u,v)^p)_{u,v\in V(\Gamma)}\), with zero diagonal. Define
\[
 F_q(p)=-(q+1)+q(q+1)2^p-q^2(q+1)3^p+q^3 4^p.
\]
There is exactly one \(\beta_q\in(0,1/q)\) with \(F_q(\beta_q)=0\). The metric \(d\) has \(p\)-negative type precisely for \(0<p\le\beta_q\); it has **strict** \(p\)-negative type precisely for \(0<p<\beta_q\). At \(p=\beta_q\), the space of equality vectors (real vectors whose coordinate sum is zero and whose quadratic form for \(\mathcal D_{\beta_q}\) vanishes) is exactly the one-dimensional span of the point-minus-line bipartition indicator.

The minimal Euclidean dimension of a realization with squared distances \(d(u,v)^p\) is \(2(q+1)(q^2+1)-1\) below the threshold and \(2(q+1)(q^2+1)-2\) at the threshold. Along any sequence of existing generalized quadrangles of orders \((q,q)\) with \(q\to\infty\),
\[
 \lim_{q\to\infty}q^3\beta_q=\frac{1}{\log(4/3)}=3.4760594967\ldots.
\]
Such geometries exist at every prime-power order (for example, the symplectic generalized quadrangles). The theorem does not assume transitivity, self-duality, or primeness of \(q\).

## Assumptions and scope
A generalized quadrangle of order \((q,q)\) is a point–line incidence structure with \(q+1\) points per line and \(q+1\) lines through every point, at most one line through each pair of distinct points, and precisely one point on a given line collinear with each point not incident with it. It has \(v=(q+1)(q^2+1)\) points and the same number of lines. Its incidence graph is connected, bipartite, of girth eight and diameter four. The theorem concerns all such incidence graphs, including nonisomorphic geometries with identical parameters.

For a finite metric space, \(p\)-negative type means \(\sum_{u,v}c_uc_vd(u,v)^p\le0\) for every real vector \(c\) with \(\sum_uc_u=0\); strictness means equality only for \(c=0\). The embedding-dimension statement refers to \(d^p\) as a squared Euclidean distance and not to a direct isometric Euclidean realization of \(d^p\).

## Proof
**(1) Distance-regular spherical decomposition.** Write \(A\) for the graph adjacency matrix and \(A_j\) for the distance-\(j\) adjacency matrices. The generalized-quadrangle axiom gives the intersection array
\[
 \{q+1,q,q,q\,;\,1,1,1,q+1\}.
\]
In particular, the polynomial identities, derived by counting walks, are
\[
 A_2=A^2-(q+1)I,\qquad A_3=A^3-(2q+1)A,
\]
\[
 A_4=\frac{A^4-(3q+1)A^2+q(q+1)I}{q+1}.
\]
The point–line biadjacency matrix \(B\) satisfies \(BB^{\mathsf T}=(q+1)I+C\), where \(C\) is the point-collinearity strongly regular adjacency matrix, with parameters \(((q+1)(q^2+1),q(q+1),q-1,q+1)\). Its nonprincipal eigenvalues are \(q-1\) and \(-q-1\). Consequently the spectrum of \(A\) consists of \(\pm(q+1)\), \(\pm\sqrt{2q}\), and \(0\), with multiplicities \(1,1\), \(f,f\), and \(2h\) respectively, where
\[
 f=\frac{q(q+1)^2}{2},\qquad h=\frac{q(q^2+1)}{2}.
\]
All integers displayed are genuine multiplicities for any existing generalized quadrangle of the stated order.

**(2) Complete powered-distance spectrum.** Since \(\mathcal D_p=A+2^pA_2+3^pA_3+4^pA_4\), the complete eigenvalue list is
\[
\begin{array}{c|c|c}
 A\text{ eigenvalue}&\mathcal D_p\text{ eigenvalue}&\text{multiplicity}\\ \hline
 q+1 &(q+1)+q(q+1)2^p+q^2(q+1)3^p+q^3 4^p&1\\
 -(q+1)&F_q(p)&1\\
 +\sqrt{2q}&(q-1)2^p-q4^p+\sqrt{2q}(1-3^p)&f\\
 -\sqrt{2q}&(q-1)2^p-q4^p+\sqrt{2q}(3^p-1)&f\\
 0&-(q+1)2^p+q4^p&2h.
\end{array}
\]
Only the first row corresponds to the constant vector. The second row corresponds to the point-minus-line vector. All remaining eigenspaces are orthogonal to constants.

**(3) Uniqueness and location of the threshold root.** Put \(a=\log(4/3)\), \(b=\log2\), and \(G_q(p)=4^{-p}F_q(p)\). Direct differentiation gives
\[
 G'_q(p)=(q+1)4^{-p}\left(q^2 a3^p-qb2^p+2b\right).
\]
The bracket \(T_q(p)\) is strictly increasing for \(p\ge0\): its derivative is positive because \(q a\log3>b^2\) for \(q\ge2\). The elementary bounds \(a>1/4\), \(b<7/10\), \(\log3>1\) suffice for this inequality. Moreover, \(T_q(0)=q^2a-(q-2)b>0\) for \(q\ge2\). Thus \(G_q\) is strictly increasing and \(G_q(0)=-1\). For \(q=2\), \(F_2(1/2)=13+6\sqrt2-12\sqrt3>0\). For \(q\ge3\), integrating the displayed derivative on \([0,1/q]\) yields
\[
 G_q(1/q)\ge-1+(q+1)4^{-1/q}(qa-b+2b/q)
 \ge-1+4\cdot4^{-1/3}(3a-b/3)>0.
\]
The last inequality follows from \(4^{-1/3}>1/2\), \(a>1/4\), and \(b<3/4\); the middle bound uses that \(qa-b+2b/q\) increases for \(q\ge3\). There is therefore a unique root \(\beta_q\in(0,1/q)\), and \(F_q(p)\) has the sign of \(p-\beta_q\) for \(p\ge0\).

**(4) No earlier obstruction.** For \(0<p\le1/q\), set \(u=2^p\). The binomial theorem gives \(u\le2^{1/q}<1+1/q\), so the zero-adjacency eigenvalue of \(\mathcal D_p\) is
\[
 -(q+1)u+qu^2=u(qu-q-1)<0.
\]
Also, because \(3^p\le4^p=u^2\) and \(\sqrt{2q}\le q\), the larger of the two eigenvalues in the \(\pm\sqrt{2q}\) rows satisfies
\[
 (q-1)u-qu^2+\sqrt{2q}(3^p-1)
 \le(q-1)u-qu^2+q(u^2-1)=(q-1)u-q<0.
\]
Therefore all nonconstant eigenvalues are negative for \(0<p<\beta_q\), exactly one is zero for \(p=\beta_q\), and for \(p>\beta_q\) the bipartition eigenvalue is positive. This proves the full negative-type classification, including endpoint uniqueness. Schoenberg's centered Gram construction \(-\tfrac12 H\mathcal D_pH\), where \(H=I-\mathbf1\mathbf1^{\mathsf T}/(2v)\), gives the two minimal Euclidean embedding dimensions.

**(5) Sharp asymptotic.** For every fixed \(c>0\), uniform Taylor expansion of the four exponentials at \(p=c/q^3\) gives
\[
 F_q(c/q^3)=-1+c\log(4/3)+O_c(q^{-1}).
\]
The uniquely located root lies between \(c_-/q^3\) and \(c_+/q^3\) for all sufficiently large \(q\), whenever \(c_-<1/\log(4/3)<c_+\). The claimed limit follows.

## Verification
The standalone `checker.py` constructs the finite symplectic generalized quadrangles over \(\mathbb F_2\), \(\mathbb F_3\), and the nonprime field \(\mathbb F_4\) directly from their alternating forms. For every vertex it checks the complete distance-shell counts and the three exact walk-polynomial identities, then numerically diagonalizes the independently constructed powered-distance matrices for several exponents against the five theoretically predicted eigenvalue classes. It also checks the exact endpoint kernel multiplicity. Command: `python checker.py` (Python 3.9+ and NumPy). It prints `GQ_NEGATIVE_TYPE_EXACT_AND_SPECTRAL_CHECKS_PASS`.

Observed values: \(\beta_2=0.345784723476\ldots\), \(\beta_3=0.137565128845\ldots\), and \(\beta_4=0.062971721769\ldots\). Finite enumeration is a check only; the all-parameter theorem follows from the proof above.

## Relationship to prior work
Sánchez's 2011 paper establishes general finite-metric negative-type criteria and derives the complete-bipartite threshold. The incidence graph here has diameter four, rather than two, and its obstruction is governed by the competition among four distance shells. The general finite-metric determinant method does not itself state or imply the explicit all-order formula without the present spherical calculation and root comparison. Aalipour et al. (2015) analyze *unpowered* distance spectra and other distance-regular families, not the above four-shell powered-distance threshold. Bamberg–Li–Swartz (2015) develops finite generalized-quadrangle geometry, not negative-type exponents. Association-scheme spherical theory supplies the eigenpolynomials used here; those constituent ingredients are not claimed as new.

The present claim is restricted to balanced incidence geometries; the primary statements do not claim a classification for unequal parameters or arbitrary regular bipartite graphs. An undiscovered equivalent consequence of a more general historical theorem is possible, and historical priority is not asserted unconditionally.

## Limitations
The numerical verification only covers orders two, three, and four. For nonexisting orders the theorem is conditional on a generalized quadrangle of that order existing. The minimal dimension is for squared Euclidean distances \(d^p\) and should not be confused with a Euclidean embedding of \(d^p\) itself. The proof uses conventional graph distance and a zero diagonal. The oldest precisely dated public motivating preprint identified for this analysis is Sánchez's arXiv submission of 2011-08-02; earlier classical foundations remain credited without inventing exact posting dates.

## References
1. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (public 2011-08-02), https://arxiv.org/abs/1108.0451.
2. J. Bamberg, C. H. Li, E. Swartz, *A classification of finite antiflag-transitive generalized quadrangles*, arXiv:1508.03565v1 (public 2015-08-14), https://arxiv.org/abs/1508.03565.
3. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196v1 (public 2015-09-03), https://arxiv.org/abs/1509.01196.
4. A. E. Brouwer and M. A. Fiol, *Distance-regular graphs where the distance-d graph has fewer distinct eigenvalues*, Linear Algebra Appl. 480 (2015), 115–126, doi:10.1016/j.laa.2015.04.020.
