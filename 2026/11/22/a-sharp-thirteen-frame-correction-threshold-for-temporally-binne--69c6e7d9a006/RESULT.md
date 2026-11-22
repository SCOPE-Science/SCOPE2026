# A sharp thirteen-frame correction threshold for temporally binned differential photometry

## Finding

An exact all-window decision boundary is obtained for a simple differential-photometry workflow: compare the uncorrected target measurement to the target measurement minus a centered odd-length **unit-weight** boxcar average of a reference star. When the common atmospheric signal has one-frame correlation \(\rho=1/2\), a finite reference correction helps for some odd window if and only if the comparison-to-atmospheric noise-variance ratio satisfies
\[
\eta=\frac{\sigma_C^2}{\sigma_A^2}<\eta_*=\frac{86399}{26624}=3.245154747596\ldots.
\]
At equality, the 13-frame reference correction ties omission of the reference, and every other finite odd window is strictly worse. Above equality, omission is strictly better than every finite unit-weight boxcar correction. This 13-frame threshold is global over **all** odd window lengths; it is not an assertion that 13 frames minimize variance at arbitrary subcritical noise ratios.

A further non-unimodal-design consequence occurs at \(\eta=13/4\): the 13-frame correction is a strict **local** variance minimum among neighboring odd lengths but has larger variance than doing no correction at all.

## Assumptions and scope

Take a bi-infinite, zero-mean, second-order stationary real sequence \((A_j)_{j\in\mathbb Z}\) with \(\sigma_A^2>0\) and \(\operatorname{Cov}(A_j,A_k)=\sigma_A^2 2^{-|j-k|}\). No Gaussian assumption is required. Independently, let centered comparison errors \((\epsilon_j)\) have variance \(\sigma_C^2\ge0\) and be mutually uncorrelated and uncorrelated with the entire atmospheric sequence. A constant reference-star flux has already been subtracted. Target measurement at the central frame is \(T_0=\mu+A_0+\xi_0\), with independent target measurement error \(\xi_0\) of arbitrary fixed variance. The reference is \(C_j=A_j+\epsilon_j\). At integer half-window width \(m\ge0\), the corrected target is
\[
\widehat\mu_m=T_0-\frac{1}{2m+1}\sum_{j=-m}^{m}C_j.
\]
The alternative is no reference correction, \(\widehat\mu_\varnothing=T_0\). These are the **only** admissible rules: the comparison coefficient is exactly one, weights within a reference window are equal, the target is not temporally averaged, and the window is centered. Target-noise variance adds equally to all choices and does not affect comparisons. The risk is the variance of the estimation error, conditional on the deterministic target level \(\mu\), normalized by \(\sigma_A^2\) after removing the common target-noise variance. All decisions and equalities apply to every real \(\eta\ge0\), every integer \(m\ge0\), and the unlimited bi-infinite data idealization; physical boundary-frame effects and photometric bias are excluded.

## Proof

Put \(N=2m+1\), \(\eta=\sigma_C^2/\sigma_A^2\) and \(\rho=1/2\). Define
\[
C_m=1+2\sum_{j=1}^{m}\rho^j,\qquad S_N=N+2\sum_{k=1}^{N-1}(N-k)\rho^k.
\]
By the covariance assumptions, the no-correction normalized risk is exactly \(R_\varnothing=1\), and the corrected risk is
\[
R_m=1-\frac{2C_m}{N}+\frac{S_N+\eta N}{N^2}
=1+\frac{\eta-B_m}{N},\quad B_m=2C_m-\frac{S_N}{N}.
\]
The finite geometric sums at \(\rho=1/2\) yield \(C_m=3-2^{1-m}\), \(S_N=3N-4+2^{2-N}\), and hence
\[
B_m=3+\frac4{2m+1}-\frac4{2^m}-\frac{2}{(2m+1)4^m}.
\]
Therefore finite correction \(m\) beats no correction precisely when \(\eta<B_m\). The nontrivial step is to maximize \(B_m\) over the **entire unbounded integer family**, not over any finite numerical search range.

