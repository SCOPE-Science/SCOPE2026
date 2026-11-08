# Finite square-index columns of Narayana numbers: exact divisor parametrization and sharp maxima

## Finding

Let \(N(a,b)=\frac1a\binom ab\binom a{b-1}\) for integers \(a\ge b\ge2\). Fix an integer \(c\ge2\) and put \(b=c^2\). Define
\[
h=\begin{cases}b-1,&c\text{ even},\\(b-1)/4,&c\text{ odd}.\end{cases}
\]
For every proper divisor pair \(u<v\) of \(h^2\), so that \(uv=h^2\), put
\[
 a(u)=\begin{cases}\frac{u+v+2h}{4},&c\text{ even},\\u+v+2h,&c\text{ odd}.\end{cases}
\]
**The complete set** of integers \(a\ge b\) for which \(N(a,b)\) is a square is precisely \(\{a(u):u<v,\ uv=h^2\}\). Different divisor pairs give different indices. Thus, writing \(\tau\) for the divisor-count function, the number of square entries in the fixed column, including the trivial entry \(N(b,b)=1\), is
\[
\frac{\tau(h^2)-1}{2};
\]
the number of nontrivial square entries with \(a>b\) is \((\tau(h^2)-3)/2\). The largest index in this column admitting a square is exactly
\[
 a_{\max}=\begin{cases}b^2/4,&c\text{ even},\\((b+3)/4)^2,&c\text{ odd}.\end{cases}
\]
There are **no nontrivial squares** at \(b=4\) or \(b=9\); every other square index \(b\ge4\) has at least one nontrivial square but only finitely many. For instance the complete index sets are \(\{4\}\), \(\{9\}\), \(\{16,20,27,64\}\), and \(\{25,27,32,49\}\) at \(b=4,9,16,25\), respectively.

Consequently the correct fixed-index infinitude dichotomy is: for integer \(b>1\), infinitely many integers \(a>b\) have \(N(a,b)\) a perfect square **if and only if \(b\) is not a square**. The infinite nonsquare-index direction is part of existing Pell-equation theory; the new contribution here is the exhaustive finite square-index branch, with counts and sharp maxima, which corrects an explicitly universal infinitude assertion in the cited work.

## Assumptions and scope

All variables \(a,b,c,h,u,v\) are ordinary positive integers with the restrictions specified above. A square means an integer square. The entry at \(a=b\) is included in the complete classification but excluded from the nontrivial count, since it equals \(1\). No claim about cubes or other perfect powers is made. The natural order is fixed \(b\), varying \(a\) over integers strictly larger than \(b\).

## Proof

