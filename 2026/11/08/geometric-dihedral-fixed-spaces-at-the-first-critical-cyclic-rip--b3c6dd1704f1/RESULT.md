# Geometric dihedral fixed spaces at the first critical cyclic Rips scale

## Finding
For every integer \(r\ge2\), put \(n=3r\), give \(\mathbb Z/n\) the shortest cyclic graph distance \(d(i,j)=\min\{(i-j)\bmod n,(j-i)\bmod n\}\), and let \(X_r=\operatorname{VR}_{\le r}(\mathbb Z/n)\) be its flag complex: a nonempty vertex set is a simplex if every pair has distance at most \(r\). The dihedral group \(D_n\) acts by \(t_k(i)=i+k\) and \(s_a(i)=a-i\), with indices modulo \(n\). Its **geometric fixed-point spaces** have the following complete classification for individual dihedral elements:

* The identity fixes \(|X_r|\simeq\bigvee^{r-1}S^2\) (known from the ordinary cyclic-power classification).
* A nonidentity rotation of order three fixes exactly \(r\) isolated points. Every other nonidentity rotation fixes the empty space.
* If \(r\) is odd, every reflection fixes a contractible space.
* If \(r\) is even, each reflection through two opposite cycle vertices (\(a\) even) fixes a space of type \(S^1\), whereas each reflection through two opposite cycle edges (\(a\) odd) fixes a space of type \(S^0\).

In particular, the full rational character on the unique nonzero reduced homology module \(\widetilde H_2(X_r;\mathbb Q)\) has value \(r-1\) at the identity and at either nonidentity order-three rotation, value \(-1\) at every other nonidentity rotation, value \(0\) at reflections if \(r\) is odd, and values \(-1\) (vertex-axis) and \(+1\) (edge-axis) at reflections if \(r\) is even.

## Assumptions and scope
All graphs and simplicial complexes are finite. Fixed points are taken **in the geometric realization**, allowing points in the interiors of setwise-invariant simplices. The convention is inclusive distance \(\le r\). The parameter range is all integers \(r\ge2\) and only the first critical family \(n=3r\). The classification is for fixed spaces of individual group elements, not an assertion about the entire equivariant homotopy type or fixed sets of arbitrary subgroups.

## Proof
**Orbit-barycenter lemma.** Let an automorphism \(g\) act on a finite flag complex \(K\). Partition its original vertices into orbits. Each orbit \(O\) spanning a simplex yields a vertex at the barycenter of \(O\) in \(|K|^{\langle g\rangle}\). A collection of such orbit barycenters spans a simplex precisely when the union of its orbits spans a simplex in \(K\). Indeed, a point of \(|K|\) is fixed exactly when its barycentric coefficients are constant along orbits. Normalizing each orbit-sum gives a linear homeomorphism between this new complex and the geometric fixed set. Since \(K\) is flag, the new complex is the clique complex of the **orbit-compatibility graph** whose vertices are individually admissible orbits and whose edges represent admissible orbit unions.

**Rotations.** A nontrivial translation \(t_k\) has orbits of size \(L=n/\gcd(n,k)\), equally spaced around the \(n\)-cycle. For \(L=2\), antipodal orbit vertices have distance \(n/2>r\). For \(L\ge4\), two vertices within such an orbit have distance at least \(\lfloor L/2\rfloor n/L>n/3=r\); hence no orbit is admissible and the fixed set is empty. The only possibility is \(L=3\), equivalent to \(k=r\) or \(k=2r\). The \(r\) admissible orbits are \(T_i=\{i,i+r,i+2r\}\), for \(0\le i<r\). Two different triples cannot coexist in a simplex: for \(0\le i<j<r\) the pair \(i,j+r\) has cyclic distance \(r+j-i>r\) (or equivalently one of the two cross-offset orientations does). Hence the fixed complex is exactly \(r\) isolated vertices.

