# An exact arithmetic-progression onset law for short-interval divisor multiplicities

## Finding
For integers \(n\ge1\), reals \(y>0\) and \(\lambda>1\), write
\[
\tau(n;y,\lambda y)=\#\{d\mid n:y<d\le\lambda y\},\qquad
H_{\ge r}(X,y,\lambda y)=\#\{1\le n\le X:\tau(n;y,\lambda y)\ge r\}.
\]
For every integer \(r\ge2\), set
\[
a=1+\left\lfloor\frac{r-1}{\lambda-1}\right\rfloor,\quad
b=a+r-1,\quad L=\operatorname{lcm}(a,a+1,\ldots,b),\quad
T=\min\{b+1,\lambda a\}.
\]
Then \(b<T\), and **for all real \(y>0\) and \(0\le X\le Ty\)**,
\[
\boxed{H_{\ge r}(X,y,\lambda y)
=\max\{0,\lfloor X/L\rfloor-\lfloor by/L\rfloor\}.}
\]
More precisely, each integer \(n\) with \(by<n\le Ty\) has at least \(r\) such divisors if and only if \(L\mid n\), in which case it has **exactly** \(r\), corresponding to the complementary divisors \(a,a+1,\ldots,b\).

For \(y\ge L/(T-b)\) the first such integer is
\[
\boxed{m_r(y,\lambda)=L\left(\left\lfloor\frac{by}{L}\right\rfloor+1\right).}
\]
For every fixed \(r\) and \(\lambda\), this has the sharp leading slope \(m_r(y,\lambda)/y\to b\), and the integer \(b\) changes in explicit steps as \(\lambda\) crosses values \(1+(r-1)/j\). In the dyadic case \(\lambda=2\), the complete initial regime is
\[
H_{\ge r}(X,y,2y)=\max\left\{0,\left\lfloor\frac{X}{L_r}\right\rfloor-\left\lfloor\frac{(2r-1)y}{L_r}\right\rfloor\right\},\quad
0\le X\le2ry,
\]
where \(L_r=\operatorname{lcm}(r,r+1,\ldots,2r-1)\). In particular, \(L_2=6\), \(L_3=60\), and \(L_4=420\).

## Assumptions and scope
The parameter \(\lambda\) is any fixed real greater than one; \(r\) is an integer at least two; \(y>0\) and \(X\ge0\) are real. Divisors are positive. The lower divisor-interval endpoint \(y\) is open and the upper endpoint \(\lambda y\) is closed. The count starts with positive integers \(n\), and the exact counting identity is asserted only for \(X\le Ty\). Outside that range, new complementary-divisor patterns can appear. The least-integer identity additionally assumes \(y\ge L/(T-b)\).

## Proof
Put \(C=n/y\). Every divisor \(d\) counted by \(\tau(n;y,\lambda y)\) corresponds bijectively under \(t=n/d\) to an integer \(t\) with
\[
\frac C\lambda\le t<C,\qquad t\mid n.
\]
Suppose there are at least \(r\) such integers, with smallest \(u\) and \(r\)-th smallest \(v\). Distinctness gives \(v\ge u+r-1\). Since \(v<C\le\lambda u\), it follows that \((\lambda-1)u>r-1\), so \(u\ge a\). Consequently \(C>v\ge u+r-1\ge b\), proving that no \(n\le by\) is counted.

Now assume \(b<C\le T\). Because \(a\) is the least positive integer satisfying \((\lambda-1)a>r-1\), we have \(\lambda(a-1)\le b-1<b<C\), hence every eligible complementary integer \(t\) is at least \(a\). Since \(C\le T\le b+1\), all eligible complementary integers are at most \(b\). On the other hand, \(C>b\) and \(C\le T\le\lambda a\) imply that every integer \(t\in\{a,\ldots,b\}\) satisfies \(C/\lambda\le a\le t\le b<C\). Thus these are **exactly** the \(r\) integer candidates. All divide \(n\) exactly when their least common multiple \(L\) divides \(n\); no extra candidates exist. Therefore on \(by<n\le Ty\), the event \(\tau(n;y,\lambda y)\ge r\) equals \(L\mid n\), and the multiplicity is exactly \(r\).

Counting multiples of \(L\) in \((by,X]\) yields the displayed floor formula; below \(by\) the count is zero. Since \((\lambda-1)a>r-1\), we have \(\lambda a>b\), and also \(b+1>b\), whence \(T>b\). The first multiple of \(L\) above \(by\) is \(m=L(\lfloor by/L\rfloor+1)\), with \(by<m\le by+L\). If \(y\ge L/(T-b)\), then \(m\le Ty\), proving the least-integer formula. Finally \(0<m-by\le L\) proves \(m/y\to b\) for fixed \(r,\lambda\).

## Verification
The standalone `onset_checker.py` checks the all-integer equivalent for rational \(\lambda\) using exact fractions and a direct divisor enumeration. It exhaustively checked 153,292 triples \((\lambda,r,y,n)\), including \(\lambda\in\{5/4,3/2,7/4,2,5/2,3,4,7\}\), \(2\le r\le6\), and \(1\le y\le30\) with bounded \(n\), checking **exactly** \(r\) counted divisors in the initial interval when \(L\mid n\), and fewer than \(r\) otherwise. It is a finite diagnostic; the proof above covers all parameters.

## Relationship to prior work
Ford, Gabdullin and Pratt (2026, arXiv:2611.15534v1) investigate \(H_{\ge r}(X,y,2y)\) and establish its order of magnitude in a large-parameter asymptotic regime. Their Theorem 1.1 imposes \(100\le y\le X/100\), a sufficiently large auxiliary scale and a bound on \(r\). Their introduction, theorem, and main preliminaries do not state this exact first-support law. The present result determines an initial, near-diagonal window (and general ratios \(\lambda\)); it does not improve or imply their far-range asymptotic. Ford and Tenenbaum (2007, arXiv:math/0607460) analyze the proportion of integers with multiple divisors in short intervals, especially near the shrinking-width limit. Their investigated limiting densities do not imply the exact integer-by-integer first-support pattern. See REVIEW.md for the qualified literature comparison.

## Limitations
The first-wave band \(X\le Ty\) is a guaranteed range of exact classification, not asserted to be maximal for every \(r\) and \(\lambda\). The least-integer formula has an explicit sufficient large-\(y\) threshold, not a claim that this threshold is necessary. No formula is established here for the full counting function at arbitrarily large \(X\). An unindexed equivalent elementary formulation remains possible; the absence of a matching search hit is not proof of uniqueness.

## References
1. K. Ford, M. R. Gabdullin and K. Pratt, *Integers with many divisors in a dyadic interval*, arXiv:2611.15534v1 (first public version 2026-11-11), https://arxiv.org/html/2611.15534v1.
2. K. Ford and G. Tenenbaum, *The distribution of integers with at least two divisors in a short interval*, arXiv:math/0607460 (2006/2007), https://arxiv.org/abs/math/0607460.
