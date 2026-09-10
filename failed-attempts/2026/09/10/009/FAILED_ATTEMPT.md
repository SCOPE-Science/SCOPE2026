# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Borel-versus-Baire edge-coloring gap on an aperiodic fiber-pattern ladder over the dyadic odometer
- **Round:** 2026-09-07-first-light-01
- **Lane:** 509
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Descriptive Set Theory
- **Method:** Borel toast decomposition with fiber-phase propagation and link-constraint certification, contrasted with Baire-generic LOCAL edge-coloring rules

## Problem

Decide Borel 3-edge-colorability of one explicit 3-regular bipartite hyperfinite Borel graph H0: a fiber-pattern ladder over the dyadic odometer whose within-fiber C6 pattern varies aperiodically. Either exhibit a toast-layered Borel proper 3-edge-coloring with layer log (collapse), or prove no Borel 3-edge-coloring exists via a finite phase-obstruction while exhibiting a Baire-measurable 3-edge-coloring on a comeager invariant set (Borel-versus-Baire edge gap).

## Attempted claim

Let X=2^N, T:X->X the dyadic odometer (binary add-one with carry, all-ones maps to all-zeros), k(x)=(least n with x(n)=1) mod 3 with k(all-zeros)=0, Y=Xx{0,1,2}x{0,1}. Let H0 have within-fiber edges ((x,i,0),(x,i+k(x)+t,1)) mod 3 for t in {0,1}, plus link edges ((x,i,0),(T(x),i,1)) for all x,i. H0 is Borel, 3-regular, bipartite by side, hyperfinite, with 6-cycle fibers. Decide with logs exactly one of: (i) an explicit toast-layered Borel proper 3-edge-coloring of H0 with layer/diameter log; or (ii) a finite fiber-phase obstruction (explicit incompatible block family plus propagation lemma) proving no Borel proper 3-edge-coloring exists, together with an explicit Baire-measurable proper 3-edge-coloring on a comeager T-invariant set, hence a Borel-versus-Baire edge gap.

## Research outcome

Decided Borel 3-edge-colorability of H0 on the collapse side: explicit k-relative Borel 3-edge-coloring (links 0, fiber offsets t=0/1 -> 2/1) is proper at every vertex for every fiber pattern, with exact value chi'_Borel(H0)=3 and a compatible toast layer/diameter log; machine replay confirms all finite checks.

## Why this attempt failed

Failed axes: value.

value: FAIL: textbook instantiation with mechanically implied invariant. H0 is defined as the edge-disjoint union of three Borel perfect matchings spelled out in its definition: links ((x,i,0),(T(x),i,1)), fiber t=0 ((x,i,0),(x,i+k(x),1)), fiber t=1 ((x,i,0),(x,i+k(x)+1,1)). DRAFT proves each vertex sees exactly one edge of each type, i.e. each type is a Borel 1-factor. The lemma 'a Borel graph edge-partitioned into Delta Borel matchings has chi'_Borel<=Delta' is immediate; coloring by type (0,2,1) just reads the definition. Aperiodicity of k(x) is no obstruction because the rule colors by the definitional offset t=j-i-k(x). No toast layering, phase analysis, or Baire-LOCAL work is needed; interfaces are identity because the global rule is already consistent, and DRAFT Sec.7 admits the scaffold 'is a verification layer over a globally consistent rule, not a general toast-construction method' with no claim beyond aligned links. The cited Delta+1 bounds (Bowen-Weilacher, Csoka) giving 4 are therefore irrelevant: the exact value 3 is baked into the construction, not an open 3-vs-4 cell decided by investigation. Odometer/C6 trappings do not make the invariant non-mechanical; a future researcher sees the 3-coloring directly from the defining edge partition without retrieving the certificate. No reusable bridge, dichotomy entry, or benchmark use survives because any graph defined as 3 explicit Borel matchings is identically class-1. This is a textbook restatement / mere instantiation even though correct and new. Intrinsic low value; no bounded addition (motivation paragraph, literature position) can supply the missing substantive content without changing the problem, so not repairable.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Collapse exploits aligned-link rigidity of H0; no claim for twisted-link ladders, higher-degree fibers, or non-amenable bases. Toast scaffold verifies a globally consistent rule (identity interfaces), not a general toast-construction method. Computation replays truncated models + exact fiber combinatorics; infinite diameter/hyperfiniteness are proofs.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
