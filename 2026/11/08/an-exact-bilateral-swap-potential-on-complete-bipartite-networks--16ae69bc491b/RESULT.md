# An exact bilateral swap potential on complete bipartite networks with a strict price-of-stability gap

## Finding

Consider the *swap average type-distance game* on the complete bipartite graph \(K_{a,b}\), with \(a,b\ge 1\) and one agent at every vertex. Each agent has a fixed type in \([0,1]\), and its cost is the average absolute type distance to its neighbors. A swap is permitted only if it strictly decreases **both** participants' costs.

Let \(A\) and \(B\) denote the agents currently located in the two parts, of sizes \(a\) and \(b\). Define
\[
\Psi(A,B)=\frac{1}{a}\sum_{\{i,j\}\subseteq A}|t_i-t_j|+\frac{1}{b}\sum_{\{i,j\}\subseteq B}|t_i-t_j|.
\]
For any cross-part swap of agents \(x\in A\) and \(y\in B\), let primes denote the post-swap state. Then the *bilateral exact-change identity* holds:
\[
\Psi(A',B')-\Psi(A,B)= [c_x(A,B)-c_x(A',B')]+[c_y(A,B)-c_y(A',B')].
\]
A within-part swap changes neither costs nor \(\Psi\). Consequently **every strictly bilaterally improving swap increases \(\Psi\)**. For every pair of part sizes and every type multiset, the game has the finite improvement property and at least one pure swap equilibrium, even when \(a\ne b\) so the graph is nonregular.

The finite improvement property does **not** force the social optimum to be a swap equilibrium. In the seven-agent instance \(K_{2,5}\) with types
\[
(0,0,0,0,\tfrac14,\tfrac34,1),
\]
the **exact price of stability**—the minimum social cost among swap equilibria divided by the minimum social cost among all placements—is \(17/15>1\).

## Assumptions and scope

The underlying graph is a finite nonempty complete bipartite graph \(K_{a,b}\), where \(a,b\) are positive integers; every vertex is occupied. The agents are labeled, but their types need not be distinct. Types are immutable real numbers in \([0,1]\). For a placement \(\sigma\), with \(N_i(\sigma)\) the agents occupying neighbors of agent \(i\), put
\[
c_i(\sigma)=\frac{1}{|N_i(\sigma)|}\sum_{j\in N_i(\sigma)}|t_i-t_j|.
\]
The allowed move is a simultaneous exchange of two agents, which is *improving* only when each participant's individual cost strictly falls. Social cost means \(\mathcal C(\sigma)=\sum_i c_i(\sigma)\). Its positive-valued instance-specific price of stability is
\[
\operatorname{PoS}=\frac{\min_{\sigma\text{ a swap equilibrium}}\mathcal C(\sigma)}{\min_{\sigma}\mathcal C(\sigma)}.
\]
No dynamics with empty vertices or unilateral movement are asserted. The proof of the potential identity works in fact for any fixed symmetric nonnegative pairwise dissimilarities \(d(i,j)\) with \(d(i,i)=0\); using the absolute difference ties the statement to the cited continuous-type game.

## Proof

