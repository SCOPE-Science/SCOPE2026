# A sharp separation and feedback-gain window for three stable states in a dual-sigmoid phosphorus model

## Finding

An idealized water-column phosphorus model with two equally strong sediment-release components having distinct logistic thresholds has **three stable positive phosphorus equilibria** if and only if an exact separation threshold is exceeded and the recycling gain belongs to a uniquely determined open interval. The equilibrium count in that interval is exactly five. This is a phase classification of the specified two-component model, **not** the claim that five equilibria or three stable equilibria are unknown in general sums of logistic functions; their possibility was established in earlier work.

Put \(\sigma(u)=1/(1+e^{-u})\). For \(k,d,A>0\) and \(C_0>\max\{A,d/2\}\), choose the inflow \(I=C_0-A>0\) and define

\[
\frac{dP}{dt}=I-P+A\sigma\!\left(k(P-C_0+d/2)\right)+A\sigma\!\left(k(P-C_0-d/2)\right),\qquad P\ge0.
\]

Define \(\chi=\cosh(kd/2)>1\), and, for \(z>0\),

\[
R_\chi(z)=\frac{\sinh z}{z(\cosh z+\chi)},\qquad R_\chi(0)=\frac{1}{1+\chi}.
\]

When \(\chi>2\), \(R_\chi\) has one strict maximum at the unique \(z_*>0\) satisfying

\[
z_*(1+\chi\cosh z_*)=\sinh z_*(\cosh z_*+\chi).\]

Set
\[
A_-=\frac{1}{kR_\chi(z_*)},\qquad A_+=\frac{1+\chi}{k};\qquad A_-<A_+.
\]

**Complete classification, counting distinct equilibria**:

| Parameter range | Distinct equilibria | Attracting equilibria |
| --- | ---: | ---: |
| \(1<\chi\le2,\ 0<A\le (1+\chi)/k\) | 1 | 1 |
| \(1<\chi\le2,\ A>(1+\chi)/k\) | 3 | 2 |
| \(\chi>2,\ 0<A<A_-\) | 1 | 1 |
| \(\chi>2,\ A=A_-\) | 3 | 1 (plus two semistable folds) |
| \(\chi>2,\ A_-<A<A_+\) | **5** | **3** |
| \(\chi>2,\ A\ge A_+\) | 3 | 2 |

At \(A=(1+\chi)/k\) when \(\chi\le2\), the sole central equilibrium is attracting but nonhyperbolic. At \(A=A_+\) when \(\chi>2\), the central equilibrium is nonhyperbolic and repelling. All other listed attracting and repelling equilibria are hyperbolic, except the two folds at \(A=A_-\). In particular, **the three-attractor regime exists precisely if**

\[
\boxed{d>\frac{2\operatorname{arcosh}(2)}{k}},
\]

and, given this separation, it exists precisely for \(A_-<A<A_+\). There are no additional positive equilibria.

A fully explicit witness is \(k=1\), \(d=2\operatorname{arcosh}(5)\), \(A=5\), \(C_0=10\), \(I=5\). It has exactly five equilibria: the central \(P=10\), inner repelling equilibria approximately \(P=10\pm1.742484457548911\), and outer attracting equilibria approximately \(P=10\pm4.498230306825003\). The central one is also attracting. These approximations illustrate, but do not prove, the universal theorem.

## Assumptions and scope

The state \(P(t)\) is a **dimensionless, well-mixed** phosphorus concentration proxy, not a laboratory calibration. The two positive logistic terms model two equal-capacity sediment phosphorus release components whose pH-response thresholds are symmetrically placed. A linear and positive pH-to-phosphorus feedback and common effective slope \(k\) are postulated, not derived from the motivating sediment experiment. The choice \(I=C_0-A\) centers the fixed-point equation and makes symmetry exact. Fixed parameters, linear removal, no water-depth dynamics, no seasonal forcing, and no microbial state variables are assumed. The condition \(C_0>\max\{A,d/2\}\) ensures positive inflow, positive nominal thresholds and positive equilibrium concentrations. Since the vector field is positive at \(P=0\) and negative for sufficiently large \(P\), solutions starting nonnegative remain nonnegative and bounded forward in time. All claims are quantified over the stated real parameter domain.

## Proof

**1. Reduction and boundedness.** Write \(y=P-C_0\) and \(z=ky\). Direct addition of the two logistics gives

\[
\sigma(z+kd/2)+\sigma(z-kd/2)-1=\frac{\sinh z}{\cosh z+\cosh(kd/2)}.
\]

