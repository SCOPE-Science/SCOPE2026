# A sharp column-screening threshold for John ellipsoids of rectangular matching polytopes

## Finding
For integers \(m,n\ge2\), let the rectangular partial-permutation (complete-bipartite matching) polytope be
\[
\mathcal D_{m,n}=\left\{X\in\mathbb R^{m\times n}:X_{ij}\ge0,\ \sum_{j=1}^nX_{ij}\le1,\ \sum_{i=1}^mX_{ij}\le1\right\}.
\]
Equip the matrix space with its Frobenius Euclidean metric. Set \(t=1/(n+1)\) and \(Q_n=[n(n+1)]^{-1}I_n-[n(n+1)^2]^{-1}J_n\), where \(J_n\) is the all-ones matrix. Consider the full-dimensional ellipsoid
\[
\mathcal E_{m,n}=\left\{t\mathbf1_{m\times n}+Y:\sum_{i=1}^mY_{i,*}Q_n^{-1}Y_{i,*}^{\mathsf T}\le1\right\},
\quad Q_n^{-1}=n(n+1)(I_n+J_n).
\]
**Exact screening theorem.** The ellipsoid \(\mathcal E_{m,n}\) is the unique maximum-volume inscribed (John) ellipsoid of \(\mathcal D_{m,n}\) **if and only if**
\[
\boxed{n+1\ge m+\sqrt m.}
\]
In this range, its squared principal semiaxes are \(1/[n(n+1)^2]\) with multiplicity \(m\), and \(1/[n(n+1)]\) with multiplicity \(m(n-1)\). Its exact volume is
\[
\boxed{\operatorname{vol}_{mn}(\mathcal E_{m,n})=\frac{\pi^{mn/2}}{\Gamma(1+mn/2)}\,[n^n(n+1)^{n+1}]^{-m/2}.}
\]
All \(mn\) coordinate facets and all \(m\) row-sum facets are tangent. The \(n\) column-sum facets are tangent precisely when equality holds in the displayed threshold. For integral parameters, this occurs exactly at \((m,n)=(s^2,s^2+s-1)\) for an integer \(s\ge2\), beginning at \((4,5)\). Otherwise, in the strict screened range, the column facets are not tangent. By transposition, the analogous theorem with row/column roles reversed holds when \(m+1\ge n+\sqrt n\). No formula is asserted here for the John ellipsoid outside these two aspect-ratio regimes.

## Assumptions and scope
The inequalities define a full-dimensional polytope in \(\mathbb R^{mn}\). By bipartite-matching integrality, its vertices are zero-one matrices with at most one nonzero entry in each row and column; its displayed \(mn+m+n\) inequalities are genuine facets for \(m,n\ge2\). The ellipsoid \(c+\{Y:\langle Y,Q^{-1}Y\rangle\le1\}\) uses a positive-definite **shape operator** \(Q\); its eigenvalues are squared semiaxes. The theorem concerns ordinary Euclidean volume and John's maximum-volume *inscribed* ellipsoid, not an enclosing ellipsoid or the largest inscribed Euclidean ball.

## Proof
**1. The reference simplex and its exact contact certificate.** Write \(\Delta_n=\{z\in\mathbb R^n:z_j\ge0,\sum_jz_j\le1\}\). The ellipsoid centered at \(t\mathbf1_n\) with shape \(Q_n\) lies in \(\Delta_n\): its support distance to the coordinate hyperplane \(z_j=0\) is \(\sqrt{(Q_n)_{jj}}=t\), and to \(\sum_jz_j=1\) is \(\sqrt{\mathbf1_n^{\mathsf T}Q_n\mathbf1_n}=t=1-nt\). Its \(n+1\) distinct support points are
\[
p_0=\frac1n\mathbf1_n,\qquad p_j=\frac1n(\mathbf1_n-e_j),\quad1\le j\le n.
\]
Set \(v_j=p_j-t\mathbf1_n\). Direct expansion shows
\[
\sum_{j=0}^nv_j=0,\quad \sum_{j=0}^n\frac n{n+1}v_jv_j^{\mathsf T}=Q_n,\quad v_j^{\mathsf T}Q_n^{-1}v_j=1.
\]
Whitening by \(Q_n^{-1/2}\) produces the positive-weight John contact identities \(\sum_j\frac n{n+1}w_j=0\) and \(\sum_j\frac n{n+1}w_jw_j^{\mathsf T}=I_n\) for unit contact vectors \(w_j\). By the classical John characterization, the displayed ellipsoid is the unique maximum-volume inscribed ellipsoid of \(\Delta_n\).

**2. The product simplex has the block shape.** Let \(\mathcal P=\Delta_n^m\) be the Cartesian product of \(m\) row simplices. The ellipsoid \(\mathcal E_{m,n}\) is contained in \(\mathcal P\), since each row's quadratic summand is at most one. For every row \(i\), each reference contact point \(p_j\) in that row, with all other rows equal to \(t\mathbf1_n\), is a contact point of \(\mathcal P\) and \(\mathcal E_{m,n}\). In whitened coordinates their contact vectors are supported on a single row block. Summing the preceding positive-weight centroid and second-moment identities over all rows yields exactly
\[
\sum_{i=1}^m\sum_{j=0}^n\frac n{n+1}w_{i,j}=0,\qquad
\sum_{i=1}^m\sum_{j=0}^n\frac n{n+1}w_{i,j}w_{i,j}^{\mathsf T}=I_{mn}.
\]
Thus John's characterization proves \(\mathcal E_{m,n}\) is the **unique** largest-volume ellipsoid of the product \(\mathcal P\). This is an ellipsoid with a direct-sum shape, not a Cartesian product of ellipsoids.

