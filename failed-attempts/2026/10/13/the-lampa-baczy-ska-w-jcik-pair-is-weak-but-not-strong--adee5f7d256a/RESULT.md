# The Lampa–Baczyńska–Wójcik pair is weak but not strong
## Finding
Let \(\mathcal{CL}_1,\mathcal{CL}_2\subset\mathbb P^2_\mathbb C\) be the two arrangements introduced by Lampa–Baczyńska and Wójcik. They have the same published weak combinatorics \((6,1;6,3,2)\) and different minimal Jacobian-relation degrees, but their stronger degree-coloured incidence data are not equivalent.

For their common unique conic
\[
C:\;x^2+y^2-25z^2=0,
\]
the numbers of incident ordinary double, triple, and quadruple singular points are
\[
(n_2(C),n_3(C),n_4(C))=(4,1,2)\quad\text{for }\mathcal{CL}_1,
\]
and
\[
(n_2(C),n_3(C),n_4(C))=(2,2,2)\quad\text{for }\mathcal{CL}_2.
\]
The component singular-point counts are correspondingly
\[
\mathcal{CL}_1:\;r_3=3,\;r_4=2,\;r_5=1,\;r_7=1,
\]
whereas
\[
\mathcal{CL}_2:\;r_3=3,\;r_4=2,\;r_6=2.
\]
Therefore \(W_{\mathcal{CL}_1}\not\simeq W_{\mathcal{CL}_2}\). In the terminology in which a strong Ziegler pair must have equivalent \(W_C\), the published pair is weak but not strong.

## Assumptions and scope
The ground field is \(\mathbb C\), although all defining equations and the incidence calculation are rational. The arrangements are exactly
\[
Q_1=(x^2+y^2-25z^2)(x-4z)(x+4z)(3x+4y)(x+3z)(6x+y+21z)(y+3z)
\]
and
\[
Q_2=(x^2+y^2-25z^2)(x+4z)x(x-4z)(y-3z)(y+3z)(3x-4y).
\]
Only the strengthened combinatorial classification of this particular pair is claimed. The published facts that the weak combinatorics is \((6,1;6,3,2)\), that both arrangements are nearly free, and that their minimal Jacobian-relation degrees are \(4\) and \(3\) are inputs from the lead source, not new claims here.

## Proof
Write the six line factors of \(Q_1\) as \(L_1,\ldots,L_6\). Exact projective intersection gives the following multiple line-intersection points. Three lines meet at \([0:1:0]\) and \([3:3:-1]\), both off \(C\). The points \([4:-3:-1]\) and \([4:-3:1]\) lie on \(C\) and each carry three lines, hence become ordinary quadruple points of the full conic-line arrangement. The point \([4:3:-1]\) lies on \(C\) and carries two lines, hence is an ordinary triple point. The remaining line-line intersections \([4:-45:1]\) and \([12:-9:-4]\) are nodes off \(C\).

For \(Q_2\), three lines meet at \([0:1:0]\) off \(C\). The points \([4:3:-1]\) and \([4:3:1]\) lie on \(C\) and each carry three lines, hence are ordinary quadruple points. The points \([4:-3:-1]\) and \([4:-3:1]\) lie on \(C\) and each carry two lines, hence are ordinary triple points. Four further line-line intersections are ordinary nodes off \(C\).

For a line \(ax+by+cz=0\), tangency to \(C\) is equivalent to \(25a^2+25b^2-c^2=0\). The exact values for the six lines are respectively
\[
(9,9,625,16,484,16)
\]
for \(Q_1\), and
\[
(9,25,9,16,16,625)
\]
for \(Q_2\). Thus every line meets the smooth conic transversely in two points. Bézout therefore supplies twelve line-conic incidences in each arrangement. In \(Q_1\), the two quadruple points use six of these incidences and the one conic triple point uses two, leaving four transverse conic-line nodes. In \(Q_2\), the two quadruple points use six incidences and the two conic triple points use four, leaving two transverse conic-line nodes. This proves the conic profiles \((4,1,2)\) and \((2,2,2)\), while recovering the common global counts \(t_2=6,t_3=3,t_4=2\).

Counting distinct singular points on each component gives line counts \((4,3,3,5,4,3)\) and conic count \(7\) for \(Q_1\), versus line counts \((3,6,3,4,4,3)\) and conic count \(6\) for \(Q_2\). Hence their sequences \(\mathbf r\) differ. The modern combinatorial type \(W_C\) contains the degree map, the incidence map, singularity types, and \(\mathbf r\), so no degree-preserving combinatorial equivalence can identify the two arrangements. In particular the unique degree-two component alone already gives an obstruction.

## Verification
The standalone verifier `artifacts/verify.py` uses integer projective arithmetic only. It enumerates every pairwise line intersection, reconstructs every line-concurrency class, evaluates the conic at those points, verifies the non-tangency criterion for all twelve line occurrences, derives the residual conic-line nodes by Bézout, and checks both the global weak counts and the stronger component-incidence counts. Its expected terminal marker is `VERIFY_OK`.

## Relationship to prior work
Lampa–Baczyńska and Wójcik introduced this pair and proved that both arrangements have weak combinatorics \((6,1;6,3,2)\) while their minimal Jacobian-relation degrees are \(4\) and \(3\). Their article frames the example only as a weak Ziegler pair.

Later work makes the distinction needed here explicit: the combinatorial type \(W_C\) records irreducible-component degrees, singularity types, the component-incidence relation, and the sequence \(r_j\); a strong Ziegler pair requires equivalent \(W_C\) but different Jacobian-syzygy modules. The calculation above places the earlier example on the weak side of this later boundary for a concrete reason: the unique conic has a different incidence profile, and even \(\mathbf r\) differs.

Targeted searches for the exact equations, their conic-incidence profiles, and a strong-combinatorics classification did not locate this statement. This is evidence of non-coverage, not a proof that no equivalent observation exists under different terminology.

## Limitations
No claim is made about the full moduli space of realizations with weak combinatorics \((6,1;6,3,2)\), nor about whether some other realization pair with those weak counts can form a strong Ziegler pair. The originality comparison is limited by ordinary indexing and terminology risk: an equivalent incidence observation could exist in an unindexed note or in a source using different language. The proof classifies only the two displayed arrangements.

## References
1. M. Lampa–Baczyńska and D. Wójcik, *Weak Ziegler pairs of conic-line arrangements with ordinary singularities*, arXiv:2403.16870v1, first public 2024-03-25; Bulletin Polish Acad. Sci. Math. 73 (2025), 19–23, DOI 10.4064/ba240508-29-8.
2. A. Bromboszcz, B. Jarosławski and P. Pokora, *On plus–one generated arrangements of plane conics*, Geometriae Dedicata 220 (2026), article 10, DOI 10.1007/s10711-025-01063-w; see Definitions 2.13–2.15 and 5.1–5.2.
3. M. Cuntz and P. Pokora, *Singular plane curves: freeness and combinatorics*, arXiv:2403.13377.
