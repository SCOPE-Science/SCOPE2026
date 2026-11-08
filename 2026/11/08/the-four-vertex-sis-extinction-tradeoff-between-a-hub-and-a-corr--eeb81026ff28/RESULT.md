# The four-vertex SIS extinction tradeoff between a hub and a corridor

## Finding

Consider the continuous-time susceptible-infected-susceptible (SIS) process with unit recovery rate and transmission rate \(\lambda>0\) per infected--susceptible edge. On four vertices, compare the star \(S=K_{1,3}\) with the path \(P=P_4\). For each \(k\in\{1,2,3,4\}\), initialize the process by choosing its \(k\) infected vertices uniformly among all \(\binom4k\) possibilities. Write \(T_{G,k}\) for its first time at the all-healthy state and \(H_{G,k}(t)=\Pr(T_{G,k}>t)\).

**Theorem.** For every \(\lambda>0\) and every \(k\in\{1,2,3,4\}\),
\[
\mathbb E T_{S,k}>\mathbb E T_{P,k}.
\]
Nevertheless, the first nonzero terms of the short-time survival differences are
\[
\begin{aligned}
H_{S,1}(t)-H_{P,1}(t)&=-\lambda^2t^3/12+O_\lambda(t^4),\\
H_{S,2}(t)-H_{P,2}(t)&=+\lambda^2t^4/72+O_\lambda(t^5),\\
H_{S,3}(t)-H_{P,3}(t)&=-\lambda^2t^5/120+O_\lambda(t^6),\\
H_{S,4}(t)-H_{P,4}(t)&=-\lambda^2t^6/180+O_\lambda(t^7).
\end{aligned}
\]
Thus, for each \(k\in\{1,3,4\}\) and **every** \(\lambda>0\), the corridor has strictly greater short-deadline survival probability despite strictly smaller mean extinction time. At some later deadline, the hub has strictly greater survival probability; at least one crossing follows. No uniqueness or precise crossing time is claimed. For \(k=2\) the short-time and mean rankings both favor the hub, and no all-time distributional ordering is asserted. This is the minimum possible tree size for a topology-dependent comparison: every tree on at most three vertices is unique up to isomorphism for its order.

## Assumptions and scope

The graph is simple, undirected, has four vertices and three edges, and does not change over time. Every occupied site recovers independently at rate one; each occupied--vacant edge contributes an independent rate \(\lambda\) of colonization (or infection). The healthy state is absorbing. The initial occupied subset is chosen uniformly *conditional on its fixed size* \(k\). The comparison holds for the same absolute transmission rate \(\lambda\) in the two graphs, **not** for rates normalized separately by graph spectral radii or metastable prevalence. All times use recovery-rate units. At \(\lambda=0\) the models coincide in distribution, since no new infections occur.

The result gives a finite SIS-network benchmark, not a comparison for general tree sizes, individual fixed source positions, non-Markovian transmissions, interventions, or real habitats without empirical calibration.

## Proof

Label the star by edges \(\{0,1\},\{0,2\},\{0,3\}\) and the path by \(\{0,1\},\{1,2\},\{2,3\}\). A configuration is a bitmask \(s\in\{0,\ldots,15\}\). Let \(Q_G\) be the row generator on all sixteen masks, with off-diagonal entries
\[
Q_G(s,s\setminus\{v\})=1\quad(v\in s),\qquad
Q_G(s,s\cup\{v\})=\lambda\,|\{w\in s:\{v,w\}\in E(G)\}|\quad(v\notin s),
\]
and diagonal entries minus the row sum. The absorbing row at \(s=0\) is zero. Let \(u_s=\mathbf1_{\{s\ne0\}}\), and let \(\mu_k\) put weight \(1/\binom4k\) on each mask of size \(k\). Finite-state Markov theory gives the *exact* survival function
\[
H_{G,k}(t)=\mu_k^\mathsf T e^{Q_Gt}u.
\]
The coefficient of \(t^j\) is \(\mu_k^\mathsf T Q_G^ju/j!\). Computing these generator products with integer-polynomial entries, all differences vanish below \(j=k+2\), and their first nonzero coefficients are exactly the four coefficients in the theorem. This proves the strict small-time signs for each fixed positive \(\lambda\). The complete unreduced generator construction and coefficient identities are reproduced in `verify.py`.

