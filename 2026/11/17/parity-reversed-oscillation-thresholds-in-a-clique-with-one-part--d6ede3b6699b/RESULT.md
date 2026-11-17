# Parity-reversed oscillation thresholds in a clique with one partially attached vertex

## Finding
For integers \(m\ge3\) and \(1\le r\le m\), form \(H_{m,r}\) from the complete graph on \(m\) labelled vertices by adding one more vertex adjacent to exactly \(r\) clique vertices. Every vertex synchronously takes the strict majority bit among its *open* neighbors, retaining its current bit if there is a tie. Let \(C_2(m,r)\) be the number of distinct primitive temporal two-cycles; spatially distinct labelled configurations are not identified by graph automorphisms.

**Exact oscillation law.** The only fixed configurations are the two unanimous ones. All eventual periods divide two, and
\[
C_2(2q,r)=
\begin{cases}
\binom{2q-r}{q},&1\le r\le q,\\
0,&q<r\le2q,
\end{cases}
\qquad(q\ge2),
\]
while
\[
C_2(2q+1,r)=\binom r{q+1}+\mathbf1_{\{r=2q\}}\binom{2q}{q}
\qquad(q\ge1),
\]
where a binomial coefficient is zero if its lower index exceeds the upper. **Every primitive two-cycle has no incoming state from outside that cycle.** Thus its complete attraction basin contains exactly its two configurations.

In particular, when the clique size is even, raising the extra vertex's degree from \(q\) to \(q+1\) destroys the last oscillation. When the clique size is odd, oscillations first appear at degree \(q+1\), and an additional \(\binom{2q}{q}\) orbits arise at degree \(2q\) (one neighbor short of making the entire graph complete). The last increment from degree \(2q\) to \(2q+1\) leaves the total equal to \(\binom{2q+1}{q+1}\). These are count statements about already periodic states, not claims about the time needed to reach consensus.

## Assumptions and scope
Let \(A\) be the \(r\) neighbors of the exceptional vertex \(h\); let \(B\) be the remaining \(s=m-r\) clique vertices. For a bit configuration write \(a\) and \(b\) for the numbers of ones in \(A\) and \(B\), \(S=a+b\), and \(h\in\{0,1\}\) also for the exceptional bit. Both clique classes are individually labelled and the rule is open-neighborhood majority with *self-retention only upon a tie*. For \(s=0\), the graph is simply the complete graph on \(m+1\) vertices. An orbit means a set of configurations under temporal iteration; a two-cycle is counted once, not twice. Binomial coefficients count the labelled ways to choose ones inside each clique class.

## Proof
**1. Exact one-step maps.** Every vertex of \(A\) has degree \(m\), and sees \(S-x+h\) one-neighbors when its present bit is \(x\); every vertex of \(B\) has degree \(m-1\), and sees \(S-x\). The hub takes the majority of its \(r\) neighbors in \(A\), retaining its bit on a tie. Evaluating both possible input bits gives the following *bitwise*, rather than merely countwise, maps:

* If \(m=2q\), all of \(A\) becomes zero for \(S+h\le q\), and all becomes one for \(S+h\ge q+1\). The \(B\)-bits become all zero for \(S<q\), are **complemented individually** for \(S=q\), and become all one for \(S>q\).
* If \(m=2q+1\), all \(B\)-bits become zero for \(S\le q\) and one for \(S\ge q+1\). The \(A\)-bits become all zero for \(S+h\le q\), are complemented individually for \(S+h=q+1\), and become all one for \(S+h\ge q+2\).

These equations include all tie boundaries exactly.

