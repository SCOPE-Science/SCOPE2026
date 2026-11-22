# Five lateral lanes are sharp for two optimal mixing intensities in a nursery-connectivity model

## Finding
Fix a drift horizon \(T>0\). Larvae start in lateral lane 1 of an idealized river cross-section with \(n\) contiguous lanes. They jump in either direction across an existing adjacent-lane boundary at common rate \(m\geq0\), with reflecting bank endpoints. At the end of the horizon, a larva in lane \(j\) settles successfully with probability \(h_j\in[0,1]\), independently conditional on its lane. Let \(P^{(n)}(x)=e^{xQ_n}\), \(x=mT\), where \(Q_n\) is minus the combinatorial Laplacian of the \(n\)-vertex path, and set
\[
C_h(x)=\sum_{j=1}^n P^{(n)}_{1j}(x)h_j.
\]

**Sharp dimension bound.** For every \(n\le4\) and every fixed suitability vector \(h\in[0,1]^n\), \(C_h\) cannot have two distinct strict local maxima on \((0,\infty)\). This fails already for \(n=5\), even with equal nearest-neighbor rates and only one scalar mixing control.

**Two equal global maxima.** For \(n=5\) and
\[
h(q)=\frac1{100}(42,44,23,q,0),\qquad95\le q\le97,
\]
there are precisely three positive stationary intensities \(0<x_1(q)<x_2(q)<x_3(q)\). The first and third are strict local maxima and the middle is a strict local minimum. A *unique* \(q_*\in(95,97)\) makes the two maxima exactly equal; at \(q_*\), they are the only global maximizers over \(x\ge0\). For orientation only,
\[
q_*\approx96.08732901099,\quad x_1(q_*)\approx0.11866614,\quad x_3(q_*)\approx2.13686359,
\quad C_{h(q_*)}(x_1)=C_{h(q_*)}(x_3)\approx0.42101462.
\]
The certified claim is the exact existence, uniqueness and global optimality, not the displayed decimal rounding.

## Assumptions and scope
The lateral process is a continuous-time, finite-state, symmetric Markov chain. Its generator has \((Q_n)_{i,i+1}=(Q_n)_{i+1,i}=1\), \((Q_n)_{ii}=-\deg(i)\), and all other entries zero. No larvae are removed or settled before the common downstream evaluation time. The downstream velocity, mortality and per-lane settlement probabilities do not change with \(m\). The five-lane vector is a deliberately idealized heterogeneous nursery-suitability profile and is not an estimate of any particular river. The variable \(q\) is a settlement-quality percentage, not a habitat mixing rate; the latter is \(m=x/T\).

