# Twenty-four forbidden supports and 6,656 Zariski chambers on the four-torsion extremal elliptic surface

## Finding
Let \(X\) be the complex extremal rational elliptic surface with singular fibers \(I_8+I_2+I_1+I_1\), which is unique up to the standard classification and has Mordell--Weil group \(\mathbb Z/4\mathbb Z\). Its Zariski-chamber support polynomial is
\[
Z_X(t)=1+14t+90t^2+346t^3+875t^4+1508t^5+1768t^6+1352t^7+600t^8+102t^9.
\]
Thus \(Z_X(1)=6656\), and the maximal negative support has nine curves, occurring for exactly \(102\) chambers. There are exactly \(24\) minimal forbidden supports, and a subset of negative curves supports a chamber if and only if it contains none of them.

## Assumptions and scope
Work over \(\mathbb C\) with the smooth relatively minimal elliptic surface and zero section. Label the eight irreducible \((-2)\)-curves in the \(I_8\) fiber cyclically \(C_0,\ldots,C_7\). Let \(D_0,D_1\) be the two \((-2)\)-components of the \(I_2\) fiber. Label the four \((-1)\)-sections \(S_0,\ldots,S_3\) by the cyclic Mordell--Weil group, with \(S_0\) the identity. Indices on \(C_i\) are modulo eight; on \(S_j\), modulo four. All section pairs are disjoint. The only intersections between distinct negative curves are
\[
C_i\cdot C_{i+1}=1,\quad D_0\cdot D_1=2,\quad S_j\cdot C_{2j}=1,\quad S_j\cdot D_{j\bmod2}=1.
\]
All fiber components have self-intersection \(-2\), sections self-intersection \(-1\). The other two singular fibers are irreducible and contribute no negative curves. The empty support is the nef chamber.

## Proof
**Exhaustion.** Write \(F\) for a general elliptic fiber. Since \(K_X=-F\) and \(F\) is nef, adjunction yields \(E^2=2p_a(E)-2+F\cdot E\) for any irreducible curve \(E\). Therefore a negative irreducible curve must be a vertical \((-2)\)-curve or a section of self-intersection \(-1\). The fiber classification and the order-four Mordell--Weil group give precisely the stated ten vertical components and four sections.

**Section incidence.** By the torsion-height identity, for an order-four section meeting component \(i\) in the \(I_8\) fiber and component \(j\) in the \(I_2\) fiber, \(0=2+2(S\cdot S_0)-i(8-i)/8-j(2-j)/2\). For a nonidentity order-four section the component-group order and the height equality force \(i=2\) or \(6\), \(j=1\), and \(S\cdot S_0=0\). Its double meets \((i,j)=(4,0)\). The bilinear height formula \(0=1+S\cdot S_0+T\cdot S_0-S\cdot T-\sum_v\operatorname{contr}_v(S,T)\) then shows all three distinct nonzero torsion sections are pairwise disjoint: their correction sums are one. This proves the specified intersection matrix.

**Finite classification.** Order the negative curves as \(C_0,\ldots,C_7,D_0,D_1,S_0,\ldots,S_3\). Form the symmetric integer matrix \(A\), the negative of their intersection matrix. Its diagonal entries are two on fiber components, one on sections; its off-diagonal entries are minus the displayed intersection numbers. For each of the \(2^{14}=16384\) subsets, test whether the corresponding principal matrix is positive definite using exact rational Schur complements. Its complement gives the supports of Zariski chambers by Bauer--Funke--Neumann Proposition 1.1. There are precisely \(24\) inclusion-minimal failed subsets:

