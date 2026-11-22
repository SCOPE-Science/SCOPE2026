# Two-corner extreme-tail law for the recursive product of spacings

## Finding

Let \(n\ge 2\) be fixed and put \(m=n+1\). Under a fully specified continuous null distribution, transform the independent observations by the null cumulative distribution function, order them, and retain the \(m\) endpoint-inclusive uniform spacings \(D=(D_1,\ldots,D_m)\). Let \(R_m\) be the recursive product-of-spacings logarithmic statistic of Eller and Shtembari [1], defined precisely below.

For any integer \(l\ge1\), any \(u=(u_1,\ldots,u_l)\) with positive coordinates summing to one, and \(0\le r<l\), set
\[
L_{r,i}^{(l)}(u)=\sum_{h=0}^{r}\binom{r}{h}u_{i+h},\qquad 1\le i\le l-r,
\]
and
\[
Q_l(u)=\prod_{r=0}^{l-1}\prod_{i=1}^{l-r}L_{r,i}^{(l)}(u).
\]
Define \(q_m=2/m\), let \(U\sim\operatorname{Dirichlet}(1,\ldots,1)\) have \(m-1\) coordinates, and put
\[
A_m=2\,\mathbb E\big[Q_{m-1}(U)^{-q_m}\big].
\]
This is a finite, strictly positive constant. The exact fixed-sample upper-tail equivalent is
\[
\boxed{\displaystyle \Pr(R_m>t)\sim A_m\exp(-2t/m)\qquad(t\to\infty).}
\]
The only leading singular configurations are the two endpoints of the spacing simplex, \(D_1\to1\) or \(D_m\to1\): all sampled points concentrate next to one boundary of the null interval. In particular,
\[
\mathbb E\exp(\theta R_m)<\infty\quad\Longleftrightarrow\quad 0\le\theta<2/m
\]
for \(\theta\ge0\), and the expectation diverges at equality.

The bounded statistic used in [1] is \(R_m^*=B_m/R_m\), with \(B_m=\sum_{j=1}^{m}j\log j\). Consequently its extreme lower tail obeys
\[
\boxed{\displaystyle \Pr(R_m^*\le x)\sim A_m\exp\!\left(-\frac{2B_m}{mx}\right)\qquad(x\downarrow0).}
\]
The inequality may be strict rather than non-strict without affecting the equivalent because the random statistic has no atoms in the relevant interior range.

For the smallest case not solved analytically in [1], \(n=2\) (\(m=3\)), the constant is explicit:
\[
\boxed{\displaystyle A_3=2\,\mathrm B(1/3,1/3)
=\frac{2\Gamma(1/3)^2}{\Gamma(2/3)}
=10.5998325017\ldots.}
\]
The \(n=1\) exact distribution was already given in [1]; inserting \(m=2\) in the present expression recovers its tail constant \(A_2=2\), which is only a consistency check.

## Assumptions and scope

The null distribution is fully specified and continuous, the \(n\) observations are independent and identically distributed, and \(n\ge2\) remains fixed as the tail threshold increases. A probability-integral transform produces \(m=n+1\) spacings with the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. There is no fitted parameter, random sample size, censoring, or simultaneous \(n\)-and-threshold limit.

Starting at \(s^{(0)}=D\), recursively define a vector of length \(m-r\) by
\[
s_i^{(r)}=\frac{s_i^{(r-1)}+s_{i+1}^{(r-1)}}{\sum_{j=1}^{m-r}(s_j^{(r-1)}+s_{j+1}^{(r-1)})}
\quad(1\le r\le m-1).
\]
Then \(R_m=-\sum_{r=0}^{m-1}\sum_{i=1}^{m-r}\log s_i^{(r)}\), exactly the recursive statistic of [1] before its final bounded transformation. All spacing coordinates are strictly positive almost surely.

## Proof

**1. Pascal-smoothing representation.** Let \(L_{r,i}=L_{r,i}^{(m)}(D)\) and \(C_r=\sum_{i=1}^{m-r}L_{r,i}\). By induction using Pascal's identity, \(s_i^{(r)}=L_{r,i}/C_r\) for every \(r\). Therefore
\[
R_m=-\log Q_m(D)+\sum_{r=0}^{m-1}(m-r)\log C_r.
\]
Because \(\sum_jD_j=1\), the coefficient of every \(D_j\) in \(C_r\) is between \(1\) and \(2^r\). Hence \(1\le C_r\le2^r\), so \(e^{R_m}\) is comparable, by positive constants depending only on \(m\), to \(Q_m(D)^{-1}\).

