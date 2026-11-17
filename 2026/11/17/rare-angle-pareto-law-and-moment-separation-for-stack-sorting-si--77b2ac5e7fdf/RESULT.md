# Rare-angle Pareto law and moment separation for stack-sorting simplices

## Finding

For each integer \(n\ge3\), let \(s\) be West's deterministic stack-sorting map and let \(\tau_n=23\cdots n1\). In the Euclidean metric inherited from \(\mathbb R^n\), define the \((n-1)\)-simplex
\[
T_n=\operatorname{conv}\{s^j(\tau_n):0\le j\le n-1\}.
\]
The multiset of *interior* dihedral angles along its \(\binom n2\) ridges is exactly
\[
\underbrace{\{\pi/2,\ldots,\pi/2\}}_{\binom{n-1}{2}\text{ occurrences}}
\ \cup\
\left\{\arccos\sqrt{\frac{n}{(n-1)k(k-1)}}:\ k=2,\ldots,n\right\}.
\]
The \(n-1\) acute angles are strictly increasing with \(k\), hence all \(n\) angle values are distinct.

Choose a ridge uniformly among the \(\binom n2\) ridges, denote its interior angle by \(\Theta_n\), and put \(\Delta_n=\pi/2-\Theta_n\). Then \(\mathbb P(\Delta_n>0)=2/n\). Conditional on \(\Delta_n>0\), the scaled deficit \(Y_n=n\Delta_n\) converges weakly to a Pareto random variable of shape one:
\[
\mathbb P(Y\le t)=\begin{cases}0,&t<1,\\1-t^{-1},&t\ge1.\end{cases}
\]
The conditional moments are not uniformly integrable. More precisely, with the convergent, positive constant
\[
C_2=\sum_{k=2}^{\infty}\arcsin^2\!\left(\frac1{\sqrt{k(k-1)}}\right),
\]
we have
\[
\mathbb E(Y_n\mid\Delta_n>0)=\log n+O(1),\qquad
\mathbb E(Y_n^2\mid\Delta_n>0)\sim C_2 n.
\]
For the unconditioned uniform-ridge deficit, the exact leading moments are
\[
\mathbb E\Delta_n=\frac{2\log n+O(1)}{n^2},\qquad
n^2\operatorname{Var}(\Delta_n)\longrightarrow2C_2.
\]
Thus a vanishing \(2/n\) fraction of acute ridges carries a nontrivial heavy-tailed conditional law, while the variance is governed by its rare fixed-index large-angle tail.

## Assumptions and scope

The coordinates of a permutation are its entries as a point in \(\mathbb R^n\); all distances and angles are those of the ambient Euclidean inner product restricted to the fixed-sum affine hyperplane. The term *ridge* means an \((n-3)\)-face of the \((n-1)\)-simplex, incident to exactly two facets; a triangle's vertices count as its ridges. The random ridge is uniform over the *unoriented* ridge set, not uniform over a spherical normal cone or over interior volume. Convergence refers to the integer sequence \(n\to\infty\). The assertion is for the canonical permutation \(23\cdots n1\), not arbitrary stack-sorting or lecture-hall simplices.

## Proof

**1. Orbit coordinates.** Set \(e=(1,2,\ldots,n)\). The stack-sorting recurrence on the prefix \(23\cdots k1\) sends it to \(23\cdots(k-1)1k\), and leaves the already increasing suffix \((k+1)\cdots n\) fixed. Hence the distinct orbit points, in reverse order, are \(e\) and \(e+d_k\), \(2\le k\le n\), where
\[
d_k=(\underbrace{1,\ldots,1}_{k-1},1-k,0,\ldots,0).
\]
These coordinates are also implied by the orbit classification in Lee--Mitchell--Vindas-Meléndez (Corollary 3.8). Directly, \(d_k\cdot d_j=0\) for \(j\ne k\), while \(\|d_k\|^2=k(k-1)\). Thus this is a simplex with a Euclidean orthogonal corner at \(e\), though orthogonality alone is not the asserted angle or limit theorem.

**2. Entire dihedral spectrum.** Translate \(e\) to the origin. In the mutually orthogonal coordinates defined by \(d_k\), the simplex is the convex hull of \(0,d_2,\ldots,d_n\). Write
\[
b=\sum_{k=2}^{n}\frac{d_k}{k(k-1)},\qquad \|b\|^2=\sum_{k=2}^{n}\frac1{k(k-1)}=\frac{n-1}{n}.
\]
An outward normal to the facet opposite the origin is \(b\). For each \(k\ge2\), an outward normal to the facet opposite \(d_k\) is \(-d_k/[k(k-1)]\). Any two of the latter normals are orthogonal. The scalar product of \(b\) with the \(k\)-th normal is \(-1/[k(k-1)]\), so their normalized outward cosine is
\[
-\sqrt{\frac{n}{(n-1)k(k-1)}}.
\]
The interior angle is the supplement of the outward-normal angle, yielding \(\Theta_{n,k}=\arccos\sqrt{n/[(n-1)k(k-1)]}\). Its associated deficit is
\[
\delta_{n,k}=\arcsin\sqrt{\frac{n}{(n-1)k(k-1)}}.
\]
There are \(\binom{n-1}{2}\) right-angle pairs and \(n-1\) exceptional pairs, establishing the exact multiset and \(\mathbb P(\Delta_n>0)=2/n\).

