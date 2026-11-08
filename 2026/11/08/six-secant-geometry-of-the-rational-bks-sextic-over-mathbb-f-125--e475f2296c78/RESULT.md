# Six-secant geometry of the rational BKS sextic over \(\mathbb F_{125}\)

## Finding
Let \(K=\mathbb F_{125}\) and let \(C\subset\mathbb P^2_K\) be the rational Borges–Korchmáros–Speziali (BKS) sextic with homogeneous equation
\[
F(X,Y,Z)=Y^6-X^5Z-XZ^5+(Y^2-2XZ)^3=0.
\]
Write \(\Omega=C(K)\). For a \(K\)-rational line \(L\), set \(w(L)=\#(L(K)\cap\Omega)\). Then \(\#\Omega=136\), and the **complete rational-line weight spectrum** is
\[
\begin{array}{c|rrrrrrr}
w(L)&0&1&2&3&4&5&6\\\hline
\#L&5940&3606&5460&610&15&0&120.
\end{array}
\]
In particular, there are exactly \(120\) six-secants. For any point \(P\in\mathbb P^2(K)\), put \(s(P)=\#\{L:w(L)=6,\ P\in L\}\). Its complete distribution is
\[
\begin{array}{c|rrrr}
s(P)&0&1&2&6\\\hline
\#P&6571&3720&5340&120.
\end{array}
\]
Restricted to points of \(\Omega\), the counts are \(16\) at \(s=0\) and \(120\) at \(s=6\); restricted to exterior points, the counts are \(6555\) at \(s=0\), \(3720\) at \(s=1\), and \(5340\) at \(s=2\). The sixteen curve points uncovered by six-secants are exactly \(C(\mathbb F_5)\). Thus \(\Omega\) is an **incomplete** \((136,6)\)-arc in \(\operatorname{PG}(2,125)\), with exactly \(6555\) external points that can be adjoined individually without creating a seven-point line.

The \(120\) six-secant lines are incident with exactly \(120\) sixfold points, all on \(C\), and exactly \(5340\) ordinary double intersections off \(C\); no three distinct six-secants concur at an exterior point. Here “sixfold” and “double” refer to the *line configuration*, not singularities of the sextic.

## Assumptions and scope
Everything is over the field \(K=\mathbb F_{5^3}\); no assertion is made for a different extension degree or characteristic. Projective points and lines are considered over \(K\); the sextic is the degree-six specialization of the established rational BKS plane curve. A rational line is called an \(i\)-secant if it contains exactly \(i\) **distinct** points of \(\Omega\). The curve is singular, and intersection multiplicities with the curve are not substituted for the above distinct-point counts. An arc is complete precisely if every exterior projective point lies on a six-secant. The finite enumerations below concern **all** \(15751\) projective points and **all** \(15751\) projective lines, not a sample.

## Proof
**Exact field model.** Set \(K=\mathbb F_5[t]/(t^3+t+1)\). The cubic has no root in \(\mathbb F_5\), hence is irreducible. Every field element is represented uniquely by a triple of base-five digits \((a_0,a_1,a_2)\). Perform addition componentwise modulo five and multiplication by polynomial convolution followed by the relation \(t^3=-t-1\). This gives a completely specified integer algorithm for exact field arithmetic. The first standalone verifier constructs every multiplication-table entry explicitly and checks \(a^{124}=1\) for each nonzero field element.

**Exhaustive rational-point and line enumeration.** Every projective point has exactly one of the following normalized representatives:
\[
(1,u,v),\ u,v\in K;\qquad (0,1,v),\ v\in K;\qquad (0,0,1).
\]
The same normalized triples represent each projective *dual* line, whose equation is \(aX+bY+cZ=0\). Thus there are exactly \(125^2+125+1=15751\) triples of either type. Evaluate the displayed homogeneous polynomial \(F\) at every normalized point, obtaining exactly \(136\) zeros. For each of the \(15751\) line triples \(L=(a,b,c)\), count the \(136\) points \(P=(x,y,z)\) for which \(ax+by+cz=0\) in \(K\). The complete resulting histogram is the seven-entry array in the finding. The two independent incidence identities
\[
\sum_L w(L)=136\cdot126=17136,\qquad
\sum_L\binom{w(L)}2=\binom{136}{2}=9180
\]
are checked exactly. The second identity is valid because any distinct two projective points determine a unique rational line.

**Every point's six-secant multiplicity.** Retain the \(120\) line triples whose weights equal six. For each of the same \(15751\) point triples count its incident retained lines. This yields the four-entry overall distribution displayed above and, after partitioning according to \(F(P)=0\), the separate on-curve and exterior distributions. Taking fifth powers in \(K\) gives a direct membership test for the embedded \(\mathbb F_5\)-subplane, and enumeration proves that the \(16\) curve points with \(s(P)=0\) are precisely the \(16\) curve points in that subplane.

**Line-configuration consequence.** By the computed spectrum, the only nonzero line-configuration multiplicities are \(1,2,6\). The \(120\) points at multiplicity six are on the sextic, and the \(5340\) multiplicity-two points are external. Every pair of the distinct six-secant lines meets once; consistency is independently confirmed by
\[
120\binom62+5340\binom22=7140=\binom{120}{2}.
\]
There are therefore no exterior points on three or more six-secants. Since \(6555\) exterior points have \(s(P)=0\), the arc is not complete.

**Independent arithmetic and incidence route.** The second verifier instead represents \(K\) as \(\mathbb F_5[u]/(u^3+u+4)\), another irreducible cubic. It obtains candidate six-secants only as normalized cross products of *pairs* of curve points, instead of scanning every dual line. Any six-secant contains such a pair, so this is exhaustive. Normalization uses the exact inverse \(a^{123}\) for each nonzero \(a\). This independently produces the same \(120\) lines and complete point-incidence distribution. These verifiers use no external algebra package and contain all field arithmetic and exhaustive loops.

## Verification
Run \(\texttt{python3 verify_direct.py}\) and \(\texttt{python3 verify_pairlines.py}\) in the same directory. Both terminate with named `PASS` assertions and independently check \(\#\Omega=136\), the complete six-secant incidence distribution, and \(6555\) exterior uncovered points. The first additionally checks the complete rational-line weight histogram and both global point-pair identities; the second checks normalized lines generated by all \(\binom{136}{2}\) point pairs in a different field representation. Exact arithmetic exhausts every finite case required for the theorem; no inference from a proper subsample or unverified random experiment is made.

## Relationship to prior work
Borges, Korchmáros and Speziali introduced and investigated the rational BKS curve, its automorphisms, and its singularities. Korchmáros, Nagy and Szőnyi (first public 20 February 2023), particularly Sections 4.2, 7.2, and 8.2, established general line-character and on-curve six-secant principles and explicitly left the small extension exponent \(r=3\) for the rational BKS curve open in the completeness problem. Their Theorem 7.5 addresses \(r\ge5\), so it does not imply the exterior six-secant multiplicity census at \((q,r)=(5,3)\). Their Theorem 8.2 already describes the on-curve uncovered locus; no novelty is claimed for that fact alone. The new claims here are the complete \(\mathbb F_{125}\) line-weight histogram, exact global and exterior six-secant multiplicities, and their line-arrangement consequence.

## Limitations
The result is a finite-field case classification, not a theorem for all \(q\) or for all exponent-three BKS curves. The set of \(6555\) external uncovered points is counted and its incidence profile determined, but it is not classified into automorphism orbits. The theorem does not assert that adding all uncovered points simultaneously preserves the arc property; each such point can be added separately. The independent historical-priority and mathematical audit has not yet been performed.

## References
1. H. Borges, G. Korchmáros, P. Speziali, *Plane curves with a large linear automorphism group in characteristic p*, first public 11 February 2022, arXiv:2202.05765, especially Proposition 4.24. https://arxiv.org/abs/2202.05765
2. G. Korchmáros, G. P. Nagy, T. Szőnyi, *Algebraic approach to the completeness problem for (k,n)-arcs in planes over finite fields*, first public 20 February 2023, arXiv:2302.10162; J. Combin. Theory Ser. A 204 (2024), 105851. https://arxiv.org/abs/2302.10162 ; open-access full text https://publicatio.bibl.u-szeged.hu/29111/1/KorchmarosNagySzonyiAlgebraicapproachtothecompletenessproblemforkn-arcsinplanesoverfinitefields.pdf
