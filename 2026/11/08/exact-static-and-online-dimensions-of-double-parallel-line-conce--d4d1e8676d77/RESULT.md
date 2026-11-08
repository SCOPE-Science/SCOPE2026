# Exact static and online dimensions of double-parallel-line concepts in finite affine planes

## Finding
Let \(\Pi\) be **any** finite affine plane of order \(q\ge 2\). Write \(X\) for its \(q^2\) points and let
\[
\mathcal D(\Pi)=\{L\cup M:L,M\text{ are two distinct parallel lines of }\Pi\}\subseteq 2^X.
\]
The VC dimension and the deterministic realizable Littlestone dimension of point-membership queries coincide, with the following exact values:
\[
\boxed{\operatorname{VCdim}(\mathcal D(\Pi))=\operatorname{Ldim}(\mathcal D(\Pi))=\begin{cases}
0,&q=2,\\
2,&q=3,\\
4,&q\ge4.
\end{cases}}
\]
These statements require only the finite affine-plane incidence axioms; no field coordinates or Desarguesian assumption are used. In particular, four is the sharp universal depth bound for online mistake trees, and the first order admitting depth four is \(q=4\).

## Assumptions and scope
An affine plane of order \(q\) has \(q^2\) points, \(q+1\) parallel classes of \(q\) disjoint \(q\)-point lines, exactly one line joining each two distinct points, and a unique line through any point parallel to a prescribed line. The concept family contains unions of **exactly two distinct parallel** lines, never intersecting pairs, individual lines, or arbitrary unions. Duplicate point sets count once. For \(q=2\) all such unions equal \(X\).

A point support \(S\subseteq X\) is VC-shattered if every subset of \(S\) occurs as the intersection \(C\cap S\) for some \(C\in\mathcal D(\Pi)\). The Littlestone dimension is the largest integer \(d\ge0\) for which a complete binary tree of depth \(d\), whose internal nodes query points of \(X\), has a consistent concept for every length-\(d\) Boolean answer path. A class consisting of a single concept has both dimensions zero. A fixed shattered support of size \(d\) gives a depth-\(d\) tree by querying those points in any fixed order.

## Proof
**1. A localization lemma for three positive queries.** For a set \(A\subseteq X\), put \(\mathcal D_A=\{C\in\mathcal D(\Pi):A\subseteq C\}\). Fix any three *distinct* points \(a,b,c\). If they are noncollinear, every covering pair of parallel lines must place two of the points on one line and the third on a distinct parallel line. Each choice of the paired points determines at most one such union, so \(|\mathcal D_{\{a,b,c\}}|\le3\). A class of at most three distinct concepts has Littlestone dimension at most one, because a complete depth-two mistake tree requires at least four concepts.

If \(a,b,c\) are collinear on a line \(L\), then two lines not parallel to \(L\) cover at most two points of \(L\). Thus every member of \(\mathcal D_{\{a,b,c\}}\) is \(L\cup M\), where \(M\ne L\) is parallel to \(L\). A point of \(L\) belongs to every member; every point outside \(L\) belongs to exactly one member. Hence no query can split this family into two subfamilies that both contain at least two members. Its Littlestone dimension is at most one. We have shown, in both cases, that
\[
\operatorname{Ldim}(\mathcal D_{\{a,b,c\}})\le1.
\]

**2. Uniform online upper bound.** We use the elementary mistake-tree recursion: a concept family can shatter a depth-\(d+1\) complete binary tree only if some first query has *both* its positive and negative subfamilies of Littlestone dimension at least \(d\). For distinct \(a,b\), any query \(c\notin\{a,b\}\) gives a positive subfamily of \(\mathcal D_{\{a,b\}}\) equal to \(\mathcal D_{\{a,b,c\}}\), of dimension at most one by step 1. Querying \(a\) or \(b\) gives no negative branch. Therefore \(\operatorname{Ldim}(\mathcal D_{\{a,b\}})\le2\). Applying the same argument first to the class containing a specified point \(a\), and then to the unrestricted class, yields
\[
\operatorname{Ldim}(\mathcal D_{\{a\}})\le3,
\qquad \operatorname{Ldim}(\mathcal D(\Pi))\le4.
\]
Since VC dimension never exceeds Littlestone dimension, this bounds both invariants by four.

**3. A four-point shattered support when \(q\ge4\).** Choose four distinct points \(p_0,p_1,p_2,p_3\) on a line \(L\) and a point \(r\notin L\). We claim that
\[
S=\{p_0,p_1,p_2,r\}
\]
is VC-shattered. Fix any requested subset \(T\subseteq\{p_0,p_1,p_2\}\) and any requested label of \(r\). If \(|T|=0\), choose two lines parallel to \(L\) other than \(L\); there are at least three such lines, so we can make their union contain or avoid \(r\). If \(|T|=3\), choose \(L\) and a second parallel line, again chosen to contain or avoid \(r\).

