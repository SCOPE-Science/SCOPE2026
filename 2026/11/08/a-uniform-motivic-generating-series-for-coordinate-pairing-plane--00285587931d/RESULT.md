# A uniform motivic generating series for coordinate-pairing planes on Fermat cubics

## Finding

For each integer \(m\ge1\), over any field \(k\) of characteristic different from \(2\) and \(3\), let
\[
X_m:\quad \sum_{i=1}^{2m}x_i^3=0\quad\subset\mathbb P_k^{2m-1}
\]
be the smooth Fermat cubic hypersurface. For every perfect matching \(M\) of the \(2m\) coordinate indices, form the linear subspace \(\Pi_M\cong\mathbb P_k^{m-1}\) given by \(x_i+x_j=0\) for every pair \(\{i,j\}\in M\). Let \(U_m\subset X_m\) be the **reduced union** of precisely these \((2m-1)!!\) designated subspaces, not the union of all linear spaces on \(X_m\). Write \(\mathbb L=[\mathbb A^1_k]\in K_0(\operatorname{Var}_k)\).

Set \(\Phi(t)=\sum_{j\ge0}t^{2j}/(j!)^2\). Define polynomials \(P_m(z)\in\mathbb Z[z]\) by the formal identity
\[
\boxed{\sum_{m\ge1}P_m(z)\frac{t^{2m}}{(2m)!}
 = \frac{\cosh t}{z-1}\left(\Phi(t)^{(z-1)/2}-1\right).}
\]
The apparent division by \(z-1\) is removable coefficient by coefficient. Then **for every such field \(k\) and every \(m\ge1\)**,
\[
\boxed{[U_m]=P_m(\mathbb L)\quad\text{in }K_0(\operatorname{Var}_k).}
\]
In particular, for every finite field \(\mathbb F_q\) of characteristic at least \(5\) and every \(r\ge1\),
\[
\#U_m(\mathbb F_{q^r})=P_m(q^r),\qquad
Z(U_m,T)=\prod_{j=0}^{m-1}(1-q^jT)^{-c_{m,j}},
\]
where \(P_m(z)=\sum_{j=0}^{m-1}c_{m,j}z^j\).

The first values, illustrating the nontrivial inclusion-exclusion cancellations, are
\[
P_1(z)=1,\qquad P_2(z)=3z,\qquad
P_3(z)=15z^2-30z+25,
\]
\[
P_4(z)=105z^3-525z^2+1120z-917.
\]
Thus the union of the \(15\) standard coordinate-pairing planes on the Fermat cubic fourfold satisfies
\[
\#U_3(\mathbb F_q)=15q^2-30q+25,\qquad
Z(U_3,T)=\frac{(1-qT)^{30}}{(1-T)^{25}(1-q^2T)^{15}}.
\]
Its rational point multiplicity distribution across the \(15\) planes is \(15(q-2)(q-3)\), \(45(q-2)\), \(15\), and \(10\) points lying on exactly \(1,2,3,6\) designated planes, respectively. These last incidence data are examples of the all-dimensional class formula, not a claim of new discovery of the classical Segre configuration.

## Assumptions and scope

All perfect matchings are on a fixed labeled set of \(2m\) indices; each pair contributes one equation \(x_i+x_j=0\). The reduced union is taken inside projective space. Over characteristic different from \(3\), \(X_m\) is smooth because the cubic partial derivatives cannot all vanish projectively. Characteristic \(2\) is excluded because sign-balanced coordinates and the intersection graph's bipartiteness rule degenerate. No assertion is made that these designated spaces exhaust the geometric linear spaces on \(X_m\); this matters in higher dimensions. The Grothendieck-ring identity is an identity of variety classes, not a determination of individual cohomology groups.

## Proof

**Linear spaces and intersection poset.** Each \(\Pi_M\) lies in \(X_m\), since paired coordinates contribute \(a^3+(-a)^3=0\). Fix any nonempty subset \(S\) of matchings. Make the graph \(G_S\) on \(2m\) vertices whose edges are the pairs in the selected matchings. In the simultaneous linear equations, a connected bipartite component contributes one free scalar: fixing a bipartition forces the coordinates to alternate between that scalar and its negative. A non-bipartite component contains an odd cycle and therefore forces its coordinates to zero, since \(2\) is invertible. If \(b(S)\) is the number of bipartite connected components, the projective intersection is \(\mathbb P_k^{b(S)-1}\) if \(b(S)>0\), and empty otherwise. Consequently inclusion-exclusion gives
\[
[U_m]=Q_m(\mathbb L),\quad
Q_m(z)=\sum_{\varnothing\ne S\subseteq\mathcal M_m}(-1)^{|S|+1}
\sum_{j=0}^{b(S)-1}z^j\in\mathbb Z[z],
\]
where an inner sum with upper limit \(-1\) means zero. Crucially, \(Q_m\) is independent of \(k\) as long as its characteristic is not two.

