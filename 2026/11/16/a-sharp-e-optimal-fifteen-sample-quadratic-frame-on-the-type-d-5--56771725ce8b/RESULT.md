# A sharp E-optimal fifteen-sample quadratic frame on the type-\(D_5\) root lines

## Finding
Let \(V=\{v_{ij}^{\pm}=(e_i\pm e_j)/\sqrt2:1\le i<j\le5\}\subset S^4\). These are twenty different real projective root directions, with exactly one representative of each antipodal pair. For every fifteen-element set \(S\subset V\), define
\[
\mathcal E_S:\operatorname{Sym}_5(\mathbb R)\longrightarrow\mathbb R^{15},\qquad (\mathcal E_S Q)_v=v^{\mathsf T}Qv,
\]
where the domain is equipped with the Frobenius inner product and the codomain with the ordinary Euclidean inner product. Put \(\lambda(S)=\lambda_{\min}(\mathcal E_S^*\mathcal E_S)\).

**Sharp optimal sampling theorem.** Exactly \(5,184\) of the \(\binom{20}{15}=15,504\) selections are invertible. All have the same squared sampling volume
\[
\det(\mathcal E_S^*\mathcal E_S)=\frac1{256},
\]
but their smallest squared singular values attain precisely three distinct values:

| Smallest squared singular value | Number of selections |
| --- | ---: |
| \(0.075171201059\ldots\) | 2,304 |
| \(0.049327534803\ldots\) | 960 |
| \(0.043850023016\ldots\) | 1,920 |

The sharp optimum \(\alpha=0.075171201059\ldots\) is the smallest real zero of
\[
16t^4-52t^3+53t^2-17t+1.
\]
It is the largest achievable lower frame bound among **all** fifteen-sample choices, including singular ones.

There is a precise geometric classification. Label each pair of directions \(v_{ij}^+,v_{ij}^-\) by the edge \(ij\) of \(K_5\). For an invertible selection \(S\), let \(H(S)\) be the graph of the **five** edges for which both signs were selected. Then \(H(S)\) is an odd-unicyclic spanning graph (a connected five-edge graph with one odd cycle), and conversely any such graph with one arbitrary sign selected for each of the five remaining edges defines an invertible selection. Exactly the following two graph shapes are E-optimal: a five-cycle, or a triangle with its two other vertices attached as leaves to **two different** triangle vertices. These give respectively \(12\cdot32=384\) and \(60\cdot32=1,920\) optimal samples.

## Assumptions and scope
The diagonal matrix entries of \(Q\) and the coordinates \(\sqrt2 Q_{ij}\) for \(i<j\) form an orthonormal coefficient system for \(\operatorname{Sym}_5(\mathbb R)\). Thus the normalization is fixed by the Frobenius inner product; no division by the sample count or by a spherical probability measure occurs. The theorem concerns linear recovery of an **arbitrary** real symmetric matrix, equivalently even degree-at-most-two spherical polynomials on \(S^4\): the scalar trace provides the constant term on the sphere, and the trace-free matrix provides the quadratic harmonic term. Sign reversal of a sample direction does not affect its rank-one evaluation, so exactly twenty lines are used. E-optimality refers to maximizing the squared least singular value for a fifteen-row, unweighted sampling operator; it does not imply optimality among free point placements or for nonuniform weights.

## Proof
**1. The graph criterion.** In the stated orthonormal matrix coordinates, the measurement row at the direction \(v_{ij}^{s}\), \(s\in\{+1,-1\}\), has entries \(1/2\) in diagonal columns \(i,j\), entry \(s/\sqrt2\) in the offdiagonal column \(ij\), and all other entries zero. If either sign pair \(\{v_{ij}^+,v_{ij}^-\}\) is wholly absent, its offdiagonal column is zero, so the fifteen-row operator is singular. Consequently an invertible fifteen-sample selection contains one member of each of the ten pairs and a second member from exactly five pairs. The doubled pairs form an edge set \(H\) with five edges.

