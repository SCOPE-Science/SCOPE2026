# Independent mathematical audit

## correctness

PASS

Reconstructed the Gaussian covariance loss on the closed ordered triangle, including coincident sites and endpoints: K+ηI is positive definite for every allowed pair. An independent SymPy certificate integrates k(t,x)k(t,y) on the three ordered intervals, computes the inverse two-by-two covariance formula, and verifies the gap-comparison and derivative identities with exact coefficients (python3 /workspace/evidence/bridge_certificate_replay.py, BRIDGE_REPLAY_OK; SymPy 1.14.0). For b≤1/2 and fixed u=(x+y−1)², the bracket multiplying u in the centered difference decreases in u and is strictly positive even at u=(1−b)², by the displayed endpoint coefficients and η>0; the prefactor is positive. For b≥1/2 the scaled difference from the centered gap 1/2 is a concave quadratic in u, nonnegative at the centered endpoint and strictly positive at the boundary endpoint. The centered endpoint is strict for b>1/2 by its η³ coefficient. These comparisons cover boundaries as well as the interior. After the rational change of variable on (0,1/3), the five intermediate coefficient polynomials have one positive noise zero each in the five reported disjoint intervals, in decreasing order of index. Thus after ignoring any zero coefficients there is one sign variation for every η>0. Together with the signs at b=0 and b=1/3, this gives one root and the derivative changes from negative to positive. The upper-interval transform verifies H<0 up to b=1, so no further minimum occurs there. At fixed b the quadratic coefficient in η turns negative below 1/4 and the linear one above 1/4; the constant is positive and the leading coefficient negative, giving exactly one positive η-zero. Interior uniqueness and compactness of the closed gap interval yield continuity; uniqueness for fixed b makes the continuous root curve injective. The simple roots in the small-noise and inverse-noise rescalings give the stated limits and local expansions, hence the direction is strictly decreasing. Independent calculations are exact sign/identity checks, not numerical evidence for a continuous optimum.

## originality

PASS

Pass for the unrestricted global result over all pairs. There is material overlap with a same-day indexed symmetric-design theorem for the same loss, including the unique optimal symmetric spacing and the two spacing asymptotics. Those features are not counted on their own as distinct. Neither that theorem nor the other strongest inspected statements establishes that every asymmetric design loses to the global symmetric optimizer or that this is the unique optimum over the closed two-site domain.

## value

PASS

The unrestricted comparison removes a substantive design constraint, including ruling out repeated readings and endpoint sacrifices as optima at every finite noise level. It answers whether asymmetric sites could improve a practically natural two-reading path recovery benchmark; center reflection by itself is insufficient. The calibrated spacing and collision law describe the verified unconstrained optimum, not merely an optimum within a symmetry ansatz. The scope is exactly this bridge and independent equal noise, not a general GP placement rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
