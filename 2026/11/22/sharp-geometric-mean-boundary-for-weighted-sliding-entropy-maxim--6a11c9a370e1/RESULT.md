# Sharp geometric-mean boundary for weighted sliding entropy maxima in path variation

## Finding
For every integer \(n\ge6\), fixed positive weights \(a,b,c\), and temperature \(\tau>0\), consider the full-window entropy-smoothed maximum
\[
(Fx)_i=\tau\log\!\left(ae^{x_i/\tau}+be^{x_{i+1}/\tau}+ce^{x_{i+2}/\tau}\right),\qquad 1\le i\le n-2.
\]
For real vectors of length \(m\), write \(V_m(h)=\sum_{j=1}^{m-1}|h_{j+1}-h_j|\). The sharp **two-input** path-variation coefficient, over all finite real inputs, is
\[
\boxed{K(a,b,c)=\sup_{V_n(x-y)>0}\frac{V_{n-2}(Fx-Fy)}{V_n(x-y)}
=1+2\frac{(\sqrt{ac}-b)_+}{\sqrt{ac}+b}.}
\]
Consequently, two-input variation nonexpansivity holds **exactly** for log-concave three-tap weights, \(b^2\ge ac\). Whenever this condition holds, finite pairs attain the sharp coefficient \(1\). When \(b^2<ac\), the coefficient is strictly larger than one and is approached but **never attained** by any finite pair. The result is independent of temperature and path length within the stated range. As the middle weight decreases to zero relative to its neighbors, the sharp amplification approaches three.

## Assumptions and scope
Every input coordinate is an arbitrary finite real number; no monotonicity or positivity restriction is imposed on signals. The three *within-window* weights are fixed by relative position, not by absolute input site. The output has exactly \(n-2\) sites and does not pad or cyclically wrap the input. All variation seminorms use unweighted adjacent differences. The coefficient is a two-input Lipschitz bound, not merely a one-input estimate. Constants in the input pass to constants in the output; the quotient therefore makes sense modulo additive constants.

## Proof
**1. Derivative and step columns.** Set \(u_j=e^{z_j/\tau}>0\) for a fixed signal \(z\). Its Jacobian \(J_z\) has row \(i\) equal to the probability distribution on the ordered triple \((i,i+1,i+2)\) proportional to \((a u_i,b u_{i+1},c u_{i+2})\), because differentiation of the logarithm cancels \(\tau\). Let \(h^{(k)}_j=\mathbf1_{\{j\ge k\}}\), for \(2\le k\le n\). The step vectors together with constants span the input and their coefficients are the input adjacent differences. Put
\[
H_i(k)=(J_z h^{(k)})_i
=\frac{\sum_{j\in\{i,i+1,i+2\}:j\ge k}w_{j-i}u_j}
{a u_i+b u_{i+1}+c u_{i+2}},\quad (w_0,w_1,w_2)=(a,b,c).
\]
As the window moves right, \(H_i(k)\) has successive values \(0\), \(p\), \(q\), \(1\), after discarding entries whose windows lie outside the finite path. Specifically, the only potentially descending pair is at \(i=k-2,k-1\). Write \(X=u_{k-1}\), \(Y=u_k\); then dropping the additional left site and ignoring the additional right site yields
\[
 p\le P=\frac{cY}{bX+cY},\qquad q\ge Q=\frac{bY}{aX+bY}.
\]
The two other steps in the tail-probability profile are always nonnegative. Therefore the total variation in \(i\) of each step column is at most \(1+2(P-Q)_+\). This also covers truncated boundary profiles, because adjoining the missing leading zero and trailing one can only increase a profile's total variation.

**2. Exact overlap defect.** Elementary algebra gives
\[
P-Q=\frac{(ac-b^2)XY}{(bX+cY)(aX+bY)}.
\]
If \(b^2\ge ac\), this is nonpositive. Otherwise, the arithmetic-geometric mean inequality yields
\[
\frac{(bX+cY)(aX+bY)}{XY}
=ab\frac XY+(ac+b^2)+bc\frac YX
\ge(\sqrt{ac}+b)^2.
\]
Equality occurs precisely when \(X/Y=\sqrt{c/a}\). Thus the exact largest possible overlap reversal is
\[
\delta=\max\left\{0,\frac{\sqrt{ac}-b}{\sqrt{ac}+b}\right\}.
\]
The step decomposition consequently shows \(V_{n-2}(J_z h)\le(1+2\delta)V_n(h)\) for every real \(h\) and every finite \(z\).

