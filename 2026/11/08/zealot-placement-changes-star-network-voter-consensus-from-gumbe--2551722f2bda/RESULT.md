# Zealot placement changes star-network voter consensus from Gumbel to exponential

## Finding

**Theorem.** For each integer \(n\ge1\), let \(G_n=K_{1,n+1}\) be a star with center \(o\) and \(n+1\) leaves. Run the continuous-time, node-update binary voter model: each non-fixed vertex updates at rate one, copying a uniformly chosen neighbor; one permanently fixed vertex is opinion \(+\), and all other vertices are initially opinion \(-\). Let \(T_n^{\mathrm{hub}}\) and \(T_n^{\mathrm{leaf}}\) be the first times at which every vertex is \(+\), with the fixed vertex placed at the center or a leaf, respectively. Then

\[
\Pr\{T_n^{\mathrm{hub}}\le t\}=(1-e^{-t})^{n+1}\quad(t\ge0),\qquad
\mathbb E T_n^{\mathrm{hub}}=H_{n+1}=\sum_{j=1}^{n+1}\frac1j,
\]
\[
T_n^{\mathrm{hub}}-\log(n+1)\;\xrightarrow{\ d\ }\;G,
\qquad \Pr\{G\le x\}=e^{-e^{-x}},
\]
whereas
\[
\frac{T_n^{\mathrm{leaf}}}{n}\;\xrightarrow{\ d\ }\;X,
\qquad \Pr\{X>t\}=e^{-t/2}\quad(t\ge0),
\qquad \mathbb E T_n^{\mathrm{leaf}}=2n+O(\log n).
\]
Thus changing only the location of the single fixed opinion changes consensus time from logarithmic/Gumbel to linear/exponential scaling, with an explicit asymptotic mean constant.

## Assumptions and scope

The graph is simple and undirected, with exactly \(n+2\) vertices and \(n+1\) edges. Clocks run in continuous physical time, independently at *rate one per non-zealot vertex*; a clock ring may leave the spin unchanged. The single fixed vertex never updates. Each ordinary vertex is initially \(-\). The result concerns the first all-\(+\) state, which is absorbing. All asymptotics are as integer \(n\to\infty\). These time constants do not apply without conversion to edge-selection or globally normalized updates.

## Proof

**Hub fixed.** Every leaf copies the fixed positive hub at its first rate-one update and never becomes negative afterward. The \(n+1\) independent first update times are exponential with rate one; their maximum is \(T_n^{\mathrm{hub}}\). Multiplying their distribution functions gives the displayed exact CDF. Integrating its tail gives \(H_{n+1}\). Replacing \(t\) by \(\log(n+1)+x\) yields the stated Gumbel weak limit.

**Leaf fixed: finite-state reduction.** Choose one leaf as the permanently positive zealot. Let \(h\in\{0,1\}\) encode the center's opinion, and let \(k\in\{0,\ldots,n\}\) count positive *ordinary* leaves. The complete jump rates between distinct states are
\[
\begin{array}{c|cc}
 h=0 &(0,k)\to(0,k-1):k &(0,k)\to(1,k):(k+1)/(n+1)\\
 h=1 &(1,k)\to(1,k+1):n-k &(1,k)\to(0,k):(n-k)/(n+1).
\end{array}
\]
Unlisted transitions have zero rate. The starting state is \(F=(0,0)\); the absorbing target is \(S=(1,n)\). From \(F\), the only state-changing event is a positive center flip with rate \(1/(n+1)\), taking the process to \((1,0)\). The ensuing excursion ends upon first reaching \(F\) or \(S\). Denote its duration by \(E_n\), its probability of success by \(q_n\), and its occupation time with a negative center by \(B_n=\int_0^{E_n}\mathbf1_{\{h(s)=0\}}\,ds\).

**Uniform excursion-length control.** During a spell with hub state \(h=1\), if \(m\) ordinary leaves disagree with the hub, then their total correcting rate is \(m\) and the hub's contrary-flip rate is \(m/(n+1)\). The conditional probability that all \(m\) leaves correct before a hub flip is \(((n+1)/(n+2))^m\ge e^{-1}\). During a spell with \(h=0\), beginning with \(k\ge1\) positive ordinary leaves, their correcting rate is \(k\) and the hub-flip rate is \((k+1)/(n+1)\); the probability of reaching \(F\) without flipping the hub is at least \(((n+1)/(n+3))^k\ge e^{-2}\). Once no disagreeing leaves remain, the spell ends at \(F\) or \(S\). Each spell has expected duration at most \(H_n\) by comparison with the sequential correction times of \(n\) independent rate-one clocks, and its conditional probability of ending the whole excursion is at least \(e^{-2}\). Therefore
\[
\mathbb E E_n\le e^2H_n,
\qquad0\le \mathbb E B_n\le e^2H_n.
\]
This finite bound also justifies stopping the following martingale.