**2. Even clique size.** Set \(m=2q\), \(q\ge2\). Because \(A\) is made homogeneous after every update, it is homogeneous in every periodic state. Write its common bit as \(\alpha\). When \(\alpha\) is constant at both phases of a two-cycle, the hub is forced to that bit at both phases. By complementation take \(\alpha=h=0\). Then \(b\le q\) is required to keep \(A\) at zero. If \(b<q\), the next \(B\)-state is all zero and remains so. If \(b=q\), the \(B\)-bits complement to have \(b'=s-q=q-r<q\), and the following update makes them all zero. Neither case gives a primitive two-cycle. Therefore \(A\) must alternate. Orient the two phases so that \(\alpha_0=0\), \(\alpha_1=1\). The hub updates to \(h_1=0\), \(h_0=1\). For \(A\) to switch up requires \(b_0+1\ge q+1\), hence \(b_0\ge q\); for it to switch down requires \(r+b_1\le q\). A \(B\)-update from \(b_0>q\) gives \(b_1=s>q-r\) and violates the latter bound. Thus \(b_0=q\), \(b_1=s-q=q-r\), with individual \(B\)-bits complemented in each direction because the two clique totals are both \(q\). Existence requires \(r\le q\); choosing the \(q\) one-bits of \(B\) gives exactly \(\binom{2q-r}{q}\) orbits, each with exactly one phase having \(A=0,h=1\).

**3. Odd clique size, with \(s\ge1\).** Let \(m=2q+1\), \(q\ge1\). All \(B\)-bits are homogeneous in every periodic state; let \(\beta_t\) be their common bit at phase \(t\). If \(\beta_0=\beta_1=0\), then \(a_t\le q\) at both phases. The \(A\)-update cannot make all ones. If it ever makes all zero, that phase cannot belong to a primitive two-cycle: with \(A=B=0\), the next update again makes \(A=B=0\), and the hub is forced to zero. Thus \(A\) must complement at both phases. The necessary equalities \(a_t+h_t=q+1\) with \(a_t\le q\) force \(a_t=q\), \(h_t=1\), and since complementing \(A\) changes \(a_t\) to \(r-a_t\), force \(r=2q\) (hence \(s=1\)). Conversely, this produces \(\binom{2q}{q}/2\) distinct temporal two-cycles with \(B=0,h=1\). Bit complementation gives the equal number with \(B=1,h=0\). Together these contribute \(\binom{2q}{q}\) orbits, only when \(r=m-1\).

If \(\beta_0\ne\beta_1\), orient so that \(\beta_0=0\), \(\beta_1=1\). The two updates of \(B\) demand \(a_0\ge q+1\) and \(a_1+s\le q\). The \(A\)-update at phase zero cannot produce all ones, since this would give \(a_1=r\) and \(a_1+s=m>q\); it therefore must complement. Consequently \(a_0+h_0=q+1\), which forces \(a_0=q+1,h_0=0\) and \(a_1=r-q-1\). The second clique total is \(a_1+s=q\). Returning to a configuration with \(q+1\) ones in \(A\) requires the second \(A\)-update to complement as well, so \(h_1=1\). The hub changes as required because \(q+1>r/2\) and \(r-q-1<r/2\). Conversely, for every \(r\ge q+1\), each choice of \(q+1\) one-bits in \(A\), with \(B=0,h=0\), gives such a primitive two-cycle. Each orbit is counted exactly once in this orientation, contributing \(\binom r{q+1}\).

For \(s=0\), the entire graph is \(K_{2q+2}\). Its \(2q+2\) vertices have odd degree; every configuration with \(q+1\) ones flips globally, all other configurations reach unanimous consensus. Thus the orbit count is \(\frac12\binom{2q+2}{q+1}=\binom{2q+1}{q+1}\), identical to the displayed odd formula at \(r=m\).

**4. Fixed states.** For even \(m\), every fixed state has homogeneous \(A\), and the hub shares its bit. With \(A=h=0\), the condition to keep \(A=0\) gives \(b\le q\). If \(b<q\), the \(B\)-update is all zero, so fixedness requires \(b=0\); at \(b=q\), \(B\) complements and cannot be fixed. Complementation supplies only the all-one state. For odd \(m\) with \(s\ge1\), a fixed state has homogeneous \(B\); with \(B=0\) it needs \(a\le q\). Mixed \(A\) cannot be fixed (at the middle threshold it complements). If \(A=1\), then \(r=a\le q\), but the necessary \(A\)-threshold \(a+h\ge q+2\) is impossible. Thus \(A=0\), and the hub is zero. Complementation gives the other fixed state; the complete-graph case is immediate.

**5. No other periods.** Write all bits as signs \(\pm1\). Add a self-loop of weight one to each even-degree vertex, and none to odd-degree vertices; let \(M\) be the symmetric resulting adjacency matrix. Every local field \((Mx)_v\) is a nonzero odd integer and its sign equals the stated tie-retaining majority rule. For successive states \(x_t\) set \(P_t=x_{t+1}^{\mathsf T}Mx_t\). Since \(x_{t+2}\) uniquely maximizes \(z^{\mathsf T}Mx_{t+1}\) over sign vectors \(z\), symmetry gives \(P_{t+1}\ge P_t\), strictly if \(x_{t+2}\ne x_t\). The integer sequence \(P_t\) is bounded, so eventually \(x_{t+2}=x_t\). Consequently every periodic point already has period one or two.

**6. Unique incoming phase.** The above classification also determines all one-step preimages of its two-cycle states. For even \(m\), take a phase with \(A=0,h=1,b=q\). If \(r<q\), its mixed \(B\)-pattern can only be produced by the \(S=q\) *complement* branch. Hence the previous \(B\)-pattern is its complement, with \(q-r\) ones. To output \(A=0\) then forces previous \(h=0\), and \(S=q\) forces all \(r\) previous \(A\)-bits to be one. If \(r=q\), the target \(B\) is all one; output \(A=0\) imposes \(S+h\le q\), which excludes the \(B\)-all-one branch and again forces \(S=q,h=0,B=0,A=1\). So the preceding phase is unique. Complementation covers the other phase.

For odd \(m\) with \(s\ge1\), take a generic phase \(B=0,h=0,a=q+1\). Producing \(B=0\) forces predecessor \(S\le q\). Its \(A\)-pattern cannot be produced by a uniform-zero output (it contains ones), nor by uniform-one output (the predecessor has \(S+h\le q+1\)); therefore \(A\) must complement with \(S=q,h=1\). The predecessor \(A\) has \(r-q-1\) ones, so the predecessor \(B\) must be one, uniquely. Complementation covers the other phase. For the exceptional \(r=2q\) cycles, take the phase \(B=0,h=1,a=q\): the same argument forces the predecessor to have \(S=q,h=1\), complemented \(A\) with \(q\) ones, and \(B=0\), uniquely. For \(s=0\), a balanced state on the complete graph has only its global complement as predecessor. Each periodic state therefore has precisely its preceding orbit phase as its entire one-step inverse image. Iterating this uniqueness backwards excludes all transient ancestors of two-cycles.

## Verification
The supplied standalone `check_direct.cpp` constructs each graph from an adjacency mask and independently exhausts every labelled configuration for \(3\le m\le15\), \(1\le r\le m\) (117 graphs and 1,834,992 configurations). It checks exactly two fixed states, the formula for primitive two-cycles, and zero one-step entries into them from nonperiodic states. The separate count-weighted `check_symbolic.py` uses the three group counts and a different local-majority implementation to check every parameter pair through \(m=60\), a total of 1,827 graph instances. Both recorded runs pass. Neither finite check replaces the infinite algebraic argument above.

## Relationship to prior work
The general finite-graph period-at-most-two theorem of Goles and Olivos (1980) has no graph-specific orbit enumerator. Benjamini et al. (arXiv:1405.2486v1, 2014) study convergence and disagreement on unimodular and random graphs, not this defect-degree census. Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1, 2015) prove voting-time bounds and clique-module reductions, not exact two-cycle counts. A published note, *A central-binomial parity switch in majority dynamics on a clique with one leaf* (2026; record `6ca03ef32ff2`), proves the \(r=1\) specialization (and sharper transient information there). It does **not** imply the intermediate degrees, the odd-clique near-completion spike, or isolation for all \(r\). Complete-graph oscillations at \(r=m\) are classical; their inclusion here fixes the boundary conditions of the varying-degree theorem. No historical-exclusivity claim is made.

## Limitations
The theorem covers a single added vertex and all its possible positive degrees, not multiple exceptional vertices or arbitrary split graphs. It counts initially periodic orbits and proves their isolation; it does not give the entry-time census of all trajectories that reach fixed points. A related original Goles–Olivos full text could not be accessed, although its abstract explicitly states the general two-period property; unindexed earlier treatment of this particular graph family remains possible. Independent mathematical audit is not performed.

## References
1. Itai Benjamini, Siu-On Chan, Ryan O'Donnell, Omer Tamuz, Li-Yang Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first public 2014-05-11, https://arxiv.org/abs/1405.2486.
2. Dominik Kaaser, Frederik Mallmann-Trenn, Emanuele Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, first public 2015-08-14, https://arxiv.org/abs/1508.03519.
3. Eric Goles and Jorge Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
4. *A central-binomial parity switch in majority dynamics on a clique with one leaf*, published research note (2026), public record identifier `6ca03ef32ff2`.