**3. The sharp screening equivalence.** One has \(\mathcal D_{m,n}\subset\mathcal P\), with exactly the additional column constraints \(\sum_iX_{ij}\le1\). The support of \(\mathcal E_{m,n}\) in any column-sum direction is
\[
\underbrace{mt}_{\text{center contribution}}+
\underbrace{\sqrt{m(Q_n)_{jj}}}_{\text{shape support}}=
\frac{m+\sqrt m}{n+1}.
\]
It follows that \(\mathcal E_{m,n}\subseteq\mathcal D_{m,n}\) exactly when the claimed inequality holds. Whenever containment holds, any ellipsoid contained in \(\mathcal D_{m,n}\) is also contained in \(\mathcal P\) and hence has no greater volume than \(\mathcal E_{m,n}\). The reference ellipsoid is therefore uniquely John for \(\mathcal D_{m,n}\). Conversely, if the threshold fails, a column support point violates the defining column inequality, so the reference ellipsoid cannot be the John ellipsoid of the rectangular matching polytope. This establishes the equivalence, including its boundary.

**4. Contact and arithmetic boundary.** All \(mn+m\) coordinate/row support equalities established in steps 1–2 remain equalities after screening; the corresponding contact points belong to \(\mathcal D_{m,n}\) because the full ellipsoid does. A column facet is tangent exactly when its support value above equals one. Since all inequalities are distinct facets and an ellipsoid has a unique support point in each given normal direction, this exhausts the contact facets and gives \(m(n+1)\) or \(m(n+1)+n\) tangencies according as the threshold is strict or equal. If \(m,n\) are integers, equality implies \(\sqrt m=n+1-m\) is an integer, hence \(m=s^2\), \(n=s^2+s-1\), and \(s\ge2\). Conversely, these pairs satisfy equality.

**5. Shape spectrum and volume.** The inverse identity follows from \((I_n-J_n/(n+1))^{-1}=I_n+J_n\). The \(\mathbf1_n\) eigendirection of \(Q_n\) has eigenvalue \(1/[n(n+1)^2]\); its \((n-1)\)-dimensional orthogonal complement has eigenvalue \(1/[n(n+1)]\). The block operator has the stated multiplicities and determinant \([n^n(n+1)^{n+1}]^{-m}\). Multiplying the volume of the unit ball in \(\mathbb R^{mn}\) by the square root of that determinant proves the volume formula. Transposition is an isometry and interchanges row and column constraints, proving the last assertion.

## Verification
The included standalone `verify.py` uses Python 3 standard library only. Running `python verify.py` reproduces exact-rational checks of the simplex covariance inverse, all \(n+1\) unit contacts and their positive-weight John centroid and covariance identities for \(2\le n\le12\). It independently checks the sharp integer screening inequality across \(2014\) rectangle shapes with \(2\le m\le39\), \(2\le n\le54\), including the equality examples \((4,5)\) and \((9,11)\). An explicit violating column-support point for \((4,4)\) verifies the necessity side. Output: `RECTANGULAR JOHN CERTIFICATE CHECKS PASSED`. These checks corroborate, rather than replace, the universal John contact proof.

## Relationship to prior work
Heuer and Striker give the partial-permutation-polytope inequality, vertex, and facet descriptions needed to identify \(\mathcal D_{m,n}\). Eisley, Matsushita, and Vindas-Meléndez analyze graph matching polytopes from the Gorenstein and integer-decomposition perspectives. The earlier result *Exact John ellipsoid of the doubly substochastic matrix polytope* determines the all-facets-contacting John ellipsoid of the **square** case \(m=n\); the present screened regime is strictly rectangular (indeed, \(n>m\) when \(m\ge2\)) and proves a qualitatively different pattern where the column facets can cease to contact. The classical John characterization proves optimality for the product envelope; the new geometric threshold arises by screening that certified ellipsoid against the genuinely additional matching constraints. These antecedents do not imply the sharp rectangular threshold as an already stated theorem. A possible equivalent earlier statement under a different ellipsoid or transportation-polytope terminology is a remaining historical-priority risk.

## Limitations
Only the exact product-envelope regime and its transpose are classified; outside these aspect ratios, the John ellipsoid of \(\mathcal D_{m,n}\) remains unevaluated here. No new claim is made about the matching polytope's face lattice, its vertices, integrality, or the square case. Finite tests are not independent certification of the infinite proof. The novelty assessment is provisional pending independent literature review and mathematical audit.

## References
1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, initial public version 2020-12-17, especially Section 3, https://arxiv.org/abs/2012.09901.
2. B. Eisley, K. Matsushita and A. R. Vindas-Meléndez, *Matching polytopes, Gorensteinness, and the integer decomposition property*, arXiv:2407.08820, initial public version 2024-07-11, https://arxiv.org/abs/2407.08820.
3. *Exact John ellipsoid of the doubly substochastic matrix polytope*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-john-ellipsoid-of-the-doubly-substochastic-matrix-polytope--12b1169a9382.
4. F. John, *Extremum problems with inequalities as subsidiary conditions*, 1948, classical characterization of maximum-volume inscribed ellipsoids.
