# The six-seat boundary for cycling swaps in cyclic three-class preferences

## Finding
Consider the standard exchange-stable seating game on a cycle with three homogeneous agent types. Agents of type \(i\in\{0,1,2\}\) value each adjacent agent of type \(i+1\pmod 3\) at \(1\), and all other neighbors at \(0\). A permitted exchange swaps two occupied seats only when **both participating agents strictly gain utility**.

**Theorem (sharp first cycle and complete first-layer census).** Among all such games on cyclic tables with \(3\le n\le6\) seats, an improvement cycle exists if and only if \(n=6\) and each type occurs exactly twice. The full directed improvement graph for \(n=6\), with all \(3^6=729\) type words included, has exactly six nontrivial strongly connected components. Each consists of six type words and exactly six internal directed edges (one directed six-cycle). Their union comprises \(36\) type words, all obtained from \((0,0,1,2,1,2)\) by seat rotations, seat reversal, and cyclic renaming of types. Every such word has utilitarian welfare \(5\), whereas the seating \((0,1,2,0,1,2)\) has welfare \(6\) and is stable. This exact boundary concerns *existence of a cyclic improvement sequence*, not nonexistence of stable arrangements or failure of every improvement path to terminate.

## Assumptions and scope
Seats are the distinct vertices \(0,\ldots,n-1\) of the simple cycle \(C_n\), with \(n\ge3\). Each seat contains one agent, and the only relevant agent attribute is a type in \(\{0,1,2\}\). All agents of a type have identical, nonnegative binary valuations. For a type word \(s\) and seat \(j\), define the current occupant's utility
\[
u_j(s)=[s_{j-1}=s_j+1\pmod 3]+[s_{j+1}=s_j+1\pmod 3],
\]
where seat indices are modulo \(n\) and brackets indicate \(0\)-\(1\) truth values. A directed edge \(s\to t\) exists when \(t\) is obtained by exchanging the occupants of distinct seats \(i,j\), and both original agents strictly improve: \(u_i(t)>u_j(s)\) and \(u_j(t)>u_i(s)\). Exchanges of equal types have no effect and cannot be strict. A *nontrivial strongly connected component* (SCC) contains at least two distinct type words. The finite claim classifies all type multisets for \(3\le n\le6\); it does not claim a census for \(n>6\). The underlying agents can also be individually labeled: the exhibited cyclic type moves lift to an infinite improving trajectory of labeled agents because their finite within-type permutation after a complete type-word circuit has finite order.

## Proof
First construct the entire finite directed graph exactly, rather than sampling it. For each integer \(n\in\{3,4,5,6\}\), enumerate the \(3^n\) words of length \(n\). For each word enumerate every unordered pair of distinct positions \(0\le i<j<n\), swap its entries, and test the two strict inequalities in the assumptions with integer comparisons. This covers *all* configurations, *all* type-multiplicity choices, and *all* feasible exchanges. Compute SCCs by the explicitly supplied Tarjan depth-first-search implementation in `verify.py`, and check the SCC partition by assertions. The certified totals are:

| \(n\) | Number of words | Directed exchange edges | Nontrivial SCCs | Their sizes |
|---|---:|---:|---:|---|
| 3 | 27 | 0 | 0 | none |
| 4 | 81 | 24 | 0 | none |
| 5 | 243 | 180 | 0 | none |
| 6 | 729 | 882 | 6 | six components, each of size \(6\) |

The verifier also proves that each of the six SCCs has exactly six internal edges, that the \(36\) vertices have type counts \((2,2,2)\), and that these are precisely the \(36\) words in the dihedral-seat / cyclic-type orbit of \((0,0,1,2,1,2)\). No SCC for \(n\le5\) contains a directed cycle; in a finite directed graph, a nonconstant directed cycle necessarily lies in a nontrivial SCC. Thus cycling is impossible before six seats, and at six seats it can occur only at multiplicities \((2,2,2)\).