Thus \(\dot y=G(y)\), where

\[
G(y)=A E_\chi(ky)-y,\quad E_\chi(z)=\frac{\sinh z}{\cosh z+\chi}.
\]

\(G\) is odd. Since \(|E_\chi(z)|<1\), any equilibrium satisfies \(|y|<A\). Hence \(P=C_0+y>C_0-A>0\). The centered state \(y=0\) is always an equilibrium. Every positive noncentral displacement corresponds to a unique positive solution of

\[
\frac{1}{Ak}=R_\chi(z),\qquad z>0.
\]

It contributes an equal negative equilibrium displacement by oddness.

**2. A single possible positive peak.** Straight differentiation yields

\[
E_\chi'(z)=\frac{1+\chi\cosh z}{(\cosh z+\chi)^2},\qquad
E_\chi''(z)=\frac{\sinh z\,(\chi^2-2-\chi\cosh z)}{(\cosh z+\chi)^3}.
\]

If \(1<\chi\le2\), then \(E_\chi''(z)<0\) for all \(z>0\). Since \(E_\chi(0)=0\), the ratio \(R_\chi(z)=E_\chi(z)/z\) strictly decreases from \(1/(1+\chi)\) to zero. It therefore intersects a horizontal positive level in either zero or one positive point, according to whether \(A\le(1+\chi)/k\) or \(A>(1+\chi)/k\).

If \(\chi>2\), put \(z_0=\operatorname{arcosh}(\chi-2/\chi)>0\). The second derivative \(E_\chi''\) is positive on \((0,z_0)\) and negative on \((z_0,\infty)\). Define

\[
J_\chi(z)=zE_\chi'(z)-E_\chi(z),\qquad J_\chi'(z)=zE_\chi''(z).
\]

