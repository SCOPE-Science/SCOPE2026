# Finite-arity saturation and the first hidden-nesting collision of ultrametric type counts

## Finding
Fix an integer \(h\ge2\). Let \(\mathbb U_h\) be the countable homogeneous universal ultrametric space with positive distances \(\{1,\ldots,h\}\), in the finite relational language recording each distance. Let \(A\subset\mathbb U_h\) be a nonempty, finite, individually named parameter set. For \(1\le j\le h\), denote by \(c_j(A)\) the number of equivalence classes on \(A\) of \(d(a,b)\le j\). In particular \(c_h(A)=1\). Write \(t_m(A)\) for the number of complete types of ordered, pairwise-distinct \(m\) new points over \(A\), all distinct from the parameters, and put \(t_0(A)=1\).

Define formal exponential series recursively by
\[
U_0(z)=1+z,\qquad U_{j+1}(z)=\exp(U_j(z)-1)\quad(j\ge0).
\]
Then, for every \(m\ge0\),
\[
\boxed{\sum_{m\ge0}t_m(A)\frac{z^m}{m!}=\prod_{j=1}^{h}U_j(z)^{c_j(A)}.}\tag{1}
\]
Moreover, for any two nonempty finite bases \(A,B\) in the same \(\mathbb U_h\), the following are equivalent:
\[
\bigl(t_m(A)=t_m(B)\text{ for }1\le m\le h-1\bigr),\quad
\bigl(t_m(A)=t_m(B)\text{ for every }m\ge0\bigr),\quad
\bigl(c_j(A)=c_j(B)\text{ for every }j\bigr).\tag{2}
\]
Thus the complete numerical all-arity injective type spectrum saturates already at arity \(h-1\).

At \(h=3\), even supplementing the complete spectrum by the *multisets of sizes of all old balls at each level* does not reconstruct the base. The first such collision occurs on **five old points**, and there is exactly **one unordered nonisometric pair** at that order with the same levelwise ball-size multisets. For both witnesses, \((c_1,c_2,c_3)=(4,2,1)\), and
\[
(t_1,t_2,t_3,t_4,t_5,t_6)=(7,53,434,3838,36566,374207).
\]

## Assumptions and scope
A finite ultrametric has \(d(a,a)=0\), positive distances in \(\{1,\ldots,h\}\), and \(d(x,z)\le\max(d(x,y),d(y,z))\). A complete type is counted with the old parameters fixed pointwise and the new coordinate positions labeled. By universality and ultrahomogeneity, complete types of injective new tuples are exactly admissible finite ultrametric extensions; this is not a count of realizations or of types allowing repeated new coordinates. The language has one binary relation for each positive distance.

For the five-point witnesses, label the old points \(0,1,2,3,4\). Both have distance-\(1\) classes
\[
\{0,1\},\quad\{2\},\quad\{3\},\quad\{4\}.
\]
Base \(A\) has distance-at-most-\(2\) classes \(\{0,1,2\},\{3,4\}\), while base \(B\) has \(\{0,1\},\{2,3,4\}\). Distances are uniquely determined by these partitions: the least level at which two old points share a class. Their old distance-\(1\) ball-size multisets are both \(\{2,1,1,1\}\), their distance-at-most-\(2\) ball-size multisets are both \(\{3,2\}\), and the root ball has size \(5\). They are not isometric: the unique two-point distance-\(1\) class belongs to a three-point distance-at-most-\(2\) class in \(A\), but to a two-point class in \(B\).

## Proof
**Singleton attachment slots.** Fix a new point \(x\) and take \(j=\min_{a\in A}d(x,a)\). For a closest \(a\), its \(d\le j\) class \(C\) is precisely the set of old points at distance \(j\) from \(x\). Every old point \(b\notin C\) is at distance \(d(a,b)>j\) from \(x\). Conversely, for every level \(j\) and every old \(d\le j\) class \(C\), these prescriptions give a consistent new-point extension. Thus the singleton types are exactly the \(c_j\) slots \((j,C)\), for all levels \(j\).

**Independent groups of new coordinates.** If two new points have distinct singleton slots, there is some old parameter at unequal distances from them; the ultrametric inequality then forces their mutual distance to be the larger of those two distances. These forced distances are jointly consistent by the standard ball-tree construction (place a new branch at the specified level in each old ball). For several new points occupying one slot \((j,C)\), their internal metric can be *any* ultrametric with positive distances in \(\{1,\ldots,j\}\); all these internal distances are at most the distances to other slots, so the blocks glue consistently. Consequently the new labeled coordinates split into disjoint subsets indexed by the old singleton slots, with independent level-\(j\) ultrametrics within each subset.

Let \(u_j(m)\) be the number of ultrametrics with distances in \(\{1,\ldots,j\}\) on \(m\) labeled points, including \(u_j(0)=1\). At level \(0\), the empty set and singleton are the only possibilities, giving \(U_0=1+z\). At level \(j+1\), the relation \(d\le j\) partitions the points into blocks, each of which carries a level-\(j\) ultrametric. The exponential formula gives \(U_{j+1}=\exp(U_j-1)\). Allocating disjoint labeled subsets to all singleton slots proves equation (1).

