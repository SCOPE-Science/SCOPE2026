# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact rational neighborhoods beyond the endomorphism-ring bound
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20075
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Number Theory
- **Method:** isogeny graph and modular polynomial techniques

## Problem

Let p>3 be prime, let ell != p be prime with ell not dividing 2q_j, and let E/F_p be supersingular with j=j(E) not in {0,1728}. Write O=End_{overline{F}_p}(E) as an explicit Ibukiyama order O(q_j) or O'(q_j), with q_j minimal. For every geometric target j' in overline{F}_p, determine explicitly r_{E,ell}(j') = #{C subset E[ell]: C is Frobenius-stable and j(E/C)=j'} and s_{E,ell}(j') = mult_{Y=j'} Phi_ell(j,Y), including loops and collisions of distinct ell-isogenies, in terms of O(q_j) or O'(q_j) and modular-/Hilbert-class-polynomial data, with no assumption p>q_j ell^2 or p>4q_j ell^2. Equivalently, give necessary and sufficient arithmetic conditions for every fiber of the norm-ell ideal-to-target map, together with the Frobenius action on those fibers; in particular, determine r_{E,ell}(j') for rational targets and the exact factorization of Phi_ell(j,Y) over F_p.

## Attempted claim

Let p>3 be prime, let ell != p be prime with ell not dividing 2q_j, and let E/F_p be supersingular with j=j(E) not in {0,1728}. Write O=End_{overline{F}_p}(E) as an explicit Ibukiyama order O(q_j) or O'(q_j), with q_j minimal. For every geometric target j' in overline{F}_p, determine explicitly r_{E,ell}(j') = #{C subset E[ell]: C is Frobenius-stable and j(E/C)=j'} and s_{E,ell}(j') = mult_{Y=j'} Phi_ell(j,Y), including loops and collisions of distinct ell-isogenies, in terms of O(q_j) or O'(q_j) and modular-/Hilbert-class-polynomial data, with no assumption p>q_j ell^2 or p>4q_j ell^2. Equivalently, give necessary and sufficient arithmetic conditions for every fiber of the norm-ell ideal-to-target map, together with the Frobenius action on those fibers; in particular, determine r_{E,ell}(j') for rational targets and the exact factorization of Phi_ell(j,Y) over F_p.

## Research outcome

Proved exact rational ell-neighborhoods via quaternion ideal fibers with no endomorphism-ring size bound, certified by a bound-violating example.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: TARGET route: reran example_check.py confirming N=14 trace 0 j=5, bound fails, 0 rational 3-kernels matching 1+(-13/3), 4 distinct geometric kernels. General trace-0, M2 splitting for ell not dividing 2q, ell+1 ideal/subgroup counts, and total 1+(-p/ell) for odd ell are correct. Essential factorization inference FAILS: Fp-roots of Phi_ell(j,Y) equated with r(j')>0 via claimed j(E/C) in Fp iff C stable, which is false under collisions where Frobenius permutes a fiber without fixing a kernel yet fixes j'. Deductive proof therefore does not establish bullet 4; example only certifies one collision-free case. originality: TARGET headline dictionary, fiber-size equality, and Frobenius fixed-point count are substantively covered by prior Deuring correspondence and Li-Ouyang-Xu Thm2.4 plus Thm1.1. Ideal-isogeny bijection, right-order conjugacy target criterion, M2(Fell) ell+1 count, and 1+(-p/ell) Fp-count are all previously recorded; removing p>q ell^2 by finite enumeration is a direct corollary, not a new arithmetic condition. Prior need not state unbounded headline verbatim to imply it. value: TARGET proof would still need independent value. As stated the result is a textbook restatement of Deuring plus linear algebra with enumeration replacing the prior closed-form loop analysis, giving no new boundary, classification, benchmark, or downstream use. Single tiny p=13 ell=3 illustration with zero rational kernels is a routine eigenvalue check, not an exact invariant of a pre-motivated natural object that future work would retrieve.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Excludes j=0,1728 and ell dividing 2*q_j as stated in the target. Uses Deuring/Tate/Ibukiyama theory as black boxes; novelty is removing the size bound by full fiber enumeration. Computation certifies one bound-violating example; the general theorem is deductive.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
