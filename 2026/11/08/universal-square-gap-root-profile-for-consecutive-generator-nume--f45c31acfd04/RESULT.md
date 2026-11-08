# Universal square-gap root profile for consecutive-generator numerical semigroups

## Finding

For every integer \(m\ge2\), put \(S_m=\langle m,m+1\rangle\). For real \(0\le u\le v\le1\), define
\[
G_m(u,v)=\#\{j\in\mathbb Z:0\le j<m,\ u\le j/m<v,\ j^2\notin S_m\}.
\]
There is an absolute constant \(C>0\) such that, simultaneously for all \(m\ge2\) and all \(u,v\),
\[
\left|G_m(u,v)-m\int_u^v(1-t^2)\,dt\right|
\le C m^{5/6}\log(2m).
\]
In particular, the number of positive square gaps of \(S_m\) is
\[
G_m(0,1)=\frac{2m}{3}+O\bigl(m^{5/6}\log(2m)\bigr),
\]
and the limiting *counting measure normalized by* \(m\) of the positive square-gap roots is the measure with density \(1-t^2\) on \([0,1]\) (of total mass \(2/3\), not a probability measure). The implied constants are absolute and do not depend on the prime factorization of \(m\).

## Assumptions and scope

The numerical semigroup \(S_m\) consists of nonnegative integer combinations of \(m\) and \(m+1\). A *square gap* is a positive perfect square not belonging to \(S_m\). The integers \(j\) above are nonnegative; zero is never a gap. Since the conductor of \(S_m\) is \(m(m-1)\), every square with root at least \(m\) belongs to \(S_m\). Thus the range \(0\le j<m\) captures every square gap. Interval endpoints in the definition use the half-open condition \(u\le j/m<v\), including \(u=v\) as the empty interval. The result applies to all integers \(m\ge2\), whether prime or composite.

## Proof

**1. An exact membership test.** Write a nonnegative integer uniquely as \(z=qm+r\), with \(q\ge0\) and \(0\le r<m\). Then
\[
z\in S_m\quad\Longleftrightarrow\quad q\ge r.
\]
Indeed, if \(q\ge r\), then \(z=(q-r)m+r(m+1)\). Conversely, any \(z=am+b(m+1)\), with \(a,b\ge0\), has \(r\equiv b\pmod m\); hence \(b=r+\ell m\) for some \(\ell\ge0\), and \(q=a+b+\lfloor b/m\rfloor\ge r\). (Equivalently, reduce the coefficient of \(m+1\) modulo \(m\).)

For \(0\le j<m\), define
\[
x_j=j/m,\qquad y_j=(j^2\bmod m)/m.
\]
The quotient in division of \(j^2\) by \(m\) is
\[
q_j=m x_j^2-y_j.
\]
The membership criterion therefore yields the exact equivalence
\[
j^2\notin S_m\quad\Longleftrightarrow\quad y_j>\frac{m}{m+1}x_j^2.\tag{1}
\]
The strict inequality correctly excludes zero and all points on the curve.

**2. A uniform complete quadratic-sum bound.** Let \(e(z)=\exp(2\pi i z)\). For arbitrary integers \(h,k\), define
\[
T_m(h,k)=\sum_{j=0}^{m-1}e\left(\frac{hj+kj^2}{m}\right).
\]
If \(k=0\) and \(0<|h|<m\), the geometric sum vanishes. If \(k\ne0\), expand the square of its absolute value and substitute \(j=\ell+d\) modulo \(m\):
\[
|T_m(h,k)|^2=\sum_{d=0}^{m-1}e\left(\frac{kd^2+hd}{m}\right)
\sum_{\ell=0}^{m-1}e\left(\frac{2kd\ell}{m}\right).
\]
The inner sum vanishes unless \(m\mid2kd\), in which case it is \(m\). There are exactly \(\gcd(2k,m)\) such residues \(d\). Taking absolute values gives
\[
|T_m(h,k)|^2\le m\gcd(2k,m)\le2|k|m.\tag{2}
\]
This calculation is valid for every modulus and avoids assuming that it is prime.

**3. Two-dimensional rectangle discrepancy.** Let \(D_m^*\) be the normalized star discrepancy of the \(m\) points \((x_j,y_j)\) in \([0,1)^2\). The standard two-dimensional Erdős–Turán–Koksma inequality gives, for each integer \(1\le H<m\),
\[
D_m^*\le C_0\left(\frac1H+
\sum_{\substack{|h|,|k|\le H\\(h,k)\ne(0,0)}}
\frac{|T_m(h,k)|}{m\max(1,|h|)\max(1,|k|)}\right).
\]
The terms \(k=0\) vanish. For \(k\ne0\), use (2) and the elementary harmonic-sum estimates to obtain
\[
D_m^*\ll H^{-1}+m^{-1/2}(\log(2H))\sqrt H.
\]
Choosing \(H=\lfloor m^{1/3}\rfloor\) for \(m\ge8\) (and enlarging the absolute constant for smaller \(m\)) gives
\[
D_m^*\ll m^{-1/3}\log(2m).\tag{3}
\]
By inclusion–exclusion, the normalized counting error for any axis-parallel half-open rectangle is at most \(4D_m^*\).

