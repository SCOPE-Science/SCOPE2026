# A graph-period dichotomy for rare-quality monopoly selection in stochastic popularity networks

## Finding
For the two-channel stochastic user-engagement process of Ravazzi, Frasca and Cocca, make each channel's strictly positive baseline quality weak by the same factor \(\varepsilon\), with fixed qualities \(q_1,q_2\in(0,1)\). Let \(\nu_\varepsilon\) be its unique stationary law and \(m_i\) the state where every user engages only with channel \(i\). The two monopoly weights tend to \(p_1\) and \(1-p_1\), with
\[
p_1=\frac{Aq_1+B(1-q_2)}{A(q_1+q_2)+B(2-q_1-q_2)},\qquad A>0,\quad B\ge0.
\]
The coefficients \(A,B\) are fully determined by the zero-quality absorption problem, the network and user sensitivities, and not by the positive quality parameters. **The sharp graph dichotomy is that \(B=0\) exactly when the irreducible contact matrix has period greater than one.** Thus \(p_1=q_1/(q_1+q_2)\) for every periodic contact matrix (in particular every connected undirected bipartite graph). For primitive contact matrices \(B>0\), and
\[
p_1-\frac{q_1}{q_1+q_2}
=\frac{B(q_1-q_2)(q_1+q_2-1)}{(q_1+q_2)[A(q_1+q_2)+B(2-q_1-q_2)]}.
\]
Therefore, among unequal qualities, a primitive graph amplifies the higher-quality monopoly when their sum exceeds one and attenuates it when the sum is below one. At sum one or equal qualities the proportional law holds regardless of period.

## Assumptions and scope
Fix an integer \(n\ge2\), a strongly connected row-stochastic matrix \(P\in[0,1]^{n\times n}\), and for each user \(v\) numbers \(a_v,b_v,g_v>0\) with \(a_v+b_v=1\). Self-loops are allowed. Take fixed \(q_1,q_2\in(0,1)\). Each state \(z\) has binary engagements \(z_{v,i}\in\{0,1\}\), with independent Bernoulli updating across all users and channels conditional on the current state. Put
\[
S_i(z)=\sum_vz_{v,i},\quad \Pi_i(z)=\begin{cases}S_i(z)/(S_1(z)+S_2(z)),&S_1(z)+S_2(z)>0,\\1/2,&S_1(z)+S_2(z)=0.\end{cases}
\]
At strength \(0\le\varepsilon<1/\max_vg_v\), define the next-step engagement probabilities as
\[
\theta_{v,i}^{(\varepsilon)}(z)=
(1-\varepsilon g_v)\left(a_v\sum_wP_{vw}z_{w,i}+b_v\Pi_i(z)\right)
+\varepsilon g_vq_i.
\]
This is the cited model with social-vs-platform weights reduced proportionally and quality coefficient \(\varepsilon g_v\). It permits simultaneous engagement with both channels. Positive \(\varepsilon\) gives all individual Bernoulli outcomes positive probability and hence a unique strictly positive stationary distribution.

At \(\varepsilon=0\), the two states \(m_1=(1,0)^n\) and \(m_2=(0,1)^n\) are absorbing. Under the positive assumptions above, the remaining states are transient and the chain is absorbed at one of the two monopolies almost surely (the zero-quality absorption result in the motivating paper). Write \(h_2(z)=\Pr_0(Z\text{ is eventually absorbed at }m_2\mid Z_0=z)\). Let \(m_1^{+v,2}\) be \(m_1\) with user \(v\) additionally engaging channel two, and let \(m_1^{-v,1}\) be \(m_1\) with user \(v\) ceasing channel-one engagement. Define
\[
A=\sum_{v=1}^ng_vh_2(m_1^{+v,2}),\qquad
B=\sum_{v=1}^ng_vh_2(m_1^{-v,1}).
\]
All statements concern finite, fixed \(n\) and the \(\varepsilon\downarrow0\) limit, with no claim of uniformity as population size grows.

## Proof
**1. First-order exits from monopoly.** At \(m_1\), the chance that user \(v\)'s channel-one engagement is absent next step is \(\varepsilon g_v(1-q_1)\), while their channel-two engagement appears with probability \(\varepsilon g_vq_2\). Cross-user and cross-channel outcomes are conditionally independent. Every event with at least two departures from the exact monopoly is \(O(\varepsilon^2)\). Thus the effective first-order rate for going from \(m_1\) to the basin of \(m_2\) is
\[
k_{12}=Aq_2+B(1-q_1).
\]
Relabeling the otherwise identical channels gives \(k_{21}=Aq_1+B(1-q_2)\). For each \(v\), the state \(m_1^{+v,2}\) has a strictly positive one-step chance of becoming \(m_2\), because platform fractions for both channels lie strictly between zero and one, all \(a_v,b_v\) are positive and \(P\) is stochastic. Consequently \(A>0\), hence both rates are positive.

