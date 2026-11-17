# Rare dimer-jamming defects in a complete graph with a deleted perfect matching

## Finding

Let \(G_m\) be the simple graph formed from \(K_{2m}\) by deleting the edges of one fixed perfect matching \(M\). Starting with every vertex unoccupied, repeatedly choose an available edge uniformly at random, cover both of its endpoints permanently with one dimer, and stop when no available edge remains. Write \(R_m\) for the final number of vacant vertices. For every integer \(m\ge2\), \(R_m\) takes values only in \(\{0,2\}\). Its exact finite-size distribution is computable by the two-integer recurrence below, and its sharp rare-defect law is

\[
\lim_{m\to\infty}m\Pr(R_m=2)=\frac34,
\qquad
\lim_{m\to\infty}m\mathbb E R_m=\frac32.
\]

In particular, a complete graph with the same number of vertices always adsorbs \(m\) dimers, whereas deleting a perfect matching creates a rare but quantifiable two-vacancy terminal configuration.

## Assumptions and scope

The deleted matching contains \(m\) disjoint unordered vertex pairs. An edge is *available* exactly when both endpoints are still vacant and the edge was not deleted. Successive available edges are selected with uniform conditional probability; equivalently, each available edge has an independent equal-rate exponential deposition clock and occupied endpoints block all incident edges. There are no removals, diffusion, monomers, variable edge weights, or other exclusion rules. The result concerns this fixed labeled graph and all positive integers \(m\ge2\), not uniform sampling among maximal matchings or equilibrium monomer–dimer Gibbs measures.

A deleted pair is called *intact* if both of its vertices are still vacant. Any remaining vacant vertex not in an intact pair is called a *singleton*. When \(k\) deleted pairs are intact and \(s\) singletons remain, there are \(2k+s\) vacant vertices and precisely \(k\) forbidden edges among them.

## Proof

**Terminal possibilities and the exact recurrence.** With at least four vacant vertices, some allowable edge always remains, since every vertex has at most one forbidden partner. At two vertices, adsorption either finishes if the two vertices are adjacent or jams if they constitute a deleted pair. Therefore \(R_m\in\{0,2\}\).

Let \(F(k,s)\) denote the conditional probability of terminating with two vacancies when the present state has \(k\) intact pairs and \(s\) singletons, with \(2k+s\) even. Define
\[
D(k,s)=\binom{2k+s}{2}-k.
\]
For \(2k+s>2\), choosing two singletons, a singleton and a vertex in an intact pair, or vertices from two different intact pairs gives the exact recurrence
\[
F(k,s)=\frac{\binom{s}{2}F(k,s-2)+2ksF(k-1,s)+2k(k-1)F(k-2,s+2)}{D(k,s)}.
\]
Terms with invalid indices or a zero combinatorial coefficient are omitted, and \(F(1,0)=1\), \(F(0,2)=0\). Thus \(\Pr(R_m=2)=F(m,0)\). This is an exact finite algorithm, not an asymptotic approximation.

**Upper bound from one tagged deleted pair.** Let \(A\) be any specified deleted pair and let \(p_m\) be the probability that both its endpoints remain until deposition ends. Write \(t\) for half the number of vacant vertices. Conditional on \(A\) being intact and there being \(k\) intact deleted pairs in total, the probability that the next deposition avoids \(A\) is
\[
r_t(k)=\frac{\binom{2t-2}{2}-(k-1)}{\binom{2t}{2}-k},\qquad 1\le k\le t.
\]
This fraction decreases with \(k\); for \(t\ge2\),
\[
\frac{t-2}{t}\le r_t(k)\le r_t(1)=\frac{2t-3}{2t+1}.
\]
The process passes through each of the sizes \(2m,2m-2,\ldots,2\). Consequently
\[
p_m\le\prod_{t=2}^{m}\frac{2t-3}{2t+1}=\frac3{(2m-1)(2m+1)}.
\]

