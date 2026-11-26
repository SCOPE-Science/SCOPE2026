# A multivariate Laplace fluctuation law for coupon frequencies at completion

## Finding

Suppose there are \(n\ge2\) equally probable coupon types; independent coupons are drawn until all types have appeared. Write \(W_n\) for the number of draws and \(K_{n,r}\) for the number of types represented exactly \(r\) times among the first \(W_n\) draws. For any **fixed** positive integer \(R\), define
\[
G_n=\frac{W_n}{n}-\log n,\qquad
M_{n,r}=\frac{e^{-G_n}}{r!}\left(\frac{W_n}{n}\right)^r,\qquad
Y_{n,r}=\frac{K_{n,r}-M_{n,r}}{(\log n)^{r/2}}\quad(1\le r\le R).
\]
Then, jointly as \(n\to\infty\),
\[
(G_n,Y_{n,1},\dots,Y_{n,R})\ \xrightarrow{\ d\ }
\left(-\log E,\sqrt{E}Z_1,\sqrt{\frac{E}{2!}}Z_2,\dots,\sqrt{\frac{E}{R!}}Z_R\right),
\]
where \(E\sim\operatorname{Exp}(1)\), the variables \(Z_1,\dots,Z_R\) are independent standard normal variables, and the Gaussian vector is independent of \(E\). In particular the unconditioned frequency residuals have the multivariate Laplace-type characteristic function
\[
\mathbb{E}\exp\left(i\sum_{r=1}^{R}\theta_rY_r\right)
=\left(1+\frac12\sum_{r=1}^{R}\frac{\theta_r^2}{r!}\right)^{-1}\quad(\theta_1,\dots,\theta_R\in\mathbb{R}).
\]
The coordinates are conditionally independent given the Gumbel completion-time limit, but not jointly independent without that conditioning.

## Assumptions and scope

Each of the \(W_n\) sampled types is independent and uniform on \(\{1,\dots,n\}\). The integer \(R\) is fixed as \(n\to\infty\); no assertion is made for a dimension increasing with \(n\), unequal type probabilities, or higher collection quotas. The random centering \(M_{n,r}\) depends on the **observed** stopping time. Deterministic centering is not equivalent, since first-order fluctuations are of order \((\log n)^r\), larger than the residual scale \((\log n)^{r/2}\).

## Proof

**1. Independent Poisson streams and the exact conditional law.** Run an independent rate-one Poisson process for each type, and merge the streams. The merged process has rate \(n\), with independent uniform coupon marks. Let \(E_i\) be the first time type \(i\) appears, and put \(\tau_n=\max_{1\le i\le n}E_i\). The \(E_i\) are independent unit exponentials. Thus \(U_n=e^{-\tau_n}\) has the \(\operatorname{Beta}(1,n)\) law, and
\[
\mathbb P\{nU_n>x\}=\left(1-\frac{x}{n}\right)^n\longrightarrow e^{-x}\quad(x\ge0).
\]
Consequently \(nU_n\Rightarrow E\sim\operatorname{Exp}(1)\) and \(\tau_n-\log n=-\log(nU_n)\Rightarrow-\log E\).

The maximizer \(J\) is almost surely unique. Conditional on \((\tau_n=t,J=j)\), the stream for type \(j\) contributes exactly one coupon, and the counts for the other \(n-1\) types are independent \(\operatorname{Pois}(t)\) variables conditioned to be positive. For each fixed integer \(r\ge1\), the conditional probability of count \(r\) is therefore
\[
q_r(t)=\frac{e^{-t}t^r}{r!(1-e^{-t})}.
\]
For every fixed \(R\), the vector \((K_{n,1}-1,K_{n,2},\ldots,K_{n,R})\) conditional on \(\tau_n=t\) is multinomial with \(n-1\) trials and cell probabilities \(q_1(t),\ldots,q_R(t)\) (plus the residual cell). Its exact conditional means are
\[
\mu_{n,r}(t)=\boldsymbol 1_{\{r=1\}}+(n-1)q_r(t).
\]
This conditional multinomial formula is valid for all \(n\ge2\) and all \(t>0\).

**2. Joint conditional central limit theorem.** Set \(L=\log n\). On any event \(\varepsilon\le nU_n\le A\), with fixed \(0<\varepsilon<A<\infty\), one has \(\tau_n=L+O(1)\), uniformly in the event. Hence for every fixed \(r\),
\[
\frac{(n-1)q_r(\tau_n)}{L^r}=\frac{nU_n}{r!}+o(1),\qquad
\frac{(n-1)q_r(\tau_n)q_s(\tau_n)}{L^{(r+s)/2}}=o(1)\quad(r\ne s).
\]
The same conclusion follows for the diagonal variance, since \(q_r(\tau_n)=o(1)\). Consider independent categorical indicator vectors forming this conditional multinomial sample. Their centered, coordinate-scaled summands have largest norm \(O(L^{-1/2})\); their covariance sum tends uniformly on the displayed event to the diagonal matrix with entries \((nU_n)/r!\). Lindeberg's condition holds, so the multivariate triangular-array central limit theorem, equivalently a direct conditional characteristic-function expansion, yields
\[
\mathbb E\left[\left.\exp\left(i\sum_{r=1}^{R}\theta_r\frac{K_{n,r}-\mu_{n,r}(\tau_n)}{L^{r/2}}\right)\,\right|\tau_n\right]
=\exp\left(-\frac{nU_n}{2}\sum_{r=1}^{R}\frac{\theta_r^2}{r!}\right)+o(1).
\]
The error is uniform on the same event. The events \(\{\varepsilon\le nU_n\le A\}\) exhaust probability as \(\varepsilon\downarrow0\), \(A\uparrow\infty\) after \(n\to\infty\). The bounded-characteristic-function argument therefore gives joint convergence with \(\tau_n-\log n\) to the stated conditionally Gaussian mixture.

