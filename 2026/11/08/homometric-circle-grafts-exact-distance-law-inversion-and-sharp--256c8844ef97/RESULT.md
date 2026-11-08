# Homometric circle grafts: exact distance-law inversion and sharp four-site nonrigidity

## Finding

Fix a real circle circumference \(C>0\), a nontrivial compact finite **rooted metric tree** \((T,o)\) of positive total edge length \(\tau\), and an integer \(m\ge1\). For every set of \(m\) distinct circle sites \(A=\{a_1,\ldots,a_m\}\subset\mathbb R/C\mathbb Z\), form \(G_A\) by attaching, at each \(a_i\), an identical copy of \(T\), identifying its root \(o\) with that circle point. Distances are intrinsic shortest-path distances and the sampling measure is normalized total arclength.

Let \(D_A=d_{G_A}(X,Y)\) for two independent arclength-uniform points, and define the multiset of shorter-arc attachment distances
\[
H_A=\{\delta_C(a_i,a_j):1\le i<j\le m\},\qquad
\delta_C(u,v)=\min\{|u-v|,C-|u-v|\}.
\]
**Classification:** for fixed \(C,T,m\),
\[
\boxed{\mathcal L(D_A)=\mathcal L(D_B)\quad\Longleftrightarrow\quad H_A=H_B.}
\]
Thus the *complete* global distance distribution recovers exactly the attachment-distance histogram, and nothing about the circular ordering beyond that histogram. The proof supplies an explicit Laplace-transform inversion formula.

Two such graphs are intrinsically isometric if and only if their site sets are congruent by a circle rotation or reflection. For \(1\le m\le3\), the recovered histogram forces such congruence, so the distance law distinguishes isometry classes **inside this fixed-parameter family**. The bound is sharp: when \(C=8\), the site sets
\[
A=\{0,1,3,4\},\qquad B=\{0,1,2,5\}
\]
have the common shorter-distance multiset \(\{1,1,2,3,3,4\}\), but are not congruent. Consequently they yield nonisometric metric graphs with *exactly identical global distance laws* for **every** choice of common nontrivial finite rooted metric tree, including any common positive-length pendant interval.

## Assumptions and scope

A finite metric tree is a connected compact loop-free metric graph with finitely many positive-length edges; the root is any specified point. Edges are measured by their usual one-dimensional arclength. Copies of the rooted tree are attached only at the specified, pairwise distinct sites; no two copies are otherwise identified. The circle may be subdivided at attachment sites. The parameter triple \((C,T,m)\) is fixed when comparing \(G_A\) and \(G_B\), and the sampling is from their **whole** metric graphs, not solely from leaves or roots. The total length is \(L=C+m\tau\), independent of placement.

Write \(U_s=\tau^{-1}\int_T e^{-s d_T(o,x)}\,dx\), \(V_s=\tau^{-2}\int_T\int_T e^{-s d_T(x,y)}\,dx\,dy\), and \(Q_s=2(1-e^{-sC/2})/(sC)\), for \(s>0\). In particular \(U_s>0\).

## Proof

**1. Exhaustive distance decomposition.** Partition each ordered pair of sampled points according to whether its endpoints belong to (i) the circle, (ii) the circle and one attached tree, (iii) the same attached tree, or (iv) two different attached trees. Attachment and root points have zero arclength and hence need no boundary corrections.

Two independently circle-uniform points have shorter circular distance uniformly distributed on \([0,C/2]\), whose Laplace transform is \(Q_s\). For a circle point and a rooted-tree point, the distance is their circle separation from the root plus tree-root depth. Rotation invariance makes the Laplace transform \(Q_s U_s\). For two points in the same tree, their intrinsic distance remains their distance *inside* that tree (an excursion through the cycle could only leave and reenter through the same root), giving transform \(V_s\). For points in distinct attached trees at sites \(a_i,a_j\), the distance is the sum of their respective root depths and \(\delta_C(a_i,a_j)\), giving \(U_s^2e^{-s\delta_C(a_i,a_j)}\).

Weighting all these cases by unnormalized products of component lengths gives, for \(s>0\),
\[
\boxed{
L^2\mathbb E[e^{-sD_A}]
=C^2 Q_s+2Cm\tau Q_s U_s+m\tau^2V_s
+2\tau^2 U_s^2\sum_{i<j}e^{-s\delta_C(a_i,a_j)}.}
\tag{1}
\]
No independence between a tree's *two* sampled depths is assumed for the same-tree term; it is represented by the correct joint integral \(V_s\).

**2. Both directions of the classification.** If the multisets \(H_A,H_B\) coincide, their exponential sums coincide identically, and (1) gives equality of Laplace transforms and hence equality of finite probability distributions on \([0,\infty)\). Conversely, if these probability distributions coincide, solve (1):
\[
\boxed{
\sum_{h\in H_A}e^{-sh}
=\frac{L^2\mathbb E[e^{-sD_A}]-C^2Q_s-2Cm\tau Q_sU_s-m\tau^2V_s}
{2\tau^2U_s^2}.}
\tag{2}
\]
The denominator is positive for every \(s>0\). Equality of all positive-parameter exponential sums of two finite multisets implies equality of those multisets: identify the smallest support point by the slowest decay as \(s\to\infty\), its multiplicity by the leading coefficient, subtract, and iterate. This also proves the constructive inversion assertion.

