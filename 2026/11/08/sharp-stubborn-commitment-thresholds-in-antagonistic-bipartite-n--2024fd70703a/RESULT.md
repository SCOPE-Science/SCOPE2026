# Sharp stubborn-commitment thresholds in antagonistic bipartite network games

## Finding
For two opposing groups in the binary conformist–rebel network game, the minimum number of vertices whose actions must be fixed to enable a pure equilibrium has a sharp parity-dependent formula. If ties are permitted, no fixed vertices are needed precisely when both groups are even. Otherwise the minimum is the smaller of the two half-group ceilings. Requiring a unique best response at every flexible vertex always costs the smaller of the two strict-majority thresholds, even when an unmodified weak equilibrium exists. At either positive minimum, successful interventions and their probability under random deployment are classified exactly.

Specifically, for \(a,b\ge1\),
\[
 k_{\mathrm{weak}}=\begin{cases}
 0,& 2\mid a\text{ and }2\mid b,\\
 \min\{\lceil a/2\rceil,\lceil b/2\rceil\},&\text{otherwise},
 \end{cases}
 \qquad
 k_{\mathrm{strict}}=\min\{\lfloor a/2\rfloor+1,\lfloor b/2\rfloor+1\}.
\]
At a positive minimum \(k\), define the side-specific thresholds \((t_L,t_R)\) by ceilings in the weak case and by floor-plus-one in the strict case. All and only minimum-size successful interventions pin \(k\) vertices on one side with \(t_L=k\) or \(t_R=k\), and make all pins have the same chosen action. Therefore, among interventions obtained by uniformly choosing \(k\) labeled vertices and independently assigning a fair binary fixed action to each, the probability of equilibrium existence at this minimum is exactly
\[
 q_k=\frac{2\left(\mathbf1_{\{t_L=k\}}\binom ak+
 \mathbf1_{\{t_R=k\}}\binom bk\right)}{2^k\binom{a+b}{k}}.
\]
For the zero-size weak intervention when both sides are even, \(q_0=1\).

For illustration, on \(K_{4,4}\), the weak minimum is zero whereas the strict minimum is three; a random three-vertex intervention creates an active-strict equilibrium with probability \(1/28\). On \(K_{5,5}\), both minima are three and each random minimum-size intervention succeeds with probability \(1/24\).

## Assumptions and scope
Let \(L\) and \(R\) be two labeled, nonempty vertex sets with \(|L|=a\) and \(|R|=b\), with all edges between them and no others. Actions are \(0\) or \(1\). Originally each \(i\in L\) receives \(u_i=|\{j\in R:x_j=x_i\}|\); each \(j\in R\) receives \(u_j=|\{i\in L:x_i\ne x_j\}|\). An intervention replaces a selected vertex's feasible strategy set by a singleton \(\{0\}\) or \(\{1\}\). These stubborn vertices have no feasible unilateral deviation. All other vertices retain the original payoff and both actions.

A *weak pure equilibrium* is a profile in which no unpinned player has a strictly profitable deviation; ties are permitted. An *active-strict pure equilibrium* is a profile where each unpinned vertex has a **unique** payoff-maximizing action. This term is deliberately restricted to vertices with two feasible actions; no strictness property is asserted for fixed vertices. The cost of an intervention is the number of vertices converted to fixed-action agents, not the number of edges or the magnitude of transfers. The operator chooses which vertices to fix and their fixed actions. A separate probability statement describes random rather than designed interventions.

## Proof
For an action profile, let \(X\) be the number of \(1\)-actions in \(L\) and \(Y\) the number of \(1\)-actions in \(R\). Any unpinned conformist in \(L\) chooses a majority action on \(R\), allowing either action if \(Y=b/2\); any unpinned rebel in \(R\) chooses a minority action on \(L\), allowing either if \(X=a/2\). Uniqueness holds exactly when the appropriate opposite-side count is not tied.

**Weak lower bound.** Suppose there are \(k_L<\lceil a/2\rceil\) pins in \(L\) and \(k_R<\lceil b/2\rceil\) in \(R\). If \(Y\ne b/2\), every flexible conformist takes the strict majority action \(s\) on \(R\). As there are more than \(a/2\) flexible conformists, \(X\) has strict majority \(s\). Every flexible rebel then takes \(1-s\), which is a strict majority on \(R\) because there are more than \(b/2\) flexible rebels. This contradicts the choice of \(s\). Therefore \(Y=b/2\). If \(X\ne a/2\), the same argument starting with the rebels forces a strict majority on \(R\), another contradiction. Hence both \(X=a/2\) and \(Y=b/2\), which requires \(a,b\) even. In the even-even case with zero pins, a half-zero, half-one split on each side is a weak equilibrium. Otherwise any successful intervention has at least \(\min\{\lceil a/2\rceil,\lceil b/2\rceil\}\) vertices.

**Strict lower bound.** Suppose \(k_L\le\lfloor a/2\rfloor\) and \(k_R\le\lfloor b/2\rfloor\), and suppose every flexible player has a unique best response. Then neither opposite-side total may be tied. If \(s\) is the unique majority action on \(R\), all unpinned conformists choose \(s\). Since at least \(a/2\) left vertices choose \(s\), \(X\) cannot have \(1-s\) as a strict majority. Being untied, its strict majority is therefore \(s\). All unpinned rebels take \(1-s\); similarly, at least \(b/2\) right vertices take \(1-s\), so \(Y\) cannot have strict majority \(s\), a contradiction. Thus at least one side must have strictly more than half its vertices pinned.

