# A dimension-controlled transverse phase boundary for pinched sine-forced skew products

## Finding
For each integer \(d\geq1\), let \(\omega\in\mathbb T^d\) be totally irrational and define the skew product
\[
F_{\kappa,d}(\theta,x)=\left(\theta+\omega,\;g_d(\theta)\tanh(\kappa x)\right),\qquad
 g_d(\theta)=\frac1d\sum_{j=1}^{d}\sin(\pi\theta_j),
\]
on \(\mathbb T^d\times[0,1]\), with \(\kappa>0\), where each torus coordinate is represented in \([0,1]\) and endpoints are identified. The zero graph is invariant. Define its transverse Lyapunov threshold
\[
K_d:=\exp\left(-\int_{[0,1]^d}\log g_d(\theta)\,d\theta\right).
\]
Then \(\lambda_d(\kappa)=\log(\kappa/K_d)\) is the transverse Lyapunov exponent of that graph for Haar-almost every base point. The following **dimension phase diagram** holds:

1. \(K_1=2\), \(K_2=4\exp(-7\zeta(3)/\pi^2)\), and \(2=K_1>K_2>K_3>\cdots>\pi/2\), with \(K_d\downarrow\pi/2\).
2. Put \(c_1=\pi^2/16-1/2\) and \(c_2=3\pi^4/256-17\pi^2/144+1/12\). As \(d\to\infty\),
\[
\log K_d=\log(\pi/2)+\frac{c_1}{d}+\frac{c_2}{d^2}+O(d^{-3}).
\]
Both coefficients are strictly positive.
3. For every fixed \(\pi/2<\kappa<2\), there is a unique least dimension \(d_*(\kappa)\) with \(\lambda_d(\kappa)>0\) for all \(d\ge d_*(\kappa)\), while \(\lambda_d(\kappa)\le0\) for all \(d<d_*(\kappa)\). With \(\delta=\log(2\kappa/\pi)\),
\[
d_*(\kappa)=\frac{c_1}{\delta}+O(1)\qquad (\kappa\downarrow\pi/2).
\]
At equality \(\kappa=K_d\) the corresponding exponent is zero, not positive. For \(\kappa\le\pi/2\) it is negative in every finite dimension; for \(\kappa\ge2\) it is nonnegative in every dimension and strictly positive except \((d,\kappa)=(1,2)\).

For \(\kappa<K_d\), almost every base phase and every \(x_0>0\) satisfy \(x_n\to0\) exponentially, with \(\limsup_{n\to\infty}n^{-1}\log x_n\le\log(\kappa/K_d)<0\). The theorem asserts the sign of the transverse exponent, not the precise nonlinear behavior at a neutral threshold.

## Assumptions and scope
The dimension \(d\) is a positive integer, \(\kappa>0\), and \(\omega\) is a totally irrational torus translation. The functions \(g_d\) are nonnegative and vanish only where all coordinate sines vanish; their logarithms are Lebesgue-integrable. The formulae for \(K_d\) are independent of the particular totally irrational \(\omega\). All limits in dimension concern the sequence of these explicitly defined forcing functions, not a fixed dynamical system as its state-space dimension changes. We make no finite-time Lyapunov probability, physical-measure uniqueness, or neutral-fiber nonlinear stability assertion.

## Proof
**The exponent.** Along \(x=0\) the fiber derivative is \(\kappa g_d(\theta)\). Since \(\log g_d\) is integrable and a totally irrational rotation is Haar-ergodic, Birkhoff's theorem gives \(\lambda_d(\kappa)=\log\kappa+\int\log g_d=\log(\kappa/K_d)\) for Haar-a.e. base phase. For \(x_0>0\), \(\tanh(\kappa x)\le\kappa x\) yields \(x_n\le x_0\kappa^n\prod_{j=0}^{n-1}g_d(\theta+j\omega)\), proving the subcritical nonlinear bound.

**Strict ordering.** Let \(Z_i=\sin(\pi U_i)\), with independent uniform \(U_i\) on \([0,1]\), and \(M_d=d^{-1}\sum_{i=1}^d Z_i\). Write \(Y_j=d^{-1}\sum_{i\ne j}^{d+1}Z_i\) for the \(d+1\) leave-one-out means. Their arithmetic mean is \(M_{d+1}\). The strict concavity of logarithm gives \(\log M_{d+1}\ge(d+1)^{-1}\sum_j\log Y_j\), strictly except on the zero-probability event when all \(Z_i\) are equal. Taking expectations, \(\mathbb E\log M_{d+1}>\mathbb E\log M_d\). Consequently \(K_{d+1}<K_d\). Since \(\mathbb E Z_i=2/\pi\), strict Jensen gives \(K_d>\pi/2\) at every finite \(d\).

