# Exact polynomial certificates

This note provides explicit coefficient certificates for the two nontrivial comparisons used in the accompanying theorem. They concern polynomials over the integers, not numerical fits.

## One positive threshold

Use the rational expressions \(S_n(t)\), \(M_n(t)\), and the positive denominator \(D_n(t)\) defined in `RESULT.md`; set
\[
Q_n(t)=D_n(t)[M_n(t)-S_n(t)].
\]
Set \(u=n-3\ge0\). In the expansion \(Q_{u+3}(t)=\sum_{j=0}^6 c_j(u)t^j\), the exact coefficients are
\[
\begin{aligned}
c_0(u)&=-(u+1)(4u^6+55u^5+314u^4+932u^3+1501u^2+1242u+414),\\
c_1(u)&=2(u+1)(4u^6+44u^5+182u^4+300u^3+31u^2-395u-282),\\
c_2(u)&=(u+1)(44u^5+480u^4+2060u^3+4129u^2+3678u+1093),\\
c_3(u)&=2(u+1)(48u^4+466u^3+1722u^2+2729u+1507),\\
c_4(u)&=104u^4+960u^3+3359u^2+5002u+2595,\\
c_5(u)&=4(14u^3+107u^2+284u+239),\\
c_6(u)&=4(3u^2+18u+31).
\end{aligned}
\]
Thus \(c_0(u)<0\), while \(c_j(u)>0\) for \(2\le j\le6\); the coefficient \(c_1(u)\) may have either sign. Ignoring zeros, the coefficient sequence in descending powers has exactly one sign change. Descartes' rule gives at most one positive root, while the endpoint values of \(Q\) give existence. In particular,
\[
Q_n(1/2)=(n-1)^2(6n^2-6n+1)>0.
\]

## Elimination of unmatched cross-part pairs

Write \(U_n(t)\) for the unmatched-pair inverse-square trace and
\[
H_n(t)=2n^2+4nt-5n+2t^2-4t+2,
\]
which is strictly positive in the domain: it is a positive factor of the determinant of a strictly positive definite grounded block. The identity
\[
U_n(t)-S_n(t)=\frac{R_n(t)}{(n+t-1)^2(n+2t-2)^2H_n(t)^2}
\]
holds identically. For \(n=u+3\) and \(t=v+1\), with \(u,v\ge0\), the numerator is \(R_{u+3}(v+1)=\sum_{j=0}^{6}b_j(u)v^j\), where
\[
\begin{aligned}
b_0(u)&=(u+3)^5(4u^2+21u+28),\\
b_1(u)&=4(u+3)^4(6u^2+32u+43),\\
b_2(u)&=(u+3)^2(60u^3+498u^2+1361u+1227),\\
b_3(u)&=2(u+3)(40u^3+326u^2+853u+711),\\
b_4(u)&=60u^3+473u^2+1158u+841,\\
b_5(u)&=12(u+1)(2u+7),\\
b_6(u)&=4(u+1).
\end{aligned}
\]
Each coefficient is strictly positive for \(u\ge0\), so \(U_n(t)>S_n(t)\) whenever \(t\ge1\).

For \(0<t<1\), relabel the remaining vertices so that the off-diagonal block of the matched-pair grounded Laplacian is \(B_M=J_{n-1}+(t-1)I_{n-1}\), whereas the unmatched-pair block is \(B_U=J_{n-1}+(t-1)\operatorname{diag}(I_{n-2},0)\). Consequently \(B_U\ge B_M\) entrywise, with a strict inequality. Both grounded matrices have the form \(dI-W\) with \(d=n-1+t\) and nonnegative symmetric \(W\) of spectral radius less than \(d\). Their resolvents are the convergent positive Neumann series \(d^{-1}\sum_{k\ge0}(W/d)^k\), which implies a strict increase in the trace of the square upon replacing \(B_M\) by \(B_U\). Thus \(U_n(t)>M_n(t)\) for \(0<t<1\). These two inequalities exclude unmatched pairs at every positive conductance.

## Two-scale threshold separation

Expanding the exact polynomial at \(t=1/2-a/n^3-b/n^4\) and multiplying by \(n^{-7}\) gives coefficients \((6-8a)n^{-3}\) and \((28a-8b-18)n^{-4}\) at the first two nonzero orders. The unique positive root therefore satisfies
\[
\theta_n=\frac12-\frac{3}{4n^3}-\frac{3}{8n^4}+O(n^{-5}).
\]
For the first inverse power, the cubic given in `RESULT.md` has positive derivative on the positive axis, takes the value \(n-1\) at \(t=1/2\), and has derivative \(2n^3+O(n^2)\) there. Its unique root satisfies
\[
\gamma_n=\frac12-\frac{1}{2n^2}+O(n^{-3}).
\]
Hence \(\theta_n-\gamma_n=1/(2n^2)+O(n^{-3})>0\) for all sufficiently large \(n\). The formulas are independent exact algebraic statements; no root locations are inferred from finite sampling.
