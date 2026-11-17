# Poisson cross-dimer counts and parity jamming on two matching-linked cliques

## Finding

For each fixed \(\lambda>0\), take two complete graphs \(K_n\), each with vertices indexed by \(1,\ldots,n\), and join corresponding vertices by precisely the \(n\) matching edges. In irreversible dimer adsorption, each internal edge attempts deposition at rate \(1\), and each matching edge at rate \(\lambda\); a dimer is accepted if both endpoints are vacant. Let \(X_n\) denote the number of accepted matching-edge dimers and \(R_n\) the number of vacant vertices at jamming. Then

\[
X_n\ \xRightarrow[n\to\infty]{}\ \operatorname{Poisson}(\lambda),\qquad
R_n=2\mathbf1_{\{n-X_n\text{ is odd}\}}\quad\text{for every }n.
\]

In particular, if \(n\) is even,

\[
\Pr(R_n=2)\longrightarrow \frac{1-e^{-2\lambda}}2,\qquad
\Pr(R_n=0)\longrightarrow \frac{1+e^{-2\lambda}}2.
\]

For odd \(n\), the two limits are reversed. The graph always admits a perfect matching (the full set of matching edges), yet the probability that adsorption fails to cover it remains positive.

## Assumptions and scope

The vertices are permanently excluded from further deposition once matched. All arrival clocks are independent: internal graph edges have Poisson attempt processes of rate \(1\), and interclique matching edges rate \(\lambda\). The only successful transitions occur along currently available edges, hence the same law results from drawing the next available edge proportionally to its rate, removing its endpoints and repeating. All asymptotics hold for any **fixed** \(\lambda\in(0,\infty)\); no uniformity over rates depending on \(n\) is asserted. The parameter \(n\) is any integer at least \(2\).

## Proof

**Exact state dynamics.** Let \(K_A(t),K_B(t)\) be vacant counts and \(H(t)\) the number of matching edges both of whose endpoints are vacant. Write their current values as \(a,b,h\). Internal accepted edges in the two cliques have total rates \(\binom a2\) and \(\binom b2\); accepted crossing edges have total rate \(\lambda h\). An internal edge removing two uniformly chosen vacant sites in the first clique reduces \(h\) by a hypergeometric variable of mean \(2h/a\). Analogously for the other clique. A crossing event changes \((a,b,h)\) to \((a-1,b-1,h-1)\) and increments \(X_n\).

**Finite-time fluid law.** Put \(s=nt\) and \(U_{A,n}(s)=K_A(s/n)/n\), \(U_{B,n}(s)=K_B(s/n)/n\), and \(W_n(s)=H(s/n)/n\). Their predictable drifts are, uniformly on compact parameter regions,

\[
\dot U_A=-U_A^2+O(n^{-1}),\qquad
\dot U_B=-U_B^2+O(n^{-1}),\qquad
\dot W=-(U_A+U_B)W+O(n^{-1}).
\]

Each jump has size at most \(2/n\) and the quadratic variations of their martingale terms on any fixed interval \([0,S]\) are \(O_S(n^{-1})\): an internal event has scaled rate at most \(O(n)\), and a crossing event at most \(\lambda\). Doob's inequality and Grönwall's lemma therefore give uniform convergence in probability on \([0,S]\) to the unique initial-value solution

\[
u_A(s)=u_B(s)=\frac1{1+s},\qquad w(s)=\frac1{(1+s)^2},\qquad s\ge0.
\]

Conditional crossing intensity in \(s\)-time is \(\lambda W_n(s)\). The standard random-time-change coupling with a unit-rate Poisson process, together with convergence of the integrated intensity, gives the counting-process limit on each fixed \([0,S]\): the crossing events converge to an inhomogeneous Poisson process with intensity \(\lambda/(1+s)^2\). In particular,

\[
X_n(S/n)\Rightarrow\operatorname{Poisson}\!\left(\frac{\lambda S}{1+S}\right).
\]

**Uniform control of the terminal tail.** A finite-time limit cannot by itself justify passing to jamming. Define a bounded nonnegative Lyapunov function on all vacant states by

\[
F(a,b,h)=\begin{cases}h/a+h/b,&ab>0,\\0,&ab=0.\end{cases}\qquad 0\le F\le2.
\]

For \(a\ge3\), removal of a uniformly chosen internal edge from the first clique makes \(\mathbb E[h'/(a-2)]=h/a\), while \(\mathbb E[h'/b]=(1-2/a)h/b\), so that the first-clique contribution to \(-\mathcal LF\) equals \(h(a-1)/b\). For \(a=2\) this contribution is at least \(h(a-1)/b\), since removal eliminates all crossing edges and yields \(F=0\). The analogous statement holds in the second clique. Crossing events never increase \(F\), because \((h-1)/(a-1)\le h/a\) whenever \(1\le h\le a\), with the zero-denominator case defined as above. Thus when \((a,b)\ne(1,1)\), and \(h>0\),

