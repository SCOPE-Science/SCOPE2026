# Rigidity and two resonance periods for perfect matching cuts at Petersen steps \(4\)–\(7\)

## Finding
For integers \(4\le k\le7\) and \(n\ge2k+1\), let \(P(n,k)\) be the simple generalized Petersen graph with distinct vertices \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+k}\). A **perfect matching cut** is the set of all edges crossing a nontrivial vertex bipartition when those edges form a perfect matching; unordered partitions and their edge-cut sets are counted once.

**Theorem.** The number \(c_k(n)\) of perfect matching cuts is exactly
\[
\begin{aligned}
c_4(n)&=1,\\
c_5(n)&=1+2\mathbf1_{4\mid n},\\
c_6(n)&=1,\\
c_7(n)&=1+2\mathbf1_{4\mid n}+5\mathbf1_{5\mid n}.
\end{aligned}
\]
These formulas hold for every admissible \(n\), without a large-order qualification. Every cut is in one of the following three explicitly classified families:

- **Spoke cut:** all \(n\) spokes cross, occurring once for every \(k\).
- **Period-four cuts:** if \(k\in\{5,7\}\) and \(4\mid n\), the selected rim-transition words alternate \(1010\ldots\) and \(0101\ldots\). They give two cuts, neither containing any crossing spoke.
- **Period-five cuts:** if \(k=7\) and \(5\mid n\), the transition words are the five cyclic shifts of \((10100)^{n/5}\). They give five cuts, each containing exactly \(n/5\) crossing spokes.

In particular, the two even inner jumps \(4\) and \(6\) are rigid, while both resonances coexist at jump \(7\), giving eight cuts when \(20\mid n\). This is a single structural classification, not merely a decision algorithm for existence.

## Assumptions and scope
Every index is reduced modulo \(n\). The condition \(n>2k\) ensures that the three families of edges give an ordinary connected cubic graph. Since the graph is connected, its crossing edge set determines the associated bipartition uniquely up to exchange of its shores. It is crucial that the entire set of edges *across the cut* is a perfect matching; perfect matchings whose deletion merely disconnects the graph are not counted unless they themselves form the cut.

Set \(a_i\in\{0,1\}\) and \(b_i\in\{0,1\}\) for the two shore colors at \(u_i,v_i\), respectively. Let \(\oplus\) denote binary XOR, and introduce the rim-transition bits \(t_i=a_i\oplus a_{i+1}\). The transition word is cyclic of length \(n\). Its parity is even, \(\sum_i t_i\equiv0\pmod2\), because the \(a_i\) form a closed word.

## Proof
**Step 1: the outer rim forces the entire partition.** Write \(d_i=a_i\oplus b_i\). Exactly one cross-cut neighbor at outer vertex \(u_i\) means
\[
t_{i-1}+t_i+d_i=1.
\tag{1}
\]
The addition here is ordinary addition of nonnegative integers, not XOR. Thus no two consecutive \(t\)-bits can both be one, and the spoke difference is forced:
\[
d_i=1-t_{i-1}-t_i,\qquad b_i=a_i\oplus d_i.
\tag{2}
\]
Given an even-parity cyclic \(t\)-word with no adjacent ones, choose \(a_0=0\), recover successively \(a_{i+1}=a_i\oplus t_i\), then recover \(b_i\) from (2). The only other coloring with the same transitions is the simultaneous complement. Thus each valid \(t\)-word gives exactly one unordered cut and different \(t\)-words give different cuts.

**Step 2: the inner rim becomes an exact local constraint.** Put
\[
s_i=b_i\oplus b_{i+k}
=\left(\bigoplus_{j=i}^{i+k-1}t_j\right)\oplus d_i\oplus d_{i+k}.
\tag{3}
\]
Exactly one cross-cut neighbor at inner vertex \(v_i\) is equivalent to
\[
s_{i-k}+s_i+d_i=1,
\tag{4}
\]
again with ordinary integer addition. Equations (1)–(4), with even parity of \(t\), are both necessary and sufficient for a perfect matching cut. In particular, no unidentified choices of the inner colors remain.

**Step 3: an exhaustive finite-state lemma.** Fix \(k\). For a binary window \(w\) of length \(2k+2\), index its bits as \(t_{-k-1},\ldots,t_k\). Define \(d_j\) for \(j\in\{-k,0,k\}\) by (2). Admit \(w\) exactly when these three \(d\)-values belong to \(\{0,1\}\) and (3)–(4) hold at the central index zero. Draw an arc from the first \(2k+1\) bits of \(w\) to its last \(2k+1\) bits. In integer notation, with the earliest bit least significant, this is the arc
\[
w\bmod 2^{2k+1}\ \longrightarrow\ \lfloor w/2\rfloor.
\tag{5}
\]
Every length-\(n\) cyclic transition word satisfying the local equations corresponds to a length-\(n\) closed directed walk in (5), and conversely. This remains valid when windows wrap more than once: overlap forces every coordinate of the periodic word consistently. The separate even-parity condition is then imposed on the word.

The exact strongly connected components containing directed cycles are given by the following complete finite certificate; the other states cannot occur in any closed walk.

