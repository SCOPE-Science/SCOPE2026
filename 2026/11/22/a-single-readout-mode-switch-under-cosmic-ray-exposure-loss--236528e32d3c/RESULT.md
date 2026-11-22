# A single readout-mode switch under cosmic-ray exposure loss

## Finding

Consider two astronomical detector readout modes whose only differences are positive read-noise variances and positive readout dead times. For homogeneous, independent cosmic-ray hits that invalidate an entire affected exposure, optimize the expected information on a constant source amplitude **per unit of wall-clock observing time**, allowing each mode to choose its own exposure duration.

Put \(a_i=\sigma_i^2/b>0\), \(h_i>0\), \(s_i=a_i+h_i\), and \(p_i=a_i h_i\) for modes \(i=1,2\), where \(b>0\) is the common background variance rate. Let \(\lambda>0\) be the cosmic-ray rate for the source aperture, identical in both modes. Then:

1. Each mode has exactly one optimal exposure duration \(t_i(\lambda)>0\). It is the unique solution of
   \[
   \lambda=\frac{a_i}{t(t+a_i)}+\frac{h_i}{t(t+h_i)}.
   \]
2. If \(s_1\le s_2\) and \(p_1\le p_2\), with at least one strict inequality, mode 1 is uniquely better at every \(\lambda>0\). Reverse the inequalities to reverse the winner. If both pairs agree exactly, the two modes have identical achievable information rates at every \(\lambda\), even when their read-noise and overhead parameters are interchanged.
3. If \(s_1<s_2\) but \(p_1>p_2\), there is **exactly one** \(\lambda_*>0\) at which the two optimized information rates tie. Mode 1 is better for \(0<\lambda<\lambda_*\), whereas mode 2 is better for \(\lambda>\lambda_*\). At the tie, both optimizers are global and have different durations, with \(t_1(\lambda_*)>t_2(\lambda_*)\). Thus the globally preferred duration jumps **downward** at the unique mode change. Interchanging the mode labels covers the other crossed-ranking case.
4. For each mode separately, the optimal exposure is longer than the mean cosmic-ray waiting time precisely when \(\lambda^2 a_i h_i>1\), and it is always strictly shorter than twice that waiting time:
   \[
   t_i(\lambda)>1/\lambda\iff\lambda^2a_i h_i>1,
   \qquad 0<\lambda t_i(\lambda)<2.
   \]

The crossing threshold is an exact one-dimensional implicitly defined number, not a universal decimal constant. A reproducible instance is \((a_1,h_1)=(4,4)\) and \((a_2,h_2)=(1/10,20)\), for which
\[
\lambda_*=1.098884851672\ldots,\quad
 t_1(\lambda_*)=1.358587148822\ldots,\quad
 t_2(\lambda_*)=0.954820016526\ldots.
\]
Here both positive duration parameters and both read-noise equivalents are measured using the same time unit.

## Assumptions and scope

For mode \(i\), a clean exposure of duration \(t>0\) produces one independent Gaussian statistic \(Y\sim N(\theta t,bt+\sigma_i^2)\), where \(\theta>0\) is an unknown constant source amplitude, \(b>0\) is calibrated and independent of \(\theta\), and \(\sigma_i^2>0\) is the mode's calibrated read-noise variance. Contamination is flagged and the statistic discarded whenever at least one cosmic-ray hit occurs during the integration. Hits follow a Poisson process of rate \(\lambda>0\) independent of the signal and noise, so a clean exposure has probability \(e^{-\lambda t}\); no part of a contaminated exposure is salvaged. A completed observation requires an additional fixed overhead \(h_i>0\), during which no useful signal is integrated. Identical source aperture, background, and hit rate across modes are essential.

The objective is asymptotic expected Fisher information per wall-time for repeated independent cycles of the same design. It is **not** the signal-to-noise ratio of one exposure, a finite-horizon optimal stopping problem, or a claim about detectors with continuously salvageable partial read ramps. The Gaussian model is an exact stipulated approximation to a background-dominated regime, not a claim that Poisson photon counts have Gaussian statistics at every flux.

## Proof

