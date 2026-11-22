# Sharp three-regime Kolmogorov constants for discretized inverse-gamma maxima

## Finding

Let \(M_n\) be the maximum of \(n\) independent integer-floor inverse-gamma observations. Its normalized distribution converges to a Fréchet law, but the *sharp uniform error constant* undergoes a three-way transition at shape one. With the notation below, define the Kolmogorov error
\[
K_n=\sup_{x\in\mathbb R}\left|\Pr\left(\frac{M_n}{a_n}\le x\right)-G_\alpha(x)\right|.
\]
For every fixed pair of positive shape and scale parameters,
\[
\boxed{
\begin{array}{ll}
\displaystyle\lim_{n\to\infty}nK_n=2e^{-2},&0<\alpha<1,\\[5pt]
\displaystyle\lim_{n\to\infty}nK_n=\frac{4e^{-2}}{\beta},&\alpha=1,\\[7pt]
\displaystyle\lim_{n\to\infty}n^{1/\alpha}K_n=
\alpha c^{-1/\alpha}\left(1+\frac{\beta}{\alpha+1}\right)
\left(1+\frac1\alpha\right)^{1+1/\alpha}e^{-1-1/\alpha},&\alpha>1.
\end{array}}
\]
These are strict, positive asymptotic equivalents, not only upper bounds. The source distribution, its floor discretization, and its Fréchet first-order limit are existing concepts; the claimed result is the exact global-error classification.

## Assumptions and scope

Fix \(\alpha>0\) and \(\beta>0\), without allowing the parameters to vary with sample size. For each integer \(n\ge1\), the independent parent observations have density
\[
f_Y(y)=\frac{\beta^\alpha}{\Gamma(\alpha)}y^{-\alpha-1}e^{-\beta/y},\qquad y>0.
\]
Set \(X_i=\lfloor Y_i\rfloor\in\{0,1,2,\ldots\}\), \(M_n=\max_{1\le i\le n}X_i\),
\[
c=\frac{\beta^\alpha}{\Gamma(\alpha+1)},\quad a_n=(cn)^{1/\alpha},\quad G_\alpha(x)=\begin{cases}e^{-x^{-\alpha}},&x>0,\\0,&x\le0.\end{cases}
\]
This is a Kolmogorov-distance statement about the entire distribution, not just pointwise convergence or a threshold-exceedance fit. The integer-floor convention is essential: rounding to the nearest integer changes the constants.

## Proof

**1. Tail and smooth maximum.** Let \(F\) be the continuous inverse-gamma distribution function, and let \(H_n(x)=F(a_nx)^n\) for positive \(x\), extended by zero at nonpositive \(x\). The incomplete-gamma integral at the origin gives, as \(y\to\infty\),
\[
1-F(y)=\frac{1}{\Gamma(\alpha)}\int_0^{\beta/y}u^{\alpha-1}e^{-u}\,du
=c y^{-\alpha}\left(1-\frac{\alpha\beta}{(\alpha+1)y}+O(y^{-2})\right).
\]
For every compact subinterval of \((0,\infty)\), insert this expansion into \(n\log F(a_nx)\), obtaining uniformly
\[
\log H_n(x)=-x^{-\alpha}
+\frac{\alpha\beta}{(\alpha+1)a_n}x^{-\alpha-1}
-\frac1{2n}x^{-2\alpha}
+O(a_n^{-2}+n^{-1}a_n^{-1}+n^{-2}). \tag{1}
\]
Consequently, as \(n\to\infty\), on each such compact set,
\[
\begin{split}
 n\big(H_n(x)-G_\alpha(x)\big)&\longrightarrow-\tfrac12G_\alpha(x)x^{-2\alpha},&&0<\alpha<1,\\
 a_n\big(H_n(x)-G_\alpha(x)\big)&\longrightarrow\frac{\alpha\beta}{\alpha+1}G_\alpha(x)x^{-\alpha-1},&&\alpha>1.
\end{split}\tag{2}
\]
At \(\alpha=1\), the inverse-gamma parent is exactly inverse-exponential: \(F(y)=e^{-\beta/y}\) and \(a_n=\beta n\). Hence \(H_n(x)=G_1(x)\) for **every** positive \(x\) and every \(n\); the two displayed terms in (1) cancel exactly.

