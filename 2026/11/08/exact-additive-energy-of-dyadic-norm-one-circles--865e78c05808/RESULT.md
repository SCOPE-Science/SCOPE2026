# Exact additive energy of dyadic norm-one circles

## Finding
For every integer \(k\ge4\), let \(N=2^k\), let \(R=\mathbb Z/N\mathbb Z\), and define the norm-one circle
\[
C_k=\{(x,y)\in R^2:x^2+y^2\equiv1\pmod N\}.
\]
Write \(E(C_k)\) for the number of ordered quadruples of circle points satisfying \(u_1+u_2=u_3+u_4\). Then
\[
\boxed{|C_k|=2^{k+1},\qquad E(C_k)=3(k-2)2^{2k+3}.}
\]
In particular, \(E(C_k)/|C_k|^2=6(k-2)\). If
\[
S_k(a,b)=\sum_{(x,y)\in C_k}\exp\!\left(\frac{2\pi i(ax+by)}N\right),
\]
then the exact (unweighted) Fourier fourth moment is
\[
\boxed{\frac1{N^2}\sum_{a,b\in R}|S_k(a,b)|^4=3(k-2)2^{2k+3}.}
\]

## Assumptions and scope
All congruences below are in the stated quotient rings. The circle is the set of *points*, not a multiset obtained by choosing square roots. Ordered quadruples count repeated points and their order. The character sum is unnormalized; the ambient frequency average is divided by \(N^2\). We assume \(k\ge4\); no small-modulus formula is being extrapolated. Represent a pair \((x,y)\) as \(x+iy\) in \(R[i]\), with \(i^2=-1\), multiplication \((x+iy)(u+iv)=(xu-yv)+i(xv+yu)\), conjugation \(\overline{x+iy}=x-iy\), and norm \(z\bar z=x^2+y^2\). The norm-one elements form a group under multiplication.

## Proof
**1. Circle cardinality and a convenient quotient.** For \(k\ge4\), a circle point has exactly one odd coordinate. The even coordinate must be divisible by four, since every odd square is one modulo eight. There are \(N/4\) choices for an even coordinate divisible by four. For each, the other coordinate solves \(x^2=1-y^2\), whose right side is one modulo eight, and therefore has exactly four roots modulo \(2^k\). Thus there are \(N\) points of each of the two orientations, and \(|C_k|=2N\).

Put \(M=2^{k-1}\), \(n=k-3\), \(P=2^n\), and work temporarily in \((\mathbb Z/M\mathbb Z)[i]\). Define
\[
h(z)=\frac{1+2iz}{1-2iz}
=\frac{1-4z^2+4iz}{1+4z^2},\qquad z\in\mathbb Z/P\mathbb Z.
\]
Every denominator is odd, hence invertible. The images \(i^j h(z)\) for \(j\in\{0,1,2,3\}\), \(z\in\mathbb Z/P\mathbb Z\), are distinct: \(j\) is determined by the pair modulo four, and equality for fixed \(j\) implies
\[
(z-w)(1-4zw)\equiv0\pmod P,
\]
so \(z=w\), as the second factor is odd. All these \(4P=2^{k-1}\) images are reductions of norm-one points modulo \(N\), by using the same fractions modulo \(N\). Conversely, any reduction of a norm-one point has at least four lifts in \(C_k\), obtained by adding \(M\) independently to either coordinate, without changing the norm modulo \(N\). Since \(|C_k|=2^{k+1}\), the reduction image consists exactly of these \(4P\) points, and every image has exactly four preimages.