\[
-\mathcal L F\ge h\left(\frac{a-1}{b}+\frac{b-1}{a}\right)\ge h.
\]

Here the last inequality is elementary for positive integer \(a,b\), excluding \((1,1)\). At \((a,b,h)=(1,1,1)\), only the crossing edge can be accepted and \(-\mathcal LF=2\lambda h\). Therefore with \(c_\lambda=\min\{1,2\lambda\}>0\), **for every reachable state**

\[
-\mathcal L F\ge c_\lambda h.
\]

Dynkin's formula from physical time \(S/n\) through termination and the nonnegativity of \(F\) give

\[
\begin{aligned}
\mathbb E[X_n(\infty)-X_n(S/n)]
&=\lambda\mathbb E\int_{S/n}^{\infty}H(t)\,dt\\
&\le \frac{\lambda}{c_\lambda}\,\mathbb E F\big(K_A(S/n),K_B(S/n),H(S/n)\big)
\longrightarrow\frac{2\lambda}{c_\lambda(1+S)}.
\end{aligned}
\]

The integral identity uses the compensated counting-process martingale. The displayed right-hand limit follows from the finite-time fluid law and boundedness of \(F\). Taking \(S\to\infty\) shows that any crossings after \(S/n\) are negligible uniformly as \(n\to\infty\). Together with the finite-time Poisson convergence this proves \(X_n\Rightarrow\operatorname{Poisson}(\lambda)\), since \(\lambda S/(1+S)\uparrow\lambda\).

**Exact terminal parity.** Every successful internal dimer removes two vertices of a single clique, while every successful interclique dimer removes one vertex from each. Hence, at jamming, the two vacant counts are congruent to \(n-X_n\) modulo \(2\). Neither clique can have two vacancies (any such pair would be a still-available internal edge). Both vacant counts are therefore in \(\{0,1\}\), and their parity is identical. They are both \(1\) precisely when \(n-X_n\) is odd, proving the claimed pathwise identity. Finally, the Poisson probability generating function \(\mathbb E[(-1)^X]=e^{-2\lambda}\) yields both parity limits.

## Verification

The accompanying Python file `verify.py` implements an exact rational dynamic program on the state \((a,b,h)\), using the actual hypergeometric rates for internal-edge choices, and an unrelated labeled-vertex event simulation. It also checks the Lyapunov generator inequality for thousands of finite states. Run `python verify.py` using Python 3 and no third-party packages. Finite enumeration checks are diagnostics; they are not substituted for the proof of the limit.

## Relationship to prior work

Penrose and Sudbury (2005) develop graph-based dimer adsorption and finite-time probability tools; their regular-tree results and bounded-degree Gaussian approximation do not state the fixed-size bridge-count Poisson limit for this growing-degree two-clique family. Dyer and Frieze (1991) study edge-greedy matching on fixed graphs, with performance bounds particularly for forests. The available abstract does not imply the present exact crossing-count limit and parity-jamming probability; a full-text comparison was not possible and remains a priority risk. Aronson, Dyer, Frieze and Suen (1995) analyze a different vertex-first randomized greedy matching algorithm. Uniformly random *perfect* matchings and randomly greedy *maximal* matchings are distinct probability laws; no transfer of published uniform-perfect-matching results is assumed.

## Limitations

Only two equal-sized complete communities, precisely one indexed matching between them, and constant positive \(\lambda\) are treated. The theorem concerns the **number** of accepted interclique dimers and the **jammed uncovered count**, not their spatial placement, the distribution of jamming time, or varying-\(\lambda\) regimes. Literature priority remains provisional because at least one relevant early algorithmic source was accessible only by abstract; a negative index search cannot exclude mathematically equivalent old results. No independent scientific audit has been performed.

## References

- M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability **15** (2005), 853–889, https://arxiv.org/abs/math/0503519 (first public preprint March 24, 2005), https://doi.org/10.1214/105051604000000765.
- M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms **2** (1991), 29–45, https://doi.org/10.1002/rsa.3240020104 (abstract examined).
- J. Aronson, M. Dyer, A. Frieze and S. Suen, *Randomized greedy matching. II*, Random Structures & Algorithms **6** (1995), 55–73, https://doi.org/10.1002/rsa.3240060107 (abstract examined).