**Matching lower bound.** Fix an integer \(T\ge2\) and take \(m\ge T\). The same conditional survival inequality implies that the probability \(A\) is still intact at size \(2T\) is at least
\[
L_{T,m}:=\prod_{t=T+1}^{m}\frac{t-2}{t}=\frac{T(T-1)}{m(m-1)}.
\]
For two distinct specified deleted pairs \(A,B\), conditional on both being intact and a total of \(k\ge2\) intact pairs, the probability that the next deposition avoids all four tagged vertices is
\[
q_t(k)=\frac{\binom{2t-4}{2}-(k-2)}{\binom{2t}{2}-k},\qquad t\ge3.
\]
It decreases with \(k\) and satisfies
\[
q_t(k)\le q_t(2)=\frac{(2t-4)(2t-5)}{2t(2t-1)-4}
\le\left(\frac{t-2}{t}\right)^2.
\]
The final inequality follows upon clearing positive denominators: the right-minus-left cross-product is \(8(t-2)>0\). It follows that
\[
\Pr(A,B\text{ both intact at size }2T)\le L_{T,m}^2.
\]
The union bound then gives
\[
\Pr(A\text{ intact and the sole intact pair at size }2T)
\ge L_{T,m}-(m-1)L_{T,m}^2.
\]
If \(A\) is the sole intact pair at that size, then conditional on survival of \(A\), it remains the sole intact pair, so the probability of surviving from \(2T\) vertices down to the final two is exactly
\[
\prod_{t=2}^{T}r_t(1)=\frac3{(2T-1)(2T+1)}.
\]
Combining these estimates and using nonnegativity if the displayed lower bound is negative,
\[
p_m\ge
\left[L_{T,m}-(m-1)L_{T,m}^2\right]
\frac3{(2T-1)(2T+1)}.
\]
For any fixed \(T\), multiply by \(m^2\) and let \(m\to\infty\); then send \(T\to\infty\). The lower bound tends to \(3/4\), matching the upper bound. Hence
\[
\lim_{m\to\infty}m^2 p_m=\frac34.
\]
Exactly one of the \(m\) deleted pairs can remain as the last two vertices, and these events are disjoint and exchangeable. Thus \(\Pr(R_m=2)=mp_m\). Since \(R_m=2\mathbf1_{\{R_m=2\}}\), both limits in the finding follow.

## Verification

The accompanying `checker.py` independently computes \(F(m,0)\) from the reduced state recursion and from exhaustive labeled-vertex dynamic programming for \(2\le m\le7\). It also verifies the displayed one-pair, two-pair, upper-bound, and finite-\(T\) lower-bound inequalities over thousands of exact-rational finite cases. The first failure probabilities are \(F(2,0)=0\), \(F(3,0)=1/5\), and \(F(4,0)=8/65\). Run using `python3 checker.py` with Python 3's standard library. The all-size asymptotic conclusion follows from the written inequalities, not from this finite enumeration.

## Relationship to prior work

Randomized greedy matching is a classical process. Dyer and Frieze (1991) studied its approximation behavior on general and sparse graph families. Gamarnik and Goldberg (2008), notably their Theorem 5, proved bounds for bounded-degree, high-girth regular graphs; those hypotheses do not apply here, since \(G_m\) is dense with triangles and degree \(2m-2\). Miller and Pritikin (1997) gave general performance-ratio inequalities, not an exact rare-jamming asymptotic for this graph. Turban (2019) solved covering-time statistics for a fully connected adsorption substrate, which can always be covered completely; the deleted matching introduces a new terminal obstruction. The asymptotic factor \(3/4\) is not obtained by a complete-graph substitution or by counting uniformly selected maximal matchings. A checked-source and historical-priority assessment appears separately in the review documents.

## Limitations

The exact finite recurrence and the limiting constant apply only to uniform edge-choice deposition on \(K_{2m}\setminus M\). No finite-size closed form for \(F(m,0)\) is claimed; the recurrence is exact. The proof establishes the leading \(m^{-1}\) term but not a full next-order expansion. A leading term for probability and mean does not determine the distribution of deposition time. A general randomized-greedy-matching paper from 1991 was available only through an abstract in the accessible literature comparison; historical priority remains provisional.

## References

- D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277v1 (first posted 2008-07-08), https://arxiv.org/abs/0807.1277.
- M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms **2** (1991), 29–46, https://doi.org/10.1002/rsa.3240020104.
- Z. Miller and D. Pritikin, *On randomized greedy matchings*, Random Structures & Algorithms **10** (1997), 353–383, https://doi.org/10.1002/(SICI)1098-2418(199705)10:3%3C353::AID-RSA5%3E3.0.CO;2-V.
- L. Turban, *Random sequential adsorption of k-mers on the fully-connected lattice*, arXiv:1908.00940v1 (first posted 2019-08-02), https://arxiv.org/abs/1908.00940.
