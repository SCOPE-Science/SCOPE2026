# Exact ternary fibre frequencies of the Narayana recurrence

## Finding
Let \(a_0=0\), \(a_1=a_2=1\), and \(a_{n+3}=a_{n+2}+a_n\). For \(k\ge1\), its least period modulo \(3^k\) is \(T_k=8\cdot3^{k-1}\). For a target \(y\bmod3^k\), let \(N_k(y)\) be the number of indices \(0\le n<T_k\) with \(a_n\equiv y\pmod{3^k}\). The following formula specifies **every** target multiplicity, not just the support or the minimum.

Write \(b(y)=1\) for \(y\equiv2\pmod3\) and \(b(y)=2\) otherwise. Define \(R_m(z)=\#\{u\bmod3^m:u^2\equiv z\pmod{3^m}\}\) and \(R_0(z)=1\). There are uniquely defined \(3\)-adic integers \(\beta_0\equiv9\pmod{81}\) and \(\beta_2\equiv1\pmod{81}\), as constructed in the proof. For \(k\ge4\),
\[
\begin{aligned}
N_k(y)={}&b(y)+6\mathbf 1_{y\equiv0\ (27)}+3\mathbf 1_{y\equiv19\ (27)}+12\mathbf 1_{y\equiv1\ (27)}\\
&+9\mathbf 1_{y\equiv\beta_0\ (81)}R_{k-4}\!\left(\frac{y-\beta_0}{162}\right)\\
&+9\mathbf 1_{y\equiv\beta_2\ (81)}R_{k-4}\!\left(\frac{y-\beta_2}{81}\right).
\end{aligned}
\]
The quotients in the final two terms are interpreted in \(\mathbb Z_3/3^{k-4}\), after the displayed divisibility condition. The cases \(k=1,2,3\) are
\[
(N_1(0),N_1(1),N_1(2))=(3,4,1),
\]
\[
N_2(y)=b(y)+3\mathbf1_{y\equiv0\ (9)}+6\mathbf1_{y\equiv1\ (9)},
\]
\[
\begin{aligned}
N_3(y)={}&b(y)+6\mathbf1_{y\equiv0\ (27)}+3\mathbf1_{y\equiv19\ (27)}\\
&+15\mathbf1_{y\equiv1\ (27)}+3\mathbf1_{y\equiv9\ (27)}.
\end{aligned}
\]
Here and below each indicator depends on its stated modulus. In particular, every residue modulo \(3^k\) appears, and precisely the targets congruent to \(2\pmod3\) appear once; the singular targets have unbounded multiplicities as \(k\) grows.

## Assumptions and scope
The recurrence is indexed from zero as specified; no restriction on the positive integer \(k\) or on the residue \(y\) is imposed. A fibre is counted over exactly one least period, not over an arbitrary prefix. The prime is specifically \(3\). The \(3\)-adic centers are defined using derivatives of locally analytic interpolations, not floating-point approximations.

## Proof
Set
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&0&1\end{pmatrix},\quad v=(0,1,1)^T,\quad U=M^8=I+3B,\quad B=\begin{pmatrix}1&1&2\\2&1&3\\3&2&4\end{pmatrix}.
\]
Thus \(a_n=e_1^TM^nv\). As \(U\equiv I\pmod3\), each sequence \(a_{8t+r}\) extends analytically from integer \(t\) to \(\mathbb Z_3\) by
\[
A_r(t)=e_1^T\exp(t\log U)M^rv\qquad(0\le r<8).
\]
The matrix logarithm converges on \(3M_3(\mathbb Z_3)\), with coefficients controlled by \(\nu_3(3^j/j!)\to\infty\). Direct multiplication gives, for the five regular classes \(r\in\{1,4,5,6,7\}\),
\[
\nu_3(A_r(t)-A_r(s))=1+\nu_3(t-s),\qquad t\ne s.
\]
Indeed the coefficient of \(t\) in \((A_r(t)-a_r)/3\) is a unit, while every higher coefficient is divisible by \(3\): the linear coefficient equals \(e_1^TBM^rv\) modulo \(3\), which is nonzero in those five cases; the tail of \(\exp(t\log U)\) has valuation at least \(2\). The residue values \(a_r\pmod3\) for these classes are \(1,2,0,1,0\), respectively. Each such class gives one preimage to every target in its residue ball, producing \(b(y)\).

