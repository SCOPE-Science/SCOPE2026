# Full-support singular opinions at a critical random-action learning rate

## Finding
Consider a three-agent network with two stubborn agents that always act \(0\) and \(1\), and one ordinary agent whose opinion is \(X_t\in[0,1]\). The ordinary agent gives weight \(s\in(0,1)\) to its own Bernoulli action and weight \((1-s)/2\) to each stubborn action. For learning rate \(\alpha\in(0,1)\), its update is
\[
 X_{t+1}=(1-\alpha)X_t+\alpha\left(\frac{1-s}{2}+s B_t\right),
 \qquad \Pr(B_t=1\mid X_t)=X_t.
\]
Independent uniform random variables generate the successive actions conditionally on the current opinions. For every initial law on \([0,1]\):

1. There is exactly one stationary opinion law \(\mu_{\alpha,s}\), and the law of \(X_t\) converges to it in \(1\)-Wasserstein distance with contraction factor \(c=1-\alpha(1-s)<1\). In particular,
\[
 \mathbb E_{\mu}[X]=\frac12,\qquad
 \operatorname{Var}_{\mu}(X)=
 \frac{\alpha s^2}{4\{2(1-s)-\alpha(1-2s)\}}>0.
\]
2. With \(a=(1-s)/2\), the support is the affine copy \(a+s K_\alpha\) of the attractor of the two similarities \(y\mapsto(1-\alpha)y\) and \(y\mapsto(1-\alpha)y+\alpha\). It is the whole interval \([a,1-a]\) when \(\alpha\le1/2\), but a Cantor set of dimension \(\log 2/[-\log(1-\alpha)]\) when \(\alpha>1/2\).
3. At the exact contact point \(\alpha=1/2\), the stationary law is **singular continuous with full interval support**: it has no atoms, assigns probability one to a Lebesgue-null set, and charges every nonempty open subinterval of \([a,1-a]\). If \(h\) denotes the entropy rate (in natural units) of its stationary binary action sequence, then
\[
 h=\mathbb E_{\mu}[H(X)]<\log2,\qquad
 \dim_H\mu\le\frac{h}{\log2}\le
 1-\frac{s^2}{(6-4s)\log2}<1,
\]
where \(H(p)=-p\log p-(1-p)\log(1-p)\), and \(\dim_H\mu\) means the infimum of the Hausdorff dimensions of Borel sets having full \(\mu\)-measure. For \(\alpha>1/2\), the stationary law is also nonatomic and singular, though its support now has gaps.

In particular, *full topological support does not imply a density* for opinion equilibria; endogenous self-action feedback forces singularity at the same parameter at which the geometric gaps just close.

## Assumptions and scope
The stubborn agents have fixed opinions and fixed actions \(0\) and \(1\). The ordinary agent samples one Bernoulli action per discrete time step, with probability of \(1\) equal to its current continuous opinion. The update uses the ordinary agent's own action together with the two fixed actions, not a Bernoulli action drawn from a sampled other agent. The trust weights sum to one, the two stubborn influences are equal, and \(0<\alpha,s<1\). This is a reducible, absorbing-stubborn specialization of the random-actions learning rule, not an irreducible random-actions consensus network. No claim concerns more than one ordinary agent, unequal stubborn weights, or a nonlinear confidence gate.

Let \(W_1\) be the transportation distance with cost \(|x-y|\) on \([0,1]\). All limits and stationary distributions are for the discrete-time Markov law, not necessarily pathwise opinion convergence.

