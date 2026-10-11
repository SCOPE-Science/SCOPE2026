# A support-exponent obstruction for Jordan-totient product collisions

## Finding
For positive integers \(a,b,s\), define
\[
F_{a,b,s}(n)=n^aJ_s(n)^b,
\]
where
\[
J_s(n)=n^s\prod_{p\mid n}\left(1-\frac1{p^s}\right)
\]
is Jordan's totient function.

Suppose
\[
m\ne n
\quad\text{and}\quad
F_{a,b,s}(m)=F_{a,b,s}(n).
\]
Let
\[
S=\{p:p\mid m,\ p\nmid n\},
\qquad
T=\{q:q\mid n,\ q\nmid m\},
\]
and define
\[
e_r=
\begin{cases}
\nu_r(m),&r\in S,\\
\nu_r(n),&r\in T.
\end{cases}
\]
Then \(S\) and \(T\) are both nonempty and
\[
\prod_{r\in S\cup T}
r^{(a+sb)e_r-2sb}<1.
\]

In the open parameter range
\[
a<sb,
\]
this is equivalently
\[
\prod_{\substack{r\in S\cup T\\e_r=1}}
r^{sb-a}
>
\prod_{\substack{r\in S\cup T\\e_r\ge2}}
r^{(a+sb)e_r-2sb}.
\]
Thus any collision in that range must contain at least one prime that occurs to exponent \(1\) on exactly one side.

A positive integer is powerful if every prime dividing it occurs with exponent at least \(2\). Therefore, for every
\[
a,b,s\ge1,
\]
the restriction of
\[
n\longmapsto n^aJ_s(n)^b
\]
to the powerful positive integers is injective.

For \(s\ge3\) and \(a<sb\), this gives both a natural infinite-domain positive result and a quantitative obstruction on any possible collision in the unresolved case of Question 31 of Noppakaew and Pongsriiam.

## Assumptions and scope
All variables are positive integers. The convention \(J_s(1)=1\) is used. The integer \(1\) is treated as powerful vacuously.

The result does not prove injectivity on all positive integers when \(s\ge3\) and \(a<sb\). It gives a necessary condition for a collision and proves injectivity on the powerful subdomain.

## Proof
For
\[
n=\prod_{p\mid n}p^{v_p},
\]
the prime-power factorization of \(F_{a,b,s}\) is
\[
F_{a,b,s}(n)
=
\prod_{p\mid n}
p^{(a+sb)v_p-sb}(p^s-1)^b.
\]

Assume
\[
F_{a,b,s}(m)=F_{a,b,s}(n)
\]
with \(m\ne n\).

First, the prime supports cannot be properly nested. Suppose, for example, that every prime divisor of \(m\) divides \(n\), while \(q\) divides \(n\) but not \(m\). Cancel from the two factorizations the common factors
\[
(p^s-1)^b
\]
for primes occurring in both supports. The prime \(q\) divides the remaining prime-power part on the \(n\)-side, but on the \(m\)-side only prime bases from the common support remain, so \(q\) cannot divide that side. This is impossible. The reverse nesting is symmetric. Hence \(S\) and \(T\) are both nonempty.

Let
\[
c=a+sb,
\]
and define
\[
L_S=\prod_{p\in S}p^{c\nu_p(m)-sb},
\qquad
C_S=\prod_{p\in S}(p^s-1)^b,
\]
and similarly
\[
L_T=\prod_{q\in T}q^{c\nu_q(n)-sb},
\qquad
C_T=\prod_{q\in T}(q^s-1)^b.
\]

After the common cyclotomic factors are cancelled, every prime-power factor belonging to \(L_S\) must be supplied on the other side by \(C_T\): its prime base lies neither in the common support nor in \(T\). Thus
\[
L_S\mid C_T.
\]
By symmetry,
\[
L_T\mid C_S.
\]
Therefore
\[
L_S\le C_T
<
\prod_{q\in T}q^{sb}
\]
and
\[
L_T\le C_S
<
\prod_{p\in S}p^{sb},
\]
where the strict inequalities use
\[
q^s-1<q^s
\quad\text{and}\quad
p^s-1<p^s.
\]

