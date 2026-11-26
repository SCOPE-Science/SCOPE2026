# Bounded, topology-dependent Nash spectra for binary public-goods ladders

## Finding

Consider a strict, homogeneous binary public-goods game: each vertex chooses whether to produce a public good, and its unique preferred action is production when the number of producing neighbors is **even**, and nonproduction when that number is odd. On graphs of maximum degree three this means exactly \(T(0)=T(2)=1\) and \(T(1)=T(3)=0\). All equilibria below are pure Nash equilibria in the sense of this response rule.

Write \(L_n=P_n\square K_2\) for the ordinary open ladder with \(n\ge2\) rungs; \(C_n\square K_2\) for the cylindrical ladder with \(n\ge3\) rungs; and \(M_n\) for the Möbius ladder with \(n\ge3\), obtained by connecting the two open ends of \(L_n\) with **crossed** horizontal edges. The \(2n\) vertices are labeled by their rung number and their row. Denote the number of distinct labeled equilibria on a graph \(G\) by \(E(G)\).

**Theorem.** The complete equilibrium census depends only on the number of rungs modulo four:

| Graph | \(n\equiv0\pmod4\) | \(n\equiv1\pmod4\) | \(n\equiv2\pmod4\) | \(n\equiv3\pmod4\) |
|:--|--:|--:|--:|--:|
| Open \(L_n\) | 1 | 2 | 1 | 4 |
| Cylinder \(C_n\square K_2\) | 16 | 2 | 4 | 2 |
| Möbius \(M_n\) | 4 | 2 | 8 | 2 |

More strongly, **every** equilibrium configuration is obtained by restricting a four-periodic sequence of two-bit rung states satisfying the appropriate open, periodic, or twisted-periodic boundary condition. Hence none of these graph families exhibits unbounded growth of the number of equilibria as \(n\to\infty\).

## Assumptions and scope

Graphs are finite, simple, undirected, and unweighted. Each vertex has one of two actions, labeled \(0\) or \(1\), and the stated parity response is its unique best response, with no indifference. The ordinary ladder has endpoint vertices of degree two; both closed ladders have degree three. No claims are made about best-response dynamics, mixed equilibria, or arbitrary high-degree graphs.

For rung \(i\), write its two actions as the column \(z_i=(a_i,b_i)\in\mathbb F_2^2\). Let \(e=(1,1)\), \(u_i=a_i+b_i\in\mathbb F_2\), and let \(S(a,b)=(b,a)\) exchange rows. Sums in the proof take place in \(\mathbb F_2\).

## Proof

**Local parity and a four-periodic recurrence.** Because the preferred action is \(1\) at an even neighboring count and \(0\) at an odd one, the best-response equation for every vertex \(v\) is
\[
 x_v+\sum_{w\sim v}x_w=1\quad\text{in }\mathbb F_2.
\]
At an interior rung, the top and bottom vertex equations become
\[
 a_{i-1}+a_i+a_{i+1}+b_i=1,\qquad
 b_{i-1}+b_i+b_{i+1}+a_i=1.
\]
Consequently
\[
 z_{i+1}=z_{i-1}+(1+u_i)e,\qquad u_{i+1}=u_{i-1}.
\]
Any initial adjacent pair \((z_0,z_1)\in(\mathbb F_2^2)^2\) determines a unique doubly infinite sequence. In particular,
\[
 z_2=z_0+(1+u_1)e,\quad
 z_3=z_1+(1+u_0)e,\quad
 z_4=z_0,\quad z_5=z_1.
\]
Thus **every sequence has period dividing four**, with exactly sixteen possible initial ordered pairs. The boundary conditions below are both necessary and sufficient for this sequence to give a Nash equilibrium, so an exact finite check is an exhaustive proof for all \(n\), not a numerical sample.

