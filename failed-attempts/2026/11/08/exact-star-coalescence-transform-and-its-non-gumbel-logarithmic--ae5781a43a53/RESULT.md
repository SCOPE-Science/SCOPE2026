# Exact star-coalescence transform and its non-Gumbel logarithmic limit

## Finding
Let \(S_b=K_{1,b}\), with \(b\ge1\), and start one particle at every vertex. Every surviving particle performs an independent continuous-time simple random walk, jumping at rate one to a uniformly chosen neighbor. Particles merge immediately upon occupying the same vertex, and the merged particle continues with rate one. Let \(T_b\) be the time until only one particle remains.

**Exact finite law.** For every real \(s\ge0\), with the empty product interpreted as one,
\[
\mathbb E[e^{-sT_b}]
=\frac{(b+1)(s+2)}{b(s+2)^2-2(b-1)}
\prod_{j=2}^{b}
\frac{j(j+1+s)((b+1)j+bs)}{(j+s)\{b(j+1+s)^2-(b-j)(j+1)\}}.
\]
In particular, writing \(H_b=\sum_{j=1}^b 1/j\),
\[
\mathbb E[T_b]=\frac{b}{b+1}H_b+\frac{b-1}{b+1}.
\]

**Limit law.** As \(b\to\infty\), \(T_b-\log b\) converges weakly to a nondegenerate real-valued random variable \(Y\). For \(|s|<1/16\),
\[
\mathbb E[e^{-sY}]=\frac{\Gamma(1+\alpha_+(s))\Gamma(1+\alpha_-(s))}{\Gamma(2+s)},\qquad
\alpha_\pm(s)=\frac{1+2s\pm\sqrt{1-4s}}2.
\]
Its mean and variance are
\[
\mathbb E[Y]=1+\gamma,\qquad \operatorname{Var}(Y)=\frac{\pi^2}{2}-1,
\]
where \(\gamma\) is the Euler--Mascheroni constant. In particular, the centered limit is not a unit-scale Gumbel law, whose variance is \(\pi^2/6\).

## Assumptions and scope
The graph is the simple star with one central vertex and \(b\) distinct leaves; no self-loops are present. The rate-one clocks belong to particles, not edges, and a merger yields one rate-one particle (no inherited acceleration). All \(b+1\) vertices are initially occupied, and there is no particle immigration or branching. The finite transform holds for each integer \(b\ge1\) and every \(s\ge0\). The centered limiting transform is asserted only in a neighborhood of zero; no global transform extension is needed for the weak-convergence claim.

## Proof
Write \(f_j(s)\) for the transform of the remaining coalescence time from a state with the hub occupied and exactly \(j\) occupied leaves, and \(g_j(s)\) for the state with the hub empty and \(j\) occupied leaves. By permutation symmetry, these are complete Markov states. The absorbing states are \(f_0(s)=g_1(s)=1\). If the hub is empty and \(j\ge2\), the first of the \(j\) leaf particles jumps to the hub at total rate \(j\), giving
\[
g_j(s)=\frac{j}{j+s}f_{j-1}(s).
\]
If the hub is occupied, its own rate-one jump hits an occupied leaf with probability \(j/b\), or an empty leaf with probability \((b-j)/b\). Each of the \(j\) leaf particles jumps to the occupied hub at rate one and merges. Consequently, for \(1\le j\le b\),
\[
(j+1+s)f_j(s)=j f_{j-1}(s)+\frac jb g_j(s)+\frac{b-j}{b}g_{j+1}(s).
\]
Here \(g_1=1\) for the \(j=1\) equation, rather than the formula for \(j\ge2\). Substituting \(g_2=2f_1/(2+s)\) gives the exact initial value
\[
f_1(s)=\frac{(b+1)(s+2)}{b(s+2)^2-2(b-1)}.
\]
For every \(2\le j\le b\), substitution of the empty-hub equation yields
\[
\frac{f_j(s)}{f_{j-1}(s)}=
\frac{j(j+1+s)((b+1)j+bs)}{(j+s)\{b(j+1+s)^2-(b-j)(j+1)\}},
\]
proving the product transform because the initially full state has transform \(f_b\). These equations remain valid for \(|s|<1/16\) as moment-generating identities: their denominators are strictly positive and the finite-state hitting time has the corresponding exponential moment (equivalently, the same first-step system is a positive transient resolvent).

