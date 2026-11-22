# Three is the sharp local-attractor capacity of a conformist behavioral SIRS model

## Finding

**Theorem.** In the behavioral susceptible–infectious–recovered–susceptible (SIRS) model defined below, for every admissible choice of parameters there are **at most three locally exponentially attracting equilibria** in the closed biological phase space. Of these, at most one has genuinely mixed intervention adherence \(0<x<1\); the other two can occur at the fully non-adherent and fully adherent faces. This bound is sharp. A strictly admissible rational choice of parameters has exactly six biological equilibria, with exactly three hyperbolic sinks: one endemic non-adherence state, one endemic mixed-adherence state, and one disease-free full-adherence state. Their coexistence persists on an open parameter neighborhood.

For the exact parameter choice in the proof, the three sinks in \((S,I,x)\) coordinates are
\[
\boxed{\left(\frac13,\frac13,0\right),\qquad
\left(\frac{64}{75},\frac{11}{150},\frac34\right),\qquad
(1,0,1).}
\]
The three remaining equilibria are not locally attracting.

## Assumptions and scope

Let \(S,I,R\ge0\) be susceptible, infectious, and recovered fractions with \(S+I+R=1\), and let \(x\in[0,1]\) be the proportion following a voluntary protective intervention. The dynamics on the invariant simplex \(S\ge0,I\ge0,S+I\le1,0\le x\le1\) are
\[
\begin{aligned}
\dot S&=\mu-\beta b(x)SI+\delta(1-S-I)-\mu S,\\
\dot I&=\beta b(x)SI-(\gamma+\mu)I,\\
\dot x&=\varepsilon x(1-x)\alpha(x,I),
\end{aligned}
\]
\[
b(x)=(1-ax)(1-ex),\qquad
\alpha(x,I)=-c+a\xi\beta I(1-ex)+\kappa(2x-1).
\]
Assume \(\beta,\gamma,\delta,\mu,\xi,c,\varepsilon>0\), \(0\le a,e\le1\), and \(\kappa\ge0\). Infection-state-independent adherence, homogeneous mixing, and the above replicator update are essential model assumptions. An equilibrium is *locally exponentially attracting* if every eigenvalue of its full three-dimensional Jacobian has strictly negative real part (on the biological state space, with natural one-sided interpretation on faces).

## Proof

**Step 1: at most one stable equilibrium on either adherence face.** For any fixed \(x\in[0,1]\), set
\[
\rho=\frac{\beta}{\gamma+\mu},\quad
K=\frac{\delta+\mu}{\delta+\mu+\gamma}.
\]
The fixed-adherence SIRS subsystem has the disease-free equilibrium \((S,I)=(1,0)\) and, if and only if \(\rho b(x)>1\), the positive endemic equilibrium
\[
S_x=\frac{1}{\rho b(x)},\qquad
I_x=K\left(1-\frac{1}{\rho b(x)}\right).
\]
At the disease-free state the infection eigenvalue is \((\gamma+\mu)(\rho b(x)-1)\), so that state is unstable within its adherence face if the endemic equilibrium exists. At a positive endemic state, the epidemiological Jacobian has negative trace and positive determinant, and hence its two eigenvalues lie in the left half-plane. At the threshold \(\rho b(x)=1\), the disease-free equilibrium has a zero eigenvalue. Thus each of \(x=0\) and \(x=1\), which is invariant because of the replicator factor, contains at most one locally exponentially attracting equilibrium of the full system. (The extra transverse eigenvalue may render even that one unstable.)

**Step 2: no stable disease-free mixed-adherence state.** On the infection-free set \(I=0\), the behavioral payoff is \(\alpha(x,0)=-c-\kappa+2\kappa x\). If \(\kappa=0\), it has no interior zero because \(c>0\); if \(\kappa>0\), any interior zero has the strictly positive behavioral eigenvalue \(2\varepsilon\kappa x(1-x)\). Because the Jacobian is block triangular at \(I=0\) in the infectious direction, this eigenvalue is an eigenvalue of the full Jacobian. Hence no disease-free interior-adherence equilibrium is locally exponentially attracting. If \(a=0\), then \(\alpha\) is also independent of infection prevalence; the same argument excludes *all* locally attracting interior-adherence equilibria.

