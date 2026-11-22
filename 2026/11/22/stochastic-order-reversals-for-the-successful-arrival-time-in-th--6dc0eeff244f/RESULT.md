# Stochastic-order reversals for the successful arrival time in the two-choice secretary problem

## Finding

Consider the classical random-permutation secretary problem with one or two irrevocable opportunities to choose the overall best candidate. Let \(W_{1,N}\) and \(W_{2,N}\) be the positions of that candidate, **separately conditioned** on the optimal one-choice and two-choice procedures succeeding. Although the second procedure can succeed earlier, its conditional success-time law does **not** uniformly precede the first procedure in first-order stochastic order. The set of integer horizons where the two conditional laws are *incomparable* has natural density

\[
\boxed{d= e^{-1/2}(1-e^{-1}/2)^2=0.4039217492201783\ldots.}
\]

At the complementary natural density \(1-d\), the two-choice success time is stochastically earlier; the reverse stochastic order is impossible for all sufficiently large horizons.

More precisely, let \(1\le a<b<N\) be *arbitrary* two-choice rejected-count thresholds and compare the corresponding procedure with the one-choice rejected-count threshold \(b\). Put

\[
S=\sum_{j=b}^{N-1}\frac1j,\quad T=\sum_{j=b}^{N-1}\frac1{j^2},\quad V=\sum_{j=a}^{b-1}\frac1j,
\quad Z=\frac{S^2+T}{2}-\frac{S}{N-1}-V.
\]

The **exact finite-horizon criterion** is

\[
\begin{cases}
W_{2,N}\le_{\rm st}W_{1,N},&Z\le0,\\
W_{2,N}\text{ and }W_{1,N}\text{ are incomparable},&Z>0.
\end{cases}
\]

For the second case, the difference of the two conditional distribution functions changes sign once (from positive to negative) in the interior. These assertions are for \(1\le a<b<N\); the density assertion uses the nested, recursively compatible optimal thresholds in the cited work.

## Assumptions and scope

Candidates have distinct absolute ranks and appear in a uniformly random permutation of \(1,\ldots,N\). A record is a candidate with a better absolute rank than every earlier arrival. For one choice, reject positions \(1,\ldots,b\), then accept the first subsequent record. For two choices, reject positions through \(a\), allow one accepted record in positions \(a+1,\ldots,b\), and allow up to two accepted records after position \(b\). A global best is selected if and only if the procedure succeeds. Conditioning is on success **separately for each strategy**; no claim is made about coupled success times on a common permutation.

For the optimal comparison, \(b=b_N\) is the largest maximizing one-choice rejected-count threshold, while \(a=a_N\) is the largest maximizing two-choice early threshold with \(b_N\) held fixed. The threshold convention is the one in Grau Ribas and Sánchez Galán [1]. For sufficiently large \(N\), \(1\le a_N<b_N<N\). First-order stochastic order \(U\le_{\rm st}V\) means \(\Pr(U\le t)\ge\Pr(V\le t)\) for every real \(t\). Natural density is the limiting proportion of positive integer horizons \(N\le M\) as \(M\to\infty\).

## Proof

**1. Exact conditional success-by-position masses.** Let \(p_k(i)\) be the *unconditional* probability that the best overall candidate arrives at position \(i\) and is accepted by the procedure with \(k\) selections. Its position is uniform on \(\{1,\ldots,N\}\). Conditional on its position, the earlier prefix is a random permutation; in particular the probability of no record after rejected count \(b\) through position \(i-1\) is \(b/(i-1)\). Thus

\[
Np_1(i)=\begin{cases}0&i\le b,\\b/(i-1)&i>b.\end{cases}
\]

For two selections, the best at \(i\in(a,b]\) is selected if it is the first record after \(a\), with conditional probability \(a/(i-1)\). When \(i>b\), it is selected if either no record occurred in positions \(b+1,\ldots,i-1\), or exactly one selected record in that block was the first record after \(a\). For a candidate first selected at \(j\in(b,i)\), the latter disjoint event has conditional probability \(a/[(j-1)(i-1)]\). Consequently

