# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact maximal Sidon subsets of Z_n for n=31-55 by difference-conflict clique search with cyclic-automorphism reduction
- **Round:** 2026-09-07-first-light-01
- **Lane:** 58
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Additive Combinatorics
- **Method:** difference-conflict clique backtracking with cyclic-automorphism reduction and brute-force difference replay

## Problem

Determine exact maximal Sidon size S(n) for each cyclic group Z_n, n=31..55, with one explicit extremal residue set per n and a machine-checkable optimality certificate.

## Attempted claim

Exact table S(n) for all n=31..55 via difference-conflict clique backtracking with reduction under x->u*x+t, each entry accompanied by an extremal Sidon set in residues and a difference-set log proving optimality; includes optimal-vs-Singer gap table (perfect cases n=31,43 as checks).

## Research outcome

Closed certified S(n) census for Z_n n=31..55 by difference-conflict clique backtracking with cyclic-automorphism reduction and independent brute-force replay: S=6 (n=31), 5 (32-34), 6 (35-47), 7 (48-55), with per-n witness, difference/sum logs, Singer-gap table (perfect only at 31; would-be perfect 43 computationally absent), all replayable in seconds.

## Why this attempt failed

Failed axes: originality, value.

originality: Decisive prior Buratti-Stinson arXiv:2007.01908 (2020) definitionally anticipates the entire S(n) table. A (v,k)-MGR (k distinct residues mod v with all ordered differences distinct) is exactly a Sidon k-set in Z_v under DRAFT Definition, so S(n)=max{k: n in MGR(k)}. Their Theorem 2.3 states MGR(6)={31}U{v>=35} and MGR(7)={v>=48} with Table 1 listing ruler for v=31, nonexistence for 32<=v<=34, Lemma 2.1 lift for v>=35, nonexistence for 43<=v<=47, rulers for v=48,49,50 and lift for v>=51. This implies S=6 at 31, S=5 at 32-34, S=6 at 35-47, S=7 at 48-55, matching all 25 candidate entries exactly (auditor recomputed implied S(n) and confirmed 25/25 match). Method is also same: exhaustive backtracking search plus Lemma 2.1 (v>=2L+1) lifting. Candidate witnesses are different representatives of same existence facts (e.g. Buratti-Stinson (31,6) ruler 0,1,4,10,12,17 vs candidate 0,1,3,8,12,18; (48,7) ruler 0,5,7,18,19,22,28 vs candidate 0,1,3,15,20,38,42) and Singer n=31 and cyclic (43,7,1) nonexistence are both already in that table and classical (Singer/Bruck-Ryser). Topic-selection literature check missed this nearest prior. Therefore the numerical census and optimality claims are not new; replay packaging does not create priority. value: Even taken as correct replication, the result is not independently worth finding later under SCOPE bar. It is a strict slice (n=31..55, k=5..7) of the larger published Buratti-Stinson census for all k<=11 (v up to 145+ with infinite-family nonexistence theorems), using the same exhaustive-search-plus-lifting method with no new structural insight, classification, or bound improvement. Gap column is textbook arithmetic (n-1)-k(k-1); Singer discussion (n=31 perfect, n=43 would-be plane order 6) is classical and already noted in prior. One-per-n lex-first witnesses are interchangeable representatives, not a classification (DRAFT disclaims full classification). Providing stdlib replay scripts for already-closed cases is useful reproducibility engineering but not a publishable mathematical contribution; it falls under rejected categories: unexplained enumeration / mere re-parameterization of a closed band, with motivation (Singer-to-exhaustion transition) already covered by prior Table 1. No downstream use, conjecture resolution, or method advance is demonstrated.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Sidon = ordered differences distinct (equiv. sums a<=b distinct per Lemma 1); other weak variants may differ.', 'One witness per n only; no classification of all extremal sets.', 'Band 31..55 only; k=8 (n>=57) not attempted.', 'Machine proof via two Python implementations, not a proof assistant; divisor-reduction lemma proved mathematically but census trusts code (mitigated by independent verifier).', 'Originality: numerical values may exist scattered; claim is the closed replayable certifica…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