**Step 3: strict concavity limits stable endemic mixed-adherence states to one.** Suppose \(a>0\), and consider the positive endemic region \(0<x<1\) with \(\rho b(x)>1\). Write \(P=a\xi\beta K>0\). At an interior endemic equilibrium the adherence fraction is a zero of
\[
\begin{aligned}
G(x)&=\alpha(x,I_x)\\
&=-c-\kappa+2\kappa x+P(1-ex)-\frac{P}{\rho(1-ax)}.
\end{aligned}
\]
The denominators are strictly positive throughout this region. Direct differentiation gives
\[
G'(x)=2\kappa-Pe-\frac{Pa}{\rho(1-ax)^2},\qquad
\boxed{G''(x)=-\frac{2Pa^2}{\rho(1-ax)^3}<0.}
\]
Thus \(G'\) is strictly decreasing. More strongly, \(G\) is strictly concave, so it has at most two distinct zeros, and **at most one zero can have \(G'(x)<0\)**: if \(x_1<x_2\) are two distinct zeros, strict concavity makes \(G'(x_1)>0\) and \(G'(x_2)<0\). This remains true on every interval comprising a positive-endemic branch because \(b(x)\) is nonincreasing on \([0,1]\); in fact its endemic domain is an interval.

At a positive endemic equilibrium, writing \(A\) for the upper-left \((S,I)\) epidemiological Jacobian, direct differentiation and a Schur complement give
\[
\det A=\beta b(x)I_x(\mu+\delta+\gamma)>0,
\quad
\det J=\varepsilon x(1-x)\det A\,G'(x).
\]
A three-dimensional Hurwitz matrix has negative determinant. Hence \(G'(x)<0\) is **necessary** for an attracting interior endemic equilibrium (it is not asserted to be sufficient). Strict concavity therefore permits at most one. Combined with Steps 1–2, there can be at most three locally exponentially attracting equilibria. This argument also covers equality and tangency boundaries: a root with \(G'=0\) gives a zero Jacobian determinant and is not exponentially attracting.

**Step 4: exact attainment with a strictly admissible rational parameter vector.** Choose
\[
\begin{gathered}
a=e=\frac12,\quad\beta=3,\quad\gamma=\frac23,\quad
\mu=\delta=\frac13,\quad\xi=\frac43,\\
c=\frac{41}{140},\quad\kappa=\frac{169}{420},\quad
\varepsilon=\frac1{10}.
\end{gathered}
\]
Then \(\rho=3\), \(K=1/2\), \(P=1\), and on the positive endemic branch
\[
G(x)=\frac{2(4x-3)(4x-1)}{105(x-2)}.
\]
Its only two roots are \(x=1/4\) and \(x=3/4\). Both lie below the threshold \(2-2/\sqrt3\) at which endemic prevalence vanishes. On the disease-free branch the unique interior behavioral equilibrium is \(x=146/169\), where the disease eigenvalue is negative. The complete biological equilibrium list is:

| \((S,I,x)\) | Stability |
|---|---|
| \((1,0,0)\) | Saddle (infection invades) |
| \((1/3,1/3,0)\) | Sink |
| \((64/147,83/294,1/4)\) | Saddle |
| \((64/75,11/150,3/4)\) | Sink |
| \((1,0,146/169)\) | Saddle |
| \((1,0,1)\) | Sink |

For the lower and upper mixed endemic equilibria, respectively, the characteristic polynomials \(\lambda^3+C_1\lambda^2+C_2\lambda+C_3\) have exact coefficients
\[
\begin{aligned}
(C_1,C_2,C_3)_{x=1/4}&=\left(\frac{614017}{470400},\frac{20281}{23520},-\frac{83}{58800}\right),\\
(C_1,C_2,C_3)_{x=3/4}&=\left(\frac{248267}{336000},\frac{8989}{84000},\frac{11}{42000}\right).
\end{aligned}
\]
The first has \(C_3<0\) and therefore at least one positive real eigenvalue. The second satisfies all strict cubic Routh–Hurwitz inequalities; in particular
\[
C_1C_2-C_3=\frac{2224280063}{28224000000}>0.
\]
For the endemic no-adherence point the two epidemiological eigenvalues are \((-5\pm i\sqrt{23})/6\) and the behavior eigenvalue is \(-1/350\). For the disease-free full-adherence point the eigenvalues are \(-2/3,-1/4,-23/2100\). Both are sinks. The remaining disease-free states have positive eigenvalues: \(2\) at no adherence and \(1679/177450\) at interior adherence. Every listed equilibrium is thus hyperbolic. The explicit zero equation enumerates all biological equilibria, so no state has been omitted. Since each inequality is strict, the three sinks persist for sufficiently small perturbations of parameters, within the admissible region.

