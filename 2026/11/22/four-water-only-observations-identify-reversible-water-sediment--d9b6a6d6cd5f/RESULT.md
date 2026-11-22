# Four water-only observations identify reversible water–sediment loss under a selective decay perturbation

## Finding

Consider an initially normalized aqueous eDNA pulse with reversible exchange to a sorbed or sediment-associated pool, positive decay in both pools, and a known intervention that changes only the aqueous decay rate. All four positive physical rates can be uniquely recovered from just **four scalar water-only observations**: three at equally spaced positive times in one condition and one at the first of those times in a second condition. No choice of fewer than four scalar measurements, at arbitrary fixed positive observation times and known intervention levels, can identify all four parameters globally and continuously across the open positive parameter domain. With only one intervention condition, even the complete noiseless continuous water curve leaves a precisely characterized one-dimensional family of positive parameter choices indistinguishable.

This is an exact *structural identifiability* and *measurement-count* result for the model below, not a statistical precision guarantee or a field-calibrated eDNA prescription. Prony's recovery of a sum of exponentials, and one-condition two-compartment nonidentifiability, are established methods and are not asserted to be new.

## Assumptions and scope

Let the four unknown **strictly positive** time-constant rates be \(a,b,d,e>0\). Here \(a\) transfers water-associated material into the sediment-associated pool, \(b\) returns it to water, \(d\) is the unperturbed aqueous degradation constant, and \(e\) is the sediment-pool degradation constant. A known positive multiplier \(\theta\) alters *only* the aqueous degradation. For each independent, identical, initially normalized pulse experiment,

\[
\begin{aligned}
\dot W_\theta(t)&=-(a+\theta d)W_\theta(t)+bS_\theta(t),\\
\dot S_\theta(t)&=aW_\theta(t)-(b+e)S_\theta(t),\\
W_\theta(0)&=1,\qquad S_\theta(0)=0.
\end{aligned}
\]

Fix \(h>0\) and two *distinct, known* intervention levels \(\theta_1,\theta_2>0\). Only the four water values

\[
\bigl(W_{\theta_1}(h),W_{\theta_1}(2h),W_{\theta_1}(3h),W_{\theta_2}(h)\bigr)
\]

are measured. Initial normalization and time zero are known, and there is no additional unknown observation gain, background, input, transport, or intervention-dependent exchange. Positive physical parameters ensure two distinct real decay modes without exceptional repeated-root cases. The observations are ideal exact values; the inverse is not asserted stable uniformly as rates become close or small.

## Proof

**1. Three invariants encoded by one water trace.** Introduce the observable combinations

\[
A_\theta=a+\theta d,\qquad D=b+e,\qquad B=ab>0.
\]

Since \(A_\theta D>B\), both modal decay rates of the matrix are positive. Direct elimination of the unobserved pool gives

\[
\ddot W_\theta+(A_\theta+D)\dot W_\theta+(A_\theta D-B)W_\theta=0,
\quad W_\theta(0)=1,\quad\dot W_\theta(0)=-A_\theta.
\]

Equivalently its Laplace transform is

\[
\widehat W_\theta(s)=\frac{s+D}{(s+A_\theta)(s+D)-B}.
\]

Define \(\lambda_{-}<\lambda_{+}\) as the positive roots of

\[
\lambda^2-(A_\theta+D)\lambda+(A_\theta D-B)=0.
\]

Because the characteristic polynomial evaluated at \(D\) equals \(-B<0\), one has \(\lambda_-<D<\lambda_+\). Hence

\[
W_\theta(t)=w e^{-\lambda_-t}+(1-w)e^{-\lambda_+t},\qquad
w=\frac{D-\lambda_-}{\lambda_+-\lambda_-}\in(0,1).
\]

All three of \(A_\theta,D,B\) and no additional individual rates are determined by the entire exact curve. Indeed \(-\dot W_\theta(0)=A_\theta\), and the two nonzero distinct poles and residues identify \(D,B\).

**2. Exact finite recovery from three equally spaced water readings.** Put \(y_0=1\) (known from initialization) and \(y_j=W_{\theta_1}(jh)\) for \(j=1,2,3\). Define

\[
V=y_2-y_1^2>0,\qquad
T=\frac{y_3-y_1y_2}{V},\qquad U=Ty_1-y_2.
\]

Here \(V>0\) because it is the weighted variance of two different numbers \(r_s=e^{-\lambda_-h}\) and \(r_f=e^{-\lambda_+h}\), both having strictly positive weights. The standard two-term recurrence \(y_{j+2}=Ty_{j+1}-Uy_j\) gives