For the other three classes define
\[
F_0(t)=A_0(t)/9,\qquad F_2(t)=(A_2(t)-1)/9,\qquad F_3(t)=(A_3(t)-1)/9.
\]
The indicated quotients have integral, restricted analytic series. Using \(U^t=\sum_{j\ge0}3^j\binom tj B^j\), only \(j\le3\) survive after division by \(9\) and reduction modulo \(3\); direct integer matrix multiplication yields coefficientwise
\[
F_0(t)\equiv2t+2t^2,\quad F_2(t)\equiv2t+t^2+2t^3,\quad F_3(t)\equiv t+2t^3\pmod3.
\]
The derivative of the first polynomial vanishes only at \(t=1\pmod3\); that of the second only at \(t=2\pmod3\). On every other residue disc, nonzero derivative together with the restricted-series bound gives a bijective isometry onto its prescribed residue ball. For \(F_0\), both regular discs map onto \(3\mathbb Z_3\), producing \(6\) further preimages to \(y\equiv0\pmod{27}\). For \(F_2\), its regular discs map onto \(3\mathbb Z_3\) and \(2+3\mathbb Z_3\), respectively, yielding \(3\) extra preimages at each of \(y\equiv1,19\pmod{27}\). Since \(F_3(t)\equiv0\pmod3\) but \(F'_3(t)\equiv1\pmod3\), its three input discs separately map isometrically onto \(3\mathbb Z_3\); accounting for lifting from \(t\bmod3^{k-1}\) produces \(9\) extra preimages at \(y\equiv1\pmod{27}\). This gives the baseline terms, including the \(12\) at \(y\equiv1\pmod{27}\).

By derivative Hensel lifting there is a unique \(\tau_0\equiv1\pmod3\) with \(F'_0(\tau_0)=0\), and a unique \(\tau_2\equiv2\pmod3\) with \(F'_2(\tau_2)=0\). Set \(\beta_0=A_0(\tau_0)\), \(\beta_2=A_2(\tau_2)\). Taylor expansion on the critical discs, using the quadratic coefficients \(F_0''(\tau_0)/2\equiv2\pmod3\) and \(F_2''(\tau_2)/2\equiv1\pmod3\), gives restricted analytic isometries \(h_0,h_2:\mathbb Z_3\to\mathbb Z_3\) satisfying
\[
A_0(\tau_0+3u)=\beta_0+162h_0(u)^2,\qquad
A_2(\tau_2+3u)=\beta_2+81h_2(u)^2.
\]
To justify the normalization, divide each Taylor remainder by \(81u^2\). The resulting analytic unit is congruent to \(2\), respectively \(1\), modulo \(3\) *as a restricted series*. After division by its displayed unit representative, its square root exists coefficientwise in \(1+3\mathbb Z_3\langle u\rangle\). Multiplication by \(u\) gives \(h_i(u)=u+3g_i(u)\) for an integral restricted analytic \(g_i\), hence \(\nu_3(h_i(u)-h_i(v))=\nu_3(u-v)\). At \(k\ge4\), each root modulo \(3^{k-4}\) has precisely \(9\) lifts to the allowed index parameter modulo \(3^{k-1}\). This proves the two square-root terms, while their zero-precision versions give the special \(k=3\) formula.

For completeness, \(R_m(z)\) is explicitly computable without search: it equals \(3^{\lfloor m/2\rfloor}\) if \(z\equiv0\pmod{3^m}\); otherwise, with \(e=\nu_3(z)<m\), it is \(2\cdot3^{e/2}\) if \(e\) is even and \(3^{-e}z\equiv1\pmod3\), and is zero otherwise. These cases are exactly Hensel's criterion for square roots of units, with the elementary lifting count for nonunits. Finally, the recurrence has least period eight modulo \(3\); any period modulo \(3^k\) is therefore a multiple of eight. The regular-branch isometry forces its index multiplier to be a multiple of \(3^{k-1}\); conversely \(U^{3^{k-1}}\equiv I\pmod{3^k}\). Hence the least period is \(T_k\), completing the proof.

## Verification
The companion `verify_narayana.py` implements two separate routes: direct iteration of the recurrence over the full period, and a calculation of all predicted fibre counts using the critical \(3\)-adic centers and root formulas. It verifies every target for all \(k=1,\ldots,9\), checks total mass, least-cycle state return, and the unique-preimage count. The computations support but do not replace the infinite analytic and Hensel-lifting proof.

## Relationship to prior work
Guadalupe (2021) studies the \(3\)-adic valuations (zero targets) of Narayana numbers. Ismail--Rihanaa--Anwar (2022) treat valuations of Narayana numbers and their shifts by one. Kuloğlu--Özkan--Shannon (2022) analyze periods and finite-group recurrence behavior. An earlier result already established the five isometric index branches, full ternary residue coverage, least periods, and the unique-preimage class; those are used here as background and not claimed as a new discovery. The new statement is the *exact full target-by-target contribution from the three remaining singular branches*, including both quadratic root-count terms at arbitrary precision. Related cubic-recurrence fibre results concern different sequences, not this singular structure.

## Limitations
The result applies to the specified Narayana normalization and prime three only. The construction of the critical centers is implicit but effective by derivative Hensel lifting; the accompanying checker evaluates them to any requested finite precision. Other recurrence normalizations require reindexing. Although relevant primary papers and indexed records were checked, the possibility of an unindexed or implicitly equivalent earlier result cannot be eliminated. There has been no independent external mathematical audit.

## References
- R. Guadalupe, *On the 3-adic valuation of the Narayana numbers*, first public 2021-12-12, https://arxiv.org/abs/2112.06187.
- M. Ismail, R. Rihanaa and T. Anwar, *Narayana Sequence and The Brocard-Ramanujan Equation*, first public 2022-06-18, https://arxiv.org/abs/2206.09174.
- Kuloğlu, Özkan and Shannon, *The Narayana Sequence in Finite Groups*, public 2022, https://www.researchgate.net/publication/366657637_THE_NARAYANA_SEQUENCE_IN_FINITE_GROUPS.
- OEIS A271901, modular period record, https://oeis.org/A271901.
