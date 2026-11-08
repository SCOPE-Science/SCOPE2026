# A one-edge restoration threshold for minority traps in matching-deleted bicliques

## Finding

For integers \(n\ge3\) and \(0\le t\le n\), define the labelled bipartite graph
\[
G_{n,t}=K_{n,n}\setminus\{L_iR_i:1\le i\le t\},
\]
with shores \(L_1,\ldots,L_n\) and \(R_1,\ldots,R_n\). At each discrete time, choose one of the \(2n\) vertices uniformly, and set its binary spin to the minority value in its **closed neighborhood**, retaining its spin if the two values tie. Let \(R_{n,t}\) be the number of recurrent spin configurations, and \(K_{n,t}\) the number of closed communicating classes of this finite Markov chain.

**Theorem.** Every recurrent class is a singleton absorbing configuration, every initial state is absorbed almost surely, and
\[
\boxed{R_{n,t}=K_{n,t}=2+\mathbf1_{\{n\text{ even},\,t=n\}}\binom{n}{n/2}.}
\]
The binomial term is understood to occur only when \(n\) is even. The two absorbing states always present are the proper bipartite 2-colorings. For even \(n\ge4\) and \(t=n\), the other \(\binom{n}{n/2}\) configurations are exactly those satisfying \(s(L_i)=s(R_i)\) for every \(i\), with exactly \(n/2\) indices in state one. Each such state cuts precisely \(n^2/2\) of the \(n(n-1)\) edges; the two proper colorings cut all edges. In particular, restoring **one** missing matching edge to \(G_{n,n}\) removes every suboptimal recurrent configuration, for every even \(n\ge4\).

For even \(n\to\infty\), the number of nonoptimal absorbing states is asymptotic to \(2^n\sqrt{2/(\pi n)}\); their cut-to-optimum ratio is exactly \(n/(2(n-1))\to1/2\). Thus the recurrent-state entropy per graph vertex is \((\log 2)/2\) for the fully deleted matching and zero for any proper deleted submatching, including \(t=n-1\).

## Assumptions and scope

The graph is simple, unweighted, undirected and labelled. The deleted edges form a matching: no two share an endpoint. The update is single-site and asynchronous, with every vertex selected with positive probability (uniform selection is imposed for definiteness). The vertex itself participates in the minority vote, and a tie **preserves** the current bit. Spin configurations are labelled, not counted modulo color complement or graph automorphisms. Recurrent classes are closed communicating classes of the Markov chain; self-loops arising from inactive selections are included. The result concerns the exact zero-noise rule, not noisy Glauber dynamics, synchronous updates, or the open-neighborhood rule.

## Proof

**1. Bipartite conjugacy.** Define dual bits \(u_i=s(L_i)\) and \(v_i=1-s(R_i)\). An original agreeing edge becomes a dual disagreeing edge. If a dual vertex has \(d\) neighbors and \(h\) of them have bit one, its induced update chooses their strict majority, and **flips its own bit when \(h=d/2\)**. This follows directly from the original closed-neighborhood minority condition: a vertex with \(S\) same-colored open neighbors flips precisely when \(2(S+1)>d+1\), equivalent for integer \(S\) to \(2S\ge d\). Since original agreement across an edge means dual disagreement, the dual process is the asserted majority rule with tie-flip. In particular, the dual polarized configurations (all bits zero or all bits one) are absorbing and correspond to the two original proper 2-colorings.

Put \(a=\sum_i u_i\) and \(b=\sum_i v_i\). At a vertex with index \(i\le t\), the opposite shore has one excluded neighbor, so its degree is \(n-1\) and the number of adjacent ones is \(b-v_i\) on the left (or \(a-u_i\) on the right). At indices \(i>t\), the vertex degree is \(n\), and its number of adjacent ones is \(b\) or \(a\), respectively.

**2. All cases except complete matching deletion at even size.** First let \(n=2k+1\) be odd. If \(b\ge k+1\), then every dual left zero can be changed to one: for an undeleted index its \(2k+1\) neighbors contain a strict majority of ones, while at a deleted index the \(2k\) neighbors contain at least \(b-v_i\ge k\) ones, so either a strict majority or a tie-flip changes zero to one. Update all left zeros, then all right zeros; this yields the all-one dual configuration. If \(b\le k\), the symmetric argument changes all left ones to zero and then all right ones, yielding all zero. Thus for **every** initial dual configuration with odd \(n\) there is a finite permitted update path to an absorbing polarized state, for each \(t\).

Now let \(n=2k\) and \(t<n\). If \(b\ge k+1\), every left zero can change to one (a deleted-index vertex sees at least \(k\) ones among \(2k-1\) neighbors, and an undeleted-index vertex sees more than \(k\) among \(2k\)); after changing all left zeros, change all right zeros to reach all one. If \(b\le k-1\), symmetrically reach all zero. When \(b=k\), the same argument applied in the **right** shore reaches polarization whenever \(a\ne k\). The sole remaining case is \(a=b=k\). Because \(t<n\), choose an undeleted left vertex \(i>t\). It sees exactly \(k\) ones among its \(2k\) neighbors, so selecting it flips its bit. This changes \(a\) to \(k+1\) or \(k-1\), and the preceding right-shore argument reaches polarization. Therefore every state has a path to one of the two absorbing states when \(n\) is odd or \(t<n\).

