# Poisson hub switching and three distinct survival ensembles for many walkers on a star

## Finding

**Theorem (exact star collision-avoidance laws).** For integers \(n\ge3\) and \(2\le k<n\), let \(k\) independently moving labelled particles run continuous-time simple random walk on the \(n\)-vertex star, with rate one per particle: from a leaf a particle jumps to the hub, and from the hub it chooses any of the \(n-1\) leaves uniformly. Initially their positions are distinct. Let \(\tau\) be the first collision. Write \(A\) for configurations with no particle at the hub and \(B\) for configurations with one particle at the hub, and put
\[
 r=\frac{n-k}{n-1},\quad s=\sqrt{kr},\quad \lambda=k-s.
\]

(a) For any starting configuration in class \(A\), respectively \(B\), the exact no-collision survival probabilities are
\[
 S_A(t)=e^{-kt}\left(\cosh(st)+\frac{k}{s}\sinh(st)\right),\qquad
 S_B(t)=e^{-kt}\left(\cosh(st)+\frac{r}{s}\sinh(st)\right),\qquad t\ge0.
\]
In particular, both have exponential decay rate \(\lambda\).

(b) In the process obtained by conditioning on no collision up to a horizon and sending the horizon to infinity (the \(Q\)-process), the hub-occupation indicator is a symmetric two-state continuous-time Markov chain with switching rate exactly \(s\) in each direction. Consequently, its number of switches in a time interval of length \(t\) is \(\operatorname{Poisson}(st)\), and its unique stationary hub-occupation probability is \(1/2\), independently of \(n,k\).

(c) Three canonical ways of avoiding or suppressing collisions have exactly different long-time hub-occupation probabilities:
\[
 \underbrace{\frac12}_{\text{never-collide }Q\text{-process}}
 <\underbrace{\frac{\sqrt{k}}{\sqrt{k}+\sqrt r}}_{\text{ordinary independent walks conditioned on }\tau>t\text{, observed at }t\to\infty}
 <\underbrace{\frac{k}{k+r}}_{\text{exclusion, suppressing colliding jumps}}.
\]
The exclusion indicator alternates between exponential holding times with rates \(k\) and \(r\), unlike the homogeneous Poisson switching of the \(Q\)-process. In particular the exact total-variation distance between the respective stationary **hub indicators** of exclusion and the \(Q\)-process is
\[
 \frac{k-r}{2(k+r)}.
\]
The assertions concern hub-occupancy projections and hold also when the full labelled chain has disconnected communicating classes (in particular at \(k=n-1\)). No assertion about uniqueness of a stationary distribution on the entire labelled state space is needed.

## Assumptions and scope

All edges of the star are unweighted. Each particle's waiting clock has rate one. Particles carry distinct, persistent labels. The collision time is the first entry into a configuration with two particles at the same vertex. The \(Q\)-process is defined through finite-horizon conditioning \(\Pr(\cdot\mid\tau>T)\) with \(T\to\infty\), for each fixed finite observation interval. Its hub indicator has state \(0\) in \(A\) and \(1\) in \(B\). The theorem requires \(2\le k<n\): at \(k=n\) there is no class \(A\) and the formulas do not apply. All times are continuous, \(t\ge0\).

## Proof

**1. Exact killed generator.** Every collision-free configuration belongs to \(A\) or \(B\). In class \(A\), each of the \(k\) particles may jump to the vacant hub safely, so the total safe transition rate \(A\to B\) is \(k\), and the killing rate is zero. In class \(B\), only the hub particle can jump safely, and exactly \(n-k\) of the \(n-1\) leaves are vacant, so the total safe transition rate \(B\to A\) is \(r\). The other attempts collide: \(k-1\) leaf attempts and hub attempts of rate \((k-1)/(n-1)\), summing to \(k-r\). Thus the killed indicator generator, acting on test functions, is
\[
 Q=\begin{pmatrix}-k&k\\r&-k\end{pmatrix}.
\]
Since every full-state transition changes the hub class and the total safe and killing rates depend only on that class, this is an exact strong lumping, not an approximation.

**2. Survival.** Since \(Q=-kI+\begin{psmallmatrix}0&k\\r&0\end{psmallmatrix}\), whose off-diagonal part squares to \(kr I\), direct exponentiation gives
\[
 e^{tQ}=e^{-kt}\left(\cosh(st)I+\frac{\sinh(st)}s\begin{pmatrix}0&k\\r&0\end{pmatrix}\right).
\]
Multiplying by the all-ones column proves (a). Both positive leading coefficients accompany \(e^{-(k-s)t}\), proving the decay rate.