\[
Np_2(i)=\begin{cases}
0&i\le a,\\a/(i-1)&a<i\le b,\\
\frac b{i-1}\left(1+\frac ab\sum_{j=b+1}^{i-1}\frac1{j-1}\right)&i>b.
\end{cases}
\]

Empty sums are zero. Summing these masses, and using \(\sum_{b\le j<k\le N-1}1/(jk)=(S^2-T)/2\), gives the *exact* success probabilities

\[
NP_1=bS,\qquad NP_2=bS+a\left(V+\frac{S^2-T}{2}\right).
\]

The normalized conditional success-time probability masses are \(p_k(i)/P_k\).

**2. A single exact stochastic-order test.** The ratio of the conditional masses for \(i>b\) is

\[
\frac{\Pr(W_2=i)}{\Pr(W_1=i)}
=\frac{P_1}{P_2}\left(1+\frac ab\sum_{j=b+1}^{i-1}\frac1{j-1}\right).
\]

It increases strictly with \(i\); its first value, at \(i=b+1\), is \(P_1/P_2<1\). On \(i\in(a,b]\), the two-choice law has positive mass but the one-choice law has none, so \(W_1\le_{\rm st}W_2\) is impossible. If the final ratio at \(N\) is at most one, every tail point has two-choice conditional mass at most one-choice conditional mass, proving \(W_2\le_{\rm st}W_1\). If the final ratio exceeds one, then at \(i=N-1\) the two-choice CDF is *smaller* (because its final mass is larger), while at \(i=b\) it is *larger*. Thus neither ordering holds. The increasing mass ratio makes the CDF difference decrease then increase toward zero, so this interior sign crossing is unique. Substituting the displayed expressions for \(P_1,P_2\) into the final ratio and cancelling the positive factor \(a\) shows that final ratio \(>1\) is **equivalent** to \(Z>0\). Equality belongs to the ordered case.

**3. Optimal threshold input and uniform harmonic expansion.** Put

\[
\alpha=e^{-1},\quad \beta=e^{-3/2},\quad
c_1=(1-\alpha)/2,\quad c_2=(1-e^{-1/2})/2.
\]

The published exact rounding theorem [1, Theorem 6.2 and Section 7.1] gives, outside a set of horizons of natural density zero,

\[
b_N=\lfloor\alpha N+c_1\rfloor,\qquad a_N=\lfloor\beta N+c_2\rfloor.
\]

Write \(u_N=\{\alpha N+c_1\}\), \(v_N=\{\beta N+c_2\}\) and therefore \(b_N=\alpha N+c_1-u_N\), \(a_N=\beta N+c_2-v_N\). Uniformly for these bounded displacements, Euler--Maclaurin expansion gives

\[
\begin{aligned}
S&=\log(N/b_N)+\tfrac12(1/b_N-1/N)+O(N^{-2}),\\
T&=1/b_N-1/N+O(N^{-2}),\\
V&=\log(b_N/a_N)+\tfrac12(1/a_N-1/b_N)+O(N^{-2}).
\end{aligned}
\]

For general bounded \(s_1=b_N-\alpha N\), \(s_2=a_N-\beta N\), substitution gives

\[
NZ=-2+\frac{3/2-2s_1}{\alpha}+\frac{s_2-1/2}{\beta}+O(N^{-1}).
\]

Finally substituting the exact correction constants from [1] reduces this to the simple fluctuation law

\[
\boxed{NZ=-1+\frac{2u_N}{\alpha}-\frac{v_N}{\beta}+O(N^{-1}).}
\]

The remainder is uniform for bounded displacements, and no control inside the exceptional rounding bands is needed for the natural-density conclusion.

**4. Equidistribution and the sharp density.** The numbers \(1,\alpha,\beta\) are linearly independent over the rationals by the Lindemann--Weierstrass theorem applied to distinct algebraic exponents \(0,-1,-3/2\). Hence Kronecker--Weyl gives equidistribution of \((u_N,v_N)\) on the unit square. The limiting sign test is

