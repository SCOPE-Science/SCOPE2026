# Binary game-state disorder eliminates current in a mobile defector boundary on a cycle

## Finding
In a frozen two-state public-goods environment on a cycle, the payoff-imitation dynamics of a single cooperator block have an exact recurrent boundary chain. Suppose every edge synergy belongs to \(\{r_L,r_H\}\), with \(1<r_L<r_H<1+r_L/2\). Starting with one cyclic block of at least two cooperators and one nonempty complementary block of defectors, the process almost surely reaches and thereafter remains within states with exactly one or two adjacent defectors. All \(2n\) such states communicate, and **their stationary chain is reversible for every binary edge-state pattern**. Its stationary law is the explicit finite product recurrence below, yielding an exact stationary mean number of defectors. For homogeneous synergy \(r\in(1,2)\), the mean is precisely \(2/r\), independently of the ring size. Binary reversibility does not extend to arbitrary three-level edge environments: a five-edge example has forward/backward cycle-product ratio \(77/75\). The upper strict-positivity bound is sharp across all binary patterns: for \(r_H>1+r_L/2\) (with \(1<r_L<2\)), there are environments in which an isolated defector can disappear.

## Assumptions and scope
Let \(n\ge4\) and vertices be \(\mathbb Z/n\mathbb Z\); the game group at edge \(e_i=\{i,i+1\}\) has fixed benefit multiplier \(r_i\). The strategy \(s_i\) is \(1\) (cooperation) or \(0\) (defection). Contributions cost one unit per group, and each vertex plays both adjacent edge games and averages the two resulting payoffs:
\[
P_i(s)=-s_i+\tfrac12\bigl[r_{i-1}(s_{i-1}+s_i)+r_i(s_i+s_{i+1})\bigr].
\]
At each discrete update choose a focal vertex uniformly and then either adjacent edge uniformly. If the other endpoint has the opposite strategy and strictly greater payoff, the focal vertex copies it with probability equal to the payoff difference divided by a fixed \(\Delta\ge2\max_i r_i+2\); otherwise the configuration remains unchanged. There are no mutations or edge-state transitions. This is a frozen-environment, pair-group restriction of a payoff-comparison public-goods model; it is not a claim about randomly resampled hypergraphs or active game transitions.

Write \(S_j\) for the state with only vertex \(j\) defective, and \(E_j\) for the state with exactly vertices \(j,j+1\) defective. Put \(h=1/(2n\Delta)\). Under \(1<r_L<r_H<1+r_L/2\), all four quantities below are positive:
\[
\begin{aligned}
a_j^+&=h(1+r_{j-1}/2-r_{j+1}),& a_j^-&=h(1+r_j/2-r_{j-2}),\\
b_j^-&=h(r_{j+2}-1),& b_j^+&=h(r_{j-2}-1).
\end{aligned}
\]
The only moves within the recurrent class are \(S_j\to E_j\) with probability \(a_j^+\), \(S_j\to E_{j-1}\) with probability \(a_j^-\), \(E_j\to S_j\) with probability \(b_j^-\), and \(E_j\to S_{j+1}\) with probability \(b_j^+\), together with self-loops.

## Proof
**Boundary reduction.** When both cyclic blocks contain at least two vertices, an adjacent boundary cooperator has the other cooperator as its interior neighbor. The difference between that cooperator's payoff and its neighboring boundary defector's payoff is exactly \(r_{\mathrm{interior\ cooperator\ edge}}-1>0\). Consequently only boundary defectors may switch to cooperation, reducing the length of the contiguous defector block. As long as at least two defectors remain, its length decreases almost surely in finitely many steps, because an eligible positive-probability transition persists until it occurs. When exactly one defector remains, the two neighboring cooperators have smaller payoffs by \(1+r_j/2-r_{j-2}\) and \(1+r_{j-1}/2-r_{j+1}\), respectively, both strictly positive by the multiplier bound. The isolated defector therefore cannot disappear and may only expand to a neighboring pair. In a pair, only the two boundary defectors can copy cooperation, at respective differences \(r_{j-2}-1\) and \(r_{j+2}-1\). Every indicated transition is positive. The \(2n\) states thus form one irreducible recurrent class, and neither all-cooperation nor all-defection is accessible.

