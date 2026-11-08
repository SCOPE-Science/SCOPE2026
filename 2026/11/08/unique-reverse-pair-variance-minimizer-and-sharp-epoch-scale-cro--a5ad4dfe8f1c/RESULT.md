# Unique reverse-pair variance minimizer and sharp epoch-scale crossover for equal-curvature reshuffling

## Finding

For scalar equal-curvature quadratic finite sums under fresh uniform random reshuffling, averaging the two full epoch maps obtained from a random permutation and any fixed rearrangement of that same permutation has a **unique variance-minimizing rearrangement: reversal**. The complete exact epoch and stationary variance ratios depend only on the sample size and normalized component step, not on the individual centers. For at least three components, reverse pairing produces strictly less than half of ordinary reshuffling's variance, with a sharp transition from a vanishing ratio when the normalized epoch step is small to the limiting ratio of one half when the epoch size grows with a fixed positive component step.

## Assumptions and scope

Let \(n\ge2\) be an integer, let \(a>0\), and choose real centers \(c_1,\ldots,c_n\) with \(s^2=n^{-1}\sum_i(c_i-\bar c)^2>0\), where \(\bar c=n^{-1}\sum_i c_i\). Define component losses \(f_i(x)=\frac a2(x-c_i)^2\). Let the component SGD step be \(\eta>0\), set \(q=1-\eta a\in(0,1)\), and let \(\pi\) be a uniform permutation of \(\{1,\ldots,n\}\). A single epoch starting from the same deterministic input \(x\) applies the component steps in the order \(\pi(1),\ldots,\pi(n)\), giving \(T_\pi(x)\).

For any **fixed permutation of positions** \(\sigma\) chosen independently of both \(\pi\) and the centers, consider the two-pass, averaged epoch map
\[
T_{\pi,\sigma}^{\mathrm{pair}}(x)=\tfrac12\bigl(T_\pi(x)+T_{\pi\circ\sigma}(x)\bigr).
\]
Both constituent full epochs start from the same input, not in sequence. The optimization over \(\sigma\) is *not* over all arbitrary permutation couplings, randomized couplings, gradient-dependent choices, or weighted averages. Fresh independent \(\pi\) is drawn for each new epoch when a stationary claim is made. This two-pass map is not the single-permutation reversal heuristic used in some optimization implementations.

Put \(r=1-q\), \(G_n=(1-q^{2n})/(1-q^2)\), and \(W_n=1-q^n\). The ordinary and optimally reverse-paired one-epoch variances (about their common mean) are exactly
\[
V_{\mathrm{RR}}=\frac{ns^2}{n-1}\left(r^2G_n-\frac{W_n^2}{n}\right),\qquad
V_{\mathrm{rev}}=\frac{ns^2}{n-1}\left(\frac{r^2}{2}(G_n+nq^{n-1})-\frac{W_n^2}{n}\right).
\]
These do not depend on the initial input. For every \(\sigma\),
\[
\operatorname{Var}_\pi\!\left(T_{\pi,\sigma}^{\mathrm{pair}}(x)\right)\ge V_{\mathrm{rev}},
\]
with equality **if and only if** \(\sigma(j)=n+1-j\) for all \(j\). In particular, if \(n=2\), then \(V_{\mathrm{rev}}=0\), and for every \(n\ge3\) the exact ratio \(R_n(q)=V_{\mathrm{rev}}/V_{\mathrm{RR}}\) obeys \(0<R_n(q)<1/2\).

The ratio has three sharp asymptotic regimes:
\[
R_n(1-r)=\frac{n^2-4}{60}r^2+O_n(r^3)\quad(r\downarrow0,\ n\text{ fixed}),
\]
\[
\lim_{n\to\infty}R_n(q)=\frac12\quad(q\in(0,1)\text{ fixed}),
\]
and, for each fixed \(\lambda>0\),
\[
\lim_{n\to\infty}R_n(1-\lambda/n)=\frac{B(\lambda)}{U(\lambda)},
\]
where
\[
U(\lambda)=\frac\lambda2(1-e^{-2\lambda})-(1-e^{-\lambda})^2,
\quad B(\lambda)=\frac\lambda4(1-e^{-2\lambda})+\frac{\lambda^2}{2}e^{-\lambda}-(1-e^{-\lambda})^2.
\]
Here \(U(\lambda)>B(\lambda)>0\). The crossover ratio tends to \(\lambda^2/60\) as \(\lambda\downarrow0\) and to \(1/2\) as \(\lambda\to\infty\).

