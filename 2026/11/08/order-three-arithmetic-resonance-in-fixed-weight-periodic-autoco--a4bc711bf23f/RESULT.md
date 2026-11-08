# Order-three arithmetic resonance in fixed-weight periodic autocorrelation

## Finding

Let \(N\ge6\) and \(0\le k\le N\) be integers. Choose a \(k\)-element subset \(S\) uniformly from \(\mathbb Z/N\mathbb Z\). For any undirected, non-antipodal cyclic distance
\[
1\le d\le \left\lfloor\frac{N-1}{2}\right\rfloor,
\]
define its occupied-pair count
\[
A_d=\#\bigl\{\{i,i+d\}:i\in\mathbb Z/N\mathbb Z,\quad i,i+d\in S\bigr\}.
\]
Each unordered pair is counted once. Thus \(A_d\) is a fixed-Hamming-weight version of a nonzero periodic binary autocorrelation, with the potentially antipodal matching distance deliberately excluded.

Put \((x)_r=x(x-1)\cdots(x-r+1)\), with \((x)_0=1\). For **all** these distances, independently of \(d\),
\[
\mathbb E A_d=\frac{k(k-1)}{N-1},\qquad
\operatorname{Var}(A_d)=\frac{k(k-1)(N-k)(N-k-1)}{(N-2)(N-1)^2}.
\]
The third centered moment has the **complete arithmetic classification**
\[
\boxed{\begin{aligned}
\mathbb E[(A_d-\mathbb EA_d)^3]
={}&\frac{k(k-1)(N-k)(N-k-1)((2k-N)^2-1)}{(N-3)(N-2)(N-1)^3}\\
&+2N\,\mathbf1_{\{3\mid N,\ d=N/3\}}\frac{(k)_3(N-k)_3}{(N)_6}.
\end{aligned}}
\]
For \(3\le k\le N-3\), the additional term is strictly positive at the unique distance \(d=N/3\) when \(3\mid N\), and is absent at every other permitted distance. If \(3\nmid N\), all permitted distances have equal first three moments. These statements do **not** assert equality of their full distributions.

A particularly sharp effect occurs when \(6\mid N\) and \(k=N/2\): all non-resonant distances have a negative third centered moment, while distance \(N/3\) has a positive one. Explicitly,
\[
\begin{aligned}
\mu_{3,\mathrm{ordinary}}&=-\frac{N^2(N-2)}{16(N-3)(N-1)^3}<0,\\
\mu_{3,\mathrm{resonant}}&=\frac{N^2(N-2)(N^2-3N-2)}{32(N-5)(N-1)^3}>0.
\end{aligned}
\]
At \(N=6,k=3\), these are \(-3/125\) and \(72/125\), respectively.

## Assumptions and scope

The index set is cyclic, not a line. The subset \(S\) is sampled uniformly *conditional on exactly \(k\) occupied sites*. Equivalently, the binary string is sampled uniformly among words of length \(N\) containing exactly \(k\) ones. The distances are undirected and satisfy \(d<N/2\); when \(N\) is even, distance \(N/2\) gives a matching rather than a two-regular graph and is outside the claim.

The parameter range \(N\ge6\) makes \((N)_6\) positive and permits both the triangular and nontriangular comparison. The expressions remain valid at \(k=0,1,2,N-2,N-1,N\), where the exceptional term vanishes. Strictly positive resonance requires at least three ones and three zeros.

## Proof

For \(j=2,\ldots,6\), write
\[
p_j=\frac{(k)_j}{(N)_j},
\]
with \(p_j=0\) if \(k<j\). A fixed set of \(j\) distinct sites is wholly occupied with probability \(p_j\).

For each admissible \(d\), the graph with edge set \(E_d=\{\{i,i+d\}:i\in\mathbb Z/N\mathbb Z\}\) is a simple two-regular graph with exactly \(N\) edges. Its components are cycles of common length \(N/\gcd(N,d)\). It has triangular components if and only if \(3\mid N\) and \(d=N/3\), in which case the number of triangular components is \(t=N/3\); otherwise \(t=0\).

Write \(I_e\) for the indicator that both endpoints of an edge \(e\) are occupied, so \(A_d=\sum_{e\in E_d}I_e\). There are \(N\) ordered identical edge pairs, \(2N\) ordered pairs of distinct adjacent edges and \(N(N-3)\) ordered pairs of disjoint edges. Therefore
\[
\mathbb EA_d=Np_2,
\qquad
\mathbb EA_d^2=Np_2+2Np_3+N(N-3)p_4.
\]
Subtracting the square of the mean and simplifying gives the displayed universal variance.