\[
r_s=\frac{T+\sqrt{T^2-4U}}2,\qquad
r_f=\frac{T-\sqrt{T^2-4U}}2,\qquad0<r_f<r_s<1.
\]

Consequently the *unique* recovered parameters of the first response are

\[
\begin{aligned}
\lambda_-&=-\log(r_s)/h,&\lambda_+&=-\log(r_f)/h,\\
w&=\frac{y_1-r_f}{r_s-r_f},&A_1&=w\lambda_-+(1-w)\lambda_+,\\
D&=\lambda_-+\lambda_+-A_1,&B&=A_1D-\lambda_-\lambda_+.
\end{aligned}
\]

The notation \(A_1=A_{\theta_1}\) will be used below. These formulas are valid for *every* strictly positive original parameter choice and any fixed \(h>0\).

**3. One selectively perturbed water value identifies the missing invariant.** Keeping the recovered \(D,B\) fixed, regard \(W(A,D,B;t)\) as the water response of the two-mode system with free diagonal-loss combination \(A>B/D\). Differentiate its Laplace transform with respect to \(A\):

\[
\frac{\partial}{\partial A}\widehat W(s)
=-\left[\frac{s+D}{(s+A)(s+D)-B}\right]^2.
\]

The convolution theorem therefore gives for every \(t>0\)

\[
\frac{\partial}{\partial A}W(A,D,B;t)
=-\int_0^t W(A,D,B;u)W(A,D,B;t-u)\,du<0.
\]

Strictness holds because \(A>B/D\), \(B,D>0\) imply a positive convex combination of the two exponential modes. Thus the scalar equation

\[
W(A_2,D,B;h)=W_{\theta_2}(h)
\]

has **at most one** solution \(A_2>B/D\), and the true experiment supplies its existence. Bisection on this strictly monotone continuous function recovers \(A_2=A_{\theta_2}\) exactly in the noiseless mathematical sense. Then

\[
\boxed{\quad d=\frac{A_2-A_1}{\theta_2-\theta_1},\quad
 a=A_1-\theta_1d,\quad b=\frac{B}{a},\quad e=D-b.\quad}
\]

This proves global injectivity of the four-measurement map. Notice that the order of \(\theta_1\) and \(\theta_2\) is unrestricted; the denominator is merely required nonzero.

**4. Sharp one-condition ambiguity.** For a single fixed \(\theta_1\), any value

\[
\frac{B}{D}<z<A_1
\]

produces a distinct strictly positive physical parameter quadruple

\[
a_z=z,\qquad b_z=B/z,\qquad
 d_z=(A_1-z)/\theta_1,\qquad e_z=D-B/z.
\]

Every such quadruple has the same \(A_1,D,B\) and hence the *same complete water trajectory*. Conversely, equality of full trajectories enforces equality of the three invariants derived in step 1, so this open interval is the **entire** positive ambiguity fiber. It is nonempty because the actual \(a\) lies strictly inside it: \(a<A_1\) and \(a>B/D\) are both consequences of positive \(d,e\). The second-condition measurement removes the fiber by strict monotonicity in step 3.

**5. Minimum scalar observation count.** For any *fixed, finite* design of \(k<4\) scalar water measurements at arbitrary positive times and arbitrary known intervention multipliers, the parameter-to-observation map is continuous on the open set \((0,\infty)^4\). It cannot be one-to-one: otherwise padding its \(k\) components with \(4-k\) zeros gives a continuous injection from an open subset of \(\mathbb R^4\) into \(\mathbb R^4\), contradicting invariance of domain, since its image lies in a proper coordinate hyperplane and has empty interior. Therefore at least four scalar readings are necessary, and the construction above attains this lower bound. The argument does not count the *given* normalized initial value as an observation.

## Verification

The included `verify.py` uses high-precision arbitrary-precision arithmetic to reconstruct all four rates from 150 reproducible randomly selected positive parameter sets with \(\theta_1=1\), \(\theta_2=2.5\), and varying \(h>0\). It also tests the explicit one-condition ambiguity fiber and the strict direction of the intervention response; 2,250 numerical assertions passed. The checker does **not** establish the universal theorem; the analytic steps above do.

A concrete example takes \((a,b,d,e)=(1.2,0.8,0.7,0.5)\), \(h=0.7\), and the same multipliers. The exact-model observations, rounded to 19 significant digits, are