For the means, let \(R_G=-Q_G[1{:}15,1{:}15]\), the \(15\times15\) transient negative generator, and let \(\boldsymbol1\) be the all-one column. The first-step equation is \(R_Gm_G=\boldsymbol1\), so that \(\mathbb E T_{G,k}=\mu_k^\mathsf T(0,m_G)^\mathsf T\). Write
\[
D(\lambda)=(3\lambda+2)(4\lambda+3)(4\lambda^2+9\lambda+6)
(12\lambda^3+31\lambda^2+32\lambda+12).
\]
Exact elimination, with no numerical approximation, gives
\[
\begin{aligned}
\Delta_1&=\frac{\lambda^2N_1(\lambda)}{2D(\lambda)},\\
\Delta_2&=\frac{\lambda^2N_2(\lambda)}{12(\lambda+1)D(\lambda)},\\
\Delta_3=\Delta_4&=\frac{\lambda^2N_3(\lambda)}{6(\lambda+1)D(\lambda)},
\end{aligned}
\]
where \(\Delta_k=\mathbb ET_{S,k}-\mathbb ET_{P,k}\), and
\[
\begin{aligned}
N_1(z)={}&96z^7+656z^6+1895z^5+3083z^4+3131z^3+2030z^2+792z+144,\\
N_2(z)={}&648z^8+5262z^7+18320z^6+36564z^5+46792z^4+40131z^3+22880z^2+7980z+1296,\\
N_3(z)={}&324z^8+2595z^7+8941z^6+17676z^5+22477z^4+19319z^3+11195z^2+4032z+684.
\end{aligned}
\]
Every coefficient of these three polynomials and every factor in the denominators is positive for \(\lambda>0\), so \(\Delta_k>0\) as claimed. The equality \(\Delta_4=\Delta_3\) also follows without algebra: the first recovery from the fully infected state occurs after mean time \(1/4\) and leaves a uniformly chosen infected triple, hence \(\mathbb ET_{G,4}=1/4+\mathbb ET_{G,3}\).

Finally, \(\mathbb ET_{G,k}=\int_0^\infty H_{G,k}(t)\,dt\) because extinction has finite mean. For \(k\in\{1,3,4\}\), the continuous difference \(H_{S,k}(t)-H_{P,k}(t)\) is strictly negative at sufficiently small positive \(t\), yet its integral is \(\Delta_k>0\). It must therefore be strictly positive at another positive time and cross zero at least once. The argument makes no uniqueness assertion.

## Verification

The standalone `verify.py` constructs two independent \(16\times16\) generators directly from edge lists, checks each row sum, calculates exact Taylor coefficients to the first nonzero difference for every initial count, and symbolically inverts the transient \(15\times15\) generators to verify each rational mean formula. All symbolic coefficients are checked to be nonnegative with positive support for numerators and strictly positive for denominators. An independent exact rational Gaussian elimination verifies the four mean gaps at each of three positive rational transmission rates. The checker uses Python 3 and SymPy; run `python verify.py` in the same directory. No stochastic simulation, finite-time truncation, or unverified floating-point root is used in the proof.

## Relationship to prior work

Mountford, Mourrat, Valesin and Yao's first publicly posted 2012 preprint develops extinction-time estimates for finite contact processes, especially large bounded-degree trees. Their asymptotic results do not distinguish the exact four-site hub and corridor under a uniform fixed initial count or their opposite short-time and mean rankings. Van de Bovenkamp and Van Mieghem (2015) derive exact mean survival times for complete and star networks and compare various graph types numerically at fixed normalized transmission or metastable prevalence, including path and star graphs. Their inspected analytical and comparison sections do not give the four-site, all-absolute-rate, all-four-initial-count sign formulas or the objective-ranking disagreement. The general Markov generator itself is classical: novelty is claimed only for this exact comparison and the minimality/tradeoff statement, not for matrix-exponential methods. Historical-priority assessment remains provisional, especially regarding other exact finite-graph SIS/reliability calculations.

## Limitations

The first Taylor term determines the short-time sign but not how many later sign changes occur. A positive mean gap implies a later positive difference but not stochastic dominance or uniqueness of a crossing. The finding does not extend by assertion to larger trees, rate-normalized topology comparisons, or fixed identified seeds. This is a theoretical SIS model rather than an intervention or empirical inference. A complete historical-priority census is not claimed.

## References

1. T. Mountford, J.-C. Mourrat, D. Valesin, Q. Yao, *Exponential extinction time of the contact process on finite graphs*, first public arXiv version dated 2012-03-13, https://arxiv.org/abs/1203.2972 .
2. R. van de Bovenkamp and P. Van Mieghem, *Survival time of the susceptible-infected-susceptible infection process on a graph*, Physical Review E 92, 032806 (2015), https://doi.org/10.1103/PhysRevE.92.032806 .