For an independently readable explicit witness, begin with
\[
(2,2,0,1,0,1).
\]
Using zero-based seat indices, perform the following six mutual improvements, in order:
\[
(0,3),\quad(2,5),\quad(1,4),\quad(0,3),\quad(2,5),\quad(1,4).
\]
The consecutive type words are
\[
\begin{aligned}
&(2,2,0,1,0,1)\to(1,2,0,2,0,1)\to(1,2,1,2,0,0)\\
&\to(1,0,1,2,2,0)\to(2,0,1,1,2,0)\\
&\to(2,0,0,1,2,1)\to(2,2,0,1,0,1).
\end{aligned}
\]
The respective ordered gains of the two moving agents are \((1,2),(2,1),(2,1),(2,1),(1,2),(1,2)\), strictly positive in each coordinate. The six states are distinct before the return. Each has welfare \(5\), i.e. five unlike-type adjacent seat pairs. The contrasting word \((0,1,2,0,1,2)\) has six unlike-type pairs, total welfare \(6\), and no improving exchange. The stated cycle and exhaustive SCC census together prove the theorem. \(\square\)

## Verification
Run `python3 verify.py` in the same directory using Python 3 and its standard library. The code enumerates every type word and every pair of exchange positions for \(3\le n\le6\), forms exact integer utility comparisons, identifies SCCs with Tarjan's algorithm, validates the six-state witness step by step, checks all stated counts and orbit identities, and prints `VERIFIED` only when all assertions pass. This is a *finite exhaustive certificate*, not a numerical sample or an unsupported extrapolation to larger cycles. A separate exploratory graph implementation using a different SCC library agreed on all four orders and six six-word SCCs; that alternative library is not required to reproduce the package.

## Relationship to prior work
Berriaud, Constantinescu and Wattenhofer (2023) introduce the seating-game formulation and prove in Theorem 6.6 that **every** three-class binary-preference game on a cyclic table admits a stable arrangement. Their Lemma 10 addresses exactly the cyclic three-class preference pattern considered here: it shows that a welfare-maximizing seating is stable, and its proof considers swaps that sometimes preserve welfare. This theorem retains their stability result in full. Its narrower **dynamic** question is whether *arbitrary successive strictly mutually beneficial exchanges* terminate, and, at the first failing order, how the entire directed improvement graph decomposes. The previously proved existence of a stable seating and characterization of welfare-maximizers do not imply that every improvement trajectory converges. Their four-agent nonconvergence example is on a **path** with a different preference profile; it does not give this exact six-seat cyclic-three-class boundary and SCC census.

Ceylan, Chen and Roy (2023) primarily analyze computational complexity of computing optimal, envy-free, or exchange-stable seatings on graph families. Their theorem statements concern decision/optimization problems, rather than this minimal cyclic-improvement transition. Searches of relevant published mathematical records and articles identified no equivalent six-seat directed-component classification; absence in accessible sources cannot establish publication priority.

## Limitations
The proof gives a complete exact classification only through six seats, with arbitrary type counts at those sizes. It does **not** assert that larger games always or never cycle. The six nontrivial SCCs have outgoing improving edges leading to other words: they are not closed/absorbing recurrent classes, and some improving choices terminate. The finite class-word quotient does not by itself return individual agent labels after one circuit; repeating the circuit a finite number of times does. Novelty relative to unindexed or inaccessible equivalent work remains an uncertainty. No independent external audit has been performed.

## References
- D. Berriaud, A. Constantinescu, and R. Wattenhofer, *Stable Dinner Party Seating Arrangements*, arXiv:2305.09549, first public 2023-05-16. https://arxiv.org/abs/2305.09549
- E. Ceylan, J. Chen, and S. Roy, *Optimal Seat Arrangement: What Are the Hard and Easy Cases?*, IJCAI 2023, DOI:10.24963/ijcai.2023/285. https://www.ijcai.org/proceedings/2023/285
