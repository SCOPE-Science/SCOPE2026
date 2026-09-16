# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Small-curvature-ratio uniqueness of the asymptotic cone of an expanding gradient Ricci soliton
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20446
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Geometric Analysis
- **Method:** entropy-monotonicity and cone-splitting analysis

## Problem

Let n>=3. Does there exist epsilon(n)>0 such that the following holds? If (M^n,g,nabla f) is a complete expanding gradient Ricci soliton with finite asymptotic curvature ratio A(g):=limsup_{r_p(x)->+infty} r_p(x)^2 |Rm(g)|(x) < epsilon(n), with no curvature-sign assumption, then its asymptotic cone is unique: for any fixed p in M and any two sequences t_k->+infty, s_k->+infty, the pointed Gromov-Hausdorff limits of (M,t_k^{-2}g,p) and (M,s_k^{-2}g,p) furnished by Chen-Deruelle Theorem 1.2 are isometric as pointed metric cones (equivalently, the cross-section (S_infty,g_{S_infty}) is independent of the blow-down sequence up to isometry).

## Attempted claim

Let n>=3. Does there exist epsilon(n)>0 such that the following holds? If (M^n,g,nabla f) is a complete expanding gradient Ricci soliton with finite asymptotic curvature ratio A(g):=limsup_{r_p(x)->+infty} r_p(x)^2 |Rm(g)|(x) < epsilon(n), with no curvature-sign assumption, then its asymptotic cone is unique: for any fixed p in M and any two sequences t_k->+infty, s_k->+infty, the pointed Gromov-Hausdorff limits of (M,t_k^{-2}g,p) and (M,s_k^{-2}g,p) furnished by Chen-Deruelle Theorem 1.2 are isometric as pointed metric cones (equivalently, the cross-section (S_infty,g_{S_infty}) is independent of the blow-down sequence up to isometry).

## Research outcome

Proved existence of epsilon(n)>0 such that small asymptotic curvature ratio forces a unique expander asymptotic cone: every subsequential Chen-Deruelle blow-down is a flat cone over a constant-curvature-1 link on one fixed diffeomorphism type, hence all mutually isometric.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: proof claims exact Ricci-flat limit and flat cones from small A(g), but scaling is invalid. Expander equation Ric+Hess f+g/2=0 does not pass to a finite limit under g_k=t_k^-2 g because the g/2 term blows up as t_k^2; general limits need not be Ricci-flat. Bryant expanders with cone angle c near 1 have arbitrarily small A(g)>0 yet non-flat asymptotic cones (link round sphere radius c, Einstein constant (n-2)/c^2, sectional curvature 1/c^2), directly refuting Steps 3-5 exact Einstein (4) and flatness (6). Step 7 diffeomorphic-implies-isometric for constant-curvature-1 space forms is also unproved in stated generality. Artifact only checks elementary delta<=0.4 pinching arithmetic.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The argument cites standard black boxes without re-proving them: Chen-Deruelle subsequential cone existence, expander potential asymptotics f ~ -r^2/4 and limit Ricci-flatness, Anderson/Cheeger-Colding/Cheeger-Gromov-Taylor regularity upgrade on annuli, Brendle-Schoen differentiable sphere theorem with Ricci-flow stationarity (or equivalent Einstein pinching rigidity), and Wolf spherical space-form rigidity. The final epsilon(n) is existential (minimum of dimensional thresholds); only the 1/4-p…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
