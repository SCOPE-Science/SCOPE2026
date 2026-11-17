# Exact vertex covariance and a six-leaf eigenaxis transition for two-hub graphical zonotopes

## Finding

For every integer \(q\ge3\), let \(G=K_{2,q}\) be the complete bipartite graph on hubs \(A,B\) and leaves \(1,\ldots,q\). In \(\mathbb R^{q+2}\) with its ordinary Euclidean metric, form the centered graphical zonotope
\[
Z_q=\sum_{j=1}^q\left[-\frac{e_A-e_j}{2},\frac{e_A-e_j}{2}\right]
+\sum_{j=1}^q\left[-\frac{e_B-e_j}{2},\frac{e_B-e_j}{2}\right]\subset\mathbf1^\perp.
\]
Let \(X_q\) be uniform over the **distinct vertices** of \(Z_q\); this is not the uniform intrinsic-volume distribution. Write \(C_q=\operatorname{Cov}(X_q)\) and \(D_q=2\cdot3^q-2^q\). There are exactly \(D_q\) vertices. The three positive eigenvalues of \(C_q\), acting on \(\mathbf1^\perp\), are
\[
\boxed{\begin{aligned}
\lambda_{\mathrm{hub}}&=\frac{q(q+2)3^{q-2}}{D_q} &&\text{(multiplicity 1)},\\
\lambda_{\mathrm{leaf}}&=\frac{4\cdot3^{q-1}-2^q}{D_q} &&\text{(multiplicity \(q-1\))},\\
\lambda_{\mathrm{block}}&=\frac{q+2}{2}\lambda_{\mathrm{leaf}} &&\text{(multiplicity 1)}.
\end{aligned}}
\]
Their mutually orthogonal eigenspaces are, respectively,
\[
\begin{aligned}
E_{\mathrm{hub}}&=\operatorname{span}(e_A-e_B),\\
E_{\mathrm{leaf}}&=\{v:v_A=v_B=0,\ \sum_{j=1}^qv_j=0\},\\
E_{\mathrm{block}}&=\operatorname{span}\!\left(\frac q2e_A+\frac q2e_B-\sum_{j=1}^qe_j\right).
\end{aligned}
\]
The least-variance space is always \(E_{\mathrm{leaf}}\), whereas the top eigenspace is \(E_{\mathrm{block}}\) for \(3\le q\le5\) and \(E_{\mathrm{hub}}\) for \(q\ge6\). No integer \(q\ge3\) gives a top-eigenvalue tie. More precisely,
\[
\lambda_{\mathrm{block}}-\lambda_{\mathrm{hub}}
=\frac{q+2}{D_q}\left((6-q)3^{q-2}-2^{q-1}\right).
\]
The spectral condition number in the affine span is exactly
\[
\boxed{\kappa(C_q|_{\mathbf1^\perp})=
\begin{cases}
\dfrac{q+2}{2},&3\le q\le5,\\[3pt]
\dfrac{q(q+2)}{12-9(2/3)^q},&q\ge6,
\end{cases}}
\qquad \kappa(C_q|_{\mathbf1^\perp})\sim q^2/12.
\]

## Assumptions and scope

The graph has exactly two labeled hub vertices and \(q\ge3\) labeled leaves; all edge generators have unit weight, and different acyclic orientations correspond bijectively to **distinct** vertices. Covariance uses the equal-probability counting measure on those vertices. The ambient covariance has one additional zero eigenvalue, on the all-ones direction; the displayed condition number excludes that forced zero. The case \(q=2\), already a single cycle, is not part of the claimed new classification.

The primary mathematical objects are a centrally symmetric Euclidean polytope and its discrete vertex moment tensor. No assertion is made about the covariance of a uniform interior point, arbitrary edge weights, or larger hub classes.

## Proof

