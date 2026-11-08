# Volume moments detect block designs in sparse-paving matroid polytopes

## Finding
Let \(2\le r\le n-2\), let \(\mathcal H\) be a family of \(\lambda\) distinct \(r\)-subsets of \([n]\), and suppose any two distinct members intersect in at most \(r-2\) elements. The \(r\)-subsets outside \(\mathcal H\) form the bases of a sparse-paving matroid. Write \(P\) for its incidence-vector base polytope, assume \(P\) has dimension \(n-1\), and let \(X\) be uniform on \(P\) with respect to its intrinsic volume. Let \(d_i=|\{H\in\mathcal H:i\in H\}|\) and \(c_{ij}=|\{H\in\mathcal H:i,j\in H\}|\), for distinct indices.

Define \(A=A(n-1,r-1)\), the Eulerian number counting permutations on \(n-1\) letters with \(r-1\) descents, and
\[
\eta=\frac{\binom{n-2}{r-1}}{A},\quad \theta=1-\lambda\eta>0,\quad
\gamma=\frac{\eta}{\theta}\frac{(r-1)(n-r-1)}{r(n-r)}.
\]
The volume centroid obeys the exact **degree-displacement law**
\[
\boxed{\mathbb E X_i=\frac rn-\gamma\left(d_i-\frac{\lambda r}{n}\right).}
\]
In particular, the centroid equals the hypersimplex centroid \(r\mathbf1/n\) **if and only if** the family \(\mathcal H\) is a one-design (all degrees \(d_i\) equal). Its squared Euclidean displacement is
\[
\boxed{\left\|\mathbb EX-\frac rn\mathbf1\right\|^2
=\gamma^2\left(\sum_i d_i^2-\frac{\lambda^2r^2}{n}\right).}
\]
All entries of the continuous-volume covariance matrix are explicit rational functions of \(n,r,\lambda,d_i,c_{ij}\), plus a finite Eulerian-type alternating sum depending only on \(n,r\), as displayed below. **Within the one-design subfamily**, the covariance is a scalar multiple of the orthogonal projector onto \(\mathbf1^\perp\) **if and only if** \(\mathcal H\) is a two-design (all pair codegrees \(c_{ij}\) equal). This includes the empty family. In every nondegenerate case, the covariance is positive definite on \(\mathbf1^\perp\).

Thus two sparse-paving matroids can have identical Ehrhart polynomials and normalized volumes while their *interior-volume centroids* differ. For \((n,r,\lambda)=(6,3,2)\), the families \(\{\{1,2,3\},\{4,5,6\}\}\) and \(\{\{1,2,3\},\{1,4,5\}\}\) both yield normalized volume \(54\). The first has centroid \((1/2,\ldots,1/2)\); the second has centroid
\[
\left(\frac{73}{162},\frac12,\frac12,\frac12,\frac12,\frac{89}{162}\right).
\]

## Assumptions and scope
All volumes and probabilistic moments are taken in the affine hyperplane \(\sum_i x_i=r\) with the metric induced by \(\mathbb R^n\). For the center and covariance results, the family may be empty; for a family with \(\lambda>0\), the positivity of \(\theta\) is equivalent to positive \((n-1)\)-dimensional volume. The exceptional potential zero of the pair-codegree coefficient occurs at \((n,r)=(4,2)\); at that size, every positive-volume degree-regular admissible family is empty, so the two-design equivalence still holds. The formulas do not concern the uniform distribution on the vertices.

Set \(b=n-r\) and \(s_1=(n-1)/n\), \(s_2=(n-1)/(n+1)\). For one cut-cap, put
\[
\begin{aligned}
 h_1&=1-s_1/r,& \ell_1&=s_1/b,\\
 h_2&=1-2s_1/r+2s_2/[r(r+1)],&\ell_2&=2s_2/[b(b+1)],\\
 h_h&=1-2s_1/r+s_2/[r(r+1)],&
 h_\ell&=s_1/b-s_2/(rb),&
 \ell_\ell&=s_2/[b(b+1)].
\end{aligned}
\]
Define \(t_k=r-k\), let \(\binom{n-1}{-1}=0\), and put
\[
\begin{aligned}
 Z&=\sum_{k=0}^{r-1}(-1)^k\binom nk\frac{t_k^{n-1}}{(n-1)!},\\
 Q&=\sum_{k=0}^{r-1}(-1)^k\left[
 \frac{2\binom nk t_k^{n+1}}{(n+1)!}
 +\binom{n-1}{k-1}\left(\frac{2t_k^n}{n!}+\frac{t_k^{n-1}}{(n-1)!}\right)\right],\\
 u_2&=Q/Z,&u_{11}&=(r^2-nu_2)/[n(n-1)].
\end{aligned}
\]
The exact uncentered second moments are
\[
\begin{aligned}
 \mathbb E X_i^2&=\frac{u_2-\eta[\lambda\ell_2+(h_2-\ell_2)d_i]}{\theta},\\
 \mathbb E X_iX_j&=\frac{u_{11}-\eta[\lambda\ell_\ell+(h_\ell-\ell_\ell)(d_i+d_j)
 +(h_h-2h_\ell+\ell_\ell)c_{ij}]}{\theta}\quad(i\ne j).
\end{aligned}
\]
Subtracting \((\mathbb E X_i)(\mathbb E X_j)\) yields the covariance. These are exact finite expressions, not numerical approximations.