**Sharp constructions.** To meet a left-side weak threshold, pin \(k_L=\lceil a/2\rceil\) left vertices to action \(0\), let every remaining conformist use \(1\), and let every right rebel use \(1\). The conformists best respond to the unanimous right side and the rebels see \(X=a-k_L\le a/2\), so choosing \(1\) is optimal (with a possible tie). The same construction is active-strict when \(k_L=\lfloor a/2\rfloor+1\), because then \(X<a/2\). Alternatively, pin \(\lceil b/2\rceil\) right vertices to \(1\), assign all other right rebels to \(0\), and assign all left conformists to \(1\); this is weakly stable because \(Y\ge b/2\), and it is active-strict with \(\lfloor b/2\rfloor+1\) pins. Reversing all actions produces the symmetric constructions. These attain the lower bounds.

**Characterization at a positive minimum.** The lower-bound arguments apply whenever both pin counts are below their respective thresholds, so all minimum-cost pins must lie on a side attaining the minimum threshold. If all pins lie on \(L\), with none on \(R\), any successful profile at a positive minimum has a unanimous or untied right-side response unless the even-even zero-pin case applies. Every flexible left player then takes the same action \(s\); the unpinned right players may mix only when the left total ties; nevertheless the right total must have a strict majority action \(s\) so that all flexible left players take \(s\). The left total must have either a tie (for weak equilibrium with even \(a\)) or a strict majority opposite \(s\) (odd weak case or active-strict case). At exactly \(k_L=\lceil a/2\rceil\) or \(k_L=\lfloor a/2\rfloor+1\), that condition forces every pinned left vertex to take \(1-s\). The argument with the roles of the sides exchanged shows that any minimum intervention entirely on \(R\) likewise pins a unanimous action. The constructions above show every such unanimous choice succeeds.

**Random deployment.** There are \(\binom{a+b}{k}2^k\) equally likely labeled intervention descriptions of a specified positive size \(k\). For each side whose threshold equals \(k\), there are \(\binom{\text{side size}}k\) choices of fixed positions and exactly two uniformly assigned fixed-action profiles (all \(0\) or all \(1\)). Distinct sides give disjoint sets of intervention descriptions. Division yields \(q_k\). In particular, at \(K_{4,4}\) the strict count is \(2\binom43+2\binom43=16\) out of \(\binom83 2^3=448\), giving \(1/28\); at \(K_{5,5}\) the minimum count is \(2\binom53+2\binom53=40\) out of \(\binom{10}3 2^3=960\), giving \(1/24\).

## Verification
Run `python3 verify.py` from the extracted package directory using standard Python only. The checker independently enumerates all allowed pin positions, both fixed actions for each pin, and every action profile of the flexible vertices, directly checking best responses. It verifies the two minimum-budget formulas and the number of successful intervention descriptions at the minimum for all \(1\le a,b\le5\). This is a finite falsification test, not a substitute for the proof for all positive \(a,b\).

## Relationship to prior work
Pei, Cao and Zhang, *Network games with three types of players* (arXiv:2607.10997v1, July 13, 2026), Section 3.1 Result 3, show that an **unpinned** complete bipartite conformist–rebel game with \(m\) actions has a pure equilibrium exactly when both side sizes are divisible by \(m\); the present binary zero-pin case agrees with that characterization. Their later sections study stubborn-player equilibrium existence on other special graph classes and give general sufficient conditions, but do not give these minimum intervention costs, active-strict bounds, or random minimum-budget success probabilities. Cao, Sánchez and Zhang, *Network games with heterogeneous players* (arXiv:2607.05932v1, July 7, 2026), give general sufficient conditions for equilibrium in binary three-type networks; the present explicit constructions are consistent with, and partly follow from, those sufficient criteria, whereas the optimal lower bounds and the sharp tie-robustness contrast are additional. Earlier fashion-game work establishes existence/nonexistence and homophily principles without fixing stubborn-action intervention budgets.

## Limitations
This theorem concerns an undirected unweighted complete bipartite graph, exactly two actions, one initially homogeneous conformist class and one initially homogeneous rebel class, unit cost per fixed player, and existence rather than reachability of an equilibrium. Fixed agents have singleton feasible strategy sets; the active-strict refinement does not claim strictness for those agents. Arbitrary graph topology, heterogeneous thresholds, multiple strategies, synchronization of best-response dynamics and adversarially fixed pin actions are not classified. The stochastic formula assumes *uniform random pin positions and independent fair fixed actions*, and applies only at a minimum budget. No uniqueness or literature-exhaustiveness assertion is made.

## References
1. Shan Pei, Wenjie Cao, Boyu Zhang, *Network games with three types of players*, arXiv:2607.10997v1 (first public July 13, 2026), especially Sections 2–4. https://arxiv.org/abs/2607.10997
2. Wenjie Cao, Angel Sánchez, Boyu Zhang, *Network games with heterogeneous players*, arXiv:2607.05932v1 (first public July 7, 2026), Sections 2–3. https://arxiv.org/abs/2607.05932
3. Boyu Zhang, Zhigang Cao, Cheng-Zhong Qin, Xiaoguang Yang, *Fashion and Homophily*, Operations Research 66 (2018), 1486–1497. https://doi.org/10.1287/opre.2018.1746
