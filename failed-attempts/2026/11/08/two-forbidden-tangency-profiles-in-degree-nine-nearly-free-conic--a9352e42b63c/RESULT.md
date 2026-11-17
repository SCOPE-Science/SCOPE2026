# Two forbidden tangency profiles in degree-nine nearly free conic–line arrangements

## Finding
Let \(Q\subset\mathbb P^2_{\mathbb C}\) be a smooth conic and \(L_1,\ldots,L_7\) seven distinct complex lines, none a component of \(Q\). Assume the reduced curve \(D=Q\cup L_1\cup\cdots\cup L_7\) has only ordinary nodes \(A_1\), tacnodes \(A_3\), and ordinary triple points \(D_4\). Let \(t\) be the number of tacnodes (equivalently, the number of lines tangent to \(Q\)), \(n_2\) the number of nodes, and \(n_3\) the number of ordinary triple points.

**Theorem.** If \(D\) is nearly free, then exactly one of the following two *necessary* weak-combinatorics profiles holds:
\[
(t,n_2,n_3)=(3,2,9)\quad\text{or}\quad(4,3,8).
\]
In particular, a nearly free arrangement with precisely one or precisely two lines tangent to \(Q\) does not exist. Neither surviving profile is asserted to be realizable, and the theorem does not settle the unrestricted degree-nine existence problem.

The new exclusions are the one- and two-tangency cases. The fact that only \(1\leq t\leq4\) is numerically possible follows from previously published inequalities; it is not claimed as new.

## Assumptions and scope
Work over the algebraically closed field \(\mathbb C\); the seven lines are distinct and the conic is smooth. An ordinary triple point has three smooth branches with distinct tangent directions. A tacnode consists of a conic and one line meeting with multiplicity two; no additional component passes through it under the stated singularity assumption. Every line not tangent to the conic meets it at two distinct points. The Jacobian syzygy degree is \(r=\operatorname{mdr}(D)\), and nearly free means that the saturation quotient of its Jacobian ideal has graded dimensions at most one and is nonzero, in the standard sense.

For a nearly free reduced curve of degree \(9\) in this class, the known inequality \(r\geq \tfrac23(9)-2=4\), together with \(r\leq\lfloor9/2\rfloor=4\), gives \(r=4\). The numerical near-freeness criterion yields \(\tau(D)=8^2-4(8-4)-1=47\). Bézout and local Tjurina numbers give
\[
 n_2+2t+3n_3=\binom72+2\cdot7=35,\qquad
 \tau(D)=n_2+3t+4n_3.
\]
Thus \(t+n_3=12\) and \(n_2=t-1\). The published Hirzebruch-type inequality \(8+n_2+\tfrac34n_3\geq7+\tfrac52t\) forces \(t\leq4\). Nonnegativity forces \(t\geq1\). Therefore the four *numerically* permitted profiles are
\[
 (t,n_2,n_3)=(1,0,11),(2,1,10),(3,2,9),(4,3,8).
\]
We exclude the first two geometrically and combinatorially.

## Proof
**Incidence bookkeeping.** Split ordinary triple points into \(u\) points consisting of three lines (type \(LLL\)) and \(v\) points consisting of the conic and two secant lines (type \(QLL\)). A \(QLL\) point cannot involve a tangent line: at a conic tangency any additional component would violate the prescribed singularity types. A line pair is used exactly once, either at an \(LLL\) point (three line pairs), a \(QLL\) point (one line pair), or a line–line node (one line pair). A secant line has exactly two conic-intersection positions, hence \(2v\leq2(7-t)\), or \(v\leq7-t\). Distinct conic triple points correspond to distinct pairs of secant lines.

**One tangent line.** Suppose \(t=1\). Then \(n_2=0,n_3=11\). Since \(u+v=11\), and the \(\binom72=21\) pairs of lines give \(3u+v=21\), necessarily \(v=6,u=5\). Write \(T\) for the tangent line and \(N_1,\ldots,N_6\) for the secants. Each secant meets the conic at two \(QLL\) points, so the graph on the six secant lines whose edges record \(QLL\) points is two-regular. Every one of the six intersections \(T\cap N_i\) must be an \(LLL\) triple, pairing the secants into three disjoint pairs because nodes are absent. Thus exactly three \(LLL\) points have type \(TNN\), and two have type \(NNN\). For each secant, two of its five secant–secant pairs have been consumed at conic triples and one at a \(TNN\) point. The remaining two pairs must be used together at a single \(NNN\) point. It follows that the two \(NNN\) points each contain three secants and partition the six secants into concurrent triples \(A_0,A_1,A_2\) and \(B_0,B_1,B_2\). Every pair within each triple is already used at its point of concurrence. The six \(QLL\) pairs therefore form a two-regular bipartite graph between the two triples, namely \(K_{3,3}\) minus a perfect matching: a six-cycle. The three missing cross-pairs are the \(TNN\) points, all lying on the tangent line \(T\).

**Secant-Pascal lemma.** Such a configuration of six secant lines is incompatible with a *tangent* matching line. Here is a direct projective proof, not merely an appeal to a picture of Pascal's theorem. Normalize the conic to \(Q:XZ=Y^2\), parametrized by \(P(z)=[z^2:z:1]\). The three concurrent chords \(A_i\) induce one involution \(\sigma\) of \(Q\), and the three concurrent chords \(B_j\) another \(\eta\). Neither center lies on \(Q\), since that would force more than three branches through a point. The six-cycle says that their product acts as a three-cycle on three distinct points; since a nonidentity projectivity of \(\mathbb P^1\) cannot fix three points, their product has order three. Conjugating in \(\operatorname{PGL}_2(\mathbb C)\), one may write \(\sigma(z)=1/z\) and \(\eta(z)=\omega/z\), where \(\omega^3=1\) and \(\omega\neq1\). The six distinct points are, after relabeling, the orbits of \(s\in\mathbb C^\times\) under these involutions; \(s^2\notin\{1,\omega,\omega^2\}\).

