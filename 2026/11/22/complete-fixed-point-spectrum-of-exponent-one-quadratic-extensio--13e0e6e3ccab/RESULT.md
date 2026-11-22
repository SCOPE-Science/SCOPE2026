# Complete fixed-point spectrum of exponent-one quadratic-extension permutation binomials

## Finding
Let \(q\) be any odd prime power, \(K=\mathbb F_q\), \(L=\mathbb F_{q^2}\), and \(f_a(X)=X(X^{2(q-1)}+a)\) for \(a\in L\). Write \(N_q(j)\) for the number of coefficients for which \(f_a:L\to L\) is a permutation with exactly \(j\) fixed points. Set
\[
\epsilon_q=\mathbf1_{3\nmid(q+1)},\qquad
\eta_q=\mathbf1_{q\bmod60\in\{7,43\}},\qquad
m_q=\begin{cases}(q+1)/2,&\operatorname{char}K=3,\\q+1,&\operatorname{char}K\ne3.\end{cases}
\]
Then the complete fixed-point spectrum is
\[
\boxed{N_q(2q-1)=\epsilon_q+2\eta_q,\qquad N_q(1)=m_q-2\eta_q,\qquad N_q(j)=0\quad(j\notin\{1,2q-1\}).}
\]
In particular, the exceptional **nonzero** coefficients number exactly two if \(q\equiv7,43\pmod{60}\), and zero otherwise. In the two-coefficient case, choose \(t\in L\) with \(t^2=5\), put \(\phi=(1+t)/2\), and the exceptional coefficients are exactly \(a_\pm=1+\phi^{\pm4}\). Whenever \(\epsilon_q=1\), the additional exceptional coefficient is \(a=0\).

## Assumptions and scope
All statements cover every odd prime power, including powers of three and five. A fixed point means \(x\in L\) with \(f_a(x)=x\); zero is always fixed. Coefficients, not permutation-conjugacy or monomial equivalence classes, are counted. A binomial with \(a=0\) is counted as a degenerate member of the specified polynomial family, and its contribution is separately explicit. The nonzero-coefficient permutation criterion is quoted exactly from Tang--Fan [1, Theorem 1.2/Table 1] in its exponent-one specialization: writing \(h=(q+1)/2\) and \(s=(-a)^h\), for \(a\ne0\) admissibility is equivalent to \(s=-1\) or \(s=3\); the second option disappears in characteristic three. The first option satisfies the additional coprimality condition because \(r=1\).

## Proof
**1. Permutation-coefficient count.** For \(a\ne0\), exponentiation \(a\mapsto(-a)^h\) on the cyclic group \(L^\times\) has kernel size \(h\), and its image includes every element of \(K^\times\) (image order \(2(q-1)\)). Thus each of the two distinct values \(-1\) and \(3\) has exactly \(h\) preimages when the characteristic is not three, while only \(-1\) is allowed in characteristic three. The special coefficient \(a=0\) gives \(X^{2q-1}\); this is a permutation precisely when
\[
\gcd(2q-1,q^2-1)=\gcd(3,q+1)=1,
\]
which is equivalent to \(\epsilon_q=1\).

**2. Rigidity of the fixed-point count.** For \(x\ne0\), the equation \(f_a(x)=x\) is \(x^{2(q-1)}=u:=1-a\). The map \(x\mapsto x^{2(q-1)}\) from \(L^\times\) has kernel of order \(2(q-1)\), and its image is the subgroup \(\mu_h=\{u\in L^\times:u^h=1\}\). Hence a nonzero fixed point exists if and only if \(u^h=1\), and in that case there are exactly \(2(q-1)\) of them. This proves the two-point spectrum \(\{1,2q-1\}\). For \(a=0\), \(u=1\) and the larger count always holds whenever the monomial is a permutation.

**3. Exclusion of the norm-one coefficient branch.** Suppose \(a\ne0\), \((-a)^h=-1\), and \(u^h=1\). Because \(h=(q+1)/2\), the first equality implies \(a^{q+1}=1\); the second implies \(u^{q+1}=1\). Taking the norm of \(u=1-a\) gives \(1-\operatorname{Tr}_{L/K}(a)+\operatorname{N}_{L/K}(a)=1\), so \(\operatorname{Tr}(a)=1\) and \(a^2-a+1=0\). Consequently \(u=1-a=a^{-1}\), and \(u^h=1\) forces \(a^h=1\). The equality \((-a)^h=-1\) then forces \(h\) to be odd. But \(a^2-a+1=0\) implies \(a^3=-1\); in odd characteristic \(a\) therefore has even multiplicative order, inconsistent with \(a^h=1\) for odd \(h\). No coefficient in this branch has a nonzero fixed point.

