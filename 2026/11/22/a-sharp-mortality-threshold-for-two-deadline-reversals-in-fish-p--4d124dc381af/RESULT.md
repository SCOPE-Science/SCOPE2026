# A sharp mortality threshold for two deadline reversals in fish-passage timing

## Finding
Let a migrant's time to pass one barrier be either an exponential random variable of mean \(\tau>0\) (design E) or a two-stage Erlang variable with shape \(2\) and the same mean \(\tau\) (design R). An independent exponential mortality clock of rate \(\mu\ge 0\) runs throughout the attempt. A successful observation by deadline \(T>0\) requires passage before both mortality and the deadline. Define \(x=T/\tau\) and \(a=\mu\tau\), and write \(P_R(x,a)-P_E(x,a)=\Delta_a(x)\). Let \(x_-\in(0,1)\) and \(x_+>1\) be the two positive solutions of \(4x=e^x\), with \(x_-\approx0.357402956181389\) and \(x_+\approx2.153292364110349\).

**Theorem.** A unique \(a_c\in(0,1)\), approximately \(0.316461352642136\), is determined by \(\Delta_{a_c}(x_+)=0\). For \(a=0\), there is exactly one finite positive crossing \(c_1\in(x_-,x_+)\): R is worse for \(0<x<c_1\) and better for \(x>c_1\). For \(0<a<a_c\), there are exactly two distinct finite positive crossings \(c_1(a)\in(x_-,x_+)\) and \(c_2(a)>x_+\); R is better precisely for \(c_1(a)<x<c_2(a)\) and E is better elsewhere. For \(a=a_c\), R and E tie only at \(x=x_+\) among positive finite deadlines, with E otherwise strictly better. For \(a>a_c\), E is strictly better at every finite positive deadline. Moreover \(c_2(a)\to\infty\) as \(a\downarrow0\), while both crossings converge to \(x_+\) as \(a\uparrow a_c\).

These are comparisons of *unconditional probability of successful passage by the deadline*, not conditional transit times among eventual survivors. The passage-time distributions have exactly the same mean but different variability.

## Assumptions and scope
The barrier is treated as one isolated stochastic passage operation. A passage attempt begins at time zero. For E, the passage-time density is \(\tau^{-1}e^{-t/\tau}\). For R, the passage-time density is \(4t\tau^{-2}e^{-2t/\tau}\), corresponding to two independent exponential stages of rate \(2/\tau\). Mortality is independent of passage, occurs with constant hazard \(\mu\), and permanently prevents success. Neither design changes mean passage time or mortality hazard. Time is continuous; parameters satisfy \(\tau>0\), \(\mu\ge0\), \(T>0\). No claim is made for general passage distributions, multiple barriers, nonconstant hazards, or calibrated field response.

## Proof
With dimensionless time \(s=t/\tau\), independence of the death clock gives
\[
P_E(x,a)=\int_0^x e^{-(1+a)s}\,ds=\frac{1-e^{-(1+a)x}}{1+a},\qquad
P_R(x,a)=\int_0^x 4s e^{-(2+a)s}\,ds=\frac{4\{1-[1+(2+a)x]e^{-(2+a)x}\}}{(2+a)^2}.
\]
Consequently
\[
\Delta_a(0)=0,\qquad \Delta_a'(x)=e^{-ax}\bigl(4x e^{-2x}-e^{-x}\bigr)=e^{-(2+a)x}(4x-e^x).
\]
The strictly concave function \(\log(4x)-x\) tends to \(-\infty\) at both positive endpoints and attains \(\log4-1>0\) at \(x=1\). Hence it has exactly two roots \(x_-<1<x_+\); \(\Delta_a\) decreases on \((0,x_-)\), increases on \((x_-,x_+)\), and decreases on \((x_+,\infty)\), for *every* \(a\ge0\). In particular \(\Delta_a(x_-)<0\).

Direct integration gives
\[
\lim_{x\to\infty}\Delta_a(x)
=\frac4{(2+a)^2}-\frac1{1+a}
=-\frac{a^2}{(1+a)(2+a)^2}.
\]
At \(a=0\) this limit is zero. Strict decrease of \(\Delta_0\) after \(x_+\) implies \(\Delta_0(x_+)>0\). Therefore exactly one finite positive crossing exists at zero mortality, between \(x_-\) and \(x_+\), and \(\Delta_0(x)>0\) thereafter.