In a finite Markov chain, a closed communicating class containing a state from which an absorbing state is reachable must itself be that absorbing state. Hence the only recurrent classes in these cases are the two polarized singletons. Since the state space is finite and these are its only closed classes, absorption occurs almost surely.

**3. Fully deleted perfect matching at even size.** Now let \(n=2k\ge4\) and \(t=n\). All vertices have odd degree \(2k-1\), so there are no neutral spin flips in the dual majority dynamics. Every actual flip strictly reduces the number of disagreeing dual edges, equivalently strictly raises the original cut size. Therefore the recurrent states are exactly the absorbing states.

We classify these states. In a dual absorbing state, a left one at index \(i\) requires \(b-v_i\ge k\), while a left zero requires \(b-v_i\le k-1\). If the left shore contains both zero and one, these two requirements force \(b=k\), and moreover \(v_i=1-u_i\) at every index. Consequently \(a=k\), and the right-shore conditions hold as well. Conversely, every dual configuration with \(a=b=k\) and \(v_i=1-u_i\) is absorbing. There are \(\binom{n}{k}\) such configurations. If the left shore is unanimous, each right vertex necessarily takes the same dual value for stability, giving just the dual all-zero and all-one configurations. Thus there are exactly \(2+\binom{n}{k}\) absorbing states, each a separate recurrent class. Since every nonabsorbing flip strictly increases cut size in this case, every trajectory eventually freezes almost surely.

**4. Cut sizes and asymptotics.** Returning to original bits, the \(\binom{n}{k}\) additional dual configurations have \(s(L_i)=s(R_i)\) and exactly \(k\) ones in each shore. There are \(2k(n-k)=n^2/2\) cross-color edges in the full biclique, and the deleted diagonal edges are monochromatic, so this is still the cut size in \(G_{n,n}\). Proper bipartite colorings cut all \(n(n-1)\) edges. Central-binomial asymptotics \(\binom{2k}{k}\sim4^k/\sqrt{\pi k}\) give the asserted count, ratio and entropy per \(2n\) vertices. All claims follow. \(\square\)

## Verification

Run `python3 verify_transitions.py` and `python3 verify_equilibria.py` in a directory containing the two standalone scripts. The transition-graph program constructs all one-site updates and computes terminal strongly connected components without external dependencies. It checks all \(22\) graphs with \(3\le n\le6\), \(0\le t\le n\), totaling \(36,352\) state-space vertices; every closed class is a singleton and all class populations match the theorem. The independent checker directly evaluates each vertex's closed-neighborhood minority stability inequalities for all \(39\) graphs with \(3\le n\le8\), totaling \(757,248\) configurations; it also checks the suboptimal cut sizes. Exact standard-output captures are included. These finite tests are supplementary: the infinite-family theorem rests on the preceding proof.

## Relationship to prior work

Rouquier, Regnault and Thierry introduced and analyzed the same stochastic minority rule, its energy monotonicity and a dual-majority representation on bipartite graphs; their article treats cliques, paths, cycles, trees and general bipartite reachability methods. Its accessible text does not supply the matching-deletion threshold and exact recurrent-class enumeration proved here. Lampis studies minimum locally stable cuts and their computational complexity on general graphs. That work supplies the local Max-Cut/Nash equilibrium motivation and general worst-case comparison but no special classification of the present graph family. The statement here is also expressible as a tie-sensitive absorbing-state result for the dual asynchronous majority rule, or as the exact count of fixed 1-flip stable cuts when all vertex degrees are odd. The central binomial coefficient is a classical sequence and its appearance as a number alone is not a novelty claim.

## Limitations

This is a zero-noise finite-state classification. It gives no uniform bounds on absorption times or on the probabilities of absorption into individual traps, and no claim about thermal spin-flip rates. For a proper deleted submatching, ordinary 1-flip **weak** cut local optimality can include tied vertices and thus differs from absorption under the specified tie-flip dual rule. Priority is qualified: the exact matching-deletion threshold was not found in the inspected sources, but an equivalent unindexed construction in local Max-Cut or anti-coordination-game literature cannot be ruled out. Independent scientific validation has not been performed.

## References

1. J.-B. Rouquier, D. Regnault and É. Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119, first made public November 23, 2010. Accessible full text: https://ar5iv.labs.arxiv.org/html/1011.5119.
2. M. Lampis, *Minimum Stable Cut and Treewidth*, ICALP 2021, DOI:10.4230/LIPIcs.ICALP.2021.92, arXiv:2104.13097 (first posted April 27, 2021); https://drops.dagstuhl.de/opus/volltexte/2021/14161/pdf/LIPIcs-ICALP-2021-92.pdf.
