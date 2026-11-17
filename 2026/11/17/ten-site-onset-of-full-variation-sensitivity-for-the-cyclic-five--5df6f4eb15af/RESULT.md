# Ten-site onset of full variation sensitivity for the cyclic five-point median

## Finding

For every integer \(n\ge5\), let \(M_n:\mathbb R^n\to\mathbb R^n\) be the centered five-point cyclic running-median operator, and let \(V_n\) be cyclic total variation, as defined below. Its sharp two-input Lipschitz coefficient \(\Lambda_n\) satisfies
\[
\Lambda_n<5\quad(5\le n\le9),\qquad
\Lambda_n=5\quad(n\ge10).
\]
In fact, for \(5\le n\le9\) the quantitative upper estimate \(\Lambda_n\le\lfloor n/2\rfloor\) holds (and \(\Lambda_5=0\)). The value five is attained by distinct, finite real input pairs for **every** \(n\ge10\), not merely approached by a derivative limit. Thus ten sites are exactly the first cyclic sample size at which the five-site median achieves its full fivefold two-input variation amplification.

## Assumptions and scope

All indices are taken modulo \(n\). For real \(a=(a_0,\dots,a_{n-1})\), write
\[
(M_na)_i=\operatorname{median}\{a_{i-2},a_{i-1},a_i,a_{i+1},a_{i+2}\},\qquad
V_n(a)=\sum_{i=0}^{n-1}|a_{i+1}-a_i|.
\]
The median is the third order statistic; for \(n\ge5\) all five indices in each window are distinct. Define
\[
\Lambda_n=\sup_{V_n(a-b)>0}\frac{V_n(M_na-M_nb)}{V_n(a-b)}.
\]
The inputs are unrestricted real cyclic sequences. Translation by a common constant changes neither seminorm. The theorem concerns a **single** simultaneous filtering pass and perturbation variation, not the variation of each input separately.

## Proof

**1. Local selection and the universal fivefold bound.** Away from ties in the five-point windows, each output median is one of its input coordinates. Hence on each open ordering chamber the map is a linear selection operator \(S\), \((Sh)_i=h_{s_i}\), where the selected index \(s_i\) belongs to the cyclic window \(\{i-2,\ldots,i+2\}\). Fix an output edge joining \(i\) to \(i+1\). Choose integer representatives \(s_i\in[i-2,i+2]\), \(s_{i+1}\in[i-1,i+3]\). The elementary path inequality gives
\[
|h_{s_{i+1}}-h_{s_i}|\le\sum_{j\text{ between }s_i\text{ and }s_{i+1}}|h_{j+1}-h_j|.
\]
For any fixed input edge \(j\to j+1\), this path can traverse that edge only if the output edge index \(i\) belongs to \(\{j-2,j-1,j,j+1,j+2\}\), modulo \(n\). Consequently each input edge is charged at most five times, and \(V_n(Sh)\le5V_n(h)\). The running median is continuous and piecewise affine, so integrating chamber derivatives along an arbitrary line segment, then using the triangle inequality for \(V_n\), gives
\[
V_n(M_na-M_nb)\le5V_n(a-b)
\]
for all \(a,b\). Ties follow by approximation or almost-everywhere differentiation.

**2. The finite-cycle obstruction.** For any fixed linear selection matrix \(S\), the quotient seminorm \(V_n(h)\) identifies \(\mathbb R^n/\mathbb R\mathbf1\) with the mean-zero difference subspace \(\{d\in\mathbb R^n:\sum d_j=0\}\) equipped with \(\ell^1\)-norm. The extreme points of its unit ball are \((e_j-e_k)/2\), \(j\ne k\). Their cyclic discrete primitives, up to additive constants, are half of indicators of nonempty proper cyclic intervals. Thus the variation operator norm of \(S\) is attained by an interval indicator. Its image under \(S\) is binary, so it has at most \(2\lfloor n/2\rfloor\) cyclic jumps, whereas the input indicator has exactly two. It follows that \(V_n(Sh)\le\lfloor n/2\rfloor V_n(h)\). Integrating the chamber derivatives as in step 1 gives \(\Lambda_n\le\lfloor n/2\rfloor<5\) whenever \(n\le9\). For \(n=5\), every median window contains all five inputs, hence the output is constant and \(\Lambda_5=0\).

**3. Exact finite witnesses through nineteen sites.** Let \(a\) be the following integer sequences, let \(h_i=1\) for \(0\le i<\lfloor n/2\rfloor\) and \(h_i=0\) otherwise, and take \(b=a+\frac14h\). Each sequence has distinct integer entries, so the median selection is unchanged along the segment from \(a\) to \(b\). Directly sorting the five entries of each cyclic window yields \(V_n(h)=2\) and \(V_n(M_nb-M_na)=10/4\), giving ratio five:

