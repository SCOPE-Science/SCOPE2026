# First failure of greedy latitude placement at spherical band-limit \(L=12\)

## Finding
Fix the optimal-dimensionality spherical-harmonic sampling geometry with one polar sample and \(2j+1\) equally spaced longitude samples on ring \(j\), \(1\le j\le L-1\). The available co-latitudes are the discrete equiangular grid
\[
\vartheta_t=\frac{(2t+1)\pi}{2L-1},\qquad 0\le t\le L-1,
\]
with \(\theta_0=\vartheta_{L-1}=\pi\). A placement is a permutation of the other \(L-1\) co-latitudes among rings \(1,\ldots,L-1\). For positive order \(m\), let \(\Lambda_m\) be the exact maximum weighted-Lagrange extrapolation row sum from resolving rings \(j\ge m\) to smaller rings \(j<m\), and let \(\mathcal A_L=\max_{1\le m<L}\Lambda_m\).

The greedy placement defined by maximizing the sine at the largest ring and then minimizing the next-order extrapolation row sum is a **global minimizer of \(\mathcal A_L\)** for every \(2\le L\le11\), but **not for \(L=12\)**. At \(L=12\), its exact cost is \(4.4912808131248\ldots\), whereas the *globally smallest* cost among all \(11!\) admissible orderings is \(3.7469440041222\ldots\), an improvement exceeding \(16\%\).

Index the nonpolar co-latitudes by \(t=0,\ldots,10\), with \(\vartheta_t=(2t+1)\pi/23\). Listing the index on rings \(11,10,\ldots,1\) in that order, the unique-choice greedy algorithm gives
\[
(5,7,4,6,2,9,3,8,1,10,0),
\]
while a globally optimal placement is
\[
(4,5,6,8,3,7,2,9,1,10,0).
\]
The former bottleneck has order \(m=5\), resolving index set \(S_g=\{2,3,4,5,6,7,9\}\), and its worst omitted index is \(t=8\). The latter bottleneck has order \(m=6\), resolving index set \(S_*=\{3,4,5,6,7,8\}\), and its worst omitted index is \(t=2\). These specifications define the two exact constants through the formula below; the decimals are explanatory approximations, not the proof.

## Assumptions and scope
For every integer \(L\ge2\), let \(T_L=\{0,\ldots,L-2\}\) index the nonpolar nodes. For nonempty \(S\subseteq T_L\) set \(m=L-|S|\), \(x_t=\cos\vartheta_t\) and \(y_t=\sin\vartheta_t>0\). Define \(F_L(T_L)=0\), and for every proper nonempty \(S\subset T_L\) define
\[
F_L(S)=\max_{t\in T_L\setminus S}\ \sum_{s\in S}
\left(\frac{y_t}{y_s}\right)^m
\prod_{r\in S\setminus\{s\}}
\left|\frac{x_t-x_r}{x_s-x_r}\right|.
\]
The pole contributes zero to every positive-order extrapolation row and is omitted from this maximum. An ordering \(p=(p_1,\ldots,p_{L-1})\) of \(T_L\) assigns \(p_i\) to ring \(L-i\) and has cost
\[
\mathcal A_L(p)=\max_{1\le i\le L-1}F_L(\{p_1,\ldots,p_i\}).
\]
All minimizations in this result are over these **fixed-grid permutations only**, not continuously variable rings, different ring sample counts, alternate pole choices, or all spherical sampling designs.

## Proof
**Weighted cardinal interpolation.** The longitudinal Fourier profile of spherical order \(m>0\) belongs to \((\sin\theta)^m\mathcal P_{L-1-m}(\cos\theta)\). This follows directly from the associated Legendre Rodrigues formula. On the \(L-m\) resolving rings, ordinary polynomial Lagrange interpolation of its polynomial factor gives the cardinal weight for a source node \(s\):
\[
\mathcal L_{s,m}(\theta)=
\left(\frac{\sin\theta}{\sin\theta_s}\right)^m
\prod_{r\in S\setminus\{s\}}
\frac{\cos\theta-x_r}{x_s-x_r}.
\]
The induced operator norm from bounded resolving-ring errors to the omitted rings, with the maximum norm on each finite vector, is exactly the largest absolute row sum. Substituting the available nodes gives \(F_L(S)\). The omitted polar ring is zero for every \(m>0\), so no polar term is missing.

