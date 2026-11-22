# Sharp minimax variance of two marginally uniform samples for bandlimited periodic quadrature

## Finding

Let \(m\geq1\) be any integer. Among **all** joint Borel laws of two individually uniform points on the unit circle, the equal-weight two-point quadrature rule for real trigonometric polynomials with frequencies at most \(m\) has exact smallest worst-case variance

\[
\inf_{\pi}\ \sup_{\substack{f\in\mathcal T_m^0\\\|f\|_{L^2}=1}}
\operatorname{Var}_{\pi}\left(\frac{f(X)+f(Y)}2\right)
=\frac{m-1}{2m}.
\]

A sharp construction is: draw \(X\) uniformly from the unit circle, draw \(J\) independently and uniformly from \(\{1,\ldots,m\}\), and set
\[
Y=\left(X+\frac{J}{m+1}\right)\bmod1.
\]

This construction has the same variance, equal to \((m-1)/(2m)\), for **every** mean-zero real trigonometric polynomial of unit \(L^2\) norm in the specified band. Furthermore, for every globally optimal coupling, the relative displacement belongs almost surely to the nonzero \((m+1)\)-st roots of unity, and all its first \(m\) cosine moments equal \(-1/m\). For \(m\ge3\), a deterministic **constant** relative shift cannot be optimal; for \(m=1,2\), the corresponding fixed shifts are optimal.

## Assumptions and scope

Identify the circle with \(\mathbb T=\mathbb R/\mathbb Z\), carrying normalized Lebesgue probability measure. Set
\[
\mathcal T_m^0=\left\{f(x)=\sqrt2\sum_{k=1}^{m}\bigl(a_k\cos(2\pi kx)+b_k\sin(2\pi kx)\bigr):a_k,b_k\in\mathbb R\right\}.
\]
Here \(\|f\|_{L^2}^2=\sum_{k=1}^m(a_k^2+b_k^2)\) and \(\int_{\mathbb T}f=0\). The coupling \(\pi\) ranges over every Borel probability measure on \(\mathbb T^2\) whose **two** marginals are each normalized Lebesgue measure. Its coordinates \(X,Y\) need not be independent, exchangeable, or related by a translation. The numerical integration rule is \(Q(f)=(f(X)+f(Y))/2\); it uses exactly two function evaluations and its weights are fixed at one half. All such rules are unbiased because each marginal is uniform. The risk supremum is over a fixed finite-dimensional real Fourier space and is an unconditional variance over the sampling law.

## Proof

**1. Relate worst-case variance to displacement moments.** Fix an admissible coupling, write \(\Delta=(Y-X)\bmod1\), and set
\[
c_k=\mathbb E_\pi\cos(2\pi k\Delta),\qquad 1\le k\le m.
\]
For any \(f\in\mathcal T_m^0\) with \(\|f\|_{L^2}=1\), marginal uniformity implies \(\mathbb E f(X)=\mathbb E f(Y)=0\) and \(\mathbb E f(X)^2=\mathbb E f(Y)^2=1\). Therefore
\[
\operatorname{Var}_\pi Q(f)=\frac{1+\mathbb E_\pi[f(X)f(Y)]}{2}.
\]
For each frequency \(k\), the functions \(u_k(x)=\sqrt2\cos(2\pi kx)\) and \(v_k(x)=\sqrt2\sin(2\pi kx)\) have unit norm, and the addition identity gives
\[
\frac{\mathbb E[u_k(X)u_k(Y)]+\mathbb E[v_k(X)v_k(Y)]}{2}=c_k.
\]
At least one of these two unit functions has cross-covariance at least \(c_k\). Thus, without assuming stationarity of the coupling,
\[
\sup_{\|f\|_{L^2}=1}\operatorname{Var}_\pi Q(f)
\ \ge\ \frac{1+\max_{1\le k\le m}c_k}{2}.
\]

**2. A universal Fejér-kernel obstruction.** The elementary nonnegative polynomial \(P_m(z)=\sum_{j=0}^m z^j\) satisfies
\[
0\le\mathbb E_\pi|P_m(e^{2\pi i\Delta})|^2
=(m+1)+2\sum_{k=1}^m(m+1-k)c_k.
\]
Because \(\sum_{k=1}^m(m+1-k)=m(m+1)/2\), the strict inequalities \(c_k<-1/m\) for all \(k\) are impossible. Consequently \(\max_k c_k\ge-1/m\). Combining with the previous display proves the lower bound \((m-1)/(2m)\) for **every** admissible joint law.