For each interval of indices \(I=[i,i+r]\), the corresponding linear factor is bounded between \(\sum_{j\in I}D_j\) and \(2^r\sum_{j\in I}D_j\). Thus integrability of \(e^{\theta R_m}\) is exactly integrability on the simplex of
\[
\prod_{I\text{ a nonempty consecutive index interval}}
\left(\sum_{j\in I}D_j\right)^{-\theta}.
\]

**2. Exact sector power count.** Partition the simplex into the finitely many sectors with \(D_{\pi(1)}\ge\cdots\ge D_{\pi(m)}\) for a permutation \(\pi\). Set \(v_j=D_{\pi(j)}/D_{\pi(j-1)}\in(0,1]\) for \(2\le j\le m\). Then
\[
D_{\pi(1)}=\left(1+\sum_{k=2}^{m}\prod_{j=2}^{k}v_j\right)^{-1}
\]
is between \(1/m\) and \(1\). The simplex volume element is
\[
D_{\pi(1)}^{m}\prod_{j=2}^{m}v_j^{m-j}\,dv_2\cdots dv_m.
\]
Let \(S_j=\{\pi(j),\ldots,\pi(m)\}\), and let \(H(S)\) count the nonempty consecutive index intervals entirely contained in \(S\). The largest coordinate in each interval is its first coordinate in the \(\pi\)-ordering. Thus the integrand times the Jacobian is comparable to
\[
\prod_{j=2}^{m}v_j^{m-j-\theta H(S_j)}.
\]
The integral on this sector converges if and only if \(\theta H(S_j)<|S_j|\) for each \(j\). If \(S\) has consecutive runs of lengths \(b_1,\ldots,b_h\) and total size \(k\), then
\[
H(S)=\sum_{a=1}^{h}\frac{b_a(b_a+1)}2\le\frac{k(k+1)}2.
\]
Every proper nonempty \(S\) has \(k\le m-1\); consequently \((2/m)H(S)\le k\), with equality only when \(k=m-1\) and \(S\) is consecutive. Among complements of a single index, consecutiveness occurs precisely when that index is \(1\) or \(m\). This proves finite exponential moments for \(\theta<2/m\); it also proves that all sectors away from small neighborhoods of the two endpoint vertices admit a moment of order \(2/m+\eta\), for some \(\eta>0\) depending on those neighborhoods.

Conversely, near \(D_1=1\) the radial coordinate \(\varepsilon=1-D_1\) has density \((m-1)\varepsilon^{m-2}\). There are exactly \(K=m(m-1)/2\) linear factors that vanish proportionally to \(\varepsilon\) with the remaining ratios held in a compact interior region. Hence the integral of \(e^{\theta R_m}\) contains a positive constant times \(\int_0^\delta\varepsilon^{m-2-\theta K}\,d\varepsilon\), which diverges for \(\theta\ge(m-1)/K=2/m\). This establishes the sharp moment boundary.

**3. Sharp leading constant.** In a fixed neighborhood of \(D_1=1\), write
\[
D=(1-\varepsilon,\varepsilon U_1,\ldots,\varepsilon U_{m-1}).
\]
Here \(U\sim\operatorname{Dirichlet}(1^{m-1})\) is independent of \(\varepsilon\), while \(\Pr(\varepsilon\le y)=y^{m-1}\) for \(0\le y\le1\). For each \(r\), the interval factor with initial index \(1\) tends uniformly to one, and its normalization \(C_r\) also tends uniformly to one. Every other interval factor equals \(\varepsilon\) times the corresponding Pascal linear factor of \(U\). It follows that
\[
R_m=K\log(1/\varepsilon)-\log Q_{m-1}(U)+O_m(\varepsilon),
\]
where the remainder is uniform over the positive angular simplex, for sufficiently small \(\varepsilon\).

For fixed \(U\), the radial threshold is asymptotic to
\[
\varepsilon_t(U)=\exp(-t/K)Q_{m-1}(U)^{-1/K}.
\]
The radial probability therefore satisfies
\[
\lim_{t\to\infty}e^{(2/m)t}\Pr(R_m>t,\ D_1>1-\delta\mid U)
=Q_{m-1}(U)^{-2/m}.
\]
A fixed small \(\delta\) and the uniform remainder give an integrable upper bound proportional to \(Q_{m-1}(U)^{-2/m}\). Its integrability follows by applying the sector calculation from step 2 in dimension \(m-1\), since \(2/m<2/(m-1)\). Dominated convergence now yields the contribution \(\mathbb E Q_{m-1}(U)^{-2/m}\). Reflection of the spacings gives the same contribution at \(D_m=1\).

