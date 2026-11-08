# Bottleneck depth controls the exact heavy tail of inverse-age social cascades

## Finding

**Theorem (finite-network bottleneck law).** For every finite undirected simple social network with integer adoption thresholds and at least one susceptible vertex belonging to the deterministic bootstrap closure of the initial adopter set, consider irreversible threshold adoption in continuous time. Each still-susceptible, currently eligible vertex adopts at instantaneous rate \(a/(t+2)\), with common \(a>0\), at physical time \(t\ge 0\). Let \(T\) be the time at which the deterministic closure is completely adopted. There are explicitly computable integers \(b\ge1\) and positive rational numbers \(A\), defined solely by the eligible-set counts along permitted adoption orders, such that

\[
\Pr(T>t)\sim \frac{A}{(b-1)!}\left(\frac{2}{t+2}\right)^a\left[a\log\left(\frac{t+2}{2}\right)\right]^{b-1},\qquad t\longrightarrow\infty.
\]

The exponent \(b-1\) is exactly one less than the greatest number of states having **exactly one eligible susceptible vertex** encountered along any feasible complete adoption order. Furthermore, for every real \(r>0\),

\[
\mathbb E[T^r]<\infty\quad\Longleftrightarrow\quad r<a.
\]

In particular, with the inverse-age exponent \(a=1\), the cascade completes almost surely in finite time but its mean completion time is infinite on every nontrivial finite network. For a seeded endpoint of a path with \(m\ge1\) remaining vertices and one-neighbor eligibility, \(b=m\) and \(A=1\); for a seeded hub of an \(m\)-leaf star, \(b=1\) and \(A=m\).

## Assumptions and scope

Let \(G=(V,E)\) be a finite simple undirected graph. Each nonseed vertex \(v\) of positive degree has an integer threshold \(q_v\) with \(1\le q_v\le\deg(v)\); for an isolated nonseed set \(q_v=1\), which is unattainable. Fix a nonempty initial adopter set \(S_0\subseteq V\). A susceptible vertex \(v\) becomes **eligible** at adopter set \(S\) if it has at least \(q_v\) neighbors in \(S\). Define \(B\) by iterating deterministic bootstrap addition of all eligible vertices starting from \(S_0\) until no new vertex is eligible. Assume \(B\setminus S_0\ne\varnothing\). Vertices outside \(B\) never adopt. All original seeds remain adopted.

At each time \(t\ge0\), the jump \(S\to S\cup\{v\}\) for an eligible susceptible vertex \(v\) occurs at rate \(a/(t+2)\), independently of the other eligible-site clocks conditional on the current state. No other jumps occur. Thus the generator is a **common time-dependent scalar** times a finite pure-birth generator, with no memory reset on a failed activation attempt. This is a precisely specified continuous-time analogue of inverse-age *endogenous* activation, not an assertion about the paper's discrete random-asynchronous update schedule or its exogenous-reset rule.

A **permitted adoption order** is any listing of all \(m=|B\setminus S_0|\) new adopters such that every next vertex is eligible just before its adoption. Let \(\mathcal P\) be the nonempty set of these orders. For an order \(\pi\), write its successive transient adopter sets as \(S_{\pi,0}=S_0,\ldots,S_{\pi,m-1}\), and let \(e_{\pi,j}\) be the number of eligible susceptible vertices in \(S_{\pi,j}\). Each \(e_{\pi,j}\) is a positive integer. Put