## Proof
**1. Contractivity, existence, and moments.** Write \(r=1-\alpha\) and \(a=(1-s)/2\). For starting opinions \(x\le y\), use the same uniform \(U\) to generate actions \(B_x={\bf1}\{U\le x\}\) and \(B_y={\bf1}\{U\le y\}\). The successor opinions remain ordered, hence
\[
 \mathbb E|X'_y-X'_x|=r(y-x)+\alpha s(y-x)=c(y-x).
\]
Taking infima over initial couplings proves \(W_1(P\nu,P\eta)\le cW_1(\nu,\eta)\). On compact \([0,1]\), the complete metric space of probability laws therefore has a unique invariant \(\mu\) by the contraction theorem; \(W_1(P^t\nu,\mu)\le c^tW_1(\nu,\mu)\le c^t\). The conditional mean is \(cX+\alpha a\), so stationarity gives \(m=cm+\alpha a=1/2\). With \(V=\mathbb E[(X-1/2)^2]\) under stationarity, total variance gives
\[
 V=c^2V+\alpha^2s^2\mathbb E[X(1-X)]
  =c^2V+\alpha^2s^2(1/4-V).
\]
Rearranging yields the stated formula and strictly positive variance. For any initial law of mean \(1/2\), the variance follows the exact recursion \(V_{t+1}=dV_t+\alpha^2s^2/4\) with \(d=(1-\alpha)(1-\alpha+2\alpha s)\in(0,1)\).

**2. Support and gap threshold.** The affine normalization \(Y=(X-a)/s\) transforms the two possible updates to \(f_0(Y)=rY\) and \(f_1(Y)=rY+\alpha\). Their conditional probabilities are \(1-(a+sY)\) and \(a+sY\). On \(Y\in[0,1]\), both probabilities are bounded below by \(a>0\). The invariant measure gives positive mass to every finite cylinder image and has support equal to the unique nonempty compact attractor \(K_\alpha=f_0(K_\alpha)\cup f_1(K_\alpha)\). When \(r\ge1/2\), the intervals \([0,r]\) and \([\alpha,1]\) cover \([0,1]\), and uniqueness of the attractor implies \(K_\alpha=[0,1]\). When \(r<1/2\), the two images are disjoint and the strong-separation similarity dimension is the unique \(d\) satisfying \(2r^d=1\). This proves the asserted Cantor support and dimension. For every finite binary word of length \(n\), its stationary action probability is at most \((1-a)^n\). Consequently no infinite action word has positive mass; the coding by the contracting maps shows \(\mu\) is nonatomic (overlapping codings at \(\alpha\le1/2\) are irrelevant to the critical and separated cases).

**3. The critical singularity.** Now \(\alpha=1/2\). Construct a bi-infinite stationary version driven by independent uniforms: starting the recursion at time \(-n\) and using common subsequent uniforms makes its values at time zero Cauchy in \(L^1\), since successive approximants differ in expected absolute value by at most \(c^n\). Their shift-equivariant limit realizes the unique stationary chain as a factor of the independent uniform sequence, and thus the joint state/action process and its binary action factor are stationary ergodic. Iterating the normalized recursion backward gives, almost surely,
\[
 Y_0=\sum_{j=1}^\infty 2^{-j}B_{-j}.
\]
The conditional probability of the current action given all past actions is exactly \(X_0=a+sY_0\), since the displayed binary series determines the current opinion. Therefore the entropy rate of the stationary binary process is
\[
 h=H(B_0\mid B_{-1},B_{-2},\ldots)=\mathbb E[H(X_0)].
\]
The Shannon--McMillan--Breiman theorem applies to its reversed stationary ergodic action process. For any \(\varepsilon>0\), there exist sets of at most \(\exp[n(h+\varepsilon)]\) binary past words of length \(n\) whose total stationary probability tends to one. Under the above binary coding, each word restricts \(Y_0\) to an interval of length \(2^{-n}\). Their union has Lebesgue length at most \(\exp[n(h+\varepsilon)-n\log2]\). Since \(H\) is strictly concave, the stationary mean is \(1/2\), and stationary variance is positive, \(h<\log2\). Choosing \(\varepsilon<\log2-h\), a subsequence of these covers has Lebesgue lengths summable while their stationary probabilities tend to one; hence \(\mu\) is supported on a Lebesgue-null set. The same covers show \(\dim_H\mu\le h/\log2\). Finally, Bernoulli's relative-entropy inequality \(\log2-H(p)\ge2(p-1/2)^2\) implies
\[
 \log2-h\ge2\operatorname{Var}_\mu(X)
 =\frac{s^2}{6-4s}.
\]
At \(\alpha=1/2\), dyadic cylinders are disjoint except for endpoint codings; the bound \((1-a)^n\to0\) makes every single opinion nonatomic. Together with the already-established full support, this proves singular continuity and the quantitative dimension bound.

