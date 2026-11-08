# A persistent ten-switch cycle in a six-agent coordinating imitation–best-response network

## Finding

**Theorem (a fair periodic non-equilibrating orbit).** There is a connected six-vertex simple undirected network with strictly opponent-coordinating, vertex-dependent two-action payoff matrices, four payoff-neighbor imitators and two exact best responders, and a **periodic activation sequence that visits every vertex in each period**, under which the asynchronous binary state never stabilizes. Its recurring orbit has ten genuine state switches, and a periodic activation word of length eleven activates every agent. All imitation steps have a unique highest-earning neighbor, and all best-response switches are strict.

In particular, convergence under *every* persistent asynchronous activation sequence, and a strict globally decreasing potential for every effective update, fail for general connected graphs in this precisely defined mixed model. The claim is existential. It does not imply nonconvergence under random activation or under the different rule that prohibits imitation of a neighbor with a payoff below one's own.

## Assumptions and scope

Use vertices \(V=\{0,1,2,3,4,5\}\), strategies \(A,B\), and the undirected edge set
\[
E=\{01,02,04,05,13,14,23,24,35\}.
\]
Here \(ij\) denotes the unordered edge joining vertices \(i\) and \(j\). Vertices \(0,2\) are exact best responders (BR), and \(1,3,4,5\) are imitators (I). For each vertex \(i\), the four payoff entries \((R_i,S_i,T_i,P_i)\) are payoffs against a neighboring strategy pair \((A,A),(A,B),(B,A),(B,B)\), respectively:

| \(i\) | type | \(R_i\) | \(S_i\) | \(T_i\) | \(P_i\) |
| --- | --- | ---: | ---: | ---: | ---: |
| 0 | BR | 2 | 0 | −1 | 5 |
| 1 | I | 12 | −1 | 0 | 13 |
| 2 | BR | 3 | −4 | −7 | 2 |
| 3 | I | 1 | −6 | −7 | 5 |
| 4 | I | 4 | −4 | −6 | 9 |
| 5 | I | 10 | −4 | −2 | 5 |

All six matrices satisfy \(\min\{R_i,P_i\}>\max\{S_i,T_i\}\), the strict opponent-coordination condition of the cited model. A vertex's utility \(u_i(x)\) is the **sum**, without degree normalization, of its pairwise payoffs against all neighbors in the current configuration \(x\).

An activated BR vertex selects the strategy giving larger hypothetical present utility against the unchanged neighbors, retaining its incumbent strategy in a tie. An activated imitator copies the strategy of a neighbor \(j\in N_i\) maximizing that neighbor's **total** utility \(u_j(x)\); if maximizing neighbors have conflicting strategies, it retains its incumbent strategy. The current vertex itself is **not** included among the candidate neighbors. This is the formal neighbor-only imitation rule (2) of Hasheminejad–Ramazi; comparing the neighbor's payoff with the imitator's own payoff is not part of the rule. Only one vertex updates in a step.

For every six-bit word below, the printed leftmost bit records vertex \(0\) and a \(1\) indicates \(A\) (a \(0\) indicates \(B\)).

## Proof

All edges in the displayed set are undirected. The graph is connected; for instance, vertex \(0\) connects to vertices \(1,2,4,5\), and vertex \(3\) connects to both \(1\) and \(5\). The payoff table gives the required opponent-coordination inequalities directly.

The following exact ten-switch trajectory uses activation word \((0,4,1,2,3,0,4,1,2,3)\). Each row gives the state **before** activation, the updating vertex and its rule, the state afterward, and a numerical witness to its legitimacy.

| Before | activated | After | Exact update witness |
| --- | --- | --- | --- |
| `110101` | \(0\), BR | `010101` | own payoff \(4\to8\) |
| `010101` | \(4\), I | `010111` | unique winning neighbor \(1\), payoff \(10\), plays \(A\) |
| `010111` | \(1\), I | `000111` | unique winning neighbor \(0\), payoff \(2\), plays \(B\) |
| `000111` | \(2\), BR | `001111` | own payoff \(-12\to2\) |
| `001111` | \(3\), I | `001011` | unique winning neighbor \(1\), payoff \(13\), plays \(B\) |
| `001011` | \(0\), BR | `101011` | own payoff \(2\to6\) |
| `101011` | \(4\), I | `101001` | unique winning neighbor \(1\), payoff \(13\), plays \(B\) |
| `101001` | \(1\), I | `111001` | unique winning neighbor \(0\), payoff \(4\), plays \(A\) |
| `111001` | \(2\), BR | `110001` | own payoff \(-5\to-3\) |
| `110001` | \(3\), I | `110101` | unique winning neighbor \(1\), payoff \(10\), plays \(A\) |

