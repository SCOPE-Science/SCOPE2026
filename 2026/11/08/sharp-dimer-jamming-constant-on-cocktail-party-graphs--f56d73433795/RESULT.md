# Sharp dimer-jamming constant on cocktail-party graphs

## Finding
For every integer \(n\ge2\), let \(G_n=K_{2n}\setminus M_n\), where \(M_n\) is a fixed perfect matching. Starting with all vertices vacant, irreversibly occupy the endpoints of a uniformly chosen currently available graph edge with a dimer, repeat until no available edge remains, and let \(q_n\) be the probability that the final adsorption covers only \(2n-2\) vertices rather than all \(2n\).

The only possible jammed outcomes have zero or two uncovered vertices. In the latter case the uncovered vertices form one of the deleted pairs. Define rational numbers \(F(k,\ell)\), for nonnegative integers \(k,\ell\) with even \(2k+\ell\ge2\), by \(F(1,0)=1\), \(F(0,2)=0\), and, when \(2k+\ell\ge4\),
\[
F(k,\ell)=\frac{\binom{\ell}{2}F(k,\ell-2)+2k\ell F(k-1,\ell)+2k(k-1)F(k-2,\ell+2)}{\binom{2k+\ell}{2}-k},
\]
where terms with zero coefficients are omitted (and therefore never call an out-of-domain argument). Then the exact jam probability is \(q_n=F(n,0)\), and
\[
\boxed{\lim_{n\to\infty}nq_n=\frac34.}
\]
More precisely, \(0\le q_n\le 3n/(4n^2-1)\), and the proof gives \(nq_n=3/4+O(n^{-1/3})\). The first exact values are \(q_2=0\), \(q_3=1/5\), \(q_4=8/65\), \(q_5=1231/11375\), and \(q_6=562248/6062875\).

## Assumptions and scope
The graph has labeled vertices grouped into \(n\) disjoint forbidden pairs. Its only nonedges are the \(n\) pairings in \(M_n\). At each successful deposition a graph edge between two currently unoccupied vertices is selected uniformly. Equivalently, all presently feasible edges have identical independent exponential arrival rates. There is no desorption, no site-dependent deposition rate, and no finite-time observation cutoff. The limit takes integer \(n\to\infty\) in this specified complete multipartite graph family \(K_{2,2,\ldots,2}\).

## Proof
**1. Jam states and finite recurrence.** At any stage, let \(k\) be the number of forbidden pairs with both endpoints unoccupied, and \(\ell\) the number of unoccupied singletons whose forbidden partners are already occupied. No two such singletons share a forbidden pair. There are \(2k+\ell\) free vertices and exactly \(\binom{2k+\ell}{2}-k\) admissible dimer edges. Those edges partition into: \(\binom\ell2\) edges between two singletons, \(2k\ell\) edges between one intact pair and a singleton, and \(4\binom k2=2k(k-1)\) edges joining two different intact pairs. The respective new states are \((k,\ell-2)\), \((k-1,\ell)\), and \((k-2,\ell+2)\). This proves the recurrence by conditioning on the first subsequent chosen edge. Every jammed free-vertex set is independent in \(G_n\), so has at most two vertices; two remain exactly when they form an intact forbidden pair. Thus \(q_n=F(n,0)\).

**2. Survival of a tagged forbidden pair.** Fix one deleted pair \(P\), and let \(S_{n,L}\) mean both its endpoints remain free when there are exactly \(2L\) unoccupied vertices. In a state with \(2m\) free vertices, \(k\) intact forbidden pairs including \(P\), and \(1\le k\le m\), the conditional probability that the next dimer avoids the endpoints of \(P\) is
\[
p_1(m,k)=\frac{\binom{2m-2}{2}-(k-1)}{\binom{2m}{2}-k}.
\]
This decreases as \(k\) increases, so for all \(m\ge2\),
\[
\frac{m-2}{m}\le p_1(m,k)\le\frac{2m-3}{2m+1}.
\]
Multiplying the conditional bounds from \(m=n\) down to \(m=L+1\), for \(2\le L\le n\), gives
\[
\frac{L(L-1)}{n(n-1)}\le\Pr(S_{n,L})\le\frac{(2L-1)(2L+1)}{(2n-1)(2n+1)}.
\]
The upper inequality continued down to one free pair shows that the probability \(s_n\) that the particular pair \(P\) is the two-vertex jam set satisfies \(s_n\le3/[(2n-1)(2n+1)]\). By symmetry and mutual exclusivity of the \(n\) possible jammed pairs, \(q_n=ns_n\).

