# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp Bergman-Sobolev threshold on the smooth worm
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1497
- **Disposition:** NO_RESULT
- **Domain:** several complex variables
- **Method:** Barrett scaling model asymptotics

## Problem

Let W_beta in C^2, beta>pi/2, be the standard smoothly bounded rotation-symmetric Diederich-Fornaess worm domain with total winding 2*beta and fixed smooth cutoff, and let P_beta be its Bergman projection. Let c(beta)=pi/(2*beta). Prove or disprove: P_beta extends to a bounded operator H^s(W_beta)->H^s(W_beta) if and only if s<c(beta), for the full range beta>pi/2 and s>=0, where H^s is the L^2-Sobolev space. A complete answer proves boundedness for every s<c(beta) with a beta,s-dependent bound and exhibits, for every s>=c(beta), an explicit function in H^s whose Bergman projection is not in H^s, or refutes the stated if-and-only-if by establishing either boundedness at some s>=c(beta) or failure at some s<c(beta) with a rigorous witness.

## Attempted claim

Let W_beta in C^2, beta>pi/2, be the standard smoothly bounded rotation-symmetric Diederich-Fornaess worm domain with total winding 2*beta and fixed smooth cutoff, and let P_beta be its Bergman projection. Let c(beta)=pi/(2*beta). Prove or disprove: P_beta extends to a bounded operator H^s(W_beta)->H^s(W_beta) if and only if s<c(beta), for the full range beta>pi/2 and s>=0, where H^s is the L^2-Sobolev space. A complete answer proves boundedness for every s<c(beta) with a beta,s-dependent bound and exhibits, for every s>=c(beta), an explicit function in H^s whose Bergman projection is not in H^s, or refutes the stated if-and-only-if by establishing either boundedness at some s>=c(beta) or failure at some s<c(beta) with a rigorous witness.

## Research outcome

Target blocked: stated sharp constant pi/(2beta) is misaligned with the Barrett flat-length model prediction and the cutoff geometry is underspecified, while boundedness for all s<c needs deep worm-specific estimates; no Audit-ready alternative exists, so clean exit with notes preserved.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The lane could not close either half of the iff: the Barrett failure route yields a model exponent tied to the unspecified flat cutoff length rather than the stated total-winding constant, the positive boundedness half needs literature-scale weighted dbar-Neumann theory, and the endpoint needs borderline analysis. Working notes and the bounded gap computation are preserved in output/WORKLOG.md and output/artifacts/ for future work once the cutoff geometry is pinned down.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The lane could not close either half of the iff: the Barrett failure route yields a model exponent tied to the unspecified flat cutoff length rather than the stated total-winding constant, the positive boundedness half needs literature-scale weighted dbar-Neumann theory, and the endpoint needs borderline analysis. Working notes and the bounded gap computation are preserved in output/WORKLOG.md and output/artifacts/ for future work once the cutoff geometry is pinned down.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
