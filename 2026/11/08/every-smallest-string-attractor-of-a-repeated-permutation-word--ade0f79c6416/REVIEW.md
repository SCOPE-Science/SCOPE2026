# Scientific review of a repeated-permutation string-attractor classification

## Correctness (C): PASS

The object is the finite linear word \(P^k\), with \(q\ge3\)
distinct base-period letters and \(k\ge2\). The lower bound \(q\) is
forced by single-letter factors. The proof establishes a full
necessary-and-sufficient classification: every size-\(q\) set is one
position per letter, and the only excluded condition is simultaneous
selection of the two extreme positions. For short factors, occurrence
alignment with an internal period junction suffices. For factors of
length at least one period, every occurrence begins in a single
residue class, the union of intervals is contiguous, and the only
possible outside-only transversal chooses both endpoints. The count
subtracts exactly \(k^{q-2}\) invalid choices from \(k^q\).

`verify.py` independently enumerates distinct factors and all their
occurrences for 31 finite parameter cases and 204695 candidate
sets, with maximum tested word length 35. The complete-integer proof
is independent of this computational evidence. Limits: the verifier
does not exhaust all integer parameters or replace a proof.

## Originality (O): PASS, subject to priority risk

Material comparisons were made against arXiv:1907.04660 (original
finite-word framework, Proposition 4 and Corollary 2),
arXiv:2206.00376 (periodic and infinite-word attractor profiles),
the public author version of Cassaigne and collaborators (2024),
and CPM 2026 results on Fibonacci/period-doubling attractors.
The first work bounds minimum sizes for powers and supplies a
particular attractor for a distinct-run base word; none of the cited
specific theorems determines all minimal transversals and their
exact count for powers of a permutation on at least three letters.
The binary alternating case is credited rather than claimed as new.
A check of indexed relevant prior findings likewise did not locate
the multi-letter all-minimizer theorem. Remaining risk: a differently
formulated or unindexed equivalent result.

## Mathematical value (V): PASS

All minimal solutions to a combinatorial optimization problem are
classified for a natural unbounded two-parameter family. The count
\(k^{q-2}(k^2-1)\) and the reduction of an all-factor condition
to a single length-two junction factor reveal a local-to-global
rigidity that is not provided by the general power inequality.
This exact position structure makes the result relevant to the
study of attractor multiplicity and position dispersion, not merely
to calculating an already known minimum cardinality. The binary
specialization alone would be insufficient, hence the domain
\(q\ge3\) is essential to the novelty assessment.

## Limitations

Only ordinary finite linear factors and full repetition of a
permutation period are covered. Priority remains subject to independent
bibliographic review; the mathematical checks reported are not an
independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