**3. Infinite-horizon conditioning and Poisson switching.** Define on the full collision-free state space the positive function \(h\) taking value \(\sqrt{k}\) on \(A\) and \(\sqrt r\) on \(B\). By step 1, the full killed generator \(\mathcal Q\) obeys \(\mathcal Qh=-\lambda h\) at every configuration. Step 2, applied from either class, gives \(\Pr_x(\tau>T)\sim c h(x)e^{-\lambda T}\) for one common positive constant \(c\): the two asymptotic coefficients have ratio \(\sqrt{k}/\sqrt r=h(A)/h(B)\). For a fixed finite path event \(F\) measurable by time \(t\), the Markov property and the survival asymptotics yield
\[
 \lim_{T\to\infty}\Pr_x(F\mid\tau>T)
 =\mathbb E_x\left[\mathbf1_F\mathbf1_{\{\tau>t\}}e^{\lambda t}\frac{h(X_t)}{h(x)}\right].
\]
The corresponding Doob transform multiplies each safe jump rate from \(x\) to \(y\) by \(h(y)/h(x)\). Hence the total hub-class jump rates are \(k\sqrt{r/k}=s\) and \(r\sqrt{k/r}=s\). The hub indicator is a symmetric two-state chain and its successive waiting times are independent \(\operatorname{Exp}(s)\), establishing the Poisson switch count and stationary probability in (b).

**4. Present-time conditioning versus exclusion.** Under conditioning only on \(\tau>t\), the class-\(B\) probability at observation time \(t\), started in \(A\), is \((e^{tQ})_{AB}/S_A(t)\). From the matrix exponential this tends to
\[
 \frac{k}{k+s}=\frac{\sqrt{k}}{\sqrt{k}+\sqrt r}.
\]
Starting in \(B\) yields the same limit (use \((e^{tQ})_{BB}/S_B(t)\)). In exclusion, collision-causing jumps are suppressed rather than killed. The exact lumped class jump rates remain \(k\) and \(r\), so stationary class-\(B\) probability is \(k/(k+r)\). Since \(0<r<k\), the three probabilities are strictly ordered, and the total variation of two Bernoulli laws is their parameter difference. This establishes (c).

## Verification

The independent finite-state enumeration script `verify_star.py` reconstructs each full labelled collision-free configuration for \(3\le n\le7\) and \(2\le k<n\). It enumerates all safe and fatal particle moves, tests the killed-generator eigenfunction and Doob rates on every configuration, and tests the exact lumped matrix identities and survival formulas at five times. The run produced 50,965 passing numerical/finite-state assertions. The theorem for all \(n,k,t\) is established by the analytic proof above, not by finite tests. Run using `python verify_star.py` with Python 3 standard library only.

## Relationship to prior work

Shiatis (arXiv:2610.00741v1, September 30, 2026) proves a general exponential-martingale/Doob-transform relationship between exclusion and noncolliding Markov chains. This supplies conceptual context and a broad abstract transform, but the paper's explicit examples concern asymmetric exclusion on cycles and on the integer line; its statement and examples do not give the star's exact survival eigenpair, universal Poisson hub-switch law, or three distinct hub-occupation probabilities. Our proof directly calculates these in the star family. Finite absorbing-chain quasi-stationarity and Doob transforms are established classical tools (Darroch–Seneta, 1967); the eigenvalue and distributional distinctions here are specific calculations, not claims of a new general conditioning theory.

## Limitations

No result about all-particle mixing, full labelled stationary uniqueness, collision avoidance on general trees, or independence of labelled trajectories is asserted. At \(k=n-1\), the full labelled configuration graph has disconnected components, although each projected hub law remains as stated. The distinction between long-horizon conditioning (\(Q\)-process) and observation at the terminal time conditioned on present survival is essential; the two distributions should not be conflated. Historical priority of this star-specific formula beyond the accessible literature requires external assessment.

## References

- R. Shiatis, *Exclusion vs Noncolliding dynamics in Markov processes*, arXiv:2610.00741v1 (first publicly posted September 30, 2026), https://arxiv.org/html/2610.00741v1.
- J. N. Darroch and E. Seneta, *On quasi-stationary distributions in absorbing continuous-time finite Markov chains*, Journal of Applied Probability 4 (1967), https://doi.org/10.2307/3212311.
