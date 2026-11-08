# Pathwise range inclusion for independent stationary walks on complete bipartite graphs

## Finding

Let \(a,b\ge1\), \(k\ge2\), and let \(t_1,\ldots,t_k\) be arbitrary nonnegative integers. On the complete bipartite graph \(K_{a,b}\), independently start \(k\) non-lazy simple random walks \(X_i\) from stationarity, and let \(Y\) be a single stationary non-lazy simple random walk with \(T=\sum_i t_i\) transitions. There exists a joint coupling satisfying both prescribed walk laws and

\[\mathcal R_Y(T)\subseteq\bigcup_{i=1}^k\mathcal R_{X_i}(t_i)\quad\text{almost surely}.\]

Consequently, the collaborative set stochastically dominates the single-walk set in the inclusion order, not just in cardinality: every increasing function \(f:2^{V(K_{a,b})}\to\mathbb R\) satisfies

\[\mathbb E f\Bigl(\bigcup_i\mathcal R_{X_i}(t_i)\Bigr)\ge\mathbb E f(\mathcal R_Y(T)),\]

provided the expectations exist. No condition on the parity of \(T\) is imposed.

## Assumptions and scope

The graph has two nonempty parts \(A,B\) of orders \(a,b\). Every edge joins different parts. The stationary distribution is uniform in each part, with stationary mass \(1/2\) on each part (even when \(a\ne b\)). Each transition chooses a uniformly random vertex of the opposite part, independently of prior such choices. A trajectory of length \(t\) includes its initial vertex and exactly \(t\) transitions. All \(k\) collaborative trajectories are mutually independent, including starting vertices; the single walk is not required to be independent of them under the coupling.

## Proof

**1. Side-specific coupon representation.** For each collaborating walker \(i\), choose an independent fair starting-side coin \(\sigma_i\). Given the coins, generate all the vertices used by the walkers from two independent families of identically distributed uniform vertex labels, one in \(A\) and one in \(B\), using disjoint draws for different vertex visits. Assign these labels to the walks in any fixed deterministic order of their visits on each side. The labels are independent of the side coins. This represents precisely \(k\) independent stationary non-lazy walks on \(K_{a,b}\).

**2. Count the allocated coupons.** Let \(o\) be the number of odd \(t_i\), and let \(e_A\) and \(e_B\) be the numbers of even \(t_i\) whose starting sides are \(A\) and \(B\), respectively. Since an odd-length walk makes an equal number of visits to each side, while an even-length walk makes one extra visit to its starting side, the joint numbers \(N_A,N_B\) of vertex-label draws satisfy

\[N_A=\frac{T+o}{2}+e_A,\qquad N_B=\frac{T+o}{2}+e_B.\]

The displayed expressions are integers since \(o\) and \(T\) have the same parity. Also \(N_A+N_B=T+k\).

**3. Choose a stationary starting side for the single walk.** If \(T\) is odd, then \(o\ge1\); hence \(N_A,N_B\ge(T+1)/2\). Select the single walk's initial side by an additional fair coin. A length-\(T\) alternating path then needs exactly \((T+1)/2\) labels of each side, which are available from the collaborative pools.

If \(T\) is even, both \(N_A,N_B\ge T/2\), and the sum \(N_A+N_B=T+k\ge T+2\) guarantees \(\max\{N_A,N_B\}\ge T/2+1\). Choose the single walk's starting side to be whichever side has the larger pool; break ties with a fresh fair coin. This choice is itself fair: simultaneously flipping every independent fair \(\sigma_i\) swaps the distribution of \(N_A\) and \(N_B\), and the tie-breaking rule is symmetric. Thus the chosen starting side has exactly the stationary side distribution. The single walk requires \(T/2+1\) labels from its starting side and \(T/2\) from the other, so enough labels are again available.

**4. Include the sampled labels pathwise.** In each part, order the collaborative label draws into a single independent uniform sequence. Generate the single walk by taking the first number of draws required by its alternation pattern from each part's sequence, in their visiting order. The single walk's side choice is independent of both label sequences, so it is a correct stationary random walk. Its labeled range is a subset of the union of collaborative labels, by construction. All collaborative walkers retain their independent joint law because their assigned labels were disjoint independent coordinates. This completes the coupling.

The set-inclusion statement immediately implies stochastic domination for every increasing event on subsets, in particular \(\Pr(|\bigcup_i\mathcal R_{X_i}(t_i)|\ge h)\ge\Pr(|\mathcal R_Y(T)|\ge h)\) for all integers \(h\ge0\).

## Verification

The standalone `checker.py` enumerates all starting-side patterns for \(k\le4\) with \(t_i\le4\), verifying the two side-count inequalities and that the chosen starting side has available draws. It separately computes the exact rational distributions of labeled visited sets for \(1\le a,b\le3\) and \(k=2,3\) with short lengths, and verifies the implied range-size stochastic inequalities without using the coupling construction. The run produced **20,729 exact finite checks passed**. These diagnostics do not replace the all-parameter proof in Steps 1--4.

As one nontrivial illustration, on \(K_{2,3}\) for two independent stationary one-step walkers, the probability of discovering at least three distinct vertices is \(5/6\), compared with \(7/12\) for one stationary two-step walker.

Reproduce with `python checker.py` using Python's standard library alone.

## Relationship to prior work

Dey, Kim and Terlov (2023) prove an expectation inequality for multiple independent stationary walks on general graphs (their Theorem 1.1) and explicitly ask whether the corresponding range-size stochastic domination holds (Question 3.6). Their discussion also leaves the unrestricted-parity discrete-time expectation comparison as Conjecture 3.1. The present statement establishes the stronger labeled-set inclusion for the natural family of *all* complete bipartite graphs and removes the parity restriction in that family. It is not a claim for general graphs.

The complete-graph case has a different independent-uniform-draw structure, with an exact seed-augmentation representation; it does not imply the alternating two-part coupling here. Likewise, fixed-start comparisons of two walks on balanced bicliques do not settle stationary collaboration against a single walk.

## Limitations

The proof relies on complete adjacency between the two parts, uniform simple-walk transitions, and independent stationary starting vertices. It does not establish the same ordering on general bipartite graphs, nonstationary starts, or with side-dependent holding probabilities. The single walk is coupled to the collaborative collection and need not be independent of it. The claim includes no statement about a time-aligned containment of trajectories. Historical-priority assessment is based on accessible primary full text and targeted searches; the 2025 publisher typesetting of the cited paper could not be inspected in full.

## References

1. P. S. Dey, D. Kim and G. Terlov, *Collaboration of Random Walks on Graphs*, arXiv:2302.14241v1, publicly posted 2023-02-28. Full HTML: https://arxiv.org/html/2302.14241v1 ; see Theorem 1.1, Conjecture 3.1 and Question 3.6.
2. P. S. Dey, D. Kim and G. Terlov, *Collaboration of Random Walks on Graphs*, *Proceedings of the American Mathematical Society* 153 (2025), 4961--4974. DOI: https://doi.org/10.1090/proc/17332 .
