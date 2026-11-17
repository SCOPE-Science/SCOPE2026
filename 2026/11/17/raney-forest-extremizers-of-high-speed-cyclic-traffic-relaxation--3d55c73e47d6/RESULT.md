# Raney-forest extremizers of high-speed cyclic traffic relaxation

## Finding

Consider the deterministic high-speed one-lane cellular automaton with speed cap \(v\ge2\) on an indexed cyclic road of \(n\) cells containing \(m\ge2\) indistinguishable cars, in the low-density domain \(n\ge(v+1)m\). At each parallel update a car advances by the lesser of \(v\) and the number of empty cells immediately in front of it. Let \(T(x)\) be the least nonnegative time at which every car has at least \(v\) empty cells ahead (and consequently all later updates translate the cars by \(v\)).

**Theorem.** For every integer \(v\ge2\), \(m\ge2\), and \(n\ge(v+1)m\),
\[
\max_x T(x)=m-1,\qquad
\#\{x:T(x)=m-1\}=\frac{n}{m}\binom{(v+1)m-2}{m-1}.
\]
Here the count is over indexed binary ring configurations with precisely \(m\) cars, not cyclic necklaces. The extremizers admit a unique distinguished last-delayed car and are counted by ordered forests of \(v\) full \((v+1)\)-ary trees with a total of \(m-1\) internal vertices.

If \(n=(v+1)m+h\), with \(v\ge2\) and \(h\ge0\) fixed while \(m\to\infty\), the probability for a uniformly chosen indexed \(m\)-car configuration to have maximal relaxation time satisfies
\[
\frac{\frac{n}{m}\binom{(v+1)m-2}{m-1}}{\binom{n}{m}}
\longrightarrow \left(\frac{v}{v+1}\right)^{h+1}.
\]
Thus the sharpest delay retains positive probability in each fixed-surplus critical window, with an explicit speed-dependent limit.

## Assumptions and scope

The sites of the road are labelled \(0,\ldots,n-1\) modulo \(n\). All cars update *simultaneously* with no stochastic braking. In the Fukui–Ishibashi deterministic rule, the rightward displacement is \(\min(v,g)\) if the current forward gap is \(g\). The low-density condition ensures \(n-m\ge vm\), but no assumption is made about how the vacancies are initially distributed. Once all gaps are at least \(v\), parallel translation preserves them, so the definition of \(T\) is unambiguous. The theorem excludes the different speed-one automaton, for which a related Catalan statement was established previously.

## Proof

**1. A global min-plus formula.** Index cars by their cyclic order and lift their occupied positions to integers \(p_i(t)\), extended by \(p_{i+m}(t)=p_i(t)+n\). No overtaking occurs. A parallel update gives exactly
\[
p_i(t+1)=\min\{p_i(t)+v,\ p_{i+1}(t)-1\}.
\]
Inducting on \(t\), including the base case \(t=0\), yields
\[
p_i(t)=vt+\min_{0\le j\le t}\{p_{i+j}(0)-(v+1)j\}.
\]
Indeed, the two terms of the update respectively retain the old minimum and introduce the new endpoint \(j=t+1\). For fixed \(i\), the terms \(A_i(j)=p_{i+j}(0)-(v+1)j\) satisfy
\[
A_i(j+m)=A_i(j)+n-(v+1)m\ge A_i(j).
\]
Hence a global minimum occurs among \(0\le j\le m-1\), and after \(m-1\) steps every car moves at speed \(v\). Consequently \(T(x)\le m-1\).

**2. The strict-new-minimum test.** Define the cyclic initial gaps \(g_i=p_{i+1}(0)-p_i(0)-1\) and increments \(w_i=g_i-v\), so \(w_i\ge-v\) and \(\sum_{i=0}^{m-1}w_i=n-(v+1)m\ge0\). For a fixed car \(i\), the update at time \(m-2\) is slower than \(v\) exactly when \(A_i(m-1)\) is strictly smaller than all the preceding \(A_i(0),\ldots,A_i(m-2)\). Because \(A_i(j+1)-A_i(j)=w_{i+j}\), this is equivalent to
\[
\sum_{r=j}^{m-2}w_{i+r}<0\quad\text{for each }0\le j\le m-2.
\]
Reverse these \(m-1\) gaps and denote them by \(u_1,\ldots,u_{m-1}\). The condition is exactly
\[
u_j\ge0,\qquad \sum_{j=1}^{k}u_j\le vk-1\quad(1\le k\le m-1).
\]
A state has \(T(x)=m-1\) if and only if at least one car passes this test.

