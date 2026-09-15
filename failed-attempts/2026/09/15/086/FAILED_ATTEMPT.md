# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Two-sided Kazhdan-Lusztig/Soergel character multiplicity formula for affine Hecke algebra of type G2 at q^2=-1
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20301
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Representation Theory
- **Method:** Kazhdan-Lusztig combinatorics and Soergel bimodule analysis

## Problem

Let H be the extended affine Hecke algebra of type G2 over C with equal parameter q where q^2=-1. For t in T=Hom(X-lattice torus) let M(t) be the principal series module with central character W0-orbit W0 t, and let L run over finite-dimensional simples. For every central character (Davis G2 representatives), determine the exact finite composition multiplicities [M(t):L] and formal weight characters ch(L)=sum dim L^{gen} and prove they are given by an explicit closed formula in terms of (p-)Kazhdan-Lusztig polynomials / indecomposable Soergel-bimodule characters for affine Weyl group of type G2, constant on two-sided cells, recovering Davis's q^4=1 dimension vectors (e.g. 1,2,2 at t_{1,-1} and 1,1,2,3,3 merger) as values at 1.

## Attempted claim

Let H be the extended affine Hecke algebra of type G2 over C with equal parameter q where q^2=-1. For t in T=Hom(X-lattice torus) let M(t) be the principal series module with central character W0-orbit W0 t, and let L run over finite-dimensional simples. For every central character (Davis G2 representatives), determine the exact finite composition multiplicities [M(t):L] and formal weight characters ch(L)=sum dim L^{gen} and prove they are given by an explicit closed formula in terms of (p-)Kazhdan-Lusztig polynomials / indecomposable Soergel-bimodule characters for affine Weyl group of type G2, constant on two-sided cells, recovering Davis's q^4=1 dimension vectors (e.g. 1,2,2 at t_{1,-1} and 1,1,2,3,3 merger) as values at 1.

## Research outcome

Resonant-simplicity obstruction at q^2=-1 for G2 principal series with exact engine and certified KL data.

## Why this attempt failed

Failed axes: originality, value.

originality: Davis arXiv:1104.4826 (J. Algebra 2012), inspected in full text, already classifies crystallographic rank-two affine Hecke algebras at all q including G2. Under the standard parameter translation q_sub=q_D^2, the submission's q_s^2=-1 is Davis's q^8=1 column, whose G2 table rows read t1,1=12 and t1,-1=12 (simple), t1,q2-type distinct irreps 1,1,2,3,3 (M(t) composition 1,1,2,2,3,3 with the 2-dimensional factor doubled), and t1,+-q 6,6 — exactly the submitted numbers. Kato's criterion (Davis Thm 3c) implies the (1,1) simplicity and the orbit theorem (Thm 3a) makes (-1,1) redundant. The exact-integral engine, mod-17 Burnside certificates, and KL tables are new verification technology, but per the shared STANDARD certification and recomputation do not create originality. Prior work substantively implies the headline. value: No new theorem, boundary, or counterexample results: every headline number is already in Davis's classification, and the claimed 'obstruction' refutes only a misdefined +-1 resonance test while the true reducibility locus P(t) (values +-i) is empty at exactly these points, so the uniform-formula program is not actually blocked. An exact invariant of a natural object can pass value when unknown, but here the values are known. The engine and certified KL dataset are reusable infrastructure, yet the STANDARD states certification strengthens but does not create value. This is a known-classification recomputation with certificates: independently correct, but not worth retrieving as a new record.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Proved: engine relations, center scalarity, generic simplicity, KL polynomiality and degree bounds, and resonant simplicity at (1,1),(1,-1),(-1,1) by the two-method certificate. Computed evidence only: exact dimension vectors [1,1,2,2,3,3] and [6,6] (algorithm outputs cross-checked mod 17, without full block simplicity proofs), mod-17 image dims 81/108/46 as invariants, and cell-constancy of any future multiplicity formula. The full closed (p-)KL/Soergel formula for every central character with…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
