# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Genus-0 degree-12 Belyi passport (4-3-2-2-1, 5-3-2-1-1, 4-3-3-2)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1889
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** Belyi maps / dessins / Hurwitz existence
- **Method:** S12 transitive-triple census plus primitivity/parity and braid orbit

## Problem

Decide the realizability of the genus-zero degree-12 Belyi passport P3 = ([4,3,2,2,1], [5,3,2,1,1], [4,3,3,2]) over {0,1,infinity}: does there exist a connected cover f: P^1_C -> P^1_C of degree 12 branched only over 0,1,infinity with exactly these ramification partitions, satisfying Riemann-Hurwitz with 5+5+4=14 parts? A complete answer is either an explicit transitive triple (u0,u1,uinf) in S12 with the stated cycle types, u0*u1*uinf=1, generating a transitive subgroup K identified up to conjugacy including primitivity/imprimitivity and parity (inside A12 or not), together with its braid-orbit size and an explicit field of definition with model, or a rigorous proof of non-existence identifying the failing condition (combinatorial triple count, transitivity, primitivity, or field-of-moduli obstruction). Scope is fixed to degree 12, genus 0, three branch points.

## Attempted claim

Decide the realizability of the genus-zero degree-12 Belyi passport P3 = ([4,3,2,2,1], [5,3,2,1,1], [4,3,3,2]) over {0,1,infinity}: does there exist a connected cover f: P^1_C -> P^1_C of degree 12 branched only over 0,1,infinity with exactly these ramification partitions, satisfying Riemann-Hurwitz with 5+5+4=14 parts? A complete answer is either an explicit transitive triple (u0,u1,uinf) in S12 with the stated cycle types, u0*u1*uinf=1, generating a transitive subgroup K identified up to conjugacy including primitivity/imprimitivity and parity (inside A12 or not), together with its braid-orbit size and an explicit field of definition with model, or a rigorous proof of non-existence identifying the failing condition (combinatorial triple count, transitivity, primitivity, or field-of-moduli obstruction). Scope is fixed to degree 12, genus 0, three branch points.

## Research outcome

Genus-0 degree-12 passport P3 proved realizable via explicit S12 triple; repaired census 111680/88608 with 1277/923 classes, per-triple pure-braid orbit 1, full-B3 orbit 6, Q-field proved; no exact polynomial coefficients claimed.

## Why this attempt failed

Failed axes: correctness.

correctness: Core triple reproduces: cycle types (4,3,2,2,1)/(5,3,2,1,1)/(4,3,3,2), product identity under stated left action, transitivity (orbit 12), centralizer order 1, signs -1/-1/+1, Riemann-Hurwitz (14 parts, defect 22), and sympy group order 12! transitive primitive were independently re-run. But the headline as stated is not fully established: (a) the primitivity word certificate as written is false under the stated composition convention, since U0^2∘U1 sends 0 to 10, not 0 (a fixing pair exists only in path-application order, confirmed by BFS pair AAB/aBBB); (b) defined-over-Q is inferred from a singleton pure-braid orbit among 923 transitive classes plus trivial Aut, which does not imply field of moduli Q since Galois can permute singleton orbits, so Q-definition is unproved and no model is exhibited; (c) census counts (111680/88608/1277/923) cannot be reproduced because censusA/B and braid scripts are absent from inputs/artifacts, with only rate-level sampling support.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: An exact Q-polynomial model (coefficients of f=cP/Q) was not recovered: a bounded multi-ansatz numerical program plateaued at residual F~1e-9 with degenerate fiber collisions, so the report proves existence of the Q-model via the per-triple rigidity criterion rather than exhibiting coefficients; no numerical vector is claimed as the model. The prior draft's superseded global-count, global-rigidity, and centralizer-denominator statements are withdrawn and replaced as documented in output/DRAFT.m…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