**3. Uniqueness of the last-delayed car.** Suppose cars \(i\) and \(i+s\), \(1\le s\le m-1\), both pass the strict-new-minimum test. The test for the first car makes the consecutive increment sum from \(i+s-1\) to \(i+m-2\) strictly negative. The test for the second car makes the complementary increment sum from \(i+m-1\) cyclically through \(i+s-2\) strictly negative. These disjoint arcs partition all \(m\) increments, so their total would be negative, contradicting \(\sum_i w_i\ge0\). Thus there is exactly one last-delayed car in every extremizer.

**4. The forest bijection and exact count.** A full ordered \((v+1)\)-ary rooted tree is a plane rooted tree in which each internal vertex has \(v+1\) ordered children and all other vertices are leaves. Form a forest with exactly \(v\) ordered roots, and encode its vertices by a depth-first preorder of the \(m-1\) internal vertices. Let \(u_j\) be the number of leaves processed immediately before internal vertex \(j\), with the remaining leaves processed after the last internal vertex. Before the \(j\)-th internal vertex one must have at least one available slot: the number of slots is \(vj-\sum_{r=1}^j u_r\), so the feasibility condition is precisely \(\sum_{r=1}^j u_r\le vj-1\). Conversely every such finite sequence describes a unique ordered forest after the final available slots are filled by leaves.

Let \(H(z)\) be the formal generating function of full ordered \((v+1)\)-ary rooted trees by number of internal vertices. It satisfies \(H=1+zH^{v+1}\), so the forest count is \([z^{m-1}]H(z)^v\). Lagrange inversion, with \(H=1+U\) and \(U=z(1+U)^{v+1}\), gives
\[
[z^{m-1}]H(z)^v
=\frac{v}{m-1}[u^{m-2}](1+u)^{(v+1)(m-1)+v-1}
=\frac1m\binom{(v+1)m-2}{m-1}.
\]
For \(m\ge2\) the displayed coefficient calculation is valid directly. The omitted closing gap is uniquely forced by the total vacancy count:
\[
g_{i+m-1}=n-m-\sum_{j=1}^{m-1}u_j\ge n-m-v(m-1)+1\ge v+1,
\]
so there is no hidden closing-gap restriction. The uniquely distinguished last-delayed car has \(n\) possible initial sites. For each site, the \(m\) gaps are uniquely reconstructed from one admissible forest and the forced closing gap; conversely, the physical extremizer recovers its distinguished car uniquely. Thus there is no rotation or car-label overcounting. The number of extremal indexed configurations is exactly \(n\) times the forest count, giving the asserted \(\frac{n}{m}\binom{(v+1)m-2}{m-1}\). The forest count is positive, proving sharpness of the \(m-1\) bound.

**5. Critical-window probability.** Divide the exact extremizer count by \(\binom{n}{m}\). At \(n_0=(v+1)m\), cancellation yields
\[
P_{m,0}=\frac{vm}{(v+1)m-1}\longrightarrow\frac{v}{v+1}.
\]
With fixed surplus \(h\), one further has
\[
\frac{P_{m,h}}{P_{m,0}}=\frac{(v+1)m+h}{(v+1)m}
\frac{\binom{(v+1)m}{m}}{\binom{(v+1)m+h}{m}}
\longrightarrow\left(\frac{v}{v+1}\right)^h,
\]
which proves the displayed limiting law.

## Verification

