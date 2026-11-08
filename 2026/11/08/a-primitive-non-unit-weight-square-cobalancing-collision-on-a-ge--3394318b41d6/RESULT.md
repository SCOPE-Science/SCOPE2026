# A primitive non-unit-weight square-cobalancing collision on a genus-one cubic

## Finding
Let \(P(t)=\sum_{j=1}^{t}j^2=t(t+1)(2t+1)/6\) for integers \(t\ge0\). An index \(n\ge1\) is an \((a,b)\) square-cobalancing index when there is an integer \(r\ge1\) with
\[
aP(n)=b\big(P(n+r)-P(n)\big),\qquad a,b\in\mathbb Z_{>0},\quad\gcd(a,b)=1.
\]
For the **primitive coefficient pair \((a,b)=(563,11)\)**, the distinct positive indices \(n=5\) and \(n=142\) are both square-cobalancing indices, with corresponding cobalancers \(r=15\) and \(r=390\). Hence nonuniqueness occurs with **both coefficients nonzero, the right coefficient greater than one, and both indices greater than one**. The two representations correspond to distinct positive integral points on the nonsingular plane cubic
\[
11Y(Y^2-Z^2)=574X(X^2-Z^2).
\]
No assertion is made that these are the only square-cobalancing indices for this pair.

## Assumptions and scope
Every index, cobalancer and coefficient in the displayed definition is an integer in the indicated range. An endpoint \(m=n+r\) must strictly exceed \(n\). The pair \((563,11)\) is coprime because \(563\equiv2\pmod{11}\). The claim establishes two explicit solutions, not a formula for all coefficients or all integral points.

## Proof
For arbitrary positive \(a,b,n\) and \(m>n\), the square-cobalancing equality is exactly
\[
(a+b)P(n)=bP(m).\tag{1}
\]
At \((a,b)=(563,11)\), equation (1) becomes
\[
574P(n)=11P(m).\tag{2}
\]
The four integer values are obtained directly from the cubic polynomial defining \(P\):
\[
\begin{aligned}
P(5)&=55,&P(20)&=2870,\\
P(142)&=964535,&P(532)&=50331190.
\end{aligned}
\]
These give two independent exact equalities:
\[
574\cdot55=11\cdot2870=31570,
\]
\[
574\cdot964535=11\cdot50331190=553643090.
\]
Thus equation (2) holds for \((n,m)=(5,20)\) and \((142,532)\). Their cobalancers \(m-n\) are respectively \(15\) and \(390\). Both are positive; both indices are greater than one and distinct. In the original sums, equivalently,
\[
563\cdot55=11\cdot2815=30965,
\]
\[
563\cdot964535=11\cdot49366655=543033205.
\]
This proves the square-cobalancing assertion.

To identify its Diophantine structure, put \(x=2n+1\) and \(y=2m+1\). The exact identity \(24P(n)=x(x^2-1)\) turns (2) into
\[
11y(y^2-1)=574x(x^2-1).\tag{3}
\]
The two positive integer solutions become \((x,y)=(11,41)\) and \((285,1065)\). Homogenizing (3) yields the displayed projective cubic \(F(X,Y,Z)=0\), where
\[
F=11Y(Y^2-Z^2)-574X(X^2-Z^2).
\]
Its partial derivatives are
\[
F_X=-574(3X^2-Z^2),\quad F_Y=11(3Y^2-Z^2),\quad F_Z=Z(1148X-22Y).
\]
There is no common projective zero of these three derivatives: if \(Z=0\), the first two derivatives force \(X=Y=0\), forbidden in projective space. If \(Z\ne0\), they force \(X^2=Y^2=Z^2/3\), while the third forces \(11Y=574X\). Together these imply \(11^2=574^2\), a contradiction. Thus the cubic is nonsingular. A nonsingular projective plane cubic has genus one; it has the rational point \((11:41:1)\), so it is a genus-one curve with a rational base point. This structural observation does not classify its other integral points.

## Verification
The accompanying `checker.py` uses arbitrary-precision integer arithmetic and two distinct evaluations of the square sums: direct summation and the closed polynomial. It checks the coprimality, both original weighted identities, their endpoint ratio identities and their points on the cubic. A separate bounded scan through \(1\le n\le10000\) finds precisely the two displayed indices in that interval. That bounded observation is not an infinite completeness proof. Executing `python checker.py` reproduces `verification_output.txt`.

## Relationship to prior work
Cui, Cui, Davis, Durmić, Hu, Liu, Miller, Ren, Smith Reina and Sosis (first public preprint 5 December 2022) define these square-cobalancing indices in Definition 5.2 and ask in Section 6 whether some coefficients have more than one. Their plotted numerical range \(1\le a,b\le120\) supplies no example; the present coefficient \(a=563\) lies outside that range. Their evidence is not a uniqueness theorem.

The known square-pyramidal product \(P(115)=P(11)P(14)=506\cdot1015\), recorded in OEIS A374500 (2024), already implies **other** nonunique square-cobalancing examples with \(b=1\) and one index \(n=1\). The broad existential conclusion is therefore not asserted as new. The present claim isolates the genuinely nondegenerate situation \(b>1\) and both indices \(n>1\). That prior product identity neither states nor entails the explicit \(574:11\) ratio collision between \((P(5),P(20))\) and \((P(142),P(532))\). The common cross-product \(P(20)P(142)=P(5)P(532)=2768215450\) is itself not square-pyramidal, since \(P(2024)<2768215450<P(2025)\).

Related work on ordinary (unsquared) \((a,b)\)-type cobalancing in arithmetic progressions addresses a different summand and does not give (2). Literature searches found no source identifying the two nontrivial solutions for this primitive pair; unindexed equivalences remain possible.

## Limitations
Only the stated explicit coefficient pair and the two displayed indices are proved. No minimality in the coefficients, no classification of all indices, no infinitude of nonunique coefficient pairs and no Mordell–Weil computation is claimed. The bounded scan is supporting evidence only. The known OEIS product example already covers the weaker claim that *some* coefficient pair has multiple square-cobalancing indices; the distinguishing content here is the primitive non-unit right coefficient and two nontrivial indices. Independent validation has not been performed.

## References
1. H. Cui et al., *Sums of Reciprocals of Recurrence Relations*, arXiv:2212.02639v1 (public 2022-12-05), Definition 5.2, Figure 2 and Section 6. Author-hosted full text: https://web.williams.edu/Mathematics/sjmiller/public_html/math/papers/SumReciprocalsRecurrences_EurekaUrop20.pdf.
2. OEIS A000330, *Square pyramidal numbers*, https://oeis.org/A000330.
3. OEIS A374500, *Square pyramidal numbers that are products of smaller square pyramidal numbers*, created 2024-07-09, https://oeis.org/A374500.
4. *Balances in the Set of Arithmetic Progressions*, Axioms 10 (2021), 350, https://www.mdpi.com/2075-1680/10/4/350 (ordinary, unsquared case).
