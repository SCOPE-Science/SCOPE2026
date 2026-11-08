# A six-conic ceiling for nearly free arrangements, with a rigid triple-free boundary

## Finding
Let \(\mathcal C\subset\mathbb P^2_{\mathbb C}\) be the reduced union of \(k\ge2\) distinct smooth conics. Suppose that all its singularities are nodes \(A_1\), tacnodes \(A_3\), ordinary transverse triple points \(D_4\), two-branch contacts \(A_5\), or two-branch contacts \(A_7\). If \(\mathcal C\) is nearly free, then **\(k\le6\)**. If there are no ordinary triple points, then **\(k\le5\)**, and \(k=5\) forces precisely
\[
(n_2,t_3,n_3,t_5,t_7)=(13,0,0,1,6).
\]
Here \(n_2,t_3,n_3,t_5,t_7\) count the five singularity types in the order given above. In that hypothetical five-conic case, the graph joining pairs of conics at their \(A_7\)-contact points is exactly \(K_{2,3}\); the unique \(A_5\) pair is a nonedge. In the still narrower subclass permitting only \(A_1\) and \(A_7\), one has the **sharp bound \(k\le4\)**. The explicit four-conic witness below realizes equality.

The conditional five-conic profile is not asserted to be geometrically realizable. No assertion of existence is made for six conics with ordinary triple points.

## Assumptions and scope
The ground field is \(\mathbb C\). The conics are smooth and pairwise distinct; their union is reduced. The singularities listed above are **exhaustive**, so no quadruple points, triple tangencies, or contacts involving three branches are permitted. The local contact multiplicities of \(A_3,A_5,A_7\) between two smooth branches are, respectively, two, three, four. Each of these quasihomogeneous singularities has local Tjurina number three, five, seven; a node has one, an ordinary triple point four. For \(f\) the degree-\(2k\) defining equation, near freeness is characterized by the standard Dimca–Pokora criterion in Reference [2]: if \(r=\operatorname{mdr}(f)\), then \(r\le k\) and
\[
\tau(\mathcal C)=(2k-1)^2-r(2k-r-1)-1.
\]
The Arnold-exponent syzygy inequality used in Reference [2] gives \(r\ge5k/4-2\), since all allowed local thresholds are at least \(5/8\). In particular Reference [2] establishes \(k\le8\) for nearly free arrangements under these assumptions, and \(r=k\) when \(5\le k\le8\). The theorem here improves and stratifies this published upper bound.

## Proof
**1. Incidence equations.** Write \(K=k(k-1)\). Pairwise Bézout and the local Tjurina numbers give
\[
2K=n_2+2t_3+3n_3+3t_5+4t_7,\qquad
\tau=n_2+3t_3+4n_3+5t_5+7t_7.
\]
For \(5\le k\le8\), the cited near-free syzygy constraint gives \(r=k\), hence \(\tau=3K\). Subtracting yields
\[
K=t_3+n_3+2t_5+3t_7,\quad
n_2=t_5+2t_7-n_3.
\]
Put \(x=n_3,\ y=t_5,\ z=t_7\), so that \(x\le y+2z\) and \(x+2y+3z\le K\).

**2. An improved global bound.** Zieliński's inequality [1, Theorem 1.1] is
\[
560k+100n_2+75n_3\ \ge\ 184t_3+404t_5+608t_7.
\]
The displayed substitutions reduce it, with no discarded terms, to
\[
F:=159x+64y+144z\ \ge\ 184K-560k.
\]
On the other hand,
\[
462(x+2y+3z)-5F=-333x+604y+666z\ge271y\ge0.
\]
Consequently \(F\le462K/5\). For \(k=8\), this contradicts the preceding lower bound since \(458(k-1)>2800\). The existing \(k\le8\) bound rules out every larger integer.

To exclude \(k=7\), put \(K=42\), \(a=n_2\), and \(b=t_3\). The two incidence equations imply
\[
3y=42-5z+a-b,\qquad
3F=223\cdot42+271z-254a-223b.
\]
The lower bound on \(F\) is equivalent to
\[
271z-254a-223b\ge2058.
\]
If \(z\le7\), the left side is at most \(1897\). If \(z=8\), then \(a=b=0\) would be forced, but \(3y=2\) has no integer solution. If \(z\ge9\), nonnegativity of \(y\) gives \(a\ge5z-42+b\), hence
\[
271z-254a-223b\le10668-999z-477b\le1677,
\]
again impossible. This proves \(k\le6\).

**3. Excluding the triple-free six-conic case.** If \(x=0\), then
\[
F=64y+144z\le48(2y+3z)\le48K.
\]
Thus \(136K\le560k\), or \(136(k-1)\le560\), excluding \(k\ge6\). With \(k=5\), \(K=20\) and \(F\ge880\). The inequalities \(2y+3z\le20\) and \(64y+144z\ge880\), for nonnegative integers \(y,z\), force \(z=6\), \(y=1\): if \(z\le5\) the maximum is \(848\), whereas \(z=6\) allows \(y\le1\) and requires \(y\ge1\). Back substitution gives \(t_3=0\), \(n_2=13\). Since \(y=1\), the narrower nodes-and-\(A_7\) class has no five-conic member and hence has \(k\le4\).

