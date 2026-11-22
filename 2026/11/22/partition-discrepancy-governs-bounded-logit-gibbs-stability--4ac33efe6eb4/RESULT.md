# Partition discrepancy governs bounded-logit Gibbs stability

## Finding

For each integer \(n\ge2\), positive weights \(c_i\), inverse temperature \(\beta>0\), and \(R>0\), define the weighted exponential-normalization map

\[
G_{\beta,c}(x)_i=\frac{c_i\exp(\beta x_i)}{\sum_{j=1}^n c_j\exp(\beta x_j)},
\qquad X_R=\{x\in\mathbb R^n:\max_i x_i-\min_i x_i\le R\}.
\]

Write \(C=\sum_i c_i\), and define the *balanced-subset discrepancy*

\[
\rho(c)=\min_{\emptyset\ne S\subsetneq\{1,\ldots,n\}}
\left|1-\frac{2}{C}\sum_{i\in S}c_i\right|\in[0,1).
\]

The sharp global two-input mixed-norm coefficient is

\[
\boxed{\sup_{\substack{x,y\in X_R\\x\ne y}}
\frac{\|G_{\beta,c}(x)-G_{\beta,c}(y)\|_1}{\|x-y\|_\infty}
=\beta\operatorname{sech}^{2}\!\left(
\left(\operatorname{artanh}\rho(c)-\frac{\beta R}{2}\right)_+\right).}
\tag{1}
\]

Here \(a_+=\max\{a,0\}\), and \(\operatorname{sech}(t)=1/\cosh(t)\). In particular the coefficient attains the absolute upper bound \(\beta\) if and only if
\[
\beta R\ge 2\operatorname{artanh}\rho(c).
\tag{2}
\]

If all \(c_i\) are equal, then \(\rho(c)=0\) for even \(n\) and \(\rho(c)=1/n\) for odd \(n\). Hence every even class count has coefficient \(\beta\) for every positive budget. For odd class counts the first saturation budget is
\[
R_* = \beta^{-1}\log\frac{n+1}{n-1}.
\tag{3}
\]
The limiting coefficient as \(R\downarrow0\) is \(\beta(1-1/n^2)\) for odd \(n\), although the coefficient **at** \(R=0\) is exactly zero because the restricted map is constant on the diagonal.

Finally, exact saturation testing for arbitrary positive integer weights is NP-hard: given integers \(c_1,\ldots,c_n\), put \(C=\sum_i c_i\), \(\beta=1\), and rational \(R=1/C\). Then (1) equals one **if and only if** the integers admit an equal-sum two-part partition.

## Assumptions and scope

All weights are strictly positive real numbers; no normalization \(C=1\) is needed. Inputs are real and obey a bound on their **score diameter**, not on the diameter of the offset logits \(\log c_i+\beta x_i\). The input difference uses \(\ell^\infty\), the probability-output difference uses the unhalved \(\ell^1\) norm (twice the conventional total-variation distance). The exact coefficient is a supremum over distinct finite inputs in the same convex domain. The theorem concerns the map itself and not the Lipschitz coefficient of a preceding learned score-producing network. The positive-budget hypothesis is essential: \(X_0\) consists only of constant vectors, on which \(G_{\beta,c}\) is constant.

## Proof

**1. Exact derivative norm.** Put \(p=G_{\beta,c}(x)\). Direct differentiation gives, for \(h\in\mathbb R^n\),
\[
(DG(x)h)_i=\beta p_i\left(h_i-\sum_jp_jh_j\right).
\tag{4}
\]
The function \(h\mapsto\|DG(x)h\|_1\) is convex. Its maximum on the input cube \([-1,1]^n\) is therefore attained at a sign vector. If that vector equals \(+1\) on \(S\) and \(-1\) outside, with \(q=p(S)\), the weighted mean is \(2q-1\), and the output norm in (4) is exactly \(4\beta q(1-q)\). Consequently
\[
\|DG(x)\|_{\ell^\infty\to\ell^1}
=4\beta\max_{\emptyset\ne S\subsetneq[n]}p(S)(1-p(S))
=\beta\max_S\operatorname{sech}^2\!\left(\frac12\log\frac{p(S)}{1-p(S)}\right).
\tag{5}
\]
The empty and whole subsets contribute zero and cannot maximize, since all \(p_i>0\).

**2. Exact attainable subset odds.** Fix a proper nonempty subset \(S\), let \(A=\sum_{i\in S}c_i\), \(B=C-A\). For \(x\in X_R\), comparing any coordinate in \(S\) with any coordinate outside \(S\) yields
\[
e^{-\beta R}\frac AB\le\frac{p(S)}{1-p(S)}\le e^{\beta R}\frac AB.
\tag{6}
\]
Every odds ratio in this interval is attained: assign constant score \(t\) to coordinates in \(S\), score zero to the others, and vary \(t\in[-R,R]\). Hence the smallest attainable absolute log-odds for this subset is
\[
\left(\left|\log\frac AB\right|-\beta R\right)_+.
\tag{7}
\]
Since \(A+B=C\),
\[
\left|\log\frac AB\right|=2\operatorname{artanh}\left|1-\frac{2A}{C}\right|.
\tag{8}
\]
The hyperbolic tangent is strictly increasing on the nonnegative axis, so taking the minimum of (7) over all proper subsets and substituting in (5) gives
\[
\max_{x\in X_R}\|DG(x)\|_{\infty\to1}
=\beta\operatorname{sech}^2\!\left(\left(\operatorname{artanh}\rho(c)-\frac{\beta R}{2}\right)_+\right).
\tag{9}
\]