| Step \(k\) | Admitted windows/arcs | States incident to arcs | Recurrent directed-cycle lengths | Minimum integer state in each cycle |
|---|---:|---:|---|---|
| 4 | 180 | 280 | 1 | 0 |
| 5 | 720 | 1120 | 1, 2 | 0, 682 |
| 6 | 2880 | 4480 | 1 | 0 |
| 7 | 11520 | 17920 | 1, 2, 5 | 0, 10922, 5285 |

Here “recurrent” refers precisely to a strongly connected component containing a positive-length directed cycle; *each* listed component is an induced directed cycle with every member having one predecessor and one successor inside that component. The entire computation is reconstructed from (2)–(5), without external data, by `certify_transfer.py` (Tarjan components and complete within-component degree checks); its complete observed output is in `transfer_output.txt`. There are \(2^{2k+2}\) candidate windows for each specified step, all directly checked. No claim about large \(n\) rests on the finite-size graph experiments: the finite-state reduction is exact for every \(n\).

**Step 4: parity and counting.** The loop at state zero is the all-zero transition word, yielding the spoke cut. Each listed two-cycle is the alternating transition word; it can close at length \(n\) only when \(2\mid n\), and its number \(n/2\) of ones is even precisely when \(4\mid n\). Its two root phases give two distinct cuts. The five-cycle for \(k=7\) is generated by the five shifts of \(10100\): each period contributes two transitions, so even parity holds automatically whenever \(5\mid n\). These five root phases give five distinct cuts. There are no other recurrent components and hence no other admissible cut transition words. Summing the three disjoint types gives the theorem.

## Verification
`certify_transfer.py` independently generates all local transition windows, constructs the directed graph, runs Tarjan's algorithm, and verifies that the recurrent components have precisely the claimed cycle lengths and internal degrees. `verify_direct.py` does *not* use this automaton: it enumerates independent cyclic outer transition sets of even parity, reconstructs vertex shore colors, and directly checks the original six neighbor comparisons per column on each graph, for every \(n\) from \(2k+1\) through \(24\), and every \(k\in\{4,5,6,7\}\). Their observed outputs are `transfer_output.txt` and `direct_output.txt`. Execute with Python 3 by running `python3 certify_transfer.py` and `python3 verify_direct.py` in the directory containing these standalone files. All code and outputs are included unchanged in the accompanying package.

## Relationship to prior work
Le and Telle's full 2021 paper [2] formalizes perfect matching cuts, distinguishes them from merely disconnecting perfect matchings, and explicitly identifies counting/enumeration as a research direction. Its complexity and recognition theorems do not imply the formulas above. Dudek's 2014 paper [1] studies the spectral gap of all \(P(n,k)\); the earlier Naz et al. 2014 article [3] studies metric dimension of \(P(n,4)\). These invariants do not determine perfect matching cuts.

Two earlier exact special-family classifications [4,5] give the corresponding formulas for jumps two and three: \(1+5\mathbf1_{5\mid n}\) and \(1+2\mathbf1_{4\mid n}+5\mathbf1_{5\mid n}\), respectively. Their displayed proofs and complete claims were inspected. They do not quantify over jumps four through seven, although isolated small graphs may be isomorphic under the usual inverse-jump symmetry (for example \(P(16,5)\cong P(16,3)\) and \(P(20,7)\cong P(20,3)\)). Such individual instances are not asserted as novel. The present assertion covers every admissible order at four new fixed jumps, and proves the disappearance and reappearance of the two periods. The full 2024 study [6] develops general recognition complexity and a bounded-treewidth algorithm, not an all-order enumeration of these graphs.

## Limitations
The theorem does not assert a corresponding formula for arbitrary \(k\ge8\). Its finite-state cyclic-core classification is computer-assisted but exhaustive with executable source and explicit stated search space; it is not a purely handwritten analysis of all those windows. Direct graph tests cover only finite orders and are corroboration, not the proof of the infinite-order claim. Earlier literature not indexed or inaccessible may contain stronger statements. No independent scholarly audit has been performed.

## References
[1] A. Dudek, *On the Spectrum of the Generalised Petersen Graphs*, arXiv:1412.3531, first posted 2014-12-11, https://arxiv.org/abs/1412.3531.

[2] V. B. Le and J. A. Telle, *The Perfect Matching Cut Problem Revisited*, arXiv:2107.06399, first posted 2021-07-13, https://arxiv.org/abs/2107.06399.

[3] S. Naz, M. Salman, U. Ali, I. Javaid, S. A.-u.-H. Bokhary, *On the Constant Metric Dimension of Generalized Petersen Graphs P(n,4)*, Acta Mathematica Sinica 30 (2014), 1145–1160, published online 2014-06-15, https://doi.org/10.1007/s10114-014-2372-8.

[4] *All perfect matching cuts of generalized Petersen graphs with second jump two*, publicly accessible mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-all-perfect-matching-cuts-of-generalized-petersen-graphs-with-se--07ff361ad99e/RESULT.md.

[5] *Perfect matching cuts of P(n,3): two nonspoke resonance periods*, publicly accessible mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-perfect-matching-cuts-of-p-n-3-two-nonspoke-resonance-periods--71466def2f69/RESULT.md.

[6] V. Bouquet and C. Picouleau, *The complexity of the perfect matching-cut problem*, Journal of Graph Theory 108 (2025), 432–462, first online 2024-10-06, https://doi.org/10.1002/jgt.23167.