Here \(J_\chi(0)=0\), \(J_\chi\) increases strictly on \((0,z_0)\), decreases strictly afterward, and tends to \(-1\) as \(z\to\infty\). Consequently, it vanishes exactly once on \((0,\infty)\), at \(z_*>z_0\). Because \(R_\chi'(z)=J_\chi(z)/z^2\), the ratio strictly increases to the global maximum \(R_\chi(z_*)\), then strictly decreases to zero. Its maximum is strictly greater than its initial value \(1/(1+\chi)\), proving \(A_-<A_+\). The stated equation for \(z_*\) is exactly \(J_\chi(z_*)=0\) with positive denominators cleared.

**3. Exact root count.** For \(A<A_-\), \(1/(Ak)\) lies above the ratio maximum, so there is no nonzero equilibrium. At \(A=A_-\) the horizontal line touches at one positive \(z\), producing precisely the two symmetric nonzero fold equilibria and the centered one. For \(A_-<A<A_+\) the line lies strictly between \(R_\chi(0)\) and its maximum, and meets the ascending and descending branches once each; these yield four distinct nonzero equilibria and the center. At \(A=A_+\) it coincides with \(R_\chi(0)\) but, because \(R_\chi(z)>R_\chi(0)\) immediately to the right of zero, it has exactly one *positive* intersection on the descending branch; the center remains and the outer symmetric pair persists. The same one-positive-intersection statement holds for every \(A>A_+\). This yields every row of the table. At most five distinct equilibria occur.

**4. Stability and degeneracies.** Since \(G(y)=y(AkR_\chi(ky)-1)\) for \(y>0\), the sign diagram immediately gives the attracting/repelling alternation for the positive roots; oddness gives the corresponding negative roots. Moreover \(G'(0)=Ak/(1+\chi)-1\): the center is attracting below \(A_+\) and repelling above it. At \(A=A_+\) with \(\chi\le2\), strict decrease of \(R_\chi\) gives \(G(y)<0\) for \(y>0\) and stability from both sides even though \(G'(0)=0\). With \(\chi>2\), the initial increase of \(R_\chi\) instead makes \(G(y)>0\) for small \(y>0\), proving the central equilibrium is repelling at the same zero-derivative boundary. At \(A=A_-\) the two nonzero tangencies are semistable, and the center remains attracting. All strict sign-changing crossings are simple because they lie on strict monotonic branches of \(R_\chi\). This proves the full classification.

**5. Exact five-root certificate.** For \(k=1\), \(\chi=5\), \(A=5\), the central derivative is \(G'(0)=5/6-1=-1/6<0\). At \(y=\log9\), the identity \(E_5(\log9)=20/43\) gives

\[
G(\log9)=\frac{100}{43}-\log9>0.
\]

Indeed \(\log9<9/4<100/43\): the first inequality follows from the first six positive Taylor terms in \(e^{9/4}\), whose sum already exceeds nine. Also \(G(5)<5-5=0\), because \(E_5(5)<1\). There is therefore one root between zero and \(\log9\), and another between \(\log9\) and 5. The one-peak theorem excludes any further positive roots. Oddness supplies their two negative partners, totaling exactly five. With \(C_0=10>A\), every one is a strictly positive phosphorus concentration.

## Verification

The independent Python script `verify.py` uses SymPy to check the logistic-addition identity and both nonstandard derivative identities; it verifies the *exact* rational Taylor and sign witnesses, then uses arbitrary precision to check representative parameter regimes and the example's stability signs. Execute `python verify.py` with SymPy and mpmath installed. The global quantifiers are proved by the sign and monotonicity arguments above, **not** by the finite tests. The approximate equilibrium positions are diagnostic only. No observational measurements were fitted.

## Relationship to prior work

Ding et al. (2023) empirically formulate a *single* logistic sediment phosphorus equilibrium response to pH. The present two-component model and linear positive feedback are new **assumptions** for a benchmark, not a theorem or calibrated mechanism in that paper. Carpenter (2005) and Zeng et al. (2017) discuss lake eutrophication and standard alternative stable states, but their systems do not establish the exact two-logistic separation-and-gain window here.

Crucially, Wainwright (2020, section 3.4 and Appendix A) *already* proves that a sum of two logistic responses can have at most five fixed points and, when it has five, three are stable. Those **general observations are not claimed as new**. Wainwright's classification and symmetric case do not supply the analytic boundary \(\chi=2\) and unique gain interval \((A_-,A_+)\) for the continuous-time, symmetrically staggered sediment-response family. The mathematical contribution asserted here is this explicit **necessary-and-sufficient two-parameter frontier with complete boundary classification** and proof, not the abstract possibility of tri-stability. Duncan et al. (2021) address stability of networks of steep sigmoids, not the stated exact finite-slope critical surfaces. General logistic-mixture modality studies may contain related curvature thresholds; mathematical priority beyond inspected documents is not established.

## Limitations

The result does not demonstrate that any actual lake has three stable water-phosphorus regimes, nor that the required feedback intensity or separation is realistic. Phosphorus release, pH and algal growth are coupled dynamically in nature; explicit pH dynamics, hydrology, mixed nonlinear kinetics, unequal sediment-pool amplitudes, and stochastic disturbances are outside the exact theorem. Only the symmetric equal-slope, equal-amplitude two-pool family is completely classified. All source dates refer to earliest verified accessible public evidence, not later journal pagination. The motivating experimental article's full text was not accessible despite open-access and authorized institutional retrieval attempts, so its methods and appendices cannot be excluded as an originality risk solely from the abstract.

## References

1. Y. Ding, Q. Yi, Q. Jia, J. Zhang, Z. Zhou, X. Liu, “Quantifying phosphorus levels in water columns equilibrated with sediment particles in shallow lakes: From algae/cyanobacteria-available phosphorus pools to pH response,” *Science of the Total Environment* 868 (2023), 161694. Epub 2023-01-21. https://doi.org/10.1016/j.scitotenv.2023.161694 ; https://pubmed.ncbi.nlm.nih.gov/36690114/.
2. S. R. Carpenter, “Eutrophication of aquatic ecosystems: Bistability and soil phosphorus,” *PNAS* 102 (2005), 10002–10005. https://doi.org/10.1073/pnas.0503959102 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC1177388/.
3. C. Zeng et al., “Stochastic ecological kinetics of regime shifts in a time-delayed lake eutrophication ecosystem,” *Ecosphere* (2017). https://doi.org/10.1002/ecs2.1805.
4. A. Wainwright, “A Model of Pro-Environmental Behaviour with Heterogeneous Agents,” MRes dissertation, University of Bath (2020), section 3.4 and Appendix A. https://purehost.bath.ac.uk/ws/portalfiles/portal/212053187/MRes_Dissertation.pdf.
5. W. Duncan, T. Gedeon, H. Kokubu, K. Mischaikow, H. Oka, “Equilibria and Their Stability in Networks with Steep Sigmoidal Nonlinearities,” arXiv:2103.17184 (first posted 2021-03-31), https://arxiv.org/abs/2103.17184.