## Proof
**1. Disjoint corner caps.** Let \(\Delta=\{x\in[0,1]^n:\sum x_i=r\}\). For every \(H\in\mathcal H\), define \(C_H=\{x\in\Delta:\sum_{i\in H}x_i>r-1\}\). The standard sparse-paving base-polytope inequality description gives \(P=\Delta\setminus\bigcup_H C_H\), up to boundary of measure zero. Alternatively, each cut removes precisely the hypersimplex vertex \(\mathbf1_H\) and intersects every incident edge at its other endpoint. For distinct \(H,H'\),
\[
\sum_{i\in H}x_i+\sum_{i\in H'}x_i
=\sum_{i\in H\cup H'}x_i+\sum_{i\in H\cap H'}x_i
\le r+|H\cap H'|\le 2r-2.
\]
Thus the interiors of the corner caps cannot overlap.

**2. Exact cap law and volume fraction.** For a fixed cap, write
\[
X_i=1-SU_i\ (i\in H),\qquad X_j=SV_j\ (j\notin H).
\]
Here \(U\sim\operatorname{Dirichlet}_r(1,\ldots,1)\), \(V\sim\operatorname{Dirichlet}_b(1,\ldots,1)\) are independent, and \(S\sim\operatorname{Beta}(n-1,1)\) independently. This follows by the affine change of variables with \(S=\sum_{j\notin H}X_j\): the conditional cross section is a product of simplices whose Jacobian contributes \(S^{(r-1)+(b-1)}=S^{n-2}\). In the coordinate-lattice normalization \((n-1)!\operatorname{vol}(\cdot)/\sqrt n\), the cap has volume \(\binom{n-2}{r-1}\); the hypersimplex has volume \(A\). Hence each cap occupies probability \(\eta\) inside \(\Delta\), and \(P\) occupies fraction \(\theta\). For every integrable \(f\),
\[
\mathbb E_P f=\frac{\mathbb E_\Delta f-\eta\sum_{H\in\mathcal H}\mathbb E_{C_H}f}{\theta}.
\]
In this identity, \(\mathbb E_{C_H}\) is *the normalized continuous-volume expectation inside the cap*.

**3. First moments and sharp center classification.** Since \(\mathbb ES=s_1\) and every symmetric Dirichlet coordinate has mean \(1/r\) or \(1/b\), a cap has coordinate mean \(h_1\) on \(H\) and \(\ell_1\) off \(H\). By permutation symmetry \(\mathbb E_\Delta X_i=r/n\). The difference is
\[
h_1-\ell_1=\frac{(r-1)(b-1)}{rb}>0,
\]
and \(\ell_1+(r/n)(h_1-\ell_1)=r/n\). Substituting the \(d_i\) cap incidences into the decomposition gives the stated centroid formula. Its squared displacement follows from \(\sum_i d_i=\lambda r\). Since \(\gamma>0\), all mean coordinates equal \(r/n\) exactly when all degrees are equal.

**4. Covariance and the design rigidity.** The moments \(\mathbb ES^2=s_2\), \(\mathbb EU_i^2=2/[r(r+1)]\), \(\mathbb EU_iU_j=1/[r(r+1)]\) for distinct indices, and analogous formulas for \(V\), give the six cap quantities in the assumptions. The density of a sum of \(n\) independent \(\operatorname{Unif}(0,1)\) variables at \(r\), by inclusion-exclusion, is \(Z\). Applying the same inclusion-exclusion to \(X_1^2\) on that slice gives \(Q\), so \(u_2=Q/Z\). The deterministic equation \(\sum_i X_i=r\) and permutation symmetry give \(u_{11}\). Sum the cap moments using \(d_i\) and \(c_{ij}\), obtaining the displayed raw-moment formulas.

If all degrees are equal, the centroid and diagonal entries of covariance are constant. The difference between any two off-diagonal covariances is a nonzero fixed multiple of the corresponding difference between codegrees, except possibly \((n,r)=(4,2)\). In detail, the codegree coefficient is \(-\eta\kappa/\theta\) with
\[
\kappa=h_h-2h_\ell+\ell_\ell
=\frac{r^2b^2-r^2b-r^2-rb^2+rb+r-b^2+b}{rb(r+1)(b+1)}.
\]
Writing \(u=r-2\ge0\), \(v=b-2\ge0\), its numerator equals
\[
u^2v^2+3u^2v+u^2+3uv^2+9uv+3u+v^2+3v.
\]
It is strictly positive unless \(u=v=0\). At \((n,r)=(4,2)\), a nonempty degree-regular family of admissible two-sets consists of two disjoint sets and has zero \((n-1)\)-dimensional volume fraction, excluded by hypothesis. Therefore, among full-dimensional degree-regular cases, all off-diagonal covariances agree exactly when all codegrees agree. With row-sums zero (because \(\sum_iX_i=r\)), equal diagonals and off-diagonals are equivalent to covariance being a multiple of \(I-\mathbf1\mathbf1^T/n\). This proves the two-design equivalence. Positive definiteness on the affine tangent space follows because \(P\) has full-dimensional interior there.

**5. Ehrhart-equivalent illustration.** For either of the two displayed families, \(A(5,2)=66\), the cap normalized volume is \(\binom42=6\), and \(\lambda=2\), so \(P\) has normalized volume \(66-12=54\). Ferroni's circuit-hyperplane relaxation formula, independently elaborated by Hanely and collaborators, shows that the entire Ehrhart polynomial is determined by \((n,r,\lambda)\) in the sparse-paving class. The two degree sequences are respectively \((1,1,1,1,1,1)\) and \((2,1,1,1,1,0)\). Here \(\gamma=4/81\); the center formula produces the exact centroids displayed above.

## Verification
The standalone `checker.py` evaluates the exact formulas in rational arithmetic and, independently, integrates over simplicial decompositions of the *actual convex hulls of basis indicators* for multiple nontrivial small instances. The simplex integrals are computed exactly from integer determinants and rational Dirichlet moments; floating point is used only to select a triangulation. It also checks the center and covariance of the seven-line Fano-design example, polynomial identities for \(\kappa\), and duality of the model. Execute with `python checker.py` using Python 3, NumPy, SciPy, and SymPy. Finite checks corroborate but cannot prove the all-dimensional theorem; the analytic steps above provide that proof.

## Relationship to prior work
Ferroni's circuit-hyperplane relaxation and Hanely et al.'s paving-matroid Ehrhart analysis already provide the cap decomposition and show that sparse-paving Ehrhart polynomials depend only on the count of nonbases. Joswig–Schröter identify compatible hypersimplex vertex cuts with sparse-paving matroids. Ferroni–Schröter give a more general valuative framework for matroid subdivisions, which potentially recovers *formal* integral inclusion-exclusion. These known facts are not claimed here. The claimed evaluation is the label-sensitive **continuous interior-volume centroid–degree law**, the exact degree/codegree covariance and its **one-/two-design rigidity**, and the demonstrated geometric separation despite Ehrhart equivalence. Their proofs require explicit cap distributions and the positive codegree coefficient, neither of which is asserted by the cited general valuation formulas. Prior priority under alternative terminology is not excluded.

## Limitations
No independent audit has been conducted. The result does not claim that centered covariance is isotropic only for two-designs when degree regularity is omitted, nor does it characterize higher-order uniform-volume moment tensors. It does not claim novelty for the hypersimplex volume, the sparse-paving cap subdivision, Eulerian volumes, general matroid valuations, or Ehrhart-equivalence of fixed-parameter sparse-paving matroids. The original literature may contain equivalent centroid or inertia statements not located by the searches recorded in the review.

## References
1. L. Ferroni, *On the Ehrhart Polynomial of Minimal Matroids*, arXiv:2003.02679, first posted March 5, 2020; Discrete & Computational Geometry (2022), DOI 10.1007/s00454-021-00313-4.
2. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442, first posted January 28, 2022, especially Remark 5.12 and Section 7.
3. L. Ferroni and B. Schröter, *Valuative Invariants for Large Classes of Matroids*, arXiv:2208.04893, first posted August 9, 2022, especially Theorem 5.3 and Section 7.
4. M. Joswig and B. Schröter, *Matroids from hypersimplex splits*, arXiv:1607.06291, first posted July 21, 2016, especially Corollary 21 and Theorem 26 (background on the earlier cut construction).
