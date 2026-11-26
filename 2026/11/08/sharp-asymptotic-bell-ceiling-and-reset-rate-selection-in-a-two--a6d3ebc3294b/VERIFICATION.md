---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The repaired theorem uses dimensionless time and explicitly fixes the units issue: r_*~Omega^2/(2J) does not imply r_*->0 along arbitrary j->infinity (e.g. Omega=j,J=j^2); with Omega fixed it does. CHSH is taken over nondegenerate projective spin observables. In the occupied subspace, A has energy -j and (B,S) is the block with diagonals -j,j and off-diagonals 1. Expanding B in its two eigenvectors cancels the entire lower-mode error; the remaining upper-mode vector is sin(theta)(exp(-i omega t)-exp(i omega t))/sqrt(2) times its unit eigenvector. Its norm bound yields the stated projector trace-norm bound pointwise and after averaging against any age law. Integration against qe^{-qt} gives the effective 00/11 block; the correlation singular values are 1,|kappa/(1+kappa^2)|,|kappa/(1+kappa^2)|. The Tsirelson operator-norm bound gives the Lipschitz constant 2 sqrt(2). The profile tends to 2 at both ends, so a positive profile gap off a compact neighborhood plus the all-rate bound gives interior attainment by continuity and forces every optimizer to kappa=1 asymptotically (no finite-j uniqueness claimed). The dropped fixed-j statement is correct under the same nondegenerate convention: dephasing leaves T_{yy}=1/[2(1+j^2)] and T_{zz}=(2j^2+1)/[2(1+j^2)]. An independent column-stacked stationary solve in /tmp/opencode/frozen_1_2_3_checks.py confirmed finite examples, e.g. j=40 at q=delta gives 2.235637382686. Read the uploaded check.py but did not execute it.

## originality

PASS

PASS applies to the repaired uniform-in-time approximation of the evolving density projector, robust under age averaging, with global Poisson optimization as its consequence. The pointwise CHSH window, its sqrt(5) peak, and the fixed-j zero-rate limit are directly covered by earlier Resultary findings and are no longer presented as new. The nearest prior finite-rate tensor determines the Bell function and could be used to derive uniform estimates by additional bounds; it does not give the repaired trace-norm theorem or state the all-rate optimizer conclusion. This comparison is based on primary passages and does not assert priority beyond them.

## value

PASS

An explicit time-uniform two-state approximation keeps the correct slow energy gap, avoiding secular phase errors and allowing arbitrarily long or widely distributed ages. Its all-rate consequence rules out better Bell values at escaping reset scales and answers an optimization question not settled by a scaling-family peak. The selected physical scale and its dimensional qualification are usable without claiming newness for the old window or endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