Multiplying gives
\[
\left(
\prod_{p\in S}p^{c\nu_p(m)-sb}
\right)
\left(
\prod_{q\in T}q^{c\nu_q(n)-sb}
\right)
<
\left(
\prod_{p\in S}p^{sb}
\right)
\left(
\prod_{q\in T}q^{sb}
\right).
\]
After division,
\[
\prod_{r\in S\cup T}
r^{ce_r-2sb}<1,
\]
which is the claimed obstruction.

Now assume
\[
a<sb.
\]
If \(e_r=1\), then
\[
ce_r-2sb=a-sb<0.
\]
If \(e_r\ge2\), then
\[
ce_r-2sb
=
(a+sb)e_r-2sb
\ge2a>0.
\]
Moving the negative-exponent factors to the other side yields
\[
\prod_{\substack{r\in S\cup T\\e_r=1}}
r^{sb-a}
>
\prod_{\substack{r\in S\cup T\\e_r\ge2}}
r^{(a+sb)e_r-2sb}.
\]
In particular, the left product cannot be empty, so at least one unique-support prime has exponent \(1\).

Finally, suppose both \(m\) and \(n\) are powerful. Then every \(e_r\ge2\), so every exponent
\[
ce_r-2sb
\]
is at least \(2a>0\). The obstruction product is then strictly greater than \(1\), contradicting the required strict inequality. Hence two distinct powerful integers cannot collide.

If two powerful integers have the same prime support, equality of the two values cancels the factors
\[
(p^s-1)^b
\]
and unique factorization gives equality of each linear exponent
\[
(a+sb)v_p-sb,
\]
hence equality of every \(v_p\). Thus the restriction is injective, including the same-support case.

## Verification
The accompanying `verify.py` independently evaluates Jordan's totient function from prime factorizations and checks the powerful-number corollary for every powerful integer up to \(20000\) throughout the grid
\[
3\le s\le6,\qquad 1\le b\le3,\qquad 1\le a<sb.
\]

The checker also verifies the published collision
\[
J_3(28268)=J_3(28710)
\]
from the recent work of Fu. Both integers contain exponent-one prime factors, which is consistent with the structural role of the squarefree layer emphasized by the theorem.

These finite checks are regression evidence only. The collision obstruction and powerful-domain injectivity are proved symbolically above.

## Relationship to prior work
Noppakaew and Pongsriiam prove that
\[
n\longmapsto n^aJ_s(n)^b
\]
is injective when \(s=2\), and for general \(s\) when
\[
a\ge sb.
\]
They explicitly ask whether it is injective when
\[
s\ge3,\qquad a<sb.
\]
Their proof observes that the condition \(a\ge sb\) is used only in the product-size comparison that excludes incomparable prime supports.

The present result refines that comparison rather than discarding it. Multiplying the two divisibility inequalities produces an exact support-exponent imbalance condition in the unresolved range. It isolates exponent-one primes as necessary for any collision and closes the entire powerful subdomain for every parameter choice.

Fu recently proved that the bare Jordan functions \(J_3,J_4,J_6\) are not injective and developed a prime-support framework for their collisions. That work concerns \(J_s\) itself, corresponding to the absence of the positive \(n^a\) factor, and does not state the weighted support inequality above or injectivity of \(n^aJ_s(n)^b\) on powerful integers.

Targeted searches for the exact product, Question 31, powerful-number restrictions, symmetric-support collisions, and the exponent-one obstruction did not locate a prior statement of this result.

## Limitations
The theorem does not settle Question 31 on all positive integers. In the open range
\[
a<sb,
\]
a collision involving exponent-one primes remains possible in principle.

The weighted inequality is necessary, not sufficient. It does not characterize all candidate symmetric-support sets.

The strongest residual originality risk is an unindexed observation that extracts the same powerful-number corollary from the size comparison in the 2023 proof. The focal full text, a recent full-text paper on noninjectivity of Jordan totients, targeted web searches, published-finding corpus semantic searches, and the closest OEIS powerful-Jordan entry were checked without locating this statement.

## References
1. Passawan Noppakaew and Prapanpong Pongsriiam, “Product of Some Polynomials and Arithmetic Functions,” Journal of Integer Sequences 26 (2023), Article 23.9.1. First verified public version: 2 November 2023. Primary MSC 11A25.
2. Hang Fu, “On the noninjectivity of Jordan's totient functions,” arXiv:2609.23901v1, 20 September 2026.
3. OEIS A001694, powerful numbers.
4. OEIS A379716, the second Jordan totient function evaluated on the powerful numbers.
