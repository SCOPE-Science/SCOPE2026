# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** AD-regular Falconer threshold in R^3 via decoupling-to-projection energy transfer
- **Round:** 2026-09-07-first-light-01
- **Lane:** 415
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Harmonic Analysis
- **Method:** decoupling and Orponen-type projection transfer with Frostman-measure energy estimates

## Problem

Can the Falconer distance-positivity threshold in R^3 be lowered inside the Ahlfors-David regular class by a checkable decoupling-to-projection-to-energy inequality chain, and if not, does an explicit thin AD-regular extremal block that route?

## Attempted claim

Let E subset B(0,1) subset R^3 be compact Ahlfors-David s-regular with constant at most 10. If s > 69/40 (= 7/4 - 1/40 = 1.725) then the distance set Delta(E) = {|x-y| : x,y in E} has positive Lebesgue measure, via the explicit chain: (i) l^2 cone-decoupling bound, to (ii) Orponen-type spherical-projection L^2 estimate for the normalized s-Frostman measure on E, to (iii) finiteness of the Mattila-Wolff energy integral.

## Research outcome

Proved an explicit conditional Mattila-Wolff reduction for the AD-regular Falconer chain in R^3 at s=69/40 (hypothesis M_T<=10*T^{-1/20} => |Delta(E)|>=2.0e-6, all constants exact and replayed), with exact tier arithmetic showing the strong/fallback decays need beta=61/40 resp. 81/40 against proved beta_3(7/4) in {7/6,9/8}. Full target and preset fallback both remain unproved (neither claimed); the fallback is additionally diagnosed as unreachable from cited technology (38x-14700x envelope mismatch) without claiming a certified disproof.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Scripts correctly verify PURE ARITHMETIC conditional on the assumed Frostman constant: tail 10/(1-2^{-1/20})=293.5679 in (293,294), I=293.9012, 64*pi^2*I=185644.08, 100*0.04^{69/40}=0.3877, mass>=0.6122, mass^2/L2^2=2.019e-6; sine-isometry constant 1/4 verified by closed form g=r*exp(-r) (1/4 vs 1/16) and odd-extension Plancherel; polar identity, w-formula, and mass^2/||w||^2 step are standard and numerically correct. DECISIVE GAP: Step 1 claims uniformly for every E in B(0,1) AD s-regular (C<=10, s=69/40) that H^s(E)>=2^s/10>=0.3306 because E subset B(x,2), hence sup mu(B(x,r))<=100 r^s (A'=100 exactly). This uses the AD lower bound at radius r=2, outside the admissible range when diam(E)<2. By dilation invariance of AD-regularity (rho*E has same constant C), any AD example yields arbitrarily small-diameter examples with H^s(E)=rho^s*H^s(E0) arbitrarily small, violating the claimed 0.3306 lower bound and the uniform A'=100 bound (for r=diam(E), mu=1 vs 100*r^s<<1). The covering B(x,r) subset B(y,2r) gives mu<=C*(2r)^s/H^s(E), which equals 100 r^s ONLY if H^s(E)>=2^s/10 is already known - circular. The dyadic hypothesis M_T<=10*T^{-1/20} for T>=1 controls only high frequencies and is not shown to imply any H^s lower bound, so nu([0,0.04])<=0.3878 and the uniform |Delta|>=2.0e-6 are unproved as stated. Small-diameter sets also make the conclusion's uniformity suspect without a non-degeneracy hypothesis. Hence the headline conditional is not proved; scripts assume A'=100 and do not check the faulty inference. Minor rounding: 0.6122^2=0.3748 not 0.3758, immaterial. Obstruction tier algebra (beta 61/40, 81/40, dividends, T^{5/3} envelope ratios 38x-14700x) is arithmetically correct but presented honestly as non-implication from known inputs with no certified violator claimed - no overclaim there. originality: Route is EMERGENT_FINDING: it is genuinely link (iii) of the admitted target chain (l2-decoupling -> Orponen projection -> Mattila-Wolff energy), isolated during target work, so not scope evasion; absence from topic.json is not adverse. Assessed under ordinary full standard with no presumption. Nearest substantive prior is the classical Mattila-Wolff L2 criterion (Du et al arXiv:1802.10186 Sec.2 Mattila approach Prop 2.3/Thm 2.2; Wolff/Erdogan theory): summable spherical-average energy int S^2 r^2 dr < inf + finite alpha-energy => distance measure has L2 density => |Delta|>0. Theorem R assumes M_T<=10*T^{-1/20} (i.e. beta>=61/40>3/2, summable) and re-derives the same implication with plugged parameters s=69/40, C_AD=10, rate 1/20, delta=0.04. Proof steps (Frostman upper bound, radial pushforward, sine-isometry, Cauchy-Schwarz) are the textbook mechanism; explicit numbers A'=100 (even if fixed), tail interval, 185645, 0.6122, 2.0e-6 and fractions 61/40, 81/40, 103/120, 9/10, 1/8 are obtained by elementary substitution 3-2*beta and geometric series, mechanically recomputable by any reader of the general theorem in minutes. No prior s…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Proves only the conditional reduction: the dyadic hypothesis M_T<=10*T^{-1/20} for all dyadic T>=1 is assumed, not established; the full target s>69/40 positivity remains open.', 'Does not prove the preset fallback (six-block D-decay) nor refute it: the tier/envelope arithmetic shows it cannot follow from cited beta_3 inputs, but no Frostman-certified violating measure is constructed.', 'Link (iii) proof uses the classical Mattila L^2 route (sine-isometry + Frostman small-ball); links (i) dec…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
