# Exact plateau lifetimes and a quarter-atom limit for sliding sample maxima

## Finding

For any integer window width \(w\ge1\), consider the stationary sliding-window maximum
\[
M_t=\max\{X_t,X_{t+1},\ldots,X_{t+w-1}\},\qquad t\in\mathbb Z,
\]
of an independent, identically distributed sequence with any continuous marginal distribution. A new constant-value plateau starts at time zero on \(S=\{M_{-1}\ne M_0\}\); write \(U=\{M_0>M_{-1}\}\) for an upward start and \(D=\{M_0<M_{-1}\}\) for a downward start. Its duration is \(L=\min\{j\ge1:M_j\ne M_0\}\), an integer in \(\{1,\ldots,w\}\) on \(S\).

**Theorem (complete plateau-duration law).** The two start types have the same probability,
\[
\Pr(U)=\Pr(D)=\frac1{w+1},\qquad \Pr(S)=\frac2{w+1}.
\]
For every \(1\le\ell\le w\),
\[
\begin{aligned}
\Pr(L\ge\ell\mid U)&=\frac{w+1}{w+\ell},\\
\Pr(L\ge\ell\mid D)&=\frac{(w-\ell+1)(w+1)}{(w+\ell-1)(w+\ell)},\\
\Pr(L\ge\ell\mid S)&=\frac{w(w+1)}{(w+\ell-1)(w+\ell)},\\
\Pr(U\mid L\ge\ell,S)&=\frac{w+\ell-1}{2w}.
\end{aligned}
\]
In particular, the maximum-duration atom is
\[
\Pr(L=w\mid S)=\frac{w+1}{2(2w-1)}\longrightarrow\frac14.
\]
The expected durations conditional on type, with \(H_m=\sum_{j=1}^m 1/j\), are
\[
\begin{aligned}
\mathbb E[L\mid U]&=(w+1)(H_{2w}-H_w),\\
\mathbb E[L\mid D]&=(w+1)(1-H_{2w}+H_w),\\
\mathbb E[L\mid S]&=\frac{w+1}{2}.
\end{aligned}
\]
As \(w\to\infty\), \(L/w\mid S\) converges weakly to a law on \([0,1]\) with density \(2/(1+x)^3\) for \(0<x<1\) and an atom of mass \(1/4\) at \(x=1\). At the distinct sampling scheme of an arbitrary stationary time, the forward waiting time \(R=\min\{j\ge1:M_j\ne M_0\}\) instead has, for every integer \(0\le\ell\le w\),
\[
\Pr(R>\ell)=\frac{w-\ell}{w+\ell}.
\]
Consequently \(R/w\) tends to the continuous law with survival \((1-x)/(1+x)\) for \(0\le x\le1\), and \(\mathbb E[R]/w\to2\log2-1\).

## Assumptions and scope

The underlying sample is bi-infinite, iid and **atomless**. There is no moment, tail or density assumption. Probability statements about \(L\) are conditional on an actual change in the sliding maximum immediately before time zero; probabilities about \(R\) are unconditional at a stationary deterministic time. These two sampling schemes must not be interchanged. The limit \(w\to\infty\) concerns window width; there is no sample-size asymptotic required for the finite identities. The substantive statistical setting is the use of strongly overlapping block maxima, where repeated extreme observations create ties across adjacent windows even with atomless raw data.

## Proof

By the probability-integral transform and absence of ties, the relative ranks of any finitely many observations are uniform; work with iid \(V_i\sim\operatorname{Uniform}(0,1)\). The two windows at times \(-1\) and \(0\) share \(w-1\) observations and together contain \(w+1\) samples. They differ if and only if the greatest of those \(w+1\) samples is the outgoing \(V_{-1}\) (downward change) or incoming \(V_{w-1}\) (upward change). Every position is equally likely to carry the greatest sample, proving both type probabilities.

Conditional on an upward start, the incoming value \(A=V_{w-1}\) is the maximum of \(w+1\) uniforms, hence has density \((w+1)a^w\) on \((0,1)\). It is at the newest position and stays in the window through the next \(w-1\) slides. Its level remains the maximum for at least \(\ell\) plateau observations exactly when the next \(\ell-1\) new inputs are below \(A\). For \(1\le\ell\le w\),
\[
\Pr(L\ge\ell\mid U)=\mathbb E[A^{\ell-1}]=(w+1)/(w+\ell).
\]

Conditional on a downward start, \(V_{-1}\) is the greatest of \(w+1\) uniforms and the new maximum \(B\) is their second greatest. Thus \(B\) is \(\operatorname{Beta}(w,2)\), with density \(w(w+1)b^{w-1}(1-b)\). Independently of the order statistics, its location among the \(w\) current observations is uniform. For its value to persist for \(\ell\) plateau observations, its position must be among the \(w-\ell+1\) trailing positions, and each of \(\ell-1\) future independent inputs must be below \(B\). The two factors give
\[
\begin{aligned}
\Pr(L\ge\ell\mid D)
&=\frac{w-\ell+1}{w}\,\mathbb E[B^{\ell-1}]\\
&=\frac{w-\ell+1}{w}\,\frac{w(w+1)}{(w+\ell-1)(w+\ell)},
\end{aligned}
\]
including \(w=1\). Averaging the two equally likely types and applying Bayes' rule yields the stated unconditional-start survival probability and linear upward-type posterior. Every value necessarily leaves its length-\(w\) window after at most \(w\) observations, so \(L\le w\). At \(\ell=w\), its survival probability equals its terminal atom.

