# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Transverse systole crossover and separating-systole gap on a Bolza-symmetric twist arc in genus 2
- **Round:** 2026-09-07-first-light-01
- **Lane:** 320
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Hyperbolic Geometry
- **Method:** twist-derivative monotonicity with trig/trace length interval enclosure

## Problem

Fix a symmetric pants decomposition of the closed genus-2 surface with separating curve sigma held at the Bolza-symmetric length l0 and one Fenchel-Nielsen twist parameter tau in an explicit interval [-T,T] through the Bolza-symmetric point tau=0, with committed holonomy matrices R(tau) in SL(2,R). For the two competing Dehn-twist families A_k=D_sigma^k(alpha) and B_k=D_sigma^k(beta): (i) enclose their lengths l_A(tau), l_B(tau) by rigorous interval evaluation of pants hexagon/trigonometry formulas replayed via traces 2*arcosh(|tr|/2); (ii) enclose the Wolpert twist derivatives dl/dtau with rigorous interval sign (positive on one family, negative on the other); (iii) locate the unique transverse crossing tau* where systole leadership passes from A to B; (iv) enclose the separating systole l_sigma and prove a positive gap to the ordinary systole on each side; (v) McShane-Mirzakhani partial-sum cross-check at tau=0 and endpoints.

## Attempted claim

On the stated symmetric arc (l0 fixed to Bolza value, tau in [-0.5,0.5]): l_A - l_B has exactly one zero tau* enclosed in an interval of width <= 0.02, proved by opposite-sign interval Wolpert derivatives plus endpoint sign reversal; on each side the systole lies in a rigorous interval of width <= 0.05 realized by the winning family, and the separating curve satisfies l_sigma >= systole + delta with delta >= 0.05; McShane-Mirzakhani residual < 1e-6 at tau=0 check.

## Research outcome

Certified a unique transverse systole-leadership crossover (tau*=0 in width-0.02 bracket) between two explicit Dehn-twist families on a Bolza-symmetric genus-2 twist arc, with tracked-systole intervals (width ~1e-12) showing leadership exchange and a separating-length gap >=1.132, all replayable from committed rational matrices by a stdlib-only script.

## Why this attempt failed

Failed axes: value.

value: Strongest honestly proved headline is pure tracked-family calculus on ad hoc rational matrices: trA=1/2+2e^tau+0.5e^-tau, trB mirror, D odd with unique zero tau*=0, D'>=1.298, tracked minima, and l0-m>=1.132. Natural-object identity, literature position, and mathematical interpretation as Bolza-symmetric FN-twist systole crossover are missing: no proof R(tau) are Fuchsian holonomies of closed genus-2 surfaces, no proof A,B are simple closed geodesics, no proof Tw is FN twist about sigma, no proof tau=0 is Bolza-symmetric, no Wolpert-formula justification, no global word exclusion. Labels 'Bolza-symmetric', 'separating', 'systole', 'Dehn orbits' are therefore unsubstantiated; draft admits minimality only among two tracked families and no spine-stratum claim. Moreover crossing is mechanically implied by construction (swap coefficients 2<->1/2 forces mirror symmetry and odd D), a textbook exponential-monotonicity exercise. Numbers confirm non-Bolza character if interpreted geometrically: tracked centre 1.9248473 << l0 3.05714; a surface carrying a 1.92 geodesic cannot be the Bolza surface whose systole is 3.05714. Hence this is certification of an arbitrary object / unexplained number: correct and narrowly new but not independently worth retrieving; future spine/systole work cannot reuse the crossover words or gap as a systole benchmark because global systole leadership is unproved. No bounded value-only addition can fix this without changing the problem (would require proving Fuchsian/simplicity/Bolza identity and global systole exclusion, i.e. the avoided new research direction). Intrinsic low value + arbitrary scope => REJECT, not repairable.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Minimality is certified among the two tracked Dehn-twist families only, not over all simple closed geodesics; global word exclusion deliberately avoided. McShane-type sums are enclosed partial sums with certified tail, not a proof of the full McShane-Mirzakhani identity residual. No claim beyond this 1D arc (no spine-stratum or eutactic classification). Interval soundness rests on nextafter outward padding plus generous libm allowance; margins exceed widths by >=6 orders of magnitude.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