The classical Narayana identity (Checcoli--D'Adderio, equation (3.1)) is
\[
N(a,b)=\frac{b}{a(a-b+1)}\binom ab^2.
\]
Since a positive rational number whose square is an integer must itself be an integer, it follows that \(N(a,b)\) is a perfect square if and only if \(a b(a-b+1)\) is an integer square. In the square-index branch \(b=c^2\), this is equivalent to the existence of an integer \(y\ge0\) satisfying
\[
 y^2=a(a-b+1)=a(a-d),\qquad d=b-1.
\]
For \(a\ge b=d+1\), both factors are positive, so \(y>0\). Completing the square gives
\[
(2a-d)^2-(2y)^2=d^2.
\]
Set \(U=2a-d-2y\) and \(V=2a-d+2y\). Both are positive integers, \(U<V\), and \(UV=d^2\). Conversely, given such a factor pair with the requisite parity, reconstruct \(a=(U+V+2d)/4\) and \(y=(V-U)/4\); then the displayed identity holds.

**Even \(c\).** Here \(d\) is odd, hence \(U,V\) are odd. Since \(UV=d^2\equiv1\pmod4\), the two factors are congruent modulo \(4\). Therefore \(V-U\) is divisible by \(4\), and \(U+V+2d\) is divisible by \(4\), giving integer \(y\) and \(a\). Every proper factor pair \(u<v\) of \(d^2=h^2\) thus yields \(a=(u+v+2h)/4\), and all solutions arise this way.

**Odd \(c\).** Now \(d=c^2-1\) is a multiple of \(8\). The definitions show \(U\equiv V\pmod4\) and both even. They cannot both be \(2\pmod4\), because \(UV=d^2\) is divisible by \(64\), so both are divisible by \(4\). Write \(U=4u\), \(V=4v\) and \(h=d/4\). Then \(uv=h^2\), and the inverse formulas give \(a=u+v+2h\), \(y=v-u\). Conversely every proper factor pair \(u<v\) of \(h^2\) defines such an integer solution.

In both cases \(u+v\ge2h\), with equality only at \(u=v=h\); proper pairs have \(u+v>2h\). The formulas therefore give \(a>d=b-1\), i.e. \(a\ge b\). One proper pair gives the trivial solution \(a=b\): in the even case \((u,v)=(c-1,c+1)\), and in the odd case \((u,v)=((c-1)/2,(c+1)/2)\). Conversely the trivial solution has \(y=c\), fixing that pair uniquely. The map from pairs to \(a\) is injective because for a fixed product \(h^2\), the sum \(u+h^2/u\) is strictly decreasing as \(u\) increases over \(0<u<h\). As \(h^2\) is a square, it has exactly \((\tau(h^2)-1)/2\) proper unordered positive divisor pairs. Removing the trivial pair proves both counts.

The largest sum \(u+v\) with \(uv=h^2\) and \(u<v\) is \(1+h^2\), achieved uniquely by \((1,h^2)\). This yields \(a_{\max}=(h+1)^2/4=b^2/4\) when \(c\) is even, and \(a_{\max}=(h+1)^2=((b+3)/4)^2\) when \(c\) is odd. The nontrivial count vanishes exactly when \(\tau(h^2)=3\), i.e. when \(h\) is prime. For even \(c\), \(h=(c-1)(c+1)\), prime only for \(c=2\). For odd \(c\), \(h=((c-1)/2)((c+1)/2)\), prime only for \(c=3\). This proves the two exceptional columns.

To complete the **dichotomy** for nonsquare \(b\), write \(b=D s^2\) with squarefree \(D>1\). By the classical Pell theorem, there is a unit \(X+Y\sqrt D>1\) satisfying \(X^2-DY^2=1\). Replace it by its square to ensure \(Y\) even. Its successive positive powers have coordinates \(X_j,Y_j\) with \(Y_j\) even, \(X_j\) increasing, and \(X_j^2-DY_j^2=1\). Put \(d=b-1\) and \(a_j=d(X_j+1)/2\), an integer. For all sufficiently large \(j\) we have \(a_j>b\), and
\[
 a_jb(a_j-b+1)=\frac{d^2D^2s^2Y_j^2}{4}
 =\left(\frac{dDsY_j}{2}\right)^2.
\]
Hence each \(N(a_j,b)\) is a nontrivial square. The \(a_j\) grow strictly, producing infinitely many, as already established by the nonsquare Pell method in the source.

## Verification

The supplementary Python verifier (`verify.py`, standard library only) enumerates every factor pair for 149 square indices \(b=c^2\) with \(2\le c\le150\), checks exact counts, maximal indices, and the square criterion, compares a range of indices by direct enumeration, checks Narayana binomial values exactly at smaller indices, and tests Pell construction witnesses for nonsquare \(b\). Run `python3 verify.py`. Its successful output begins `VERIFY_OK square_indices=149 exact_divisor_families=4678`. These are finite corroborating checks; the proof above is unrestricted.

## Relationship to prior work

Checcoli and D'Adderio, *Perfect powers in Catalan and Narayana numbers* (arXiv:1306.5929, originally posted June 25, 2013), provide the square criterion and the reduction to a generalized Pell equation. Their Theorem 3.2 and abstract assert infinitely many nontrivial squares for **every** fixed \(b>1\). In their notation, the squarefree parameter \(D\) equals \(1\) precisely when \(b\) itself is a square; this changes the Pell equation to a difference of two squares and removes Pell-unit infinitude. Their asserted infinitude contradicts the finite classification above. Their nonsquare-index Pell branch remains valid and is not claimed as new.

The correction here is the precise exceptional branch: a complete divisor parametrization, exact count, sharp maximal index, and the only two empty nontrivial columns. The classification follows elementarily from their square criterion, and that mathematical dependence is acknowledged. Targeted comparisons did not locate a previously published statement of these exact formulas or the correction; historical priority is not conclusively established.

## Limitations

This classifies only perfect **squares**, not higher powers. The new square-index result is an elementary consequence of the preexisting Narayana criterion and does not claim to replace the deeper nonsquare Pell theory. Other literature, including unlocated corrections, could affect priority. Independent mathematical validation has not been performed.

## References

1. S. Checcoli and M. D'Adderio, *Perfect powers in Catalan and Narayana numbers*, arXiv:1306.5929 (first posted 2013-06-25), especially equation (3.1), Theorem 3.2 and its proof. https://arxiv.org/abs/1306.5929 ; lawful full text: https://ar5iv.labs.arxiv.org/html/1306.5929.
2. R. Kavitha, *Generating Infinitely Many Perfect Squares Among Narayana Numbers* (2023), DOI:10.5281/zenodo.7764462, pp. 10-13; related criterion and Pell examples, with no identified finite-square-column classification. https://zenodo.org/records/7764462.
3. Classical Pell-equation existence theorem for nonsquare positive integers, as recalled in Checcoli--D'Adderio, Section 2.
