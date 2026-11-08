# Euclidean incenters of minimal-matroid base polytopes form rank-corank simplices

## Finding

Let \(k,r\ge 2\) be integers, \(n=k+r\), and let \(P_{k,r}\) be the canonical, incidence-vector base polytope of the connected minimal matroid of rank \(k\) on \(n\) elements. In the intrinsic Euclidean metric inherited from \(\mathbb R^n\), put
\[
 h=\sqrt{\frac{n-1}{n}},\qquad b=\sqrt{\frac{kr}{n}},\qquad M=\max\{k,r\},\qquad m=\min\{k,r\}.
\]
Then the exact largest-inscribed-ball radius is
\[
 \boxed{\rho_{k,r}=\frac1{Mh+b}=
 \frac{\sqrt n}{M\sqrt{n-1}+\sqrt{kr}}.}
\]

After the Euclidean isometry \(y_i=1-x_i\) for the first \(k\) coordinates and \(z_j=x_{k+j}\) for the remaining \(r\) coordinates, set \(\ell=h\rho_{k,r}\). If \(k>r\), the **entire incenter locus** is
\[
 \mathcal I_{k,r}=\left\{(y,z):
 y_i=\ell\ (1\le i\le k),\quad
 z_j=\ell+w_j\ (1\le j\le r),\quad
 w_j\ge0,\ \sum_{j=1}^r w_j=(k-r)\ell\right\}.
\]
If \(r>k\), exchange \(y,k\) with \(z,r\). If \(k=r\), the unique incenter has all \(n\) transformed coordinates equal to \(\ell\). Therefore the optimal-center set is a regular simplex of affine dimension \(m-1\) and edge length \(\sqrt2\,|k-r|\ell\) when \(k\ne r\), and is a singleton precisely when \(k=r\).

At an incenter in the relative interior of the center simplex, exactly \(M+1\) facets of \(P_{k,r}\) are tangent to the optimal ball when \(k\ne r\). In the balanced case all \(n+1\) facets are tangent. For fixed \(n\ge4\), the maximum incenter-locus dimension among all connected minimal-matroid base polytopes of ground-set size \(n\) is sharply
\[
 \boxed{\left\lfloor\frac{n-3}{2}\right\rfloor.}
\]

## Assumptions and scope

The minimal matroid is the unique connected matroid with the fewest bases at the given rank and ground-set size; the rank and corank satisfy \(k,r\ge2\). Label the \(k\) black elements first and \(r\) mutually parallel red elements last, as in Ferroni's graphical realization. The canonical metric means the restriction of the standard ambient Euclidean metric to the affine span \(\sum x_i=k\), not a metric transported from an affinely equivalent order polytope. Balls, centers and facet distances are all taken in this \((n-1)\)-dimensional affine span. The exact statements concern this canonical realization; arbitrary affine deformation need not preserve them.

## Proof

**1. Vertex and halfspace model.** The bases in Ferroni's graphical model consist of all \(k\) black elements or of exactly one red element and all black elements except one. On applying the coordinate reflections specified above, this yields
\[
 Q_{k,r}=\operatorname{conv}\bigl(\{0\}\cup\{e_i+f_j:1\le i\le k,\ 1\le j\le r\}\bigr),
\]
where \(e_i\) and \(f_j\) are mutually orthogonal standard vectors. The affine span becomes
\[
 H=\{(y,z):\sum_i y_i=\sum_j z_j\},\quad
 s=\sum_i y_i=\sum_j z_j.
\]
Exactly (not merely necessarily),
\[
 Q_{k,r}=\{(y,z)\in H:y_i\ge0,\ z_j\ge0,\ s\le1\}.
\]
For the reverse inclusion, when \(s>0\), let \(a_{ij}=y_i z_j/s\). Then \(a_{ij}\ge0\), \(\sum_{ij}a_{ij}=s\), and \((y,z)=(1-s)0+\sum_{ij}a_{ij}(e_i+f_j)\). The case \(s=0\) gives only the origin. For \(k,r\ge2\), every coordinate inequality is a genuine facet (the origin and the corresponding base-face vertices affinely span a hyperplane of dimension \(n-2\)), and \(s\le1\) is the base facet; hence there are exactly \(n+1\) facets.

**2. Intrinsic normal lengths.** The unit normal to \(H\) in ambient space is \(u=(\mathbf1_k,-\mathbf1_r)/\sqrt n\). The projected normal for every coordinate inequality has length
\[
 \|\operatorname{proj}_{H} e_i\|=\|\operatorname{proj}_{H}f_j\|=h=\sqrt{(n-1)/n}.
\]
For the base facet, the projected normal to \(s=\sum y_i\) has length
\[
 \left\|\operatorname{proj}_{H}(\mathbf1_k,0)\right\|=b=\sqrt{kr/n}.
\]
Thus a radius-\(\rho\) ball with center \((y,z)\in H\) is contained in \(Q_{k,r}\) if and only if
\[
 y_i\ge h\rho\quad(1\le i\le k),\qquad
 z_j\ge h\rho\quad(1\le j\le r),\qquad
 s+b\rho\le1.
\]
No other inequalities are needed because the displayed halfspaces define the entire polytope.