**3. Two-tag estimate.** Fix a second deleted pair \(Q\ne P\). Conditional on both pairs being intact with \(2m\) vertices free, the probability that the next dimer avoids all four tagged vertices is
\[
p_2(m,k)=\frac{\binom{2m-4}{2}-(k-2)}{\binom{2m}{2}-k},\qquad 2\le k\le m.
\]
This also decreases in \(k\). For every \(m\ge3\),
\[
p_2(m,k)\le\frac{\binom{2m-4}{2}}{\binom{2m}{2}-2}
\le\left(\frac{m-1}{m+1}\right)^2.
\]
Indeed the difference between the last expression and the middle expression equals
\[
\frac{4(2m^2-2m-3)}{(m+1)^2(2m^2-m-2)}>0.
\]
Hence the probability that both tagged pairs survive to the \(2L\)-free-vertex stage is at most
\[
\left(\frac{L(L+1)}{n(n+1)}\right)^2.
\]
Let \(R_{n,L}\) be an upper bound for the conditional probability, given \(S_{n,L}\), that at least one *other* forbidden pair is still intact. A union bound over the \(n-1\) alternatives, the two-tag estimate, and the one-tag lower bound give
\[
R_{n,L}=\frac{(n-1)^2L(L+1)^2}{n(n+1)^2(L-1)}.
\]
For every fixed \(L\ge2\), this tends to zero as \(n\to\infty\).

**4. Completion and sharp constant.** Conditional on \(S_{n,L}\) and no other intact forbidden pair, exactly \(P\) is forbidden among the remaining \(2L\) free sites. Until either endpoint of \(P\) is covered, every other pair is admissible. Therefore the exact conditional chance that \(P\) survives to become the final jam set is
\[
\prod_{m=2}^{L}\frac{2m-3}{2m+1}=\frac{3}{(2L-1)(2L+1)}.
\]
Together with the preceding bounds, for every fixed \(L\ge2\) and all \(n\ge L\),
\[
\frac{3nL(L-1)}{(n-1)(4L^2-1)}\max\{0,1-R_{n,L}\}
\le nq_n\le\frac{3n^2}{4n^2-1}.
\]
First take \(n\to\infty\) with \(L\) fixed. The lower and upper limiting bounds are \(3L(L-1)/(4L^2-1)\) and \(3/4\). Then take \(L\to\infty\); both converge to \(3/4\). For the stated error term, take \(L=\lfloor n^{1/3}\rfloor\) for sufficiently large \(n\): the lower-bound losses \(O(1/L)\) and \(O(L^2/n)\) are both \(O(n^{-1/3})\), while the upper-bound excess is \(O(n^{-2})\).

## Verification
Run `python checks/verify_exact.py` and `python checks/verify_asymptotic.py` from the directory containing this document. The first compares the \((k,\ell)\) rational recurrence to a separate, fully labeled unoccupied-vertex bitmask recurrence at every graph size \(2\le n\le7\). Both exact methods return the displayed values and the corresponding values for \(n=7\). The second checks the critical rational inequalities symbolically using SymPy and evaluates the finite recurrence at sizes up to \(n=400\); the latter numerical evaluations illustrate convergence but are **not** a proof of the limit. The proof above supplies the infinite-family argument.

## Relationship to prior work
Random sequential adsorption and uniform-edge random greedy matching are established in work by Pippenger and Dyer–Frieze, while Gamarnik–Goldberg treat greedy matching on bounded-degree, large-girth regular graphs. Their inspected framework and asymptotic bounds do not establish the exact rare two-site jamming probability on the high-degree, girth-three graphs \(K_{2,2,\ldots,2}\). Johnston–Kayll–Palmer analyze *static counts of perfect matchings* avoiding prescribed pairs, including the complete graph minus a matching. Their probability of a uniformly sampled perfect matching meeting the restriction is a different experiment from irreversible sequential adsorption, which may terminate without a perfect matching. The complete original Dyer–Frieze and Pippenger papers could not be inspected through available access; historical priority therefore remains provisional.

## Limitations
The sharp constant holds only for the uniform feasible-edge deposition process and this graph family, not for arbitrary rates, random vertex-choice greedy algorithms, or general dense graphs. No finite-time adsorption kinetics or claim about static perfect-matching proportions is made. Priority cannot be guaranteed against unindexed sources or inaccessible full texts. No independent scientific audit has been performed.

## References
1. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277, initially public 2008-07-08. https://arxiv.org/abs/0807.1277
2. D. Johnston, P. M. Kayll, and C. Palmer, *Deranged matchings: proofs and conjectures*, arXiv:2209.11319 (2022). https://arxiv.org/abs/2209.11319
3. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms **2** (1991), 29–45. https://doi.org/10.1002/rsa.3240020104
4. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. **2** (1989), 393–401. https://doi.org/10.1137/0402034
