# Proof-structure checklist (verification-critical)

Target: Schafhauser Conjecture D (target-only topic, no fallback).

## Claims and their basis
1. UCT case (Thm 2): abstract (kappa,gamma)+(star) => Ell-isomorphism => A≅B.
   - Order-from-traces lemma: uses stable rank one (Rørdam), strict comparison
     (Matui–Sato), Haagerup quasitrace theorem — all UCT-free structural facts.
   - K-theoretic lift converse: Rosenberg–Schochet UCT Cor 7.5 (needs UCT).
   - Classification: Kirchberg–Phillips + Elliott–Gong–Lin–Niu / TWW (needs UCT).
2. Traceless UCT-free (Thm 3): Kirchberg–Phillips only. No traces needed.
3. Realized UCT-free (Thm 4 = Schafhauser Thm 3.2): one-sided unital embedding
   with invertible KK/KL + invertible trace map => isomorphism via Elliott
   intertwining. Ingredients all UCT-free:
   - CETW Thm 2.1 (maps into B^∞ by traces; CPoU).
   - CGSTW Thm 2.2 (trace-kernel lifting criterion via KK).
   - CGSTW Thm 2.5 + Props 2.4/2.6/2.7 (KL secondary invariant).
   - Gabe/Kirchberg reparameterization intertwining + Elliott intertwining.
   - KL (not KK) invariance under approximate unitary equivalence — load-bearing.
4. Gap/minimality: existence half (K-theory -> KK -> homomorphism) is the only
   UCT-dependent step (UCT assumed on domain in GLN/CGSTW). Uniqueness is
   UCT-free. Hence K0-pairing (star) is complete at invariant level (Lemma 1)
   and the minimal correction is joint realizability (R1)/(R2). No explicit
   counterexample claimed (would imply non-UCT nuclear algebra; UCT problem open,
   no known examples — stated as limitation, not theorem).

## What was NOT claimed
- No proof of abstract Conjecture D without UCT and without realization.
- No explicit non-isomorphic pair satisfying abstract hypotheses.
- No claim that (star) is false as invariant compatibility; it is proved sharp.

## Reproduction
- Full self-contained proof sketch in output/DRAFT.md §§2–8.
- Source: Schafhauser arXiv:2408.02745v2, read in full (16pp) via fulltext job
  cab73ebf739d4dadb85cb8e02b153d6a; plus CGSTW 2307.06480 / GLN / CETW / KP /
  EGLN / Rørdam / Matui–Sato / Haagerup / Dadarlat–Winter as named dependencies.
