# Cyclic quotients of two-subset Kneser independence complexes are Moore-space wedges

## Finding

For every integer \(n\ge 5\) satisfying \(\gcd(n,6)=1\), let \(G_n\) be the graph whose vertices are the two-element subsets of \(\mathbb Z/n\mathbb Z\), with two vertices adjacent exactly when the corresponding subsets are disjoint. Set \(X_n=|\operatorname{Ind}(G_n)|\). Let \(C_n\) act on \(X_n\) by simultaneously adding one to each label.

The action is free, and the ordinary geometric quotient has the **complete integral homotopy type**

\[
X_n/C_n\simeq M(\mathbb Z/n\mathbb Z,1)\vee\bigvee^{(n-1)(n-5)/6}S^2.
\]

Here \(M(\mathbb Z/n\mathbb Z,1)=S^1\cup_{[n]}D^2\) is the two-dimensional Moore space with an attaching map of degree \(n\). In particular,

\[
\pi_1(X_n/C_n)\cong\mathbb Z/n\mathbb Z,\qquad
H_1(X_n/C_n;\mathbb Z)\cong\mathbb Z/n\mathbb Z,
\]
\[
H_2(X_n/C_n;\mathbb Z)\cong\mathbb Z^{(n-1)(n-5)/6},\qquad
H_i(X_n/C_n;\mathbb Z)=0\quad(i\ge3).
\]

For \(n=5\) the quotient is exactly the five-torsion Moore space; for \(n=7\) it is \(M(\mathbb Z/7\mathbb Z,1)\vee S^2\vee S^2\). Composite orders such as \(n=25\) are included.

## Assumptions and scope

The graph is the ordinary two-subset Kneser graph (in the convention of Barmak, \(KG_{2,n-4}\)); its independence faces are pairwise-intersecting collections of two-subsets. The action is by the full cyclic translation of all ground-set labels, not a rotation of the graph's vertices in an unrelated enumeration. All quotient spaces are ordinary geometric orbit spaces, not homotopy or Borel quotients. The hypothesis \(\gcd(n,6)=1\) is essential to the free-action argument: it excludes invariant edges under involutions and invariant triangles under elements of order three. No conclusion is asserted at excluded values.

All spaces are regarded as finite CW complexes. The formula is an integral *homotopy* assertion, stronger than the previously known nonequivariant sphere-wedge homotopy type and the rational homology of cyclic quotients.

## Proof

**1. The invariant star-and-triangle structure.** Write \(v_{ij}\) for the vertex representing \(\{i,j\}\). Let \(\Sigma_i\) be the full simplex on all \(v_{ij}\) with \(j\ne i\), and let \(A=\bigcup_i\Sigma_i\). A pairwise-intersecting family of edges either has a common endpoint or consists of edges among \(\{ij,ik,jk\}\) for three distinct labels: after taking \(ij\) and \(ik\), any edge avoiding \(i\) must be \(jk\), and no fourth distinct edge meets all three. Hence \(X_n\) is obtained from \(A\) by attaching exactly one two-simplex \(\tau_{ijk}\) for each three-subset, along its entire boundary in \(A\). The interiors of the exceptional triangles are pairwise disjoint outside \(A\).

The simplices \(\Sigma_i\) intersect in \(\Sigma_i\cap\Sigma_j=\{v_{ij}\}\) for \(i\ne j\); triple intersections are empty. Inside each \(\Sigma_i\), let \(b_i\) be its barycenter and \(T_i\) the tree of straight segments from \(b_i\) to all its vertices. There is an explicit permutation-equivariant strong deformation retraction \(\Sigma_i\to T_i\) fixing all the \(v_{ij}\): for barycentric coordinates \(\lambda_j\), put \(\delta=\max_j\lambda_j-\operatorname{secondmax}_j\lambda_j\). If the maximum is unique at \(v_{ij}\), map \(x\) to \((1-\delta)b_i+\delta v_{ij}\); if tied, map to \(b_i\). The maximum-gap formula is continuous across ties, fixes \(T_i\), and its straight-line homotopy stays inside the simplex. Since it fixes common vertices, these retractions glue \(C_n\)-equivariantly to a deformation retraction of \(A\) onto \(T=\bigcup_iT_i\), the once-subdivided complete graph on the ground labels.

By the homotopy gluing theorem for the triangle attachments, each \(\tau_{ijk}\) can be attached instead along the image in \(T\) of its boundary, without changing the equivariant homotopy type. Its three edges map, respectively, to the paths through \(b_i,b_j,b_k\), giving the triangular boundary \(i\to j\to k\to i\) in the unsubdivided graph. All retraction and boundary homotopies are equivariant under translations. Thus \(X_n\) is \(C_n\)-equivariantly homotopy equivalent to the full two-skeleton of the \((n-1)\)-simplex on the ground labels. (One can equivalently retain the subdivided graph and hexagonal attaching boundaries.)

**2. Freeness and the quotient two-complex.** Every nonidentity translation has order \(d\ge5\) because \(\gcd(n,6)=1\). An invariant face of the two-skeleton would have a translation-invariant set of one, two, or three vertices; this is impossible since translation acts freely on the ground labels and its orbits have length \(d\ge5\). Consequently the action on the realized two-skeleton is free. The same holds on \(X_n\): a translation-invariant face contained in a star would force a fixed common center (except for a singleton pair, which would require an involution), while a nonstar face is an exceptional triangle of three graph vertices and cannot have an orbit of length at least five. The equivariant equivalence descends to an ordinary homotopy equivalence of quotients.

