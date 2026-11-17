# Exact Gaussian antithetic nested-MLMC moments and the decision-tie debiasing frontier

## Finding

For a Gaussian conditional-mean margin containing a possible atom at the exercise boundary, the standard antithetic positive-part multilevel correction has an exact second moment at every sample size. Let \(0\le p\le1\), \(\tau>0\), \(\sigma>0\), and let \(Y\) have distribution \(p\delta_0+(1-p)N(0,\tau^2)\). Conditionally on \(Y\), independent inner observations have the form \(X=Y+\sigma\xi\), with \(\xi\sim N(0,1)\). With independent inner means \(\bar X_n^{(0)}\) and \(\bar X_n^{(1)}\), each using \(n\ge1\) observations at the *same* outer draw \(Y\), define \(\phi(x)=\max\{x,0\}\) and

\[
\Delta_n=\phi\left(\frac{\bar X_n^{(0)}+\bar X_n^{(1)}}2\right)-\frac{\phi(\bar X_n^{(0)})+\phi(\bar X_n^{(1)})}{2}.
\]

For \(k\ge0\), set

\[
F(k)=(k+1)\arctan\left(\frac1{\sqrt{2k+1}}\right)-\frac12\sqrt{2k+1}.
\]

The exact, finite-\(n\) identity is

\[
\boxed{\mathbb E[\Delta_n^2]=\frac{\sigma^2}{2\pi n}\left[pF(0)+(1-p)F\left(\frac{n\tau^2}{\sigma^2}\right)\right],\qquad F(0)=\frac\pi4-\frac12.}
\]

Consequently, for every \(p>0\),

\[
\mathbb E[\Delta_n^2]\sim\frac{p\sigma^2(\pi-2)}{8\pi}\,n^{-1},
\]

whereas at \(p=0\),

\[
\mathbb E[\Delta_n^2]\sim\frac{\sigma^3}{6\pi\sqrt2\,\tau}\,n^{-3/2}.
\]

Thus a positive decision-tie mass changes the exact decay exponent from \(3/2\) to \(1\), however small that mass is.

For the *specified* single-term random-level debiaser, take \(n_\ell=2^{\ell-1}\), \(\ell\ge1\), draw the corresponding \(\Delta_{n_\ell}\) using \(2^\ell\) primitive inner observations, and select an independent level \(L\) with strictly positive probabilities \(q_\ell\). Let \(B=\phi(X_0)\) be an independent one-observation base estimator and put \(Z=B+\Delta_{n_L}/q_L\). Then \(\mathbb E Z=\mathbb E\phi(Y)\). There exists a level law with both \(\mathbb E Z^2<\infty\) and finite expected primitive-observation cost **if and only if \(p=0\)**. The impossibility for \(p>0\) concerns this single-term construction and this cost model only.

## Assumptions and scope

All normal variables are genuine independent Gaussian random variables except for the common outer variable \(Y\) shared within each antithetic pair. The two batches of size \(n\) are conditionally independent given \(Y\). Costs count primitive conditional samples, so a level-\(\ell\) correction costs exactly \(2^\ell\) such samples, in addition to the base sample. The random level and base draw are independent of the correction sampling. The outer variable has a point mass of weight \(p\) at zero and an unshifted centered Gaussian component of weight \(1-p\), with \(\tau>0\). The proposition is not asserted for non-Gaussian inner noise, arbitrary outer-margin distributions, adaptive or combined-level unbiased methods, nor computer floating-point implementations.

## Proof

**1. Antithetic cancellation.** Conditional on a realized \(Y=y\), write the two inner sample means as \(y+\sigma Z_0/\sqrt n\) and \(y+\sigma Z_1/\sqrt n\), with independent standard normals \(Z_0,Z_1\). Set \(W=(Z_0+Z_1)/2\) and \(V=(Z_0-Z_1)/2\). Then \(W,V\) are independent \(N(0,1/2)\) variables. The elementary identity

\[
\frac{(a+v)_++(a-v)_+}{2}-(a)_+=\frac{(|v|-|a|)_+}{2}
\]

holds for every real \(a,v\), where \(u_+=\max\{u,0\}\). Applying it with \(a=\sqrt n\,y/\sigma+W\) and \(v=V\), after extracting the common scaling, gives

\[
\Delta_n=-\frac{\sigma}{2\sqrt n}\left(|V|-\left|\frac{\sqrt n\,Y}{\sigma}+W\right|\right)_+.
\]

**2. Gaussian wedge integral.** If \(A\sim N(0,a^2)\) and \(V\sim N(0,b^2)\) are independent with \(a,b>0\), writing them as two orthogonal standard Gaussian coordinates and integrating in polar coordinates gives

\[
\mathbb E[(|V|-|A|)_+^2]=\frac4\pi\int_0^{\arctan(b/a)}(b\cos\theta-a\sin\theta)^2\,d\theta
=\frac2\pi\left[(a^2+b^2)\arctan\frac ba-ab\right].
\]

Indeed the radial square has expectation \(2\) and the four equivalent quadrants together have angular density \(2/\pi\), yielding the integral coefficient above. When \(Y\) is on the Gaussian component, \(A=\sqrt n\,Y/\sigma+W\) is independent of \(V\) and has variance \(a^2=\tfrac12+n\tau^2/\sigma^2\), with \(b^2=\tfrac12\). When \(Y=0\), the same statement holds with \(a^2=b^2=\tfrac12\). Substitution, multiplication by \(\sigma^2/(4n)\), and mixture linearity give the displayed exact identity.