**3. Isometry and the three-site threshold.** A graph \(G_A\) has exactly one embedded cycle, namely the original metric circle; each nontrivial attached tree is acyclic. Any intrinsic isometry therefore preserves the circle. It also preserves the set of points where a nontrivial tree component leaves the circle, namely \(A\). Every isometry of a metric circle is a rotation or reflection. Conversely a circle rotation/reflection carrying \(A\) to \(B\), together with arbitrary fixed rooted isometries between the corresponding copies of \(T\), extends to an isometry \(G_A\to G_B\).

For one or two sites, the statement that the circular pair-distance multiset determines the site configuration up to circle isometry is immediate. For three sites, let the three cyclic gaps be positive \(g_1,g_2,g_3\) with sum \(C\), and let \(d_1\le d_2\le d_3\) be the recovered three shorter-pair distances. If every gap is at most \(C/2\), the multiset of gaps is exactly \(\{d_1,d_2,d_3\}\). Otherwise one gap \(g_{\max}>C/2\), and the pairwise shorter distances are the other two gaps and their sum \(C-g_{\max}\); necessarily \(d_1+d_2=d_3\) and \(d_1+d_2+d_3<C\), and the gaps are \(\{d_1,d_2,C-d_3\}\). At equality \(g_{\max}=C/2\) both reconstructions agree. Thus the unordered cyclic gaps—and hence the triple of circle sites up to rotation/reflection—are determined. This proves sharp rigidity for \(m\le3\).

**4. Four-site counterexample.** On a circle of circumference \(8\), direct enumeration of all six unordered pairs gives \(H_A=H_B=\{1,1,2,3,3,4\}\). The cyclic gap multisets are \(\{1,1,2,4\}\) for \(A\) and \(\{1,1,3,3\}\) for \(B\). A rotation or reflection preserves the cyclic gap multiset, so no circle isometry identifies them. By steps 2 and 3, their attached-tree metric graphs are nonisometric but have the same full arclength distance distribution. This establishes minimality of four attachments and completes the proof.

## Verification

The standalone `CHECK.py` uses exact integer arithmetic for the two multisets and dihedral noncongruence. It exhaustively checks the three-site uniqueness property on grids of circumference \(4\) through \(16\) (illustrative finite tests, not a replacement for step 3), computes the exact Laplace expression for the special case when \(T\) is a rooted interval of length \(0.7\), and directly simulates independent arclength-uniform pairs in the two metric graphs. The Monte Carlo tests exercise shortest-path distances across all four pair types; the analytical proof is independent of simulation.

For a rooted interval of length \(\ell>0\), the formulas used in the checker are \(U_s=(1-e^{-s\ell})/(s\ell)\) and \(V_s=2(s\ell-1+e^{-s\ell})/(s^2\ell^2)\). These verify the same-tree normalization in (1). Equation (1) yields \(1\) at \(s\downarrow0\), since \(C^2+2Cm\tau+m^2\tau^2=L^2\).

## Relationship to prior work

The circular sets \(\{0,1,3,4\}\) and \(\{0,1,2,5\}\), including their cyclic interval homometry, are **classical**, not new: Jedrzejewski and Johnson (2013, §2) explicitly report them, tracing related homometry constructions to earlier work. Axenovich and Özkahya (2012) develop discrete-graph homometric sets, whose objects and objectives differ from area-/arclength-uniform two-point distributions on continuous metric graphs.

Mémoli and Needham (2018 preprint, 2022 revision, Proposition 3.21) prove an autocorrelation characterization of global pairwise distance distributions for *weighted circles*, and (2022, §4.1, Example 4.3) exhibit other metric-graph nonuniqueness. Their general decomposition principle is closely related to the sufficiency direction here. The present claim is restricted to a **fixed circle with identical attached finite rooted metric trees**, and asserts the two-sided complete classification (2) plus the sharp isometry threshold at exactly four attachment sites. Neither the broad fact of noninjectivity nor the classical homometric example alone is claimed as new. These existing results make the priority of any informal one-direction corollary particularly delicate.

## Limitations

The classification does not apply when the circumference, attachment count, or isometry type of the rooted trees is allowed to vary between graphs. It also does not characterize local distance distributions, provide stable recovery in the presence of measurement noise, or imply that arbitrary unicyclic metric graphs are distinguishable by their two-point laws. The four-site example is a transfer of a known circular homometric configuration; the claimed contribution is the continuous metric-graph **if-and-only-if deconvolution classification** and its minimal rigidity threshold, not the discovery of a new homometric set. Although the comparison inspected relevant sources, exhaustive historical priority is not certified.

## References

1. F. Jedrzejewski and T. Johnson, *The Structure of Z-related Sets*, arXiv:1304.6608 (first public version 23 April 2013), §§1–2, especially the four-site \(\mathbb Z_8\) example.
2. M. Axenovich and L. Özkahya, *On Homometric Sets in Graphs*, arXiv:1203.1158 (first public version 6 March 2012), §§1–3.
3. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, arXiv:1810.09646 (first public 23 October 2018), especially Proposition 3.21 and §4.1; later journal version, *Studies in Applied Mathematics* 149 (2022), 943–1001.