**Open ladder.** Encode the missing horizontal neighbors at each end by two zero-valued ghost rungs. The conditions are \(z_0=0\) and \(z_{n+1}=0\). There are four possible initial \(z_1\). According to whether \(n\bmod4\) is \(0,1,2,3\), the right boundary requires respectively \(z_1=0\), \(u_1=1\), \(z_1=e\), or no additional constraint. These admit respectively \(1,2,1,4\) initial states.

**Cylindrical ladder.** Periodicity of the two rows gives \(z_n=z_0\) and \(z_{n+1}=z_1\). At residues \(0,1,2,3\) the four-periodic recurrence permits, respectively: all sixteen initial ordered pairs; the two constant profiles \(z_i=(0,1)\) or \((1,0)\); the four pairs with \(u_0=u_1=1\); and again the two constant profiles. The counts are \(16,2,4,2\).

**Möbius ladder.** Crossing the end connections gives \(z_n=Sz_0\) and \(z_{n+1}=Sz_1\). The elementary identity \(Sz=z+u(z)e\), where \(u(z)\) is the sum of the two bits, reduces the four residue classes to:

- \(n\equiv0\pmod4\): \(u_0=u_1=0\), giving \(4\) pairs;
- \(n\equiv1\pmod4\): \(u_0=1\), \(z_1=Sz_0\), giving \(2\) pairs;
- \(n\equiv2\pmod4\): \(u_0+u_1=1\), giving \(8\) pairs;
- \(n\equiv3\pmod4\): \(u_0=1\), \(z_1=z_0+e\), giving \(2\) pairs.

Each pair counted determines exactly one labeled action vector and satisfies every vertex's strict best response. There are no others. This proves the theorem. \(\square\)

## Verification

The self-contained Python program `verify.py` checks the four-periodic recurrence exhaustively over all sixteen two-column initial states, for each of the three topologies and every permitted \(n\) through \(100\). Separately it builds each graph's adjacency list and **independently** enumerates all \(2^{2n}\) binary strategy profiles through \(n=8\), testing every vertex's actual best-response condition. All checks agree with the theorem. The proof above, rather than the finite computation, establishes the infinite-family result.

## Relationship to prior work

Gilboa and Nisan (2022) explicitly identify the parity-alternating best-response pattern as a tractable linear system over \(\mathbb F_2\). Klimm and Stahlberg (2023) cite that polynomial-time decision result while studying more general strict public-goods response patterns. **Neither is claimed to have discovered the parity reduction here.** The additional result is the uniform, explicit, topology-sensitive complete equilibrium count and four-periodicity of the three width-two network families, including twisted endpoint identification. Sánchez Muñoz and Mc Gettrick (2021) count equilibria on ordinary and circular ladders for an additive pairwise anti-coordination payoff game, finding exponential growth; their utility functions are distinct from the nonmonotone parity public-goods response considered here, so their count does not imply this one.

## Limitations

The graph family has fixed width two and the response rule is exactly the parity-alternating pattern; no claim is made for the superficially similar but *nonparity* rule \(T(0)=T(2)=1\) on vertices having degree four or greater. The exact counts are profile counts for labeled vertices, not orbit counts modulo graph automorphisms. They do not imply best-response convergence or welfare guarantees. General linear-algebraic tractability of parity-response games is already known, and the remaining novelty claim is restricted to the explicit ladder-family census and structural periodicity. An equivalent enumeration in unindexed literature cannot be ruled out.

## References

1. V. Sánchez Muñoz and M. Mc Gettrick, *Nash Equilibria in certain two-choice multi-player games played on the ladder graph*, 2021, arXiv:2101.09103, https://arxiv.org/abs/2101.09103 .
2. M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs*, 2022, arXiv:2207.04238, https://arxiv.org/abs/2207.04238 .
3. M. Klimm and M. J. Stahlberg, *Complexity of Equilibria in Binary Public Goods Games on Undirected Graphs*, 2023, arXiv:2301.11849, https://arxiv.org/abs/2301.11849 .