For the third raw moment, classify ordered triples of edges by repetitions and the union of their endpoints. Three identical edges contribute \(Np_2\). Exactly two identical edges contribute
\[
3\bigl(2Np_3+N(N-3)p_4\bigr).
\]
For three distinct edges, the numbers of **unordered** edge triples of the four possible shapes are
\[
\begin{array}{c|c|c}
\text{shape}&\text{number}&\text{distinct endpoints}\\\hline
\text{triangle}&t&3\\
\text{three-edge path}&N-3t&4\\
\text{two-edge wedge plus disjoint edge}&N(N-4)+3t&5\\
\text{three mutually disjoint edges}&\binom N3-N(N-3)-t&6.
\end{array}
\]
Indeed, each edge is the middle edge of exactly one adjacent-edge triple unless its component is a triangle, giving \(N-3t\) paths. There are \(N\) two-edge wedges; the third edge is disjoint from the wedge at \(N-4\) choices outside a triangle and \(N-3\) choices within a triangle. Subtracting all three previously counted shapes from \(\binom N3\) gives the final row. Each unordered triple has six orderings. Consequently,
\[
\begin{aligned}
\mathbb EA_d^3={}&Np_2+3\bigl(2Np_3+N(N-3)p_4\bigr)\\
&+6\Bigl(tp_3+(N-3t)p_4+[N(N-4)+3t]p_5\\
&\hspace{2.9em}+[\binom N3-N(N-3)-t]p_6\Bigr).
\end{aligned}
\]
The dependence on \(t\) in this exact expression is only
\[
6t(p_3-3p_4+3p_5-p_6).
\]
The finite-population binomial identity gives
\[
p_3-3p_4+3p_5-p_6
=\frac{(k)_3(N-k)_3}{(N)_6};
\]
this is also the probability that three specified vertices are occupied and three other specified vertices are unoccupied. Thus the triangular contribution is nonnegative and, for \(t=N/3\), equals exactly the additional term in the finding.

Finally, the third centered moment is
\[
\mathbb EA_d^3-3(\mathbb EA_d)(\mathbb EA_d^2)+2(\mathbb EA_d)^3.
\]
Substitution of the first three raw moments, followed by elementary rational cancellation, gives the stated non-resonant term. Both lower moments are independent of \(t\), so the triangular correction remains unchanged under centering. At \(k=N/2\), substitution and simplification yield the two displayed opposite-sign expressions; \(N^2-3N-2>0\) for \(N\ge6\). This completes the proof for every stated parameter.

## Verification

The standalone file `verify.py` uses only the Python standard library and exact rational arithmetic. Run `python verify.py`. It exhaustively enumerates all subsets for \(6\le N\le12\), every \(0\le k\le N\), and every permitted \(d\), comparing the exact first three centered moments with the formulas. It additionally checks the independent edge-motif raw-moment expression and the balanced sign reversal at \(N=6,12,18\) by rational formulas. The observed run passed 827 exact comparisons across 274 enumeration cases. This finite replay corroborates the identities; the proof above establishes their universal scope.

## Relationship to prior work

Mercer (2006) studies moments and tail behavior of **aperiodic** autocorrelations of unconditioned independent fair binary signs; that sampling law and boundary convention are different. Willms (2012/2013) gives deterministic relationships between a binary sequence's run structure and its periodic or aperiodic autocorrelations, not the fixed-weight third centered moments of individual cyclic distances. Zhong, Zhou and Jiang (2013) use a third-order *three-symbol* cyclic correlation to construct signals; their higher-order statistic is not the third moment over uniformly sampled binary words of a *two-symbol* lag autocorrelation. Caullery, Érard and Rodier (2024) analyze extreme periodic correlations under independent binary signs, not fixed content or a third-moment order-three arithmetic exception.

An accessible published analysis of pairwise transition indicators in fixed-composition binary words gives second-order covariance according to whether pairs of transitions share a position. That result explains second moments after summation, but pairwise covariance alone cannot determine this third cumulant or distinguish triangular triples of edges. The arithmetic resonance requires the new three-edge motif classification above. Searches of the stated moment formula, the shift-order-three exception, the model's aliases and relevant literature did not find a dominating published statement. Non-observation is not a proof of absolute priority.

## Limitations

The theorem concerns moments through order three, not the complete distribution or higher-order lag moments. The antipodal distance is excluded by definition. At the sparse and nearly-full boundaries the exceptional term vanishes, so no strict skewness comparison is asserted there. The source comparison leaves a historical risk that older circular-run enumeration or fixed-composition sequence-design literature contains an equivalent arithmetic third-moment formula not readily indexed under autocorrelation terminology.

## References

1. I. D. Mercer, “Autocorrelations of Random Binary Sequences,” *Combinatorics, Probability and Computing* 15 (2006), 663–671. DOI: https://doi.org/10.1017/S0963548306007589. Online publication: 2006-07-31.
2. J. Willms, “Autocorrelations of Binary Sequences and Run Structure,” arXiv:1206.4572, first posted 2012-06-20; *IEEE Transactions on Information Theory* 59 (2013), 4985–4993. https://arxiv.org/abs/1206.4572.
3. Y. Zhong, Z. Zhou and T. Jiang, “Research on perfect binary correlation sequences based on higher-order cumulant,” *EURASIP Journal on Wireless Communications and Networking* (2013), article 123. https://doi.org/10.1186/1687-1499-2013-123.
4. F. Caullery, E. F. Érard and F. Rodier, “Periodic autocorrelation of sequences,” arXiv:2410.11347, first posted 2024-10-15. https://arxiv.org/abs/2410.11347.
