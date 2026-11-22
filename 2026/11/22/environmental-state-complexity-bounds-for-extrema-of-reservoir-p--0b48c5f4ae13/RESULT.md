# Environmental-state complexity bounds for extrema of reservoir pollutant concentration

## Finding
Consider a well-mixed fixed-volume water reservoir in a stationary environment with \(n\ge2\) discharge regimes. Let the regime be an irreducible, reversible, continuous-time Markov chain whose generator is \(\kappa G\), with fixed conservative generator \(G\) and a variable common switching multiplier \(\kappa>0\). In state \(i\), the volumetric flushing rate \(q_i>0\) and external pollutant loading rate \(u_i>0\) give
\[
\dot C(t)=u_{X_t}-q_{X_t}C(t).
\]
Let \(M(\kappa)\) be the stationary, time-averaged concentration (an expectation, not a sample-path maximum). **Unless \(M\) is constant, it has at most \(n-2\) distinct critical points on \((0,\infty)\)** and hence at most \(n-2\) strict local extrema. The bound is zero for two discharge regimes and one for three regimes.

The three-regime transition is real even if both flushing and loading increase strictly with the discharge regime: take the symmetric nearest-neighbour generator
\[
G=\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{pmatrix},\quad(q_1,q_2,q_3)=(1,10,100),\quad(u_1,u_2,u_3)=(1,40,50).
\]
Then
\[
M(\kappa)=\frac{273\kappa^2+9040\kappa+5500}{3(\kappa+10)(111\kappa+100)}.
\]
There is exactly one strict interior maximum, at the positive root of \(7479\kappa^2+7500\kappa-26500=0\), namely \(\kappa_*\approx1.446584864600\). Its value is \(M(\kappa_*)\approx2.139979258105\); the slow- and fast-switching limits are respectively \(11/6\) and \(91/111\). Thus the intermediate rate raises mean concentration approximately \(16.7261\%\) above even the worse endpoint regime, and illustrates that faster environmental switching is not a monotone improvement in mean reservoir water quality.

## Assumptions and scope
The reservoir volume is constant, inlet and outlet water volumes balance instantaneously, and all physical rates are fixed except the common environmental switching multiplier. Regimes have independent of \(C\) transitions. \(G\) is an irreducible row-generator (nonnegative off-diagonal entries and zero row sums) that obeys detailed balance \(\pi_iG_{ij}=\pi_jG_{ji}\) for a strictly positive stationary probability vector \(\pi\). There is no additional sediment exchange, pollutant reaction, or demographic feedback. \(q_i>0\) ensures exponential forgetting of initial pollutant concentration; the input \(u_i>0\) is measured in concentration per unit time. The result is about stationary expectations and not about stationary distributions, variances, transient maxima, or nonreversible environmental cycles.

## Proof
**Existence and moment balance.** The stationary solution is the convergent bounded random integral
\[
C(t)=\int_{-\infty}^{t}u_{X_s}\exp\left(-\int_s^t q_{X_r}\,dr\right)ds.
\]
Indeed \(0<C(t)\le\max_i u_i/\min_i q_i\). Since the regime chain is irreducible and exponentially mixing and the scalar dynamics contract, this stationary law is unique. Let \(D=\operatorname{diag}(q_i)\), \(\Pi=\operatorname{diag}(\pi_i)\), and \(m_i=\mathbb E[C\,\mathbf1_{\{X=i\}}]\). Applying the product generator to the indicator-weighted concentration and setting its expected derivative to zero gives
\[
(D-\kappa G^T)m=\Pi u,\qquad M(\kappa)=\mathbf1^Tm.
\]
The matrix is nonsingular for every nonnegative \(\kappa\), since it is a strictly diagonally stable \(M\)-matrix with positive diagonal killing rates.

**Reversible spectral reduction.** Detailed balance implies \(B=\Pi^{-1/2}G^T\Pi^{1/2}\) is symmetric, with one zero eigenvalue and all other eigenvalues strictly negative. Put \(L=-B\), \(H=D^{-1/2}LD^{-1/2}\), \(a=D^{-1/2}\Pi^{1/2}\mathbf1\), and \(b=D^{-1/2}\Pi^{1/2}u\). Then \(H\) is symmetric positive semidefinite with rank \(n-1\), and
\[
M(\kappa)=a^T(I+\kappa H)^{-1}b.
\]
Orthogonal diagonalization of \(H\) gives, after grouping equal eigenvalues, 
\[
M(\kappa)=c_0+\sum_{j=1}^{m}\frac{c_j}{1+\kappa\lambda_j},\qquad 1\le m\le n-1,
\]
with distinct \(\lambda_j>0\) and real, possibly signed \(c_j\). Some coefficients can vanish. The \(\kappa\) derivative is a real linear combination of functions \((\kappa+a_j)^{-2}\) with distinct \(a_j>0\).

