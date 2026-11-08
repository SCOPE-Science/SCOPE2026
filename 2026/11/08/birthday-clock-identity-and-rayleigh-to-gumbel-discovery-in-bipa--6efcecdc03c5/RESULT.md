# Birthday-clock identity and Rayleigh-to-Gumbel discovery in bipartite internal DLA

## Finding

Let \(K_{a,b}\) have labeled vertex classes \(A,B\), with \(a\ge2\), \(b\ge1\), and fix an initial occupied vertex \(o\in A\). In **sequential internal diffusion-limited aggregation (IDLA)**, each further particle starts at \(o\), performs an independent non-lazy simple random walk, and settles on its first previously unoccupied vertex. Let \(J_{a,b}\) be the number of vertices of \(B\) occupied at the moment the last vertex of \(A\) becomes occupied.

For every integer \(0\le j<b\), exactly

\[
\Pr(J_{a,b}\le j)=\sum_{k=0}^{a-1}(-1)^k\binom{a-1}{k}\prod_{r=0}^{j}\frac{b-r}{b-(1-k/a)r}.
\]

Also \(\Pr(J_{a,b}\le b)=1\). This is an exact finite-size law, not an asymptotic approximation.

For fixed \(a\ge2\) and \(b\to\infty\), the first-occupation levels in \(B\), divided by \(\sqrt b\), of all \(a-1\) non-root vertices of \(A\) converge jointly to **independent** nonnegative variables \(R_1,\ldots,R_{a-1}\) with

\[
\Pr(R_i>t)=e^{-t^2/(2a)}\quad(t\ge0).
\]

In particular,

\[
\Pr(J_{a,b}/\sqrt b\le t)\longrightarrow\left(1-e^{-t^2/(2a)}\right)^{a-1},
\qquad
\frac{\mathbb E J_{a,b}}{\sqrt b}\longrightarrow
\sqrt{\frac{\pi a}{2}}\sum_{k=1}^{a-1}(-1)^{k+1}\binom{a-1}{k}k^{-1/2}.
\]

The underlying rare-repeat approximation is quantitative. If \(j=\lfloor t\sqrt b\rfloor<b\) and \(N_v(j)\) counts the visits to \(v\in A\setminus\{o\}\) immediately following a repeated \(B\)-vertex draw before the \((j+1)\)-st new \(B\) vertex is discovered (including visits to already occupied \(v\)), then

\[
 d_{\mathrm{TV}}\!\left(\mathcal L((N_v(j))_v),\bigotimes_{v\in A\setminus\{o\}}\operatorname{Pois}\left(\frac{t^2}{2a}\right)\right)
 \le\frac{2}{b^2}\sum_{r=0}^j r^2+\frac{t}{2\sqrt b}+\frac1{8b}.
\]

There is also a growing-small-class crossover: if \(a=a_b\to\infty\) and \(a_b(\log a_b)^3=o(b)\), then for each real \(x\),

\[
\Pr\left(\frac{J_{a,b}^2}{2ab}-\log(a-1)\le x\right)
\longrightarrow\exp(-e^{-x}).
\]

## Assumptions and scope

All random-walk transitions select uniformly among the opposite class, independently at each step; they do not hold. Each settled particle is replaced by a fresh particle at \(o\). The class \(A\) is the class containing the initial occupied vertex. For the exact law, \(a\) and \(b\) are arbitrary positive integers with \(a\ge2\). The fixed-class limit holds only for fixed \(a\) and \(b\to\infty\). The growing-class Gumbel law assumes \(a\to\infty\) and \(a(\log a)^3/b\to0\). The count-vector bound is for a finite time \(t\) with \(\lfloor t\sqrt b\rfloor<b\); it does not claim total-variation convergence of the (discrete) scaled discovery times to a continuous law.

## Proof

