# A unique finite-horizon reversal for reactive transient storage in a two-zone stream model

## Finding

A single mobile parcel can leave a stream reach, react in the mobile water, or enter and later return from a reactive transient-storage zone. Under the rates and initial condition below, adding the storage zone has a complete, sharp three-regime effect on the probability of **reaction by a fixed deadline**:

1. When storage has no reaction, cumulative reaction is strictly *smaller* at every finite positive deadline and equal in the infinite-horizon limit.
2. When the positive storage reaction rate is strictly below the mobile reaction rate, there is exactly one finite positive deadline \(T_*\). Storage strictly decreases cumulative reaction before \(T_*\) and strictly increases it after \(T_*\).
3. When the storage reaction rate is at least the mobile reaction rate, storage strictly increases cumulative reaction at every positive deadline.

In the middle regime, the unique deadline \(T_*\) strictly decreases as the storage reaction rate increases, diverges logarithmically as that rate approaches zero, and vanishes linearly as it approaches the mobile reaction rate. This is a statement about a precisely specified continuous-time competing-risk model, not an empirical stream-reach prediction.

## Assumptions and scope

Fix four positive rates \(v,\alpha,\beta,k>0\) and a storage reaction rate \(\ell\ge0\). All have units of inverse time. A mass-normalized solute parcel starts mobile. While mobile it exits the modeled reach irreversibly at rate \(v\), reacts irreversibly at rate \(k\), and enters storage at rate \(\alpha\). In storage it reacts irreversibly at rate \(\ell\) or returns mobile at rate \(\beta\). All exponential competing clocks are independent conditional on the current state. No material enters after the initial unit pulse.

Let \(M(t)\), \(S(t)\) be the probabilities of remaining unreacted and unexited in the mobile and storage states, and \(U_\ell(t)\) the probability of having reacted by time \(t\). Their forward equations are

\[
\begin{aligned}
M'&=-(v+k+\alpha)M+\beta S,\\
S'&=\alpha M-(\beta+\ell)S,\\
U_\ell'&=kM+\ell S,\\
(M(0),S(0),U_\ell(0))&=(1,0,0).
\end{aligned}
\]

The no-storage comparator removes the transition into storage, leaving all other relevant rates fixed. Its cumulative reaction probability is

\[
U_0^{\mathrm{base}}(t)=\frac{k}{v+k}\bigl(1-e^{-(v+k)t}\bigr).
\]

The subscript \(0\) in \(U_0^{\mathrm{base}}\) denotes no storage; the distinct notation \(U_{\ell=0}\) means *inert but still accessible* storage. The comparison is for every real \(t>0\), not solely at a selected observation time.

## Proof

**Exact two-state spectrum.** Put \(c=v+k\), \(A=c+\alpha\), \(B=\beta+\ell\), and

\[
\Delta=\sqrt{(A-B)^2+4\alpha\beta},\qquad
\lambda_\pm=\frac{A+B\pm\Delta}{2}.
\]

Since \(AB-\alpha\beta=c(\beta+\ell)+\alpha\ell>0\), both eigen-decay rates \(\lambda_-<\lambda_+\) are positive. Solving the two-state equations with the given initial condition yields

\[
U_\ell'(t)=P e^{-\lambda_-t}+Qe^{-\lambda_+t},
\]

where

\[
P=\frac{k(\lambda_+-A)+\alpha\ell}{\Delta},\qquad
Q=\frac{k(A-\lambda_-)-\alpha\ell}{\Delta},\qquad P+Q=k.
\]

Consequently

\[
U_\ell(t)=\frac{P}{\lambda_-}(1-e^{-\lambda_-t})+
\frac{Q}{\lambda_+}(1-e^{-\lambda_+t}). \tag{1}
\]

Equation (1) remains valid if \(Q\) is negative; positivity of \(Q\) is asserted only in the regime where it is proved below.

**Strictly slower storage reaction, \(0\le\ell<k\).** Evaluate the characteristic polynomial of the positive decay matrix at \(c\):

\[
(A-c)(B-c)-\alpha\beta=\alpha(\ell-c)<0.
\]

Thus \(0<\lambda_-<c<\lambda_+\). The symmetric positive off-diagonal product \(\alpha\beta>0\) gives \(\lambda_+>A\), so \(P>0\). Moreover,

\[
k(A-\lambda_-)-\alpha\ell
=k(c-\lambda_-)+\alpha(k-\ell)>0,
\]

hence \(Q>0\). Divide the reaction density by the no-storage reaction density \(k e^{-ct}\):