**3. Exact attainment.** Let \(X\) be uniform and let \(J\) be independent and uniform on \(\{1,\dots,m\}\), with \(Y=X+J/(m+1)\pmod1\). Translation preserves uniformity, so both marginals meet the requirement. Finite geometric-sum orthogonality gives, for each \(1\le k\le m\),
\[
\mathbb E e^{2\pi i k\Delta}
=\frac1m\sum_{j=1}^m e^{2\pi i kj/(m+1)}=-\frac1m.
\]
Averaging first over \(X\) and then over \(J\) and using the Fourier orthogonality relations gives, for every \(f\in\mathcal T_m^0\),
\[
\mathbb E[f(X)f(Y)]=-\frac1m\|f\|_{L^2}^2.
\]
Thus the variance of \(Q(f)\) is \(\frac{m-1}{2m}\|f\|_{L^2}^2\) for **every** \(f\) in the band. The lower bound is attained, and the minimax identity follows.

**4. Necessary support and moment conditions for all optima.** Suppose an arbitrary coupling attains the minimax value. Step 1 then forces \(c_k\le-1/m\) for every \(k\). In Step 2 every coefficient \(m+1-k\) is strictly positive. Its nonnegative left side and these upper bounds can coexist only if **every** \(c_k=-1/m\) and \(\mathbb E|P_m(e^{2\pi i\Delta})|^2=0\). The nonnegative random variable inside this expectation must vanish almost surely. The zeros of \(P_m\) on the unit circle are exactly the nonidentity \((m+1)\)-st roots. Therefore
\[
\Pr\left(\Delta\in\left\{\frac1{m+1},\ldots,\frac m{m+1}\right\}\right)=1.
\]
These conditions are **necessary** for optimality of an arbitrary nonstationary coupling; no assertion is made that they alone classify all such couplings.

**5. Rigidity against constant offsets.** If \(Y=X+\delta\pmod1\) is a constant-shift optimal coupling, Step 4 implies that both \(\cos(2\pi\delta)\) and \(\cos(4\pi\delta)\) equal \(-1/m\) when \(m\ge2\). The double-angle identity gives \(2/m^2-1=-1/m\), hence \((m-2)(m+1)=0\), requiring \(m=2\). Indeed \(\delta=1/3\) or \(2/3\) attains the bound at \(m=2\), and \(\delta=1/2\) attains it at \(m=1\). Thus no constant displacement can attain the minimax bound for \(m\ge3\).

## Verification

The accompanying standalone `verify.py` checks the exact triangular-weight identity and Fejér equality for finite bandwidths, numerical root-of-unity identities through bandwidth \(40\), and independently discretizes the two-sample mean-square integration error for four coefficient vectors at each bandwidth through \(16\). It completed **2,341 supplementary checks**. These finite calculations are not used as a proof of the all-bandwidth, all-coupling minimax assertion; the analytic steps above establish that assertion.

## Relationship to prior work

Antithetic variance reduction through dependence is classical. Casarin, Craiu, Frattarolo and Robert develop general dependence-based sampling frameworks and discuss covariance reduction and Monte Carlo integration. Dick, Goda and Suzuki analyze random rank-one lattice rules in periodic function spaces, while Kritzer, Kuo, Nuyens and Ullrich study nearly optimal randomized integration rates for smooth periodic classes. These constitute important earlier methodology. The present statement instead fixes **exactly two evaluations**, fixes **both sampling marginals**, optimizes over **every joint law**, and gives the **exact** finite-bandwidth minimax variance plus support rigidity. Roach and Wright discuss general optimal antithetic sampling for specified models, rather than the stated full-Fourier-band minimax quantifier. The Fejér nonnegativity argument itself is classical; originality is claimed only for the resulting specified two-node minimax characterization, subject to independent publication-priority verification.

## Limitations

The exact guarantee concerns only a one-dimensional finite Fourier band, marginally uniform nodes, equal deterministic weights, and unbiased two-evaluation estimators. It does not cover arbitrary smooth functions, additive observation noise, differing weights, more evaluations, or adaptive designs. In particular, the constructed rule has risk \(1\), rather than \((m-1)/(2m)\), on the normalized cosine at frequency \(m+1\): that mode aliases completely under all selected shifts. The relative reduction versus two independent uniform nodes is \(1/m\), which tends to zero as bandwidth grows. The support and cosine-moment conditions derived above do not amount to a classification of every optimal nonstationary coupling. A short proof using classical Fejér kernels leaves open the historical possibility of an equivalent previously known formulation.

## References

1. J. Dick, T. Goda and K. Suzuki, *Component-by-component construction of randomized rank-1 lattice rules achieving almost the optimal randomized error rate*, first publicly available September 23, 2021, https://arxiv.org/abs/2109.11694 .
2. R. Casarin, R. V. Craiu, L. Frattarolo and C. P. Robert, *Living on the Edge: An Unified Approach to Antithetic Sampling*, first publicly available October 28, 2021, https://arxiv.org/abs/2110.15124 .
3. P. Kritzer, F. Y. Kuo, D. Nuyens and M. Ullrich, *Lattice rules with random n achieve nearly the optimal error independently of the dimension*, 2017, https://arxiv.org/abs/1706.04502 .
4. W. Roach and R. Wright, *Optimal antithetic sampling plans*, 1977, https://doi.org/10.1080/00949657708810144 (abstract and bibliographic record inspected; full text not verified).
