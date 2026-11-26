# Fibonacci-cube components of the involution-induced permutahedron

## Finding

Let \(G_n\) have all involutions on the labelled linear order \([n]\), \(n\ge1\), as vertices; an edge swaps the values at two neighboring positions in one-line notation. Let \(\Gamma_d\) be the Fibonacci cube on binary strings of length \(d\) without consecutive ones, with Hamming-distance-one adjacency, and let \(F_0=0,F_1=1,F_{k+2}=F_{k+1}+F_k\).

Index the components by matchings \(M\) of nonconsecutive pairs of labels. Delete the vertices covered by \(M\) from the path on \([n]\); let \(\ell_a\) be the lengths of the maximal nonempty residual runs. Then exactly one component \(H_M\) has \(M\) as its nonconsecutive two-cycles, and
\[
 H_M\cong\mathop{\square}_a \Gamma_{\ell_a-1},\qquad |H_M|=\prod_a F_{\ell_a+1},\qquad \operatorname{diam}(H_M)=\sum_a(\ell_a-1).
\]
An empty product of graphs is a singleton. The distance of two involutions in a component is the size of the symmetric difference of their sets of adjacent two-cycles.

The unique largest component is \(H_\varnothing\), of order \(F_{n+1}\). For \(n\ge3\) the unique second largest is indexed by \(\{\{1,n\}\}\), of order \(F_{n-1}\). Write \(I_0=I_1=1\) and \(I_n=I_{n-1}+(n-1)I_{n-2}\). The component count is
\[
C_n=\sum_{j=0}^{\lfloor n/2\rfloor}(-1)^j\binom{n-j}{j}I_{n-2j},
\]
and the graph has \((n-1)I_{n-2}\) edges for \(n\ge2\) and none for \(n=1\).

## Assumptions and scope

Fixed points are allowed. Swaps exchange consecutive linear positions, not arbitrary positions, and are not conjugations. A matching is an unordered set of pairwise disjoint unordered pairs. Results for an abstract Fibonacci cube, or random-involution motif limits, are not claimed here as new.

## Proof

**Move rule.** A swap at positions \(i,i+1\) takes \(\pi\) to \(\pi s_i\), with \(s_i=(i\ i+1)\). Since both factors are involutions, the product is an involution iff the factors commute. Conjugation by \(\pi\) sends \(s_i\) to \((\pi(i)\ \pi(i+1))\), so this happens iff the two positions are both fixed or are each other's partners. The swap exactly toggles the corresponding adjacent two-cycle. Every nonconsecutive two-cycle is invariant.

**Components and metric.** Given \(M\), all remaining transpositions are matchings of the residual path. Their edge indicator vectors have no consecutive ones within a run and have independent coordinates across runs. Each legal toggle is a Hamming-distance-one step. From one matching remove all edges not in the target, then add the target's missing edges. All intermediate sets are matchings, giving connectivity and a path attaining the Hamming lower bound. The number of matchings of a path of \(\ell\) vertices is \(F_{\ell+1}\), by deciding whether its first vertex is covered. Complementary alternating edge sets attain distance \(\ell-1\) in each run, proving the diameter after summing over runs.

**Extrema.** If the residual runs have \(m\) total vertices, concatenate them as a path on \(m\) vertices. Joining the runs introduces a bridge edge at every seam and does not remove any existing edges. Each new edge alone forms a matching not previously possible, so the bound \(F_{m+1}\) is strict if there is more than one nonempty run. For \(M\ne\varnothing\), \(m\le n-2\). If \(|M|\ge2\), then \(n\ge4\), \(m+1\le n-3\), and \(F_{m+1}<F_{n-1}\) (including \(n=4\)). For \(|M|=1\), equality requires a single residual run. Deleting one nonconsecutive pair leaves a single run only if the two deleted vertices are the endpoints, because deleting the first two or last two would use a consecutive pair. This proves uniqueness of the second-largest component and the size gap to \(H_\varnothing\). For \(n=1,2\) there is only \(H_\varnothing\).