\[
F(t)=\frac{U_\ell'(t)}{k e^{-ct}}
=\frac{P}{k}e^{(c-\lambda_-)t}
+\frac{Q}{k}e^{-(\lambda_+-c)t}.
\]

Here \(F(0)=1\), \(F''(t)>0\) for every \(t\ge0\), and the forward equations give

\[
F'(0)=\frac{\alpha(\ell-k)}{k}<0.
\]

As \(t\to\infty\), \(F(t)\to\infty\). Strict convexity implies that \(F(t)=1\) has exactly one *positive* solution \(t_1\), with \(F<1\) on \((0,t_1)\) and \(F>1\) after \(t_1\). Equivalently, the derivative of the cumulative difference

\[
H_\ell(t)=U_\ell(t)-U_0^{\mathrm{base}}(t)
\]

is strictly negative until \(t_1\), then strictly positive thereafter, while \(H_\ell(0)=0\). First-step equations for the eventual probability of reaction give

\[
\begin{aligned}
U_\ell(\infty)
&=\frac{k(\beta+\ell)+\alpha\ell}
{c(\beta+\ell)+\alpha\ell},\\
H_\ell(\infty)
&=\frac{\alpha v\ell}
{c\,[c(\beta+\ell)+\alpha\ell]}.
\end{aligned}\tag{2}
\]

For \(0<\ell<k\), (2) is strictly positive. Because \(H_\ell\) first strictly decreases and then strictly increases to a positive limit, it has precisely one positive zero \(T_*>t_1\), with the signs asserted in the finding. For \(\ell=0\), the limit (2) is zero; after \(t_1\) the difference increases strictly *to zero*, so \(H_0(t)<0\) at every finite \(t>0\). These arguments also establish the equality of eventual reaction probabilities for completely inert storage.

**At-least-as-reactive storage, \(\ell\ge k\).** Couple the two experiments using a common global reaction clock of rate \(k\), a common candidate exit clock of rate \(v\), and independent entry/return clocks. The no-storage parcel is killed by reaction at the first global reaction event if it has not already exited, and exits at the first candidate exit event if still alive. The storage-enabled parcel is killed at the same global reaction event whenever still present, faces candidate exit events *only while mobile*, and additionally faces a storage-only reaction clock of rate \(\ell-k\). Thus every trajectory in which the no-storage parcel reacts by \(t\) also makes the storage-enabled parcel react by \(t\). Strictness for every \(t>0\) follows from the positive-probability event of entering storage, having a candidate exit while stored, and undergoing the shared reaction before return or the deadline. Therefore \(H_\ell(t)>0\) for all \(t>0\).

**Monotone crossover and sharp endpoint scales.** For fixed \(v,\alpha,\beta,k\), coupling additional storage-only reaction clocks establishes that \(U_\ell(t)\) is strictly increasing in \(\ell\) for every fixed \(t>0\). The one-zero conclusion then implies that \(T_*(\ell)\) is strictly decreasing on \((0,k)\). Continuity of (1), strict negativity for \(\ell=0\) at every fixed finite horizon, and strict positivity for \(\ell=k\) at every fixed positive horizon yield

\[
T_*(\ell)\to\infty\quad(\ell\downarrow0),\qquad
T_*(\ell)\to0\quad(\ell\uparrow k).
\]

For a sharper statement, let \(\nu=\lambda_-(0)\) and \(P_0=P|_{\ell=0}>0\) with all other rates fixed. Equation (2) has the expansion \(H_\ell(\infty)=\alpha v\ell/(c^2\beta)+O(\ell^2)\). At the unique crossing, the slow eigenmode in (1) dominates the remaining exponential terms. For sufficiently small \(\ell\), the slow eigenvalue remains above \(\nu/2\), and the exponential remainder in (1) is bounded by a fixed multiple of \(e^{-\lambda_- t}\); evaluating the cumulative difference at \(t=3\log(1/\ell)/\nu\) makes this remainder \(o(\ell)\) while (2) is positive of order \(\ell\). This proves \(T_*(\ell)=O(\log(1/\ell))\). Since \(\lambda_-(\ell)=\nu+O(\ell)\), the crossing equality then gives

\[
T_*(\ell)=\frac1\nu\log\left(
\frac{c^2\beta P_0}{\alpha v\nu\ell}
\right)+o(1)\qquad(\ell\downarrow0).\tag{3}
\]

For the opposite endpoint, set \(\delta=k-\ell\). Differentiating the forward equations at zero gives the uniform local Taylor expansion

\[
H_{k-\delta}(t)=-\frac{\alpha\delta}{2}t^2+
\frac{\alpha vk}{6}t^3+O(\delta t^3+t^4).
\]

Use the previously proved \(T_*(k-\delta)\to0\), substitute \(t=\delta z\), and apply the unique positive-root condition to obtain

\[
T_*(\ell)=\frac{3(k-\ell)}{vk}+O((k-\ell)^2)
\qquad(\ell\uparrow k).\tag{4}
\]

The first nonzero negative term in this expansion and its next positive term have distinct physical origins: the initial loss of fast mobile reactions during temporary storage, and the later prevention of premature exit while stored.

## Verification

The included standalone `check.py` uses Python's standard library only. Running `python3 check.py` in the directory containing this document prints `PASS: 7146 diagnostic assertions` when all tests succeed. It independently computes the four-state absorbing continuous-time Markov process by uniformization and compares it to formula (1), checks first-step absorption identities using exact rational arithmetic, exercises both signs around numerically bracketed unique crossover times, tests both boundary regimes and monotonicity, and checks the endpoint scaling limits. The numerical tests are finite diagnostics; the all-parameter assertion rests on the proof above, not on enumeration.

For example, with \((v,\alpha,\beta,k,\ell)=(1.3,1.1,0.8,2,0.6)\) the reaction-density crossover is approximately \(0.6141758202\), the **cumulative** reaction crossover is approximately \(T_*=1.5349178811\), and the ultimate reaction advantage from storage is approximately \(0.0492424242\) in probability units. No calibration to a field experiment is claimed.

## Relationship to prior work

O'Connor, Hondzo and Harvey (first published 9 November 2009) explicitly formulate first-order stream/storage exchange and channel/storage reaction and demonstrate the importance of transient storage when interpreting observed nutrient uptake. The model here is a *single exponentially exiting parcel*, with a fixed observation deadline and a direct comparator to a stream without storage; it is not the original spatial advection-dispersion partial differential equation of that paper. The original paper's continuum equations do not, by themselves, state this three-regime cumulative-reaction comparison, its unique finite switching deadline, or the two sharp endpoint laws.

Liao, Lemke, Osenbrück and Cirpka (2013) treat reactive stream-tracer breakthrough inversion with residence-time and sorption dynamics; Boano and colleagues (2014) review reactive hyporheic exchange and time-scale limitations; Aubeneau and colleagues (published online 9 January 2015) formulate and simulate more general continuous-time random-walk transport with zone-specific reactions and give a distinct *hyporheic signal detection time* comparison. Their inspected material concerns downstream breakthrough, inverse identification, and kinetic tempering rather than the exact signed cumulative reaction **relative to no storage** of the present two-state competing-risk model. The current classification is not established merely by the generic possibility of representing two transient states by sums of exponentials: the sign trichotomy, the unique cumulative crossing, and endpoint scales require the particular competing-risk constraints.

The result should be treated as provisional with respect to historical priority. Related textbook phase-type and competing-risk models may permit an unlocated equivalent formulation. No priority claim is based solely on absent search hits.

## Limitations

A parcel-level exponential reach-exit clock is a deliberately coarse alternative to spatial advection-dispersion, and its fixed rate is not a calibrated discharge distribution. Entry and return are memoryless; rates are constant; reactions are first order and irreversible; there is one homogeneous storage zone; the model has no nonlinear sorption, flow-dependent feedback, lateral loading, finite detection thresholds, or spatial gradients. Cumulative reaction is not identical to measured downstream concentration or whole-stream restoration performance. The proof does not address arbitrary residence-time distributions, multiple reactive zones, or empirically inferred reaction rates. Source coverage and general phase-type precedent remain potential priority risks. Independent external validation has not been performed.

## References

1. O'Connor, B. L., Hondzo, M., and Harvey, J. W. (2010). *Predictive Modeling of Transient Storage and Nutrient Uptake: Implications for Stream Restoration.* Journal of Hydraulic Engineering 136, 1018–1032. First published online 9 November 2009. DOI: https://doi.org/10.1061/(ASCE)HY.1943-7900.0000180 . Lawful author-hosted manuscript: https://water.usgs.gov/nrp/jharvey/pdf/O%27Connor%20et%20al_2010%20Predictive%20transient%20storage%20modeling_JHE.pdf
2. Liao, Z., Lemke, D., Osenbrück, K., and Cirpka, O. A. (2013). *Modeling and inverting reactive stream tracers undergoing two-site sorption and decay in the hyporheic zone.* Water Resources Research 49, 3406–3422. https://doi.org/10.1002/wrcr.20276
3. Boano, F., et al. (2014). *Hyporheic flow and transport processes: Mechanisms, models, and biogeochemical implications.* Reviews of Geophysics 52, 603–679. https://doi.org/10.1002/2012RG000417
4. Aubeneau, A. F., et al. (2015). *Effects of benthic and hyporheic reactive transport on breakthrough curves.* Freshwater Science 34, 301–315. Published online 9 January 2015. https://doi.org/10.1086/680037
