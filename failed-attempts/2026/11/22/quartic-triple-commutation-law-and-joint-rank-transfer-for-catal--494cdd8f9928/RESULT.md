# Quartic triple-commutation law and joint-rank transfer for Catalan monoids

## Finding
For each integer \(n\ge1\), let \(\mathcal C_n\) be the monoid of nondecreasing, regressive maps of \([n]\) to itself. Write \(E_n\) for its idempotents. Count **ordered** triples \((a,b,c)\in E_n^3\), allowing repeated entries, for which \(ab=ba\), \(ac=ca\), and \(bc=cb\). Let \(a_{n,k}\) count triples whose common product \(abc\) has image rank \(k\). Then the full rank-refined generating function is
\[
\boxed{\sum_{n\ge1}\sum_{k=1}^n a_{n,k}t^{n-1}u^{k-1}
=\frac{1-2t^2+2t^3}{1-(7+u)t+16t^2-(14-2u)t^3+(4-2u)t^4}.}
\]
Equivalently, defining
\[
G(t)=\frac{1-2t^2+2t^3}{1-7t+16t^2-14t^3+4t^4},
\]
the exact coefficient for every \(n\ge k\ge1\) is
\[
\boxed{a_{n,k}=[t^{n-k}]G(t)^k.}
\]
The unrefined triple counts \(a_n=\sum_k a_{n,k}\) have the particularly short quartic generating function
\[
\boxed{\sum_{n\ge1}a_nt^{n-1}
=\frac{1-2t^2+2t^3}{1-8t+16t^2-12t^3+2t^4},}
\]
with \(a_1=1\), \(a_2=8\), \(a_3=46\), \(a_4=254\), and
\[
a_n=8a_{n-1}-16a_{n-2}+12a_{n-3}-2a_{n-4}\quad(n\ge5).
\]

The result also determines **all four joint ranks**. Define
\[
R_n(x,y,z,u)=\sum_{\substack{a,b,c\in E_n\\ab=ba,\ ac=ca,\ bc=cb}}
x^{\operatorname{rk}(a)-1}y^{\operatorname{rk}(b)-1}
z^{\operatorname{rk}(c)-1}u^{\operatorname{rk}(abc)-1}.
\]
For each pair in the ordered list \((A,B),(A,C),(B,C)\), use a state coordinate in \(\{0,1,2\}\) recording which exclusive fixed-point color (if any) has appeared since the last common fixed point of that pair. Let \(\Sigma\) be the following **thirteen** states (the same order can be used throughout):
\[
\begin{split}
\Sigma=\{&(0,0,0),(0,1,1),(0,2,2),(1,0,2),(1,1,0),
(1,1,1),(1,1,2),\\
&(1,2,2),(2,0,1),(2,1,1),(2,2,0),(2,2,1),(2,2,2)\}.
\end{split}
\]
For a three-bit symbol \(b=(b_A,b_B,b_C)\in\{0,1\}^3\), the transition \(\delta(s,b)\) is invalid if any pair is shown the exclusive color opposite to its already recorded color. Otherwise the pair coordinate resets to zero when both its bits are one, changes from zero to the respective exclusive color on a single one, and is unchanged on two zeros or on a repeat of the recorded exclusive color. Let \(T(x,y,z,u)\) be the thirteen-by-thirteen matrix
\[
T_{s,s'}(x,y,z,u)=\sum_{\substack{b\in\{0,1\}^3\\\delta(s,b)=s'}}
x^{b_A}y^{b_B}z^{b_C}u^{b_Ab_Bb_C}.
\]
Then, with \(e_0\) the coordinate row of \((0,0,0)\) and \(\mathbf1\) the all-ones column,
\[
\boxed{R_n(x,y,z,u)=e_0T(x,y,z,u)^{n-1}\mathbf1\quad(n\ge1).}
\]
This is an exact finite transfer for every simultaneous image-rank profile, not an approximation or solely a count of three-way products.

## Assumptions and scope
Transformations compose as ordinary functions, with the rightmost map applied first. All maps are total, nondecreasing and order-decreasing. All ordered triples, including those with coincidences, are counted. All ranks are cardinalities of images, ranging between \(1\) and \(n\). Powers of indeterminates and formal generating functions are identities in the integer polynomial and formal power-series rings; no convergence assumption is needed. The case \(n=1\) consists of the unique all-identity triple.

