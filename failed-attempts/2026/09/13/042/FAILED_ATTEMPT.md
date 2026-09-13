# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Critical N^{4/5} Painleve-I correction at gc
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1550
- **Disposition:** AUDIT_1_REJECT
- **Domain:** random matrix theory critical one-matrix model
- **Method:** string equation plus Painleve-I double scaling

## Problem

Let mu_{N,g}(dM) = Z_{N,g}^{-1} exp(-N Tr(M^2/2 + g M^4/4)) dM with V_g(x)=x^2/2+g x^4/4, critical coupling g_c=-1/12 where the one-cut off-critical regularity hypothesis fails, and let m_2^{(0)}(g_c) be the finite planar limit of E[N^{-1} Tr M^2] at g_c known from the genus-zero solution. Prove or disprove: at fixed g=g_c the mean has the critical scaling limit L = lim_{N->infinity} N^{4/5}(E_{mu_{N,g_c}}[N^{-1} Tr M^2]-m_2^{(0)}(g_c)) existing, finite and nonzero, equal to an explicit constant c_* determined by the Painleve-I double-scaling function at zero deformation parameter, and in particular the fixed-g N^{-2} genus-one Schwinger-Dyson expansion does not extend uniformly to g_c. A complete answer proves the 4/5 exponent, existence and explicit value c_* via finite-N Schwinger-Dyson/string equations plus double-scaling asymptotics with normalizations verified, or refutes it by proving a different decay exponent, divergence to infinity, non-existence of the limit, or a different explicit value.

## Attempted claim

Let mu_{N,g}(dM) = Z_{N,g}^{-1} exp(-N Tr(M^2/2 + g M^4/4)) dM with V_g(x)=x^2/2+g x^4/4, critical coupling g_c=-1/12 where the one-cut off-critical regularity hypothesis fails, and let m_2^{(0)}(g_c) be the finite planar limit of E[N^{-1} Tr M^2] at g_c known from the genus-zero solution. Prove or disprove: at fixed g=g_c the mean has the critical scaling limit L = lim_{N->infinity} N^{4/5}(E_{mu_{N,g_c}}[N^{-1} Tr M^2]-m_2^{(0)}(g_c)) existing, finite and nonzero, equal to an explicit constant c_* determined by the Painleve-I double-scaling function at zero deformation parameter, and in particular the fixed-g N^{-2} genus-one Schwinger-Dyson expansion does not extend uniformly to g_c. A complete answer proves the 4/5 exponent, existence and explicit value c_* via finite-N Schwinger-Dyson/string equations plus double-scaling asymptotics with normalizations verified, or refutes it by proving a different decay exponent, divergence to infinity, non-existence of the limit, or a different explicit value.

## Research outcome

Disproved the critical N^{4/5} Painleve-I claim: the fixed-coupling Gibbs measure at g_c=-1/12 does not exist at any N, so the limit cannot exist; exponent also mismatched.

## Why this attempt failed

Failed axes: originality, value.

originality: The headline divergence Z=+inf for negative quartic coupling is elementary calculus and mechanically implied by prior work, not a new theorem. Bender-Moshe-Sarkar 1206.4943 explicitly states the integral representation ceases to exist for negative g and the conventional double-scaling limit is inconsistent because the critical coupling is negative, requiring PT/contour regularization. Hermitian N>1 follows by restriction to scalar matrices M=xI. Planar 4/3 and (1-t)^-2 singularity are standard genus-zero/one formulas. No prior source needed to state gc=-1/12 verbatim: the known stronger fact covers it. value: ADMISSION_DEFECT: the TARGET as stated defines a fixed-g Lebesgue Gibbs measure at gc=-1/12<0 where no finite-N measure exists, so the claimed limit is meaningless at every N. This negative resolution is only vacuity/type-error exposure via the one-line fact int exp(+|g|x^4)=+inf, the exact cheap-defect class STANDARD and TARGET policy exclude from value even when literally false. Admission should have ruled out non-confinement before admitting. Formal N^-6/5 power count is heuristic about no specified regularized model and adds no independently retrievable exact invariant.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The disproof addresses the target exactly as stated for the fixed-coupling Lebesgue Gibbs measure. It does not classify cutoff, contour-deformed, or analytically-continued regularizations of the critical quartic model, nor does it construct the double-scaling limit of any such regularized observable; the N^{-6/5} power count in Section 4 of DRAFT.md is formal supporting evidence, not a theorem about a regularized model.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
