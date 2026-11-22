# Exact weighted hyperplane-blocking thresholds for regular-simplex ball obstacles

## Finding

**Theorem (weighted hyperplane obstruction and complete equality profiles).** Fix an integer \(d\ge2\), let \(N=d+1\), and let \(v_1,\ldots,v_N\in\mathbb R^d\) be the vertices of a regular simplex with centroid \(0\), each with norm \(R>0\). Choose *arbitrary* weights \(b_1,\ldots,b_N>0\), and form the union of open balls
\[
E_\lambda=\bigcup_{i=1}^N B(v_i,\lambda Rb_i),\qquad \lambda>0.
\]
For any nonempty proper subset \(S\subset[N]\), write \(T=[N]\setminus S\), \(B_S=\sum_{i\in S}b_i\), and \(B_T=\sum_{j\in T}b_j\). Define \(z^S\in\mathbb R_{>0}^N\) as follows:

- If \(B_S\ge B_T\), set \(z_i^S=b_i\) for \(i\in S\). On \(T\), choose the unique *water-filling* vector \(z_j^S=\max\{b_j,c\}\) whose sum is \(B_S\); when \(B_S=B_T\), this simply means \(z_j^S=b_j\) for every \(j\in T\).
- If \(B_T>B_S\), interchange \(S,T\): retain the lower bounds on \(T\) and water-fill \(S\) up to total \(B_T\).

The water-filled vector is uniquely defined even if the level \(c\) is not unique at the degenerate equal-sum endpoint. Put
\[
\mathcal E(S)=\sum_{i=1}^N(z_i^S)^2,\quad
\mathcal E_* =\min_{\varnothing\ne S\subsetneq[N]}\mathcal E(S),\qquad
\boxed{\lambda_* =\sqrt{\frac{N}{d\mathcal E_*}}.}
\]
Then **every hyperplane through the centroid meets** \(E_\lambda\) **if and only if** \(\lambda>\lambda_*\). At \(\lambda=\lambda_*\), all and only the avoiding *unoriented* hyperplanes are those whose unit normal \(u\) has the vertex projection profile
\[
\boxed{\langle u,v_i/R\rangle=
\begin{cases}
+\lambda_*z_i^S,&i\in S,\\
-\lambda_*z_i^S,&i\notin S,
\end{cases}}
\]
for subsets \(S\) minimizing \(\mathcal E\), with \(S\) and its complement representing the same hyperplane. Thus the threshold and **all equality configurations** are determined by a finite, explicit set of one-dimensional water-filling problems; no continuous directional optimization remains.

When all \(b_i=1\), the minimizing bipartitions have sizes \(\lfloor N/2\rfloor\) and \(\lceil N/2\rceil\), and the threshold simplifies to
\[
\lambda_*=\sqrt{\frac{\lfloor N/2\rfloor}{d\lceil N/2\rceil}}.
\]
This equal-weight case shares its balanced optimal directions with classical regular-simplex minimum-width theory, whose priority is fully credited below; it is not presented as a new optimizer classification by itself.

**Unequal-weight example.** In dimension \(d=3\), the weights \((1,1,1,2)\) have \(\mathcal E_*=19/2\), attained by partitions placing the weight-\(2\) vertex with one weight-\(1\) vertex opposite the remaining pair. The optimal magnitudes are \((2,1,3/2,3/2)\), up to permutation of the three unit weights, and \(\lambda_*=\sqrt{8/57}\). Unlike equal-weight minimizers, these profiles have three distinct positive magnitudes, making the water-filling active set essential.

**Geometric consequence.** Set \(b_{\max}=\max_i b_i\) and \(Q=\max_{i\ne j}(b_i+b_j)\). If
\[
\lambda_*<\min\left\{\frac1{b_{\max}},\frac{\sqrt{2N/d}}Q\right\},
\]
then any \(\lambda\) strictly between these two sides has pairwise disjoint balls avoiding the centroid, but every hyperplane through each point of the nonempty open ball
\[
B\left(0,R\min\{1-\lambda b_{\max},\ (\lambda-\lambda_*)\min_i b_i\}\right)
\]
meets \(E_\lambda\). The strict inequality holds for equal weights in every dimension and, by continuity, throughout an open neighborhood of the equal-weight ray in positive weight space. Thus *unequal and disjoint* balls can possess an interior hyperplane-nonconvexity-point region.

