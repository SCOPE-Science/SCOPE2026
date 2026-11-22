# Geometry-signed two-site kinetic interference on the Petersen adsorption network

## Finding

Let \(G\) be the Petersen graph in its Kneser representation: its ten vertices are the two-element subsets of \(\{1,2,3,4,5\}\), with two vertices adjacent exactly when the subsets are disjoint. Independently assign to each vertex a first attempted adsorption time of exponential rate one, except for two distinct marked vertices \(u,v\), with respective positive rates \(a,b\). Process attempted arrivals chronologically, accepting a monomer if and only if none of its neighbors is already occupied, and retaining accepted particles forever. Write \(K\) for the number eventually accepted. Set

\[
H(a,b)=\frac{(a-1)(b-1)}{3(a+2)(b+2)(a+b+1)(a+b+8)}.
\]

For **every** \(a,b>0\), the complete terminal-size law is

\[
\begin{array}{c|cc}
&\Pr(K=4)&\Pr(K=3)\\ \hline
u\sim v & \frac23+4H(a,b)&\frac13-4H(a,b)\\
u\not\sim v & \frac23-2H(a,b)&\frac13+2H(a,b).
\end{array}
\]

No other terminal size occurs. Thus, for two simultaneously accelerated sites \(a,b>1\), adjacent marked sites **increase** the chance of four occupied vertices, while nonadjacent marked sites **decrease** it; the signs reverse if precisely one rate is below one. The adjacent and nonadjacent changes have ratio exactly \(-2\), independent of the two positive rates, and both vanish if either rate equals one.

## Assumptions and scope

The result is a finite, exactly ten-site, irreversible, nearest-neighbor-excluding monomer adsorption model. One exponential first-arrival attempt per site is made, including sites already rendered ineligible; ignoring attempts at ineligible sites is equivalent for the accepted set. Rates of the eight unmarked sites are exactly one. The two marks are distinct, and the only two relative-geometry classes are disjoint or intersecting two-subsets (adjacent or nonadjacent Petersen vertices). No large-network limit or multiple-attempt model is asserted.

## Proof

**Terminal support.** An independent set in \(G\) is a pairwise-intersecting family of two-subsets of a five-element set. Any maximal such family is either the four edges of a full star or the three edges of a triangle: two intersecting edges have a common endpoint; every further edge intersecting both either contains that endpoint or is the opposite edge completing the triangle. In the latter case no fourth edge can meet all three, and otherwise maximality forces the whole star. Since processing all ten first attempts produces a maximal independent set, \(K\in\{3,4\}\). There are five star-type and ten triangle-type terminal sets.

**Exact recursion.** For a vertex set \(S\) still eligible after previous accepted particles, let \(F(S)\) be the expected additional number of accepted sites. With site rates \(r_i\), the exponential race and memorylessness give the finite exact recurrence

\[
F(\varnothing)=0,\qquad
F(S)=1+\frac{\sum_{i\in S}r_iF(S\setminus N[i])}{\sum_{i\in S}r_i},
\]

where \(N[i]\) is the closed neighborhood in \(G\). Deleting an ineligible site's future attempt cannot change acceptance, and the next eligible attempt has rate proportional to \(r_i\), justifying the recurrence. The graph and recurrence have only \(2^{10}\) possible bitmask arguments; the actual root calculation visits 52 distinct masks for each position class. The companion exact symbolic rational-function certificate `verify_symbolic.py` constructs those masks, evaluates the recurrence with indeterminates \(a,b\), and verifies the following identities by exact polynomial cancellation:

\[
F(V)=\begin{cases}
\displaystyle \frac{11}{3}+4H(a,b),&u\sim v,\\[2pt]
\displaystyle \frac{11}{3}-2H(a,b),&u\not\sim v.
\end{cases}
\]

As \(K\in\{3,4\}\), its expectation is \(3+\Pr(K=4)\), which gives the entire asserted size distribution.