The convergences in (2) are uniform over \(x>0\), and the derivatives satisfy
\[
\sup_{x>0}|H_n'(x)-G_\alpha'(x)|\longrightarrow0.
\tag{3}
\]
Here are explicit tail controls that justify both extensions beyond compact sets. Choose \(y_0>0\) large enough that for \(y\ge y_0\) the survival function is between fixed positive multiples of \(c y^{-\alpha}\) and the tail remainder in (1) is bounded by a constant times \(y^{-\alpha-1}\). In the region \(a_nx\ge y_0\), both \(H_n(x)\) and \(G_\alpha(x)\) are bounded above by \(e^{-C x^{-\alpha}}\) for some \(C>0\), while their derivatives are bounded by \(C' x^{-\alpha-1}e^{-C x^{-\alpha}}\). Applying \(|e^u-e^v|\le |u-v|e^{\max(u,v)}\) to the logarithmic expansion, with the same survival bounds, controls the scaled differences in (2) by sums of constants times \(x^{-\alpha-1}e^{-C x^{-\alpha}}\), \(x^{-2\alpha}e^{-C x^{-\alpha}}\) and higher-order analogues. All these envelopes vanish as \(x\to0\) and as \(x\to\infty\). When \(a_nx<y_0\), use \(H_n(x)\le F(y_0)^n\), \(G_\alpha(x)\le e^{-cn/y_0^\alpha}\), and \(H_n'(x)\le na_n \|f_Y\|_\infty F(y_0)^{n-1}\), exponentially negligible even after either scaling. This proves (2) uniformly and (3) by the same compact/tail argument.