For independent reshuffling between epochs, the same ratio \(R_n(q)\) holds for the two methods' *stationary mean-square errors around the common minimizer*. More precisely, if \(X_t\) is either epoch-end iterate and \(V\) its respective one-epoch variance,
\[
\mathbb E[(X_t-\bar c)^2]=q^{2nt}(X_0-\bar c)^2+
V\frac{1-q^{2nt}}{1-q^{2n}},
\quad \lim_{t\to\infty}\mathbb E[(X_t-\bar c)^2]=\frac{V}{1-q^{2n}}.
\]

## Proof

**Epoch representation.** Each component step sends \(z\) to \(qz+rc_i\). Composition gives
\[
T_\pi(x)=q^n x+\sum_{j=1}^n w_j c_{\pi(j)},
\quad w_j=rq^{n-j},\quad\sum_j w_j=W_n.
\]
The weights are strictly increasing because \(0<q<1\). In the averaged pair, the coefficient multiplying \(c_{\pi(k)}\) is \(v_k=\frac12(w_k+w_{\sigma^{-1}(k)})\), with \(\sum_k v_k=W_n\).

**Permutation variance and unique optimality.** For any deterministic weights \(v_k\), sampling without replacement gives
\[
\operatorname{Var}_\pi\!\left(\sum_k v_k c_{\pi(k)}\right)=
\frac{s^2}{n-1}\left(n\sum_kv_k^2-\Big(\sum_kv_k\Big)^2\right).
\]
Indeed, the diagonal covariances are \(s^2\) and the off-diagonal ones are \(-s^2/(n-1)\). As \(s^2>0\) and \(\sum v_k=W_n\) is fixed, minimizing variance is equivalent to minimizing \(\sum v_k^2\). The identity
\[
\sum_kv_k^2=\frac12\sum_kw_k^2+\frac12\sum_kw_k w_{\sigma^{-1}(k)}
\]
reduces this to the strict rearrangement inequality for a strictly increasing positive sequence: pairing largest with smallest is the unique minimizer. Hence only complete reversal is optimal, for all admissible centers and stepsizes.

**Exact variances and strict improvement.** The ordinary sum of squared weights is \(r^2G_n\). Under reversal, each cross-product is \(w_jw_{n+1-j}=r^2q^{n-1}\), so the paired squared-weight sum is \(r^2(G_n+nq^{n-1})/2\). Substituting into the permutation identity proves the formulas. The covariance between an ordinary epoch's random innovation and its reversed innovation equals
\[
\frac{s^2}{n-1}\bigl(n^2r^2q^{n-1}-W_n^2\bigr)<0,
\]
because \(W_n/n>r q^{(n-1)/2}\) is the *strict* arithmetic-geometric-mean inequality for the nonconstant \(w_j\). Consequently the paired variance is strictly below \(V_{\mathrm{RR}}/2\). For \(n=2\), all paired weights are equal, hence the paired variance vanishes. For \(n\ge3\) the first two reversed paired weights differ by \(r(1-q)(1-q^{n-2})/2>0\), so the paired variance is strictly positive.

**Small-step and dimension transitions.** For fixed \(n\), set \(t=n-j\) and \(m=(n-1)/2\). Expanding \(w_j=r(1-r)^t\) yields an ordinary centered weight of \(-r^2(t-m)+O_n(r^3)\), while the *reversal-averaged* centered weight is
\[
\frac{r^3}{2}\left((t-m)^2-\frac{n^2-1}{12}\right)+O_n(r^4).
\]
The uniform integer-position moments are
\[
\operatorname{Var}(t)=\frac{n^2-1}{12},\qquad
\operatorname{Var}\bigl((t-m)^2\bigr)=\frac{(n^2-1)(n^2-4)}{180}.
\]
Their squared centered norms give the fixed-\(n\) coefficient \((n^2-4)/60\). For fixed \(q\in(0,1)\), divide the exact paired and ordinary variance braces by their common dominant term \(r^2/(1-q^2)\); as \(n\to\infty\), the terms involving \(W_n^2/n\) and \(nq^{n-1}\) vanish, leaving \(1/2\).

