# Exact least genus quasiperiod for quotients of three consecutive generators

## Finding
For integers \(a\ge3\) and \(p\ge2\), put
\[
S_a=\langle a,a+1,a+2\rangle,\qquad Q_{a,p}=\{n\ge0:pn\in S_a\},
\]
and write \(G_p(a)=|\mathbb Z_{\ge0}\setminus Q_{a,p}|\). For every fixed \(p\), \(G_p(a)\) is a quadratic quasipolynomial in \(a\) of leading coefficient \(1/(4p)\). Its *least eventual quasipolynomial period* is exactly \(2p\) for every \(p\ge3\), and exactly \(2\) for \(p=2\).

More precisely, write uniquely \(a=2pm+r\), \(m\ge0\), \(0\le r<2p\), and define
\[
D_p(r)=r-p+1-\frac{\gcd(p,r)+\gcd(p,r+2)}2,\quad h(r)=\left\lfloor\frac{r-2}{2}\right\rfloor,
\]
\[
C_p(r)=\sum_{s=0}^{h(r)}\left(\left\lfloor\frac{(s+1)r-1}{p}\right\rfloor-\left\lfloor\frac{s(r+2)}p\right\rfloor\right),
\]
where a sum with upper endpoint \(-1\) is zero. The *exact, non-eventual* genus formula is
\[
\boxed{G_p(2pm+r)=pm^2+(p+D_p(r))m+C_p(r).}
\]
In particular, the coefficient of \(a\) in its branch polynomial depends only on \(a\bmod p\) and equals
\[
\boxed{\frac{2-\gcd(p,a)-\gcd(p,a+2)}{4p}.}
\]
For \(p=2\), this reduces to \(G_2(a)=(a^2-2a)/8\) for even \(a\), and \(G_2(a)=(a^2-1)/8\) for odd \(a\).

## Assumptions and scope
All semigroups are additive submonoids of nonnegative integers. The genus counts excluded nonnegative integers (zero is always included). The quotient need not have any specified embedding dimension, and the divisibility assumption \(p\mid a\) is **not** imposed. A quasipolynomial period \(T\) means that for each residue \(u\pmod T\) a polynomial in \(a\) gives the values for all sufficiently large integers \(a\equiv u\pmod T\). The least period is the least positive such \(T\). The proof gives formulas for every \(a\ge3\), not just sufficiently large \(a\).

## Proof
**1. Exact gap intervals.** If \(N=qa+r\) with \(q\ge0\), \(0\le r<a\), then \(N\in S_a\) exactly when \(r\le2q\): a sum of exactly \(q\) generators contributes every increment from \(0\) to \(2q\), while a sum of fewer generators cannot reach \(qa+r\) if \(r>2q\), and more than \(q\) generators exceed it. Consequently, all gaps of \(S_a\) form the disjoint intervals
\[
I_q=[q(a+2)+1,(q+1)a-1]\cap\mathbb Z,
\quad 0\le q\le\left\lfloor\frac{a-2}2\right\rfloor.
\]
Counting their multiples of \(p\) proves
\[
G_p(a)=\sum_{q=0}^{\lfloor(a-2)/2\rfloor}
\left(\left\lfloor\frac{(q+1)a-1}{p}\right\rfloor-\left\lfloor\frac{q(a+2)}p\right\rfloor\right).\tag{1}
\]

**2. Block decomposition.** Write \(a=2pm+r\). For \(q=tp+s\), \(0\le s<p\), the summand in (1) is
\[
2(m-t)+\delta_s(r),\quad
\delta_s(r)=\left\lfloor\frac{(s+1)r-1}{p}\right\rfloor-\left\lfloor\frac{s(r+2)}p\right\rfloor.
\]
The summation range is exactly \(m\) full blocks \(0\le t<m\) and an optional tail \(q=mp+s\), \(0\le s\le h(r)\). Thus
\[
G_p(a)=pm(m+1)+m\sum_{s=0}^{p-1}\delta_s(r)+C_p(r).\tag{2}
\]
The elementary floor-sum identity
\[
\sum_{s=0}^{p-1}\left\lfloor\frac{sk}{p}\right\rfloor
=\frac{(p-1)(k-1)+\gcd(p,k)-1}{2},\quad k\ge0,
\]
obtained by pairing fractional parts (or counting the multiples in the rectangle), yields
\[
\sum_{s=0}^{p-1}\delta_s(r)=r-p+1-\frac{\gcd(p,r)+\gcd(p,r+2)}2=D_p(r).
\]
Substitution into (2) establishes the displayed exact formula. Expressing \(m=(a-r)/(2p)\) shows that its quadratic coefficient is \(1/(4p)\) and its linear coefficient is \([2-\gcd(p,r)-\gcd(p,r+2)]/(4p)\). The remaining coefficient is periodic modulo \(2p\), so \(2p\) is an actual period.