**Step 1: conditional and average information.** In a clean Gaussian observation the variance does not depend on \(\theta\), hence Fisher information is \(t^2/(bt+\sigma_i^2)\). The clean/contaminated indicator has a distribution independent of \(\theta\). Thus the information per cycle, averaged over that indicator, is \(e^{-\lambda t}t^2/(bt+\sigma_i^2)\). Dividing by cycle time \(t+h_i\) and multiplying by the common positive constant \(b\) gives the exact normalized efficiency
\[
 j_i(t,\lambda)=\frac{e^{-\lambda t}t^2}{(t+a_i)(t+h_i)}
 =\frac{e^{-\lambda t}t^2}{t^2+s_it+p_i}.
\]
Write \(F_i(\lambda)=\max_{t>0}j_i(t,\lambda)\). The maximum exists because the efficiency tends to zero at both endpoints for \(\lambda>0\).

**Step 2: unique time optimum and the mean-hit-time criterion.** The logarithmic derivative is
\[
 \frac{\partial}{\partial t}\log j_i(t,\lambda)
 =k_i(t)-\lambda,\qquad
 k_i(t)=\frac{a_i}{t(t+a_i)}+\frac{h_i}{t(t+h_i)}.
\]
Each summand of \(k_i\) decreases strictly from infinity to zero on \((0,\infty)\); therefore its graph intersects \(\lambda\) once, at the unique global maximum. Since each term is smaller than \(1/t\), \(t_i<2/\lambda\). By monotonicity, \(t_i>1/\lambda\) exactly when
\[
 \frac{\lambda a_i}{1+\lambda a_i}
 +\frac{\lambda h_i}{1+\lambda h_i}>1,
\]
which is algebraically equivalent to \(\lambda^2a_ih_i>1\). Equalities give equality of the durations.

**Step 3: pointwise mode dominance.** With \(D_i(t)=t^2+s_it+p_i\), all numerators are identical. If both \(s_1\le s_2\) and \(p_1\le p_2\), with one strict, then \(D_1(t)<D_2(t)\) for all \(t>0\). Inserting mode 2's finite maximizer into mode 1 gives \(F_1(\lambda)>F_2(\lambda)\). Equal sums and products give \(D_1\equiv D_2\), and conversely. Every parameter pair falls under dominance, equivalence, or opposite rankings.

**Step 4: exactly one crossing under opposite rankings.** Assume \(s_1<s_2\) and \(p_1>p_2\). Direct differentiation shows
\[
 k_1(t)-k_2(t)
 =\frac{(s_1-s_2)t^2+2(p_1-p_2)t+s_2p_1-s_1p_2}{D_1(t)D_2(t)}.
\]
The numerator is a downward-opening quadratic with positive constant, so it has one negative root and exactly one positive root \(t_c\). Consequently \(k_1-k_2\) is positive for \(0<t<t_c\), negative for \(t>t_c\), and zero only at \(t_c\). Set \(\lambda_c=k_1(t_c)=k_2(t_c)>0\). Because each \(k_i\) is strictly decreasing, \(t_1(\lambda)<t_2(\lambda)\) for \(0<\lambda<\lambda_c\), they agree at \(\lambda_c\), and \(t_1(\lambda)>t_2(\lambda)\) for \(\lambda>\lambda_c\).

The envelope theorem applies to the smooth unique interior maxima, giving
\[
 \frac{d}{d\lambda}\log\frac{F_1(\lambda)}{F_2(\lambda)}
 =t_2(\lambda)-t_1(\lambda).
\]
Hence the logarithmic optimal-efficiency ratio increases strictly below \(\lambda_c\) and decreases strictly above it. Its endpoint behavior is determined directly by the stationary equations:
\[
 t_i(\lambda)\sim\sqrt{\frac{s_i}{\lambda}},\qquad
 F_i(\lambda)=1-2\sqrt{s_i\lambda}+O(\lambda)
 \quad(\lambda\downarrow0),
\]
\[
 t_i(\lambda)\sim\frac2\lambda,\qquad
 F_i(\lambda)\sim\frac{4e^{-2}}{p_i\lambda^2}
 \quad(\lambda\to\infty).
\]
As \(s_1<s_2\), the first limit makes \(F_1/F_2>1\) near zero, with ratio tending to one. As \(p_1>p_2\), the last limit makes \(F_1/F_2\to p_2/p_1<1\). The strictly single-peaked log ratio therefore crosses zero exactly once, necessarily at \(\lambda_*>\lambda_c\). Both global maximizing times at the tie are unique within their modes; since \(\lambda_*>\lambda_c\), they satisfy \(t_1>t_2\), establishing the discontinuity in the choice of preferred duration. Interchange labels for the reverse crossed case.

