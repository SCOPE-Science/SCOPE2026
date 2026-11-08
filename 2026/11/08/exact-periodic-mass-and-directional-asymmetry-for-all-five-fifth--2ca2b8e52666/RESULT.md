# Exact periodic mass and directional asymmetry for all five fifth-rotated odometers

## Finding
Write \(I=[0,1)\), and let \(a:I\to I\) be the von Neumann–Kakutani interval exchange
\[
a(x)=x-1+3\cdot 2^{-n},\qquad 1-2^{1-n}\le x<1-2^{-n},\quad n\ge1.
\]
For \(k\in\{0,1,2,3,4\}\), set \(F_k(x)=a((x+k/5)\bmod1)\). Then the set of periodic points is empty for \(k=0,1,3\). For \(k=2\) the periodic set is precisely the following five half-open intervals:
\[
P_2=[1/8,7/40)\cup[1/5,1/4)\cup[11/40,13/40)\cup[7/20,2/5)\cup[17/40,19/40).
\]
For \(k=4\), it is precisely
\[
P_4=[1/4,7/20)\cup[2/5,1/2)\cup[11/20,13/20)\cup[7/10,4/5)\cup[17/20,19/20).
\]
Every point in either set has **least period exactly five**. Thus their Lebesgue measures across the five rotations are exactly
\[
(\lambda(P_0),\ldots,\lambda(P_4))=(0,0,1/4,0,1/2).
\]
In particular the dynamics of a rotation by \(2/5\) and the inverse rotation by \(3/5\) have sharply different periodic support, and the inverse rotation by \(4/5\) has twice the periodic mass of the rotation by \(2/5\).

## Assumptions and scope
The fractional part uses the half-open convention \([0,1)\), so all endpoint claims include the displayed left endpoints and exclude their right endpoints. The classification is global for every real initial point in \(I\), not merely almost everywhere. The family consists of all five cyclic translations of the five equal subintervals, not of all \(120\) permutations.

## Proof
For any one-line permutation \(p=(p_0,\ldots,p_4)\) of \(\{0,\ldots,4\}\), let \(G_p=a\circ R_p\), where \(R_p\) translates the fifth \([i/5,(i+1)/5)\) onto \([p_i/5,(p_i+1)/5)\). Put \(C_j=[j/40,(j+1)/40)\), \(0\le j<40\), and \(J=[0,1/8)=\bigcup_{j=0}^{4}C_j\). The finite-cell rule below is exact and includes all endpoints.

For a cell label \(j\), write \(i=\lfloor j/8\rfloor\) and \(r=8p_i+(j\bmod8)\). If \(0\le r<20\), then \(G_p(C_j)=C_{r+20}\); if \(20\le r<30\), then \(G_p(C_j)=C_{r-10}\); if \(30\le r<35\), then \(G_p(C_j)=C_{r-25}\). In these cases the action is a translation. If \(35\le r<40\), the entire cell goes into \(J\), and the return action on that cell is a rescaled copy of \(a\):
\[
a(7/8+u/8)=a(u)/8,\qquad 0\le u<1.
\]
This identity follows on every dyadic branch by substituting the formula defining \(a\). Thus all first-return and omission claims reduce to a graph on exactly forty labelled cells.

Start from each of the five cells \(C_0,\ldots,C_4\), follow the translation arrows until the next arrow enters \(J\), and record its length \(h_i\), the terminal \(r-35\) label \(p'_i\), and the omitted cell labels. The exact finite calculation gives these rows (permutations are written in one-line notation):

| \(p\) | \((h_0,\ldots,h_4)\) | induced \(p'\) | omitted cells |\n|:--|:--|:--|--:|\n| 01234 | 8,8,8,8,8 | 01234 | 0 |\n| 12340 | 2,2,2,2,32 | 12340 | 0 |\n| 23401 | 6,6,6,6,6 | 12340 | 10 |\n| 34012 | 2,2,20,8,8 | 34201 | 0 |\n| 34201 | 2,2,20,8,8 | 34201 | 0 |\n| 40123 | 2,8,8,1,1 | 42301 | 20 |\n| 42301 | 2,18,18,1,1 | 42301 | 0 |\n
Each row can be reproduced from the preceding three-case integer rule without floating-point approximations. The independently executable `certificate5.py` exhausts these cell paths and verifies all omissions, terminal labels and cycles.

The return map to \(J\) is exactly \(G_{p'}\) under the scaling \(x\mapsto8x\): this follows from the last displayed tail-scaling identity and the terminal labels. When a row has no omitted cells, every cell of \(I\) lies in the finite tower over \(J\). For \(p\in\{01234,12340,34201,42301\}\), the induced permutation equals \(p\) itself and the tower is complete. Renormalizing repeatedly, every orbit enters \([0,8^{-m})\) for each integer \(m\ge1\). No point can be periodic: a finite periodic orbit approaching zero would have to contain zero, but zero is not in the range of \(G_p\), because \(a(I)=(0,1)\). (This argument also covers interval endpoints exactly.)

For the first-stage rotations \(p=23401\) and \(p=40123\), the induced permutations are respectively \(12340\) and \(42301\), both just proved aperiodic. Thus the entire tower over \(J\) contains no periodic points. Its complement consists exactly of the omitted cells: ten in the former case and twenty in the latter. Applying the same integer rule, the omitted cells split into respectively two and four directed cycles of length five; adjacent cells merge to give the five stated intervals. There are no omitted cycles of other lengths, proving the global classification. All intervals in each five-cycle are permuted by translations, so the return after five iterations is the identity there; disjointness of their supports makes the least period exactly five. Their lengths sum to \(10/40=1/4\) and \(20/40=1/2\), respectively.

## Verification
Run `python3 certificate5.py` using only the Python standard library. Its exact integer graph computes every gate transition for all seven necessary first-return rows, checks disjointness and exhaustiveness of the towers and omitted cells, and traces every omitted cycle. In addition, rational point checks at interior representatives confirm the rescaled induced maps and exclude early returns; those finite numerical checks are supplementary, not the proof of the infinite statement. The infinite conclusion uses the exact tail-scaling identity and the stationary first-return renormalization.

## Relationship to prior work
Bruin and Lukina introduced rotated odometers and proved their general first-return structure. Their 2023 *Rotated odometers*, Proposition 5.11 and Example 5.21, already establish that the \(2/5\)-rotation first return is the \(1/5\)-rotation and that its first return is non-covering; these facts and their general procedure are credited. The new claim is the simultaneous **complete explicit census for all five cyclic fifth-rotations**, including the \(4/5\) periodic mass \(1/2\), the asymmetric \(3/5\) aperiodicity and all exact periodic interval endpoints. Their separate treatment of dyadic subdivisions does not cover fifths. A related explicit three-interval census concerns a different family and does not imply this five-rotation classification.

## Limitations
This result concerns only the five rotations by integer multiples of \(1/5\), and does not classify other permutations of five pieces or arbitrary denominators. It gives the periodic set and least periods, not all spectral invariants of the aperiodic components. It has undergone self-review but no independent mathematical audit. Searches cannot rule out independently discovered equivalent formulas in unindexed work.

## References
1. H. Bruin and O. Lukina, *Rotated Odometers and Actions on Rooted Trees*, first posted 2021-04-12, arXiv:2104.05420 (for the definition of general rotated odometers and dyadic comparison).
2. H. Bruin and O. Lukina, *Rotated odometers*, Journal of the London Mathematical Society 107 (2023), 1983–2024, doi:10.1112/jlms.12731. In particular Proposition 5.11, Example 5.21, and Section 8.3 (for the non-covering quarter-mass precedent and renormalization).