For \(\alpha>1/2\), the separated support is a zero-Lebesgue-measure Cantor set and each infinite coding has probability zero by the same cylinder bound, proving singular continuity there as well.

## Verification
The included stand-alone `verify.py` uses only Python's exact rational arithmetic. It checks stationary and finite-time moment identities, the contraction and endpoint formulas, and the algebraic gap transition on a grid of rational learning rates and trust weights (550 exact checks). Execute `python verify.py` from a directory containing that file; expected output is `VERIFY_OK 550 exact rational checks`. The infinite support, ergodicity, entropy, and singularity statements are proved analytically above; finite verification cannot certify them.

## Relationship to prior work
Leshem and Scaglione introduced the random-actions learning rule and studied consensus and bounded-confidence fluctuations; the present specialization adds two absorbing agents with opposite fixed actions and proves a stationary-measure geometry. Abrahamsson, Danev, and Larsson analyzed random-actions networks with a single stubborn agent and convergence to that agent's action; this two-opposite-source system is not covered by their one-source consensus theorem. Cao and Cortez proved fractal equilibrium supports for a different random pairwise-persuasion, large-population model. In their symmetric setting the random persuasion branch probability is fixed by the mean, whereas here it depends on the current opinion; this difference is precisely what makes the critical full-support equilibrium singular instead of the ordinary fair dyadic law. Classical place-dependent iterated-function-system theory, coding arguments, Bernoulli entropy inequalities, and Shannon--McMillan--Breiman are invoked as established ingredients, not claimed as new general results. A wider, previously unnoticed theorem encompassing this exact special model remains a priority risk.

## Limitations
The full-support singularity is established at the exact rate \(\alpha=1/2\) for every \(s\in(0,1)\). The absolute-continuity classification for \(0<\alpha<1/2\) is not determined. The Hausdorff dimension bound concerns the measure, not the already-computed topological support; no equality with \(h/\log2\) is asserted. No almost-sure limit of the individual opinion path is asserted, and the model is not an empirical fit. The proof uses standard ergodic and information-theoretic theorems rather than a standalone derivation of those classical theorems. Independent external audit has not been performed.

## References
- A. Leshem and A. Scaglione, *The impact of random actions on opinion dynamics*, arXiv:1704.01660, first public version 2017-04-05. https://arxiv.org/abs/1704.01660
- O. Abrahamsson, D. Danev, and E. G. Larsson, *Opinion Dynamics with Random Actions and a Stubborn Agent*, arXiv:1912.04183, 2019. https://arxiv.org/abs/1912.04183
- O. Abrahamsson, D. Danev, and E. G. Larsson, *On the Impact of Random Actions on Opinion Dynamics*, arXiv:2012.15154, 2020. https://arxiv.org/abs/2012.15154
- F. Cao and R. Cortez, *Fractal opinions among interacting agents*, arXiv:2408.01624, 2024; SIAM Journal on Applied Dynamical Systems, 24 (2025). https://arxiv.org/abs/2408.01624
- M. F. Barnsley, S. Demko, J. Elton, and J. Geronimo, *Invariant measures for Markov processes arising from iterated function systems with place-dependent probabilities*, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 24 (1988), 367–394.
- The classical Shannon--McMillan--Breiman ergodic theorem and Pinsker/Bernoulli relative-entropy inequality, used in their standard forms.
