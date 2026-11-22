# The exact first band of bounded integral matrix centralizers

## Finding

Fix an integer \(H\ge1\). Let \(\mathcal B_H\) be the set of integer \(2\times2\) matrices with all four entries in \([-H,H]\), and for \(A\in\mathcal B_H\), set
\[
C_H(A)=\#\{B\in\mathcal B_H:AB=BA\}.
\]
For any real \(2\le z\le4\), put
\[
L_H(z)=\left\lceil\frac{(6-z)H+3}{2}\right\rceil,
\qquad
Q_H(p)=\sum_{r\mid p}\mu(r)\bigl(2\lfloor H/r\rfloor+1\bigr)^2.
\]
The exact finite lower-band count is
\[
\boxed{\#\{A\in\mathcal B_H:C_H(A)\le zH\}
=2\sum_{p=L_H(z)}^{2H}(2H+1-p)Q_H(p),}
\]
where the sum is zero if its lower limit exceeds its upper limit. Uniformly for all real \(z\in[2,4]\),
\[
\boxed{\frac{\#\{A\in\mathcal B_H:C_H(A)\le zH\}}{(2H+1)^4}
=\frac{(z-2)^2}{16\zeta(3)}+O(H^{-1}).}
\]
The least value of \(C_H(A)\) among nonscalar matrices in \(\mathcal B_H\) equals \(2H+3\). The first stratum \(C_H(A)\le4H\) therefore has limiting density \(1/(4\zeta(3))\), and the lower-edge cumulative law is quadratic. These statements refer to uniform sampling of \(A\) from the complete four-dimensional integer box, not uniform sampling from the nonscalar locus (the scalar locus is negligible).

## Assumptions and scope

All matrices are integer \(2\times2\) matrices, all bounds on entries are inclusive, \(H\) is a positive integer, and \(z\) is real in the closed interval \([2,4]\). The Möbius function is \(\mu\) and \(\zeta\) is the Riemann zeta function. The assertion is a uniform first-band result only; it makes no claim about the distribution when \(z>4\). Constants implicit in the error term are absolute. A scalar matrix commutes with all \((2H+1)^4\) matrices in the box and hence never contributes to these lower-tail events.

## Proof

Write \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), and assume \(A\) is nonscalar. Define
\[
g=\gcd(|b|,|c|,|a-d|),\quad p=|a-d|,\quad M=\max(2|b|,2|c|,p),\quad S=\lfloor2gH/M\rfloor.
\]
Here \(g,M\) are positive integers. The rational commutant of a nonscalar \(2\times2\) matrix is spanned by \(I\) and \(A\). The integer commutants are uniquely parametrized, for integer \(j,y\), as
\[
B=\begin{pmatrix}
y&(b/g)j\\ (c/g)j&y-((a-d)/g)j
\end{pmatrix}.
\]
Indeed, the three integer coefficients \((b/g,c/g,(a-d)/g)\) have gcd one, so Bézout's identity forces their common rational multiplier to be an integer. Bounding both off-diagonal entries and the difference of the diagonal entries gives \(|j|\le S\). For each such \(j\), the two diagonal entries fit the box in exactly \(2H+1-(p/g)|j|\) ways. In particular,
\[
C_H(A)=(2H+1)(2S+1)-(p/g)S(S+1). \tag{1}
\]
This reconstructs the pointwise count appearing in Afifurrahman–Wicaksono [1].

Since \(M\le2H\), we have \(S\ge g\ge1\). Since \(S\le2gH/M\), one has \(p/g\le M/g\le2H/S\). Substituting this inequality into (1) gives
\[
C_H(A)\ge (2H+1)(2S+1)-2H(S+1)=2HS+2S+1. \tag{2}
\]
Consequently \(S\ge2\) implies \(C_H(A)\ge4H+5\). In the event \(C_H(A)\le zH\le4H\), therefore, \(S=1\), and \(g=1\) follows from \(S\ge g\). Equation (1) now becomes
\[
C_H(A)=6H+3-2p,
\]
so the event requires \(p\ge L_H(z)\). Conversely, \(p\ge L_H(z)\ge H+2\) and \(g=1\) imply \(H<M\le2H\), hence \(S=1\), and equation (1) shows \(C_H(A)\le zH\). Thus the exact predicate is
\[
\boxed{C_H(A)\le zH\quad\Longleftrightarrow\quad |a-d|\ge L_H(z),\quad\gcd(b,c,a-d)=1.} \tag{3}
\]
For each positive diagonal difference \(p\), the number of ordered pairs \((a,d)\) with \(|a-d|=p\) is \(2(2H+1-p)\). Möbius inversion counts the corresponding \((b,c)\):
\[
\#\{(b,c)\in[-H,H]^2\cap\mathbb Z^2:\gcd(b,c,p)=1\}=Q_H(p).
\]
Summing (3) over \(p\) gives the exact finite formula.