**2. Convert energy into a Gaussian bilinear congruence.** Since \(-C_k=C_k\), ordered sum energy equals ordered difference energy. An equality \(u-v=u'-v'\) between circle-point differences may be written as
\[
v(t-1)=v'(s-1),\quad t=uv^{-1},\quad s=u'(v')^{-1},
\]
where \(s,t,v,v'\) belong to \(C_k\). Put \(w=v'v^{-1}\). Then \(t=1+w(s-1)\), and for each pair \((s,w)\) satisfying \(t\bar t=1\) there are exactly \(|C_k|\) choices of \(v\). Expanding the norm and using \(s\bar s=w\bar w=1\) gives
\[
t\bar t-1=\operatorname{Tr}((w-1)(s-1)),\qquad \operatorname{Tr}(a+ib)=2a.
\]
Consequently,
\[
E(C_k)=|C_k|\,T_k,\quad T_k=\#\{(s,w)\in C_k^2:\operatorname{Re}((s-1)(w-1))\equiv0\pmod M\}.
\]
The condition depends only on the reductions modulo \(M\), each having four lifts, so \(T_k=16T'_k\), where \(T'_k\) counts ordered pairs among the \(4P\) displayed values \(i^j h(z)\).

**3. Exact valuation count.** Write \(a,b\in\mathbb Z/P\mathbb Z\) for the parameters of the two reduced points. Set
\[
\begin{array}{c|c}
j&N_j(a)\text{ in }i^j h(a)-1=N_j(a)/(1-2ia)\\\hline
0&4ia\\1&(i-1)(1+2a)\\2&-2\\3&-(1+i)(1-2a)
\end{array}
\]
Clearing the Gaussian denominator and its conjugate multiplies the real-part congruence only by the odd unit \((1+4a^2)(1+4b^2)\). The resulting integer expressions for unordered orientation pairs are
\[
\begin{array}{c|l}
(j,\ell)&(1+4a^2)(1+4b^2)\operatorname{Re}((i^j h(a)-1)(i^\ell h(b)-1))\\\hline
(0,0)&16ab(4ab-1)\\
(0,1)&4a(2b+1)(4ab+2a+2b-1)\\
(0,2)&16a(a+b)\\
(0,3)&4a(2b-1)(4ab-2a-2b-1)\\
(1,1)&4(a+b)(2a+1)(2b+1)\\
(1,2)&-2(2a+1)(4ab-2a-2b-1)\\
(1,3)&2(2a+1)(2b-1)(4ab-1)\\
(2,2)&-4(4ab-1)\\
(2,3)&2(2b-1)(4ab+2a+2b-1)\\
(3,3)&-4(a+b)(2a-1)(2b-1)
\end{array}
\]
Every factor not explicitly a power of two, \(a\), \(b\), or \(a+b\) is odd. Because \(M=2^{n+2}\) with \(n\ge1\), the \((1,2),(1,3),(2,2),(2,3)\) types never vanish modulo \(M\). For the other types, \((0,1)\) and \((0,3)\) require \(a=0\pmod P\); \((1,1)\) and \((3,3)\) require \(a+b=0\pmod P\); and \((0,0)\), \((0,2)\) require, respectively,
\[
2^{n-2}\mid ab,\qquad 2^{n-2}\mid a(a+b).
\]
For \(n=1\), these last two conditions are understood as automatic. Let \(Z_n\) be the number of ordered pairs \((a,b)\in(\mathbb Z/2^n\mathbb Z)^2\) satisfying \(2^{n-2}\mid ab\). Direct valuation summation yields
\[
Z_n=n2^{n+1}\quad(n\ge1).
\]
Indeed, for \(n\ge2\), put \(t=n-2\). The fraction of pairs with product divisible by \(2^t\) is \((t+2)/2^{t+1}\); for \(n=1\) all four pairs qualify, again giving the formula. The substitution \(b\mapsto a+b\) is a bijection, so the \((0,2)\) count also equals \(Z_n\).

Counting *ordered* orientation pairs gives three occurrences of \(Z_n\): \((0,0),(0,2),(2,0)\). The four cross-orientation types \((0,1),(1,0),(0,3),(3,0)\) contribute \(4P\) in total, while the two equal-orientation types \((1,1),(3,3)\) contribute \(2P\). Hence
\[
T'_k=3Z_n+6P=6(n+1)2^n=6(k-2)2^{k-3}.
\]
It follows that
\[
E(C_k)=2^{k+1}\cdot16\cdot6(k-2)2^{k-3}=3(k-2)2^{2k+3}.
\]
This proves the all-dimensional count, without extrapolation from finite computation. Finally, Fourier orthogonality on the group \(R^2\) gives \(N^{-2}\sum_{a,b}|S_k(a,b)|^4=\sum_z(\mathbf1_{C_k}*\mathbf1_{C_k}(z))^2=E(C_k)\), completing the proof.

## Verification
Run `python3 verify_dyadic_circle_energy.py`. It performs independent direct circle enumeration and exact convolution-energy counting for \(4\le k\le9\); separately checks the rational-parameter angular incidences and the sixteen-lift identity, reporting `DYADIC_CIRCLE_ENERGY_CHECK_PASS`. These computations check finite instances, while the valuation and counting arguments above prove the formula for every \(k\ge4\).

## Relationship to prior work
Nica's work on unimodular graphs and Eisenstein sums (first publicly available 2015) develops character-sum and valuation-ring spectral methods, explicitly in odd residue characteristic; its unimodular incidence graphs and unramified-extension Eisenstein sums do not give the present 2-adic Gaussian-circle energy. Hickman and Wright (first preprint 2018) study Fourier restriction over residue rings and the effect of divisor scales, with primary model surfaces including paraboloids; their stated global restriction criteria do not provide this precise constant-input, norm-one-circle fourth moment. Earlier finite-field conic results and odd-prime-power anisotropic-circle calculations do not imply the characteristic-two identity. The identity \(E(C_k)/|C_k|^2=6(k-2)\) exhibits a genuine depth-dependent enhancement.

## Limitations
Only the dyadic ring and the unweighted fourth Fourier moment are classified. The theorem does not assert the optimal extension norm for arbitrary complex weights, a full distribution of two-point sums, results for non-dyadic moduli, or historical uniqueness beyond the inspected comparisons. More general prior local-density identities could imply the same count; this remains a priority risk. No independent mathematical audit has been performed.

## References
1. B. Nica, *Unimodular graphs and Eisenstein sums*, arXiv:1505.05034, first public 2015-05-19, https://arxiv.org/abs/1505.05034.
2. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176, first public 2018-01-09, https://arxiv.org/abs/1801.03176.