\[
 b=\max_{\pi\in\mathcal P}\sum_{j=0}^{m-1}\mathbf1\{e_{\pi,j}=1\},\qquad
 A=\sum_{\substack{\pi\in\mathcal P:\,\#\{j:e_{\pi,j}=1\}=b}}\prod_{j:e_{\pi,j}>1}\frac{1}{e_{\pi,j}-1}.
\]

The empty product is one. These definitions involve no probabilistic asymptotic or fitted coefficient. In fact \(1\le b\le m\) and \(A>0\).

## Proof

**1. Closure and the logarithmic clock.** Eligibility is monotone in the adopter set. Consequently every reachable nonterminal \(S\subsetneq B\) has at least one eligible susceptible vertex: if not, it would be a closed superset of \(S_0\) strictly smaller than its least closed superset \(B\). Each permitted order has exactly \(m\) steps. Define the strictly increasing, unbounded time change

\[
 s(t)=a\log\left(\frac{t+2}{2}\right),\qquad \frac{ds}{dt}=\frac{a}{t+2}.
\]

In this transformed time the chain is homogeneous; every eligible vertex jumps at rate one, and a state with \(e\) eligible vertices has an exponential holding time of rate \(e\). Since only \(m\) transitions are needed and all holding-time rates are positive, its absorption time \(U=s(T)\) is finite almost surely.

**2. A complete order expansion.** Conditional on reaching a state with \(e\) eligible vertices, the next adopted vertex is uniform among them and the holding time is independent \(\operatorname{Exp}(e)\). Therefore, writing \(\phi(z)=\mathbb E[e^{-zU}]\), for \(\operatorname{Re}z\ge0\) the exact order expansion is

\[
 \phi(z)=\sum_{\pi\in\mathcal P}\prod_{j=0}^{m-1}\frac{1}{z+e_{\pi,j}}.
\]

This is not merely a finite-state simulation: it sums every possible complete adoption order, including those in which several vertices are simultaneously eligible. Because the last transient state has one remaining eligible vertex, at least one factor \((z+1)^{-1}\) occurs on every order, and \(b\ge1\). Near \(z=-1\), the terms with exactly \(b\) unit-rate factors contribute \(A(z+1)^{-b}\). All their coefficients are positive, so no leading-pole cancellation is possible; terms from the other orders have poles of lower order. Thus

\[
 \phi(z)=\frac{A}{(z+1)^b}+O((z+1)^{-(b-1)})\quad(z\to-1).
\]

**3. Exact leading survival term.** For \(\operatorname{Re}z>0\), the Laplace transform of \(\Pr(U>s)\) is \((1-\phi(z))/z\). This is a rational function with poles only among the negative integers \(-1,-2,\ldots\). At \(z=-1\) it has leading principal part \(A/(z+1)^b\) (the factor \(-1/z\) has value one there). Partial-fraction inversion gives

\[
 \Pr(U>s)=\frac{A}{(b-1)!}s^{b-1}e^{-s}\bigl(1+o(1)\bigr),\qquad s\to\infty.
\]

All remaining poles at negative integers at most \(-2\) are exponentially smaller; lower-order terms at \(-1\) are smaller by powers of \(s\). Substituting \(s=s(t)\) proves the displayed physical-time survival asymptotic. The tail-integral formula \(\mathbb E[T^r]=r\int_0^\infty t^{r-1}\Pr(T>t)dt\) proves the sharp moment criterion: the integrand behaves, up to a positive constant, like \(t^{r-a-1}(\log t)^{b-1}\). At \(r=a\) the integral diverges because \(b\ge1\).

**4. Exact contrasting motifs.** On a path with a seeded endpoint and one-neighbor thresholds, only the successive next vertex is ever eligible, so \(U\) is a sum of \(m\) independent rate-one exponentials. Its exact physical-time survival function is

\[
 \Pr(T>t)=\left(\frac2{t+2}\right)^a\sum_{j=0}^{m-1}\frac{\bigl[a\log((t+2)/2)\bigr]^j}{j!}.
\]

For a star with seeded hub, all \(m\) susceptible leaves are eligible from the start and have independent time-changed rate-one exponential clocks. Hence

\[
 \Pr(T>t)=1-\left[1-\left(\frac2{t+2}\right)^a\right]^m.
\]

The path has \((b,A)=(m,1)\); the star has \((b,A)=(1,m)\). The contrast holds even though the two graphs have the same number of initially susceptible vertices and the same inverse-age hazard. This completes the proof.

## Verification

The provided standalone `verify.py` reconstructs deterministic closure and eligible transitions, computes \((b,A)\) by dynamic programming, and independently enumerates complete adoption orders for comparison with exact rational arithmetic. It also compares exact rational Laplace transforms and evaluates independent finite-chain uniformization probabilities for path/star motifs. All checks are finite sanity checks; the preceding algebraic argument proves the general statement.

On the checked execution: 408 graph/seed/threshold cases agreed on \((b,A)\); 816 rational Laplace comparisons passed; 17 extra uniformization state checks and 14 path/star checks passed. Run with `python verify.py` using Python's standard library.

## Relationship to prior work

Abella, San Miguel and Ramasco, *Aging in binary-state models: The Threshold model for Complex Contagion* (arXiv:2209.05990, first posted 2022-09-13), introduced inverse-age endogenous activation and studied cascade growth through numerical experiments and approximate compartment equations on random networks and lattices. Its explicit finite-size open direction motivates an exact finite-network analysis. The precise continuous-time hazard here is a separate model: it is **not** the paper's original random-asynchronous discrete update rule.

The generic phase-type representation of finite Markov-chain absorption times, including \(\boldsymbol\alpha e^{Qs}\mathbf1\), is classical and is not claimed as novel. The claimed contribution is the **positive eligible-order expansion and its sharp graph-theoretic bottleneck-depth/leading-coefficient rule**, including the uniform moment threshold and topology-dependent logarithmic correction under inverse-age activation. Richter, Henkel and Böttcher (arXiv:2006.05937) study aging and relaxation for a different, reversible, bistable contagion model; their finite-network claims do not imply the present progressively activated network law.

## Limitations

The theorem concerns finite graphs, progressive adoption, deterministic static integer thresholds, identical physical-time hazard \(a/(t+2)\), and a strictly nonempty eventual new-adopter set. It does not cover exogenous resets, heterogeneous aging clocks or per-site rates, discrete random-asynchronous update schedules, threshold changes, or stochastic initial graphs. Constants \(A,b\) can require exponentially many adoption states to compute; the theorem does not claim a polynomial-time general algorithm. Phase-type methods provide broad preexisting machinery, leaving a residual possibility of an equivalent combinatorial specialization in literature not identified by the searches. No independent audit has been performed.

## References

1. D. Abella, M. San Miguel, and J. J. Ramasco, *Aging in binary-state models: The Threshold model for Complex Contagion*, arXiv:2209.05990 (2022), https://arxiv.org/html/2209.05990v2 and https://arxiv.org/abs/2209.05990 (earliest posting 2022-09-13).
2. P. Richter, M. Henkel, and L. Böttcher, *Aging and equilibration in bistable contagion dynamics*, arXiv:2006.05937 (2020), https://arxiv.org/abs/2006.05937.
3. M. Bladt and B. F. Nielsen, *Matrix-Exponential Distributions in Applied Probability* (2017); phase-type background as described in https://www.stat.ethz.ch/CRAN/web/packages/PhaseTypeR/vignettes/PhaseTypeR.html.
4. *MSC2020*, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=91D30 (91D30: social networks; opinion dynamics).