**4. Structure of the six extreme contacts.** Build a simple graph on the conics, joining two vertices when those conics have an \(A_7\) contact. It is triangle-free. Indeed, suppose two conics \(Q_2,Q_3\) have full order-four contact with a common smooth conic \(Q_1\) at distinct points \(P\) and \(Q\). Distinctness follows from the exclusion of higher multibranch singularities. A projective coordinate change puts \(Q_1=xz-y^2\), \(P=[1:0:0]\), \(Q=[0:0:1]\). Since the complete intersection divisor on \(Q_1\) is \(4P\) or \(4Q\), the quadratic equations may be scaled to \(Q_2=Q_1+\alpha z^2\), \(Q_3=Q_1+\beta x^2\) with \(\alpha\beta\ne0\). Their difference factors as \(\alpha z^2-\beta x^2\), a pair of distinct lines meeting away from \(Q_2\) and \(Q_3\). Therefore \(Q_2,Q_3\) have at least two distinct intersection points and cannot themselves meet in one \(A_7\) point. Every triangle is excluded. The unique triangle-free graph with six edges on five vertices is \(K_{2,3}\), by the equality case of Mantel's theorem. The remaining unique \(A_5\) contact must occupy a nonedge, because an \(A_7\) pair already accounts for all four Bézout intersections.

**5. Sharpness for nodes and \(A_7\) contacts.** The following four smooth conics form a nearly free arrangement:
\[
\begin{aligned}
Q_0&=x^2+y^2-z^2, &Q_1&=2x^2+y^2+2xz,\\
Q_2&=x^2+y^2+2xz, &Q_3&=4x^2+6y^2+4xz-8z^2.
\end{aligned}
\]
The identities \(Q_1-Q_0=(x+z)^2\), \(Q_1-Q_2=x^2\), \(6Q_2-Q_3=2(x+2z)^2\), and \(6Q_0-Q_3=2(x-z)^2\) prove exact fourfold contacts at \([-1:0:1]\), \([0:0:1]\), \([-2:0:1]\), \([1:0:1]\), respectively. Each conic is smooth. The two other pairs have exactly four transverse intersections each: \(Q_0-Q_2=-z(z+2x)\) gives two points at \(z=0\) and two at \(z=-2x\), while \(Q_3-2Q_1=4(y^2-2z^2)\) gives two on each line \(y=\pm\sqrt2z\). These eight points are all distinct and lie away from the four contacts. There are no triple intersections: \(Q_1=Q_2=0\) forces \(x=y=0\), when neither \(Q_0\) nor \(Q_3\) vanishes; \(Q_0=Q_1=0\) forces \(x=-z,y=0\), when \(Q_3=-8z^2\ne0\); and \(Q_0=Q_2=Q_3=0\) would force \(z(z+2x)=0\) and \(x+2z=0\), hence \(x=z=0\), contrary to \(Q_0=0\). Hence the singularity vector is \((8,0,0,0,4)\) and \(\tau=8+4\cdot7=36\). The reproducible exact coefficient-linear-algebra check below gives \(\operatorname{mdr}(Q_0Q_1Q_2Q_3)=3\), including the exclusion of syzygies in degrees zero, one, two. Since \(36=7^2-3(8-3-1)-1\), the near-free criterion applies.

## Verification
Run `python verify_conic_cutoff.py` (Python 3 standard library) for the exhaustive integer necessary-condition census on \(5\le k\le8\). Run `python verify_four_conic_example.py` (SymPy) for the exact quadratic identities, projective smoothness tests, and the degree-by-degree Jacobian-syzygy calculation for the explicit octic. The expected success markers are `CONIC_CUTOFF_ARITHMETIC_PASS`, `FOUR_CONIC_INCIDENCE_PASS`, and `FOUR_CONIC_MDR_3_PASS [0, 0, 0, 1]`. The general nonexistence results are proved symbolically in Steps 1–4; enumeration is corroboration, not an argument over infinitely many arrangements.

## Relationship to prior work
Zieliński [1] proved the orbifold inequality used here. Pokora [2] proved the coarse nearly free upper bound of eight conics and explicitly noted the absence of known examples with five through eight conics; an existing four-conic nearly free construction motivates sharpness of the last clause. The results here concern the simultaneous application of the near-free Tjurina identity, the orbifold inequality, an integer integrality obstruction at seven conics, and the combinatorial structure of the five-conic boundary. They exclude seven and eight conics rather than merely searching for them, eliminate the no-triples six-conic case, and isolate a single hypothetical five-conic incidence profile and its contact graph. Bromboszcz, Jarosławski and Pokora [3] examine plus-one-generated arrangements and prove another general arrangement inequality; their principal conclusions do not classify this nearly free upper boundary.

## Limitations
The universal bound six is not proved sharp. No six-conic near-free example is claimed. The unique five-conic numerical profile is **necessary only**, not an existence or realization theorem. The only sharpness statement here is for arrangements whose singularities belong to \(\{A_1,A_7\}\). The cited external theorems, particularly the near-free characterization and orbifold inequality, are mathematical premises; verification scripts check the new reductions and explicit finite witnesses, not all published foundational proofs. Priority remains subject to independently checking older unindexed treatments of the same near-free constraints.

## References
[1] M. Zieliński, *On plane conic arrangements with \(A_5\) and \(A_7\) singularities*, Rendiconti del Circolo Matematico di Palermo, first published 17 May 2023, DOI 10.1007/s12215-023-00890-8. Theorem 1.1.

[2] P. Pokora, *On free and nearly free arrangements of conics admitting certain ADE singularities*, arXiv:2303.08584 (15 March 2023), and Annali dell'Università di Ferrara, DOI 10.1007/s11565-023-00481-6 (27 November 2023). Definition 1.3, Theorem 2.3 and Remark 2.7.

[3] A. Bromboszcz, B. Jarosławski, P. Pokora, *On plus–one generated arrangements of plane conics*, Geometriae Dedicata (21 January 2026), DOI 10.1007/s10711-025-01063-w, Theorem 3.4.