**Reflections, even \(r=2h\).** With \(n=6h\), every reflection is conjugate to \(s_0\) or \(s_1\) according as its axis passes through vertices or through edge midpoints. For \(s_0\), all admissible orbits are
\[A_i=\{i,-i\},\quad B_j=\{3h-j,3h+j\},\qquad 0\le i,j\le h,\]
with repeated endpoints interpreted as singletons and coordinates modulo \(6h\). Both orbit sets \(\{A_0,\ldots,A_h\}\) and \(\{B_0,\ldots,B_h\}\) form cliques because every within-family distance is at most \(2h\). A cross-edge requires, already from the pair \(i\in A_i\), \(3h+j\in B_j\), that \(3h-|i-j|\le2h\); thus \(|i-j|\ge h\). The only possibilities are \((i,j)=(0,h)\) and \((h,0)\), and both do satisfy every cross-pair distance bound. Consequently the flag quotient is two disjoint simplices connected by two edges with distinct endpoints and no additional cross-faces. Contracting each simplex gives a cycle, so the fixed space is \(S^1\).

For \(s_1\), the admissible orbits are
\[A_i=\{-i,1+i\},\quad B_j=\{3h-j,3h+1+j\},\qquad 0\le i,j<h.\]
Each family is a clique. There is no cross-edge: for a proposed pair \(A_i,B_j\), the elements \(1+i\) and \(3h+1+j\) have cyclic distance \(3h-|i-j|\ge2h+1>r\). Thus the fixed complex is a disjoint union of two nonempty simplices, of homotopy type \(S^0\).

**Reflections, odd \(r=2h+1\).** Here \(n=6h+3\), all reflections are conjugate, and it suffices to take \(s_0\). Its admissible orbits are
\[A_i=\{i,-i\},\quad B_j=\{3h+1-j,3h+2+j\},\qquad 0\le i,j\le h.\]
Each family is a clique. For \(i\ge1\), the elements \(i\in A_i\) and \(3h+2+j\in B_j\) have cyclic distance at least \(2h+2>r\), so they cannot form a cross-edge. For \(i=0\), compatibility with \(B_j\) holds exactly when \(j=h\). The orbit graph is therefore two cliques joined by one edge. Its clique complex is contractible. This proves all geometric fixed-point types.

**Homology character.** The ordinary equivalence \(X_r\simeq\bigvee^{r-1}S^2\) is a previously established theorem about clique complexes of powers of cycles; it is not part of the novelty claim. Since a finite-order simplicial automorphism has Lefschetz number equal to the Euler characteristic of its geometric fixed set (using a barycentric subdivision), and the only ordinary rational homology degrees are \(0\) and \(2\), we have \(\operatorname{tr}(g\mid\widetilde H_2)=\chi(|X_r|^g)-1\). Substitution of the complete fixed-space classification gives the asserted character. No statement about integral equivariant representation splitting is inferred.

## Verification
The standalone file `verify_dihedral_critical_rips.py` constructs the original distance graph independently for every critical parameter \(2\le r\le24\), every nonidentity rotation and every reflection. It enumerates admissible complete orbits, compares exact orbit-compatibility graphs with the structural proof (all reflections, not only representatives), and computes reduced mod-two homology of each representative reflection graph for \(2\le r\le12\). Execute `python3 verify_dihedral_critical_rips.py`. The corresponding recorded output is `verify_dihedral_critical_rips.out`. Finite enumerations are corroboration, not an infinite proof. The graph-identification argument above supplies the unrestricted result.

## Relationship to prior work
Adamaszek's 2011 preprint, *Clique complexes and graph powers* (arXiv:1104.0433, §6), determines the ordinary homotopy type of the clique complexes of cycle powers, including the \(n=3r\) sphere wedge. Jaemin Park's October 19, 2026 preprint, *Homotopy distributions for Vietoris-Rips complexes of random circle samples* (arXiv:2610.26366, §§1–2), studies critical circle Rips homotopy distributions. Those results concern nonequivariant homotopy types and random orbit counts, not geometric dihedral fixed spaces. The present result does not reprove or rebrand the nonequivariant classification. For the stable scale-two regime \(n\ge7\), fixed-point conclusions are already known; this statement instead concerns the distinct critical boundary \(n=3r\), uniformly for every scale \(r\ge2\), with the new loop-versus-disconnected reflection dichotomy and full critical character.

## Limitations
This is a geometric fixed-space classification for individual elements of \(D_{3r}\) only. It does not classify all subgroup fixed intersections, coherent equivariant attaching maps, noncritical scales, or the integral module structure. The proof assumes the inclusive graph metric (rather than a strict inequality at the critical diameter).

## References
- J. Park, *Homotopy distributions for Vietoris-Rips complexes of random circle samples*, arXiv:2610.26366, first posted October 19, 2026, particularly §§1–2.
- M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (2011), particularly §6 and Corollary 6.7.