**1. Orientations and a disjoint-union count.** Give every edge the reference orientation from its hub to its leaf. A sign matrix \(s=(s_{Aj},s_{Bj})\in\{-1,1\}^{2\times q}\) represents a vertex when it represents an acyclic orientation. Every undirected simple cycle in \(K_{2,q}\) is a four-cycle. Such a cycle is directed exactly when the columns \((-1,+1)\) and \((+1,-1)\) both occur. Hence the acyclic signs are the union of the two product alphabets
\[
\mathcal T_- =\{(-1,-1),(-1,+1),(+1,+1)\}^q,
\quad
\mathcal T_+=\{(-1,-1),(+1,-1),(+1,+1)\}^q.
\]
Their intersection is \(\mathcal B=\{(-1,-1),(+1,+1)\}^q\). The normal fan of the graphical zonotope is the graphical hyperplane arrangement: its chambers are the acyclic orientations and correspond one-to-one with vertices. Therefore inclusion-exclusion yields
\[
|\operatorname{vert}(Z_q)|=|\mathcal T_-|+|\mathcal T_+|-|\mathcal B|=2\cdot3^q-2^q=D_q.
\]
For each such sign matrix, the centered vertex has coordinates
\[
z_A=\frac12\sum_js_{Aj},\quad z_B=\frac12\sum_js_{Bj},\quad
z_j=-\frac{s_{Aj}+s_{Bj}}2.
\]
They satisfy \(z_A+z_B+\sum_jz_j=0\). Global sign inversion preserves the acyclic family, so the uniform vertex mean is zero.

**2. Leaf contrast variance.** For any leaf \(j\), its coordinate \(z_j\) is \(+1\), \(0\), or \(-1\), according as the column is \((-1,-1)\), mixed, or \((+1,+1)\). On each of the two ternary product families, its second-moment weight is \(2/3\); on the intersection binary family it is \(1\). Thus
\[
\mathbb E[z_j^2]=\frac{2\cdot3^q(2/3)-2^q}{D_q}
=\frac{4\cdot3^{q-1}-2^q}{D_q}=\lambda_{\mathrm{leaf}}.
\]
For distinct leaves \(j\ne k\), independence inside each product family and zero single-coordinate means show that every contribution to \(\mathbb E[z_jz_k]\) is zero, including the subtracted binary intersection. Hence the entire leaf-by-leaf covariance block is \(\lambda_{\mathrm{leaf}}I_q\). Symmetry under leaf permutations forces leaf contrasts to be orthogonal in covariance to both hub coordinates; \(E_{\mathrm{leaf}}\) is therefore an eigenspace of dimension \(q-1\).

**3. Hub-difference variance.** Let \(m\) be the number of mixed columns in a ternary-family sign matrix. On \(\mathcal T_-\) the hub difference \(z_A-z_B=-m\); on \(\mathcal T_+\) it equals \(+m\); on \(\mathcal B\) it equals zero. Since \(m\) is binomial with \(q\) trials and success probability \(1/3\) in either ternary product family, the exact unnormalized second-moment sum is
\[
2\cdot3^q\mathbb E[m^2]
=2\cdot3^q\left(\frac{2q}{9}+\frac{q^2}{9}\right)
=2q(q+2)3^{q-2}.
\]
The unit hub-difference eigenvector is \((e_A-e_B)/\sqrt2\). Thus its variance is half the normalized hub-difference second moment:
\[
\lambda_{\mathrm{hub}}=\mathbb E[(z_A-z_B)^2]/2
=\frac{q(q+2)3^{q-2}}{D_q}.
\]
Interchanging the two hubs is a symmetry, so this is an eigenvector and it is covariance-orthogonal to the remaining block-constant direction.

