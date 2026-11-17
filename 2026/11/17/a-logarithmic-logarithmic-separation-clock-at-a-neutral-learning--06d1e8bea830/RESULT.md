# A logarithmic-logarithmic separation clock at a neutral learning bifurcation

## Finding

Consider the symmetric two-player multiplicative-weights map
\[
F(x,y)=\left(\frac{x}{x+(1-x)e^{8(y-1/2)}},\frac{y}{y+(1-y)e^{8(x-1/2)}}\right),\qquad (x,y)\in(0,1)^2.
\]
Let \(L(x)=\log[x/(1-x)]\), and let \(f(x)=F(x,x)_1\). Define the countable exceptional set \(E=\bigcup_{k\ge0}\{z\in(0,1):f^k(z)=1/2\}\). For every fixed \(z\in(0,1)\setminus E\), there is \(\delta_0(z)>0\) such that, for any fixed \(0<\delta<\delta_0(z)\), the trajectory from
\[
(x_0,y_0)=\left(L^{-1}(L(z)+\varepsilon),L^{-1}(L(z)-\varepsilon)\right)
\]
with \(\varepsilon>0\) sufficiently small first reaches log-odds separation \(L(x_N)-L(y_N)\ge 2\delta\) at the finite integer time
\[
\boxed{N_{z,\delta}(\varepsilon)=\frac{\log(1/\varepsilon)}{\log3}
+\frac{\log\log(1/\varepsilon)}{2\log3}+O_{z,\delta}(1).}
\]
The coefficient of the logarithmic-logarithmic delay is independent of the nonexceptional diagonal start and sufficiently small fixed exit threshold. At the central starting point \(z=1/2\), which is exceptional, the corresponding law has **no** logarithmic-logarithmic term:
\[
N_{1/2,\delta}(\varepsilon)=\frac{\log(1/\varepsilon)}{\log3}+O_\delta(1).
\]
The same two-term law holds if the exit condition is replaced by a sufficiently small fixed physical separation \(x_N-y_N\ge2\delta\), after adjusting the allowable threshold and the bounded remainder. All clocks count original iterations of \(F\).

## Assumptions and scope

The gain is fixed at the neutral diagonal flip value \(a=8\), with symmetric payoff parameter \(b=1/2\). Only positive initial log-odds imbalance is written; reversing the players gives the opposite sign. The orbit starts in the open probability square. The exceptional set is precisely the backward orbit of the diagonal fixed point under the scalar map. The asserted global-in-diagonal-start statement uses the established convergence of all interior diagonal orbits to \(1/2\) at this critical gain. No assertion about the rate for every other exceptional start is made. The \(O(1)\) constants and allowable thresholds can depend on the fixed start and exit scale; they are not uniform over \(z\) or in \(\delta\).

## Proof

