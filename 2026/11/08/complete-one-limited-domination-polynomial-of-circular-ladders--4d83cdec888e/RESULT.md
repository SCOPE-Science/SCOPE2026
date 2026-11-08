# Complete one-limited domination polynomial of circular ladders

## Finding
For every integer \(n\ge3\), let \(G_n=C_n\square K_2\), with cyclically indexed columns \(i\in\mathbb Z/n\mathbb Z\) and two layers \(h\in\{0,1\}\). A one-limited dominating set \(D\) dominates every vertex outside \(D\), and each vertex in \(D\) has at most one neighbour outside \(D\). Define the labelled-set polynomial
\[
L_n(z)=\sum_{D\text{ one-limited dominating in }G_n}z^{|D|}.
\]
Put
\[
\begin{aligned}
Q(u,z)={}&(1-zu)(1-zu+z^3u^2)\\
&\cdot\bigl(1-z^2u-z^3u^2-(z^5+2z^4)u^3\\
&\qquad -(z^6+z^5+z^4)u^4-z^6u^5\bigr).
\end{aligned}
\]
Then, for all \(n\ge3\), the **entire polynomial** is determined by the rational bivariate generating identity
\[
\boxed{L_n(z)=[u^n]\left(-u\frac{\partial}{\partial u}\log Q(u,z)\right).}
\]
In particular,
\[
\boxed{\gamma^{\mathrm L}_1(G_n)=n,\qquad [z^n]L_n(z)=2+4\mathbf1_{4\mid n}.}
\]
All minimum sets are classified: two are the complete individual cycle layers; if \(4\mid n\), exactly four additional sets consist of entire columns selected according to a binary sequence \((a_i)\) satisfying \(a_{i+2}=1-a_i\). There are no other minima.

The total number of one-limited dominating sets has an exponential asymptotic
\[
L_n(1)\sim\lambda^n,\quad \lambda\approx2.29237024940527,
\]
where \(\lambda\) is the unique positive root of \(t^5-t^4-t^3-3t^2-3t-1\). The identity counts labelled subsets, not symmetry orbits.

## Assumptions and scope
All graphs are finite, simple and undirected. For \(n=3\), \(C_3\) is the triangle, so each vertex still has three distinct neighbours in the prism. Vertex labels are the ordered pairs \((i,h)\). The index \(n\) is at least three; formal terms of the rational series at exponents one and two are not assigned graph-theoretic meanings. The full vertex set qualifies as one-limited dominating.

## Proof
Write \(S=V(G_n)\setminus D\). Encode column \(i\) by two bits \(s_i=(s_{i,0},s_{i,1})\in\{0,1\}^2\), with bit one indicating membership in \(S\). For bits \(a,b,c\in\{0,1\}^2\) define
\[
q_h(a,b,c)=a_h+c_h+b_{1-h}\qquad(h=0,1).
\]
A chosen column triple \((a,b,c)\) is **admissible** precisely if, for each \(h\),
\[
 b_h=1\ \Longrightarrow\ q_h\le2,\qquad
 b_h=0\ \Longrightarrow\ q_h\le1.
\]
Indeed, when \(b_h=1\), domination of this outside vertex demands at least one neighbour in \(D\), i.e. at most two in \(S\). When \(b_h=0\), the one-limited constraint demands at most one neighbour in \(S\). The three neighbours are distinct by \(n\ge3\).