## Proof
**1. The sharp lower bound.** The path Laplacian has simple eigenvalues
\[
\lambda_k=2-2\cos(k\pi/n),\qquad k=0,1,\ldots,n-1.
\]
Thus \(C_h(x)\) is a constant plus at most \(n-1\) decaying real exponentials, and \(C_h'(x)\) has at most \(n-1\) nonzero exponential terms. A nonzero combination of \(r\) exponentials with distinct real exponents has at most \(r-1\) real zeros *counted with multiplicity*: divide by the slowest exponential, differentiate, and apply Rolle's theorem inductively, retaining multiplicities. Hence \(C_h'\) has at most \(n-2\) real zeros unless it vanishes identically. Two distinct strict interior maxima require a maximum, an intervening minimum, and another maximum, hence at least three derivative zeros. This is impossible for \(n\le4\). A constant score also has no strict maxima.

**2. Exactly three extrema with five lanes.** For \(n=5\), write \(F_q(x)=100C_{h(q)}(x)=e_1^{\mathsf T}e^{xQ_5}(42,44,23,q,0)^{\mathsf T}\). The exact-rational certificate described below establishes, for each endpoint \(q\in\{95,97\}\),
\[
F_q'(0)>0,\quad F_q'(1/2)<0,\quad F_q'(1)>0,\quad F_q'(4)<0.
\]
Because \(F_q'\) depends affinely on \(q\), these strict signs hold for every \(q\in[95,97]\). The intermediate value theorem supplies three positive derivative roots; the four-exponential zero bound permits no others and forces all three to be simple. Their alternating derivative signs give two strict local maxima and one strict local minimum.

**3. Certified opposite peak rankings at the parameter endpoints.** The certificate isolates the first and third roots for \(q=95\) in the rational intervals
\[
(0.1181,0.1182),\quad(2.0262,2.0263),
\]
and for \(q=97\) in
\[
(0.1191,0.1192),\quad(2.2297,2.2298).
\]
It then bounds the unknown stationary values by exact rational uniformization, using \(|F_q'(x)|\le\|Q_5(42,44,23,q,0)^{\mathsf T}\|_\infty\). The resulting rigorous enclosures for the *late maximum minus the early maximum*, in the unnormalized \(F_q\) scale, are
\[
-0.1190<\Delta(95)<-0.0855,\qquad0.0727<\Delta(97)<0.1070.
\]
These wider displayed rational bounds follow from (and are strictly weaker than) the exact checked rational intervals in the checker.

**4. Uniqueness of the equal-peak parameter.** Let \(p(x)=(e^{xQ_5})_{14}\). We prove \(p'(x)>0\) for every \(x>0\). There are four nonconstant spectral modes, so \(p'\) is a nontrivial four-exponential sum with at most three zeros, counted with multiplicity. Since the shortest path from lane 1 to lane 4 has three jumps, the exact matrix expansion gives \(p'(x)=x^2/2+O(x^3)\) at zero. Thus zero itself is a double root of \(p'\). The slowest spectral coefficient of \(p(x)\) is \(-\sqrt5/10\), and its decay rate is \((3-\sqrt5)/2\), so \(p'(x)>0\) for all sufficiently large \(x\). If \(p'\) ever became negative, it would have to cross zero twice on \((0,\infty)\), exceeding the three-zero total together with its double root at zero. Hence \(p'(x)>0\) everywhere positive.

All three stationary roots depend smoothly on \(q\), because they are simple. By the chain rule and stationarity,
\[
\Delta'(q)=p(x_3(q))-p(x_1(q))>0.
\]
Continuity, strict increase and the opposite endpoint signs in step 3 give exactly one \(q_*\) with \(\Delta(q_*)=0\).

**5. Global optimality at the tie.** At every \(q\in[95,97]\), \(F_q(0)=42\); its initial derivative is positive, so the early local maximum is strictly above 42. The stationary limiting value is \(\lim_{x\to\infty}F_q(x)=(109+q)/5\le41.2<42\). At \(q_*\) the only two local maxima have equal height, above both boundary limits. As the derivative has no other roots, these two are exactly the global maximizers over \([0,\infty)\).

## Verification
The self-contained standard-library Python file `verification/check_certificates.py` executes exact Fraction arithmetic, not floating-point sign decisions. It sets \(P=I+Q_5/2\), a stochastic matrix, and uses the uniformization identity
\[
e^{xQ_5}=e^{-2x}\sum_{k=0}^{\infty}\frac{(2x)^k}{k!}P^k.
\]
For each rational \(0\le x\le4\), it sums through term 65. The remaining exponential-series tail is bounded by
\[
R=\frac{(2x)^{66}}{66!}\frac{1}{1-(2x)/67}.
\]
Positive-series reciprocal bounds \(1/(S+R)\le e^{-2x}\le1/S\), where \(S=\sum_{k=0}^{65}(2x)^k/k!\), and the stochastic bound on powers of \(P\) give exact rational enclosures for all required values and derivatives. The checker tests the four derivative signs at both endpoint parameters, root-bracket endpoint signs, peak differences with a rigorous Lipschitz correction, and the three-jump leading coefficient. Its output is a finite certificate for precisely these inequalities; all-time statements follow from the analytic proof, not from a finite grid.

## Relationship to prior work
Farò and Wolter (2024) integrate numerical larval-drift trajectories and habitat suitability to assess riverine spawning-to-nursery connectivity, documenting that strong spatial barriers can leave much suitable habitat functionally unreachable. Their full text examines drift models, simulated restoration scenarios and hydraulic sensitivities, not the sharp five-lane mode-count theorem or an exact equality of two optimal mixing rates.

The spectral exponential-zero bound is classical and not claimed as new. A published five-state reversible-chain result on *first-passage density* establishes two modes with a non-path transition graph; a published four-vertex *operator Lipschitz norm* example has two peaks via switching maximizing edges. Neither is a fixed terminal expected suitability of a single unit-rate reflecting path with two equal global optima. A different two-design Brownian crossing comparison concerns ranking changes over downstream distance, not bimodality in one mixing control. These comparisons clarify the mathematical contribution without asserting historical uniqueness.

## Limitations
The model uses discrete uniform lateral lanes, common symmetric exchange, a fixed deterministic drift horizon, no early settling or mortality, and a selected heterogeneous suitability vector. It does not establish bimodality for all five-lane profiles or quantify realistic hydrodynamic flow control. The minimality is **within the stated uniform-rate finite path model for strict interior maxima**, not across arbitrary continuous-space dynamics or alternate objective functionals. The exact parameter \(q_*\) is implicitly unique; decimal values are illustrative. Historical-priority claims remain provisional pending broader expert comparison.

## References
1. D. Farò and C. Wolter, “Integrating Habitat Suitability and Larval Drift Modeling for Spawning-To-Nursery Functional Habitat Connectivity Analysis in Rivers,” *Water Resources Research* **60** (2024), e2023WR036827. First published 2024-09-16. https://doi.org/10.1029/2023WR036827.
2. R. R. McDonald and J. M. Nelson, “A Lagrangian particle-tracking approach to modelling larval drift in rivers,” *Journal of Ecohydraulics*. https://doi.org/10.1080/24705357.2019.1709102.
3. “A reversible five-state chain with a bimodal first-passage density” (2026), public mathematical research record: https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-reversible-five-state-chain-with-a-bimodal-first-passage-densi--38ac1ba31442.
4. “A unique heat-gradient migration and two transient amplification peaks on a weighted four-vertex path” (2026), public mathematical research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-unique-heat-gradient-migration-and-two-transient-amplification--ecbe5ad031f6.