| \(n\) | Sequence \(a\) in cyclic order |
|---|---|
| 10 | 4, 8, 10, 1, 5, 7, 2, 3, 9, 6 |
| 11 | 3, 6, 9, 11, 5, 7, 10, 2, 1, 4, 8 |
| 12 | 7, 11, 9, 1, 12, 4, 5, 2, 6, 3, 10, 8 |
| 13 | 8, 10, 3, 1, 11, 6, 5, 7, 12, 2, 9, 13, 4 |
| 14 | 10, 12, 4, 14, 5, 9, 3, 6, 1, 8, 2, 13, 7, 11 |
| 15 | 13, 4, 9, 1, 11, 3, 6, 5, 12, 2, 8, 15, 10, 14, 7 |
| 16 | 6, 12, 9, 13, 16, 4, 14, 7, 11, 5, 15, 2, 1, 8, 3, 10 |
| 17 | 10, 17, 6, 13, 4, 11, 15, 5, 8, 16, 3, 1, 2, 7, 14, 9, 12 |
| 18 | 6, 1, 4, 18, 11, 14, 9, 13, 10, 12, 8, 17, 3, 7, 15, 16, 2, 5 |
| 19 | 13, 18, 6, 2, 16, 19, 7, 3, 10, 9, 5, 11, 17, 4, 8, 1, 15, 14, 12 |

**4. Uniform finite witnesses for all larger cycles.** For every \(n\ge20\), set
\[
T=(31,44,7,92,38,40,4,60,25,32)
\]
and concatenate the ten entries of \(T\), the ten entries of \(T+100\), and, if \(n>20\), the \(n-20\) entries \(1000,1001,\ldots,1000+n-21\). Call the resulting integer vector \(a\). Let \(h_i=1\) on indices \(0,\ldots,4\) and \(15,\ldots,n-1\), and zero elsewhere. Then \(V_n(h)=2\). The median selection near the first boundary produces an alternating binary mask across five consecutive output edges, and the translated copy produces the same five alternations near the second boundary; all other output edges have constant masks. Explicitly, the masks on output centers \(2,3,4,5,6,7\) alternate \((1,0,1,0,1,0)\), and those on centers \(12,13,14,15,16,17\) alternate \((0,1,0,1,0,1)\). Thus \(V_n((h_{s_i})_i)=10\). The finite pair \(a,b=a+\frac14 h\) consequently has ratio exactly five. Combining steps 1–4 proves the theorem.

## Verification

The accompanying standalone Python file `checks/median_five_cycle.py` uses only the standard library. It performs exact integer and rational median computations for all ten finite witnesses \(10\le n\le19\), checks the uniform gadget at additional cycle lengths, and tests the combinatorial edge-multiplicity bound on random ordering chambers. The finite table is an explicitly replayable certificate; the unbounded claim for \(n\ge20\) follows from the proved two-gadget construction, not from numerical extrapolation. Run `python checks/median_five_cycle.py`.

## Relationship to prior work

The foundational running-median and stack-filter theory of Maragos and Schafer explains the nonlinear order-statistic construction. Arias-Castro and Donoho study median smoothing from a mean-square-risk perspective, whereas Little and Jones prove a **one-input** total-variation smoothing property for a three-point median in their Appendix A. Neither statement gives a five-point **two-input** variation modulus. Related exact three-point cyclic variation results have a different window length, and a broader-radius comparison available for lengths at least eight times the radius gives the five-point coefficient only once \(n\ge16\); it does not settle the new ten-site onset or the intermediate six cases \(10\le n\le15\). The new contribution is the **exact smallest saturation dimension** together with witnesses for the previously uncovered sizes, rather than rediscovery of the universal upper bound or large-cycle sharpness.

## Limitations

The claim is specific to real signals on cycles, uniform five-point centered medians, and cyclic total variation of **differences**. It does not calculate the exact Lipschitz coefficient for each \(5\le n\le9\), nor classify noncyclic boundary conventions, weighted medians, arbitrary radii, or repeated filtering. Historical-priority comparison is necessarily provisional, particularly for older unindexed median-filter analyses.

## References

- E. Arias-Castro and D. L. Donoho, *Does median filtering truly preserve edges better than linear filtering?* arXiv:math/0612422, first public preprint December 14, 2006. https://arxiv.org/abs/math/0612422
- M. A. Little and N. S. Jones, *Generalized methods and solvers for noise removal from piecewise constant signals. I. Background theory*, Proc. R. Soc. A 467 (2011), 3088–3114, Appendix A. https://pmc.ncbi.nlm.nih.gov/articles/PMC3191861/
- P. Maragos and R. W. Schafer, *Morphological Filters—Part 2: Their Relations to Median, Order-Statistic, and Stack Filters*, technical report (1987). https://drum.lib.umd.edu/items/95ac7d84-40fc-46bd-9e9e-936ef1bbcb34
- A. Restrepo and L. Chacón, *A smoothing property of the median filter*, IEEE Transactions on Signal Processing 42 (1994), 1553–1555. https://doi.org/10.1109/78.286974 (abstract consulted; full text not independently inspected).