**3. Least period from the linear coefficient.** Define \(H_p(r)=\gcd(p,r)+\gcd(p,r+2)\) on \(\mathbb Z/p\mathbb Z\). For \(p\ge5\), its unique maxima occur at the two residues \(0,-2\). Their value \(p+\gcd(p,2)\) is strictly larger than every other value, because two proper divisors of \(p\) sum to at most \(p\). The two-point set \(\{0,-2\}\) has no nontrivial translational symmetry for \(p\ge5\). Thus the linear coefficient has least period \(p\). For \(p=3\), the same conclusion follows directly from \(H_3(0)=H_3(1)=4\), \(H_3(2)=2\). At \(p=4\), its least period is \(2\).

When \(p\) is odd, the branch polynomial for \(r=p\) is exactly \(1/4\) less than that for \(r=0\), as follows from \(C_p(0)=C_p(p)=0\) and the expression for \(D_p\). Hence the full genus quasipolynomial cannot have period \(p\).

For even \(p\), compare branches \(r=1\) and \(r=p+1\). Put \(\alpha=(3-\gcd(p,3))/2\). Directly from the tail formula, \(C_p(1)=0\), \(C_p(p+1)=\lceil p/3\rceil\), \(D_p(1)=\alpha-p\) and \(D_p(p+1)=\alpha\). After expressing the two branches as polynomials in \(a\), their difference is the positive constant
\[
\Delta_p=\left\lceil\frac p3\right\rceil-\frac{p+2\alpha}4
=\begin{cases}
 p/12,&p\equiv0\pmod6,\\
 (p-2)/12,&p\equiv2\pmod6,\\
 (p+2)/12,&p\equiv4\pmod6.
\end{cases}
\]
It is positive for all even \(p\ge4\), but zero for \(p=2\). Hence \(p\) is not a period for even \(p\ge4\).

A common eventual quasipolynomial function with periods \(T\) and \(2p\) also has period \(\gcd(T,2p)\): on each compatible pair of infinite arithmetic progressions the branch polynomials agree identically. For \(p\ne4\), \(p\ge3\), every period must be divisible by \(p\), yet period \(p\) is excluded, so every period is divisible by \(2p\). For \(p=4\), the linear coefficient excludes odd periods; a period \(2\) would imply period \(4\), which the positive branch difference excludes. Thus the least period is \(8\). The explicit two-branch formula for \(p=2\) has distinct linear coefficients on the even and odd branches, giving least period \(2\). This completes the proof.

## Verification
`verify.py` separately constructs membership of \(\langle a,a+1,a+2\rangle\) by unbounded coin-change dynamic programming on a proven finite conductor range, then counts the excluded multiples of \(p\). It compares this with the closed formula for \(3\le a<128\) and \(2\le p<29\): 3,375 exact cases. Further tests check 1,978 complete quasipolynomial branches and the linear-coefficient minimal periods for 98 moduli. Execute with `python3 verify.py`; Python 3 standard library is the only dependency. These finite tests are not a proof of infinite exact periods; Section Proof supplies that proof.

## Relationship to prior work
Adeniran–Butler–Defant–Gao–Harris–Hettle–Liang–Nam–Volk (2018) give a general root-of-unity identity for the genus of a quotient, and analyze three-term arithmetic progression quotients specifically when the quotient modulus divides the first generator. Their Section 3 does not state a sharp quasipolynomial period for every residue class of the first generator. Liu (2026, July 25) proves a period-*dividing*-\(p\) result for the Frobenius number of *two*-generator consecutive quotients. Liu (2026, April 29) studies a different class of quotient semigroups under a divisibility assumption on the first generator. The result above identifies an exact, generally doubled period for the *genus* of a three-generator consecutive family, with a new explicit gcd-controlled linear coefficient. The universal root-of-unity formula can be used in principle to recalculate individual genus values, but does not by itself provide this sharp period classification.

## Limitations
The result concerns genus, not the Frobenius number or a general \(\ell\)-term arithmetic progression. The least-period assertion is *eventual* in its definition, although the formulas themselves hold for all \(a\ge3\). Existing general quotient formulas may offer alternative derivations. Historical priority has only been checked against the relevant accessible primary literature and research-index matches; unindexed equivalent derivations remain possible. No independent audit has been performed.

## References
- A. Adeniran et al., *On the genus of a quotient of a numerical semigroup*, arXiv:1809.09360 (2018), especially Theorem 1.3 and Section 3. https://arxiv.org/abs/1809.09360
- F. Liu, *On the Frobenius Number of Quotients of Numerical Semigroups*, arXiv:2607.23076, publicly posted 2026-07-25; Theorem 1.4. https://arxiv.org/abs/2607.23076
- F. Liu, *The Frobenius problem for a class of quotients of numerical semigroups*, arXiv:2604.26415, publicly posted 2026-04-29; Introduction. https://arxiv.org/abs/2604.26415
