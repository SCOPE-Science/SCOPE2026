# A sharp global drawdown-duration switch for two fish-refuge classes

## Finding

**Theorem (complete global optimum and a discontinuous policy boundary).** Consider a fish class mixture with fast-refuge fraction \(0<w<1\), positive response rate \(\lambda>0\), positive independent exposure-mortality rate \(\mu>0\), and deterministic refuge-travel requirements \(0\le c_f<c_s\). Each individual has an independent exponential reaction latency of rate \(\lambda\). A member of class \(j\in\{f,s\}\) succeeds under a drawdown of duration \(T\ge0\) exactly when its latency plus \(c_j\) is no greater than \(T\), and its independent exponential mortality clock of rate \(\mu\) exceeds \(T\). The expected successful fraction is

\[
S(T)=e^{-\mu T}\left[w(1-e^{-\lambda(T-c_f)})_+ +(1-w)(1-e^{-\lambda(T-c_s)})_+\right],
\]

where \((1-e^{-\lambda u})_+=0\) for \(u\le0\), and equals \(1-e^{-\lambda u}\) for \(u>0\). Put

\[
r=\frac{\mu}{\lambda},\qquad d=\lambda(c_s-c_f),\qquad K=1+\frac1r,\qquad C(d)=w+(1-w)e^d,
\]
\[
 d_* =\log\frac{w^{-1/r}-w}{1-w},\qquad
 T_f=c_f+\frac{\log K}{\lambda},\qquad
 T_s(d)=c_f+\frac{\log(KC(d))}{\lambda}.
\]

Then \(d_*>\log K>0\) and the **entire set of global maximizing drawdown durations** is

\[
\boxed{\operatorname*{arg\,max}_{T\ge0}S(T)=
\begin{cases}
\{T_s(d)\},&0<d<d_*,\\
\{T_f,T_s(d_*)\},&d=d_*,\\
\{T_f\},&d>d_*.
\end{cases}}
\]

At coexistence the two optimal durations are strictly separated, and their exact gap is

\[
\boxed{T_s(d_*)-T_f=\frac{-\log w}{\mu}>0.}
\]

As the slow class's additional refuge travel requirement increases through the sharp threshold, the globally preferred drawdown duration thus **jumps downward** by \(-\log(w)/\mu\), even though the maximum success probability is continuous. Every single-class version has one continuously varying optimal duration, so two distinct required refuge-travel times are the minimal heterogeneity in this model for this phenomenon.

## Assumptions and scope

The decision is the **duration** of one fixed-amplitude, constant-rate drawdown, not an arbitrary flow waveform. If the level/discharge reduction is fixed at \(H>0\), corresponding mean ramping speed is \(H/T\). Every animal is assigned to the fast or slow class with the fixed frequencies above; within either class, refuge-travel time is deterministic. Reaction latency is memoryless; exposure death runs independently for the whole drawdown, even if refuge is reached earlier; and failures of either condition imply no success. No between-fish variation in rates, channel morphology, feedback behavior, predation, repeated peaks, or density dependence is modeled. The analytical statement concerns this explicit surrogate, not a calibrated hydrodynamic or fisheries policy.

Both rates are strictly positive and \(c_s>c_f\ge0\); the thresholds, maxima, and equality statements apply to every admissible real parameter choice. All logarithm arguments above are positive. The dimensionless delay \(d\) is varied by changing \(c_s\) while fixing \(c_f,w,\lambda,\mu\).

## Proof

**1. Probability law.** For an exponential reaction time \(L\) of rate \(\lambda\), independence gives
\[
\Pr\{L+c_j\le T,\ M>T\}=e^{-\mu T}(1-e^{-\lambda(T-c_j)})_+.
\]
Averaging over the two mutually exclusive classes proves the displayed expression for \(S\). For \(T<c_f\), success is zero; since it is positive for some later \(T\), no such time maximizes it.

**2. Exactly one candidate on each smooth branch.** Write \(s=\lambda(T-c_f)\). Up to the positive constant \(e^{-\mu c_f}\), the objective on \(s\ge0\) is
\[
F(s)=\begin{cases}
w(e^{-rs}-e^{-(r+1)s}),&0\le s<d,\\
e^{-rs}-C(d)e^{-(r+1)s},&s\ge d.
\end{cases}
\]
For any \(A>0\), the smooth profile \(e^{-rs}-A e^{-(r+1)s}\) has its unique unrestricted maximum at \(s=\log(KA)\), with value
\[
 B A^{-r},\qquad B=\frac{r^r}{(r+1)^{r+1}}>0.
\]
Thus the *unrestricted* maximum of the early branch is \(wB\), at \(s_f=\log K\); the unrestricted maximum of the late branch is \(BC(d)^{-r}\), at \(s_s=\log(KC(d))\). These are upper bounds on each restricted branch even when a stationary point lies outside that branch.

**3. Existence and feasibility of the tie.** Since \(C(d)\) increases strictly from \(1\) to infinity, the two upper bounds are equal at exactly one positive delay, given by \(wC(d_*)^r=1\), which solves to the displayed \(d_*\). By strict convexity of \(u\mapsto u^{-1/r}\), its chord lies strictly above its tangent at \(u=1\), so
\[
w^{-1/r}>1+\frac{1-w}{r};
\]
subtracting \(w\) and dividing by \(1-w\) proves \(e^{d_*}>K\), hence \(d_*>s_f\).