**Excursion success probability.** Define the degree-weighted magnetization
\[
M(h,k)=\frac{h}{2}+\frac{k+1}{2(n+1)}.
\]
A direct substitution of the above rates into the Markov generator \(\mathcal L\) gives
\[
(\mathcal L M)(h,k)=\frac{1-h}{2(n+1)}.
\]
At the excursion start, \(M(1,0)=(n+2)/(2(n+1))\), at failure \(M(F)=1/(2(n+1))\), and at success \(M(S)=1\). Dynkin's identity up to \(E_n\) gives the exact relation
\[
(2n+1)q_n=n+1+\mathbb E B_n.
\]
Consequently
\[
q_n=\frac12+O\!\left(\frac{\log n}{n}\right),
\qquad q_n\longrightarrow\frac12.
\]

**Renewal and weak limit.** Each return to \(F\) restarts the process. There are geometrically many excursions until success, with independent and identically distributed experiment outcomes and success probability \(q_n\). Before each excursion a fresh holding time \(W_n\sim\mathrm{Exp}(1/(n+1))\) occurs at \(F\); all such holding times are independent of all excursion outcomes. The sum of the holding times until the successful attempt is therefore exactly exponential with rate \(q_n/(n+1)\), including the case of a first-attempt success. The sum of all excursion durations has expectation \(\mathbb E E_n/q_n=O(\log n)\) by the renewal-reward identity, so its quotient by \(n\) converges to zero in probability. Since \(nq_n/(n+1)\to1/2\), the scaled total passage time converges to an exponential random variable of rate \(1/2\). The exact renewal mean is
\[
\mathbb E T_n^{\mathrm{leaf}}=\frac{(n+1)+\mathbb E E_n}{q_n}
=2n+O(\log n).
\]
This completes the proof for every \(n\ge1\).

## Verification

Run the included independent finite-state checker via `python3 verify.py`. It enumerates the full binary-spin continuous-time generator separately from the two-coordinate reduction and solves rational hitting-time and excursion equations. For \(n=1,\ldots,5\), all full-state and reduced-state exact mean values agree, the stopped-martingale identity holds as rational equality, and the excursion bounds hold; additional checks inspect no-flip inequalities for larger \(n\). This is a finite computational cross-check, **not** an infinite proof. The proof of the weak limits and the time-scale separation is the analytic argument above.

## Relationship to prior work

The general voter model, fixed or biased opinion agents, and random-walk/magnetization methods are well established. Mobilia's [1] single-zealot study focuses on Euclidean lattices and local magnetization rather than fixed-vertex placement and first-passage distribution on stars. Mobilia, Petersen and Redner [2] study competing populations of zealots. Iwamasa and Masuda [3] study consensus times on different graphs *without* fixed zealots. Moreira and coauthors [4] investigate star-network binary dynamics driven by *external opinion-maker nodes* connected to voters and characterize stationary distributions and transitions, not the one-internal-fixed-leaf absorption observable. Recent star voting protocols [5] use discordant push/pull updates and no permanently fixed source. Fudolig and Esguerra [6] analyze one-opinion zealots on a *complete graph*, a different topology for the fixation observable. The elementary rate reduction and martingale are tools, not claimed innovations. The statement claimed here is the joint, position-sensitive Gumbel/exponential asymptotic dichotomy with the coefficient \(2\) in the fixed-leaf scaling.

## Limitations

Priority could be affected by unindexed equivalent analyses or by an implicit special case of general finite-graph voter duality. The full text of [4] could not be systematically opened at one source during literature checking, although substantial author-uploaded text describing its model and conclusions was inspected; it is a residual originality risk. The claim does not cover arbitrary initial densities, multiple zealots, other graph families, or alternative clock normalizations. Finite checks provide no independent mathematical audit of the asymptotic proof.

## References

[1] M. Mobilia, *Does a Single Zealot Affect an Infinite Group of Voters?*, arXiv:cond-mat/0304670 (first public version 2003-04-30), https://arxiv.org/abs/cond-mat/0304670.

[2] M. Mobilia, A. Petersen and S. Redner, *On the Role of Zealotry in the Voter Model*, arXiv:0706.2892 (2007), https://arxiv.org/abs/0706.2892.

[3] Y. Iwamasa and N. Masuda, *Networks Maximizing the Consensus Time of Voter Models*, arXiv:1404.6360 (first public version 2014-04-25), https://arxiv.org/abs/1404.6360.

[4] C. A. Moreira, D. M. Schneider and M. A. M. de Aguiar, *Binary Dynamics on Star Networks under External Perturbations*, arXiv:1504.03638 (first public version 2015-04-14), https://arxiv.org/abs/1504.03638.

[5] *Voting Protocols on the Star Graph*, Acta Scientiarum Mathematicarum (2024), https://doi.org/10.1007/s44146-024-00125-x.

[6] M. I. D. Fudolig and J. P. H. Esguerra, *Analytic Treatment of Consensus Achievement in the Single-Type Zealotry Voter Model*, Physica A 413 (2014), https://doi.org/10.1016/j.physa.2014.07.033.