To classify positive mortality, put \(h(s)=4s e^{-2s}-e^{-s}\) and \(J(a)=\Delta_a(x_+)=\int_0^{x_+}e^{-as}h(s)\,ds\). Define \(H(a)=e^{a x_-}J(a)\). Then
\[
H'(a)=\int_0^{x_+}(x_--s)e^{a(x_--s)}h(s)\,ds<0,
\]
because \(h(s)<0\) on \((0,x_-)\) and \(h(s)>0\) on \((x_-,x_+)\). Moreover \(H(0)>0\), while \(H(a)\to-\infty\) as \(a\to\infty\): its negative integral over any compact subinterval of \((0,x_-)\) grows exponentially after multiplication by \(e^{a x_-}\), whereas the positive contribution is uniformly bounded. Thus a unique \(a_c>0\) has \(J(a_c)=0\). At \(a=1\), using \(e^{x_+}=4x_+\), direct simplification gives \(J(1)=-1/18+(3x_+/2-1)/(144x_+^3)<0\); indeed \(x_+>2\) since \(8>e^2\), and the positive fraction is less than \(1/384\). Thus \(a_c<1\). A numerical approximation of the unique root is provided only for orientation.

If \(0<a<a_c\), the positive interior maximum \(\Delta_a(x_+)>0\), the negative local minimum at \(x_-\), and the negative limit at infinity give exactly two positive zeros with the stated strict signs. At \(a=a_c\) the maximum equals zero, and at \(a>a_c\) it is negative, proving the remaining cases. The crossing-continuity assertions follow from continuity and strict monotonicity on each branch. The second crossing tends to infinity as \(a\downarrow0\) because on every finite compact interval to the right of the zero-mortality crossing, \(\Delta_0\) is strictly positive; it cannot converge to any finite positive limit. Finally, as \(a\uparrow a_c\), both crossings must converge to the only positive zero of \(\Delta_{a_c}\), namely \(x_+\). This completes the proof.

## Verification
The self-contained file `verify.py` implements both closed-form successful-passage probabilities and independent numerical quadratures of their defining integrals, brackets the two common stationary locations and the unique mortality threshold, and checks representative strict-sign patterns and the two-crossing regime. Its finite tests are supplementary to the analytical proof, not a proof over infinitely many parameters. Run `python3 verify.py` using Python's standard library; no data files are needed. The proof does not depend on its numerical root estimates.

## Relationship to prior work
Castro-Santos and Haro (2003) developed time-to-event analysis for fish passage at a hydroelectric barrier, including migratory delay and alternative routes, rather than exact comparisons between two specified equal-mean waiting-time laws under a shared independent mortality clock. Castro-Santos and Perry (2012) explicitly motivate the sequential and competing-risk approach to fishway performance, but do not present the stated mortality threshold or two-crossing classification in the material examined. Silva et al. (2018) describe approach, entry, passage and failure states and stress time-based passage and competing risks; their open full text was examined in the relevant methods and discussion sections. The standard Erlang/gamma CDF formulas yield the two probabilities, but not by themselves the global classification and uniqueness of the mortality threshold. Related literature on stochastic ordering of convolutions of exponential variables (Kochar and Xu, 2010) concerns different random-sum comparisons and does not supply this discounted, equal-mean, finite-deadline trichotomy in its inspected text.

## Limitations
This is an exact result in an idealized competing-risks model, not an empirically established optimal fishway design or a general claim that Erlang delays improve real migration. Equal mean does not imply equal variance or equal successful-passage probability. The common exponential mortality clock is independent of passage progress, and design choices are exogenous; both assumptions may fail in practice. Only the two stated waiting-time laws are classified. Historical priority remains subject to broader literature review; no independent scientific audit has been performed.

## References
- Castro-Santos, T., and Haro, A. (2003), *Quantifying migratory delay: a new application of survival analysis methods*, Canadian Journal of Fisheries and Aquatic Sciences 60, 986–996, https://doi.org/10.1139/f03-086 . Public record: https://www.usgs.gov/publications/quantifying-migratory-delay-a-new-application-survival-analysis .
- Castro-Santos, T., and Perry, R. W. (2012), *Time-to-event analysis as a framework for quantifying fish passage performance*, https://www.usgs.gov/publications/time-event-analysis-a-framework-quantifying-fish-passage-performance .
- Silva, A. T., et al. (2018), *The future of fish passage science, engineering, and practice*, Fish and Fisheries 19, 340–362, https://doi.org/10.1111/faf.12258 .
- Kochar, S., and Xu, M. (2010), *On the right spread order of convolutions of heterogeneous exponential random variables*, Journal of Multivariate Analysis 101, 165–176, https://doi.org/10.1016/j.jmva.2009.07.001 .