At the tie, \(C(d_*)=w^{-1/r}\). With \(q=K=1+1/r>1\), strict convexity of \(u\mapsto u^q\) implies
\[
\frac{e^{d_*}}{C(d_*)}=\frac{1-w^q}{1-w}<q=K.
\]
Hence \(s_s(d_*)>d_*\): the late stationary maximum is *inside its actual branch* at the tie. Moreover, \(s_s(d)-d=\log(K[w e^{-d}+1-w])\) strictly decreases with \(d\). It follows that \(s_s(d)>d\) for every \(0<d\le d_*\). This step is required: comparing two **unrestricted** maxima alone would not establish a global optimum.

**4. Strict global comparison.** For \(d<d_*\), \(wC(d)^r<1\) and therefore \(BC(d)^{-r}>wB\). The late peak is feasible by Step 3 and strictly exceeds every early-branch value; it is the unique global maximizer. At \(d=d_*\), the early peak is feasible because \(d_*>s_f\), and the late peak is feasible by Step 3. Both achieve \(wB\), no other point on either strictly unimodal smooth branch achieves that value, and the join \(s=d_*\) achieves strictly less. For \(d>d_*\), \(d>s_f\) and \(wB>BC(d)^{-r}\); the early peak is feasible and strictly exceeds every value on the late branch. This gives all strict and equality cases, including the joining boundary.

**5. Jump size, sharpness and minimality.** At the tie, \(s_s(d_*)-s_f=\log C(d_*)=-\log(w)/r\). Dividing by \(\lambda\) proves the jump \(-\log(w)/\mu\). Both branch maxima depend continuously on \(d\); hence their maximum does, though its maximizing argument switches discontinuously. For a sole fast class or coincident refuge times, the expression reduces to a positive multiple of \(e^{-\mu T}(1-e^{-\lambda(T-c)})_+\), with the unique optimum \(T=c+\log(1+\lambda/\mu)/\lambda\), which varies continuously with \(c\). Thus one class cannot exhibit this abrupt global switch.

## Verification

The standard-library script `checker.py` runs 5,000 seeded randomized admissible parameter cases, comparing the claimed optimum against 301 time-grid values and the nonsmooth join (1,505,000 grid evaluations plus 5,000 join checks). It also checks 20 critical-delay identities at different hazard ratios and weights. These finite comparisons are diagnostic, **not** a proof for all real inputs; the full proof is Steps 1–5.

There is an exact nondegenerate witness with \(\lambda=\mu=1\), \(w=1/3\), \(c_f=\log2\), and \(c_s=\log8\). Then \(d=\log4=d_*\). The two distinct global optima are \(T_f=\log4\) and \(T_s=\log12\), each with success probability exactly \(1/24\). At the intervening joining time \(T=c_s=\log8\), the probability is only \(1/32\). These are exact rational evaluations of exponential factors, not rounded numerical fits.

## Relationship to prior work

Hedger and colleagues (2023) use an individual-based model to examine the effects of down-ramping speed, movement speed and stranding susceptibility on salmon parr; their sensitivity analysis does not state a two-class exponential-latency optimization theorem. Their study notes that biological properties were not varied among individuals in the simulations. Hayes and colleagues (2019) discuss stage-specific flow rules, rather than deriving this global policy boundary. Le Coarer and colleagues (2022) develop a hydraulic shoreline-recession indicator, not the present individual-response objective.

There is a **precise mathematical relation** to previously analyzed delayed Bateman profiles: our normalized function is a positive weighted mixture of two *shifted two-exponential response profiles*. Published work on delayed Bateman inputs derives the existence and number of local peaks, plus stationary-point formulas, in a broader fixed-amplitude response setting. Those facts are prior mathematics, **not** claimed as new. The current claim instead classifies which peak is **globally optimal along the biologically constrained amplitude path**, gives the single exact delay threshold for that global dominance, and calculates the optimizer's jump. The inspected published mode-count result does not state this global-dominance result; nevertheless its formulas are closely related and make independent historical priority particularly important to check.

## Limitations

This model intentionally replaces hydraulic evolution and spatial movement with two fixed refuge-travel times, one exponential reaction clock and a whole-event independent mortality clock. The whole-event mortality assumption does not describe a refuge that eliminates risk immediately on arrival. The predicted discontinuity need not persist under arbitrary heterogeneity of all parameters, other survival laws, finite control bounds or physical river geometry. A mathematically positive success fraction does not imply a realistic field success rate. The model is not calibrated to empirical fish survival, and provides no operational ramping rate recommendation. Historical originality is conditional on the inspected sources; adjacent exponential-mixture literature may give stronger coverage. No independent scientific audit or field validation has been performed.

## References

1. Hedger, R. D., Sundt-Hansen, L. E., Juárez-Gómez, A., Alfredsen, K., and Foldvik, A. (2023), *Exploring sensitivities to hydropeaking in Atlantic salmon parr using individual-based modelling*, *Ecohydrology* 16(6), e2553, first online 2023-04-24, https://doi.org/10.1002/eco.2553 .
2. Hayes, D. S. et al. (2019), *Life Stage-Specific Hydropeaking Flow Rules*, *Sustainability* 11(6), 1547, https://doi.org/10.3390/su11061547 .
3. Le Coarer, Y., Lizée, M.-H., Beche, L., and Logez, M. (2023), *Horizontal ramping rate framework to quantify hydropeaking stranding risk for fish*, first online 2022-12-05, https://doi.org/10.1002/rra.4087 .
4. *A sharp reentrant two-peak window for delayed unequal Bateman inputs* (2026), published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-reentrant-two-peak-window-for-delayed-unequal-bateman-in--2eb46436a2c9 .