For integer-valued durations, \(\mathbb E[L\mid \cdot]=\sum_{\ell=1}^w\Pr(L\ge\ell\mid\cdot)\). Summing the upward expression yields \((w+1)(H_{2w}-H_w)\). The conditional-on-start survival function telescopes as \(w(w+1)[1/(w+\ell-1)-1/(w+\ell)]\), giving \(\mathbb E[L\mid S]=(w+1)/2\). This also agrees with the reciprocal of the start intensity \(2/(w+1)\), as required by stationary plateau counting. The downward mean follows by the equal-weight mixture.

At an unconditioned stationary time, the location of the maximum among the current \(w\) values is uniform and independent of its magnitude \(C\sim\operatorname{Beta}(w,1)\). Survival over the next \(\ell\) slides requires its location in the \(w-\ell\) positions that have not yet departed and the \(\ell\) new inputs all less than \(C\). Therefore, for \(0\le\ell\le w\),
\[
\Pr(R>\ell)=\frac{w-\ell}{w}\,\mathbb E[C^\ell]
=\frac{w-\ell}{w+\ell}.
\]

For each fixed \(x\in(0,1)\), insert \(\ell=\lfloor wx\rfloor+1\) in the survival formula to obtain \(\Pr(L/w>x\mid S)\to(1+x)^{-2}\); values above one have zero probability. The resulting limit has derivative density \(2/(1+x)^3\) on the interior and residual point mass \(1/4\) at one, proving weak convergence at its continuity points. The uniform-time formula similarly gives \(\Pr(R/w>x)\to(1-x)/(1+x)\) in the interior, without an endpoint atom. The limit of the means follows by bounded convergence or by integrating this last survival function. No finite-rank experiment is used to establish these arbitrary-width statements.

## Verification

The included standalone `verify_moving_max_plateaus.py` uses only the Python standard library. It enumerates every strict ranking of the \(2w+1\) input observations needed for \(w=1,2,3,4\), measures actual starts, up/down types and every survival event, then compares their exact fractions to the formulas. The recorded standalone execution passed **368,046 rank-permutation cases and 56 exact rational checks**, as reported by the program; these finite tests corroborate the proof but do not replace it. To reproduce, run `python3 verify_moving_max_plateaus.py` from the extracted directory.

## Relationship to prior work

Bücher and Haufs [1], first publicly submitted on 2025-02-20, analyze sliding and disjoint blockwise top-two order statistics, their likelihood estimators and their asymptotic statistical efficiency. That work supplies a direct reason to understand the fine dependence and repeated identical maximum values created by overlapping blocks. The present result instead gives exact finite-width, distribution-free durations and a geometric-type-origin limiting occupation law; it does **not** establish a new estimator or asymptotic inference guarantee. Alon and Feldheim [2] study general sliding-window processes and the occurrence of monotone runs, not this exact maxima-plateau classification. Baz and Pellerey [3] study **expanding-prefix** maximum processes and copula concordance, not fixed-width sliding maxima; their preprint appeared after the week-eligibility anchor and is cited only for comparison. Classical extreme-clustering/record literature does not itself provide the two start-type formulas or the random-time versus start-time law [4].

## Limitations

The theorem requires continuous iid raw observations. It need not hold unchanged for atoms, serial dependence, unequal window weights, irregular windows or other block statistics. The distinction between plateau starts and stationary observations is essential. The results describe equality of *observed sliding maxima*, not exceedance-cluster lengths at a fixed threshold or the lifetime of an expanding-prefix record. The exact formulas may have unlocated earlier equivalents in the extensive record-statistics or sliding-extreme literature; the claim of novelty is therefore bounded by the specific source comparisons and searches reported separately. No independent scholarly review has been completed.

## References

1. A. Bücher and E. Haufs, *Extreme Value Analysis based on Blockwise Top-Two Order Statistics*, arXiv:2502.15036, first version 20 February 2025, https://arxiv.org/abs/2502.15036 (full HTML version examined at https://arxiv.org/html/2502.15036v3).
2. N. Alon and O. N. Feldheim, *A note on general sliding window processes*, arXiv:1402.1975 (2014), https://arxiv.org/abs/1402.1975.
3. J. Baz and F. Pellerey, *Dependence properties between marginals of discrete-time maximum processes*, arXiv:2611.22599, first version 17 November 2026, https://arxiv.org/html/2611.22599v1.
4. P. Hall, L. Peng and Q. Yao, *Moving-maximum models for extrema of time series*, LSE Research Online Documents on Economics 6084 (2002), https://researchonline.lse.ac.uk/id/eprint/6084/.