**Independent enumeration of the identity.** Fix the first marked vertex in priority position \(r\) and the second in distinct position \(s\), with \(0\le r,s<10\). For each of the \(8!\) relative permutations of the other sites, the deterministic acceptance rule determines whether \(K=4\). The independently constructed `verify_priority.py` counts all \(90\times8!=3,628,800\) marked-position/permutation cases for each adjacency class, yielding integers \(C_{r,s}\). For a fixed full priority order with rates \(w_0,\ldots,w_9\) (equal to \(a,b\) at the marked positions and one otherwise), its exact probability is

\[
\prod_{t=0}^{9}\frac{w_t}{\sum_{q=t}^{9}w_q}.
\]

Consequently the complete four-particle probability equals \(\sum_{r\ne s}C_{r,s}\prod_t w_t/(\sum_{q=t}^9 w_q)\); this is an independently constructed finite sum with explicit integer counts, algebraically equal to the two rational functions displayed above. The included independent checker computes its coefficients exhaustively and evaluates it using rational arithmetic at six positive rate pairs per class. The companion full-symbolic recurrence, rather than these samples, proves the identity for every positive real rate pair.

**Sign.** Each factor in the denominator of \(H(a,b)\) is strictly positive for \(a,b>0\). Thus its sign is exactly the sign of \((a-1)(b-1)\), with the opposite prefactors \(+4\) and \(-2\) proving all asserted strict signs and the constant ratio.

## Verification

Execute `python verify_symbolic.py` (requires SymPy) and `python verify_priority.py` (Python standard library). The former gives exact symbolic rational-function identities for both marked-site geometry classes; the latter exhausts 3,628,800 priority configurations per class and checks six independently computed exact rational probabilities. Both tests passed. They substantiate a complete *finite* exact identity, not an extrapolation from samples to infinitely many graphs. Positivity for arbitrary real positive rates follows algebraically from the derived rational identities.

## Relationship to prior work

Random sequential adsorption and greedy maximal independent sets on graphs are established processes. Pippenger (1989) studies regular graphs, principally long-girth occupancy limits, rather than this two-impurity finite Petersen law. Dhara, van Leeuwaarden and Mukherjee (2016) analyze generalized adsorption on Erdős–Rényi graphs with large-size asymptotics, not fixed Petersen geometry with two nonuniform arrival rates. Krivelevich, Mészáros, Michaeli and Shikhelman (2023) study greedy-independent-set local limits for graph sequences, not this complete two-rate terminal distribution. A related exact result treats biased monomer adsorption on the entire two-subset Kneser family, including the Petersen graph, but changes the rates of **all** sites containing a distinguished ground point simultaneously. At five ground points, that is four marked sites, not the two arbitrarily located, independently adjustable marked sites studied here. Its one-parameter formula and its star-versus-triangle support classification do not imply the adjacent/nonadjacent two-rate law. Other published and indexed calculations concern edge-dimer deposition on the Petersen graph or monomer deposition on the Robertson cage, which use different observables or substrates. A single changed rate on any vertex-transitive graph leaves an automorphism-invariant terminal statistic unchanged by the elementary symmetry of the distinguished vertex's rank; the present nonzero, sign-reversing two-site term is the first parameter interaction not eliminated by that observation.

## Limitations

The theorem is specific to the Petersen graph, independent one-shot exponential clocks, and two variable site rates; it does not classify higher-order impurity interactions, other graphs, all-time coverage, or microscopic output-set probabilities. The calculation is finite and exact but its historical priority remains provisional: older general graph adsorption literature was partly accessible only as an abstract, and equivalent finite calculations may be unindexed. No independent external scientific audit has been performed.

## References

1. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401, https://doi.org/10.1137/0402034.
2. S. Dhara, J. S. H. van Leeuwaarden and D. Mukherjee, *Generalized Random Sequential Adsorption on Erdős–Rényi Random Graphs*, arXiv:1604.03918, first public preprint 2016-04-13, https://arxiv.org/abs/1604.03918; J. Stat. Phys. 164 (2016), 1217–1232, https://doi.org/10.1007/s10955-016-1583-z.
3. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy Maximal Independent Sets via Local Limits*, Random Structures Algorithms 64 (2024), 986–1015, first published 2023-12-18, https://doi.org/10.1002/rsa.21200.