\[
v< 2e^{-1/2}u-e^{-3/2}.
\]

The right-hand side first becomes positive at \(u=\alpha/2\) and is strictly below one at \(u=1\), since \(2e^{-1/2}-e^{-3/2}<1\). Its subgraph therefore has area

\[
\int_{\alpha/2}^1\left(2e^{-1/2}u-e^{-3/2}\right)\,du
=e^{-1/2}(1-\alpha/2)^2.
\]

The separating line has area zero, as do the exceptional threshold bands by [1, Theorem 6.2 and Corollary 6.4]. Outside arbitrarily small neighborhoods of these null sets, the sign of \(Z\) agrees with the limiting sign for all sufficiently large \(N\). Equidistribution then gives the stated exact natural densities.

## Verification

Two exact optimal-cutoff examples illustrate opposite outcomes: with ten candidates, \((b,a)=(3,2)\) gives \(Z=268339/705600>0\), whereas with eleven candidates, \((b,a)=(4,2)\) gives \(Z=-1577189/6350400<0\). These are finite illustrations only.

The standalone Python 3 standard-library program `verify.py` computes exact success-by-position masses as rational numbers and independently enumerates all permutations for every pair of nondegenerate cutoffs through eight candidates. It also compares the exact harmonic criterion against directly computed conditional CDFs for cutoffs through sixty candidates. Its numerical larger-horizon test for the rounded cutoffs yields a frequency of \(0.40392623676859013\) on horizons \(500\) through \(250000\), close to the proven \(0.4039217492201783\ldots\); this numerical comparison does **not** prove the natural-density theorem. Execute from the directory containing `verify.py` with `python3 verify.py`. The infinite-horizon conclusion follows from the analytic expansion and the cited rounding/equidistribution results, not from numerical experiments.

## Relationship to prior work

Grau Ribas and Sánchez Galán [1] derive the exact multiple-choice winning-pattern totals, the optimal integer rounding shifts \(c_1,c_2\), and their joint frequencies. Those statements are required inputs here and are not claimed as new. The present claim concerns *success-conditioned arrival-time distributions*, an exact stochastic-order test for their full CDFs and the resulting curved (nonrectangular) equidistribution region with natural density \(e^{-1/2}(1-e^{-1}/2)^2\). The sharp density is not implied by merely knowing separate rounding frequencies or by comparing total success probabilities: one must establish the conditional index law and its final-mass sign criterion. Rapoport, Seale, and Spiliopoulos [2], particularly their two-choice secretary appendix, give total winning-event formulas and analyze stopping heuristics; they do not state this conditional stochastic-order classification or arithmetic-density law. Classical last-success and multiple-choice secretary theory supplies the threshold structure. Earlier priority in this wide literature is not excluded solely by the present literature search.

## Limitations

The positive-density statement applies to two choices compared with one, each using the recursively compatible optimal rule. The exact finite-cutoff criterion holds more generally for any \(1\le a<b<N\) but does not settle alternative tie-breaking, different objectives, nonuniform permutations, more than two choices, or a growing number of selection opportunities. No quantitative rate for the natural density is asserted. An uninspected historical source could conceivably imply the order comparison even if it does not state this particular constant. No independent external assessment has been performed.

## References

[1] J. M. Grau Ribas and R. Sánchez Galán, *Second-Order Threshold and Value Asymptotics in Multiple-Stopping Secretary Problems*, arXiv:2611.19541v1, first posted 2026-11-14. https://arxiv.org/html/2611.19541v1. Especially Sections 2, 6, and 7.1.

[2] A. Rapoport, D. A. Seale, and L. Spiliopoulos, *Progressive stopping heuristics that excel in individual and competitive sequential search*, Theory and Decision 94 (2023), 135–165, published online 2022-03-10, DOI:10.1007/s11238-022-09881-0. https://link.springer.com/article/10.1007/s11238-022-09881-0.

[3] T. S. Ferguson, *Who solved the secretary problem?*, Statistical Science 4 (1989), 282–289. Context for the one-choice problem.