**4. Transfer from rectangles to the square-gap region.** Set \(f_m(x)=\frac{m}{m+1}x^2\). For any \(0\le u\le v\le1\), divide \([u,v)\) into at most \(K\) half-open vertical intervals of width at most \(1/K\). Since \(f_m\) is increasing and has Lipschitz constant at most \(2\), the portion of the region \(y>f_m(x)\) over each strip is squeezed between the rectangles with lower vertical boundaries \(f_m\) at the right and left strip endpoints. Their total area difference is at most \(2/K\). In the lower rectangle, inclusion of its lower vertical boundary is harmless because the right endpoint of the strip is excluded and \(f_m\) is strictly increasing on \([0,1]\); in the upper rectangle the boundary may be included. Thus the strict-inequality convention in (1) is respected without an unbounded boundary error.

Using the rectangle discrepancy bound on both approximating unions,
\[
\left|G_m(u,v)-m\int_u^v\bigl(1-f_m(t)\bigr)\,dt\right|
\ll m/K+mK D_m^*.
\]
Take \(K=\lceil m^{1/6}\rceil\) and use (3): this error is \(O(m^{5/6}\log(2m))\). Finally,
\[
0\le m\int_u^v\left(t^2-f_m(t)\right)\,dt
\le\frac{m}{m+1}\int_0^1t^2\,dt<1,
\]
so replacing \(1-f_m(t)\) by \(1-t^2\) changes the estimate by less than one. This proves the theorem uniformly in both interval endpoints. Setting \(u=0,v=1\) gives the count, since \(\int_0^1(1-t^2)\,dt=2/3\). \(\square\)

## Verification

The standalone `check.py` uses only the Python standard library. It compares the exact semigroup membership test with direct nonnegative-generator enumeration for thousands of small instances, separately checks finite samples of the quadratic-sum bound, and prints exact square-gap counts for selected moduli. Reproduce its output with `python check.py`; the accompanying `check-output.txt` is the expected output. None of these experiments constitutes a proof of the asymptotic statement: the latter depends on the exact membership criterion, the complete exponential-sum bound, and the stated standard discrepancy inequality.

## Relationship to prior work

Chappelon and Ramírez Alfonsín (2020), *The Square Frobenius Number*, study the largest missing square of numerical semigroups, including semigroups generated by consecutive integers. Binner (2021), *Proofs of Chappelon and Alfonsín Conjectures On Square Frobenius Numbers and its Relationship to Simultaneous Pell's Equations*, develops the maximum-gap theory and gives a quotient–remainder membership test (Lemma 6). These results concern the location of the last square gap, not the number or normalized spatial distribution of all square-gap roots. The exact test used here is classical and not claimed new; the statement of interest is the uniform quantitative root profile. The analytic ingredients (complete quadratic sums and Erdős–Turán–Koksma) are standard; the application to square-gap enumeration is the contribution assessed here. No general novelty guarantee is inferred from unsuccessful searches.

## Limitations

The error term is a uniform power-saving estimate, not claimed sharp. The limiting density describes roots of square gaps normalized by the smaller generator, not the density of squares among all ordinary gaps. The result is specific to two consecutive generators; it is not a theorem for arbitrary two-generator semigroups, arbitrary polynomial powers, or short intervals that shrink with \(m\). While the mathematical derivation is self-contained apart from the standard discrepancy inequality, an independently conducted scientific audit has not been performed, and equivalent prior work under other terminology remains a risk.

## References

1. S. Chappelon and J. L. Ramírez Alfonsín, *The Square Frobenius Number*, arXiv:2006.14219 (first version 25 June 2020). https://arxiv.org/abs/2006.14219
2. D. S. Binner, *Proofs of Chappelon and Alfonsín Conjectures On Square Frobenius Numbers and its Relationship to Simultaneous Pell's Equations*, arXiv:2112.15474 (first version 31 December 2021). https://arxiv.org/abs/2112.15474
3. M. Drmota and R. F. Tichy, *Sequences, Discrepancies and Applications*, Lecture Notes in Mathematics 1651, Springer, 1997 (standard Erdős–Turán–Koksma discrepancy inequality).