**Exact rational-point count.** Fix an odd finite field \(\mathbb F_q\), and put \(R=(q-1)/2\). A nonzero vector \(v\in\mathbb F_q^{2m}\) represents a point of \(U_m\) precisely when (i) its number of zero coordinates is even and (ii) for each unordered pair of opposite nonzero field values \(\{a,-a\}\), the values \(a\) and \(-a\) appear equally often. Necessity follows from the pairing equations; conversely, matching each value with its opposite and pairing the zero coordinates constructs a suitable matching. For an antipodal value-pair used \(j\) times on each side, the exponential generating weight is \(t^{2j}/(j!)^2\). For \(2s\) zeros it is \(t^{2s}/(2s)!\). Multiplying these independent choices gives exactly
\[
(2m)![t^{2m}]\cosh(t)\Phi(t)^R
\]
**vectors**, including the all-zero vector once. The \(q-1\) nonzero scalar representatives of each projective point therefore give
\[
\#U_m(\mathbb F_q)=\frac{(2m)![t^{2m}]\cosh(t)\Phi(t)^{(q-1)/2}-1}{q-1}=P_m(q).
\]
Here \(\Phi(t)^{(z-1)/2}\) is defined formally by its binomial expansion about \(\Phi(0)=1\). At fixed \(t\)-degree \(2m\), the numerator is a polynomial in \(z\) of degree at most \(m\); at \(z=1\), the coefficient becomes \((2m)![t^{2m}]\cosh(t)-1=0\). Hence the quotient is polynomial of degree at most \(m-1\) over \(\mathbb Q\).

**From point counts to motives.** Evaluating the inclusion-exclusion polynomial \(Q_m\) over every odd finite field gives \(Q_m(q)=\#U_m(\mathbb F_q)=P_m(q)\). This holds for infinitely many distinct prime powers of characteristic at least \(5\), so polynomial identity forces \(Q_m(z)=P_m(z)\). In particular, every coefficient of \(P_m\) is an integer and \([U_m]=P_m(\mathbb L)\) over every allowed field, not just finite fields.

**Zeta function.** Apply the point-count formula to every extension \(\mathbb F_{q^r}\). Then, by the definition of the Hasse--Weil zeta function,
\[
\log Z(U_m,T)=\sum_{r\ge1}P_m(q^r)\frac{T^r}{r}
=-\sum_{j=0}^{m-1}c_{m,j}\log(1-q^jT),
\]
proving the product formula.

**The six-coordinate multiplicities.** For the cubic fourfold, the number of matchings compatible with a vector with \(2s\) zeros and multiplicity \(e_a\) of each opposite value-pair is \((2s-1)!!\prod_a e_a!\) (with \((-1)!!=1\)). Partitioning the six coordinate positions by the possible zero counts \(0,2,4\) and opposite-value multiplicities gives the four stated strata \(1,2,3,6\). The displayed formulas follow from elementary multinomial choices and division by the scalar group of size \(q-1\).

## Verification

The self-contained Python files `verify_family.py`, `verify_intersections.py`, `verify_planes.py`, and `verify_combinatorics.py` require only the standard library. `verify_family.py` directly enumerates all designated spaces for \(m=1,2,3,4\) over prime fields of cardinalities \(3,5,7\), independently computes the binomial-series coefficient, and compares the first four polynomials. `verify_intersections.py` enumerates all \(2^{15}-1\) nonempty subsets of the \(15\) six-coordinate matchings and reconstructs the integral motivic class \(15\mathbb L^2-30\mathbb L+25\) through bipartite graph components. `verify_planes.py` enumerates six-coordinate projective points independently by sweeping the fifteen planes for \(q=5,7,11,13\); `verify_combinatorics.py` independently enumerates all projective vectors over \(q=5,7\). All four completed with `PASS`. The infinite-dimensional statement is proved symbolically above; no finite experiment is presented as a proof for all \(m\).

## Relationship to prior work

The existence of coordinate-pairing planes on Fermat cubic hypersurfaces is classical. Degtyarev--Itenberg--Ottem, *Planes in cubic fourfolds*, §2.5 (first public May 28, 2021), explicitly describes \(405\) planes over \(\mathbb C\), including the \(15\) sign-pairing planes used at \(m=3\); it also studies the lattice of plane classes. Their description is acknowledged and is not claimed as new. The \(15\)-plane configuration is also visible on the classical Segre cubic primal. Debarre--Laface--Roulleau analyze finite-field rational lines, Fano varieties, and zeta functions of cubic hypersurfaces; those are distinct from the Grothendieck classes of the specified unions across arbitrary \(m\). The contribution here is the uniform exact motivic generating series in \(m\), with its simultaneously determined field-uniform point counts and zeta functions; a proof or explicit formula of this strength was not located in the examined sources.

## Limitations

The formulas concern only the labeled coordinate-pairing subarrangement; other maximal linear spaces may exist, and counts here do not measure the union of **all** such spaces. The theorem does not determine the cohomology groups or singularity schemes of the unions. Although no prior equivalent all-dimensional generating series was found, a classical combinatorial reformulation not indexed in the inspected literature remains a historical-priority risk. The characteristic-two analogue requires a different incidence analysis; characteristic three is excluded to retain smooth ambient Fermat cubics.

## References

1. A. Degtyarev, I. Itenberg, J. C. Ottem, *Planes in cubic fourfolds*, arXiv:2105.13951 (first public May 28, 2021), *Algebraic Geometry* 10 (2023), 228--258, DOI:10.14231/AG-2023-007, §2.5.
2. O. Debarre, A. Laface, X. Roulleau, *Lines on cubic hypersurfaces over finite fields*, arXiv:1510.05803 (2015), especially the introduction and discussion of finite-field Fano-variety zeta functions.
3. Classical Segre cubic primal configuration of fifteen planes, ten nodes and forty-five distinguished lines; see the treatment in the literature on Segre cubic geometry. The classical configuration is acknowledged, not asserted to be new.