To obtain a uniform asymptotic, denote by \(T=2\sum_{p=L_H(z)}^{2H}(2H+1-p)\) the number of ordered diagonal pairs with the required large difference. A short arithmetic progression sum gives, uniformly in \(z\),
\[
T=(2H-L_H(z)+1)(2H-L_H(z)+2)=\frac{(z-2)^2}{4}H^2+O(H).
\]
For any positive integer \(r\le2H\), the number of permissible \(b\in[-H,H]\cap\mathbb Z\) divisible by \(r\) is \(B_r=2\lfloor H/r\rfloor+1=(2H+1)/r+O(1)\). The number \(T_r\) of ordered pairs \((a,d)\) with \(|a-d|\ge L_H(z)\) and \(r\mid(a-d)\) satisfies
\[
T_r=2\sum_{\substack{L_H(z)\le p\le2H\\r\mid p}}(2H+1-p)=T/r+O(H),
\]
uniformly in \(r,z\), by an endpoint estimate for arithmetic progression sums. Möbius inversion and \(r\le2H\) yield
\[
\begin{aligned}
\#\{A:C_H(A)\le zH\}
 &=\sum_{r\le2H}\mu(r)B_r^2T_r\\
 &= (2H+1)^2T\sum_{r\le2H}\frac{\mu(r)}{r^3}+O(H^3)\\
 &=\frac{(2H+1)^2T}{\zeta(3)}+O(H^3).
\end{aligned}
\]
For clarity, the accumulated error is bounded by the sum over \(r\le2H\) of \(O(H^3/r^2+H^2/r+H)\), hence is \(O(H^3)\); extending the absolutely convergent Dirichlet series incurs \(O(H^2)\). Dividing by \((2H+1)^4\) proves the stated uniform law.

Equation (2) gives the lower bound \(2H+3\) for nonscalar matrices. It is attained by \(A=\begin{pmatrix}H&1\\0&-H\end{pmatrix}\), since \(g=S=1\) and \(p=2H\); thus the minimum assertion also holds.

## Verification

The independent finite checker `edge_checker.py` uses two distinct descriptions of commutation: an exhaustive scan of integer matrices \(B\) versus the closed formula (1). It checks all \(3^4+5^4+7^4=3107\) choices of \(A\) for \(H=1,2,3\). It then checks each of 35 threshold cases \(H=1,\dots,7\), \(z\in\{2,5/2,3,7/2,4\}\), comparing direct event enumeration with both the finite sum and an independent Möbius-sieve implementation. The checker also prints three larger finite samples. All tests pass with exit line `CENTRALIZER_EDGE_OK 3107 35`. No finite test is offered as a proof of the uniform infinite asymptotic; that follows from the estimates in the proof.

## Relationship to prior work

Afifurrahman and Wicaksono [1, Theorem 1.1] compute the bounded commutant of each fixed nonscalar \(2\times2\) integer matrix; that pointwise formula is the starting input. Their subsequent statistics concern other centralizer invariants, not the cumulative distribution of this cardinality across a growing entry box. Chapman and Mudgal [2] compute an asymptotic for the total number of commuting integer matrix pairs, which gives a first moment but cannot determine this lower-tail distribution. Mudgal [3] proves bounds for arbitrary matrix-set commuting-pair probabilities, without an exact first-band law or the present \(\zeta(3)\) coefficient. The new statement characterizes the entire first nontrivial cardinality band and computes its limiting mass. Literature comparison does not exclude unknown equivalent results outside the inspected sources.

## Limitations

This theorem does not classify later lower-tail bands, determine the full limiting law, or establish an optimal error term. The calculation relies on the symmetric entry box and does not automatically extend to unequal side lengths, other matrix sizes, or other sampling measures. Although explicit and proved here, originality is assessed relative to identified literature, not asserted as an exhaustive priority certification. Independent audit has not been performed.

## References

1. Muhammad Afifurrahman and Wildan Bagus Wicaksono, *Statistics of centralizers of integer matrices*, arXiv:2611.11287v1 (first public November 8, 2026), https://arxiv.org/abs/2611.11287.
2. Jonathan Chapman and Akshat Mudgal, *On commuting integer matrices*, arXiv:2504.15839v1 (April 22, 2025), https://arxiv.org/abs/2504.15839.
3. Akshat Mudgal, *On commuting pairs in arbitrary sets of \(2\times2\) matrices*, *Mathematische Zeitschrift* 313, article 84 (2026), https://doi.org/10.1007/s00209-026-04097-2.