**3. Pareto limit.** Given \(\Delta_n>0\), the index \(K_n\) is uniform on \(\{2,\ldots,n\}\). Then \(K_n/n\) converges in distribution to uniform measure on \((0,1)\). Whenever \(k/n\to u>0\), the small-angle expansion \(\arcsin z=z+O(z^3)\) gives \(n\delta_{n,k}\to1/u\). The continuous mapping theorem away from the null endpoint \(u=0\) shows \(Y_n\Rightarrow 1/U\), which has exactly the asserted Pareto distribution.

**4. Moment separation.** Put \(A_n=\sum_{k=2}^n\delta_{n,k}\) and \(B_n=\sum_{k=2}^n\delta_{n,k}^2\). Uniformly for \(k\ge3\),
\[
\delta_{n,k}=\frac1{\sqrt{k(k-1)}}+O\left(\frac1{nk}+\frac1{k^3}\right).
\]
The remaining \(k=2\) term is uniformly bounded. Since the harmonic comparison gives \(\sum_{k=2}^n[k(k-1)]^{-1/2}=\log n+O(1)\), we have \(A_n=\log n+O(1)\). For each fixed \(k\), \(\delta_{n,k}\to\arcsin([k(k-1)]^{-1/2})\). A uniform \(O(k^{-2})\) bound on their squares, plus dominated convergence for series, gives \(B_n\to C_2\). Since every nonzero angle occurs exactly once,
\[
\mathbb E(Y_n\mid\Delta_n>0)=\frac{nA_n}{n-1},\quad
\mathbb E(Y_n^2\mid\Delta_n>0)=\frac{n^2 B_n}{n-1},
\]
and
\[
\mathbb E\Delta_n=\frac{2A_n}{n(n-1)},\quad
\operatorname{Var}\Delta_n=\frac{2B_n}{n(n-1)}-\left(\frac{2A_n}{n(n-1)}\right)^2.
\]
The displayed asymptotics follow. The limiting Pareto law has infinite first and second moments, consistently with the diverging conditional moments. This completes the proof.

## Verification

The accompanying `check_angles.py` uses only the Python standard library. Run `python3 check_angles.py` to replay independently implemented stack-sorting orbits for every \(3\le n\le60\), exact integral/rational Gram and facet-normal identities and every facet-pair classification, followed by numerical finite-size checks for \(n=100,1000,10000\). The observed successful output is `STACK_SORT_RARE_ANGLES_PASS n=3..60 orbit_vertices=1827 facet_pairs=35989 asymptotics=100,1000,10000`. This is a finite corroboration, not an infinite proof; the unrestricted result follows from the preceding argument.

## Relationship to prior work

Lee, Mitchell and Vindas-Meléndez introduced the canonical simplex, established the stack-sort orbit description and its combinatorial and Ehrhart structure (first public preprint August 31, 2023). Ake, Lewis, Louie and Vindas-Meléndez later proved the Euclidean volume and relative volume of all \(Ln1\) stack-sorting simplices (first public preprint July 31, 2025). Their coordinate and altitude computations are compatible with this orthogonal-corner representation. Neither of the relevant geometric sections inspected presents the entire ridge-dihedral multiset, its conditional Pareto limit, or the asymptotic variance coefficient. The elementary calculation of a facet angle from outward normals is standard; it is not claimed as a new general method. Existing solid-angle results for arbitrary orthogonal simplices concern vertex cones, rather than this uniform-ridge measure. Historical noncoverage beyond the searched sources remains provisional.

## Limitations

The formula depends on the standard Euclidean coordinate realization; lattice equivalence does not preserve dihedral angles. The heavy-tailed law is conditional on a rare class of ridges and is not the weak limit of the unconditional deficit (which tends to zero). The theorem neither establishes independent mathematical verification nor proves global historical priority. The exact angle classification is analytic; finite checker runs are only supporting evidence.

## References

1. E. Lee, C. Mitchell and A. R. Vindas-Meléndez, *Stack-sorting simplices: geometry and lattice-point enumeration*, arXiv:2308.16457, initially posted 2023-08-31. https://arxiv.org/abs/2308.16457
2. C. Ake, S. F. Lewis, A. Louie and A. R. Vindas-Meléndez, *On the geometry of stack-sorting simplices*, arXiv:2508.00219, initially posted 2025-07-31. https://arxiv.org/abs/2508.00219
