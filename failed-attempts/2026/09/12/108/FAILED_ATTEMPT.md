# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Ungraded rank-5 categorification with one dual pair
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1347
- **Disposition:** AUDIT_1_REJECT
- **Domain:** fusion categories
- **Method:** fusion-ring enumeration plus pentagon F-symbols and obstruction witnesses

## Problem

Let R range over all rank-5 fusion rings containing exactly one non-self-dual pair plus three self-dual basis elements, with trivial universal grading and not isomorphic to a direct product of lower-rank fusion rings. For each such R, decide: does there exist a complex fusion category C, necessarily with matching duality pairing, such that K(C) is isomorphic to R? A complete answer classifies all fusion-rule tables in this non-self-dual ungraded non-product class and, for each table, either constructs associativity F-symbols solving every pentagon equation or proves no complex categorification exists by an explicit witness evaluated on that table.

## Attempted claim

Let R range over all rank-5 fusion rings containing exactly one non-self-dual pair plus three self-dual basis elements, with trivial universal grading and not isomorphic to a direct product of lower-rank fusion rings. For each such R, decide: does there exist a complex fusion category C, necessarily with matching duality pairing, such that K(C) is isomorphic to R? A complete answer classifies all fusion-rule tables in this non-self-dual ungraded non-product class and, for each table, either constructs associativity F-symbols solving every pentagon equation or proves no complex categorification exists by an explicit witness evaluated on that table.

## Research outcome

Commutative multiplicity-≤2 census of rank-5 one-dual-pair based rings: 7 and 77 tables, grading verdicts, Casimir fake-ring separation, and TY(Z4) identification.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: I independently re-verified the raw computations: all 7 M1 and 77 M2 tables satisfy associativity, unit, duals and the report's own S-symmetry; I reproduced the M1 raw count 18 with an independent 2^20 brute-force einsum TEMPEST; canonical forms are pairwise distinct; M1 embeds in M2; grading verdicts reproduce exactly (graded M2 indices {2,5,9,12,16}); the M2#2 table matches TY(Z4) entrywise with global dimension 8; FPdim collision pairs agree numerically. But three essential inferences fail. (1) The Casimir Lemma is FALSE as stated: A=CxC with basis x0=(1,1), x1=(i,-i), trivial involution and real structure constants (x1^2=-x0) is commutative semisimple, yet its Casimir C=x0^2+x1^2=0 is singular. (2) Its proof step F_{i*}=F_i^T is false, failing on most census tables (e.g. fake table 18 has N[2,1,1]=2 versus N[1,1,2]=0). Hence the det(C)=0 => non-semisimple => no-categorification chain is unproved as presented (the three tables are in fact non-semisimple via the trace-form discriminant and an explicit nilpotent z^2=0, an argument the report does not give). (3) Axiom mismatch: the report's 'Frobenius' (full S_3 symmetry of S[i,j,k]=N[i,j,dual[k]]) is strictly weaker than standard Frobenius reciprocity N_ab^c=N_{abar c}^b; 64 of the 77 tables, including the three 'fake' tables, violate the standard axiom, so they are not fusion/based rings in the literature sense and the 'minimal-rank witnesses that those axioms alone do not imply semisimplicity' framing is false under standard axioms (a cheap Frobenius mismatch, not a subtle semisimplicity phenomenon). M2 completeness over the 3^20 space was also not independently re-enumerated. claim_route EMERGENT_FINDING is genuine target-derived work, but that does not repair correctness. originality: One scope_literature_search call submitted the literal claim, equivalent formulations (rank-5 based/Grothendieck rings, one dual pair, TY(Z4), universal grading, multiplicity <=2), and dominance queries (exhaustive rank-5 censuses, classifications, databases), fused across SerpBase/Serpent/OpenAlex/Crossref/OpenAIRE (20 results), followed by full-text fetching of Vercleyen-Slingerland arXiv:2205.15637, Alekseyev-Bruns-Dong-Palcoux arXiv:2507.07023, and the Liu-Palcoux-Ren multiplicity-one classification. The standard-axiom substance of the claim is covered by stronger prior work: Vercleyen-Slingerland exhaustively enumerated ALL fusion rings through rank 9 (rank-5 totals: 4 multiplicity-free, 17 at multiplicity 2), Liu-Palcoux-Ren classified multiplicity-one Grothendieck rings to rank 6, Alekseyev et al. classified integral Grothendieck rings to rank 5 (including the TY-type case), and the AnyonWiki/FusionRings.wl database tabulates these rings; I computed that exactly 13 of the 77 tables satisfy standard Frobenius reciprocity, i.e. the genuine fusion-ring subset is database-covered recomputation, and TY(Z4) is classical. The 7/77 counts are new only as numbers for a nonstandard weakened-Frobenius…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Commutative slice only: noncommutative based rings with this duality type were not enumerated. Multiplicity bound 2 only: the M=3 search timed out with 147 partial tables and no multiplicity cap is proved. Categorification verdicts cover only TY(Z4) (by a cited known construction, not reproved) and the three singular-Casimir tables (by the proved lemma); remaining genuine rings carry computed data but no per-table pentagon or obstruction verdict. Possible overlap with published rank-5 classific…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
