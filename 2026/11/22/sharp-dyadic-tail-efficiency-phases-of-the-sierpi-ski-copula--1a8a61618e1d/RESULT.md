# Sharp dyadic tail-efficiency phases of the Sierpiński copula

## Finding

Let \(\mathcal P\) consist of joint laws of three Uniform\([0,1]\) coordinates with every pair independent. Write \(M(t)=\sup_{\pi\in\mathcal P}\Pr_\pi(U_1\ge t,U_2\ge t,U_3\ge t)\), the sharp common-threshold bound. Write \(S(t)\) for that probability under the odd-parity Sierpiński coupling: independent uniforms \(X,Y\) and \(Z=1-(X\oplus Y)\), with exclusive-or on their binary digits.

The coupling attains \(M(t)\) for all \(0\le t\le1/2\). For \(p=1-t\in[2^{-(k+1)},2^{-k}]\), \(k\ge1\), the comparison is exactly
\[
S(t)=4^{-k}-3\,2^{-k}p+3p^2,\qquad
M(t)-S(t)=2(p-2^{-(k+1)})(2^{-k}-p).
\]
Thus in the upper half the coupling is optimal only at \(t=1-2^{-k}\), \(k\ge1\), and at the trivial endpoint \(t=1\). The sharp relative efficiency is \(\inf_{0\le t<1}S(t)/M(t)=3/4\), attained precisely at \(t=1-(2/3)2^{-k}\), \(k\ge1\).

Suboptimality persists for the explicit real-analytic, strictly increasing score \(f(x)=(1+\exp[-512(x-5/8)])^{-1}\): some \(\pi\in\mathcal P\) has
\[
\mathbb E_\pi\prod_{i=1}^3 f(U_i)-\mathbb E_{\mathrm{Sierpiński}}\prod_{i=1}^3 f(U_i)>1/128.
\]

## Assumptions and scope

Every two-dimensional marginal is the uniform product measure. No joint density, symmetry or conditional independence is assumed. Dyadic ambiguity in the binary expansion is immaterial on a null set. The odd-parity law is the maximizer for the linear score product \(xyz\) [1]; no universal maximizing property for increasing scores is assumed. The results concern one common threshold and three coordinates, not unequal thresholds, a coupling simultaneously maximizing all thresholds, or the exact logistic optimizer.

## Proof

**Benchmark envelope.** For \(p=1-t\) the threshold indicators are pairwise independent, with common marginal probability \(p\). The sharp upper bound for their triple intersection is
\[
r=\min\{p^2,1-3p+3p^2\}.
\]
This is the \(n=3\) equal-probability specialization of [2, Corollary 15(iii), (3.11)], also obtainable from the sharp two-binomial-moment bound [3, Eq. (1.7)]. To see the specialization directly, let \(r'\) be the probability of the all-ones pattern. Pair probabilities force \(r'\le p^2\); nonnegative probability of the all-zeros pattern forces \(r'\le 1-3p+3p^2\). For \(r'=r\), assign per-pattern probabilities by Hamming weight three, two, one and zero as
\[
r,\quad p^2-r,\quad p-2p^2+r,\quad 1-3p+3p^2-r.
\]
For \(p\le1/2\) these are \(p^2,0,p(1-p),(1-p)(1-2p)\); for \(p\ge1/2\) they are \(1-3p+3p^2,(1-p)(2p-1),(1-p)^2,0\). Hence they are nonnegative, sum to one with the respective multiplicities, and give the required single and pair probabilities. Given the binary pattern, draw the coordinates independently and uniformly on \([0,t)\) or \([t,1]\) according to the bit. The unconditional pairs are independent uniforms; the upper event has probability \(r\). The endpoints follow by uniformity. Thus \(M(t)=1-3t+3t^2\) on the lower half and \(M(t)=(1-t)^2\) on the upper half. This known event bound and its uniform lift are the benchmark, not the new extremum claimed here.