**3. Large-sample asymptotics.** Put \(t=\sqrt{2k+1}\). Using the Taylor expansion \(\arctan(1/t)=t^{-1}-t^{-3}/3+O(t^{-5})\) yields

\[
F(k)=\frac12[(t^2+1)\arctan(t^{-1})-t]=\frac{1}{3t}+O(t^{-3})
\quad(k\to\infty).
\]

The atomic term is exactly \(\sigma^2p(\pi-2)/(8\pi n)\). If \(p=0\), substituting \(t\sim\sqrt{2n}\,\tau/\sigma\) yields the stated \(n^{-3/2}\) coefficient. If \(p>0\), the non-atomic term has smaller order and the atomic coefficient dominates.

**4. The single-term frontier.** Let \(P_n=\phi(n^{-1}\sum_{j=1}^n X_j)\) with all observations from a shared outer draw. By the definition of antithetic coupling,

\[
\mathbb E\Delta_{n_\ell}=\mathbb EP_{2^\ell}-\mathbb EP_{2^{\ell-1}}.
\]

Since \(\phi\) is one-Lipschitz, \(\mathbb E|P_n-\phi(Y)|\le\sigma/\sqrt n\), so \(\mathbb EP_{2^\ell}\to\mathbb E\phi(Y)\). Convexity makes every correction nonpositive, and therefore \(\sum_{\ell\ge1}\mathbb E|\Delta_{n_\ell}|=\mathbb EP_1-\mathbb E\phi(Y)<\infty\). This proves absolute integrability and unbiasedness of \(Z\) for every positive level law \((q_\ell)\).

Because the base is independent and square-integrable, \(Z\) has a finite second moment exactly when \(\sum_{\ell\ge1}\mathbb E[\Delta_{n_\ell}^2]/q_\ell<\infty\). Finite expected sample cost requires \(\sum_{\ell\ge1}q_\ell2^\ell<\infty\). By Cauchy--Schwarz, satisfying both implies

\[
\sum_{\ell\ge1}\sqrt{2^\ell\mathbb E[\Delta_{n_\ell}^2]}<\infty.
\]

For \(p>0\), every summand tends to the strictly positive limit \(\sqrt{p\sigma^2(\pi-2)/(4\pi)}\), an impossibility. For \(p=0\), the second moments are \(\Theta(2^{-3\ell/2})\). Choosing \(q_\ell\) proportional to \(2^{-r\ell}\) for any \(1<r<3/2\) makes both sums finite, proving sufficiency. All equalities and endpoint cases \(p=0\) and \(p=1\) are covered.

## Verification

Run `python check.py` using only the Python standard library. The supplied script independently evaluates the Gaussian wedge integral by composite Simpson quadrature over the angular wedge and compares it to the closed form for several batch sizes and variance scales; it also checks the atomic coefficient, the smooth asymptotic constant, and seeded direct-sample Monte Carlo diagnostics. The 86 numerical checks passed. The proof above, not these finite checks, establishes identities for every permitted parameter and every integer sample size.

## Relationship to prior work

Haji-Ali and Spence (2023) study nested antithetic multilevel estimation for a maximum of a conditional mean and a benchmark, and provide general convergence/cost bounds under regularity assumptions. Giles and Goda (2017) establish multilevel performance for decision problems under transversality-type conditions and discuss positive-measure decision ties as outside those assumptions. The result here does not claim novelty of antithetic coupling, the positive-part reduction, general strong-rate bounds, or the Cauchy--Schwarz random-level cost criterion. Its narrower contribution is the exact Gaussian mixture second-moment function, the two sharp asymptotic constants, and the consequent if-and-only-if sampling-cost/moment frontier for the specified canonical single-term debiaser. The established smooth-case rate is compatible with the general literature; a positive atom violates the usual small-margin anti-concentration condition.

## Limitations

The Gaussian mixture and inner normal-noise assumptions are essential to the displayed closed form, though the cost obstruction itself is expressed using the resulting rates. No universal impossibility result is claimed for all unbiased nested estimators; analytic integration, adaptive allocation, modified couplings, and alternative estimators are outside scope. The criterion uses expected primitive conditional-observation cost, not wall-clock complexity. Relevant general literature was examined, but specialist publication precedence for the exact coefficient remains a residual risk; a plausibly related initial-margin multilevel paper was identifiable but its full text was not available for this comparison. No independent scientific audit was performed.

## References

- A.-L. Haji-Ali and J. Spence, *Nested Multilevel Monte Carlo with Biased and Antithetic Sampling* (2023), arXiv:2308.07835, first posted 15 August 2023, https://arxiv.org/abs/2308.07835.
- M. B. Giles and T. Goda, *Decision-making under uncertainty: using MLMC for efficient estimation of EVPPI* (2017), arXiv:1708.05531, https://arxiv.org/abs/1708.05531.
- M. B. Giles and A.-L. Haji-Ali, *Multilevel nested simulation for efficient risk estimation* (2018), arXiv:1802.05016, https://arxiv.org/abs/1802.05016.
- F. Bourgey, S. De Marco, E. Gobet, and J. Zhou, *Multilevel Monte Carlo Methods and Lower–Upper Bounds in Initial Margin Computations* (2020), DOI:10.1515/mcma-2020-2062. Full text not inspected; retained as a publication-precedence risk.