The associated chords are
\[
 A_i:\ X-(s\omega^i+s^{-1}\omega^{-i})Y+Z=0,
 \quad B_j:\ X-(s\omega^j+s^{-1}\omega^{1-j})Y+\omega Z=0,
 \qquad i,j\in\mathbb Z/3\mathbb Z.
\]
The two conic intersections on \(A_i\) lie on \(B_i\) and \(B_{i+1}\), so the unmatched cross-point is \(M_i=A_i\cap B_{i-1}\). Let \(a_i=s\omega^i+s^{-1}\omega^{-i}\) and \(b_{i-1}=s\omega^{i-1}+s^{-1}\omega^{2-i}\). Directly \(a_i=\omega b_{i-1}\). Substituting \(X=\omega^2Z\) into both chord equations therefore gives the same equation for \(Y\), so each \(M_i\) lies on
\[
 T_0:\quad X-\omega^2 Z=0.
\]
The three \(M_i\) are distinct: equality of two would force both concurrency centers to coincide and produce a forbidden higher multiple intersection. Thus their common line \(T\) equals \(T_0\). But \(Q\cap T_0\) consists of \(P(\omega)\) and \(P(-\omega)\), which are distinct in characteristic zero. Hence \(T_0\) is a secant, not a tangent. Contradiction.

**Two tangent lines.** Suppose \(t=2\). Then \(n_2=1,n_3=10\). The line-pair count gives \(21\geq3u+v=30-2v\), hence \(v\geq5\). There are five secants and each supplies two conic intersections, so \(v\leq5\). Consequently \(v=5\), \(u=5\), and exactly one of the line pairs is an ordinary node. In particular, every secant has exactly two \(QLL\) points.

Let \(a,b,c\) respectively count \(LLL\) triples of types tangent–tangent–secant, tangent–secant–secant, and secant–secant–secant. There is only one pair of tangent lines, so \(a\leq1\). We have \(a+b+c=5\). Among the ten secant–secant pairs, five are already used at \(QLL\) points. The other \(LLL\) triples use \(b+3c\leq5\) such pairs. Substituting \(b=5-a-c\) yields \(2c\leq a\leq1\), whence \(c=0\).

If \(a=0\), then \(b=5\); these five triples consume all ten tangent–secant pairs. On either tangent line, the five secants would have to be paired at triple intersections, impossible because five is odd. If \(a=1\), then \(b=4\); the one tangent–tangent–secant triple and four tangent–secant–secant triples again consume all ten tangent–secant pairs. The secant appearing in the first triple cannot appear at another \(LLL\) triple (there are no \(NNN\) triples and its intersections with both tangents have been used). Of its four secant–secant pairs, exactly two occur at its \(QLL\) points, so the remaining two must be distinct ordinary nodes. This contradicts \(n_2=1\). Therefore \(t=2\) is also impossible.

Combining both exclusions with the four previously available numerical candidates proves the theorem. \(\square\)

## Verification
The standalone `verify_incidence_pascal.py` reproduces the exact arithmetic of the four candidate profiles; enumerates all abstract incidence decompositions for the one- and two-tangency cases under the necessary pair-incidence constraints; and checks the cyclotomic Laurent-polynomial identity \(a_i=\omega b_{i-1}\) in \(\mathbb Z[\omega]/(\omega^2+\omega+1)\). Run `python3 verify_incidence_pascal.py`. Its success marker is `DEGREE9_INCIDENT_PASCAL_PASS 60 {6: 60} 0 0 3`. The 60 labelled one-tangency abstract decompositions all have the required six-cycle; no two-tangency decomposition exists. Finite incidence enumeration is a cross-check: the proof above is self-contained for arbitrary complex parameters and does not infer geometry from a finite search.

## Relationship to prior work
Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969 (first posted 2022-04-29), supplies the nearly free numerical criterion, the Jacobian-syzygy bound, and the Hirzebruch-type inequality used to restrict the possible profiles. The paper explicitly leaves degree nine unresolved; it does not provide the two geometric exclusions proved here. Măcinic and Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228 (2023-09-26), treats defect-two plus-one generated arrangements and discusses degree-nine candidate weak types for a different homological condition; those statements do not settle the defect-one, nearly free profiles here. Pokora, arXiv:2312.13052 (2023-12-20), treats free arrangements with ordinary singularities, not the nearly free tacnodal profiles under consideration. Classical Pascal and Möbius-involution geometry provides tools for the one-tangency argument, but their application to the degree-nine nearly free weak-combinatorics question is the additional result.

## Limitations
The theorem is confined to one smooth conic and seven distinct lines over \(\mathbb C\), with exactly the three specified singularity types. It does **not** exclude nearly free arrangements with three or four tacnodes, arrangements having two or more conics, or arrangements admitting other singularities. It is a necessary-condition theorem, not an existence theorem for the two remaining types. Historical priority has been compared with the specified literature and mathematical-record searches but has not been independently certified; classical incidence literature may contain a less specialized version of the secant-Pascal lemma.

## References
1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969, 2022; https://arxiv.org/abs/2204.13969.
2. A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228, 2023; https://arxiv.org/abs/2309.15228.
3. P. Pokora, *Freeness of arrangements of lines and one conic with ordinary quasi-homogeneous singularities*, arXiv:2312.13052, 2023; https://arxiv.org/abs/2312.13052.
