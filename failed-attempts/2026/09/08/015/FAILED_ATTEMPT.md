# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** SAT-certified census around R(3,4)=9 with R(3,5) witness: DRAT UNSAT on K9, full isomorphism census on K8, and explicit (3,5)-free coloring of K13
- **Round:** 2026-09-07-first-light-01
- **Lane:** 74
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Extremal Combinatorics
- **Method:** Boolean satisfiability encoding with DRAT unsatisfiability certification and explicit coloring replay

## Problem

Let F_n^(s,t) be the CNF over C(n,2) variables x_e (x_e=True means edge e red, False means blue): for each s-subset S of [n] add clause OR_{e in K_S} (-x_e) forbidding a red K_s, and for each t-subset T add clause OR_{e in K_T} (x_e) forbidding a blue K_t. Tasks: (a) prove F_9^(3,4) UNSAT with a DRAT proof checkable by drat-trim; (b) exhaustively enumerate all satisfying assignments of F_8^(3,4) up to vertex-permutation isomorphism, reporting the exact number N of isomorphism classes with canonical representatives, automorphism orders, and red-degree sequences; (c) exhibit one explicit satisfying assignment of F_13^(3,5) with machine-checkable matrices. All DIMACS files, DRAT proofs, enumeration logs, and a one-command Python replay verifier (which rechecks red-triangle-freeness and blue-K4/K5-freeness by brute force without invoking the solver) must be archived.

## Attempted claim

F_9^(3,4) is UNSAT (verified by drat-trim), F_8^(3,4) has exactly N isomorphism classes of (3,4)-free red-blue colorings (N determined by exhaustive SAT enumeration with blocking clauses plus nauty/bliss canonical labeling, with explicit representatives and logs), and there exists an explicit (3,5)-free coloring of K13 (adjacency matrix plus independent brute-force triangle/K5-freeness log), together establishing a replay-verifiable certificate package for R(3,4)=9 approaching R(3,5)=14.

## Research outcome

Certified census around R(3,4)=9 with R(3,5) witness, replay-verifiable in ~10s: F9 UNSAT by 40.6M-completion extension proof over a twice-enumerated complete K8 census (17640 labeled models, 3 isomorphism classes with canonical reps/aut orders/degree seqs), plus an explicit brute-force-checked (3,5)-free K13 coloring. DRAT format not delivered (no solver in environment); see limitations.

## Why this attempt failed

Failed axes: value.

value: FAIL: textbook restatement + tiny-scale unexplained enumeration, not independently worth finding later even though correct and narrowly new. R(3,4)=9 and R(3,5)>13 have been textbook since Greenwood-Gleason 1955; classical proofs are short hand-checkable case analyses, so a machine re-proof at n=8/9 adds no needed auditability (contrast Li et al. R(3,8)/R(3,9) where 59h search and 7-day SAT-only timeout justify certificates). Computation here is trivial: 28 vars/126 clauses, ~1.4M/0.6M-node DFS, 40.6M-completion extension check, full replay ~10s wall - undergraduate-scale exercise. The K13 witness existence is implied by known R(3,5)=14 and explicit 13-vertex (3,5)-free colorings are classical (cyclic constructions); this witness claims no extremality, uniqueness, structural insight, or use toward the R(3,5)=14 upper bound (DRAFT Limitation 4 admits this). The F8 census (17640 in 3 classes with aut orders/degree seqs) is published as bare counts + matrices with no downstream theorem beyond re-proving known R(3,4)<=9 and no transferable method: SAT-Ramsey encoding is standard (Molnar/Kullmann), dual backtrackers + brute-force S8 lex-min are routine parameter substitution, and the promised DRAT/solver/nauty artifacts that might have given benchmark reuse value were not delivered. A 'certified dataset/data paper' for a 10-second 8-vertex census at a 1955 threshold is not independently citable; the SCOPE-FAIL-20260907-007 precedent (value-REJECT for a correct narrowly-new SAT+DRAT Ramsey-Turan number) applies a fortiori here. This is exactly the textbook-restatement / mere-parameter-substitution / unexplained-enumeration exclusion.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: No DRAT proof and no drat-trim check: environment had no SAT solver and no installer, so UNSAT is certified by the machine-checked extension argument, not DRAT as the audit plan required. No solver cross-check (bespoke backtrackers only, mitigated by two independent enumerators + from-source reruns). Isomorphism by brute-force lex-min over S8, not nauty/bliss. Values R(3,4)=9/R(3,5)=14 are classical; novelty is the certificate/census packaging; R(3,5)=14 upper bound not addressed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