**Step 5: adaptive or mixed cycles cannot beat the best rate.** For any finite sequence of exposure choices predictable from preceding results, conditional expected Fisher information in cycle \(j\) is at most \(F_*(\lambda)(t_j+h_{i_j})/b\), where \(F_*\) is the larger of the two normalized optimized efficiencies. The likelihood-score increments are conditionally mean zero, so their cross-information terms vanish. Summing expectations shows that adaptive mode and exposure mixing cannot exceed \(F_*/b\) information per unit expected total cycle time. A constant best mode and its unique optimum attain the bound; at \(\lambda_*\), arbitrary mixtures of the two optimal pairs attain it. This comparison assumes no learning of previously unknown nuisance parameters and a known stationary hazard.

## Verification

The accompanying standalone \(\texttt{check.py}\) recomputes the implicit mode optima by monotone bisection. It checks the derivative conditions, global dominance against four scaled perturbations per sampled optimum, the analytic mean-hit-time threshold, the swap equivalence, numerical mode dominance, the unique positive quadratic crossing, and the illustrative two-mode threshold. The checker uses Python's standard library and a fixed random seed and reports 29,265 finite diagnostic assertions. These finite diagnostics do not establish the theorem for all positive real parameters; the proof above does.

## Relationship to prior work

Fixsen et al. (2000) analyze cosmic-ray rejection and read-noise efficiency, comparing Fowler sampling with nondestructive readouts and demonstrating the value of salvaging partial ramps. Regan and Stockman (2001) present an optimization method for the mean squared signal-to-noise per exposure time, with numerical comparisons of three detector read modes at specified cosmic-ray conditions. The 2011 Space Telescope Imaging Spectrograph handbook explicitly discusses the operational trade-off between long exposures, cosmic-ray damage, and added read noise. Those comparisons motivate the normalized clean-exposure model here. Their physically richer protocols are not represented as instances of this full-exposure-loss, fixed-overhead model.

The result proved here concerns a different comparison axis: the global **number and direction of readout-mode switches as a common cosmic-ray rate varies**, under independently reoptimized exposure duration, together with the exact sum/product parameter test and the discontinuous optimal-duration jump. No inspected source states or implies that all-rate classification for this stipulated two-mode model. In particular, a procedure to optimize each mode at one specified hit rate does not itself prove that the optimized curves cross exactly once as the rate varies. The comparisons do not rule out uncatalogued earlier derivations; priority remains subject to independent historical verification.

## Limitations

The hit process is homogeneous Poisson and modes have a common hit rate. Contaminated exposures are completely discarded; partially usable ramps, pixel-level masking, saturation, source shot noise, background uncertainty, correlated read noise, dithering, changing target flux, maximum exposure length, finite observing windows, and mode-switch setup costs are excluded. The model's Gaussian known-variance information score is a deliberately narrow benchmark and must not be read as empirically optimal HST or JWST operating guidance. No observational validation or independent audit is claimed.

## References

1. Fixsen, D. J. et al., *Cosmic Ray Rejection and Readout Efficiency for Large-Area Arrays*, 2000, arXiv:astro-ph/0005486, first public arXiv posting 2000-05-24; https://arxiv.org/abs/astro-ph/0005486 ; https://ar5iv.labs.arxiv.org/html/astro-ph/0005486 .
2. Regan, M., and Stockman, P., *Optimum Integration Times for Different Read Modes*, Space Telescope Science Institute technical memorandum STSCI-NGST-TM-2001-0005, dated 2001-10-30; https://ridl.cfd.rit.edu/docs/radiation/TM-2001-0005-A_TM-2001-0005A.pdf .
3. Ely, J., et al., *Space Telescope Imaging Spectrograph Instrument Handbook for Cycle 20*, Version 11.0, December 2011, STScI, section on CCD exposure splitting and cosmic-ray trade-offs; https://studylib.net/doc/11603992 .
4. Anderson, R. E., and Gordon, K. D., *Optimal Cosmic-Ray Detection for Nondestructive Read Ramps*, first posted 2011-09-12, arXiv:1109.2626; https://arxiv.org/abs/1109.2626 . This last source concerns hit detection rather than an exact two-mode switch.