Three standalone Python 3 programs accompany this result. `verify_gap.py` independently advances the cyclic gap dynamical system, enumerates 70 bounded parameter cases, and checks both the sharp relaxation time and the exact number of extremal gap vectors. `verify_binary.py` simulates physically occupied sites for eight separate car-count, speed and surplus cases, independently checking the number of extremal indexed binary configurations against the formula. `verify_forest.py` compares a ballot-path recurrence, an independent formal-power-series computation of the ordered-forest coefficients, and the binomial expression in 30 cases. Their recorded outputs are included in separate text files and were reproduced directly. All-length correctness follows from the proof, **not** from these finite checks.

## Relationship to prior work

Fukui and Ishibashi's 1996 traffic model introduces deterministic simultaneous high-speed motion with a finite speed cap. Fukś and Boccara (1997) define the deterministic generalized traffic family \(R_{v,1}\) and its fundamental diagram. Wang and collaborators (1998) treat stationary flow and convergence, expressly citing a 1997 finite-time approach of Wang, Wang and Hui. Fukś (1999) derives exact infinite-Bernoulli preimage probabilities and fundamental diagrams in deterministic high-speed traffic. These establish the model and related convergence questions but the inspected source material does not give the joint sharp low-density \(m-1\) extremal-time theorem, the indexed multiplicity, or its critical-window forest law.

An additional 1998 statistical-mechanical Fukui–Ishibashi paper reports speed-density relations and exact calculations in its abstract; its full text was unavailable, so no stronger noncoverage conclusion is drawn.

A previously published theorem for *speed one*, Rule 184, gives the corresponding Catalan extremizer count and a \(2^{-h-1}\) critical-window law. That special-speed formula does not imply the stated result for arbitrary fixed speeds \(v\ge2\): the local min-plus increments now range down to \(-v\), and the extremal structures form \(v\)-component \((v+1)\)-ary forests instead of one plane tree. The proof adapts the cyclic-minimum strategy to this genuinely different speed-dependent enumeration, so no novelty is claimed for the speed-one case. The original 1996 and the short 1997 finite-convergence articles were not fully accessible; historical priority is therefore qualified rather than certified.

## Limitations

Only deterministic simultaneous traffic updates, labelled cyclic rings, \(v\ge2\), and low-density \(n\ge(v+1)m\) are covered. The first time all cars attain maximum speed is not a stochastic mixing time, stationary total delay, or a general high-density relaxation time. The positive probability limit holds for each fixed \(v\) and fixed excess \(h\) as \(m\to\infty\), not uniformly over growing speed or surplus. Full inspection of two plausible archival sources was unavailable and their unexamined contents remain a specific originality risk. Independent expert validation has not been performed.

## References

- M. Fukui and Y. Ishibashi, *Traffic Flow in 1D Cellular Automaton Model Including Cars Moving with High Speed*, Journal of the Physical Society of Japan **65** (1996), 1868, issue published June 1, 1996. https://www.jstage.jst.go.jp/browse/jpsj/65/6/_contents
- H. Fukś and N. Boccara, *Generalized deterministic traffic rules* (1997), https://arxiv.org/abs/adap-org/9705003.
- B.-H. Wang et al., *Analytical results for the steady state of traffic flow models with stochastic delay* (1998), https://arxiv.org/abs/cond-mat/9804269.
- H. Fukś, *Exact results for deterministic cellular automata traffic models* (1999), https://arxiv.org/abs/comp-gas/9902001.
- B. Wang, B.-H. Wang and Z.-X. Hui, *One-dimensional Fukui–Ishibashi traffic flow model*, Journal of the Physical Society of Japan **66** (1997), 3683, https://www.jstage.jst.go.jp/browse/jpsj/66/11/_contents.
- B.-H. Wang, Y.-R. Kwong and P.-M. Hui, *Statistical mechanical approach to Fukui-Ishibashi traffic flow models*, Physical Review E **57** (1998), 2568, https://doi.org/10.1103/PhysRevE.57.2568.
- *Catalan extremizers for cyclic traffic relaxation under Rule 184* (published 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-catalan-extremizers-for-cyclic-traffic-relaxation-under-rule-184--59fbc93a8b51.