**3. Global bound.** For arbitrary finite input pairs set \(h=y-x\). By the fundamental theorem of calculus,
\[
F(y)-F(x)=\int_0^1J_{x+th}h\,dt.
\]
The triangle inequality for adjacent variation and the universal Jacobian estimate from step 2 give \(V_{n-2}(F(y)-F(x))\le(1+2\delta)V_n(y-x)\).

**4. Sharpness and attainment.** Work at the interior cut \(k=4\), possible because \(n\ge6\). The first output window lies wholly to the left of the cut and the fourth wholly to its right; the associated step-column profile begins at zero and ends at one. When \(b^2\ge ac\), all intervening steps are nonnegative, so the variation of this step column equals one for **every** finite signal. More strongly, if \(y-x\) is any nonzero multiple of the suffix step \(h^{(4)}\), integration along the input segment preserves monotonicity of the output difference, which equals zero in the first window and the chosen step height in the fourth and later windows. Hence equality in the global Lipschitz bound is attained.

If \(b^2<ac\), choose positive exponentials at positions three and four satisfying \(u_3/u_4=\sqrt{c/a}\); make \(u_2\) and \(u_5\) tend to zero while leaving all other exponentials fixed and positive. The successive step-column values tend to \((0,P,Q,1,\ldots,1)\), and \(P-Q\to\delta>0\). Thus its derivative variation tends to \(1+2\delta\). Taking a sufficiently small positive step perturbation in the input turns these derivatives into genuine finite two-input quotients arbitrarily close to this value. For any fixed finite signal, \(u_2,u_5>0\), so the potential reversal is **strictly** less than \(\delta\). All finitely many derivative step columns are therefore strictly below \(1+2\delta\); this strict bound remains uniform along the compact segment joining two finite inputs. Consequently no finite pair attains the superunit supremum. This completes the proof.

## Verification
The standalone `check_weighted_lse.py` checks the Jacobian step-column norm, randomized two-input path-variation inequalities, near-extremal concentration patterns, and finite-pair equality for log-concave weights, for lengths six through twenty-two. It passed \(9{,}800\) random derivative/finite-pair tests, \(48\) near-sharpness checks, and \(12\) finite equality checks. Run `python check_weighted_lse.py` using Python's standard library. These finite tests corroborate the independent, quantified analytical proof and are not an exhaustive proof.

## Relationship to prior work
Nesterov's 2003 mathematical-programming preprint derives entropy-based log-sum-exp smoothing of maxima and its softmax gradient, but no moving weighted-window variation norm. Saumard and Wellner's 2014 review identifies discrete log-concavity with monotone likelihood ratio and Pólya-frequency order two; this explains the *nonexpansive side* qualitatively, not the exact amplification beyond that boundary or finite attainment status. A separate mathematical result on **cyclic** log-sum-exp windows assumes weights attached to **absolute sites** and derives a nonexpansivity-and-attainment classification; those site weights remain identical on overlapping sites, whereas the present weights shift by relative position. It therefore cannot imply the superunit law for non-log-concave relative-position weights. Previous sharp results on weighted moving isotonic regression use weighted least-squares projection and different Jacobians and constants. The geometric-mean threshold is shared, but not a theorem transfer between these nonlinear maps.

## Limitations
This theorem covers exactly three-point full windows on finite open paths of length at least six, fixed strictly positive position weights, and unweighted real adjacent variation. Short paths, longer or data-dependent windows, time-varying weights, cyclic topology, arbitrary graph neighborhoods and multivariate inputs are not classified. Sharpness on the expansive side is an unattained supremum, not a finite equality case. Literature coverage is bounded by the cited and indexed material; equivalent older monotone-kernel literature may be unindexed. Independent validation has not occurred.

## References
1. Yu. Nesterov, *Smooth minimization of non-smooth functions*, CORE Discussion Paper 2003/12, original dated public preprint January 10, 2003, https://research.dial.uclouvain.be/bitstreams/5e279fca-57a4-4476-9fe8-e8df213808c4/download . Especially Section 4.1, Lemma 4.
2. A. Saumard and J. Wellner, *Log-concavity and strong log-concavity: a review*, arXiv:1404.5886v1, April 23, 2014, https://arxiv.org/abs/1404.5886 . Especially Proposition 2.3 on monotone likelihood ratios.
3. *Sharp variation nonattainment threshold for cyclic entropy-smoothed maxima*, previously published result, full scientific statement and proof, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-sharp-variation-nonattainment-threshold-for-cyclic-entropy-smoot--67758c789c79/RESULT.md .
