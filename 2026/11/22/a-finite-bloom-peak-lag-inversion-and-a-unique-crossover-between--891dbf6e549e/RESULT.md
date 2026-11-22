# A finite-bloom peak-lag inversion and a unique crossover between two serial toxin responses

## Finding

For a single finite rectangular toxicant exposure driving two successive first-order compartments, the terminal downstream response always peaks **after the input has stopped**. Its time lag is strictly decreasing in exposure duration and exactly invertible if the rates and input shutoff time are known. Two responses with different rates can reverse which peaks first as bloom duration varies. An exact two-pair construction has **one and only one** crossover, not merely an illustrative pair of numerical samples.

Write \(\tau_{r,s}(L)\) for the downstream peak lag after a positive input of duration \(L\). The exact formula is
\[
\tau_{r,s}(L)=\frac{1}{s-r}\log\!\left(\frac{1-e^{-sL}}{1-e^{-rL}}\right).
\]

For rate pairs \((r_A,s_A)=(1,5)\) and \((r_B,s_B)=(2,3)\), the peak-time ranking switches exactly once, at
\[
L_c=-\log z_0=0.281199574322962\ldots,
\qquad z_0^3+z_0^2=1,\quad 0<z_0<1.
\]
Response A peaks earlier for \(0<L<L_c\), and later for \(L>L_c\). Both peak strictly after the common shutoff time \(L\).

## Assumptions and scope

Time starts at the onset of one rectangular, spatially homogeneous input. For each separately calibrated response system fix \(q>0\), \(L>0\) and distinct rates \(0<r<s\) (inverse-time units), and take
\[
\dot U(t)=q\mathbf1_{[0,L]}(t)-rU(t),\quad
\dot V(t)=U(t)-sV(t),\qquad U(0)=V(0)=0.
\]
Here \(U\) is a hidden transient precursor burden and \(V\) the measured downstream burden, **not** total organismal toxicity. A different positive conversion factor in the second equation would rescale \(V\) without changing its peak time. Input shutoff is exact; rates do not vary with dose or time. For comparing A with B, both experience the same \(L\), but may have distinct positive input strengths. Rate labels can always be swapped because the impulse response is symmetric in the two rates; \(r<s\) fixes notation.

## Proof