**The two-dimensional exact value.** Put \(u=\pi U_1,v=\pi U_2\). The elementary identity \((\sin u+\sin v)/2=\sin((u+v)/2)\cos((u-v)/2)\) leads to the absolutely integrable logarithmic average
\[
\mathbb E\log M_2=\frac1{\pi^2}\int_0^\pi\!\int_0^\pi
\left[\log\sin\frac{u+v}{2}+\log\cos\frac{u-v}{2}\right]du\,dv.
\]
The Abel-regularized Fourier expansions of the two logarithms are \(-\log2-\sum_{n\ge1}\cos(n(u+v))/n\) and \(-\log2-\sum_{n\ge1}(-1)^n\cos(n(u-v))/n\). For odd \(n\), their averaged cosines are respectively \(-4/(\pi^2n^2)\) and \(4/(\pi^2n^2)\), and both averages vanish for even \(n\). Integrating the Abel expansions and taking the limit gives
\[
\mathbb E\log M_2=-2\log2+\frac8{\pi^2}\sum_{\substack{n\ge1\\ n\,\mathrm{odd}}}\frac1{n^3}=-2\log2+\frac{7\zeta(3)}{\pi^2}.
\]
This proves the stated exact \(K_2\). Similarly \(\mathbb E\log Z_1=-\log2\) gives \(K_1=2\).

**The large-dimension coefficients and limit.** Set \(m=\mathbb EZ_i=2/\pi\), \(v=\operatorname{Var}Z_i=1/2-4/\pi^2\), and \(\tau=\mathbb E(Z_i-m)^3=16/\pi^3-5/(3\pi)\). For \(\Delta_d=M_d-m\), independence gives
\[
\mathbb E\Delta_d^2=v/d,\quad\mathbb E\Delta_d^3=\tau/d^2,\quad
\mathbb E\Delta_d^4=3v^2/d^2+O(d^{-3}),
\]
and \(\mathbb E\Delta_d^5=O(d^{-3})\), \(\mathbb E\Delta_d^6=O(d^{-3})\), \(\mathbb E|\Delta_d|^7=O(d^{-7/2})\). On \(|\Delta_d|\le m/2\), Taylor-expand \(\log(m+\Delta_d)\) through order six; the expected remainder is \(O(d^{-7/2})\). Hoeffding's inequality makes the complement exponentially rare. The logarithm on that complement is uniformly integrable by the AM–GM inequality \(\log M_d\ge d^{-1}\sum\log Z_i\), whose right side has uniformly bounded second moment; Cauchy–Schwarz makes the discarded contribution exponentially small. Thus
\[
-\mathbb E\log M_d=-\log m+\frac{v}{2m^2d}+
\frac{1}{d^2}\left(\frac{3v^2}{4m^4}-\frac{\tau}{3m^3}\right)+O(d^{-3}).
\]
Substitution yields \(c_1,c_2\) and \(K_d\downarrow\pi/2\). The strict positivity of \(c_2\) follows, for example, by the exact expression and \(3.14<\pi<22/7\).

**Dimension crossover.** Because \(K_d\) decreases strictly to \(\pi/2\), for \(\pi/2<\kappa<2\) the first strictly positive exponent occurs at a finite unique least dimension. With \(\delta=\log(2\kappa/\pi)\), the expansion \(\log K_d-\log(\pi/2)=c_1/d+O(d^{-2})\) implies \(d_*(\kappa)=c_1/\delta+O(1)\). Endpoints follow from the strict inequalities proved above.

## Verification
The standalone script `check_threshold.py` reproduces the exact first three sine moments, the two asymptotic coefficients, the truncated odd-frequency evaluation for \(K_2\), and deterministic direct quadrature for the same logarithmic integral. It also checks the ordering of finite-dimensional quadrature approximations and the limiting expansion as numerical consistency tests. The analytically justified expectation identities, Fourier integration, strict Jensen inequality, and controlled Taylor remainder—not these finite computations—prove the universal statements.

## Relationship to prior work
Gröger and Jäger (2011 preprint, 2013 final version), Example 4.1, introduce the same higher-dimensional sine-forced pinched skew product and study attractor geometry at sufficiently large forcing. Remo, Fuhrmann, and Jäger (2022 preprint, 2023 online publication), equations (1)–(2) and Remark 2.1, give the general integral formula for the neutral zero-line exponent and study positive finite-time exponents. That general integral is acknowledged here as prior work. The claimed addition is the strict dimension-ordering, explicit dimension-two Apéry constant, second-order high-dimensional expansion and consequent exact dimension-induced sign phase diagram. These quantitative conclusions were not found in those papers or the inspected related literature. The elementary Fourier-logarithm and sample-mean tools are standard; no priority is claimed for them in isolation.

## Limitations
This is a result specifically for equal-weight sine forcing on the base torus, not arbitrary forcing functions. The positivity transition refers to transverse Lyapunov stability of the **zero graph**, not a guarantee that every initial condition converges to a distinct physical attractor. The neutral equality case is not classified nonlinearly. The high-dimensional expansion is asymptotic and does not give uniform finite-dimensional error constants. Literature search cannot exclude an unpublished or unindexed equivalent calculation; independent validation has not been performed.

## References
- M. Gröger and T. Jäger, *Dimensions of attractors in pinched skew products*, arXiv:1111.6574 (first posted 2011-11-28), especially Example 4.1 and Lemma 4.2. https://arxiv.org/abs/1111.6574
- F. Remo, G. Fuhrmann and T. Jäger, *On the probability of positive finite-time Lyapunov exponents on strange non-chaotic attractors*, arXiv:2210.15292 (first posted 2022-10-27), especially equations (1)–(2), Remark 2.1 and Theorem 1.1. https://arxiv.org/abs/2210.15292
- G. Keller, *A note on strange nonchaotic attractors*, Fundamenta Mathematicae 151 (1996), 139–148. https://doi.org/10.4064/fm-151-2-139-148