**Totals.** A component has one vertex with no adjacent two-cycle. Count those vertices by inclusion–exclusion over the \(n-1\) adjacent pairs: \(j\) disjoint pairs can be chosen in \(\binom{n-j}{j}\) ways, after which an arbitrary involution remains on the remaining \(n-2j\) positions. For each possible swap index an edge has one endpoint with that short cycle and one endpoint with both sites fixed. It is specified uniquely by any involution on the other \(n-2\) sites. This gives the exact edge count.

## Context: random mobility is a consequence of an overlapping motif theorem

In the distinct record [3], \(A_n\) counts adjacent fixed–fixed pairs and \(B_n\) adjacent partner pairs. Its uniform-involution limit obtained by mixing at fixed-point scale \(\sqrt n\) makes \((A_n,B_n)\) asymptotically independent \(\mathrm{Poisson}(1)\) variables. The move rule identifies \(\deg(\pi)=A_n+B_n\), so the degree limit \(\mathrm{Poisson}(2)\) and the isolated fraction \(e^{-2}\) follow directly. Similarly \(C_n/I_n=\Pr(B_n=0)\to e^{-1}\), so the arithmetic mean of component sizes tends to \(e\). These limits are not part of the originality claim; the common record date does not resolve priority.

For an elementary cross-check, set \(R_m=I_m/I_{m-1}\). The recurrence \(R_m=1+(m-1)/R_{m-1}\) gives \(\sqrt m\le R_m\le\sqrt m+1\) by induction, using \((x+1/(x+1))^2\ge x^2+1\) for \(x\ge0\). Thus \(I_{n-s}/I_n\sim n^{-s/2}\) for each fixed \(s\). For any fixed \(r\), the ordered disjoint choices of \(r\) adjacent pairs number \(r!\binom{n-r}{r}\). For the degree factorial moment their probability is \(2^r I_{n-2r}/I_n\). Choices with overlaps fall into \(c<r\) runs of edges; the covered sites number \(r+c\), and each nonsingleton run forces all its sites fixed. These choices have total contribution \(O(n^c n^{-(r+c)/2})=o(1)\). Hence the factorial moments tend to \(2^r\); the same calculation for \(B_n\) has one choice per disjoint pair and no overlaps, giving moments \(1\). These Poisson laws are moment-determinate and convergence implies the claimed zero probabilities at the integer threshold.

## Verification and prior work

The supplied standalone `check_invol.py` builds the adjacent-position graph directly for \(1\le n\le9\) and checks component and edge counts and finite metrics (the latter through \(n=8\)). Finite enumeration is a consistency check, not the all-\(n\) proof. For the uniqueness assertions use the strict bridge comparison above, not just the two largest size values printed by the checker.

The Fibonacci-cube literature [2] treats the abstract cubes and their metrics, and token sliding [1] preserves token number, unlike the toggles here. The related product-of-cubes description for one-pass pop-stack-sortable permutations [4] applies to a different state space and does not index sectors by nonconsecutive two-cycles. The distinct contribution is the full component and metric classification, its extremal sectors, and associated exact graph counts for this move relation. Unindexed equivalent decompositions or catalogue entries for the component sequence remain possible. There is no claim about cyclic adjacency or a fixed-point-free subset.

## References

1. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, https://arxiv.org/abs/2203.16861.
2. Ö. Eğecioğlu, E. Saygı and Z. Saygı, *Euler numbers and diametral paths in Fibonacci cubes, Lucas cubes and Alternate Lucas cubes*, https://arxiv.org/abs/2210.13849.
3. *A fixed-point phase and independent Poisson mechanisms for one-deletion diversity of random involutions*, Finding, Assumptions and Proof §4, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-fixed-point-phase-and-independent-poisson-mechanisms-for-one-d--e2ec350e7d45/RESULT.md.
4. *Median component decomposition of the one-pass pop-stack permutahedron*, Finding and Assumptions, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-median-component-decomposition-of-the-one-pass-pop-stack-permuta--920b1e1645a1/RESULT.md.