**3. Sharp bound and attainment.** The two group sums agree with \(s\), so these inequalities force \(s\ge Mh\rho\). Combining with the base-facet constraint gives \(\rho\le1/(Mh+b)\). For equality let \(\rho=1/(Mh+b)\), \(\ell=h\rho\), \(s=M\ell\), and set \(y_i=s/k\), \(z_j=s/r\). Each coordinate is at least \(\ell\), and the base constraint is equality. This is an admissible inscribed ball of the asserted radius.

**4. Every center and all contacts.** At the optimum, \(Mh\rho+b\rho=1\). Consequently every optimal center must satisfy simultaneously \(s=M\ell\) and the coordinate lower bounds. All \(M\) coordinates in a largest group are therefore exactly \(\ell\); the remaining \(m\) coordinates have the form \(\ell+w_j\), with \(w_j\ge0\) summing to \((M-m)\ell\). Conversely every such point satisfies all inscribed-ball inequalities. If \(M>m\), the \(m\) vertices of this center simplex are obtained by concentrating all the surplus in one of the smaller-group coordinates. Their pairwise Euclidean distance is \(\sqrt2(M-m)\ell\), so the simplex is regular and has affine dimension \(m-1\). If \(M=m\), the surplus vanishes and the center is unique.

The base facet and the \(M\) largest-group coordinate facets are always tangent. The smaller-group facets are strictly separated at relative-interior centers when the groups are unequal, and all coordinate facets are tangent in the balanced case. On a boundary face of the center simplex additional smaller-group coordinate facets become tangent; these are precisely the coordinates with \(w_j=0\).

**5. Sharp rank extremum.** With \(k+r=n\), the center-locus dimension is \(\min(k,r)-1\) except that it drops to zero at equality \(k=r\). The largest attainable value for \(n\ge4\) is \(\lfloor(n-3)/2\rfloor\): use the two adjacent sizes when \(n\) is odd and the sizes differing by two when \(n\) is even; for \(n=4\) the sole admissible pair is balanced.

## Verification

The standalone file `check_minimal_matroid_inball.py` solves the intrinsic Euclidean Chebyshev-center linear program independently using numerical linear programming for all \(121\) ordered shapes \(2\le k,r\le12\). It compares the optimum against the formula, constructs each extreme center of the predicted regular simplex, checks the exact group-sum equality numerically, and checks all shifted facet inequalities. The finite checks are corroboration; the proof above handles all integer parameter values.

Run from a directory containing the file: `python check_minimal_matroid_inball.py` (NumPy and SciPy are required). Expected output: `MINIMAL_MATROID_INBALL_FINITE_CHECKS_PASSED shapes=121`.

## Relationship to prior work

Ferroni, *On the Ehrhart Polynomial of Minimal Matroids*, arXiv:2003.02679 (first posted March 5, 2020), identifies the minimal matroid and provides the decisive polytope inequality description (Proposition 2.6 in the journal version); its subject is Ehrhart theory and lattice volume, not intrinsic inballs. Knauer, Martínez-Sandoval and Ramírez Alfonsín, arXiv:1701.05529, and Benedetti, Knauer and Valencia-Porras, arXiv:2303.10458, connect snake matroid polytopes to order polytopes by **affine** equivalence; the relevant affine change of coordinates is not generally Euclidean-isometric. The earlier published minimum-enclosing-sphere result for minimal-matroid polytopes concerns an outer ball, not the inner ball. A prior rank-two matroid inradius theorem does subsume the \(k=2\) and, by duality, \(r=2\) boundaries; the genuinely higher-rank/corank family and its complete incenter simplices are the contribution assessed here.

## Limitations

This is a Euclidean result for the incidence-vector realization, not an affine-invariant assertion. The proof neither classifies the incenter loci of arbitrary matroid base polytopes nor gives the optimal ellipsoid for this family. Searches cannot rule out an unlocated earlier equivalent computation under product-of-simplices pyramid or Chebyshev-center terminology. Some related research-record full texts were inaccessible, so historical priority remains provisional. Independent external mathematical audit has not been performed.

## References

1. L. Ferroni, *On the Ehrhart Polynomial of Minimal Matroids*, arXiv:2003.02679, preprint dated 2020-03-05; *Discrete & Computational Geometry* **68** (2022), 255–273, DOI:10.1007/s00454-021-00313-4. See Proposition 2.2 and Proposition 2.6.
2. K. Knauer, L. Martínez-Sandoval, J. L. Ramírez Alfonsín, *On lattice path matroid polytopes: integer points and Ehrhart polynomial*, arXiv:1701.05529 (2017); *Discrete & Computational Geometry* **60** (2018), 698–719. See Theorems 4.1 and 4.7.
3. C. Benedetti, K. Knauer, J. Valencia-Porras, *On lattice path matroid polytopes: alcoved triangulations and snake decompositions*, arXiv:2303.10458 (2023), Theorem 3.3.
4. Published mathematical research records (2026-10-11): *Minimal-matroid base polytopes have a one-exception minimum-sphere transition* (identifier suffix 82125c812c6f), and *Exact Euclidean inradius of connected rank-two matroid base polytopes* (identifier suffix 04d0301093d4). The compared record summaries, not inaccessible full text, supplied the respective prior statements.