**Zero bound (proved rather than assumed).** For any \(p>0\), any \(r\ge1\), distinct positive numbers \(a_1,\ldots,a_r\), and coefficients not all zero, a sum \(F(x)=\sum_{i=1}^r d_i(x+a_i)^{-p}\) has at most \(r-1\) distinct zeros on \(x>0\). Induct on \(r\) after dropping zero coefficients and ordering the \(a_i\). For \(r=1\), \(F\) never vanishes. If \(F\) had \(r\) distinct zeros, so would \(F(x)/(x+a_1)^{-p}\). By Rolle, its derivative would have at least \(r-1\) distinct zeros. But division by the everywhere-positive factor \(p(x+a_1)^{p-1}\) turns that derivative into
\[
\sum_{i=2}^r d_i(a_i-a_1)(x+a_i)^{-(p+1)},
\]
which has at most \(r-2\) zeros by induction. This is a contradiction. Moreover, the derivative cannot be identically zero unless all coefficients vanish, by the same induction. Applying this at \(p=2\), \(r\le n-1\) to \(M'\) proves the critical-point bound. For \(n=2\), the mean is either constant or strictly monotone; for \(n=3\), it has at most one critical point.

**Sharp three-state onset.** For the stated symmetric three-state path, \(\pi=(1/3,1/3,1/3)\). Exact inversion of the moment balance gives the displayed rational mean and
\[
M'(\kappa)=-\frac{30(7479\kappa^2+7500\kappa-26500)}{(\kappa+10)^2(111\kappa+100)^2}.
\]
The quadratic numerator has one negative and one positive real root, and changes sign from negative to positive at its unique positive root. Thus \(M'\) is strictly positive below \(\kappa_*\) and negative above, so \(\kappa_*\) is the unique global interior maximum. Exact limits follow by taking the constant and leading coefficients. This realizes the general \(n-2\) bound at the first possible value \(n=3\); no assertion of sharpness for every \(n>3\) is needed.

## Verification
Run `python3 checker.py` from a directory containing the embedded checker. It requires only the Python standard library. The checker constructs the exact polynomial matrix and its Cramer determinants over rational numbers, verifies all numerator and denominator coefficients and the differentiated identity, replays 38 exact stationary balance systems, and checks the endpoint values and positive root interval. The printed decimal is a numerical evaluation of a root already characterized and proved unique analytically. These computations verify the concrete example and do not substitute for the universal reversible spectral and Rolle argument above.

## Relationship to prior work
Maran (2002) analyzed random lake/reservoir flushing and autocorrelation-based residence-time corrections, motivating the regime-dependent transport model. Sinzger-D'Angelo, Startceva, and Koeppl (2023) gave a **more general exact stationary mean resolvent** for linear reaction processes in a Markov environment, explicitly noting older queuing-theoretic formulas of O'Cinneide and Purdue (1986). Accordingly, the moment balance and resolvent themselves are not asserted novel. The contribution assessed here is the specific reversible **environmental-state count bound on extrema** of the stationary mean as a function of the single shared rate multiplier, together with the strict-monotone-loading three-state hydrological onset. The general resolvent does not state this zero-count result, which requires diagonal symmetrization and a reciprocal-kernel zero theorem. Meybeck and Moatar (2011) document variable empirical concentration–discharge relationships but do not study this Markov-switching objective. Published record searches and a separate mathematical-research record search did not locate an equivalent extremum-count statement; absence from searches does not certify priority.

## Limitations
Reversibility and the single common switching multiplier are essential for this proof; nonreversible generators can have complex spectral poles and are not addressed. The number of critical points is bounded, not the number of disconnected parameter regimes with noisy local estimates. No upper bound on the size of concentration amplification is claimed. The large differences among the illustrative flushing regimes are stylized; the example is not calibrated to any water body. The associated signed-resolvent zero bound uses classical spectral and Rolle tools, and historical mathematical priority remains uncertain. The motivating river rating-curve paper was accessible only as an abstract/metadata rather than a complete full text; a related 1986 queue paper was not read in full. The result does not infer pollutant exposure, regulatory compliance, or ecological harm without a separate calibration.

## References
1. S. Maran, *A stochastic approach to the evaluation of residence times*, Water Resources Research 38 (2002), doi:10.1029/2001WR000975, first published 2002-05-04. https://doi.org/10.1029/2001WR000975
2. M. Sinzger-D'Angelo, S. Startceva, H. Koeppl, *Bye bye, linearity, bye: quantification of the mean for linear CRNs in a random environment*, Journal of Mathematical Biology 87 (2023), article 43, doi:10.1007/s00285-023-01973-x. https://doi.org/10.1007/s00285-023-01973-x
3. M. Meybeck and F. Moatar, *Daily variability of river concentrations and fluxes: indicators based on the segmentation of the rating curve*, Hydrological Processes 26 (2012), 1188–1207, first published online 2011-06-29. https://doi.org/10.1002/hyp.8211
4. C. O'Cinneide and P. Purdue, 1986, earlier Markov-modulated \(M/M/\infty\) queue stationary-mean theorem, cited and compared in reference 2, Sect. 3.2. Full primary text not verified here; no stronger priority claim is made.
