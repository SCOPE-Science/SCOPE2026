# A quadratic tangency transition for stable-set polytopes of clique-joined odd cycles

## Finding

For integers \(a\ge 2\), \(t\ge 1\), put \(m=2a+1\), \(N=m+t\), and let \(G_{a,t}=C_m\vee K_t\) be the graph join of the chordless odd cycle and a complete graph. In its canonical indicator-coordinate Euclidean realization, the stable-set polytope \(P_{a,t}=\operatorname{STAB}(G_{a,t})\subset\mathbb R^N\) has the unique Euclidean incenter \(r_{a,t}\mathbf1_N\) and exact inradius
\[
r_{a,t}=\min\left\{\frac{1}{t+2+\sqrt{t+2}},
\frac{a}{2a+1+at+\sqrt{2a+1+a^2t}}\right\}.
\]
Its complete set of \(2m+t+1=N+m+1\) facets consists of \(N\) coordinate nonnegativity facets, \(m\) lifted cycle-edge clique facets and one lifted odd-hole facet.

For \(a=2\), only the coordinate facets and the odd-hole facet contact the largest ball, for every \(t\ge1\). For \(a\ge3\), define the integer \(T_a=a^2-2a-1\). The contact sets are: all \(N\) coordinate facets and all \(m\) clique facets if \(1\le t<T_a\); **all \(N+m+1\) facets** if \(t=T_a\); and all \(N\) coordinate facets and just the odd-hole facet if \(t>T_a\). Thus \(P_{a,t}\) is Euclidean-tangential (has one ball tangent to every facet) exactly when \(a\ge3\) and \(t=a^2-2a-1\). In that case \(r_{a,t}=1/[a(a-1)]\). Outside the boundary, the numbers of tangent facets are, respectively, \(N+m\) and \(N+1\).

## Assumptions and scope

A stable set contains no adjacent graph vertices and includes the empty set. Its polytope is the convex hull of all corresponding \(0\)-\(1\) characteristic vectors. The graph join adds all edges between the \(m\) cycle vertices and the \(t\) clique vertices. Coordinates \(x_1,\ldots,x_m\) index the rim, cyclically, and \(y_1,\ldots,y_t\) index the clique. The metric is the ambient, unweighted Euclidean metric on \(\mathbb R^N\), not a lattice-normalized or transformed metric. All parameters are integers in the displayed ranges.

A ball of radius \(r\) and center \(c\) fits inside the full-dimensional polytope \(\{z:h_j\cdot z\le b_j\}\) exactly when \(h_j\cdot c+r\|h_j\|_2\le b_j\) for every facet inequality. A contact facet has equality.

## Proof

**1. Exhaustive facet description.** For a chordless odd cycle \(C_{2a+1}\), its stable-set polytope has exactly the \(m\) inequalities \(x_i\ge0\), the \(m\) inequalities \(x_i+x_{i+1}\le1\), and the odd-cycle inequality \(\sum_i x_i\le a\). This familiar complete facet representation follows from the t-perfectness of cycles; it is also recorded in Miyazaki's work on cycle stable-set polytopes [1].

For \(G_{a,t}\), every stable set is either a stable set in the rim with all hub coordinates zero, or one singleton clique vertex. Thus
\[
P_{a,t}=\operatorname{conv}\bigl((\operatorname{STAB}(C_m),0), (0,e_1),\ldots,(0,e_t)\bigr).
\]
Writing \(u=\sum_jy_j\), a point with \(0\le u<1\) belongs to this convex hull precisely when \(y\ge0\) and \(x/(1-u)\in\operatorname{STAB}(C_m)\). For \(u=1\), the displayed inequalities force \(x=0\). Homogenizing the rim facets therefore yields the complete inequalities
\[
x_i\ge0,\quad y_j\ge0;\qquad
x_i+x_{i+1}+\sum_{j=1}^t y_j\le1\quad(1\le i\le m);
\qquad
\sum_{i=1}^m x_i+a\sum_{j=1}^t y_j\le a.
\]
All are facets: each rim facet lifts to a face containing an \((m-1)\)-dimensional affine span of tight rim points together with the \(t\) affinely independent hub unit vectors, yielding face dimension \(m+t-1\). The coordinate facets follow similarly from the full-dimensional coordinate faces. The origin together with all \(N\) standard unit vectors shows \(P_{a,t}\) has dimension \(N\). No facets are missing because the inequality representation is exact.