**Exact diagonal phases.** The binary digit triples of the Sierpiński law are independent across positions and uniform on \(\{111,100,010,001\}\). Each digit pair is uniform on four possibilities, giving independent uniform coordinate pairs. For \(t\le1/2\) the event that all coordinates are below \(t\) would require the forbidden first triple \(000\). Inclusion–exclusion gives \(S(t)=1-3t+3t^2\). For \(1/2\le t<1\) the upper event requires first triple \(111\), and conditional on that triple the rescaled remaining digits have the original law. Therefore \(S(t)=S(2t-1)/4\). On the stated interval of \(p\), iterate \(k\) times to obtain \(4^{-k}S(1-2^k p)\), where \(1-2^kp\in[0,1/2]\). Inserting the lower-half formula yields the polynomial and the factored deficit in the finding. These agree on shared endpoints, and \(S(1)=M(1)=0\) by continuity of the marginals.

**Exact relative minimum.** For \(L=2^{-k}\), \(L/2\le p\le L\), the expression above satisfies \(4S(t)-3p^2=(2L-3p)^2\). Since \(M(t)=p^2>0\), the ratio is at least \(3/4\), with equality precisely at \(p=2L/3\). The ratio is one on the lower half.

**Strict improvement for an analytic score.** At \(t_0=5/8\) the benchmark and Sierpiński tails are \(9/64\) and \(7/64\), respectively. For \(h=\mathbf1_{[t_0,1]}\), the logistic score in the finding obeys \(\int_0^1|f-h|<2/512\), by bounding the error on each side by \(\exp(-512|x-t_0|)\). Telescoping products of three factors bounded between zero and one shows that the expectation of the product changes by strictly less than \(6/512\) when replacing \(h\) with \(f\), under any coupling with uniform marginals. Apply this to the benchmark attaining law constructed above at \(t_0\) and to the Sierpiński law. Their difference for \(f\) is strictly greater than \(1/32-12/512=1/128\).

## Verification and relationship to other work

`python3 checker.py` uses exact rational arithmetic to check finite dyadic grids, the attaining Bernoulli law and the sharp ratio on selected scales. The continuum comparison and logistic bound follow from the analytic proof, not enumeration. The parity coupling and its optimality for \(xyz\) are from [1]. The known intersection bound [2,3] supplies the comparison envelope; the contribution is evaluation of the parity law against it on all scales, its exact relative minimum, and the analytic-score improvement. Finite copula interpolation [4] gives a general feasibility framework. The digit-linear score optimality in [5] concerns a different score class. The paper on diagonal plane sections [6] is related to the general copula viewpoint; priority beyond the sources inspected is not asserted.

## References

1. N. A. Gladkov, A. V. Kolesnikov and A. P. Zimin, *On multistochastic Monge–Kantorovich problem, bitwise operations, and fractals*, [arXiv:1803.10447](https://arxiv.org/abs/1803.10447).
2. K. Natarajan, A. K. Ramachandra and C. Tan, *Probability bounds for n random events under (n−1)-wise independence*, [arXiv:2211.01596](https://arxiv.org/abs/2211.01596), Corollary 15(iii), Eq. (3.11).
3. E. Boros and A. Prékopa, *Closed form two-sided bounds for probabilities that at least r and exactly r out of n events occur*, Mathematics of Operations Research 14 (1989), 317–342; the bound used is reproduced by A. K. Ramachandra and K. Natarajan, [arXiv:2006.00516v6](https://arxiv.org/abs/2006.00516v6), Eq. (1.7).
4. M. Omladič, M. Vuk and A. Zalar, *A linear programming approach to finite copula interpolation*, [arXiv:2611.14008](https://arxiv.org/abs/2611.14008).
5. D. V. Gvozdev and A. V. Kolesnikov, *On Pairwise Independent and Strongly Correlated Random Variables*, [arXiv:2611.20365v1](https://arxiv.org/abs/2611.20365), §3 and Theorem 4.1.
6. F. Durante, J. Fernández-Sánchez, J. J. Quesada-Molina and M. Úbeda-Flores, *Diagonal plane sections of trivariate copulas*, Information Sciences 333 (2016), 81–87, [DOI:10.1016/j.ins.2015.11.024](https://doi.org/10.1016/j.ins.2015.11.024).