**3. The Jacobian supremum is the global two-input coefficient.** The set \(X_R\) is convex because its defining diameter is a convex function. Integrating (4) along the segment between arbitrary \(x,y\in X_R\) proves that the left side of (1) is no larger than (9). When \(R>0\), \(X_R\) has nonempty Euclidean interior. Every boundary optimizer of (9) can be approximated by interior points: multiply its scores, after subtracting a common constant, by \(1-\varepsilon\). At each interior point, sufficiently short differences in any prescribed sign direction stay in \(X_R\) and their quotient approaches the derivative norm. Continuity of (4) now proves the reverse inequality. For \(R=0\), a common additive score cancels in the numerator and denominator of \(G\), so its restriction to \(X_0\) is constant and the coefficient is zero.

**4. Parity and computational saturation.** Equal weights give \(\rho(c)=0\) for even \(n\), and \(1/n\) for odd \(n\), which substituted into (1) gives (2)–(3). For computational hardness, reduce positive-integer PARTITION. Given an instance of total weight \(C\ge2\), choose \(\beta=1\) and \(R=1/C\). A balanced proper subset gives \(\rho=0\) and coefficient one. If no subset balances, every proper subset sum \(A\) is an integer with \(|C-2A|\ge1\), so
\[
\left|\log\frac A{C-A}\right|
\ge\log\frac{C+1}{C-1}>\frac2C>R.
\tag{10}
\]
The strict middle inequality follows by applying \(\log((1+u)/(1-u))>2u\) at \(u=1/C\). Thus no subset can reach balanced probability under the prescribed budget, and the coefficient is strictly below one. The transformation uses rational data of polynomial bit length; deciding exact saturation is therefore NP-hard.

## Verification

An independent-of-formula numerical calculation of the Jacobian norm was performed by exhaustive enumeration of input sign vectors for small dimensions. A standalone standard-library Python checker, `checker.py`, compares that calculation against (1) for small positive integer weight vectors and multiple score diameters, verifies random finite input-pair inequalities, checks the near-boundary interior approximation, and exhaustively verifies the integer partition-gap criterion on small instances. Running `python3 checker.py` completed **10,099 supplementary assertions**. These finite calculations do not replace the quantified analytic proof above.

## Relationship to prior work

Gao and Pavel (first public 2017) formulate softmax as the gradient of log-sum-exp and provide Euclidean Lipschitz bounds; neither the mixed input-output norm nor a weight-dependent score-diameter coefficient is their result. Kanai et al. (2020) motivate bounded logits for robustness but do not calculate this sharp probability-map coefficient. Cohen and Fausti (first public 2023) establish a sharp bound for *finite* total-variation displacement in terms of Hilbert projective distance; their finite-space Lemma 5.2 includes a subset-mass formula that implies a related **fixed-probability local sensitivity** upon differentiation. This overlap is expressly acknowledged. Nair (2025) proves the sharp global \(\ell^p\)-to-\(\ell^p\) softmax bound of one-half, a different norm pairing. The present claim optimizes the \(\ell^\infty\)-to-\(\ell^1\) derivative simultaneously over a weighted, finite score-diameter domain and identifies its subset-partition saturation boundary and NP-hard exact decision problem. An unnoticed equivalent consequence of general earlier sensitivity theory remains a priority risk.

## Limitations

The formula does not assert a dimension-free stability improvement for all logit maps: for balanced priors and any positive budget it reaches the unrestricted upper bound. The integer input hardness concerns deciding **exact equality** to that upper bound, not numerical approximation at fixed tolerance or the complexity of a known partition. The degeneracy at \(R=0\) must not be replaced by its one-sided positive-budget limit. No assertion is made for a learned network preceding \(G\), and no independent mathematical audit has been performed.

## References

- B. Gao and L. Pavel, *On the Properties of the Softmax Function with Application in Game Theory and Reinforcement Learning*, arXiv:1704.00805, first public 2017-04-03, https://arxiv.org/abs/1704.00805.
- S. Kanai et al., *Constraining Logits by Bounded Function for Adversarial Robustness*, arXiv:2010.02558, first public 2020-10-06, https://arxiv.org/abs/2010.02558.
- S. N. Cohen and E. Fausti, *Hyperbolic contractivity and the Hilbert metric on probability measures*, arXiv:2309.02413, first public 2023-09-05, https://arxiv.org/abs/2309.02413.
- P. Nair, *Softmax is \(1/2\)-Lipschitz: A tight bound across all \(\ell_p\) norms*, arXiv:2510.23012, first public 2025-10-27, https://arxiv.org/abs/2510.23012.
