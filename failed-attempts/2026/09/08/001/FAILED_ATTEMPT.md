# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Weak-Lefschetz defect census for Artinian monomial quotients QQ[x,y,z]/I of socle degree 5-6 with Hilbert table and Hessian rank-drop witnesses
- **Round:** 2026-09-07-first-light-01
- **Lane:** 52
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Commutative Algebra
- **Method:** exact monomial-basis linear algebra with Hessian-rank certification and independent rational-arithmetic replay

## Problem

For A=QQ[x,y,z]/I with I monomial Artinian of socle degree 5 or 6 (i.e. QQ-basis of monomials outside I has max degree 5 resp. 6 and x^a,y^b,z^c in I for some a,b,c): enumerate representatives of each divisor-poset stratum (divisibility poset of minimal monomial generators up to permuting variables), and for each representative compute by exact monomial-basis counting the Hilbert function HF(A)=(h0,...,h5/6) and, for ell=x+y+z, the exact QQ-rank of each multiplication map x ell: A_d -> A_{d+1} versus maximal rank min(h_d,h_{d+1}). For every stratum where rank is non-maximal at some d, produce one explicit Hessian (Macaulay-dual) matrix witness whose evaluated minor/determinant certifies the drop, plus a rational-arithmetic replay log (ideals, bases, matrices, ranks, minor values) checkable in any CAS.

## Attempted claim

Complete the divisor-poset-stratified census for socle degree 5-6: a table listing for each representative ideal I (monomial generators), its Hilbert function vector, the rank profile of ell=x+y+z across all degrees, and for each WLP-failing stratum at least one explicit Hessian matrix with evaluated minor/determinant proving non-maximal rank (e.g. a 2x2 or larger minor vanishing where maximal rank requires nonvanishing, with exact rational value). Success is a finite checkable defect table plus replay script; any new failing Hilbert vector with witness is a publishable note/counterexample section.

## Research outcome

Complete exact S3-orbit WLP census for 5-generated monomial box F (3<=a,b,c<=5, deg 2-4) with socle 5-6: 579 orbits (3246 perms), 573 pass for ell=x+y+z, 6 fail generically (socle 6, square det 0, rank n-1, parametric det(a,b,c)==0, second-ell fail) with Macaulay-dual contraction witnesses; plus 4-generated box lemma (56 orbits, 0 fails). Replay in ~1s via stdlib+sympy.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Independent replay confirms the 6 rank-drop witnesses: verify_wlp.py passes in ~1.1s (Fraction + sympy ranks agree), socle/HF correct, square dets 0 with nonzero (n-1)-minors, 1-dim kernel/cokernel, parametric det(a,b,c)==0 and second-ell (1,2,3) failure for all 6; admissible tuples 6975 and raw-tuple counts 3246/579 reproduce. BUT census as described (minimal ideals / S3-orbits of minimal ideals, divisor-poset strata, Hessian witnesses) is not what was computed: (a) census_check keys canon on raw gens without minimal reduction, so 579 = raw 5-tuple S3-orbits, not minimal-ideal orbits. Recomputation: 265/579 orbit reps contain a redundant generator (e.g. [z^2,z^3,...]), distinct minimal ideals among reps only 408, S3-orbits of minimal ideals only 391 (314x5-gen +72x4-gen +5x3-gen), distinct minimal ideals socle 5-6 arising 2159, raw tuples 3246 include 1476 non-minimal. Claim 'reduce to minimal, keep distinct ideals, 579 orbits' is therefore false as stated. (b) 4-generated lemma miscounts the same way: 239 = tuples with socle 5-6, not distinct ideals (192 distinct ideals); 56 = tuple-orbits, not ideal-orbits (45 ideal-orbits: 33 socle-6 +12 socle-5; 4-minimal-only subset 42 orbits). Zero-failure part replays (0 fails), but counts as stated are wrong. (c) 'Hessian/Macaulay-dual witness H=M^T' is just the transpose of the multiplication matrix, so det(H)=0 is tautologically equivalent to det(M)=0; it is not a Hessian in the sense of Almeida et al. higher Jacobians/Hessians or Togliatti Laplace theory, and all cases are non-level type 2-4 where the classical Gorenstein Hessian criterion does not apply. (d) Divisor-poset stratification collapses by authors' own admission (all 5-minimal sets are antichains); S3-canonical tuple used instead, contrary to topic audit plan. Core rank facts are correct; census-completeness/terminology claims are not. originality: Nearest priors substantively cover the mechanisms; delta is an arbitrary finite box, not a new stratum or theorem. Cook-Nagel 0909.3509/1105.6062 (level monomial ACI have WLP, lozenge correspondence) already implies failing examples must be non-ACI non-level as here; Altafi-Boij 1807.02138 classifies sharp HF bounds and Z/d-invariant equigenerated failures; Altafi-Lundqvist 2306.03188 classifies forcing numbers; Michalek-Miro-Roig 1310.2529 and Miro-Roig-Salat 1710.03579 / Mezzetti-Miro-Roig classify smooth minimal monomial Togliatti systems (minimal mu=2n+1=5 in 3 vars) including the cubic (x^3,y^3,z^3,xyz) analogue the draft cites. F1,F2,F4 are trivial early-socle zero-column failures (socle z^2 in degree 2 kills M_2 column parametrically) — textbook linear algebra, explicitly acknowledged as trivial. F3 is a 5x5 pigeonhole collision of two degree-2 classes onto one degree-3 class. Only F5/F6 are Laplace-type without low socle, and F6 (5-generated degree-4 equigenerated, mu=5 minimal) sits exactly in the classified minimal-Togliatti range; draft expressly disclaims novelty of indi…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Box-restricted (not all socle 5-6 monomial ideals); S3-orbits refine abstract divisor-poset antichains (all 5-minimal are antichains); census ell fixed to x+y+z with per-fail genericity proof, passes need no genericity; small failing ideals may overlap known examples — novelty claimed only for closed-box table with genericity certificates; completeness outside box unknown.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