## Proof
**1. Idempotents and the two-color gap criterion.** Each idempotent has a unique fixed-point set \(S\subseteq[n]\) with \(1\in S\); it is the predecessor projection
\[
p_S(i)=\max\{s\in S:s\le i\}.
\]
Indeed, the image of an idempotent equals its fixed points; monotonicity and regressiveness force every value to be the largest fixed point not exceeding its argument. Conversely these projections are idempotents. For two fixed-point sets \(S,T\), their projections commute exactly when no interval between consecutive points of \(S\cap T\), including the terminal interval, contains both an \(S\)-only and a \(T\)-only point. If both exclusive colors appear within one such gap, evaluate the composites at a later exclusive point immediately after a change of exclusive color: the two latest predecessor fixed points differ, and the smaller is not fixed by the opposite map, forcing noncommutation. If at most one exclusive color occurs in each gap, one projection sends the whole gap to its preceding common fixed point, and the other fixes that point. Therefore both composites equal \(p_{S\cap T}\). In particular every commuting triple has product \(p_{A\cap B\cap C}\).

**2. Thirteen-state transfer.** Positions \(2,\ldots,n\) each choose one of the eight three-bit membership symbols, while position \(1\) is fixed in all three idempotents. For each of the three unordered pairs, a three-state automaton tracks whether the current gap has had an exclusive fixed point of its first or second map. The opposite exclusive color is forbidden until a simultaneous fixed point resets that pair. By Step 1 all three pairs commute if and only if this scan avoids forbidden transitions. From initial state \((0,0,0)\), the states reachable under the eight symbols are exactly the displayed thirteen: direct application of the three-coordinate update gives closure, and each listed state is reached by a valid finite word. Every valid word determines one triple of predecessor projections. The monomial attached to a symbol records the three individual fixed-point ranks, and records one extra product fixed point exactly when all three bits equal one. Thus its product over positions \(2,\ldots,n\) has the four indicated exponents. This proves the thirteen-state formula for \(R_n\).

**3. Four-state symmetry quotient.** When all indeterminates equal one, permutation of the three idempotents preserves valid transitions. The thirteen states split into the following four orbits, written in the pair-coordinate order from Step 2:
\[
\begin{aligned}
O_0&=\{(0,0,0)\},\\
O_1&=\{(0,1,1),(1,0,2),(2,2,0)\},\\
O_2&=\{(0,2,2),(1,1,0),(2,0,1)\},\\
O_3&=\{(1,1,1),(1,1,2),(1,2,2),(2,1,1),(2,2,1),(2,2,2)\}.
\end{aligned}
\]
Each state in a given orbit has the same number of transitions to every target orbit. Explicitly summing the allowed three-bit symbols in each row gives
\[
Q=\begin{pmatrix}
2&3&3&0\\
1&2&0&2\\
1&2&2&0\\
1&1&0&2
\end{pmatrix}.
\]
Consequently \(a_n=(1,0,0,0)Q^{n-1}(1,1,1,1)^{\mathsf T}\). Define
\[
D(t)=1-8t+16t^2-12t^3+2t^4
\]
and the polynomial column vector
\[
v(t)=\begin{pmatrix}1-2t^2+2t^3\\1-3t+2t^2\\1-3t+4t^2-2t^3\\1-4t+5t^2-2t^3\end{pmatrix}.
\]
Direct multiplication, entry by entry, gives the exact certificate
\[
(I-tQ)v(t)=D(t)\mathbf1.
\]
Since \(I-tQ\) is invertible over formal series, multiplying by the initial row produces \(\sum_{n\ge1}a_nt^{n-1}=v_0(t)/D(t)\). Coefficient comparison gives the displayed recurrence.

**4. Product-rank renewal.** A position belongs to \(A\cap B\cap C\) if and only if its symbol is \((1,1,1)\). That symbol returns **every** pair coordinate to zero. Hence consecutive simultaneous fixed points split a valid triple into independent gap words, each avoiding \((1,1,1)\). Let \(G(t)\) enumerate such valid gap words by length. Allowing a free sequence of gap words separated by compulsory \((1,1,1)\) symbols gives the unrefined series \(F(t,1)=G(t)/(1-tG(t))\). Therefore
\[
G(t)=\frac{F(t,1)}{1+tF(t,1)}
=\frac{1-2t^2+2t^3}{1-7t+16t^2-14t^3+4t^4}.
\]
Giving each additional simultaneous fixed point weight \(u\) yields
\[
F(t,u)=\frac{G(t)}{1-utG(t)}
=\frac{1-2t^2+2t^3}{1-(7+u)t+16t^2-(14-2u)t^3+(4-2u)t^4}.
\]
A product of rank \(k\) has \(k-1\) internal simultaneous fixed positions, hence exactly \(k\) independent gaps; this gives \(a_{n,k}=[t^{n-k}]G(t)^k\). All steps are bijective and apply for every \(n\).