## Verification

Run `python3 verify.py` from the directory containing this result. The program uses only the Python standard library and exact rational arithmetic. It reconstructs the three model derivatives, checks all six equilibrium residuals and simplex inequalities, checks the exact endemic response and the sign of the reduced derivative at both roots, verifies the Jacobian determinant identity, and uses exact rational Routh–Hurwitz tests to distinguish the three sinks from the three other equilibria. The program explicitly checks the mixed-state characteristic coefficients and the strictly positive stability margin. This finite rational calculation establishes the **specific witness**; the universal at-most-three theorem follows from the analytic concavity, endpoint, and determinant arguments, not from numerical enumeration.

## Relationship to prior work

Kumata, Ito, and Yamamichi (2026) introduce this precise private-protection/source-control/conformity SIRS model. Their main Fig. 4 maps possible single and coexisting stable adherence states, and their Supplement S2–S3 defines the reduced function \(G\), the stationary-state conditions and the necessary stability sign \(G'<0\). The present contribution **does not claim those reductions or the sign criterion as new**. It combines the previously unstated strict-concavity consequence with a complete universal attractor-count bound and a fully exact rational witness attaining three different simultaneously stable outcomes. The originating paper discusses bistability and partial/full coexistence, without giving this sharp theorem and exact three-sink realization.

Saad-Roy and Traulsen (2023) study a related behavior–epidemic system without this private/source/conformity combination and report no concurrently stable endemic adherence equilibria. Martin, Castella and Hamelin (2026) study a related SIS imitation model and report at most one stable endemic adherence equilibrium at a time. Neither of those statements covers the present conformist SIRS parameter regime. A published entropy-convergence note for a *permanent-immunity, no-conformity* specialization proves global convergence under a source-control budget, which does not cover the present strictly positive immunity waning and conformity parameters. A separate finite-horizon Poisson masking-game result gives behavioral bistability without a coupled SIRS epidemic; it is not a three-sink capacity result for these equations.

## Limitations

The theorem counts **locally exponentially stable stationary states**; it does not rule out stable periodic orbits, quantify basins of attraction, or prove that every initial condition converges to one of the three sinks. It depends on the specified homogeneous, state-blind adherence and linear conformity incentive, and does not extend to heterogeneous risk groups, arbitrary payoff nonlinearities, or stochastic epidemics. The stable disease-free state still requires sufficient initial adherence; this is not a prediction that universal adherence will arise spontaneously. Local basin counts are model statements, not public-health prescriptions. The source paper's qualitative multistability diagrams and the accessible related literature limit historical-priority confidence; independent scientific validation and a wider literature search remain outstanding. A plausible related 2026 SIS masking article was examined from its abstract but full text was unavailable.

## References

1. R. Kumata, H. Ito, and M. Yamamichi, *Voluntary nonpharmaceutical intervention as a feedback-evolving game*, arXiv:2610.12519v1, first public October 7, 2026, https://arxiv.org/abs/2610.12519 and HTML/Supplement https://arxiv.t3mt.com/html/2610.12519v1 .
2. C. M. Saad-Roy and A. Traulsen, *Dynamics in a behavioral–epidemiological model for individual adherence to a nonpharmaceutical intervention*, Proceedings of the National Academy of Sciences **120** (2023), e2311584120, https://pmc.ncbi.nlm.nih.gov/articles/PMC10622941/ .
3. H. Martin, F. Castella, and F. Hamelin, *Wearing face masks to protect oneself and/or others: Counter-intuitive results from a simple epidemic model accounting for selfish and altruistic human behavior*, Journal of Theoretical Biology **624** (2026), 112395, https://doi.org/10.1016/j.jtbi.2026.112395 .
4. *Global endemic convergence under an explicit source-control budget*, public mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-global-endemic-convergence-under-an-explicit-source-control-budg--3291f6fe173b .
5. *A sharp bistability window for voluntary masking under finite-horizon Poisson exposure*, public mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-bistability-window-for-voluntary-masking-under-finite-ho--770aaaa71918 .
