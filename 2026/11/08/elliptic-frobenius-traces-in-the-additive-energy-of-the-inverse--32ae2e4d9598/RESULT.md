# Elliptic Frobenius traces in the additive energy of the inverse-square graph

## Finding

For every prime power \(q=p^m\), let \(\mathbb F_q\) be the field of order \(q\), and let the inverse-square graph be
\[
H_q=\{(x,x^{-2}):x\in\mathbb F_q^\times\}\subset\mathbb F_q^2.
\]
Its ordered additive energy \(\mathcal E_q\) is the cardinality of the set of quadruples \((x_1,x_2,x_3,x_4)\in(\mathbb F_q^\times)^4\) satisfying
\[
x_1+x_2=x_3+x_4,\qquad x_1^{-2}+x_2^{-2}=x_3^{-2}+x_4^{-2}.
\]
Write \(\chi_q\) for the quadratic character of \(\mathbb F_q\) with \(\chi_q(0)=0\), when \(p\) is odd. In characteristic at least five define the smooth elliptic curve and its Frobenius trace by
\[
\mathcal C:\ v^2=(1-4z)(1-4z^2),\qquad
 a_q=q+1-\#\mathcal C(\mathbb F_q)
 =-\sum_{z\in\mathbb F_q}\chi_q((1-4z)(1-4z^2)).
\]
Then **for every prime power** the exact energy is
\[
\boxed{\mathcal E_q=\begin{cases}
(q-1)(3q-5),&p=2,\\
(q-1)(3q-9-3\chi_q(-1)),&p=3,\\
(q-1)(3q-10-2\chi_q(-1)-2\chi_q(-3)-a_q),&p\ge5.
\end{cases}}
\]
For each prime \(p\ge5\) the traces over its extension fields are determined by a single base-field point count:
\[
a_{p^0}=2,\quad a_{p^1}=p+1-\#\mathcal C(\mathbb F_p),\quad
 a_{p^m}=a_{p^1}a_{p^{m-1}}-p\,a_{p^{m-2}}\quad(m\ge2).
\]
The Weil bound gives \(\lvert a_q\rvert\le2\sqrt q\). The elliptic curve has rational \(j\)-invariant \(35152/9\), so the finite-field energy contains an actual elliptic oscillatory term rather than a solely polynomial correction.

For any nontrivial additive character \(\psi\) of \(\mathbb F_q\), the same statement is an exact unnormalized fourth-moment identity:
\[
\boxed{\sum_{A,B\in\mathbb F_q}\left|\sum_{x\in\mathbb F_q^\times}\psi(Ax+Bx^{-2})\right|^4=q^2\mathcal E_q.}
\]

## Assumptions and scope

All field orders are arbitrary prime powers \(q=p^m\), with integers \(m\ge1\). Energy counts **ordered** quadruples, with graph coordinates evaluated in the same field. The elliptic-curve formula applies only when \(p\ge5\); in characteristics two and three the displayed separate formulas replace the singular cubic model. The character is the multiplicative quadratic character in odd characteristic, extended by zero at zero. Point counts on \(\mathcal C\) include its unique point at infinity. The Fourier identity uses the **unscaled** additive character sum and sums both frequency variables over the entire field.

## Proof

**1. Zero first-coordinate sum, odd characteristic.** For \(p\) odd, \(x_1+x_2=0\) forces the ordered pair \((x,-x)\), whose second-coordinate sum is \(2x^{-2}\). Each such second-coordinate value has exactly two preimages \(x\in\mathbb F_q^\times\). Consequently this first-coordinate sum contributes \(2(q-1)\) to \(\mathcal E_q\).

**2. Every nonzero first-coordinate sum.** Fix \(s\in\mathbb F_q^\times\). Put \(x_1=st\), \(x_2=s(1-t)\), \(z=t(1-t)\), excluding \(z=0\). The number of ordered pairs with the specified \(z\) is
\[
h(z)=1+\chi_q(1-4z),
\]
including the repeated-root case. Their second-coordinate sum equals \(s^{-2}f(z)\) with
\[
f(z)=\frac{1-2z}{z^2}.
\]
Thus the ordered collision count for each fixed nonzero \(s\) is
\[
\sum_{z,w\ne0\,:\,f(z)=f(w)}h(z)h(w).
\]
Multiplying through the denominators factors the condition as
\[
(z-w)(z+w-2zw)=0.
\]
The diagonal contributes
\[
\sum_{z\ne0}h(z)^2=(q-1)+2(-1)+(q-2)=2q-5,
\]
since \(\sum_{z\ne0}\chi_q(1-4z)=-1\), and exactly one nonzero value \(z=1/4\) makes its discriminant vanish.

**3. Non-diagonal collisions.** The second factor of the collision equation yields the involution
\[
w=\frac{z}{2z-1},\qquad z\notin\{0,1/2,1\}.
\]
It satisfies \(1-4w=(1-4z^2)/(2z-1)^2\), so
\[
\chi_q(1-4w)=\chi_q(1-4z^2).
\]
The off-diagonal contribution for each \(s\ne0\) is therefore
\[
\Omega_q=\sum_{z\notin\{0,1/2,1\}}
\bigl(1+\chi_q(1-4z)\bigr)
\bigl(1+\chi_q(1-4z^2)\bigr).
\]
The two linear or quadratic character sums with the three points removed both equal
\[
-1-\chi_q(-1)-\chi_q(-3).
\]