**1. Exact two-stream representation.** Each time a moving particle is at a vertex of \(A\), its next \(B\) vertex is uniform on \(B\). If that vertex is new, the particle settles and the next particle starts at \(o\in A\). If the \(B\) vertex is occupied, the next step is uniform on \(A\), independently of the \(B\) choice. Whether that \(A\) step finds a new vertex (and starts a new particle at \(o\)) or an occupied vertex (and continues the same particle), the next step again chooses an independent uniform \(B\) vertex. Thus all successive \(B\) choices form an iid uniform stream; each repeat of a previously observed \(B\) label independently creates one iid uniform \(A\) choice. Each \(A\) vertex other than \(o\) becomes occupied exactly on the first occurrence of its label in this second stream.

**2. Exact CDF.** Before the \((r+1)\)-st distinct \(B\) label occurs, there are \(F_r\) repeated \(B\) draws after the \(r\)-th new label, for \(0\le r<b\). The \(F_r\) are independent geometric-failure counts with

\[
\Pr(F_r=m)=(1-r/b)(r/b)^m\quad(m\ge0),
\qquad \mathbb E z^{F_r}=\frac{b-r}{b-rz}.
\]

Let \(M_b(j)=\sum_{r=0}^jF_r\), for \(0\le j<b\). The event \(J_{a,b}\le j\) says precisely that all \(a-1\) non-root \(A\) labels appear among the first \(M_b(j)\) iid \(A\) draws: an \(A\) vertex may be discovered at level \(j\) before the \((j+1)\)-st new \(B\) label. Conditional inclusion-exclusion gives

\[
\Pr(J_{a,b}\le j\mid M_b(j)=m)
=\sum_{k=0}^{a-1}(-1)^k\binom{a-1}{k}(1-k/a)^m.
\]

Taking expectations and multiplying the independent geometric generating functions proves the exact formula. If all \(B\) vertices are already occupied, subsequent walks must eventually discover any remaining \(A\) vertex, so \(J_{a,b}\le b\) surely.

**3. Joint rare-repeat law and finite error.** For \(j=\lfloor t\sqrt b\rfloor<b\), write \(p_r=r/b\). The chance that any \(F_r\ge2\) is at most \(\sum_{r=0}^jp_r^2\); outside this event replace each \(F_r\) by its indicator \(I_r=\mathbf1\{F_r\ge1\}\), an independent \(\operatorname{Bernoulli}(p_r)\). Attach to each event an independent uniform \(A\)-label. The marked Bernoulli array can be coupled to independent marked Poisson variables of means \(p_r\) with error at most \(\sum_{r=0}^jp_r^2\) by the elementary Bernoulli--Poisson total-variation bound. Poisson splitting yields independent Poisson counts on each \(A\) label of mean \(\lambda_j/a\), where \(\lambda_j=j(j+1)/(2b)\). Since

\[
\left|\lambda_j-t^2/2\right|\le t/(2\sqrt b)+1/(8b),
\]

coupling Poisson variables with different total intensities and projecting off the root label gives the displayed total-variation inequality. The same rare-event coupling on finitely many disjoint intervals of the level variable \(r/\sqrt b\) proves convergence of the marked point process to a Poisson process of intensity \(s\,ds\) with uniform independent marks on \(A\). Hence the first-mark times of the non-root labels are independent with survival \(\exp(-t^2/(2a))\), yielding the joint and maximum limits.

**4. Expected discovery level.** The inclusion-exclusion expression and the inequality \((b-r)/(b-r+r/a)\le\exp[-r/(ab)]\) imply for \(j<b\)

\[
\Pr(J_{a,b}>j)\le(a-1)\exp[-j(j+1)/(2ab)].
\]

For fixed \(a\), this uniform sub-Gaussian envelope gives uniform integrability of \(J_{a,b}/\sqrt b\). Integrate the limiting maximum survival function, expand its finite binomial sum, and use \(\int_0^\infty e^{-kt^2/(2a)}dt=\sqrt{\pi a/(2k)}\) to obtain the displayed mean constant.

