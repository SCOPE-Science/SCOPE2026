# A universal logarithmic finite-time correction across tricritical population recovery and extinction

## Finding

On the tricritical line of the generalized Allee–logistic population map, the signed near-critical crossover has an **explicit next-order logarithmic correction in the inverse-square population**, with the same universal coefficient on both sides of the transition. Fix an initial density \(x_0\in(0,1)\). For \(m\in[1/3,1/2]\), take \(h=(1-2m)/m\) and \(r=(1+\delta)/m\); the map becomes exactly
\[
x_{n+1}=(1+\delta)x_n(1-x_n^2).
\]
Let \(\varepsilon=|\delta|>0\), \(a_\delta=(1+\delta)^{-2}\), and
\[
B_\delta(n)=\varepsilon a_\delta^n x_0^{-2}
+\frac{2\varepsilon a_\delta(1-a_\delta^n)}{1-a_\delta}.
\]
For either sign of \(\delta\), each \(0<s_0<S<\infty\), and all integers \(n\) satisfying \(s_0\le n\varepsilon\le S\),
\[
\boxed{\frac{\varepsilon}{x_n^2}=B_\delta(n)
+\frac32\varepsilon a_\delta^n\log(1/\varepsilon)
+O_{x_0,s_0,S}(\varepsilon).}
\]
The error is uniform in these integers and in the sign of \(\delta\) as \(\varepsilon\downarrow0\). In particular, the logarithmic coefficient \(3/2\) is nonzero and sign-independent after the exact linear-growth factor is separated. For sequences with \(n\varepsilon\to s>0\), the established leading finite-time scaling law is recovered:
\[
\frac{\varepsilon}{x_n^2}\longrightarrow
\begin{cases}1-e^{-2s},&\delta=+\varepsilon,\\
e^{2s}-1,&\delta=-\varepsilon.
\end{cases}
\]
At exact tricriticality \(\delta=0\), there is a finite \(c(x_0)\) such that
\[
\frac1{x_n^2}=2n+\frac32\log n+c(x_0)+o(1).
\]
The new quantitative claim is the two-sided, joint parameter/time logarithmic correction with a uniform order-\(\varepsilon\) remainder, not the already established leading finite-time scaling or the generic parabolic mechanism.

## Assumptions and scope

The original population map is \(x_{n+1}=r x_n(1-x_n)[m(x_n-h)+1-m]\), for population fractions \(x_n\in[0,1]\). Fix \(m\in[1/3,1/2]\) and its tricritical Allee threshold \(h=(1-2m)/m\), then let \(r=(1+\delta)/m\), \(|\delta|\) sufficiently small. Fix one \(x_0\in(0,1)\) independently of \(\delta\). All iterates remain strictly between zero and one. Here \(n\) denotes discrete iteration, not a continuous-time interpolation; the parameter window is \(\delta\to0\) with \(n|\delta|\) in any prescribed compact subset of \((0,\infty)\). Constants can depend on the fixed initial state and the compact window. These assumptions exclude initial data moving toward zero with \(\delta\) and observation times outside the stated window.

## Proof

**Exact reduction.** At the specified Allee threshold, \(m(x-h)+1-m=m(1+x)\). Therefore the original map becomes precisely \(x_{k+1}=(1+\delta)x_k(1-x_k^2)\). Choose \(|\delta|\le1/8\), so that the map takes \((0,1)\) into \((0,1/2)\), because \(\max_{0\le x\le1}x(1-x^2)=2/(3\sqrt3)\). If \(\delta>0\), the unique positive equilibrium is \(x_*=\sqrt{\delta/(1+\delta)}\), below \(1/\sqrt3\); the map is increasing on \([0,1/2]\). For the fixed positive initial state and sufficiently small \(\delta\), its first iterate is larger than \(x_*\). The subsequent iterates decrease toward \(x_*\), since above \(x_*\) one has \((1+\delta)(1-x^2)<1\) and monotonicity prevents crossing. When \(\delta\le0\) they decrease to zero. Thus the transformed positive sequence \(y_k=x_k^{-2}>1\) is well defined; its denominator is uniformly separated from one at least after the first step (and at step zero for fixed \(x_0\)).

**Exact rational recurrence.** Write \(a=(1+\delta)^{-2}\) and
\[
R(y)=\frac{3y-2}{(y-1)^2}.
\]
The identity \(y(1-y^{-1})^{-2}=y+2+R(y)\) yields
\[
y_{k+1}=a\,[y_k+2+R(y_k)],
\qquad R(y)>0\quad(y>1),
\qquad R(y)=\frac3y+O(y^{-2})\quad(y\to\infty).
\]
The exact variation-of-constants identity is
\[
y_n=a^n y_0+\frac{2a(1-a^n)}{1-a}
+a^n\sum_{k=0}^{n-1}a^{-k}R(y_k).
\tag{1}
\]