**One peak and the exact lag.** The unit-input impulse response of the second compartment is
\[
g_{r,s}(u)=\frac{e^{-ru}-e^{-su}}{s-r},\quad u\ge0.
\]
It is positive at every \(u>0\). Thus \(V(t)=q\int_{\max(0,t-L)}^{t}g_{r,s}(u)\,du\). Before shutoff, \(V'(t)=qg_{r,s}(t)>0\) at all \(0<t\le L\). After shutoff,
\[
V'(t)=\frac{q}{s-r}\left[(e^{sL}-1)e^{-st}-(e^{rL}-1)e^{-rt}\right].
\]
The ratio of the positive first term to the second is strictly decreasing with \(t\); it is greater than one at \(t=L\) and tends to zero. Therefore exactly one derivative zero occurs after shutoff, from positive to negative, and it is the global maximum. Solving gives \(t_*=L+\tau_{r,s}(L)\) as stated.

**Duration inversion and conditioning.** Differentiating the lag yields
\[
\tau'_{r,s}(L)=\frac{\frac{s}{e^{sL}-1}-\frac{r}{e^{rL}-1}}{s-r}<0.
\]
Indeed \(y/(e^y-1)\) strictly decreases for positive \(y\), since its derivative has numerator \(e^y(1-y)-1<0\). Direct Taylor expansions show
\[
\tau_{r,s}(L)=\frac{\log(s/r)}{s-r}-\frac L2+\frac{r+s}{24}L^2+O(L^4)
\quad (L\downarrow0),
\]
whereas
\[
\tau_{r,s}(L)\sim\frac{e^{-rL}}{s-r}\quad(L\to\infty).
\]
Consequently \(L\mapsto\tau\) bijects \((0,\infty)\) onto \((0,\log(s/r)/(s-r))\). For a measured admissible lag, a single strictly monotone scalar equation determines duration, but \(\lvert dL/d\tau\rvert\sim1/(r\tau)\) diverges as the lag tends to zero. No claim of stable inversion is made near that boundary.

**Robust reversal criterion.** Consider two rate pairs with \(0<r_i<s_i\), and assume
\[
r_A<r_B,\qquad
\frac{\log(s_A/r_A)}{s_A-r_A}<\frac{\log(s_B/r_B)}{s_B-r_B}.
\]
For sufficiently short blooms the peak lag of A is strictly smaller than B by the small-duration limit; for sufficiently long blooms the slower dominant exponential \(e^{-r_A L}\) makes A's lag strictly larger. Continuity gives at least one crossover. The inequalities define an open, nonempty family of rate choices (for example \((1,5)\) versus \((2,3)\)); this criterion does **not** claim that every such choice has exactly one crossover.

**A complete exact one-crossover example.** Set \(z=e^{-L}\in(0,1)\). For A \((1,5)\) and B \((2,3)\),
\[
\tau_A=\tfrac14\log(1+z+z^2+z^3+z^4),\qquad
\tau_B=\log\!\left(\frac{1+z+z^2}{1+z}\right).
\]
The sign of \(\tau_A-\tau_B\) equals that of
\[
(1+z+z^2+z^3+z^4)(1+z)^4-(1+z+z^2)^4
=z(z^3-z-1)(z^3+z^2-1).
\]
On \((0,1)\), \(z^3-z-1<0\), while \(z^3+z^2-1\) increases strictly from \(-1\) to \(1\). Hence exactly one root \(z_0\in(0,1)\) exists and determines the sole crossover \(L_c\); its before/after signs follow since \(z=e^{-L}\) decreases with \(L\). The peak times themselves differ by precisely their post-shutoff lags, since their common input ends at \(L\).

## Verification

The standalone `CHECK.py` gives an independent symbolic factorization, verifies the root bracket and checks the derivative and endpoint predictions at many positive parameter sets and pulse lengths. These computations supplement, rather than replace, the exact sign and monotonicity proofs above. Run `python CHECK.py` with standard-library Python and SymPy installed. The critical proof is completely reproducible algebraically without this program.

## Relationship to prior work

Andres and coauthors [1] report timing-dependent paralytic-shellfish-toxin burdens, tissue transfer and post-removal toxin accumulation in experimental green-lipped mussels. Those findings motivate an ideal positive linear serial surrogate but do not establish the surrogate's kinetic rates or its mathematical timing comparison. Reijers and coauthors [2] experimentally study delayed drug concentration peaks after infusion and discuss adsorption/release, another physical mechanism not assumed here. Classical Bateman/serial exponential kinetics already gives the impulse response and many single-input peak results. The contribution assessed here is the **joint duration-inversion/conditioning statement and inter-response exposure-duration ranking reversal with an exact one-crossover example**, not the invention of two-stage kinetics or a claim that all ecological systems behave this way. A related published mathematical result characterizes two peaks from delayed unequal Bateman inputs; it concerns superposing distinct impulses within one system, rather than comparing the peak times of two distinct systems after one finite rectangular input.

## Limitations

The input is a single exact rectangular pulse; real blooms are time-varying and shellfish burdens have nonlinear, multiorgan and species-specific processes. Peak times alone cannot recover both unknown kinetic rates and duration simultaneously. The duration inverse presumes known shutoff time and rates and becomes arbitrarily poorly conditioned for long pulses. The general reversal criterion assures existence, not uniqueness; exact uniqueness is proved only for the displayed pairs. No observational data, confidence intervals, toxicity thresholds or risk-management outcomes are inferred. Historical priority is provisional; mathematical and pharmacokinetic literatures may contain equivalent results beyond the documents inspected.

## References

[1] Andres, J. K., et al. (9 August 2019), “Paralytic Shellfish Toxin Uptake, Assimilation, Depuration, and Transformation in the Southeast Asian Green-Lipped Mussel (Perna viridis),” *Toxins* 11(8), 468. https://doi.org/10.3390/toxins11080468 .

[2] Reijers, J. A. A., et al. (9 August 2017), “Potential Influence of Endothelial Adsorption on the Delayed Time to Maximum Concentration of Biopharmaceuticals,” *European Journal of Drug Metabolism and Pharmacokinetics* 43, 103–113. https://doi.org/10.1007/s13318-017-0430-1 .

[3] “A sharp reentrant two-peak window for delayed unequal Bateman inputs,” public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-reentrant-two-peak-window-for-delayed-unequal-bateman-in--2eb46436a2c9 .