**5. Growing-class Gumbel law.** Let \(C_a\) be the coupon-collector number of iid uniform \(A\) labels required to see the \(a-1\) non-root labels; by the two-stream construction, \(C_a\) is independent of the \(F_r\) and

\[
\{J_{a,b}\le j\}=\{C_a\le M_b(j)\},\qquad 0\le j<b.
\]

The ordinary coupon-collector limit gives \(C_a/a-\log(a-1)\Rightarrow G\), where \(\Pr(G\le x)=\exp(-e^{-x})\). Set \(j=\lfloor\sqrt{2ab(\log(a-1)+x)}\rfloor\) for fixed real \(x\) and sufficiently large \(a\). The assumption implies \(j/b\to0\). The exact geometric moments give

\[
\mathbb EM_b(j)=\sum_{r=0}^j\frac r{b-r},
\qquad
\operatorname{Var}(M_b(j))=\sum_{r=0}^j\frac{rb}{(b-r)^2}.
\]

Expanding uniformly for \(r\le j=o(b)\),

\[
\frac{\mathbb EM_b(j)}a=\log(a-1)+x+o(1),
\quad
\frac{\operatorname{Var}(M_b(j))}{a^2}=O(\log a/a)=o(1).
\]

Indeed the mean's additional error is \(O(j^3/(ab^2)+j/(ab))=O(\sqrt{a/b}(\log a)^{3/2})+o(1)\), which vanishes by assumption. Chebyshev's inequality, independence, and continuity of the Gumbel CDF show \(\Pr(C_a\le M_b(j))\to\exp(-e^{-x})\). The floor and square-root transformation are equivalent to the displayed event for large \(a\). This proves the second limiting regime.

## Verification

The standalone standard-library script `verify.py` checks the exact inclusion-exclusion CDF against an independently derived rational-state recurrence for all \(2\le a\le8\), \(1\le b\le16\), and every \(0\le j\le b\). It also checks monotonicity, endpoint probabilities, geometric moments, and the finite tail envelope. The exact symbolic checks are finite corroboration; all infinite-limit statements follow from the analytic arguments above.

## Relationship to prior work

Rivera, Stauffer, Sauerwald and Sylvester (2018) define sequential finite-graph IDLA and study dispersion time, in particular for cliques, stars, paths, trees and expanders. Their full accessible preprint does not give this complete-bipartite, class-completion clock, exact CDF or Rayleigh-to-Gumbel transition. Mittelstaedt (2019) examines a different one-dimensional IDLA occupation law on \(\mathbb Z\). Classical coupon-collector limit theory, including Erdős--Rényi and the survey/theorems of Falgas-Ravry, Larsson and Markström (2016), supplies the distribution of \(C_a\) but not the exact geometric collision clock of sequential bipartite IDLA. Here the contribution is the coupling to that clock and its graph-specific exact and asymptotic consequences. Literature searches cannot establish historical priority or rule out differently named equivalent prior results.

## Limitations

The exact formula concerns class-\(A\) completion, not the maximum particle walk length, parallel-IDLA, or global completion time. The fixed-\(a\) and growing-\(a\) theorems have distinct assumptions. The growing-class statement is not claimed at arbitrary ratios \(a/b\), and no universal threshold outside its stated regime is asserted. Independent mathematical validation and comprehensive historical-priority certification have not been performed.

## References

- N. Rivera, A. Stauffer, T. Sauerwald and J. Sylvester, *The Dispersion Time of Random Walks on Finite Graphs*, arXiv:1808.09219, initial public version 2018-08-28, https://arxiv.org/abs/1808.09219.
- K. Mittelstaedt, *A Stochastic Approach to Eulerian Numbers*, arXiv:1902.03195, initial public version 2019-02-08, https://arxiv.org/abs/1902.03195.
- V. Falgas-Ravry, J. Larsson and K. Markström, *Speed and concentration of the covering time for structured coupon collectors*, arXiv:1601.04455, initial public version 2016-01-18, https://arxiv.org/abs/1601.04455.