## Assumptions and scope

A hyperplane is an affine subspace of codimension one. The balls are **open**, so tangency does not count as intersection; the endpoint \(\lambda=\lambda_*\) therefore belongs to the avoiding regime. The nonconvexity-point set consists of points *outside* \(E_\lambda\) at which every affine hyperplane intersects \(E_\lambda\), in the sense of the \((d-1)\)-nonconvexity-point set. The weights are dimensionless radii relative to the circumradius; no condition of weak \((d-1)\)-convexity on the union itself is presumed. The theorem gives an exact finite optimization formula rather than a polynomial-time algorithm for arbitrary weights.

## Proof

**1. Reduction to the sum-zero frame.** Let \(w_i=v_i/R\). Regular-simplex geometry gives
\[
\sum_i w_i=0,\quad \langle w_i,w_j\rangle=\delta_{ij}-\frac{1-\delta_{ij}}d,\quad
\sum_iw_iw_i^{\mathsf T}=\frac NdI_d.
\]
Hence the projection vector \(a_i=\langle u,w_i\rangle\) of a unit normal satisfies
\[\sum_i a_i=0,\qquad \sum_i a_i^2=N/d.\]
Conversely, every vector \(a\in\mathbb R^N\) satisfying these two constraints comes from the *unique* unit normal \(u=(d/N)\sum_i a_i w_i\). The Gram identity proves that this formula reproduces all the \(a_i\) and yields norm one. A hyperplane through \(0\) avoids all the open balls precisely when \(|a_i|\ge\lambda b_i\) for every \(i\).

**2. Solve a fixed sign partition.** A profile avoiding positive-radius balls has all entries nonzero. Choose \(S=\{i:a_i>0\}\), with nonempty complement \(T\). Writing the positive magnitudes \(x_i=|a_i|\), the zero-sum constraint becomes \(\sum_Sx_i=\sum_Tx_j\), while \(x_i\ge\lambda b_i\). Scaling by \(\lambda\), the problem becomes minimization of \(\sum_i z_i^2\) subject to \(z_i\ge b_i\) and equal group totals. For a prescribed total \(L\ge B_S\), the unique least-square vector on \(S\) with \(z_i\ge b_i\) and sum \(L\) is \(z_i=\max(b_i,c_S(L))\), by strict convexity and the Lagrange multiplier/KKT conditions. This vector and its minimum energy depend continuously on \(L\). The minimum energy is strictly increasing in \(L\): decreasing any component strictly above its lower bound while reducing the total decreases its positive square. The same applies on \(T\). Thus the sum of the two minimum energies is minimized at the *smallest feasible common sum* \(L=\max\{B_S,B_T\}\), giving exactly the displayed \(z^S\) and \(\mathcal E(S)\). This also proves uniqueness of the profile for a fixed sign pattern.

**3. Global sharpness and complete equality.** If a unit normal avoids the balls at scale \(\lambda\), its projected magnitudes divided by \(\lambda\) form a feasible vector of energy \((N/d)/\lambda^2\). Consequently
\[
\frac Nd\frac1{\lambda^2}\ge\mathcal E(S)\ge\mathcal E_*,
\]
so \(\lambda\le\lambda_*\). Conversely, select any minimizing subset \(S\), give its unique least-energy vector \(z^S\) signs \(+\) on \(S\) and \(-\) on \(T\), and multiply it by \(\lambda_*\). Its sum is zero and its squared norm is \(N/d\), so Step 1 produces a unit normal. The resulting hyperplane avoids all open balls at \(\lambda_*\). The strict if-and-only-if threshold follows. At \(\lambda_*\), every avoiding profile must realize equality in both energy bounds and hence must coincide with this unique vector for a minimizing subset. Complementing the sign set reverses its normal, giving exactly the stated classification.