On the complement of both endpoint neighborhoods, step 2 supplies a finite moment of some order \(2/m+\eta\). Markov's inequality makes its tail \(o(e^{-2t/m})\). Adding the two disjoint corner contributions gives \(A_m\) exactly. The asserted bounded-statistic tail is the substitution \(t=B_m/x\). The tail equivalent, or the sector calculation, gives the exponential-moment statement.

**4. The first explicit constant.** For \(m=3\), the angular vector is \(U=(u,1-u)\) with uniform \(u\in(0,1)\). The three factors of \(Q_2(U)\) are \(u\), \(1-u\), and \(u+(1-u)=1\). Thus
\[
A_3=2\int_0^1[u(1-u)]^{-2/3}\,du
=2\,\mathrm B(1/3,1/3).
\]

## Verification

The self-contained script `check_rps_tail.py` reproduces the recursive and Pascal representations, reversal symmetry, uniform-spacing minimum, interval combinatorics, and corner expansions in dimensions \(2\) through \(10\), with 4912 assertions passing. It also verifies the exact \(m=2\) tail check and evaluates the \(m=3\) gamma-function constant. These finite checks do not substitute for the sector and dominated-convergence proofs above.

The supplementary script `quad_rps3.py` numerically integrates *only the two endpoint neighborhoods*, at radius cutoff \(\delta=0.01\), for the three-spacing statistic. After multiplying by \(e^{2t/3}\), these partial contributions are approximately \(9.63394\), \(10.42555\), \(10.56841\), \(10.59418\) at \(t=20,25,30,35\), approaching the proved constant \(10.5998325\ldots\). Because this is a restricted-region calculation, it is not presented as an exact finite-threshold full tail probability.

## Relationship to prior work

Eller and Shtembari [1] defined \(R_m\), gave an exact distribution for the one-observation case \(m=2\), and used large simulations and interpolated CDFs to calibrate \(m\ge3\) at moderate and small probabilities. The present claim is only the exact fixed-\(m\) far-tail equivalent (with explicit corner integral), its sharp moment threshold, and the corresponding bounded-statistic lower tail for \(m\ge3\). In particular, the known \(m=2\) special case is not presented as a novel result.

Kosta and Windisch [2] give general real-log-canonical-threshold and multiplicity formulas for hyperplane arrangements. That broader theory explains why product-of-linear-form singularities can have power-law sublevel exponents, but its inspected statements do not compute the displayed RPS-specific coefficient \(A_m\), reduce the recursive normalizers, or identify the two endpoint mechanisms. Shtembari and Caldwell [3] use RPS as a testing component within multivariate procedures and do not, in the inspected sections, derive its fixed-sample univariate far-tail constant. The related 2023 doctoral thesis [4] is a residual comparison risk because its complete text was not obtained.

## Limitations

This is a fixed-sample far-tail asymptotic, not a uniform formula for growing sample size, a finite-threshold error bound, an exact complete CDF, or a power statement under alternatives. The constant \(A_m\) is an explicit finite-dimensional angular integral rather than a general elementary closed form. It has a beta-function evaluation for \(m=3\) and the already-known \(m=2\) consistency check. Numerical corner quadrature evaluates neither the complementary region nor the entire null tail at a finite threshold. Independent mathematical validation has not been performed.

## References

1. P. Eller and L. Shtembari, *A goodness-of-fit test based on a recursive product of spacings*, arXiv:2111.02252, first public version 2021-11-03, https://arxiv.org/abs/2111.02252 ; later J. Instrum. 18 (2023), P03048.
2. D. Kosta and D. Windisch, *Classification of real hyperplane singularities by real log canonical thresholds*, arXiv:2411.13392, first public version 2024-11-20, https://arxiv.org/abs/2411.13392 ; SIAM J. Appl. Algebra Geom. 10 (2026), 238–260.
3. L. Shtembari and A. Caldwell, *On goodness-of-fit tests for arbitrary multivariate models*, arXiv:2211.03478, first public version 2022-11-07, https://arxiv.org/abs/2211.03478 ; Phys. Rev. D 108 (2023), 123006.
4. L. Shtembari, *On non-parametric tests for discovery and limit setting in one and multiple dimensions*, doctoral thesis, Technical University of Munich, 2023; bibliographic reference in [3], complete text not inspected.
