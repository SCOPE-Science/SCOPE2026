# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Primality of submaximal minors of a sparse generic symmetric matrix under 2-connectedness
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20405
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Commutative Algebra
- **Method:** Grobner degeneration and liaison analysis

## Problem

Let K be a field of characteristic zero, R=K[x_{ij}:1<=i<=j<=n] with n>=3, X the generic symmetric n×n matrix, and X_G the sparse generic symmetric matrix obtained by setting x_{ij}=x_{ji}=0 whenever ij is a non-edge of a simple graph G on [n]. Let I_{n-1}(X_G) be the ideal of all (n-1)-minors of X_G. If every induced subgraph of G on n-1 vertices is connected (i.e. G-v is connected for every vertex v), is I_{n-1}(X_G) prime?

## Attempted claim

Let K be a field of characteristic zero, R=K[x_{ij}:1<=i<=j<=n] with n>=3, X the generic symmetric n×n matrix, and X_G the sparse generic symmetric matrix obtained by setting x_{ij}=x_{ji}=0 whenever ij is a non-edge of a simple graph G on [n]. Let I_{n-1}(X_G) be the ideal of all (n-1)-minors of X_G. If every induced subgraph of G on n-1 vertices is connected (i.e. G-v is connected for every vertex v), is I_{n-1}(X_G) prime?

## Research outcome

Proved the n=4 case of the target: all 2-connected 4-vertex graphs classified (C4, diamond, K4) with I_3(X_G) prime for each, via certified squarefree lex Groebner basis plus rank-parametrization irreducibility.

## Why this attempt failed

Failed axes: originality.

originality: The EMERGENT_FINDING genuinely arose from target work (n=4 is the target's smallest nontrivial case, attacked with the target's Groebner-plus-parametrization methods), so there is no scope evasion; but full prior-art review defeats novelty. Deng-Kretschmer Proposition 15 proves in characteristic zero that for every n, I_3(X_G) is prime iff G is (n-2)-connected, which at n=4 is exactly the submitted primality claim, with the C4/diamond/K4 enumeration being elementary. The same paper's Question 16 poses the target question verbatim and records Macaulay2 verification affirmative for n<=6, so the n=4 fact was already recorded both as a proved theorem instance and computationally; Conca-Welker forest-primality plus transfer is the deeper prior implying it. The lane's delta (alternative self-contained proof, explicit S-pair certificate, incidental extension to characteristic not 2) is recomputation/certificate/parameter variation, which the STANDARD says cannot create originality; no literature search was performed in-lane.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: The full target (all n>=3) is NOT proved: for n>=5 the uniform squarefree-Groebner-basis property and the irreducibility of the coupled constraint variety Z remain open; only computational evidence is offered (C5 degree-20 irreducible plane sections, double-hub dimension checks). The primality argument is stated over characteristic not 2 (symmetric U^T U diagonalization); the target asks characteristic zero, which is covered. The sharpness remark (cut-vertex graphs give reducible ideals) is sta…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