**4. Equal weights and nonconvexity interior.** If \(b_i=1\), a group of size \(p\ge q\) is the heavier group; its \(p\) magnitudes remain \(1\), while the other \(q\) are \(p/q\). Thus \(\mathcal E(S)=p+p^2/q=pN/q\). This is smallest at \(p=\lceil N/2\rceil\), proving the displayed equal-weight formula. The ball-center distances are \(\|v_i-v_j\|=R\sqrt{2N/d}\). Hence they are disjoint when \(\lambda Q<\sqrt{2N/d}\), and their complement contains the centroid when \(\lambda b_{\max}<1\). For any unit \(u\) and \(\lambda>\lambda_*\), the global threshold implies some \(i\) has \(|\langle u,v_i\rangle|<\lambda_*Rb_i\) (the non-strict version also suffices). For a point \(y\) of norm less than the displayed neighborhood radius,
\[
|\langle u,v_i-y\rangle|\le\lambda_*Rb_i+\|y\|
<\lambda Rb_i.
\]
Thus every hyperplane through \(y\) intersects \(E_\lambda\); moreover \(\|y-v_i\|\ge R-\|y\|>\lambda Rb_i\), so \(y\notin E_\lambda\). At equal weights, \(\lambda_*^2=\lfloor N/2\rfloor/(d\lceil N/2\rceil)<N/(2d)<1\), proving the strict feasibility condition and, by continuity of all finite water-filling minima, its persistence for nearby unequal weights. \(\square\)

## Verification

The accompanying standard-library `check.py` reproduces the finite exact rational water-filling solution for diverse positive weight vectors, checks partition complement symmetry, equal-weight closed forms and equality norms, and corroborates the sharp inequality with seeded random directions. It performs finite, not exhaustive, computational comparisons; Steps 1–4 prove the result over every dimension and every positive real weight vector. Run `python3 check.py`.

## Relationship to prior work

Osipchuk, arXiv:2611.18216v1 (first public 13 November 2026), defines the \((d-1)\)-nonconvexity-point set and proves general topological statements, but not a hyperplane-blocking scale, a weighted simplex model or an explicit equality classification. Casado, García, Tóth and Hendrix (2010) study covering the entire *simplex* by vertex-centered Euclidean balls via power diagrams, not whether every hyperplane through a point meets those balls; their regular-simplex section does not imply the weighted hyperplane-incidence criterion. Har-Peled and Robson (arXiv:2301.02616) give a modern self-contained account of the **classical** regular-simplex minimum-width formula and its balanced-bipartition minimizers, credited to Gritzmann–Klee and Alexander. Those balanced directions also arise in this theorem's *equal-weight* corollary. The present new object is the arbitrary-weight inverse threshold and its water-filled active-set/equality characterization, which neither the classical width criterion nor its global optimizers supplies. Bezdek and Lángi (arXiv:2201.11234) study great-circle inradii and spherical zone coverings, including the optimal arrangement problem; that is distinct from the arbitrary vertex-weighted equator-avoidance threshold of a fixed regular simplex. Related published weighted-simplex zonotope and weighted-minimum-sphere results have different optimization constraints and do not dominate the stated balanced-sign water-filling formula.

## Limitations

The centers must form a regular simplex and the balls have a common scale \(\lambda\) times arbitrary fixed positive radii. The theorem does not characterize nonconvexity points globally, solve the general placement problem, or claim polynomial-time evaluation of the subset minimum. Its equal-weight optimizer directions are already classical in width theory, as explicitly credited. The checked published literature and mathematical records do not prove exhaustive historical priority; independent mathematical review has not been performed.

## References

1. T. M. Osipchuk, *On weakly \(m\)-convex sets, \(m=1,\ldots,n-1\), in \(n\)-dimensional Euclidean spaces*, arXiv:2611.18216v1, first publicly posted 13 November 2026, https://arxiv.org/html/2611.18216v1.
2. L. G. Casado, I. García, B. G. Tóth and E. M. T. Hendrix, *On determining the cover of a simplex by spheres centered at its vertices*, Journal of Global Optimization 50 (2011), 645–655, first online 23 January 2010, https://doi.org/10.1007/s10898-010-9524-x.
3. S. Har-Peled and E. W. Robson, *On the Width of the Regular \(n\)-Simplex*, arXiv:2301.02616v1, first publicly posted 6 January 2023, https://arxiv.org/html/2301.02616v1.
4. P. Gritzmann and V. Klee, *Inner and Outer \(j\)-Radii of Convex Bodies in Finite-Dimensional Normed Spaces*, Discrete & Computational Geometry 7 (1992), 255–280, https://doi.org/10.1007/BF02187841.
5. K. Bezdek and Zs. Lángi, *From the separable Tammes problem to extremal distributions of great circles in the unit sphere*, arXiv:2201.11234v3, https://arxiv.org/html/2201.11234v3.