For \(y=2^{-m}\), \(N=2m+1\), direct subtraction and common-denominator algebra give
\[
 B_{m+1}-B_m=\frac{-8+2yN(N+2)+\tfrac12y^2(3N+8)}{N(N+2)}.
\]
Exact rational substitution establishes \(B_{m+1}-B_m>0\) for each \(m=0,1,2,3,4,5\), and establishes \(B_7-B_6<0\). To control **every** \(m\ge6\), observe that the positive numerator terms \(2yN(N+2)\) and \(\tfrac12y^2(3N+8)\) each strictly decrease when \(m\) is increased by one for \(N\ge13\): their successive ratios are respectively \((N+4)/(2N)<1\) and \((3N+14)/(4(3N+8))<1\). Thus the numerator stays strictly negative for every \(m\ge6\). Consequently \(B_0<B_1<\cdots<B_6>B_7>B_8>\cdots\), with
\[
B_6=\frac{86399}{26624},\qquad N=13.
\]
This proves the claimed exhaustive phase boundary, strictness and unique equality case. For the stated local-but-not-global example \(\eta=13/4> B_6\), direct rational comparison in the same exact risk expression gives \(R_5>R_6<R_7\), while \(R_m>1=R_\varnothing\) for every \(m\), as required. No finite enumeration is being substituted for the infinite monotonicity argument.

## Verification

The accompanying standalone \(verify.py\) checks the covariance sum identity against direct rational finite sums, checks the finite sign boundary at half-window indices \(m=0,\ldots,6\), verifies the rational threshold and local-trap inequalities, and tests a selection of later windows. Execute \(python3 verify.py\) with only the Python standard library. The infinite-range result depends on the explicitly proved monotone-numerator ratios, not on test coverage.

## Relationship to prior work

Hartley and Wilson (2023), Sections 2.5, 3.2 and 5, introduce and test temporal binning of comparison-star light curves, explicitly discuss the noise-versus-trend trade-off and an empirical threshold relative to uncorrected measurements, and optimize window length from observed or simulated noise; that motivation and method are **prior work**, not discoveries here. The present restricted second-order AR covariance model gives an analytic, rational, global **all-odd-window threshold** and a local-minimum trap, neither of which is stated or implied by the inspected paper's empirical pipeline. General AR(1) covariance modeling is classical (Bergmans et al., 2005, cited below) and is not new. The distinct published-finding corpus comparison entries concern AR noise correlations, nonlinear noise smoothing and astronomical observation scheduling, rather than this exact full-weight boxcar/no-correction risk phase boundary. These limited searches do not establish historical uniqueness; full bibliographic priority may require further expert checking.

## Limitations

The conclusion concerns a canonical, idealized \(\rho=1/2\) stationary atmospheric covariance and an infinite central time index. It is not a universal threshold for all correlation rates, nonstationary atmospheric transparency, scintillation, spatial mismatch, variable stellar brightness, time-dependent detector errors, boundary frames, causal windows, fractional subtraction gains, adaptive Wiener filters, or other objectives. In particular, allowing a freely tuned fractional reference coefficient changes the optimization and can eliminate the no-correction regime. The model is mathematical and has not been empirically calibrated; the exact thirteen-frame figure is not asserted as a telescope-independent recommendation. Historical literature coverage is incomplete; independent external validation has not been performed.

## References

1. K. E. Hartley and R. W. Wilson (2023), *Optimized temporal binning of comparison star measurements for differential photometry*, Monthly Notices of the Royal Astronomical Society 526(3), 3482–3494, first online 2023-09-28, https://doi.org/10.1093/mnras/stad2964 . Inspected full-text sections 2.5, 3.2, and 5 through an accessible author-posted text representation, and the Durham repository publication-date record.
2. M. Bergmans and coauthors (2005), *Modeling irregularly spaced residual series as a continuous stochastic process*, Water Resources Research, https://doi.org/10.1029/2004WR003726 . Used solely for the established AR(1)/OU background, not for novel threshold claims.
3. Related research-record comparison: https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-two-boundary-layers-for-zero-crossing-and-centered-energy-covari--e0f4a1d0a49b ; distinct AR(1) zero-crossing/energy covariance quantities.