**Cycle affinity.** The non-loop transitions form a \(2n\)-cycle. Kolmogorov's finite Markov-chain cycle criterion says reversibility holds exactly when the clockwise and anticlockwise products agree. Their ratio is
\[
\mathcal R=\prod_{j=0}^{n-1}\frac{a_j^+b_j^+}{b_j^-a_{j+1}^-}
=\prod_{j=0}^{n-1}\frac{1+r_{j-1}/2-r_{j+1}}{1+r_{j+1}/2-r_{j-1}}.
\]
The factors involving \(r_{j-2}-1\) cancel by cyclic index permutation. For a binary environment, every factor with equal levels is one; a factor corresponding to an oriented \(r_L\)-to-\(r_H\) pair is the reciprocal of the factor for the opposite orientation. Under the step-two permutation on the ring, even when it has two separate parity cycles, the number of forward \(r_L\)-to-\(r_H\) transitions equals the number of reverse transitions on each cycle. Thus \(\mathcal R=1\) for **every** binary environment.

**Stationary formula.** Set \(w(S_0)=1\), and recursively for \(j=0,1,\dots,n-1\), set
\[
w(E_j)=w(S_j)\frac{a_j^+}{b_j^-},\qquad
w(S_{j+1})=w(E_j)\frac{b_j^+}{a_{j+1}^-}.
\]
The last weight agrees with \(w(S_0)\) by \(\mathcal R=1\). Normalizing by \(Z=\sum_j[w(S_j)+w(E_j)]\) gives the unique stationary distribution and
\[
\mathbb E_{\pi}[D]=\frac{\sum_j[w(S_j)+2w(E_j)]}{Z}.
\]
For equal multipliers \(r\), all singleton weights are equal and every pair weight is \((1-r/2)/(r-1)\) times its singleton weight. Substitution yields \(\mathbb E_{\pi}[D]=2/r\).

**Sharpness and a third level.** If \(r_H>1+r_L/2\), choose an isolated defector at vertex \(j\) and place \(r_{j-2}=r_H\), \(r_j=r_L\). The defector then sees its left neighboring cooperator as strictly more profitable and may copy it, reaching the absorbing all-cooperator state. At equality this move is tied, so the theorem does not assert that extinction occurs. For the five-edge pattern \((11/10,11/10,6/5,11/10,13/10)\), the same exact cycle-product expression gives \(\mathcal R=77/75\ne1\). Its positive irreducible class is nonreversible, exhibiting a stationary current. This shows the binary cancellation is substantive, not generic to every frozen payoff environment.

## Verification
The accompanying standalone `hetero_checker.py` performs exact-rational payoff comparisons directly from the definition and independently checks the predicted transitions, recursive balance weights and stationary equations for every one of the \(1008\) binary edge patterns on rings of orders \(4\) through \(9\), amounting to \(16320\) recurrent states. It also checks the all-cooperator escape beyond the bound for ring orders \(5\) through \(9\), the homogeneous mean \(2/r\), and the nonreversible three-level ratio \(77/75\). Run `python hetero_checker.py` using Python's standard library. The finite checks corroborate but do not replace the general proof.

## Relationship to prior work
Wei, Xiong, Li, Feng and Szolnoki study public-goods imitation with two kinds of games on random uniform hypergraphs and game transitions, primarily through simulations. This theorem freezes the edge environment and restricts group size to two, obtaining an exact theorem about the resulting finite stochastic dynamics. Earlier work by Cooper, Dyer and Mohanaraj analyzes a different, synchronous imitation mechanism on graph cycles; Ohtsuki and Nowak analyze fitness-based cycle replacement and fixation. Kolmogorov's cycle criterion and detailed balance are standard; the new content claimed here is the payoff-specific reduction, strict trapping threshold, binary-state cancellation and exact invariant law. Source comparison does not establish absolute uniqueness across all literature.

## Limitations
The binary multipliers must satisfy the strict bound; the equality case may have disabled transitions, and above-bound environments need not all exhibit extinction. The analysis assumes a single contiguous initial cooperative block of size at least two; it does not classify arbitrary multi-block configurations, stochastic resampling of edges, active game transitions, or mutation. The theorem is for a simple deterministic ring with stochastic asynchronous revision and two-player public-good groups, not a general hypergraph theorem. The three-level witness only demonstrates possible nonzero current, not a universal result for every ternary pattern.

## References
- Wei, N., Xiong, X., Li, Q., Feng, M., and Szolnoki, A. *Cooperation in Public Goods Games over Uniform Random Hypergraphs with Game Transitions*, first public preprint 2026-03-24, https://arxiv.org/abs/2603.22967; J. R. Soc. Interface 23 (2026), 20251319, https://doi.org/10.1098/rsif.2025.1319.
- Cooper, C., Dyer, M., and Mohanaraj, V. *On the Imitation Strategy for Games on Graphs*, preprint https://arxiv.org/abs/1102.3879.
- Ohtsuki, H. and Nowak, M. A. *Evolutionary Games on Cycles*, Proc. R. Soc. B (2006), https://doi.org/10.1098/rspb.2006.3576.
- Kolmogorov's cycle criterion for finite Markov-chain detailed balance (standard result).