- \(8: C_0,C_1,C_2,C_3,C_4,C_5,C_6,C_7\)
- \(2: D_0,D_1\)
- \(4: C_0,C_1,C_7,S_0\)
- \(3: C_0,D_0,S_0\)
- \(4: C_1,C_2,C_3,S_1\)
- \(3: C_2,D_1,S_1\)
- \(5: C_0,C_1,C_2,S_0,S_1\)
- \(9: C_0,C_2,C_3,C_4,C_5,C_6,C_7,S_0,S_1\)
- \(4: C_3,C_4,C_5,S_2\)
- \(3: C_4,D_0,S_2\)
- \(7: C_0,C_1,C_2,C_3,C_4,S_0,S_2\)
- \(7: C_0,C_4,C_5,C_6,C_7,S_0,S_2\)
- \(3: D_0,S_0,S_2\)
- \(5: C_2,C_3,C_4,S_1,S_2\)
- \(9: C_0,C_1,C_2,C_4,C_5,C_6,C_7,S_1,S_2\)
- \(4: C_5,C_6,C_7,S_3\)
- \(3: C_6,D_1,S_3\)
- \(9: C_0,C_1,C_2,C_3,C_4,C_5,C_6,S_0,S_3\)
- \(5: C_0,C_6,C_7,S_0,S_3\)
- \(7: C_2,C_3,C_4,C_5,C_6,S_1,S_3\)
- \(7: C_0,C_1,C_2,C_6,C_7,S_1,S_3\)
- \(3: D_1,S_1,S_3\)
- \(5: C_4,C_5,C_6,S_2,S_3\)
- \(9: C_0,C_1,C_2,C_3,C_4,C_6,C_7,S_2,S_3\)

Every failed subset contains a minimal failed subset because the family is finite and positive definiteness passes to principal submatrices. Conversely, no positive-definite set contains any failed principal submatrix. Thus avoidance of those \(24\) explicit supports is equivalent to being a chamber support.

The exact cardinality distribution of the positive-definite subsets, independently recomputed by inclusion--exclusion on the \(24\) forbidden supports, is
\[
(1,14,90,346,875,1508,1768,1352,600,102,0,0,0,0,0).
\]
The entry indexed \(k\) counts supports of size \(k\), proving the polynomial and its consequences.

## Verification
Run `python3 verify.py` (Python standard library only). It constructs \(A\) directly from the stated geometry; tests all \(16384\) principal submatrices by exact rational elimination; extracts every minimal obstruction; independently obtains the polynomial via the finite inclusion--exclusion identity
\[
Z_X(t)=\sum_{T\subseteq\mathcal O}(-1)^{|T|}t^{|\bigcup T|}(1+t)^{14-|\bigcup T|},
\]
where \(\mathcal O\) is the set of \(24\) minimal obstructions. Dynamic programming on union masks evaluates this identity exactly. It checks the \(24\)-obstruction count, all cardinality coefficients, the equivalence of support avoidance and positive definiteness, total \(6656\), and maximum-support count \(102\). The separately bundled verification output is from execution of that script.

## Relationship to prior work
Schütt and Shioda, *Elliptic Surfaces* (arXiv:0907.0298, first posted 2 July 2009), Section 9.5, list configuration \([1,1,2,8]\) with Mordell--Weil group \(\mathbb Z/4\mathbb Z\). Section 11 supplies the height pairing. These are prerequisites, not new results. Bauer, Funke, and Neumann (arXiv:0912.0958, Proposition 1.1) established the negative-definite support criterion and counted chambers for general-position del Pezzo surfaces. Bauer and Schmitz (arXiv:1204.4373) developed an improved general counting algorithm, primarily demonstrating it on the Segre--Schur quartic. Neither inspected paper tabulates the full \([1,1,2,8]\) intersection-graph forbidden supports or this evaluated polynomial. The result is a specific classification of chamber supports on the four-torsion surface, not a new general chamber-counting algorithm.

## Limitations
The statement concerns the complex surface with the given fiber configuration, and counts chambers by support cardinality, not their volumes or Weyl chambers. Historical priority is provisional: an unindexed calculation or a less-direct application of earlier enumeration literature might contain an equivalent polynomial. The finite exact computation is an exhaustive proof only because the negative-curve exhaustion and intersection matrix are established geometrically. No independent research audit has been performed.

## References
Schütt--Shioda, *Elliptic Surfaces*, arXiv:0907.0298 (initial submission 2009-07-02), https://arxiv.org/abs/0907.0298 .

Bauer--Funke--Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958 (2009-12-04), https://arxiv.org/abs/0912.0958 .

Bauer--Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373 (2012-04-19), https://arxiv.org/abs/1204.4373 .