**Uniform control to the inverse parameter time scale.** Fix \(S<\infty\) and restrict \(0\le k\le S/\varepsilon\), with \(\varepsilon=|\delta|\). On this window both \(a^k\) and \(a^{-k}\) are bounded above and away from zero by constants depending only on \(S\). As \(R(y_k)\) is uniformly bounded for the fixed initial state, comparison of the recurrence with the affine recurrences \(z_{k+1}=a(z_k+2)\) and \(Z_{k+1}=a(Z_k+2+C)\) gives
\[
c_S(k+1)\le y_k\le C_{x_0,S}(k+1).
\tag{2}
\]
Because \(|a-1|\le C\varepsilon\), the recurrence and (2) imply for \(k\ge1\)
\[
|y_{k+1}-y_k-2|\le C_{x_0,S}
\left(\varepsilon(k+1)+\frac1{k+1}\right).
\]
Summing shows
\[
y_k=2k+O_{x_0,S}\bigl(1+\varepsilon k^2+\log(k+1)\bigr)
\quad (1\le k\le S/\varepsilon).
\tag{3}
\]
Combining (2), (3), and the rational expression for \(R\) gives
\[
R(y_k)=\frac{3}{2k}
+O_{x_0,S}\!\left(\varepsilon+
\frac{1+\log(k+1)}{k^2}\right)
\quad (k\ge1).
\tag{4}
\]
Since \(|a^{-k}-1|\le C_S\varepsilon k\), multiplying (4) by \(a^{-k}\) and summing from \(1\) to \(n-1\) incurs a total error bounded by a constant (the \(\varepsilon\) terms sum to \(O(\varepsilon n)\), the square-summable terms to \(O(1)\), and the difference in harmonic weights to \(O(\varepsilon n)\)). Including \(k=0\),
\[
\sum_{k=0}^{n-1}a^{-k}R(y_k)=\frac32\log n+O_{x_0,S}(1).
\tag{5}
\]
On the mesoscopic strip \(s_0\le n\varepsilon\le S\), \(\log n=\log(1/\varepsilon)+O_{s_0,S}(1)\). Multiplying (1) by \(\varepsilon\) and using (5), with bounded \(a^n\), proves the boxed uniform expansion, including both signs of \(\delta\). Finally \(n\log a\to\mp2s\) as \(\delta=\pm\varepsilon\) and \(2\varepsilon a/(1-a)\to\pm1\), giving the stated leading profiles.

**Exact critical endpoint.** With \(\delta=0\), the preceding estimates hold for arbitrarily large \(n\), with \(y_k=2k+O(\log(k+1))\). Then \(R(y_k)-3/(2k)=O(\log(k+1)/k^2)\), which is absolutely summable. As \(\sum_{k=1}^{n-1}1/k-\log n\) tends to Euler's constant, the difference \(y_n-2n-(3/2)\log n\) converges to a finite limit depending on \(x_0\). This proves the critical matching formula.

## Verification

The standalone `verify.py` uses exact symbolic simplification to check the GAL cubic reduction and rational inverse-square recurrence. It also performs numerical signed-crossover checks for ten nonzero parameter choices and tests stabilization of the critical renormalized inverse-square sequence. The successful output ends with `VERIFY_OK exact_recurrence=1 GAL_reduction=1 signed_crossover_samples=10 critical_constant=1`. These finite computations corroborate algebra and sample behavior only; the quantifiers and error uniformity are justified by the preceding analytic comparison and summability proof.

## Relationship to prior work

Pires, Andrade, and Herrmann introduced the generalized Allee–logistic map, established the tricritical coordinates, its critical \(n^{-1/2}\) decay exponent, and a stationary parameter-crossover function. The leading time-dependent pitchfork scaling belongs to earlier work: Corral developed universal finite-time scaling for pitchfork maps, and Martin, Tang, and Chialvo studied finite-time scaling on low-dimensional map bifurcations. The present result does not claim those leading behaviors as new. The proposed additional fact is the uniform signed near-tricritical \(\varepsilon\log(1/\varepsilon)\) contribution to \(\varepsilon/x_n^2\), with the explicit coefficient \(3/2\) and an order-\(\varepsilon\) remainder. General parabolic iteration theory can yield logarithmic corrections at a fixed parameter; the analysis here tracks the correction through a two-sided joint parameter/time limit. The full freely available texts of the relevant finite-time scaling preprints were inspected, including their derivations and appendices; their leading-scale theorems do not explicitly provide this coefficient or the uniform next-order error. Broader parabolic-iteration literature remains a historical-priority risk.

## Limitations

The initial density is fixed, strictly between zero and one; the theorem does not cover parameter-dependent vanishing initial densities. The observation window stays at positive finite scaled times. It does not address noise, external migration, higher-period attractors away from tricriticality, or arbitrary Allee parameter perturbations. It is an analytic result for a special one-parameter slice, not a claim about experimental population measurements. The potential overlap with broad parabolic-iteration results and unlocated higher-order scaling literature is a residual historical-priority risk; independent review has not been performed.

## References

1. Marcelo A. Pires, José S. Andrade Jr., Hans J. Herrmann, *Tricriticality and chaos in a generalized Allee-logistic map*, arXiv:2606.05351v1 (first public June 3, 2026), https://arxiv.org/abs/2606.05351.
2. Álvaro Corral, *Universal finite-time scaling in the transcritical, saddle-node, and pitchfork discrete and continuous bifurcations*, arXiv:2405.19947 (first public May 30, 2024); *Chaos* **35** (2025) 013106, doi:10.1063/5.0231950.
3. Daniel A. Martin, Qian-Yuan Tang, Dante R. Chialvo, *Finite-time scaling on low-dimensional map bifurcations*, arXiv:2505.24673 (first public May 30, 2025); *Physical Review Research* **7** (2025) 043241, doi:10.1103/73cc-j6mx.