For \(q_n=1-\lambda/n\), we have \(nr\to\lambda\), \(q_n^n\to e^{-\lambda}\), and
\[
nr^2G_n\longrightarrow\frac\lambda2(1-e^{-2\lambda}),\qquad
\frac{n^2r^2q_n^{n-1}}2\longrightarrow\frac{\lambda^2}{2}e^{-\lambda}.
\]
Multiplying each variance brace by \(n\) gives exactly \(U(\lambda)\) and \(B(\lambda)\). Positivity and strict ordering follow from the continuum permutation-weight variance of the nonconstant exponential kernel and its reversal average, or by limits of the strictly positive finite-\(n\) centered integrals: specifically \(U\) and \(B\) are the variances on \([0,1]\) of \(\lambda e^{-\lambda t}\) and \(\lambda(e^{-\lambda t}+e^{-\lambda(1-t)})/2\); neither kernel is constant for \(\lambda>0\), and their negative covariance yields \(0<B<U/2\). Taylor expansion at zero gives the \(\lambda^2/60\) ratio, and direct leading terms as \(\lambda\to\infty\) give \(1/2\).

**Stationary iterates.** Each new epoch has the affine form \(X_{t+1}=q^nX_t+(1-q^n)\bar c+\varepsilon_t\), where \(\varepsilon_t\) is centered, independent of the past, and of variance \(V\). Squaring the centered recursion, taking expectations and summing its geometric series gives the exact finite-time and stationary expressions.

## Verification

Run `python3 verify.py` from the directory containing the bundled verifier. It uses only the Python standard library. It checks rational exact variance identities against complete enumeration of the \(n!\) position permutations for \(2\le n\le7\); exhaustively searches all fixed position couplings for \(2\le n\le5\); verifies the finite-time epoch recurrence with rational arithmetic; and evaluates large-\(n\) and small-step limits numerically. An actual execution returned `PASS 460 exact/numerical assertions`. Enumeration and numerical limits are supplementary consistency checks; the argument above proves the universal claims.

## Relationship to prior work

Nguyen, Phan and Kalagnanam (2026), Theorems 3.6 and 3.9, introduce and bound the permutation sensitivity and variance of *paired-reversal epoch averages*, but do not optimize the reversed coupling over all fixed position relabelings or give the exact equal-curvature stationary law and epoch-scale crossover. Their bounded-gradient smoothness assumptions do not automatically encompass globally unbounded quadratic gradients; the present formulas are directly derived for the specified quadratic model. Domingo-Enrich (2022) analyzes stationary noise in shuffled SGD using a zero-order approximation and spectral densities, without the paired coupling optimality and crossover. Safran and Shamir (2020) develop sharp reshuffling rate bounds, not this exact antithetic two-pass comparison. Strict rearrangement and sampling-without-replacement covariance are classical ingredients, not independent novelty claims.

## Limitations

The comparison is restricted to scalar equal-curvature quadratics, positive contraction factor \(q\in(0,1)\), nonconstant centers, and a pair of *full* epochs started from the same input. Each paired epoch requires two full passes, so reduced variance is not a free per-gradient-computation gain. No claim is made for heterogeneous curvature, general nonlinear loss, higher-dimensional noncommuting Hessians, arbitrary couplings of two random permutations, negative steps, or the implemented single-pass adaptive reversal algorithm. No claim is made that existing order-reversal or rearrangement principles are new. Some potentially equivalent analyses outside indexed or accessible literature could exist. Verification is same-model only; no independent audit has been performed.

## References

1. Lam M. Nguyen, Dzung T. Phan, Jayant Kalagnanam, *Learning to Shuffle: Block Reshuffling and Reversal Schemes for Stochastic Optimization*, arXiv:2604.00260v1 (first public: 2026-03-31). https://arxiv.org/html/2604.00260v1
2. Carles Domingo-Enrich, *Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis*, arXiv:2206.00632v1 (2022). https://arxiv.org/html/2206.00632v1
3. Itay Safran and Ohad Shamir, *How Good is SGD with Random Shuffling?*, COLT 2020, PMLR 125. https://proceedings.mlr.press/v125/safran20a/safran20a.pdf
4. Jiaxiang Li, *Centered Permutation Prefixes for SGD with Random Reshuffling*, arXiv:2609.04578v1 (2026); only the abstract was accessible for this comparison. https://arxiv.org/abs/2609.04578
