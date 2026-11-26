# Sharp codimension-five ideal-orbit splitting in free two-step nilpotent Lie algebras

## Finding
Let \(K=\mathbb F_q\) be any finite field and \(d\ge5\). Define \(V=K^d\), \(Z=\bigwedge^2 V\), and the free class-two Lie algebra \(L=V\oplus Z\) by \([v+z,w+z']=v\wedge w\). An **ideal** is a \(K\)-linear Lie ideal. The full group of \(K\)-linear Lie automorphisms acts on these ideals.

For an ideal \(I\), define \(U=(I+Z)/Z\subseteq L/Z\cong V\), \(W=I\cap Z\), and the intrinsic defect pair
\[
k=\operatorname{codim}_V U,\qquad \delta=\operatorname{codim}_Z W.
\]
The pair is admissible precisely when \(0\le k\le d\) and \(0\le\delta\le\binom{k}{2}\). Every such ideal has codimension \(k+\delta\). For every admissible pair, the exact number of embedded ideals is
\[
\boxed{\ N_{d,q}(k,\delta)={d\brack k}_q\,{\binom{k}{2}\brack\delta}_q\,q^{(d-k)\delta}\ },
\]
where \({a\brack b}_q\) denotes the Gaussian binomial coefficient. Consequently the full ideal-codimension polynomial is
\[
\sum_{I\triangleleft L}t^{\operatorname{codim}I}
=\sum_{k=0}^d\sum_{\delta=0}^{\binom{k}{2}}
{d\brack k}_q{\binom{k}{2}\brack\delta}_q q^{(d-k)\delta}t^{k+\delta}.
\]

**Sharp orbit threshold.** At codimension at most four, every admissible \((k,\delta)\)-stratum is a single \(\operatorname{Aut}(L)\)-orbit. At codimension five, the \((4,1)\)-stratum splits into exactly two orbits, distinguished by rank \(2\) or \(4\) of a nonzero alternating form on a four-dimensional quotient. The respective numbers of ideals in these orbits are
\[
\boxed{{d\brack4}_q q^{d-4}{4\brack2}_q},\qquad
\boxed{{d\brack4}_q q^{d-4}\bigl({6\brack1}_q-{4\brack2}_q\bigr)}.
\]
The remaining codimension-five profiles are \((5,0)\) and \((3,2)\); each is a single orbit, of sizes
\[
\boxed{{d\brack5}_q},\qquad
\boxed{{d\brack3}_q q^{2(d-3)}{3\brack1}_q}.
\]
Hence there are **exactly four** automorphism orbits of codimension-five ideals for every \(d\ge5\) and every prime power \(q\). This is the first *within-profile* splitting: the total number of orbits across all profiles of codimensions \(0,1,2,3,4,5\) is \(1,1,1,2,2,4\).

## Assumptions and scope
The bracket is alternating in all characteristics, including two. Subspaces and automorphisms are \(K\)-linear. The automorphism group is the entire group \(\operatorname{Aut}_K(L)\), including central shears, not just a chosen degree-preserving subgroup. Codimension is taken in \(L\), and \(\delta\) is taken in the full derived space \(Z\), not in the quotient exterior square. The result concerns **embedded ideals**, not abstract isomorphism types of quotient Lie algebras. No assumption that the ideal is homogeneous or contained in the center is imposed.

## Proof
**1. Ideal coordinates.** Since \([L,L]=Z\) and \([v+z,w+z']=v\wedge w\), a subspace \(I\) with projection \(U\subseteq V\) and central intersection \(W\subseteq Z\) is an ideal if and only if \(U\wedge V\subseteq W\). The exterior-product quotient is naturally
\[
Z/(U\wedge V)\cong\bigwedge^2(V/U),
\]
of dimension \(\binom{k}{2}\), where \(k=\dim(V/U)\). Thus, after choosing \(U\), an admissible \(W\) is exactly the inverse image of a codimension-\(\delta\) subspace \(W'\) of \(\bigwedge^2(V/U)\). Given \(U,W\), the ideals realizing them are precisely inverse graphs of linear maps \(U\to Z/W\), one map per ideal. There are \(q^{(d-k)\delta}\) such maps. Choosing \(U\) and \(W'\) gives the asserted Gaussian count. The exact sequence \(0\to W\to I\to U\to0\) gives \(\dim(L/I)=k+\delta\).

**2. Full automorphisms and orbit reduction.** Every map \(v\mapsto gv+s(v)\), with \(g\in\operatorname{GL}(V)\) and \(s\in\operatorname{Hom}(V,Z)\), extends uniquely to a Lie automorphism, acting by \(\bigwedge^2g\) on \(Z\); conversely every automorphism has this form because \(Z=[L,L]\) is characteristic and the bracket determines the action on it. Thus
\[
\operatorname{Aut}(L)=\operatorname{Hom}(V,Z)\rtimes\operatorname{GL}(V).
\]
For any fixed \((U,W)\), central shears act transitively on the graph maps: extend the difference of two maps \(U\to Z/W\) linearly to \(V\to Z\). The stabilizer of \(U\) inside \(\operatorname{GL}(V)\) surjects onto \(\operatorname{GL}(V/U)\). Consequently the full-automorphism orbits with defects \((k,\delta)\) are in bijection with \(\operatorname{GL}_k(K)\)-orbits on codimension-\(\delta\) subspaces of \(\bigwedge^2K^k\).

**3. The low-codimension boundary.** For \(k\le2\), \(\dim\bigwedge^2K^k\le1\), so each possible \(\delta\)-stratum has one orbit. For \(k=3\), \(\bigwedge^2K^3\) is (up to determinant twist) dual to the natural three-dimensional \(\operatorname{GL}_3(K)\)-module. Hence \(\operatorname{GL}_3(K)\) is transitive on subspaces of each dimension. If \(k\ge4\) and \(k+\delta\le4\), then \(\delta=0\), which again gives one orbit. Therefore no admissible fixed-defect stratum of codimension below five splits. At codimension five the only possibilities are \((k,\delta)=(3,2),(4,1),(5,0)\). The first and last are transitive by the preceding arguments.

**4. Two inequivalent hyperplane orbits.** For \((k,\delta)=(4,1)\), \(W'\) is a hyperplane of the six-dimensional space \(\bigwedge^2K^4\). Its annihilator \((W')^\perp\subseteq(\bigwedge^2K^4)^*\) is a projective line, spanned by a nonzero alternating bilinear form \(\beta\) on \(K^4\). Every nonzero alternating form in dimension four has rank two or four (also in characteristic two); change of basis is transitive separately on each rank by alternating-form normal form. Rank two occurs exactly when \(\beta\) is decomposable, and those projective classes correspond bijectively to two-planes in the dual four-space, giving \({4\brack2}_q\) hyperplanes. There are \({6\brack1}_q\) projective nonzero forms in all; the remaining \({6\brack1}_q-{4\brack2}_q\) have rank four. Multiplying by the number \({d\brack4}_q\) of possible \(U\) and the \(q^{d-4}\) graph lifts gives both orbit sizes. Applying the general count to the other two profiles gives their sizes, completing the four-orbit statement.

## Verification
Run the standalone `check_ideal_orbit_threshold.py` with Python 3.9 or later. It enumerates all ideals in \(L_3(\mathbb F_2)\) independently using subspace RREF and bracket closure, and compares the whole defect table (45 ideals) with the formula. It separately generates the \(\operatorname{GL}_4(\mathbb F_2)\)-orbit partition of all 63 projective alternating forms (orbit sizes 35 and 28, with ranks two and four), and counts the 364 projective alternating forms over \(\mathbb F_3\) by rank (130 and 234). Finally it cross-checks the low-codimension Gaussian sums for primes \(2,3,5\) and generator dimensions \(3,4,5,6\). The checker outputs `ALL_IDEAL_ORBIT_THRESHOLD_CHECKS_PASSED`. These finite checks corroborate but do not prove the all-prime-power assertion; the proof above does.

## Relationship to prior work
Benito and Roldán-López (arXiv:1911.01897, first public posting 2019-11-05) describe the automorphism group of free nilpotent Lie algebras and their quotients; their Proposition 1 and Remark 2 supply the characteristic-zero automorphism framework, not an embedded-ideal orbit threshold or finite-field orbit sizes. The present automorphism description is proved directly in the two-step setting for arbitrary characteristics.

Cicalò, de Graaf, and Schneider (arXiv:1011.0361) classify six-dimensional nilpotent Lie algebras over arbitrary fields and the orbits of \(\operatorname{GL}_4\) on **two-dimensional** subspaces of an exterior square (Theorem 4.4). Those orbit data neither tabulate the embedded ideals of \(L_d\) nor establish the *codimension-five, fixed-defect* splitting and sizes. Classical alternating-form rank normal forms and Gaussian subspace counts are prior ingredients, not claimed as original here. The result is an exact synthesis identifying the first non-transitive ideal defect stratum and counting both full-automorphism orbits in every finite field.

## Limitations
The result does not classify ideal orbits for all codimensions greater than five. Higher-codimension strata involve larger spaces of alternating forms and more complicated pencils. The discovery claims no novelty for the automorphism semidirect product, exterior-power quotient, rank classification of individual alternating forms, or generic Gaussian coefficients. The historical priority risk that this low-codimension threshold may be implicit in older ideal/orbit literature remains; neither absence from semantic search nor a finite computation proves uniqueness. No independent external mathematical validation has been performed.

## References
- P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897 (first posted 2019-11-05), especially Proposition 1, Remark 2 and Theorem 2.
- S. Cicalò, W. A. de Graaf and C. Schneider, *Six-dimensional nilpotent Lie algebras*, arXiv:1011.0361 (first posted 2010-11-01), especially Theorem 4.4.
- P. Benito and D. de-la-Concepción, *An overview of free nilpotent Lie algebras* (2014), Proposition 2.3.
