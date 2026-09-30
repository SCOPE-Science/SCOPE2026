# Independent Audit — 2026/09/14/026

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `bd269221d7d6d196c9777d1643382bd28a5fd38e`  
**Audited current source tree:** `bd269221d7d6d196c9777d1643382bd28a5fd38e`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` directory tree SHA exactly matches the assignment tree SHA, and the designated failed destination was verified absent.

## Correctness — PASS

PASS. The algebraic conclusion is correct. With B=kC2≅k[u]/(u^2) in characteristic 2, B is self-injective and its trivial module has an infinite periodic projective resolution, so the full algebra has infinite global dimension. Dietrich's directed-stratification/Fossum–Griffith–Reiten bound gives finitistic dimension at most 1 for the two strata k and B. The displayed left module (0,B,0) has the exact nonsplit sequence 0→(M,0)→(M,B,id)→(0,B,0)→0, so its projective dimension is 1 whenever M≠0. On the right, M_B≅B⊕k and projection to the trivial summand gives the stated projective-dimension-1 witness. Hence left and right finitistic dimensions are indeed 1.

## Originality — FAIL

FAIL. The headline exact value does not require a new phenomenon or a difficult case-specific computation. The upper bound is an immediate instance of the published directed-stratification theorem; the left lower bound is the universal one-step resolution attached to any nonzero off-diagonal bimodule, and the right lower bound follows immediately from the visibly split M_B≅B⊕k. Thus the six-dimensional example is a routine specialization of general triangular/EI-algebra machinery rather than an original research result, even if this exact tiny biset was not separately tabulated.

## Scientific value — FAIL

FAIL AS A NEW RESEARCH FINDING. The record is a correct worked example, but it adds neither a general criterion, classification, new homological mechanism, nor a nontrivial boundary case beyond the known fin.dim≤1 theorem. The finite calculation is pedagogically serviceable but too mechanically implied by standard theory to justify publication as a standalone validated finding.

## Independent checks

- rederived B=k[u]/(u^2) periodicity and self-injectivity
- constructed the left one-step resolution abstractly from the triangular algebra
- checked M_B=B⊕k from one free and one fixed C2 orbit and reconstructed the right pd-1 quotient
- checked current record tree equals the assigned tree and failed destination is vacant

## Limitations

- The scientific rejection is on originality/value, not correctness.
- The audit does not claim that the exact six-dimensional algebra has previously been printed as a named example; the failure is that the result is mechanically obtained from existing general theory plus an elementary module check.
- Open-access sources were sufficient; Oxford Download was not needed.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/14/026
- https://arxiv.org/abs/1102.2577
- https://arxiv.org/abs/0907.2141

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain exactly as previously recorded.