**2. Exact lattice displacement.** For every \(x\ge0\), define
\[
d_n(x)=\lfloor a_nx\rfloor+1-a_nx\in(0,1].
\]
Continuity of the inverse-gamma parent implies the *exact* identity
\[
\Pr(M_n/a_n\le x)=F(\lfloor a_nx\rfloor+1)^n
=H_n\big(x+d_n(x)/a_n\big).
\tag{4}
\]
By the fundamental theorem of calculus and (3), uniformly for \(x\ge0\),
\[
\Pr(M_n/a_n\le x)-H_n(x)
=\frac{d_n(x)}{a_n}G_\alpha'(x)+o(a_n^{-1}).
\tag{5}
\]
The function \(G_\alpha'\), extended continuously by zero at the origin, is uniformly continuous on \([0,\infty)\). Combining (2), the exact shape-one identity, and (5) gives the following **uniform-in-\(x\)** leading formulas:
\[
\begin{array}{ll}
\displaystyle n\left[\Pr(M_n/a_n\le x)-G_\alpha(x)\right]
=-\frac12G_\alpha(x)x^{-2\alpha}+o(1),&0<\alpha<1,\\[6pt]
\displaystyle a_n\left[\Pr(M_n/a_n\le x)-G_1(x)\right]
=d_n(x)G_1'(x)+o(1),&\alpha=1,\\[6pt]
\displaystyle a_n\left[\Pr(M_n/a_n\le x)-G_\alpha(x)\right]
=\left(d_n(x)+\frac\beta{\alpha+1}\right)G_\alpha'(x)+o(1),&\alpha>1.
\end{array}\tag{6}
\]
For \(x<0\), both CDFs vanish; at \(x=0\), \(\Pr(M_n/a_n\le0)=F(1)^n\), exponentially negligible under either scaling. The right-hand side of the first formula is understood by continuous extension at zero.

**3. Optimization and attainment.** For \(0<\alpha<1\), maximize \(\frac12e^{-x^{-\alpha}}x^{-2\alpha}\) over positive \(x\). Setting \(u=x^{-\alpha}\), the maximum of \(u^2e^{-u}/2\) is \(2e^{-2}\), attained at \(u=2\). Since (6) holds uniformly, this is the exact limit of \(nK_n\).

For \(\alpha\ge1\), differentiate \(G_\alpha\):
\[
G_\alpha'(x)=\alpha x^{-\alpha-1}e^{-x^{-\alpha}},\quad
\sup_{x>0}G_\alpha'(x)=\alpha\left(1+\frac1\alpha\right)^{1+1/\alpha}e^{-1-1/\alpha},
\]
with the unique maximum at \(x_*=(1+1/\alpha)^{-1/\alpha}\). In (6), \(d_n(x)\le1\), giving the upper bounds. For the matching lower bound, choose integers \(j_n\) with \(j_n/a_n\to x_*\), and set \(x_n=j_n/a_n\). Then \(d_n(x_n)=1\), which attains the limiting supremum. Multiply the result for \(\alpha=1\) by \(n/a_n=1/\beta\), and for \(\alpha>1\) by \(n^{1/\alpha}/a_n=c^{-1/\alpha}\). The three stated constants follow. \(\square\)

## Verification

The accompanying `check.py` uses the exact inverse-gamma CDF through a regularized incomplete gamma function and compares the sampled finite-grid Kolmogorov error against the proved asymptotic constants. The sample pairs \((\alpha,\beta)=(0.5,2),(1,2),(2,2),(3,0.5)\) at \(n=500,5000,20000\) approach the respective predictions. It samples lattice sites rather than exhausting all countable sites and **does not provide an independent proof or certified finite-sample supremum**. The argument in the Proof section is the infinite-domain justification.

## Relationship to prior work

Hitz, Davis and Samorodnitsky (2017, later printed 2024) formulate discrete maximum-domain and peak-over-threshold approximations, explicitly simulating \(X=\lfloor Y\rfloor\) for inverse-gamma \(Y\). Their theorems concern tail/exceedance models and first-order domain-of-attraction conditions, not the sharp global normalized-maximum Kolmogorov constant in all three shape regimes. Nadarajah and Lyu (2023) study a discrete inverse-gamma family and its insurance-data fit and tail properties, but do not derive these max-sample uniform error equivalents. Shimura (2012) supplies general discretization/maximum-domain criteria. Classical second-order extreme-value theory addresses convergence rates more broadly and is not claimed as new here; this result supplies explicit sharp constants and isolates a cancellation peculiar to shape one.

## Limitations

The parameters are fixed as \(n\to\infty\); no uniformity over parameter neighborhoods of shape one or inference from estimated shape is established. The constants pertain to integer floors and the scaling \(a_n=(cn)^{1/\alpha}\); other discretizations or second-order centering change them. General extreme-value convergence and the distribution family are known. The historical-priority comparison for Shimura's original article and some early rate literature is limited to accessible abstracts because their full texts could not be inspected. No claim of exclusive novelty or external verification is made.

## References

1. A. Hitz, R. A. Davis and G. Samorodnitsky, *Discrete Extremes*, preprint July 17, 2017, arXiv:1707.05033. Full accessible text: https://ar5iv.labs.arxiv.org/html/1707.05033 .
2. S. Nadarajah and J. Lyu, *New discrete heavy tailed distributions as models for insurance data*, PLOS ONE 18 (2023), e0285183, https://doi.org/10.1371/journal.pone.0285183 .
3. T. Shimura, *Discretization of distributions in the maximum domain of attraction*, Extremes 15 (2012), 299–317, https://doi.org/10.1007/s10687-011-0137-7 .
4. R. A. Davis, *The rate of convergence in distribution of the maxima*, Statistica Neerlandica 36 (1982), 31–35, https://doi.org/10.1111/j.1467-9574.1982.tb00772.x .