**4. The \(s=3\) branch.** This branch requires characteristic different from three, and \(\operatorname{N}(a)=(-a)^{2h}=9\). If \(u^h=1\), then \(\operatorname{N}(u)=1\), and \(\operatorname{N}(1-u)=9\) gives
\[
(1-u)(1-u^{-1})=9,\qquad u^2+7u+1=0.\tag{*}
\]
The discriminant is \(45\). In characteristic five the only root is \(u=-1\), but \(q\equiv1\pmod4\) makes \(h\) odd and thus \((-1)^h\ne1\). In characteristic other than three or five, if \(5\) is a square in \(K\), both roots of (*) lie in \(K\). The intersection \(K^\times\cap\mu_h\) contains only \(1\) and possibly \(-1\), while neither is a root of (*) (the two evaluations are \(9\) and \(-5\)). Therefore \(5\) must be a nonsquare in \(K\).

Choose \(t\in L\) with \(t^2=5\) and \(t^q=-t\); put \(\phi=(1+t)/2\). Then \(\phi^{q+1}=-1\), \(\phi^2+\phi^{-2}=3\), and the two roots of (*) are \(u_+=-\phi^4\) and \(u_-=-\phi^{-4}\). For either root,
\[
u_\pm^h=(-1)^h(\phi^{q+1})^{\pm2}=(-1)^h.\]
Thus \(u_\pm\in\mu_h\) exactly when \(h\) is even, or \(q\equiv3\pmod4\). Under this condition, \(u_+-1=-3\phi^2\), whence
\[
(-a_+)^h=(u_+-1)^h=(-3)^h\phi^{q+1}=-3\chi_q(3).
\]
The same holds for \(u_-\), using \(\phi^{-2}\). Here \(\chi_q\) is the quadratic character of \(K\). Hence the admissibility equation \((-a)^h=3\) holds for both roots precisely when \(\chi_q(3)=-1\). The three conditions
\[
\chi_q(5)=-1,\qquad q\equiv3\pmod4,\qquad\chi_q(3)=-1
\]
are equivalent to \(q\equiv7\) or \(43\pmod{60}\): when \(\chi_q(5)=-1\), the extension exponent in \(q=p^e\) is odd, so the quadratic-character conditions reduce to quadratic reciprocity in the odd prime \(p\) and give exactly these two invertible residue classes. The roots are distinct and yield the two stated coefficients. No other root of (*) exists, completing the exact histogram.

## Verification
Run `python3 verify.py` using Python 3 without third-party packages. The script constructs exact arithmetic in \(\mathbb F_{p^2}\), enumerates every coefficient and every field element for primes \(p=3,5,7,11,13,17,19\), checks which maps actually permute, compares the fixed-point distribution with the formulas, and additionally verifies the nonsplit quadratic-root identities at 154 primes below 2000. It reports `FIELD_FIXED_POINT_DIAGNOSTICS_OK 7 complete prime fields, 154 nonsplit torus fields through 1999`. These tests are finite diagnostics only; the argument above, including the cited general permutation classification, proves the statement for arbitrary odd prime powers.

## Relationship to prior work
Tang and Fan [1] give the complete coefficient-based permutation classification, including this exponent-one family; Hou and Pallozzi Lavorante [2, Result 1.2] record the earlier exponent-one criterion. Neither is presented here as an original membership criterion. The present assertion instead counts fixed points of the already-classified permutations, isolates the exact two-coefficient exceptional locus, and locates its prime-power congruence support. General finite-field cycle-structure studies do not by themselves give this fixed-point spectrum for the stated binomial family.

## Limitations
The conclusion concerns fixed points only, not cycle lengths greater than one or conjugacy classes. It relies on the published coefficient-permutation classification [1,2]. A relevant unindexed earlier treatment of these fixed points cannot be ruled out by database searching. The finite verification is not a proof for all prime powers. Independent mathematical validation has not been performed.

## References
[1] Zhichao Tang and Xiang Fan, *A complete classification of permutation binomials of the form \(X^r(X^{2(q-1)}+a)\) over finite fields*, arXiv:2611.14162v1 (first publicly submitted 2026-11-10), https://arxiv.org/abs/2611.14162.

[2] Xiang-dong Hou and Vincenzo Pallozzi Lavorante, *New Results on Permutation Binomials of Finite Fields*, arXiv:2111.06533, https://arxiv.org/abs/2111.06533.

[3] Xiang-dong Hou, *Permutation Polynomials of \(\mathbb F_{q^2}\) of the form \(aX+X^{r(q-1)+1}\)*, arXiv:1510.00437 (2015), https://arxiv.org/abs/1510.00437 (historical binomial-classification background).