**Finite-arity inversion.** Put \(p_m(k)=u_k(m)\), for integer \(k\ge0\). For each fixed \(m\ge1\), \(p_m(k)\) extends to a polynomial of degree exactly \(m-1\), with positive leading coefficient. This is immediate for \(m=1\), when \(p_1=1\). Inductively, the set-partition recurrence
\[
u_{k+1}(m)-u_k(m)=\sum_{\substack{\pi\text{ partition of }[m]\\|\pi|\ge2}}\prod_{D\in\pi}u_k(|D|)
\]
has a polynomial right-hand side of degree exactly \(m-2\): the terms with two blocks have positive top-degree coefficients, while partitions with more blocks have smaller degree. Discrete summation over \(k\), together with \(u_0(m)=0\) for \(m\ge2\), proves the assertion.

Taking logarithms in (1), using \(\log U_j=U_{j-1}-1\), yields
\[
m![z^m]\log\!\left(\sum_{q\ge0}t_q(A)\frac{z^q}{q!}\right)
=\sum_{j=1}^h c_j(A)p_m(j-1).\tag{3}
\]
The coefficient on the left depends only on \(t_1,\ldots,t_m\). Since \(c_h=1\), the first \(h-1\) equations for \(m=1,\ldots,h-1\) determine the other \(h-1\) cluster counts uniquely: the matrix \((p_m(j-1))_{1\le m,j\le h-1}\) is nonsingular because \(p_1,\ldots,p_{h-1}\) have successive degrees \(0,\ldots,h-2\), and evaluation at \(0,\ldots,h-2\) is invertible. Equation (1) proves the converse, completing (2).

**First collision with ball-size data.** At \(h=3\), isometry classes of nonempty finite old bases correspond exactly to two nested partitions: their \(d\le1\) blocks, grouped into \(d\le2\) blocks. An isometry-invariant canonical code is the multiset, over upper blocks, of the multiset of lower-block sizes in each upper block. Enumerating every set partition of \(n\) labeled points and every partition of its blocks exhausts all such classes. Comparing the canonical codes while retaining only the two levelwise multisets of old ball sizes gives zero collisions for \(1\le n\le4\), and exactly one pair for \(n=5\), as specified above. The standalone checker performs this finite exhaustive enumeration (the \(n=5\) case has 358 labeled nested partitions and 27 isometry types).

## Verification
Run \(`python3 check.py`\) using only the Python standard library. The program enumerates all nested partitions for old base sizes \(1\) through \(5\), checks the sharp pair classification using canonical isometry codes, independently brute-forces all ultrametric new-coordinate extensions of both five-point witnesses through new-arity \(4\), recomputes the formal-series coefficients through arity \(6\), and checks nonsingularity of the inversion matrices for heights \(2\) through \(7\). Its deterministic output is included as \(`check_output.txt`\).

The independent brute counts at new-arities \(1,2,3,4\) are \(7,53,434,3838\) for each witness. The algebraic proofs establish the general arity formula and inversion at every finite height; finite computations are not used as proofs for unlimited heights or arities.

## Relationship to prior work
The universal finite-alphabet ultrametric Fraïssé structure and its ball-tree representation are established background; Nguyen Van Thé (2007) studies finite ultrametric tree encodings, Ramsey degrees, and corresponding Urysohn spaces, not this pointed all-arity enumeration. Delhomme, Laflamme, Pouzet, and Sauer (2015, later revised) establish homogeneity and the arity-two characterization of isometries, and analyze the nerve/ball tree; the higher-arity *numerical profile factorization*, finite-arity coefficient inversion, and sharp five-point collision with preserved ball-size multisets do not follow as stated computations from their structural conclusions. Standard species/set-partition exponential formulas provide the counting tool and are not claimed as new.

The result concerns **nested** equivalence relations from ultrametric balls. Parallel published orbit-profile results for independent or ordered equivalences, and calculations of compatibility matrices for ultrametric singleton types, have different invariants and do not establish equations (1)--(3) or the five-point classification. Unindexed equivalent enumerations remain a historical-priority risk.

## Limitations
The ambient distance alphabet is finite and fixed, \(A\) must be nonempty, and all counted new coordinates are pairwise distinct and distinct from the old parameters. No reconstruction of the full old metric is claimed from these numerical counts; indeed the witness shows failure even with levelwise old ball sizes. The theorem does not assert that the complete *labeled type space*, its adjacency relations, or old-parameter relations are identical for the two bases. The only finite exhaustive first-collision assertion concerns height three and bases of at most five old points. Independent mathematical audit and a definitive historical-priority assessment have not been performed.

## References
- L. Nguyen Van Thé, *Ramsey degrees of finite ultrametric spaces, ultrametric Urysohn spaces and dynamics of their isometry groups*, arXiv:0710.2347v1 (first publicly submitted 2007-10-11), sections 2 and 5. https://arxiv.org/html/0710.2347v1
- C. Delhomme, C. Laflamme, M. Pouzet, N. Sauer, *On homogeneous ultrametric spaces*, arXiv:1509.04346v1 (first publicly submitted 2015-09-14), especially introduction, ball-tree definitions and homogeneity construction; also inspected later version. https://arxiv.org/pdf/1509.04346
