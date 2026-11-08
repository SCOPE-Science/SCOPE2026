# The first reentrant boundary order for Jacobi-weighted disk kernels

## Finding

For each integer \(m\ge0\) and real \(t>0\), consider the normalized-area weighted Bergman space on the open unit disk with weight
\[
\omega_{m,t}(z)=|z|^{2(t-1)}(1-|z|^2)^m.
\]
Write \(s=z\overline w\). Let \(N_m(t)\) denote the number, with multiplicity, of zeros of the scalar reproducing kernel \(K_{m,t}(s)\) in \(|s|<1\). Equivalently, \(N_m(t)=0\) precisely when the reproducing kernel is zero-free on the bidisk. For each \(m=0,1,2,3\), there is a **single exact zero-loss threshold**, with no later reentry:
\[
N_m(t)=\begin{cases}1,&0<t<\tau_m,\\0,&t\ge\tau_m,\end{cases}
\qquad
\begin{aligned}
\tau_0&=\tfrac12,\\
\tau_1&=\tfrac1{\sqrt2},\\
\tau_2&=\tfrac{\sqrt7-1}{2},\\
\tau_3&=\sqrt{2+\tfrac{\sqrt{10}}2}-1.
\end{aligned}
\]
The unique zero below each threshold is simple, real and negative. At the threshold it reaches the excluded boundary point \(s=-1\).

**Boundary order four is the first integer order at which the number of scalar-disk kernel zeros can increase again as \(t\) grows.** Indeed, for \(m=4\) the exact zero counts at \(t=\frac12,1,4\) are respectively \(1,0,2\). The novelty in the first-order assertion is the missing third-order boundary classification and the resulting minimal-order conclusion; the lower-order classifications and fourth-order reentry have related prior results (see References).

## Assumptions and scope

Here \(dA/\pi\) is normalized planar area measure, \(t>0\) is an arbitrary real number (not just an integer), and \(m\) is an integer. The full classification applies to \(m\in\{0,1,2,3\}\). For \(m=4\), only the three stated exact parameter witnesses are needed and proved. No statement is made for \(m\ge5\). "Scalar-disk zero" means a root in \(|s|<1\), not a zero of a fixed section at an arbitrary basepoint. Each such scalar root can be realized as \(s=z\overline w\) with \(|z|,|w|<1\).

The weight is integrable and strictly positive away from the origin and unit boundary. All analytic point evaluations are continuous, and monomials are an orthogonal complete basis.

## Proof

**1. Monomial norms and polynomial reduction.** For every integer \(k\ge0\), polar integration gives
\[
\|z^k\|^2
=\int_0^1 u^{k+t-1}(1-u)^m\,du
=\mathrm B(k+t,m+1)
=\frac{m!}{(k+t)_{m+1}},
\]
where \((x)_j=x(x+1)\cdots(x+j-1)\). Therefore, for \(|s|<1\),
\[
K_{m,t}(s)=\frac1{m!}\sum_{k=0}^{\infty}(k+t)_{m+1}s^k.
\]
Define \(P_{m,t}(s)=\frac{m!}{t}(1-s)^{m+2}K_{m,t}(s)\). Its numerator is a polynomial of degree at most \(m+1\); because \(t>0\), its roots in \(|s|<1\) are exactly the kernel roots there. Define the Cayley transform
\[
u=\frac{1+s}{1-s},\qquad s=\frac{u-1}{u+1},\qquad Q_{m,t}(u)=(1+u)^{m+1}P_{m,t}\left(\frac{u-1}{u+1}\right).
\]
The map sends the open scalar disk bijectively onto \(\operatorname{Re}u>0\). Poles and possible degree-loss factors at \(u=-1\) lie outside the open right half-plane. Elementary Eulerian-series summation yields, up to positive factors \(t^{-1},2t^{-1},2t^{-1},8t^{-1}\) respectively, the following real polynomials:
\[
\begin{aligned}
R_0(u)&=u+2t-1,\\
R_1(u)&=u^2+2tu+2t^2-1,\\
R_2(u)&=3u^3+(6t+3)u^2+(6t^2+6t-3)u
 +(2t+1)(2t^2+2t-3),\\
R_3(u)&=3u^4+6(t+1)u^3+6t(t+2)u^2\\
&\quad +(4t^3+12t^2+2t-6)u
 +2t^4+8t^3+4t^2-8t-3.
\end{aligned}
\]
These identities follow either by applying \(s\,d/ds\) repeatedly to \((1-s)^{-1}\) or by direct expansion, and are independently checked in the accompanying script.