**Nested subsets encode every placement.** For any placement, the resolving nonpolar sets are the chain \(S_i=\{p_1,\ldots,p_i\}\), with each step adjoining one index. Conversely each maximal increasing one-index-at-a-time chain determines a unique placement. Since \(F_L(S)\) depends only on the set, every global optimization can be performed on at most \(2^{L-1}\) subset nodes, not on all permutations separately.

**Finite exact cut certificate.** Let \(S^\dagger\) be the bottleneck subset on a proposed optimal chain, and put \(B=F_L(S^\dagger)\). If every other subset is classified strictly as \(F_L(S)<B\) or \(F_L(S)>B\), then the directed graph of subsets with \(F_L(S)<B\) contains a full chain if and only if there exists a placement of cost strictly below \(B\). The empty starting set is admitted; the bottleneck subset is excluded by its exact defining equality. Thus, the nonexistence of a path from the empty subset to the full set certifies that every placement costs at least \(B\). A displayed placement whose cost equals \(B\) attains this bound.

The accompanying standalone `verify.py` implements this argument using outward-rounded integer-rational intervals. It encloses \(\pi\) by Machin's arctangent identity and alternating-series error bounds, then encloses each \(\sin\vartheta_t\) and \(\cos\vartheta_t\) by Taylor polynomials and analytic remainder bounds. Every cardinal weight, sum, maximum, greedy decision and subset-versus-threshold comparison is enclosed by directed integer arithmetic. All nonidentical threshold comparisons are strict; the one equal bottleneck subset is recognized by identity, not numerical coincidence. Reachability is then tested by exact Boolean subset recursion. There is no assumption that floating-point experiments prove an exhaustive result.

For \(L=2\), the only omitted positive-order ring is the pole, so \(\mathcal A_2=0\). For each \(L=3,\ldots,11\), the supplied greedy chain attains its bottleneck value and the strict-threshold subset graph has no full chain. At \(L=12\), the alternative chain likewise attains its bottleneck value, and the strict-threshold subset graph again has no full chain. The checker separately verifies that the listed greedy chains are genuinely generated by strict greedy decisions and that the \(L=12\) alternative cost is strictly smaller than the greedy cost. This proves both the global minimax assertions and the first-failure cutoff.

## Verification
Run `python3 verify.py` (Python standard library only). The certificate checks \(L=3,\ldots,12\), including all \(2^{L-1}-1\) nonempty subsets at each band-limit. At \(L=12\) it classifies 30 subsets strictly below the optimal bottleneck and 2,017 at or above it; the latter include the bottleneck itself. Only 24 subsets are reachable through strictly suboptimal-cost prefixes, and the full subset is not reachable. The two exact costs are isolated by certified rational intervals whose decimal values begin, respectively, \(3.746944004122\) and \(4.491280813124\). An independent floating-point dynamic-programming calculation of the finite minimax problem found the same placements and values, but the finite-proof claim rests on the interval certificate, not that calculation.

## Relationship to prior work
Khalid (2026), arXiv:2611.16441, defines the exact weighted-cardinal extrapolation norm \(\Lambda_m\) in equation (23) and the descending-order greedy \(\Lambda\)-placement in Section VI-C, and explicitly raises non-greedy improvement as a direction. Its experiments and algorithm do not establish the global minimax optimum or the first failing band-limit. Nafees, Khalid, Kennedy and McEwen (2017), arXiv:1709.02497, optimize the distinct condition-number objective for spherical harmonic collocation using an elimination placement and refinement. Khalid, Kennedy and McEwen (2014), arXiv:1403.4661, formulate the optimal-dimensionality ring scheme and greedy **condition-number** placement. Those condition numbers are not \(\Lambda_m\), and improvements for the former do not imply the exact global threshold shown here. The interpolation formula itself is not claimed as new.

## Limitations
This is an exact, finite first-counterexample and cutoff theorem for the 2026 amplification objective on one fixed equiangular grid. It does not assert that the displayed globally optimal placement is unique, establish analogous optimality for larger band-limits, optimize the original coefficient condition number, or prove a reduction of realized floating-point reconstruction error for every input. The strict inequality of the model amplification constants is rigorous; a corresponding practical improvement in measured error is not asserted.

## References
1. Z. Khalid, *An \(O(L^3)\) Spherical Harmonic Transform on \(L^2\) Samples*, arXiv:2611.16441, first posted 2026-11-12, https://arxiv.org/abs/2611.16441.
2. W. Nafees, Z. Khalid, R. A. Kennedy, J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, arXiv:1709.02497, https://arxiv.org/abs/1709.02497.
3. Z. Khalid, R. A. Kennedy, J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661, https://arxiv.org/abs/1403.4661.