Moreover, because \(n e^{-\tau_n}=O_{\mathbb P}(1)\), for fixed \(r\)
\[
\mu_{n,r}(\tau_n)-\frac{n e^{-\tau_n}\tau_n^r}{r!}=O_{\mathbb P}(1),
\]
so replacing exact conditional means by the displayed random Poisson centers does not change the limit on any \(L^{r/2}\) scale.

**3. Removing the random Poisson clock.** Let \(C_1,C_2,\ldots\) be independent unit exponentials giving the successive waiting times in the rate-\(n\) superposed process after multiplication by \(n\). These waits are independent of the sequence of coupon marks. Thus
\[
\tau_n=\frac1n\sum_{j=1}^{W_n}C_j,
\qquad
\mathbb E\left(\tau_n-\frac{W_n}{n}\right)^2
=\frac{\mathbb EW_n}{n^2}=\frac{H_n}{n}=O\left(\frac{\log n}{n}\right),
\]
where \(H_n=\sum_{j=1}^n 1/j\). In particular \(\tau_n-W_n/n=O_{\mathbb P}(\sqrt{L/n})\), and the centered completion times differ by \(o_{\mathbb P}(1)\).

For each fixed \(r\), the derivative of \(f_{n,r}(t)=n e^{-t}t^r/r!\), when \(t=L+O_{\mathbb P}(1)\), is \(O_{\mathbb P}(L^r)\). The mean-value theorem and the clock estimate give
\[
\frac{f_{n,r}(\tau_n)-f_{n,r}(W_n/n)}{L^{r/2}}
=O_{\mathbb P}\left(\frac{L^{(r+1)/2}}{\sqrt n}\right)=o_{\mathbb P}(1).
\]
All coupon multiplicities remain unchanged by the Poisson clock. Slutsky's theorem therefore transfers the joint limit to the discrete collection process with precisely the centering \(M_{n,r}=f_{n,r}(W_n/n)\).

**4. Unconditional characteristic function.** Conditionally on \(E\), the coordinates of the limiting residual vector are independent centered Gaussians, with variances \(E/r!\). Since \(E\) is unit exponential,
\[
\mathbb E\exp\left(-\frac E2\sum_{r=1}^{R}\frac{\theta_r^2}{r!}\right)
=\int_0^\infty\exp\left[-u\left(1+\frac12\sum_{r=1}^{R}\frac{\theta_r^2}{r!}\right)\right]du
=\left(1+\frac12\sum_{r=1}^{R}\frac{\theta_r^2}{r!}\right)^{-1}.
\]
This proves both assertions.

## Verification

The standalone `verify_coupon.py` checks the exact singleton expectation against harmonic numbers using rational arithmetic for \(2\le n\le15\), the three-type all-singletons probability, and independent discrete and conditional-multinomial simulations. Run with `python3 verify_coupon.py`; only the Python standard library is required. All numerical tests are finite sanity checks, not substitutes for the general proof. The exact conditional multinomial identity and limiting characteristic-function calculation above are analytic.

## Relationship to prior work

Foata, Han and Lass (2001), Proposition 4.1, computed the exact **finite** multivariate generating function of completion time and joint coupon-multiplicity counts; deriving a Gaussian-mixture fluctuation limit from that exact distribution still requires a separate asymptotic argument. Myers and Wilf (2003), Section 4, derived the exact singleton distribution and expectation at coupon completion. Mahmoud and Smythe (2012), Theorems 1–2, obtained joint central limits for coupon frequencies in sublinear and linear **deterministic** sampling phases; they explicitly leave out the superlinear phase containing completion at order \(n\log n\). Saunders (2020 preprint; 2023 journal), Theorem 1.1, proves a joint **first-order** limiting law for frequency counts and collection time, not the random-centered second-order Gaussian mixture. Ilienko (2020 preprint; later journal version), Theorem 1, gives a first-order joint exponential limit for related completion-time frequency counts. The present theorem isolates the previously unresolved second-order fluctuation scale under observable stopping-time centering and identifies its multivariate Laplace dependence. These comparisons do not rule out every equivalent formulation in the wider literature.

## Limitations

The theorem assumes equal coupon probabilities and one required copy per type. The dimension \(R\) is fixed. The result is weak convergence only; it does not establish convergence rates, moderate deviations, convergence of arbitrary moments, or functional limits. A first-order exponential mixture was already known; the new assertion is the random-centered multivariate second-order law. Prior literature may contain an equivalent formulation not found in the comparison.

## References

- D. Foata, G.-N. Han and B. Lass, *Les nombres hyperharmoniques et la fratrie du collectionneur de vignettes*, Séminaire Lotharingien de Combinatoire 47 (2001), B47a, Proposition 4.1. https://irma.math.unistra.fr/~guoniu/papers/p32frere.pdf
- A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229v1 (posted 2003-04-16), Section 4. https://arxiv.org/pdf/math/0304229
- H. M. Mahmoud and R. T. Smythe, *On the Joint Behavior of Types of Coupons in Generalized Coupon Collection*, Advances in Applied Probability 44 (2012), 429–451, DOI:10.1239/aap/1339878719.
- J. C. Saunders, *The number of k-tons in the coupon collector problem*, arXiv:2005.08915 (first posted 2020-05-18), journal version Journal of Applied Probability 60 (2023), 723–736, DOI:10.1017/jpr.2022.94.
- A. Ilienko, *Limit theorems in the extended coupon collector's problem*, arXiv:2002.00650 (2020); Theorem 1. https://arxiv.org/pdf/2002.00650
