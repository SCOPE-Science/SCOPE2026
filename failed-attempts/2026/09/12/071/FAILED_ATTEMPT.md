# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Cyclic-prime two-J-class complexity-2 small monoid
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1238
- **Disposition:** AUDIT_1_REJECT
- **Domain:** finite semigroup theory
- **Method:** Green J-structure with Tilson flow obstruction and two-group wreath divisor

## Problem

Let S be a finite monoid with |S| <= 24 having exactly two nonzero regular J-classes (a Tilson small monoid), in which at most one regular J-class has nontrivial maximal subgroups and every maximal subgroup is cyclic of prime order, given by its multiplication table and egg-box data. Does there exist such an S with Krohn-Rhodes complexity exactly 2, hence a non-membership witness showing that the one-group-J-class plus cyclic-group restriction does not force complexity at most 1? A complete answer is either (i) one explicit S with its full Green's J-structure, Schutzenberger groups, and Rees matrix data, plus a certified Tilson-type complexity-1 obstruction proving S does not divide any A wr G wr B with A,B aperiodic, together with an explicit two-group wreath divisor certifying c(S) = 2, or (ii) a proof that no monoid in this scope has complexity 2.

## Attempted claim

Let S be a finite monoid with |S| <= 24 having exactly two nonzero regular J-classes (a Tilson small monoid), in which at most one regular J-class has nontrivial maximal subgroups and every maximal subgroup is cyclic of prime order, given by its multiplication table and egg-box data. Does there exist such an S with Krohn-Rhodes complexity exactly 2, hence a non-membership witness showing that the one-group-J-class plus cyclic-group restriction does not force complexity at most 1? A complete answer is either (i) one explicit S with its full Green's J-structure, Schutzenberger groups, and Rees matrix data, plus a certified Tilson-type complexity-1 obstruction proving S does not divide any A wr G wr B with A,B aperiodic, together with an explicit two-group wreath divisor certifying c(S) = 2, or (ii) a proof that no monoid in this scope has complexity 2.

## Research outcome

Proved no monoid in the admitted cyclic-prime two-J-class scope has KR-complexity 2: at most one group-carrying regular J-class forces depth <= 1 hence complexity <= 1; verified T_2 as an in-scope sharpness witness with c=1.

## Why this attempt failed

Failed axes: originality, value.

originality: The headline (at most one group-carrying regular J-class implies c<=1, hence no in-scope monoid has c=2) is mechanically implied by the strictly stronger 1968 Rhodes Depth/Depth-Decomposition Theorem c(S)<=d(S) found in Eilenberg Vol.B Ch.VII and Rhodes-Steinberg q-theory Ch.4 and restated in the retrieved Margolis-Rhodes-Schilling decidability survey. Substituting depth<=1 for general depth is a one-step parameter instantiation, not a new theorem, boundary, or counterexample. Synonymous terminology (essential J-class = regular J-class with nontrivial subgroup) and the known Tk complexity table (Tk has complexity k-1, hence T2 has complexity 1) cover the strengthened general claim and the sharpness witness respectively. A prior source need not state the headline verbatim; substantive implication suffices, which holds here. value: ADMISSION_DEFECT: the admitted target asked whether a depth<=1 restricted class (|S|<=24, two nonzero regular J-classes, cyclic prime groups) contains complexity 2, but any such S has depth<=1 so the 1968 textbook bound c<=d already forces c<=1 for arbitrary size and arbitrary groups. The negative resolution is therefore a direct textbook instantiation (depth parameter n=1) plus the standard facts c=0 iff aperiodic and c(T2)=1 from the known Tk complexity k-1 table. It is a textbook restatement / mere parameter substitution with no new boundary, classification, witness changing a known boundary, or independently retrievable exact invariant whose value was unknown or non-mechanical. The draft itself notes the scope hypotheses are unneeded. Sharpness via T2 does not add value since c(T2)=1 was already known. Value FAILS even though the literal target alternative (ii) is correctly proved.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The proof cites rather than re-proves the textbook Depth Theorem c<=d and the holonomy/prime-decomposition indexing of group wreath levels by regular J-classes (Eilenberg Vol B; Rhodes-Steinberg q-theory); it does not give a self-contained wreath decomposition. The computation verifies the sharpness witness T_2 only, not an exhaustive enumeration of all monoids of order <=24.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