For \(|T|=1\), choose the two designated intersections with \(L\) to be the member of \(T\) and the spare point \(p_3\). For \(|T|=2\), use the two members of \(T\). In either case, call those distinct points \(u,v\in L\). Each of the \(q\) directions other than that of \(L\) gives a pair of distinct parallel lines through \(u\) and \(v\), meeting \(L\) exactly in \(\{u,v\}\). Of these directions, exactly two make the union contain \(r\): the directions of \(ru\) and \(rv\), which differ because \(r\notin L\). Since \(q\ge4\), at least one remaining direction makes the union avoid \(r\). Thus both choices for the label of \(r\) are possible, independently of the requested labels on \(p_0,p_1,p_2\). All sixteen traces on \(S\) occur. Therefore \(\operatorname{VCdim}\ge4\), proving equality with the upper bound. This also supplies a depth-four nonadaptive mistake tree.

**4. Exceptional orders.** When \(q=2\), the union of two distinct parallel lines is the entire plane, so the class has a single concept and both dimensions vanish. When \(q=3\), each parallel class partitions the plane into three lines; a union of exactly two of them is the complement of the third. Thus \(\mathcal D(\Pi)\) is the class of complements of individual affine lines. Complementing all concepts preserves both VC and Littlestone dimensions (by reversing the binary answers). The class of affine lines has Littlestone dimension at most two: after one positive point query \(a\), any other positive point query \(b\ne a\) leaves at most the unique line through \(a,b\), so the class of lines through \(a\) has dimension at most one. It has VC dimension at least two: any two points can be jointly included by their line, included singly by lines through just one of them, and jointly excluded by another line parallel to their joining line. Hence both dimensions equal two for \(q=3\). All cases follow.

## Verification
An independent finite-field implementation (`verify.py`) constructs every affine line, forms all distinct unions of two different parallel lines, and evaluates the exact finite Littlestone recurrence by memoized subset recursion. It independently checks sixteen traces on the explicit four-point support for every tested \(q\ge4\). The fields tested are \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_8\), \(\mathbb F_9\), and \(\mathbb F_{11}\). The final output is `DOUBLE_PARALLEL_LINE_RANKS_PASS`. These are finite corroborations, not a proof for arbitrary planes or larger orders; the universal proof is above.

## Relationship to prior work
The 2019 paper of Cambie, Girão, and Kang investigates extremal unions and symmetric differences of arbitrary set systems; its conclusions are not the exact affine-plane double-parallel-line dimensions. The 2019 paper of Csikós, Mustafa, and Kupavskii establishes tight VC bounds for unions of real halfspaces, without parallel-line restriction or adaptive rank. Ghazi, Golowich, Kumar, and Manurangsi (2021) establish general Littlestone closure bounds; these do not determine the three exact finite-plane regimes. Eleftheriou, Papadopoulos, and Westhead (2025) establish VC dimension five for unions of two unrestricted real planar lines; their results do not calculate the online dimension for finite affine planes, nor the distinct-parallel-line threshold. Earlier results for all pairs of projective lines likewise concern a strictly larger family, not these exact online ranks. No claim is made of novelty for the standard affine-plane axioms, VC/Littlestone definitions, or general closure bounds.

## Limitations
The theorem concerns exactly-two-distinct-parallel-line unions on a finite affine plane, not arbitrary pairs of affine lines, unions of more than two lines, affine spaces of dimension greater than two, or infinite planes. It asserts no formula for the shattering polynomial or a complete classification of every four-point shattered support. The theorem is unconditional for every existing finite affine plane, including non-Desarguesian examples; it does not assert existence of planes at all numerical orders. The comparison with prior work is a best-knowledge priority assessment, not an independent literature certification.

## References
1. S. Cambie, A. Girão, and R. J. Kang, *VC dimension and a union theorem for set systems*, Electronic Journal of Combinatorics 26(3), P3.24, first published 2019-08-02, https://doi.org/10.37236/8288.
2. M. Csikós, N. H. Mustafa, and A. Kupavskii, *Tight Lower Bounds on the VC-dimension of Geometric Set Systems*, Journal of Machine Learning Research 20(81), 2019, https://jmlr.org/papers/v20/18-719.html.
3. B. Ghazi, N. Golowich, R. Kumar, and P. Manurangsi, *Near-tight closure bounds for the Littlestone and threshold dimensions*, Proceedings of Machine Learning Research 132 (2021), https://proceedings.mlr.press/v132/ghazi21a.html; arXiv:2007.03668.
4. P. E. Eleftheriou, A. Papadopoulos, and F. Westhead, *Exact VC-Dimensions of Certain Geometric Set Systems*, arXiv:2501.09847v1, first posted 2025-01-16.