**2. Complete right-half-plane root count for orders zero through three.** The first columns of the exact Routh arrays of \(R_0,R_1,R_2,R_3\) are, in descending row order:
\[
\begin{array}{c|l}
0&1,\quad 2t-1\\
1&1,\quad 2t,\quad 2t^2-1\\
2&3,\quad6t+3,\quad4t(t+1),\quad (2t+1)(2t^2+2t-3)\\
3&3,\quad6(t+1),\quad(2t+1)(2t+3),\\
 &\displaystyle\quad\frac{4t(t+1)(t+2)(t^2+2t+3)}{(2t+1)(2t+3)},
 \quad 2t^4+8t^3+4t^2-8t-3.
\end{array}
\]
Every entry except the last one is **strictly positive** for \(t>0\). Away from zero final entries, the Routh theorem therefore counts exactly one root in \(\operatorname{Re}u>0\) when the final entry is negative and none when it is positive. The four final entries have unique positive roots
\[
\tau_0=\tfrac12,\quad \tau_1=1/\sqrt2,\quad
\tau_2=(\sqrt7-1)/2,\quad
\tau_3=\sqrt{2+\sqrt{10}/2}-1,
\]
with negative signs below and positive signs above. To see uniqueness at order three, put \(y=(t+1)^2>1\): the last entry becomes \(2y^2-8y+3\), whose only root with \(y>1\) is \(y=2+\sqrt{10}/2\). The lower orders factor as displayed.

At each threshold the polynomial has \(u=0\) as a simple root and its remaining roots lie strictly in the left half-plane. Indeed, the other first-column quantities stay positive, while the coefficient of \(u\) at threshold is positive (by the same Routh elimination). Thus the only boundary contact is \(u=0\), corresponding to \(s=-1\). Below threshold the unique right-half-plane root must be real and simple, since nonreal roots occur in conjugate pairs. It maps to a real scalar root \(-1<s<1\). Since \(K_{m,t}(s)>0\) for \(0\le s<1\) by its strictly positive series coefficients, this root lies in \((-1,0)\).

**3. An exact fourth-order reentry witness.** For \(m=4\), direct polynomial summation and Cayley transformation give
\[
\begin{aligned}
Q_{4,1/2}(u)&=30(8u^5+32u^4+44u^3+16u^2-17u-20),\\
Q_{4,1}(u)&=120(u+1)^5,\\
Q_{4,4}(u)&=30(u^5+11u^4+58u^3+198u^2+501u+1023).
\end{aligned}
\]
After discarding the positive scalar factors, the exact Routh first columns for the first and third polynomials are respectively
\[
(8,32,40,128/5,77/4,-20)
\quad\text{and}\quad
(1,11,40,429/5,-896/13,1023).
\]
Their sign-variation counts are one and two. At \(t=1\) the polynomial has no right-half-plane roots, as all five roots are \(u=-1\). Hence \(N_4(1/2)=1\), \(N_4(1)=0\), and \(N_4(4)=2\). Together with Step 2, this proves that four is the smallest integer boundary order admitting reentry.

## Verification

Run `python verify_jacobi_transition.py` with Python 3, SymPy and NumPy. The script derives the generating polynomials from the factorial moments, symbolically verifies all four Cayley forms and their Routh first columns, checks the fourth-order witness polynomials and exact sign arrays, and performs 316 additional numerical root-count probes at rational parameter values. The expected successful output is:

`JACOBI_FIRST_REENTRANCE_PASS exact_cayley=4 exact_routh=4 exact_witnesses=3 sampled_cases=316`

The finite probes are illustrative, **not** a proof for arbitrary \(t>0\); the symbolic identities and the analytical Routh argument supply the general result.

## Relationship to prior work

Perälä (2017) proved general existence and finiteness results for zeros of radial weighted Bergman kernels. Miña-Díaz (2022/2023) derived kernel formulas for weights given by products of Blaschke-factor moduli; those weights do not include the independent positive boundary factor in this theorem. Karp and Vishnyakova (2025) develop a broad generalized \(f\)-Eulerian polynomial framework that includes rising-factorial generating polynomials, but the inspected zero-location criteria do not give the present sharp open-unit-disk counts. Earlier calculations of the first, second and fourth Jacobi boundary orders already establish portions of the displayed pattern; they do not supply the missing third-order cut-off or its minimal-reentry-order conclusion. The result does **not** claim that the algebraic moment formulas themselves are new.

## Limitations

The term "first" is relative to nonnegative **integer** boundary vanishing orders \(m\), not to arbitrary real boundary exponents or to all radial weights. The fourth-order contribution is an existence witness, not a new full fourth-order parameter classification. No assertion is made for \(m\ge5\), asymptotic root motions, or a root count for an arbitrary fixed kernel section. Independent external validation has not been performed. Broader classical Schur-stability and generalized-Eulerian results remain a possible priority risk, even though no directly implying theorem was identified in the inspected literature.

## References

1. A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976, first publicly posted 2017-03-17, especially Theorems 3.1, 3.3, and 3.5. https://arxiv.org/abs/1703.05976
2. E. Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space*, arXiv:2212.08118, first publicly posted 2022-12-15, Theorem 1.1. https://arxiv.org/abs/2212.08118
3. D. Karp and A. Vishnyakova, *Generalized f-Eulerian polynomials: zeros and hypergeometric representations with applications*, arXiv:2509.13897, first publicly posted 2025-09-17, introductory definitions and §§2–3. https://arxiv.org/abs/2509.13897