## Verification
The accompanying standalone Python 3 program `verify_catalan_triples.py` uses only the standard library. It independently generates all predecessor projections, forms their actual composition commutation graph, and exhaustively counts ordered pairwise-commuting triples for \(1\le n\le8\). These counts are checked against the four-state quotient and the quartic recurrence. For \(1\le n\le6\), brute-force joint individual/product-rank profiles are checked against the full thirteen-state weighted transfer. Product-rank distributions through \(n=8\) are separately checked against coefficients obtained by a polynomial recurrence from the bivariate rational function. The script verifies the polynomial certificate \((I-tQ)v=D\mathbf1\) using exact integer arithmetic. It exits with `CATALAN_TRIPLE_COMMUTANTS_OK` on success. The enumerations are finite consistency checks; the all-size proof is above.

For example, the \(n=5\) product-rank distribution for ranks \(1,2,3,4,5\) is \((445,676,240,28,1)\), totaling \(1390\). The first eight totals are \((1,8,46,254,1390,7592,41452,226316)\).

## Relationship to prior work
L. Andrenšek, *Endomorphisms of Hecke–Kiselman Monoids Associated to Simple Oriented Graphs* (arXiv:2604.15497v1, first public 2026-04-16), establishes general pairwise-idempotent product and compatibility criteria (Theorem 3.6, Corollary 3.9) and applies them to endomorphisms of Catalan monoids. In particular, homomorphisms from a free three-generator semilattice into a Catalan monoid correspond to triples of commuting idempotents, so these compatibility criteria already provide an abstract test for the triples considered here. **The condition for triples itself is not claimed as novel.** The new evaluated assertions are the quartic total and product-rank generating functions, the exact four-rank transfer, and their minimal symmetric quotient; they are not the endomorphism theorem or pairwise compatibility condition of that paper.

Earlier accessible studies give the pairwise Catalan idempotent commutation criterion and its count \(1,4,14,48,\ldots\), exact fibers with a prescribed product for **pairs**, and a binary-search-tree description of maximal commuting idempotent families. Those results constrain the same graph, but the pair sequence and prescribed pair fibers do not determine the numbers of triangles. The maximal-clique classification implicitly contains sufficient combinatorial information to recover lower-order clique counts by nontrivial overlap counting; it does not state or evaluate the displayed rational triple-rank distributions. The 2026-11-16 paper by Konieczny and Korkmaz computes centralizers of individual Catalan elements and the numbers of idempotents in individual centralizers, but its inspected Section 3 does not supply a triangle count or joint-rank spectrum. Numerical or unpublished equivalences remain possible and are not ruled out by a search.

## Limitations
No claim is made to classify higher tuples, arbitrary nonidempotent commuting elements, or the entire clique polynomial. A finite quotient automaton is a method for exact integer counting, not a proof of historical priority. Some individual numerical coefficients may occur in earlier combinatorial databases; the claimed mathematical contribution is the proved Catalan-monoid interpretation together with the full product-rank formula and all-four-rank transfer. The earlier maximal-family classification is a potentially powerful indirect starting point and remains a residual originality risk. No independent mathematical audit has been performed.

## References
1. L. Andrenšek, *Endomorphisms of Hecke–Kiselman Monoids Associated to Simple Oriented Graphs*, arXiv:2604.15497v1 (2026-04-16), https://arxiv.org/abs/2604.15497 .
2. *Commuting idempotents of Catalan monoids: a gap criterion, centralizer transfer, and exact density* (2026), public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-commuting-idempotents-of-catalan-monoids-a-gap-criterion-central--1bd10f020d19 .
3. *Common-fixed-point compatibility and product-fiber factorization for Catalan monoid idempotents* (2026), public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-common-fixed-point-compatibility-and-product-fiber-factorization--06ff39bf0d33 .
4. *Binary-search-tree classification of maximal commuting Catalan idempotent families* (2026), public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-binary-search-tree-classification-of-maximal-commuting-catalan-i--37f68a6692e4 .
5. J. Konieczny and E. Korkmaz, *Centralizers in Catalan Monoids*, arXiv:2611.21071v1 (2026-11-16), https://arxiv.org/abs/2611.21071 .