Index a \(16\)-by-\(16\) matrix \(T=T(z)\) by ordered pairs of two-bit columns \((a,b)\). Set
\[
T_{(a,b),(b',c)}=
\begin{cases}
z^{2-|b|},&b=b'\text{ and }(a,b,c)\text{ admissible},\\
0,&\text{otherwise},
\end{cases}
\]
where \(|b|\) is the number of ones in the two-bit column. A closed walk of length \(n\) in these ordered-pair states is uniquely the sequence \((s_0,\dots,s_{n-1})\) of labelled prism columns. Its weight is \(z^{\sum_i(2-|s_i|)}=z^{|D|}\), and each local condition is imposed once. Hence
\[
L_n(z)=\operatorname{tr}(T(z)^n)\quad(n\ge3).
\]
Exact expansion of the completely specified finite matrix gives
\[
\begin{aligned}
\det(tI-T)={}&t^8(t-z)(t^2-tz+z^3)\\
&\cdot\bigl(t^5-z^2t^4-z^3t^3-(z^5+2z^4)t^2\\
&\qquad -(z^6+z^5+z^4)t-z^6\bigr).
\end{aligned}
\]
This identity can be verified solely by ordinary polynomial arithmetic on the displayed 16-state matrix; `verify.py` constructs the matrix from the defining conditions and checks the factorization symbolically. Replacing \(t\) by \(1/u\), and dividing by the leading degree \(16\) monomial, yields \(\det(I-uT)=Q(u,z)\). The standard formal identity
\[
-u\partial_u\log\det(I-uT)=\sum_{j\ge1}\operatorname{tr}(T^j)u^j
\]
proves the claimed formula (only coefficients \(n\ge3\) correspond to simple prism graphs).

For the minimum, every vertex of \(S\) must have at least one neighbour in \(D\), whereas every vertex of \(D\) has at most one neighbour in \(S\). Counting crossing edges gives \(|S|\le e(D,S)\le |D|\); thus \(|D|\ge n\). A complete cycle layer realizes equality, so the minimum is exactly \(n\). Equality throughout the crossing inequalities holds if and only if every vertex has exactly one neighbour in the opposite part; equivalently the crossing edges form a perfect matching.

Classify such equality bipartitions by column. A **mixed column** has one vertex in \(D\) and one in \(S\); its vertical edge is already its required crossing edge, so both horizontal neighbours of both vertices must have the same membership. Thus both adjacent columns have the identical mixed orientation, and propagation around the cycle forces all columns to have it. There are exactly two such sets. If no column is mixed, each column lies entirely in \(D\) or entirely in \(S\). Write \(a_i\in\{0,1\}\) for the indicator of a full \(D\)-column. The requirement of exactly one crossing neighbour at every vertex becomes \(a_{i-1}\ne a_{i+1}\), or \(a_{i+2}=1-a_i\). This has a cyclic solution exactly when four divides \(n\), and then two freely chosen consecutive bits yield exactly four solutions. This is exhaustive.

Finally specialize \(z=1\). The nonzero eigenvalues of \(T(1)\), with multiplicity, are the root \(1\), the two unit-modulus roots of \(t^2-t+1\), and the five roots of \(p(t)=t^5-t^4-t^3-3t^2-3t-1\). The polynomial \(p\) has exactly one positive root \(\lambda>1\) by Descartes' rule of signs and the intermediate-value theorem. For any complex root \(w\) of \(p\), the triangle inequality gives
\[
|w|^5\le |w|^4+|w|^3+3|w|^2+3|w|+1.
\]
Since \(p\) has only one positive root, \(|w|\le\lambda\). Equality would require all summands to share a phase, in particular \(w\) and \(1\) would have the same phase, forcing \(w=\lambda\). Descartes' rule also gives simplicity of the positive root. Therefore all other eigenvalues have modulus strictly smaller than \(\lambda\). The power-sum formula for traces yields \(L_n(1)=\lambda^n+O(\eta^n)\) for some \(\eta<\lambda\), proving the asymptotic.

## Verification
The included standalone `verify.py` constructs both the transfer matrix and an independently specified graph. It checks the symbolic matrix characteristic polynomial, enumerates **all** \(2^{2n}\) labelled subsets for \(3\le n\le8\), compares every coefficient, and checks the minimum multiplicity for \(9\le n\le20\) using exact matrix powers. The output is `VERIFY_OK`. These finite checks corroborate the argument; the infinite statements follow from the exact transfer-matrix and crossing-edge proofs, not from extrapolation.

Examples are
\[
L_3(z)=z^3(z^3+6z^2+3z+2),\qquad
L_4(z)=z^4(z^4+8z^3+16z^2+6).
\]

## Relationship to prior work
One-limited domination and its capacity interpretation were introduced by Božović, Radić, Kovijanić-Vukićević and Tepeh. Tepeh's 2026 Cartesian-product work derives sharp scalar bounds and values for product families; in particular it studies prism products, but the inspected text did not enumerate the one-limited sets of circular ladders by all cardinalities. Radić and Tepeh study computational hardness and Goldberg snarks, and Radić, Radić and Tepeh study structural excess in cubic graphs. Their lower bound and the equivalence with \((1,2)\)-domination are taken as known, not claimed as new. The present result supplies the full labelled cardinality distribution, a concrete rational two-variable enumerator, and a complete minimum-set classification for one product family. Historical priority remains provisional.

## Limitations
No statement is made about arbitrary Cartesian products, open ladders, higher-dimensional grids, or unlabelled orbit counts. The rational expression enumerates the defined one-limited property, not every other domination variant. Source coverage is not exhaustive: the full text of the October 19 structural-aspects preprint was not accessible in this run and could contain an implicit special case. Independent mathematical review has not been performed.

## References
- D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, *On k-limited domination in graphs*, Computational and Applied Mathematics (published online 11 September 2026), https://doi.org/10.1007/s40314-026-03902-2.
- A. Tepeh, *On k-limited domination: complexity and Cartesian products*, arXiv:2606.22428 (first posted 21 June 2026), https://arxiv.org/abs/2606.22428.
- G. Radić and A. Tepeh, *On 1-limited and (1,2)-domination in cubic graphs*, arXiv:2610.01796 (first posted 1 October 2026), https://arxiv.org/abs/2610.01796.
- G. Radić, G. Radić and A. Tepeh, *Structural aspects of 1-limited domination in cubic graphs*, arXiv:2610.26259 (first posted 19 October 2026), https://arxiv.org/abs/2610.26259.