Let \(n=2m+1\). The quotient of the two-skeleton has one zero-cell, \(m=(n-1)/2\) one-cells (the unoriented cyclic differences \(\pm1,\ldots,\pm m\)), and \(F=\binom n3/n=(n-1)(n-2)/6\) two-cells. The last count follows because no triangle has nontrivial translation stabilizer when \(3\nmid n\). Choose positively oriented loops \(x_d\) for differences \(1\le d\le m\), and adopt \(x_{n-d}=x_d^{-1}\) for reverse differences. An oriented triangle on labels \(0,a,b\) contributes a relator \(x_a x_{b-a}x_{-b}\), with subscripts taken modulo \(n\).

**3. Elementary elimination of all but one attaching degree.** The \(m\) triangle orbits represented by \((0,j,j+1)\), \(1\le j\le m\), are distinct: their cyclic gap triples are \((j,1,n-j-1)\), with no repetitions among this range up to cyclic permutation. For \(1\le j<m\), their relations are \(x_jx_1x_{j+1}^{-1}\). These yield \(x_j=t^j\), with \(t=x_1\), by successive legitimate generator/two-cell eliminations. The remaining selected triangle \((0,m,m+1)\) has word \(x_mx_1x_m=t^n\), because the step from \(m+1\) to zero is the positive residue \(m\).

For every other triangle, after the eliminations the attaching word is \(t^s\), where \(s\) is the sum of the uniquely chosen signed representatives of its three edge differences in \([-m,m]\). This sum is divisible by \(n\), and its absolute value is at most \(3m<2n\), hence \(s\in\{-n,0,n\}\). Sliding each remaining two-cell over the already chosen degree-\(n\) cell (with sign when appropriate) makes its attaching map nullhomotopic. The resulting CW complex is the circle with one degree-\(n\) two-cell and \(F-m\) trivially attached two-cells. Such elementary eliminations and slides are homotopy-preserving, so

\[
X_n/C_n\simeq M(\mathbb Z/n\mathbb Z,1)\vee\bigvee^{F-m}S^2,
\qquad F-m=\frac{(n-1)(n-5)}6.
\]

This also proves the fundamental group and integral homology assertions, without inferring homotopy type merely from homology.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 and no third-party dependencies. The script constructs all faces of the original independence complex and checks every translation-face orbit at \(n=5,7,11\); it independently enumerates triangle orbits, the chosen elimination orbit distinctness, signed attaching exponents, cell counts and sphere ranks for \(n=5,7,11,13,17,19,25,35\). Its final output line is \(\texttt{ALL_ROTATION_QUOTIENT_CHECKS_OK}\). For instance it finds respectively \((1,2,2)\), \((1,3,5)\), and \((1,5,15)\) quotient cells at \(n=5,7,11\), giving the claimed sphere ranks \(0,2,10\).

These finite computations corroborate the arguments; the unrestricted theorem follows from the explicit star-and-triangle description, free-action reasoning and relator-elimination proof.

## Relationship to prior work

Barmak (arXiv:1007.0418v1, §4.6, Theorem 4.11) proved the **nonequivariant** wedge-of-\(\binom{n-1}{3}\) two-spheres description for the same independence complexes. This and the elementary classification of their maximal faces are used, not claimed as discoveries. Feng and Nukala (arXiv:2302.14664, §4 and Corollary 11) give a broader nonequivariant Vietoris–Rips sphere-wedge classification; the constant-weight two-subset complex at scale two is precisely \(X_n\). Neither determines this geometric cyclic orbit space.

Two separately available studies, *The integral symmetric-group homology lattice of two-subset Kneser independence complexes* (published mathematical record dated 2026-11-02) and *The integral symmetric-group homology module of two-subset Kneser independence complexes* (published mathematical record dated 2026-11-02), provide the complete integral top-homology permutation module. The first also computes the cyclic orbit space's **rational** second Betti number, \((n-1)(n-5)/6\) when \(3\nmid n\), agreeing with the free sphere rank here. The other constructs an equivariant star-to-graph retraction. Their actual stated results do not establish the **integral** quotient homotopy decomposition or its torsion fundamental group. The present result supplies those missing orbit-space invariants, but does not claim new nonequivariant homology or a new integral covering-space representation.

## Limitations

Only widths \(n\ge5\) coprime to six are classified; at widths divisible by two or three, nontrivial stabilizers require separate orbit-space analysis. The homotopy equivalence is not asserted to respect additional dihedral or symmetric-group actions after taking this quotient. No claimed consequence concerns the Kneser graphs on larger underlying subset sizes. Exhaustive finite checks do not establish the all-width theorem. An equivalent unindexed or inaccessible published quotient calculation could affect originality; no external independent scholarly validation has been performed.

## References

1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first public version 2010-07-02, §4.6, Theorem 4.11. https://arxiv.org/html/1007.0418v1
2. Z. Feng and N. C. P. Nukala, *On Vietoris-Rips complexes of finite metric spaces with scale 2*, arXiv:2302.14664, first public version 2023-02-28, §4 and Corollary 11. https://arxiv.org/html/2302.14664v3
3. *The integral symmetric-group homology lattice of two-subset Kneser independence complexes*, published mathematical record 2026-11-02: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-integral-symmetric-group-homology-lattice-of-two-subset-knes--75ac6f142af1
4. *The integral symmetric-group homology module of two-subset Kneser independence complexes*, published mathematical record 2026-11-02: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-integral-symmetric-group-homology-module-of-two-subset-knese--0727b76827f5
