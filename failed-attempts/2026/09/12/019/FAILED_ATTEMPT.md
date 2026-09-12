# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Finite-dimensional rigidity self-test for a new 3-input Bell functional
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1095
- **Disposition:** NO_RESULT
- **Domain:** Quantum Information Theory
- **Method:** sum-of-squares with Gowers-Hatami stability

## Problem

Let W3-RIGID be the explicitly specified 3-input 2-output Bell functional with fixed rational coefficients given in the target sheet, whose claimed finite-dimensional maximum is attained by the two-qubit maximally entangled state with specified Pauli observables. Determine whether every finite-dimensional optimal strategy for W3-RIGID is equivalent to that Pauli realization up to local isometries.

## Attempted claim

The Bell functional W3-RIGID with its fixed coefficients self-tests the claimed two-qubit maximally entangled state and Pauli measurements: its finite-dimensional maximum is uniquely attained up to local isometries and auxiliary degrees of freedom, with an explicit robustness bound.

## Research outcome

CLEAN_EXIT: W3-RIGID target blocked by missing exact functional definition with no auditable alternative; NO_RESULT returned.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The W3-RIGID coefficient matrix and claimed Pauli observable specification were absent from topic.json and inputs/, so no Bell operator, NPA/SOS computation, or uniqueness argument could be instantiated; inventing coefficients would decide a different functional and was refused as scope evasion.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The W3-RIGID coefficient matrix and claimed Pauli observable specification were absent from topic.json and inputs/, so no Bell operator, NPA/SOS computation, or uniqueness argument could be instantiated; inventing coefficients would decide a different functional and was refused as scope evasion.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
