# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Separating Av(1234,1342) from Av(4231,4123) by minimized insertion-encoding census to n=14 with two-method certificate
- **Round:** 2026-09-07-first-light-01
- **Lane:** 22
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Combinatorics
- **Method:** generating-tree insertion encoding with finite-automaton minimization and exact counting certificates

## Problem

Let A=Av(1234,1342) (OEIS A165543, algebraic) and B=Av(4231,4123) symmetric to Av(1324,3214) (OEIS A165542, no closed form). Both are symmetry-distinct types among the 56 pair types for length-4 patterns. Prove they are Wilf-distinct by exact enumeration: |A_n|=|B_n| for n<=6 (1,2,6,22,89,380), |A_7|=1678 vs |B_7|=1677, |A_8|=7584 vs |B_8|=7566, |A_9|=34875 vs |B_9|=34676, and construct an explicit minimized insertion-encoding / generating-tree automaton for the NOFORMULA class B (and for A where regular, else use its known algebraic GF) that independently derives counts to n=14, cross-checked by an independent brute-force enumerator to n=10. Deliver separating count vector, automaton transition files, and rerunnable counting script.

## Attempted claim

A and B are Wilf-distinct with separating vector n=1..9: A: 1,2,6,22,89,380,1678,7584,34875; B: 1,2,6,22,89,380,1677,7566,34676 (difference first at n=7 by 1, growing to 199 at n=9), plus explicit minimized automaton files for B (expected <500 states if regular, else explicit finite transfer-matrix as constructed by Kremer-Shiu type) yielding independently derived counts a_B(10)..a_B(14) matching OEIS A165542 b-file (14443? No: A165542 n=10 is 160808 per OEIS offset; to be recomputed and cited with offset) and a_A(10)..a_A(14) matching A165543, with two independent programs agreeing to n=10.

## Research outcome

Fallback-scope CLAIMED: two-program Wilf-separation certificate for Av(1234,1342) vs Av(4231,4123) to n=10 (separation 1678 vs 1677 at n=7) with P1 extension to n=13 and full 56-type census to n=10 (38 sequences, Schroder largest block to 206098). DFA/n=14 explicitly not claimed.

## Why this attempt failed

Failed axes: originality, value.

originality: The claimed Wilf-distinctness theorem is prior art, conceded by the draft itself, and no new mathematical object, classification, formula, or automaton is delivered. Nearest priors (from topic.json, treated as untrusted pointers but corroborated by draft admissions and internal consistency): (a) Le (2005) 'Wilf Classes of Pairs of Permutations of Length 4' DOI 10.37236/1922 proves the complete Wilf-classification of (4,4) pairs via block bijections — draft §1 states 'The Wilf-distinctness theorem itself is due to Le (2005); our contribution is only the machine-checkable certificate' and 'We add no new classification theorem'. Hence A vs B separation (agree to n=6, differ 1678 vs 1677 at n=7) is not new. (b) OEIS A165543 (A, algebraic) and A165542 (B, NOFORMULA): draft reproduces assignment-quoted values to n=9 exactly plus B10=160808 note; topic states b-files to 270+ terms, so vectors to n=10 and P1 extensions to n=13 (17469863 vs 16830544) add no new sequence terms beyond OEIS — mere recomputation. (c) Kremer-Shiu (2003) finite transfer matrices for many (4,4) pairs: draft states 'We do not reproduce their matrices; our trie is an unminimized generating tree.' (d) Albert-Linton-Ruskuc insertion-encoding regularity criterion: draft states 'We do not instantiate a minimized DFA for B here' and §7 records regularity_probe.py as inconclusive with correct analysis not completed. The target's novel component (minimized DFA <500 states or Kremer-type transfer matrix plus counts to n=14 resolving rationality of A165542) is explicitly NOT done. (e) 56-type census (38 sequences, largest size-10 Schroder block 1,2,6,22,90,394,1806,8558,41586,206098) is strictly weaker than Le's true classification — draft §6 admits 'No Wilf-equivalence is proved beyond n=10; blocks are candidate-equivalence (necessary but not sufficient)'. Schroder block is textbook separable-permutation enumeration. New artifacts are only scripts/checksums/runtimes, not a new gap, bijection, GF, or DFA. A timestamp or failed search does not establish priority; here priority lies with cited prior art that predates the candidate. value: Even taking correctness as given, the fallback-scope result is not independently worth finding later; it falls squarely into SCOPE reject categories. (1) Mere verification: two-program recomputation of OEIS A165542/A165543 to n=10 where OEIS already carries 270+ terms and Le already proves distinctness is textbook checking, not a finding a later researcher would search for and cite. (2) Unexplained enumeration: 38 candidate blocks to n=10 without bijections, GFs, or growth results (draft admits they 'may split at n=11+; we assert only the computed table'), and brute-force terms to n=13 (single-program for n>=11) with no generating function, bijection, growth-rate theorem, or rationality resolution. (3) Tiny unmotivated gain: extending single-program brute-force counts from n=10 (162560/160808) to n=13 where closed-form status is unchanged (A a…

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Wilf-distinctness theorem itself is Le 2005, not new; certificate only.', 'No minimized insertion-encoding DFA, no rational GF, no transfer matrix, no n=14 counts; regularity/rationality of B unresolved; probe inconclusive.', 'n=11..13 terms are single-program (P1) verified, not two-program certified.', 'No live OEIS b-file diff (offline transport error); comparison to assignment-quoted values + internal agreement.', '56-type blocks to n=10 are candidate-equivalence only; may split later.', '…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