\[
\begin{aligned}
W_{\theta_1}(h)&\approx0.3393290420208411784,\\
W_{\theta_1}(2h)&\approx0.1744219882998932181,\\
W_{\theta_1}(3h)&\approx0.1082537898942548732,\\
W_{\theta_2}(h)&\approx0.1743252703975479058.
\end{aligned}
\]

Executing `python verify.py` with `mpmath` installed (requirements documented in `requirements.txt`) reproduces the checks. Use unrounded values for reconstruction; rounding induces nonzero error.

## Relationship to prior work

Pont (2024) models eDNA retention and degradation under river transport and discusses exchange at the water–sediment interface. McKnight, Shafer and Frost (2024) report environmental treatment-dependent eDNA decay in microcosms. Sakata et al. (2020) establish that aqueous and sedimentary eDNA can exhibit very different degradation timescales. These motivate the *chosen physical processes* but do not experimentally validate a strictly selective multiplier of just one degradation constant.

The decomposition of a two-exponential time signal into its roots and weights is an instance of **classical Prony-type inference**, not a new method; see Cuyt and Lee (2018). The basic structural nonidentifiability of a single-output two-compartment model is also established, e.g. by Meshkat, Kuo and DiStefano (2014). The claimed additional result here is the combined, globally valid **three-plus-one selective-perturbation measurement design**, the exact all-positive-parameter ambiguity interval, and the sharp **four total readings** bound. Neither the earlier general method nor generic identifiability statements are claimed as new.

Kelleher et al. (2013) and Dallan et al. (2023) address parameter determination for *spatial* stream-transient-storage transport models, using sensitivity or breakthrough-curve asymptotics; their conclusions do not directly supply this pulse microcosm's two-condition four-point global inverse. Classic work by Godfrey, Jones and Brown (1980) studies additional inputs or measurements in pharmacokinetic compartment models; it remains a relevant historical-priority risk for specialized selective interventions.

## Limitations

The result assumes known and repeated initial pulse amplitude, unmeasured pool initially empty, first-order loss and reversible exchange, identical transfer parameters in both conditions, calibrated intervention selectivity and multiplier, exact clock and measurements, and no spatial transport. It does not imply that a real change in pH, temperature, filtering or microbial composition only modifies aqueous degradation: such treatments may also change sorption, desorption and sediment processing. No robustness to noise, nonlinearity, structural misspecification, observation gain drift, or close modal rates is proved. High sensitivity is possible when modal rates nearly coincide, when the two intervention multipliers nearly coincide, or when sampling is far into signal decay. Historical originality is limited to the inspected comparisons and is not a claim of exhaustive priority verification.

## References

1. Pont, D. (2024), *Predicting downstream transport distance of fish eDNA in lotic environments*, Molecular Ecology Resources. First public date 2024-02-06. https://doi.org/10.1111/1755-0998.13934
2. McKnight, E. G. W., Shafer, A. B. A., and Frost, P. C. (2024), *Quantifying the effect of water quality on eDNA degradation using microcosm and bioassay experiments*, Environmental DNA. https://doi.org/10.1002/edn3.530
3. Sakata, M. K., et al. (2020), *Sedimentary eDNA provides different information on timescale and fish species composition compared with aqueous eDNA*, Environmental DNA. https://doi.org/10.1002/edn3.75
4. Meshkat, N., Kuo, C. E., and DiStefano III, J. (2014), *On Finding and Using Identifiable Parameter Combinations in Nonlinear Dynamic Systems Biology Models and COMBOS*, PLOS ONE. https://doi.org/10.1371/journal.pone.0110261
5. Cuyt, A., and Lee, W. (2018), *Multivariate exponential analysis from the minimal number of samples*, Advances in Computational Mathematics. https://doi.org/10.1007/s10444-017-9570-8 ; preprint https://arxiv.org/abs/1610.06329
6. Kelleher, C., et al. (2013), *Identifiability of transient storage model parameters along a mountain stream*, Water Resources Research. https://doi.org/10.1002/wrcr.20413
7. Dallan, E., et al. (2023), *A Method for Calibrating the Transient Storage Model from the Early and Late-Time Behavior of Breakthrough Curves*, Water. https://doi.org/10.3390/w15050979
8. Godfrey, K. R., Jones, R. P., and Brown, R. F. (1980), *Identifiable pharmacokinetic models: the role of extra inputs and measurements*, Journal of Pharmacokinetics and Biopharmaceutics. https://doi.org/10.1007/BF01060058