**2. Sharp radius bounds.** Suppose the ball \(B(c,r)\) lies in \(P_{a,t}\). The \(N\) coordinate facets imply \(c_i\ge r\) and \(c_{m+j}\ge r\). Each lifted edge-clique facet has a normal with \(t+2\) unit entries and hence Euclidean norm \(\sqrt{t+2}\). Consequently, for each \(i\),
\[
1\ge c_i+c_{i+1}+\sum_j c_{m+j}+r\sqrt{t+2}
\ge r(t+2+\sqrt{t+2}).
\]
The lifted odd-hole facet has a normal with \(m\) unit entries and \(t\) entries equal to \(a\), and thus norm \(\sqrt{m+a^2t}\). Therefore
\[
a\ge\sum_i c_i+a\sum_j c_{m+j}+r\sqrt{m+a^2t}
\ge r(m+at+\sqrt{m+a^2t}).
\]
These prove both upper bounds in the stated minimum. Conversely put \(c=r\mathbf1_N\), where \(r\) is their minimum. Then every shifted coordinate, clique, and odd-hole inequality holds. Hence this is an inball of the claimed radius.

**3. Uniqueness and all contacts.** If the odd-hole bound is active, equality in the last displayed inequality forces \(c_i=r\) for all \(i\) and \(c_{m+j}=r\) for all \(j\), because each coefficient of every center coordinate is positive. If instead the edge-clique bound is active, every one of the \(m\) clique facets gives equality in its lower-bound chain, so every rim coordinate (each occurring in some such inequality), and every hub coordinate, must equal \(r\). In either case the incenter is unique. Since its coordinates equal \(r\), all \(N\) nonnegativity facets touch. Every lifted edge facet has the same slack and every odd-hole facet is the sole member of its orbit; their contact classification is exactly which of the two radius bounds is active.

**4. Exact phase transition.** Let
\[
F_a(t)=a\sqrt{t+2}-\sqrt{a^2t+2a+1}
=\frac{2a^2-2a-1}{a\sqrt{t+2}+\sqrt{a^2t+2a+1}}.
\]
For \(a\ge2\) its numerator is positive and its denominator increases strictly with \(t\ge1\), so \(F_a(t)\) decreases strictly. Comparing the two reciprocal radius denominators, the clique bound is active exactly when \(F_a(t)\ge1\), and the odd-hole bound is active exactly when \(F_a(t)\le1\). Solving \(F_a(t)=1\) gives \(t=a^2-2a-1\): at this value (for \(a\ge3\)) the positive quantities \(\sqrt{t+2}=a-1\) and \(\sqrt{a^2t+2a+1}=a^2-a-1\) satisfy the equation, and strict monotonicity proves uniqueness. When \(a=2\), the solution is negative, and \(F_2(t)<1\) for all \(t\ge1\). At the boundary the common reciprocal denominator is \(a(a-1)\), proving the exact tangency radius and facet counts. This completes the proof.

## Verification

A standalone checker `verify.py` builds the actual indicator vectors of all stable sets for small odd-cycle lengths, constructs the complete inequality system, verifies every asserted facet has affine dimension \(N-1\), and solves the unrestricted Euclidean Chebyshev-center linear program. It checks the analytic radius, unique candidate center, contact classifications and boundary value for 24 parameter pairs, covering both sides and the boundary. It reports `ODD_WHEEL_JOIN_INBALL_CHECKS_PASSED 24 5058 654`; these tests are finite corroboration, not a substitute for the above all-parameter proof. Dependencies appear in `requirements.txt`. Run `python verify.py`.

## Relationship to prior work

Miyazaki [1] develops the Ehrhart theory of odd-cycle stable-set polytopes and records their cycle inequality description; the complete cycle facets used here are not new. De Vries, Friedrich and Perscheid [2] study lifted odd-cycle/1-wheel inequalities and extended formulations for stable-set optimization, not the Euclidean inball of a join with an arbitrary clique. The new geometric assertion is the exact metric threshold and the complete tangency/contact classification for this two-parameter join family. The known perfect-graph inradius results do not imply it: \(G_{a,t}\) contains an induced odd hole, and so is not perfect for \(a\ge2\). Results about minimum *enclosing* spheres of wheel stable-set polytopes also do not determine inscribed-ball radii or facets. Searching does not establish unconditional historical priority.

## Limitations

This is an exact result for unweighted \(K_t\vee C_{2a+1}\) with \(a\ge2\) and \(t\ge1\) in indicator coordinates, not a theorem about arbitrary graph joins, nonchordless odd cycles, weighted Euclidean metrics, Löwner or John ellipsoids, or affine-equivalent realizations. It uses the known cycle stable-set facet description as a premise, and the novelty assessment is historical-priority provisional. No independent mathematical audit has occurred.

## References

[1] Mitsuhiro Miyazaki, *Non-Gorenstein locus and almost Gorenstein property of the Ehrhart ring of the stable set polytope of a cycle graph*, arXiv:2205.01409v1 (first public 2022-05-03), https://arxiv.org/html/2205.01409v1.

[2] Sven de Vries, Ulf Friedrich, Bernd Perscheid, *An extended formulation for the 1-wheel inequalities of the stable set polytope*, Networks, DOI:10.1002/net.21906 (first online 2019), https://onlinelibrary.wiley.com/doi/10.1002/net.21906.
