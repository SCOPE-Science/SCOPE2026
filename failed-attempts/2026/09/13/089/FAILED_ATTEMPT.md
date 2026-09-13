# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Chromatic number of the 1/sqrt(2) 2-sphere orthogonality graph
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1675
- **Disposition:** AUDIT_1_REJECT
- **Domain:** discrete geometry / chromatic number of spheres
- **Method:** finite orthogonality obstruction or explicit 4-colouring

## Problem

Let S in R^3 be the sphere of radius 1/sqrt(2) centred at the origin and G(S) the infinite graph with vertex set S joining distinct x,y iff |x-y| = 1 (equivalently inner product <x,y> = 0). Is chi(G(S)) >= 5? A complete answer either exhibits a finite subset F of S with explicit coordinates and verified pairwise inner products/distances whose unit-distance graph is not 4-colourable (certifiable by a Frankl-Wilson modular-intersection polynomial bound or by exhaustive colouring check), or gives an explicit proper colouring of all of S with 4 colours together with a rigorous proof that no monochromatic pair at distance exactly 1 occurs.

## Attempted claim

Let S in R^3 be the sphere of radius 1/sqrt(2) centred at the origin and G(S) the infinite graph with vertex set S joining distinct x,y iff |x-y| = 1 (equivalently inner product <x,y> = 0). Is chi(G(S)) >= 5? A complete answer either exhibits a finite subset F of S with explicit coordinates and verified pairwise inner products/distances whose unit-distance graph is not 4-colourable (certifiable by a Frankl-Wilson modular-intersection polynomial bound or by exhaustive colouring check), or gives an explicit proper colouring of all of S with 4 colours together with a rigorous proof that no monochromatic pair at distance exactly 1 occurs.

## Research outcome

Disproved chi >= 5 for the 1/sqrt(2) sphere orthogonality graph by an explicit verified proper 4-colouring with full proof.

## Why this attempt failed

Failed axes: originality.

originality: FAIL: headline chi<=4 (hence not chi>=5) for radius-1/sqrt2 orthogonality graph is substantively implied by the known stronger exact value chi=4 for the unit-sphere orthogonality graph (Godsil-Zaks arXiv:1201.0486 Lemma 1.1, whose note states the result was already known before 1988). Radial scaling x->sqrt(2)x is a graph isomorphism preserving orthogonality, so unit-sphere chi=4 implies submitted chi<=4. Detailed recolouring is therefore a recomputation/certificate/repackaging of a known stronger fact, not a new claim. ADMISSION_DEFECT: admission missed this direct prior coverage of the target question.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: The proof establishes chi(G(S)) <= 4 and hence refutes chi >= 5, leaving the exact value in {3,4} (the exhibited triangle gives the lower bound 3) unresolved; the computational script is supporting evidence only and the proof itself is analytic and human-checkable.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