For every doubled pair, take the sum and difference of its two measurement rows. The sum has diagonal part \(e_i+e_j\) and no offdiagonal part; the difference has solely its \(ij\) offdiagonal column. The five singleton-pair offdiagonal columns can also be eliminated. Therefore invertibility is equivalent to invertibility of the unsigned \(5\)-by-\(5\) vertex-edge incidence matrix \(B_H\). Its kernel is the space of vertex potentials satisfying \(u_i+u_j=0\) for every edge of \(H\). Each bipartite component contributes one free potential and each nonbipartite component none. Since \(H\) has five vertices and five edges, an invertible \(B_H\) requires every component to contain an odd cycle. Each such component has at least three vertices, hence \(H\) is connected with one odd cycle. Conversely every such graph gives an invertible unsigned incidence matrix. Leaf elimination along a spanning tree gives \(|\det B_H|=2\).

**2. Determinants and multiplicities.** The sum-and-difference transformation has determinant magnitude \(2^5\). The five pure offdiagonal difference rows contribute \((\sqrt2)^5\), while the five remaining singleton offdiagonal columns contribute \((1/\sqrt2)^5\). Consequently \(|\det\mathcal E_S|=|\det B_H|/2^5=1/16\), proving the uniform squared volume \(1/256\).

Every connected odd-unicyclic simple graph with five vertices either is a five-cycle, or has a triangle and two more vertices arranged as (i) distinct leaves on distinct triangle vertices; (ii) two leaves on the same triangle vertex; or (iii) a two-edge pendant path. On labeled vertices the four counts are respectively \(12,60,30,60\), as follows from choosing the five-cycle, or choosing a triangle in \(\binom53=10\) ways and respectively choosing \(3\cdot2,3,3\cdot2\) attachment choices. A chosen graph allows \(2^5=32\) independent signs on the singly measured edges. Hence there are \(32(12+60+30+60)=5184\) bases, and all \(10,320\) other fifteen-subsets are singular.

**3. Exact characteristic polynomial for all shapes.** Changing the sign of a singleton measurement corresponds to conjugating by a diagonal orthogonal sign change on its offdiagonal coefficient. Permuting the five coordinate axes also acts orthogonally. Thus the Gram spectrum depends only on the four graph shapes. Let \(Q_H=B_HB_H^{\mathsf T}\) be the unsigned graph signless Laplacian, and write \(J\) for the all-ones \(5\)-by-\(5\) matrix. In the diagonal-plus-offdiagonal coefficient basis, the five offdiagonal coordinates at doubled edges yield five unit eigenvalues. On the other ten coordinates the diagonal block equals \((3I+J+Q_H)/4\), the singleton offdiagonal block is \(I/2\), and the cross-block has product \((3I+J-Q_H)/8\). A Schur-complement computation therefore gives the exact polynomial identity
\[
\det(tI_{15}-\mathcal E_S^*\mathcal E_S)
=\frac{(t-1)^5}{4^5}\det\!\left((4t^2-5t)I_5-tJ+(1-t)Q_H\right).
\]
The identity holds for any fifteen-sample selection with one or two signs per edge and exactly five doubled edges (the nonsingularity criterion is not needed in this algebraic step).

Define \(P_H(t)=4^{-5}\det((4t^2-5t)I-tJ+(1-t)Q_H)\), and let \(F(t)=16t^4-52t^3+53t^2-17t+1\). Direct determinant expansion of the four \(5\)-by-\(5\) integer-polynomial matrices gives:

| Sorted vertex degrees of \(H\) | \(512P_H(t)\) |
| --- | --- |
| \((2,2,2,2,2)\) | \((2t^2-7t+2)F(t)^2\) |
| \((1,1,2,3,3)\) | \(F(t)(32t^6-216t^5+498t^4-499t^3+219t^2-39t+2)\) |
| \((1,1,2,2,4)\) | \((2t-1)(4t^2-6t+1)^2(16t^5-104t^4+220t^3-182t^2+49t-2)\) |
| \((1,2,2,2,3)\) | \((2t-1)(4t^2-6t+1)(64t^7-512t^6+1528t^5-2182t^4+1548t^3-506t^2+65t-2)\) |

The signs and leading constants are fixed by the displayed determinant identity and are verified independently against the direct fifteen-row Gram determinants in `verify_exact.py`.