**4. Block-contrast variance and completeness.** Put \(S=\sum_jz_j=-(z_A+z_B)\). Since distinct leaf coordinates have zero covariance, \(\operatorname{Var}(S)=q\lambda_{\mathrm{leaf}}\). The block direction
\[
w=\frac q2(e_A+e_B)-\sum_je_j
\]
has squared Euclidean norm \(q(q+2)/2\) and satisfies \(w\cdot z=-(q+2)S/2\). Consequently
\[
\lambda_{\mathrm{block}}=
\operatorname{Var}\left(\frac{w\cdot X_q}{\|w\|}\right)
=\frac{q+2}{2q}\operatorname{Var}(S)
=\frac{q+2}{2}\lambda_{\mathrm{leaf}}.
\]
This direction is an eigenspace by the same hub-swap and leaf-permutation symmetries. These three orthogonal spaces span \(\mathbf1^\perp\), proving the complete spectrum.

**5. Sharp spectral ordering.** For every integer \(q\ge3\),
\[
D_q(\lambda_{\mathrm{hub}}-\lambda_{\mathrm{leaf}})
=(q^2+2q-12)3^{q-2}+2^q>0,
\]
and \(\lambda_{\mathrm{block}}=(q+2)\lambda_{\mathrm{leaf}}/2>\lambda_{\mathrm{leaf}}\). The displayed formula for the difference of the two possible top eigenvalues has a positive bracket at \(q=3,4,5\), where it equals \(5,10,11\), respectively; for \(q\ge6\) the bracket is strictly negative. This gives the exact transition and, after division by \(\lambda_{\mathrm{leaf}}\), the stated piecewise condition number and asymptotic.

## Verification

The standalone Python standard-library program `artifacts/verify.py` independently enumerates all acyclic orientations by total vertex orders for \(3\le q\le6\); it separately constructs their two-ternary-family encoding. For \(7\le q\le9\) it independently builds the ternary sign family. Across these seven values, it computes full exact-rational covariance matrices, compares all three claimed eigenvalues on a spanning eigenbasis, and checks the forced zero mode. It also checks the strict eigenvalue ordering and exact gap for every integer \(3\le q\le100\). The successful output is `TWO_HUB_VERTEX_COVARIANCE_CHECKS_PASSED full_matrices=7 q_inequalities=98`.

The general theorem is proved by the preceding enumeration identities and symmetry, not by extrapolating from finitely many tests. Execute `python3 artifacts/verify.py` from the package root with Python 3 and no extra dependencies.

## Relationship to prior work

Chapoton and Pilaud [1] establish complete-bipartite graphical zonotopes as natural building blocks for shuffles and use acyclic orientations to describe vertices; they do not derive the uniform vertex covariance spectrum above. Padrol, Pilaud and Poullot [2] describe graphical-zonotope deformation cones, rather than vertex moment operators. Carballosa, Khera and Reyes [3] encode and enumerate acyclic orientations of complete multipartite graphs, but the examined material does not evaluate the Euclidean uniform-vertex covariance of this graph-polytope family.

A known exact Löwner ellipsoid for complete-bipartite graphical zonotopes and a known formula for their maximum vertex radius concern outer extremal geometry, not the average of squared vertex coordinates. Neither fixes this discrete covariance tensor: even an extremal contact-point probability distribution is generally different from the uniform distribution on all vertices. Likewise, a uniform-**volume** covariance formula for the same polytope, or a vertex-covariance theorem restricted to cactus graphs, does not imply this result; for \(q\ge3\), the graph \(K_{2,q}\) is not a cactus.

## Limitations

This is a theorem for the unweighted standard realization and for the uniform measure on **distinct** vertices. It is not a statement about a random linear extension (whose induced vertex distribution is generally nonuniform), nor about the intrinsic-volume distribution. The source comparison does not establish exhaustive historical priority: equivalent earlier results stated in terms of lonesum binary matrices, indegree sequences, or their second moments remain a possible overlap risk. No independent audit has been performed.

## References

[1] F. Chapoton and V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, first posted 2022-01-18, https://arxiv.org/abs/2201.06896.

[2] A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first posted 2021-11-24, https://arxiv.org/abs/2111.12422.

[3] W. Carballosa, J. Khera and F. Reyes, *Encoding and Enumerating Acyclic Orientations of Graphs*, arXiv:2303.09021, first posted 2023-03-16, https://arxiv.org/abs/2303.09021.