**4. Elliptic correction, characteristic at least five.** Write \(P(z)=(1-4z)(1-4z^2)\). For \(p\ge5\), its roots \(1/4,1/2,-1/2\) are distinct, hence \(v^2=P(z)\) is a nonsingular genus-one curve with its rational point at infinity. We have
\[
\sum_{z\in\mathbb F_q}\chi_q(P(z))=-a_q.
\]
Among the three excluded values, \(P(0)=1\), \(P(1/2)=0\), and \(P(1)=9\); their quadratic characters contribute \(1+0+1=2\). Expanding the previous sum gives
\[
\Omega_q=(q-3)-2(1+\chi_q(-1)+\chi_q(-3))-(a_q+2)
=q-7-2\chi_q(-1)-2\chi_q(-3)-a_q.
\]
Summing the zero-sum contribution and the \(q-1\) identical nonzero-sum contributions yields
\[
\mathcal E_q=2(q-1)+(q-1)(2q-5+\Omega_q),
\]
which proves the third formula. The transformation of the three roots to Legendre parameter \(3/4\) gives \(j=256(1-\lambda+\lambda^2)^3/[\lambda^2(1-\lambda)^2]=35152/9\). The Frobenius recurrence and Weil bound are standard consequences of the two Frobenius eigenvalues of an elliptic curve over \(\mathbb F_p\).

**5. Characteristic three.** The same collision and character-sum argument remains valid, except \(P(z)=(1-z)^2(1+z)\) and \(P(1)=0\). Thus
\[
\sum_z\chi_q(P(z))=-\chi_q(-1),\qquad
\Omega_q=q-6-3\chi_q(-1).
\]
Using the same diagonal and zero-sum contributions gives
\[
\mathcal E_q=(q-1)(3q-9-3\chi_q(-1)).
\]
The cubic is singular in this characteristic, so no elliptic trace is claimed.

**6. Characteristic two.** Frobenius squaring is an additive bijection, and sending a point \((x,x^{-1})\) to \((x,(x^{-1})^2)\) preserves all additive quadruple equations. It suffices to count the inverse graph. When the first-coordinate sum is zero, all \(q-1\) ordered pairs have the same second sum, yielding \((q-1)^2\) energy. When it is nonzero, the two sums determine the product \(x_1x_2\) and hence determine an unordered pair with two distinct members. Each of the \(q-1\) nonzero sums contributes \(2(q-2)\) energy. Therefore
\[
\mathcal E_q=(q-1)^2+2(q-1)(q-2)=(q-1)(3q-5).
\]

**7. Fourth moment.** Expand the fourth powers of the displayed character sums and sum separately over \(A\) and \(B\). Orthogonality gives a factor \(q^2\) exactly for the additive quadruples defining \(\mathcal E_q\), and zero otherwise. This proves the stated moment identity without any additional assumptions.

## Verification

Run `python3 verify.py` with a standard Python installation. It independently implements multiplication and inversion in explicit prime and extension fields, enumerates ordered graph-pair sums and their collisions, evaluates the predicted character sums, and checks equality for 23 prime fields and nine non-prime fields. It also verifies the elliptic trace recurrence in two quadratic extensions. Expected final line: `VERIFY_OK prime_field_cases=23 extension_cases=9 direct_energies=32 Frobenius_recursions=2 characteristic_branches=2,3,>=5`. Finite tests corroborate but are not substituted for the complete algebraic proof.

## Relationship to prior work

Katz and Koester [1] give a foundational general additive-energy result, not an exact formula for the inverse-square graph. Bourgain and Garaev [2] analyze reciprocals of intervals and multilinear Kloosterman sums, not the complete two-coordinate inverse-square graph. Classical fourth moments of the inverse graph \(\{(x,x^{-1})\}\), discussed explicitly by Kowalski [3], are elementary and do not imply the elliptic oscillatory correction above. Calderón, de Velasco and Zárate [4] consider moments averaged over a family of Dirichlet characters for a differently parametrized generalized Kloosterman sum. The accessible abstract does not imply a fixed-character two-frequency moment for the present inverse-square graph, but full-text comparison remains an open historical-priority risk.

## Limitations

The identity is specific to the graph of inverse squares and its full two-parameter unweighted fourth moment. It does not evaluate any individual exponential sum or higher moment, and it does not classify extremizing weights. A historical originality comparison was performed against accessible publications and closely related published graph-energy results; it is not an exhaustive priority certificate. Independent mathematical audit has not been performed.

## References

[1] N. H. Katz and P. Koester, *On additive doubling and energy*, arXiv:0802.4371v1 (first public version 2008-02-29), https://arxiv.org/abs/0802.4371.

[2] J. Bourgain and M. Z. Garaev, *Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*, arXiv:1211.4184v1 (2012-11-18), https://arxiv.org/abs/1211.4184.

[3] E. Kowalski, *The fourth moment of Kloosterman sums* (2010-02-26), https://blogs.ethz.ch/kowalski/2010/02/26/the-fourth-moment-of-kloosterman-sums/.

[4] C. Calderón, M. J. de Velasco and M. J. Zárate, *An explicit formula for the fourth moment of certain exponential sums*, Acta Math. Hung. **130** (2011), 203–222, doi:10.1007/s10474-010-0043-5.
