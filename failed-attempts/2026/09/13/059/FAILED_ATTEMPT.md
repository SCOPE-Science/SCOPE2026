# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** RSW persistence across symmetric Lip=1 s-embeddings
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1594
- **Disposition:** AUDIT_1_REJECT
- **Domain:** statistical mechanics / s-embeddings
- **Method:** symmetric folding construction and RSW gluing

## Problem

Consider critical FK-Ising on periodic centrally-symmetric s-embeddings with uniformly bounded edge lengths and angles and periodic origami map of zero mean drift, allowing asymptotic origami Lipschitz constant exactly 1 via symmetric local folding (no global Lorentz drift), satisfying otherwise the non-degeneracy of Mahfouf Thm 1.1 which assumes Lipschitz<=1-c. For topological quads of uniformly bounded extremal length let p denote critical FK-open crossing probabilities. Prove or disprove that uniform RSW bounds 0<c_-<=p<=c_+<1 persist across this whole symmetric Lip=1 subclass with c_-,c_+ depending only on the extremal-length bound and non-degeneracy. A complete answer either proves the uniform bounds for the subclass, or constructs an explicit symmetric Lip=1 embedding and quad sequence with crossings degenerating to 0 or 1.

## Attempted claim

Consider critical FK-Ising on periodic centrally-symmetric s-embeddings with uniformly bounded edge lengths and angles and periodic origami map of zero mean drift, allowing asymptotic origami Lipschitz constant exactly 1 via symmetric local folding (no global Lorentz drift), satisfying otherwise the non-degeneracy of Mahfouf Thm 1.1 which assumes Lipschitz<=1-c. For topological quads of uniformly bounded extremal length let p denote critical FK-open crossing probabilities. Prove or disprove that uniform RSW bounds 0<c_-<=p<=c_+<1 persist across this whole symmetric Lip=1 subclass with c_-,c_+ depending only on the extremal-length bound and non-degeneracy. A complete answer either proves the uniform bounds for the subclass, or constructs an explicit symmetric Lip=1 embedding and quad sequence with crossings degenerating to 0 or 1.

## Research outcome

Proved uniform RSW persists across the symmetric Lip=1 subclass: crossing bounds depend only on modulus bound and non-degeneracy, resolving the target dichotomy positively.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: ADMISSION_DEFECT: periodic bounded origami cannot have asymptotic Lip=1 under draft's own limsup definition, so Lip=1 qualifier is empty; local vs large-scale Lip confused. Lemma 3 base RSW relentlessly imported (DHN square-only, Tassion conditional) without proving uniform square-crossing over varying weights in C(Q); O-independence does not imply RSW. Non-vacuity toy has bounded periodic O hence asymptotic Lip 0, not 1. Duality upper bound and quasi-isometry uniformity hand-waved. Toy uses placeholder c_rect=0.1, proves nothing. originality: Headline uniform RSW over periodic symmetric elliptic class is substantively implied by stronger prior: any periodic bounded-O model satisfies Mahfouf Lip(kappa,delta) with delta=Osc/kappa plus Exp-Fat-type nondegeneracy, hence Mahfouf Thms 1.1-1.2 and Chelkak doubly-periodic Flat case already give the claimed uniform bounds. The only purported novelty (genuine asymptotic Lip=1) has no witness; draft is corollary/repackaging with misattributed black boxes, not a new boundary. value: No independently retrievable new fact: what is actually shown is square-lattice ellipticity plus placeholder gluing arithmetic, restating known periodic RSW as a Lip=1 extension without exhibiting any genuine asymptotic Lip=1 model. Vacuous/illusory parameter extension, unexplained toy enumeration with arbitrary c_rect=0.1 and astronomically small crude bounds, and no sharp constants, classification, or downstream use. ADMISSION_DEFECT vacuity noted above.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Restricted to periodic bounded-period centrally-symmetric zero-drift subclass with fixed non-degeneracy tuple Q; unbounded-period, non-periodic, asymmetric, or Lorentz-drifted Lip=1 embeddings are outside the claim. Base-scale RSW input and FKG/duality/finite-energy tools are imported as standard black boxes rather than re-proved. Constants are uniform but not sharp; quad modulus is continuum extremal length transferred via uniform quasi-isometry.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