The numerical witnesses are computed from the specified payoff matrices and neighbors. In each imitation row, the listed maximum is attained uniquely among the active vertex's neighbors; its winning neighbor's current action is the indicated new bit. In each BR row, the alternative utility is strictly higher. Thus each transition follows exactly from the rules and all ten updates change the state. The last state is the first.

At the first state `110101`, vertex \(5\) already plays \(A\), and both its neighbors \(0\) and \(3\) play \(A\); its imitation update therefore leaves it at \(A\). Consequently the **repeating eleven-activation word**
\[
(5,0,4,1,2,3,0,4,1,2,3)
\]
returns the system to `110101` after each period and activates **all six** vertices at least once per period. It is a persistent, even uniformly recurrent, activation sequence with infinitely many actual state switches; the state never reaches an equilibrium. A real-valued potential that strictly decreases on *every* effective update would give a strict inequality after one full state cycle, impossible because the first and last states coincide. This proves the theorem.

## Verification

Run the standalone standard-library program `verify_cycle.py` with Python 3. The checker recomputes all utilities as integers from the edge set and payoff rows; tests all coordination inequalities; checks each of the ten state transitions and each imitator's unique payoff-maximizing neighbor; verifies strict BR improvements; and iterates the full eleven-activation word three times. Its expected output is:

```text
PASS: strict 10-switch orbit, fair 11-activation periodic schedule; exact integers
```

This is a complete finite certificate of the existential claim, not extrapolation from simulation. Both the entire graph and every transition are specified and independently checkable by hand.

## Relationship to prior work

Hasheminejad and Ramazi (2023), arXiv:2306.03243, equations (1)–(3), analyze exactly these payoff and asynchronous update conventions. Their introduction explicitly asks whether a persistent activation sequence can prevent equilibration for a mixed population, and they establish unconditional convergence for particular paths, cycles, starlike graphs and sparse trees. The displayed connected graph has overlapping triangles and is not covered by the sparse-tree and other listed graph theorems. The present finite witness answers their **general-graph deterministic existence question negatively**, without altering their positive results.

Sakhaei, Maleki and Ramazi (2022), arXiv:2201.04185, prove **almost-sure** equilibration for coordinating populations under random activation. Almost-sure convergence does not prohibit exceptional fair deterministic schedules. The fully imitative convergence theorem of Ramazi, Riehl and Cao (2022) likewise does not cover a network with two best responders. These results therefore do not imply the nonexistence of the present periodic orbit. A literature and mathematical-record comparison did not identify an already published identical payoff-and-activation certificate, but cannot establish global novelty.

## Limitations

The certificate asserts **existence**, not minimum graph order, minimum switching period, prevalence under random activation, or failure of all possible activation sequences. It applies to neighbor-only imitation of the most successful adjacent agent **even if that agent's payoff is below the imitator's own**; an imitation rule requiring a strict payoff improvement over the imitator's own payoff is a different model and is not covered. The counterexample disproves a strictly monotone potential on the entire unconstrained connected-graph class, not graph-class-specific potentials or guarantees of almost-sure convergence. Equivalent unindexed constructions and later literature remain an originality risk. No independent mathematical audit has yet been performed.

## References

1. N. Hasheminejad and P. Ramazi, *Equilibration of Coordinating Imitation and Best-Response Dynamics*, arXiv:2306.03243 (first posted 2023-06-05), https://arxiv.org/abs/2306.03243 .
2. N. Sakhaei, Z. Maleki and P. Ramazi, *Equilibration Analysis and Control of Coordinating Decision-Making Populations*, arXiv:2201.04185 (2022), https://arxiv.org/abs/2201.04185 .
3. P. Ramazi, J. Riehl and M. Cao, *The lower convergence tendency of imitators compared to best responders*, Automatica 139 (2022), 110185, https://doi.org/10.1016/j.automatica.2022.110185 .
