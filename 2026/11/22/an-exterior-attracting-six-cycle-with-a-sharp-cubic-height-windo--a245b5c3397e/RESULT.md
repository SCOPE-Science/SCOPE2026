# An exterior attracting six-cycle with a sharp cubic height window in farthest triangle projections

## Finding
Let \(Q_h\) be the triangle with vertices \((-1,0)\), \((1,0)\), and \((0,h)\), where \(h>0\). On the union \(X_h\) of its **three complete supporting lines**, use the farthest-orthogonal-projection rule: from a point on one supporting line, project onto each of the other two lines and choose the farther projection; a tie fixes the point. Count primitive period-six orbits once up to cyclic rotation. Put \(q=h^2\), and let \(\rho\) be the unique positive solution to \(\rho^3+\rho^2=1\), with \(3/4<\rho<4/5\).

The **complete least-period-six census** is
\[
N_6(h)=\begin{cases}
1,&\rho<h^2<1,\\
0,&\text{otherwise}.
\end{cases}
\]
The existing orbit is locally attracting, with exact sixth-return multiplier
\[
\mu_6=\frac{(q-1)^2}{(q+1)^4}.
\]
It has **exactly two points outside the closed triangle sides**, lying on inclined-side extensions beyond the apex. In particular the period-six orbit of the *complete-line map* cannot occur in the version restricted to the triangle perimeter. The strict window excludes both endpoints: they are tie collisions, not continued six-cycles. Reflection in the altitude takes the unique orbit to itself after a three-step phase shift.

## Assumptions and scope
Let \(L_0\) be the horizontal base line, oriented from \((-1,0)\) toward \((1,0)\); let \(L_1\) join \((-1,0)\) to \((0,h)\); let \(L_2\) join \((1,0)\) to \((0,h)\). **All lines are infinite.** Coordinates \(t\) on these lines use the affine parametrizations
\[
\ell_0(t)=(-1+2t,0),\quad
\ell_1(t)=(-1+t,ht),\quad
\ell_2(t)=(1-t,ht).
\]
At a vertex the farthest projection is unambiguous: the other incident line has zero distance and the third line has positive distance. A periodic orbit is *primitive of period six* if its six points are distinct. The statement does not classify other periods, global basins, or arbitrary nonisosceles triangles.

## Proof
**Projection coordinates and completeness of the itinerary list.** Ordinary Euclidean orthogonal projection from \(L_i\) to \(L_j\), expressed in these coordinates, is \(t\mapsto b_{ij}t+c_{ij}\), with
\[
\begin{array}{c|ccc}
&j=0&j=1&j=2\\ \hline
 i=0&-&2t/(q+1)&2(1-t)/(q+1)\\
 i=1&t/2&-&(q-1)t/(q+1)+2/(q+1)\\
 i=2&1-t/2&(q-1)t/(q+1)+2/(q+1)&-
\end{array}
\]
(the entries show the complete affine output). In Euclidean arclength coordinates, each projection between distinct supporting lines is a strict contraction: its signed slope is the dot product of the two unit tangents, whose absolute value is less than one since the lines are nonparallel. The displayed affine coordinates have different scales on the three lines; their individual slopes need not have modulus less than one, but those scale factors cancel in any return to the starting line. Thus every prescribed cyclic line word has a unique affine six-step fixed-point candidate. A genuine primitive six-cycle has consecutive different line labels, including across the closing step, and its cyclic line word cannot have a smaller period: if it did, the corresponding shorter affine return would be a strict contraction and could not support a proper multiple-period orbit. The same reasoning handles possible vertex visits by choosing each point's label as the line targeted by the preceding step. At a vertex either incident source label yields the same farthest choice.

Exactly nine primitive cyclic words of length six on the three labels satisfy these adjacency restrictions. Up to cyclic rotation **and** reflection \(L_1\leftrightarrow L_2\), their five representatives are
\[
010102,\quad010121,\quad010212,\quad012021,\quad012121.
\]
For a word \(w=(w_0,\ldots,w_5)\), let \(p_j\) be its unique fixed-itinerary six-point candidate and define the signed switching gap
\[
G_j=\|p_j-\pi_{w_{j+1}}p_j\|^2-\|p_j-\pi_k p_j\|^2,
\]
where \(k\) is the third line label, not equal to \(w_j\) or \(w_{j+1}\). The word is a real orbit exactly if **all six** gaps are positive. Every denominator in the formulas below is strictly positive for \(q>0\).

**Four impossible reflection classes.** Directly composing the affine projections and comparing squared distances gives the following decisive switching gaps, indexed from zero:

For \(010102\),
\[
G_2=-\frac{4q(q^2+q+1)}{(q+1)(q^2+3q+3)}<0.
\]
For \(010121\),
\[
G_0=-\frac{4q(q-1)^2(q+2)}{(q+1)(q+3)(q^2+q+2)}\le0.
\]
For \(012121\),
\[
G_0=-\frac{4q(q-1)^4}{(q+1)(q^4+4q^3+14q^2+4q+9)}\le0.
\]
For \(010212\), set
\[
P(q)=q^6+3q^5+13q^4+14q^3+19q^2-9q-9,
\quad B(q)=q^3-q^2-q-3.
\]
Two of its gaps are
\[
G_1=-\frac{4qP(q)}{(q+1)(q+3)^2(q^2+q+2)^2},\quad
G_3=\frac{4q(q^2+3q+3)B(q)}{(q+3)^2(q^2+q+2)^2}.
\]
For \(0<q\le2\), \(B(q)<0\): it decreases to \(q=1\) and then increases, but its endpoint values \(B(0)=-3\) and \(B(2)=-1\) are negative. For \(q\ge2\), \(P(q)>0\), because its positive-degree terms are nonnegative and \(19q^2-9q-9>0\). Therefore at least one of these two gaps is negative for every \(q>0\). Reflection eliminates the remaining four cyclic words, leaving only \(012021\).