**1. Cross-part identity.** Write \(d(i,j)=|t_i-t_j|\), and for any agent \(z\) put \(D_A(z)=\sum_{i\in A}d(z,i)\) and \(D_B(z)=\sum_{j\in B}d(z,j)\). Take \(x\in A\), \(y\in B\) and swap them. Before the move the two participating agents pay
\[
c_x=\frac{D_B(x)}b,\qquad c_y=\frac{D_A(y)}a.
\]
Afterwards, \(A'=(A\setminus\{x\})\cup\{y\}\) and \(B'=(B\setminus\{y\})\cup\{x\}\). Therefore
\[
c_x'=\frac{D_A(x)+d(x,y)}a,\qquad c_y'=\frac{D_B(y)+d(x,y)}b.
\]
Let \(W(S)=\sum_{\{i,j\}\subseteq S}d(i,j)\). Removing \(x\) from \(A\) and inserting \(y\), and symmetrically for \(B\), yields exactly
\[
W(A')-W(A)=D_A(y)-D_A(x)-d(x,y),
\]
\[
W(B')-W(B)=D_B(x)-D_B(y)-d(x,y).
\]
Consequently
\[
\begin{aligned}
\Psi'-\Psi&=\frac{D_A(y)-D_A(x)-d(x,y)}a\\
&\qquad+\frac{D_B(x)-D_B(y)-d(x,y)}b\\
&=c_x+c_y-c_x'-c_y'.
\end{aligned}
\]
All denominators are strictly positive, including when one part is a singleton. A within-part exchange preserves each agent's part and every part's type multiset. Hence it changes no costs and leaves the potential unchanged.

**2. Termination.** If both participants strictly decrease their costs, the displayed identity makes \(\Psi'-\Psi>0\). There are only \((a+b)!\) labeled placements, fewer if symmetries are identified; thus no strictly increasing sequence can revisit a placement. Every improving sequence terminates in finitely many steps, and its terminal placement is a swap equilibrium. The proof requires no lower bound on the size of each strictly positive cost reduction.

**3. Exact price-of-stability witness.** Consider \(a=2,b=5\) and multiply all seven types by four for the following enumeration. The scaled multiset is \(\{0,0,0,0,1,3,4\}\). For a chosen two-agent part \(A\), define
\[
E(A)=\sum_{i\in A}\sum_{j\notin A}|4t_i-4t_j|.
\]
Every original placement has total social cost \(\mathcal C=(1/2+1/5)E/4=7E/40\). Up to exchanges of equal-type agents and permutation of vertices inside each part, there are exactly seven possible types in the small part. The table exhausts them; the final column records whether at least one cross-part swap strictly improves both participants.

| Scaled type multiset in the two-agent part | \(E\) | Improving swap exists? |
|---|---:|---|
| \((0,0)\) | 16 | Yes |
| \((0,1)\) | 15 | Yes |
| \((0,3)\) | 17 | No |
| \((0,4)\) | 20 | No |
| \((1,3)\) | 20 | Yes |
| \((1,4)\) | 23 | No |
| \((3,4)\) | 33 | Yes |

For example, at the unique socially least costly type profile \((0,1)\), exchanging the agent of scaled type \(1\) in the small part with the agent of scaled type \(3\) in the large part changes their individual scaled costs respectively from \(8/5\) to \(3/2\), and from \(5/2\) to \(12/5\), so both improve. All seven entries, including the no-improving-swap conclusions, follow by checking at most \(2\cdot5\) possible cross-part transpositions per row. The accompanying \(\texttt{verify.py}\) repeats these tests in exact rational arithmetic using independently defined individual costs and pair-sum potential.

Thus the global optimum has \(E=15\) but every swap equilibrium has \(E\ge17\), with equality attained at \((0,3)\). Both costs are strictly positive; hence
\[
\operatorname{PoS}=\frac{7\cdot17/40}{7\cdot15/40}=\frac{17}{15}.
\]
This also proves that the potential is **not** merely a reversed social cost on every irregular complete bipartite graph. No claim of smallest possible witness or universal worst-case price of stability is made.

## Verification

A self-contained Python 3 script \(\texttt{verify.py}\), using only \(\texttt{itertools}\) and \(\texttt{fractions}\) from the standard library, checks the cross-swap identity by two separately computed expressions. It exhaustively tests the identity in **212,500 cross-part swaps** across **1,519** multisets/part-size profiles: all nondecreasing type vectors of length \(2\) through \(7\) with entries in \(\{0,\tfrac13,\tfrac23,1\}\) and all nontrivial part sizes. It separately examines all **21** labeled choices for the two-agent part of the seven-agent witness, checks every improving move, reduces to seven distinct type profiles, and proves by finite exhaustive enumeration that the best equilibrium and social optimum have scaled cross-costs \(17\) and \(15\).

The infinite family result does **not** depend on an enumeration: it follows from the exact finite-set algebra and strict potential ascent. The finite script is a reproducibility check of its algebra and a complete certificate for the specific seven-agent example, not a proof by finite experimentation of the general theorem.

## Relationship to prior work

Bilò, Bilò, Döring, Lenzner, Molitor and Schmidt (2023) introduce the swap average type-distance game and prove its finite improvement property on **regular** graphs (Proposition 3 of the IJCAI paper, and full arXiv version). Their Theorem 17 establishes price of stability one on regular graphs; Theorem 18 establishes the same result on paths. The present result instead supplies a degree-sensitive, **within-part** potential for all complete bipartite graphs, including the irregular cases excluded by those hypotheses, and an exact irregular example whose best equilibrium is not a social optimum.

Bilò, Bilò, Lenzner and Molitor (2022) study single-peaked utilities for two categorical agent types, including bipartite graphs. Those utilities are functions of same-type fractions, rather than average **metric type-distance**; their bipartite equilibrium and price-of-stability theorems do not state the present potential identity or apply directly to its seven-agent continuous-type example. The classic 2020 categorical swap model uses a different individual satisfaction rule. Searches of relevant mathematical records and literature found no direct equivalent, but they cannot exclude unindexed or differently formulated earlier coverage.

## Limitations

Only **fully occupied**, **complete** bipartite networks are covered. Arbitrary bipartite graphs need not share the identity; the theorem makes no assertion for them, for vacancies, jumps, unilateral exchanges, heterogeneous neighbor weights, or distance functions depending on the destination. The price-of-stability example is an **instance-specific** exact ratio, not a general bound or proof of minimal order. Infinite numerical enumeration was neither needed nor attempted. Literature priority remains subject to independently checking all potentially equivalent results; no independent scientific audit or external certification is claimed.

## References

1. D. Bilò, V. Bilò, M. Döring, P. Lenzner, L. Molitor and J. Schmidt, *Schelling Games with Continuous Types*, arXiv:2305.06819v1, publicly released May 11, 2023; IJCAI 2023, 2520–2527, DOI:10.24963/ijcai.2023/280. https://arxiv.org/abs/2305.06819 ; https://doi.org/10.24963/ijcai.2023/280 .
2. D. Bilò, V. Bilò, P. Lenzner and L. Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599, 2022. https://arxiv.org/abs/2204.12599 .
3. D. Bilò, V. Bilò, P. Lenzner and L. Molitor, *Topological Influence and Locality in Swap Schelling Games*, MFCS 2020, DOI:10.4230/LIPIcs.MFCS.2020.15. https://arxiv.org/abs/2005.02752 .