**1. Exact center–difference dynamics.** Define log-odds coordinates \(u=L(x)\), \(v=L(y)\), \(m=(u+v)/2\), \(d=(u-v)/2\). The logit identities for \(F\) are \(u'=u-8(y-1/2)\) and \(v'=v-8(x-1/2)\). Put \(t=\tanh(m/2)\), \(s=\tanh(d/2)\). Addition identities for \(\tanh\) give the exact recurrence
\[
 m'=m-\frac{4t(1-s^2)}{1-t^2s^2},\qquad
 d'=d+\frac{4s(1-t^2)}{1-t^2s^2}.
\]
For \(d>0\), the second increment is strictly positive. Taylor expansion uniformly on a small square \(|m|\le\rho\), \(0\le d\le\delta_*\) yields
\[
 m'=-m+\frac16m^3+\frac12md^2+O\bigl(|m|(m^2+d^2)^2\bigr),
\]
\[
 \frac{d'}{d}=3-\frac12m^2-\frac16d^2+O\bigl((m^2+d^2)^2\bigr).
\]
Choose \(\rho,\delta_*\) small enough that \(m'\) reverses sign and \(0<|m'|<|m|\) whenever \(m\ne0\), and that \(2\le d'/d\le4\). These assertions follow directly from the displayed expansions, because the leading decrease of \(|m|\) is \(|m|(m^2/6+d^2/2)\). Thus the center remains in this square while the growing difference stays below \(\delta_*\).

**2. Uniform control of the center up to first exit.** First assume \(0<|m_0|<\rho\), \(d_0=\varepsilon>0\), and let \(N\) be the first index with \(d_N\ge\delta\), for a fixed \(0<\delta<\delta_*/4\). The preceding bounds imply \(N<\infty\), \(\delta\le d_N\le4\delta\), and, by reversing the difference-growth inequalities,
\[
 \sum_{j=0}^{N-1}d_j^2\le\sum_{k=1}^{\infty}\delta^2 2^{-2(k-1)}\le\frac43\delta^2.
\]
The exact center expansion can be factored as \(m'=-m(1-m^2/6-d^2/2+O((m^2+d^2)^2))\). Writing \(w_j=m_j^{-2}\), with all \(m_j\ne0\) by step 1, gives
\[
 w_{j+1}-w_j=\frac13+w_jd_j^2+O(m_j^2+d_j^2+w_jd_j^4).
\]
After shrinking the square, the same formula and its positivity show \(w_{j+1}-w_j\ge c>0\) and \(w_{j+1}\le(1+Cd_j^2)w_j+C\). Discrete Gronwall and the bounded sum of \(d_j^2\) prove constants \(c_1,c_2>0\), independent of \(\varepsilon\) and \(N\), with
\[
 c_1(j+1)\le w_j\le c_2(j+1),\qquad 0\le j<N.
\]
(The constants may depend on the fixed nonzero \(m_0\).) Hence
\[
 w_j=w_0+\frac j3+O\left(\log(j+1)+\sum_{k<j}(k+1)d_k^2\right).
\]
Inverting this identity using \(w_j\asymp j+1\) yields
\[
\left|m_j^2-\frac3{j+1}\right|\le C\frac{1+\log(j+1)+\sum_{k<j}(k+1)d_k^2}{(j+1)^2}.
\]
The right side is uniformly summable for \(j<N\). Indeed, after reversing the double sum,
\[
 \sum_{j<N}\frac1{(j+1)^2}\sum_{k<j}(k+1)d_k^2
 \le C\sum_{k<N}d_k^2\le C\delta^2.
\]
Therefore, uniformly as \(\varepsilon\downarrow0\),
\[
 \boxed{\sum_{j=0}^{N-1}m_j^2=3\log N+O(1).}
\]
This is stronger than simply observing pointwise critical relaxation: it remains true along the **nonlinear off-diagonal orbit all the way to its first fixed-size separation**.

**3. The sharp escape clock.** The second Taylor formula in step 1 gives
\[
 \log(d_{j+1}/d_j)=\log3-\frac16m_j^2+O(m_j^4+d_j^2).
\]
Since \(\sum_{j<N}m_j^4\le C\sum(j+1)^{-2}<\infty\) and \(\sum_{j<N}d_j^2\le C\delta^2\), the harmonic identity of step 2 implies
\[
 \log(d_N/\varepsilon)=N\log3-\frac12\log N+O(1).
\]
By the exit definition, \(\delta\le d_N\le4\delta\), so the left side equals \(\log(1/\varepsilon)+O_\delta(1)\). We obtain \(N\asymp\log(1/\varepsilon)\) and, substituting \(\log N=\log\log(1/\varepsilon)+O(1)\), the boxed claim.

**4. Arbitrary nonexceptional diagonal starts.** By Chotibut–Falniowski–Misiurewicz–Piliouras (2018, Theorem 3.9), every diagonal trajectory at \(a=8\) approaches \(1/2\). Fix \(z\notin E\) and choose a finite \(K\) such that the unperturbed \(K\)-th diagonal log-odds \(m_K^*\) is nonzero and satisfies \(0<|m_K^*|<\rho/2\). Smoothness of the finite iterate and player-interchange symmetry give \(m_K=m_K^*+O(\varepsilon^2)\), \(d_K=c_{z,K}\varepsilon+O(\varepsilon^3)\), where \(c_{z,K}>0\) because each transverse derivative is strictly positive. Hence the local analysis applies from step \(K\), for sufficiently small initial imbalance and a sufficiently small fixed exit threshold. Replacing \(\varepsilon\) by \(d_K\asymp\varepsilon\) and adding the fixed transient \(K\) changes only the \(O(1)\) term.

**5. Central-start contrast and physical separation.** If \(z=1/2\), then \(m_0=0\) and the exact recurrence preserves \(m_j=0\). Now \(\log(d_{j+1}/d_j)=\log3+O(d_j^2)\), whose accumulated error is bounded up to exit; this gives the one-term law. Finally, on a small fixed neighborhood of \(m=d=0\), the difference \(x-y\) is a smooth, strictly positive multiple of \(d\), uniformly bounded above and below. Trapping a physical-separation exit between two logit exits at fixed nearby thresholds changes the corresponding times by at most a constant, because \(d_{j+1}/d_j\ge2\) until exit. This proves the stated physical version.

## Verification

The accompanying `verify.py` implements the exact center–difference recurrence and checks finite iteration identities against direct probability-coordinate updates. It samples first-exit times at logarithmic initial imbalances and compares the exact asymptotic formula against the observed integer clock, including the exceptional center case. It uses an independent symbolic Taylor expansion with SymPy when that library is available; numerical tests corroborate but are not an infinite proof. The proof rests on the exact recurrence, uniform Taylor estimates, Gronwall bounds and convergent sums stated above.

## Relationship to prior work

Chotibut, Falniowski, Misiurewicz and Piliouras (2018) introduce precisely this two-player map, prove diagonal critical convergence at \(a=8\) and off-diagonal ultimate polarization. They do not quantify the singular first-separation clock. Kryzhevich and Zhang (2026) examine invariant averages, shift functions, and hyperbolic chaos for the related scalar replicator maps; those statements do not imply the near-diagonal finite-time law. A published result on global neutral-flip attraction and signed critical relaxation gives the symmetric scalar inverse-square and logarithmic asymptotics; these are **already known**, not claims of this finding. A separate published result on universal near-symmetry escape clocks treats \(a>8\) only and explicitly leaves the nonhyperbolic boundary \(a=8\) untreated. Its \(O(1)\)-accuracy logarithmic clock at a hyperbolic two-cycle does not imply the unbounded \(\log\log\)-delay at the neutral boundary. Here the main new ingredient is the uniform center harmonic-sum estimate along *nonlinear, off-diagonal* trajectories up to their exit; simply multiplying diagonal derivatives would not prove a nonlinear first-exit law.

## Limitations

The result concerns a fixed gain \(a=8\), exact payoff symmetry, and a fixed sufficiently small exit threshold. It gives an asymptotic first-separation time, not the subsequent time to a pure equilibrium, not a global-basin rate, and not a joint parameter–initial-imbalance scaling as \(a\) approaches \(8\). For exceptional diagonal starts other than the central fixed point no second-order clock is claimed. There remains historical-priority risk for unindexed investigations of nonhyperbolic two-player learning escape. Independent mathematical review has not been performed.

## References

1. S. Kryzhevich and Y. Zhang, *Shift maps and statistical invariants for some dynamical systems*, arXiv:2603.20685v1 (first public 2026-03-21), Sections 5–6. https://arxiv.org/html/2603.20685v1
2. T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831v1 (first public 2018-07-18), especially Theorems 3.9 and 4.6 and Section 4. https://arxiv.org/html/1807.06831v1
3. *Global neutral-flip attraction and signed critical relaxation in an entropic congestion map*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-global-neutral-flip-attraction-and-signed-critical-relaxation-in--54b59b4edf7d
4. *Universal near-symmetry escape clock in a two-player multiplicative-weights map*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-near-symmetry-escape-clock-in-a-two-player-multiplicat--ac69d0b9c5ad