**4. Sharp least-eigenvalue comparison.** Sturm rational root counting applied to the four exact polynomials proves that the smallest positive root of each lies, respectively, in the following disjoint rational intervals:
\[
\begin{array}{c|c}
(2,2,2,2,2),(1,1,2,3,3)&(75/1000,76/1000)\\
(1,1,2,2,4)&(49/1000,50/1000)\\
(1,2,2,2,3)&(43/1000,44/1000).
\end{array}
\]
For both first-row shapes the factor \(F\) has exactly one root in the stated interval and no root below it; the other factors have no smaller roots. Thus their least eigenvalue is the **same** root \(\alpha\), whereas the other two shape types have smaller least eigenvalues. This establishes optimality and all equality cases. The displayed decimal approximations are for orientation only; the polynomial factorization and Sturm isolation are the proof.

## Verification
Run `python3 verify_exact.py` with SymPy installed, from the directory containing this file. It checks the unsigned incidence identity, enumerates every one of the \(\binom{10}{5}=252\) possible doubled-edge sets, confirms the four graph classes and their counts, constructs a direct exact rational fifteen-by-fifteen measurement Gram matrix for one representative of each class, compares its complete characteristic polynomial against the independent graph determinant formula, checks the uniform Gram determinant and certifies the least-root ordering with Sturm exact rational root counts. Run `python3 verify_numeric.py` with NumPy installed for a separately constructed floating-point check of **all \(5,184\)** nonsingular fifteen-sample operators and their smallest eigenvalues and determinants. The proof applies to the finite domain in full; numerical checks are supplementary and do not establish the exact spectral ordering.

## Relationship to prior work
Xiao and Zhuang (2023) develop spherical tight framelets and sampling from spherical designs, motivating stable finite spherical measurements; the available first preprint and author-supplied full text do not contain this twenty-line type-\(D_5\), fifteen-sample optimization. Monfared and Mallik (2018) study signless incidence Laplacian determinants; their odd-unicyclic graph facts are classical ingredients, not asserted as new here. Existing work on cuboctahedral quadratic harmonic erasures gives a different twelve-point, three-dimensional rank matroid. Work on constant-plus-edge Walsh sampling of perfect matchings already yields a related odd-unicyclic determinant classification, so neither odd-cycle basis selection alone nor the uniform determinant phenomenon is claimed to be intrinsically new. The distinguishing conclusion here is the complete Frobenius-normalized **least-singular-value trichotomy** and the two **E-optimal** graph shapes within the determinant-degenerate class of bases. Searches and material comparisons found no covering theorem, though historical uniqueness is not certified.

## Limitations
Only the specified twenty projective root directions, unweighted **fifteen-point** subsets, and degree-at-most-two even spherical data on \(S^4\) are treated. The result does not address noisy data beyond linear least-squares amplification, arbitrary continuous sampling locations, complex Hermitian matrices, higher harmonic degree, or universal optimality over all spherical designs. Singular subsets have zero minimum eigenvalue but their finer rank distribution is not classified. Literature searches cannot rule out a previously unindexed equivalent enumeration or a strong general theorem implying the E-optimal classification; independent mathematical and priority assessment remains outstanding.

## References
1. Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365v1, first public 2023-03-09; SIAM Journal on Imaging Sciences 16 (2023), 2072–2104, DOI 10.1137/22M1542362, https://arxiv.org/abs/2303.05365 .
2. K. H. Monfared and S. Mallik, *An Analog of Matrix Tree Theorem for Signless Laplacians*, arXiv:1805.04759v1, first public 2018-05-12, https://arxiv.org/abs/1805.04759 .
3. *The tetrahedral graphic matroid controls quadratic-harmonic sampling on the cuboctahedron*, dated 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-tetrahedral-graphic-matroid-controls-quadratic-harmonic-samp--22932f55648e .
4. *Exact Walsh sampling determinants and optimal coordinate bases on perfect matchings*, dated 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-walsh-sampling-determinants-and-optimal-coordinate-bases-o--737b012e9a14 .
5. *Exact spherical-harmonic sampling spectrum of the regular 24-cell*, dated 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-spherical-harmonic-sampling-spectrum-of-the-regular-24-cel--2b17ab9c73cb .