**Sharp existence of the remaining six-cycle.** Write \(D=q^2+q+2\). The unique fixed-itinerary orbit of the word \(012021\), in successive \(L_0,L_1,L_2,L_0,L_2,L_1\) coordinates, is
\[
(t_0,t_1,t_2,t_3,t_4,t_5)
=\frac1D(q+1,\ 2,\ 2(q+1),\ q^2+1,\ 2,\ 2(q+1)).
\]
Its six gaps occur twice each, in the order \((A,B,C,A,B,C)\), where
\[
\begin{aligned}
A&=\frac{4q^2(1-q)}{(q+1)D},\\
B&=\frac{4q(q^3+q^2-1)}{D^2},\\
C&=\frac{4q(-q^4+3q^3+2q^2+3q+1)}{(q+1)D^2}.
\end{aligned}
\]
Here \(A>0\) exactly when \(q<1\); \(B>0\) exactly when \(q>\rho\), since \(q^3+q^2-1\) is strictly increasing on \((0,\infty)\), is negative at \(3/4\), and positive at \(4/5\). For \(0<q<1\), the numerator of \(C\) is positive because \(q^3(3-q)+2q^2+3q+1>0\). Hence all six strict switching tests hold **exactly** on \(\rho<q<1\), and equality at either endpoint makes at least one point fixed. The symbolic word is not a shorter-period repetition. Its listed coordinates lie strictly inside the corresponding line segments at indices \(0,1,3,4\), and strictly beyond the apex at indices \(2,5\), so all six points are distinct. Consequently the unique candidate gives one genuine primitive six-cycle, and no other one exists at any \(q>0\).

**Attraction and exteriority.** Multiplying the six affine projection slopes gives \(\mu_6=(q-1)^2/(q+1)^4\in(0,1)\) on the existence interval. All switching gaps are strict, so the fixed-itinerary return applies on a neighborhood and the cycle is locally attracting. Moreover
\[
\frac{2(q+1)}D>1\quad\Longleftrightarrow\quad 0<q<1.
\]
These are exactly the side parameters at steps two and five. Both projected points lie above the apex on their complete supporting lines, making the difference between whole-line and perimeter-restricted dynamics mathematically essential. Reflection switches the two inclined labels and maps \(012021\) to a cyclic shift of itself, proving the asserted phase symmetry.

## Verification
The accompanying standalone `checker.py` uses SymPy to independently form all six orthogonal-projector coordinate maps from the vertices, enumerate all nine primitive cyclic six-letter words, verify the five reflection classes, solve each affine fixed-point equation, and verify every decisive gap identity and the exact return multiplier. It also checks exact rational parameter samples. Running `python checker.py` prints `PASS: 9 cyclic primitive words...` and the numerical approximation of the positive root for diagnostic purposes. The **global** inequality arguments are in the proof above; checking a finite list of parameter samples is not a proof for all positive parameters.

## Relationship to prior work
Samuel Everett's *A Piecewise Contractive Map on Triangles* introduces the farthest orthogonal-projection map on three **complete lines** and proves qualitative periodic convergence. Its Section 4 deliberately restricts the bifurcation discussion to the **bounded triangle boundary**; the exterior six-cycle here is therefore not captured by those boundary diagrams. The author's complete freely accessible manuscript (arXiv `2408.16019`) was read together with the publisher's first-publication metadata (January 7, 2021).

Previously published exact same-map classifications cover primitive periods three, four and five separately, and a multistability theorem establishes selected period-eight itineraries. Those claims do not imply a complete period-six count, its cubic threshold, or the fact that its only cycle has two exterior points. The known attracting four-cycle exists throughout the new six-cycle window, so an additional attracting period occurs there; that four-cycle is prior work, not a second new discovery. Exact general-period identities, unindexed work, and inaccessible historical sources remain possible originality risks.

## Limitations
The theorem concerns a fixed isosceles shape family, complete Euclidean supporting lines, strict farthest-branch decisions and the tie-as-fixed convention. It does not classify periods other than six, all basins, or invariant probabilities; local attraction is not a statement about global convergence. The indexed novelty comparison is evidence of noncoverage by the inspected sources, not a proof of priority against all mathematical literature.

## References
1. S. Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* **18**(2), 183–192, DOI `10.1080/1726037X.2020.1847765`; first published online 7 January 2021 (`https://tarupublications.com/journals/jdsgt/volume/18/issue/2/a-piecewise-contractive-map-on-triangles`). Full author manuscript `https://arxiv.org/abs/2408.16019` (posted 26 August 2024).
2. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, published mathematical record (11 October 2026), `https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8`.
3. *A golden-ratio coexistence window for attracting triangle-projection cycles*, published mathematical record (8 November 2026), `https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-a-golden-ratio-coexistence-window-for-attracting-triangle-projec--4638711ed4bb`.
4. *Sharp fifth-period window for the isosceles farthest-projection map*, published mathematical record (8 November 2026), `https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-fifth-period-window-for-the-isosceles-farthest-projection--1442a77c6de3`.
5. *Sharp multistability windows for an isosceles farthest-projection map*, published mathematical record (2 November 2026), `https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-multistability-windows-for-an-isosceles-farthest-projectio--82fd9a413389`.