**2. Perturbed-chain reduction.** Order the states into the two absorbing points and the finite transient set. For the zero-strength transition matrix, the transient block \(Q_0\) has spectral radius below one, so its fundamental matrix \((I-Q_0)^{-1}\) is finite. At small strength the stationary mass on the transient set is \(O(\varepsilon)\), as follows from the transient balance equation and bounded resolvent. Eliminating it from the two monopoly-balance equations gives first-order inter-monopoly rates \(\varepsilon k_{12}+O(\varepsilon^2)\) and \(\varepsilon k_{21}+O(\varepsilon^2)\): each single perturbed departure is followed, to leading order, by zero-quality absorption. Therefore
\[
\lim_{\varepsilon\downarrow0}\nu_\varepsilon(m_1)
=\frac{k_{21}}{k_{12}+k_{21}}=p_1,
\quad \lim_{\varepsilon\downarrow0}\nu_\varepsilon(m_2)=1-p_1,
\quad \nu_\varepsilon(\text{other states})=O(\varepsilon).
\]
No ordering of the two qualities is required.

**3. Graph period detects a one-channel blackout.** In a zero-quality trajectory begun at \(m_1^{-v,1}\), channel two stays absent until (and unless) every channel-one engagement vanishes simultaneously. Prior to that event, the channel-one platform share equals one. If \(Z_t\) is the set of users not engaging channel one, then a user \(u\) can belong to \(Z_{t+1}\) only if some \(w\in Z_t\) has \(P_{uw}>0\). Conversely every such next-step zero has strictly positive conditional probability because \(a_u>0\) and some positive-weight neighbor is absent; all desired zeros and ones can be selected simultaneously with positive probability. Thus zero-set propagation is contained in the Boolean images of \(Z_t\), and equality to each successive Boolean image is a positive-probability event.

If \(P\) is irreducible of period \(d>1\), its cyclic decomposition places the successive Boolean images of a singleton in one cyclic class at a time. As \(d>1\), no such image contains every vertex. Therefore a total blackout is impossible, so the absent channel cannot appear and \(h_2(m_1^{-v,1})=0\) for every \(v\), yielding \(B=0\).

If \(P\) is primitive, some common integer \(t\) makes every entry of \(P^t\) strictly positive. Starting with the singleton zero at \(v\), there is positive probability of choosing precisely the full Boolean image of the zero set at every step. At time \(t\), all users are disengaged from channel one and from channel two. The model's empty-state convention gives both channels platform share \(1/2\), so the all-zero state has a strictly positive one-step chance of becoming \(m_2\). Hence \(h_2(m_1^{-v,1})>0\) for every \(v\) and \(B>0\).

**4. Quality interaction.** Substitution of the two effective rates yields the displayed expression for \(p_1\). Subtraction of \(q_1/(q_1+q_2)\) gives the displayed sign identity by direct algebra. A connected undirected loopless graph has irreducible random-walk period two precisely when it is bipartite; an odd cycle makes the walk primitive. These give the stated network classification.

## Verification
A reproducible complete-state calculation is provided in `verify.py`. For the three-user path, it gives \(B=0\) and limiting \(p_1=4/7\) at \((q_1,q_2)=(4/5,3/5)\) with equal social/platform weights. For the three-user triangle, \(A\approx0.5896947483867315\), \(B\approx0.00638297872340425\), and \(p_1\approx0.571868335801036>4/7\). At \(\varepsilon=10^{-5}\), the triangle's full 64-state stationary calculation gives monopoly-one mass approximately \(0.571819515244091\) and total nonmonopoly mass approximately \(0.000113217711641\). These finite checks corroborate but do not replace the general proof.

## Relationship to prior work
Ravazzi, Frasca and Cocca establish almost-sure monopoly absorption at zero quality and stationary concentration near monopoly states at small positive quality; their statements do not specify the relative stationary weights of the two competing monopolies. The present result computes those weights from zero-quality absorption and identifies their sharp graph-period boundary. Finite-state absorbing-chain perturbation, Perron–Frobenius periodicity, and the gambler's-ruin style absorption construction are standard methods and are not claimed as original. The graph-period/blackout mechanism and the quality-sum sign criterion are the specific contributions.

## Limitations
This is a first-order small-quality result for finite, strongly connected contact networks and strictly positive social and platform sensitivities. It does not provide explicit \(A,B\) for arbitrary graphs without solving finite absorption equations; no universal rate in network size is claimed. Changing the empty-state platform-share convention, allowing zero platform sensitivity, or coupling rather than independently updating engagement indicators may change the theorem. The result is a mathematical statement about the specified stochastic model, not a prediction from empirical social-media data. Historical completeness of the literature comparison is not independently certified.

## References
1. C. Ravazzi, P. Frasca, G. Cocca, *Ergodic and Metastable Behavior of Stochastic Popularity Dynamics in Social Networks*, arXiv:2610.20021 (first released October 14, 2026), https://arxiv.org/abs/2610.20021 .
2. C. Ravazzi, P. Frasca, G. Cocca, *A Coupled Friedkin-Johnsen Model of Popularity Dynamics in Social Media*, arXiv:2503.15170 (2025), https://arxiv.org/abs/2503.15170 .
3. C. Ravazzi, P. Frasca, G. Cocca, *Dominance or Fair Play? Exploring Two-Channel Competition*, arXiv:2507.03448 (2025), https://arxiv.org/abs/2507.03448 .