To evaluate the limit, set
\[
\theta_b=\frac{bs}{b+1},\quad
\alpha_b+\beta_b=1+2\theta_b,\quad
\alpha_b\beta_b=\theta_b(s+2).
\]
For real \(s\) sufficiently close to zero, label the two real roots continuously with \(\alpha_b(0)=1\) and \(\beta_b(0)=0\). Factoring the quadratic in each denominator, telescoping the product by gamma functions, and simplifying the initial factor yields the **exact identity**
\[
\mathbb E[e^{-sT_b}]
=(b+1+s)\frac{\Gamma(b+1)\Gamma(b+1+\theta_b)\Gamma(1+\alpha_b)\Gamma(1+\beta_b)}{\Gamma(2+\theta_b)\Gamma(b+1+\alpha_b)\Gamma(b+1+\beta_b)}.
\]
The identity initially follows near zero and hence also represents the original finite transform for every nonnegative real \(s\) by analytic continuation along the nonnegative real axis (or directly by the rational product). Uniform gamma-ratio asymptotics on a fixed small neighborhood of zero give
\[
\mathbb E[e^{-sT_b}]
=b^{-\theta_b}\left(
\frac{\Gamma(1+\alpha_b)\Gamma(1+\beta_b)}{\Gamma(2+\theta_b)}+o(1)\right).
\]
Since \(\theta_b\to s\), \((s-\theta_b)\log b\to0\), and \(\alpha_b,\beta_b\to\alpha_+(s),\alpha_-(s)\), respectively, the centered transforms converge to the displayed limit uniformly on a neighborhood of zero. Exponential moment bounds on both sides of zero imply tightness; the limiting analytic moment-generating function determines every subsequential limit. This proves weak convergence.

For completeness, if \(t_j\) is the mean remaining time with an occupied hub and \(j\) occupied leaves, the differentiated first-step equations yield \(t_1=(3b-1)/(2(b+1))\) and, for \(2\le j\le b\), \(t_j-t_{j-1}=(bj+2b+1)/(j(b+1)(j+1))\). These differences telescope to the displayed exact harmonic mean. Differentiating the limiting logarithmic transform at zero gives its first cumulant \(1+\gamma\) and its second cumulant \(\pi^2/2-1\). Uniform convergence on a complex neighborhood (or a smaller real exponential-moment neighborhood) justifies differentiating the limit. This also distinguishes the limit from the unit-scale Gumbel distribution.

## Verification
A standalone standard-library Python checker, `verify.py`, independently constructs the absorbing generator on all symmetry-reduced occupancy states, solves rational linear systems for Laplace transforms at several positive rational arguments, and compares them with the closed product. It also solves the mean hitting-time equations independently and checks the harmonic identity. Run `python3 verify.py`. The analytic gamma-limit step is proved above and is not inferred from finite numerical tests.

## Relationship to prior work
Ben-Ari, Panzo, Speegle and VandenBerg study quasi-stationary distributions for the voter model on unbalanced complete bipartite graphs and develop a discrete-time coalescing-walk duality. Their principal result is a Sibuya quasi-stationary law, rather than an exact continuous-time full-coalescence transform or the centered law here. Kanade, Mallmann-Trenn and Sauerwald give \(\Theta(\log b)\) full-coalescence bounds on stars for synchronous discrete-time coalescing walks, but not the rate-one asynchronous law here. Pickering and Lim analyze the two-opinion voter model spectrally, using approximation for complete bipartite graphs, which does not assert this distinct-opinion continuous-time full-coalescence law. Kátai-Urbán, Pongrácz and Szabó consider different discordant voting protocols on stars. Their time scales and update rules do not imply this law. These comparisons do not certify global historical novelty.

## Limitations
The result concerns asynchronous continuous-time rate-one particle walks. It does not apply to synchronous updates, edge-clock dynamics, ordinary two-opinion consensus initialized at arbitrary binary configurations, or growing hub classes. The bound \(|s|<1/16\) is a sufficient neighborhood rather than a claimed sharp transform domain. No independent audit or exhaustive literature-priority verification has been performed.

## References
- I. Ben-Ari, H. Panzo, P. Speegle and R. O. VandenBerg, *Quasi-Stationary Distributions for the Voter Model on Complete Bipartite Graphs*, arXiv:2004.10187, first submitted 2020-04-21, https://arxiv.org/abs/2004.10187.
- V. Kanade, F. Mallmann-Trenn and T. Sauerwald, *On coalescence time in graphs: When is coalescing as fast as meeting?*, arXiv:1611.02460, first submitted 2016-11-08, https://arxiv.org/abs/1611.02460, Appendix C.7.
- W. Pickering and C. Lim, *Solution of the Voter Model by Spectral Analysis*, arXiv:1408.2130, first submitted 2014-08-09, https://arxiv.org/abs/1408.2130, Section V.
- K. Kátai-Urbán, A. Pongrácz and C. Szabó, *Voting protocols on the star graph*, Acta Sci. Math. 90 (2024), 41--51, https://doi.org/10.1007/s44146-024-00125-x.
