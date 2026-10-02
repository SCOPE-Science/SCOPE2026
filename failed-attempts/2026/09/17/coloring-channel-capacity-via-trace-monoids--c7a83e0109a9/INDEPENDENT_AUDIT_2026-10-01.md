---
audit_date: 2026-10-01
status: failed
---

# Scientific audit

## Final claim

Coloring-channel output classes are trace-monoid histories for the pairs graph, so their exact generating function is the reciprocal signed independence polynomial and their capacity is the logarithm of the reciprocal smallest positive root; for a cycle \(C_t\) this gives \(\log_q(4\cos^2(\pi/(2t)))\).

## Correctness — PASS

The kernel of the projection tuple was reconstructed using labelled occurrences and the dependence poset: equality of all channel projections fixes every dependent pair order, and linear extensions differ only by adjacent swaps of independent letters. Independent brute-force checks for cycles \(C_3\) through \(C_7\) reproduced the signed independence polynomials and their smallest roots, including \(C_4\) root \(1/(2+\sqrt2)\). The package verifier was inspected and is consistent with these checks.

**Evidence:** package RESULT.md; artifacts/verify.py blob 4b074ae8960a6ca21d35ba9f1dc0bb06657ea242; W. Yu and M. Schwartz, arXiv:2604.08234

**Residual risk:** The finite checks are corroboration; the general trace-congruence proof and classical trace growth theorem carry the infinite statement.

## Originality — FAIL

The projection quotient used by coloring channels is already the classical history-monoid construction: tuples of projections to overlapping alphabets are isomorphic to the trace monoid whose dependency relation is the union of within-channel pairs. Once this standard identification is made, Cartier–Foata/Möbius growth gives the reciprocal polynomial formula mechanically. The 2026 coloring-channel paper may have left cycles open, but an open question in that terminology does not make a direct instance of an older general theorem original.

**Equivalent formulations.** This is statement-level equivalence, not merely an analogy.

**Broader coverage.** The general trace theorem directly dominates the channel-specific capacity claim.

**Exact database or table.** Absence of the number in the newer paper is not novelty evidence against a stronger general theorem.

**Claim versus prior implication.** These prior implications cover both the general capacity theorem and the cycle corollary.

**Checked sources:** https://doi.org/10.1093/comjnl/28.5.449; https://arxiv.org/abs/2111.00507; https://arxiv.org/abs/2604.08234; classical Cartier–Foata trace theory

**Residual risk:** Shields's full text was inaccessible, but the history-monoid projection equivalence is a standard established formulation reproduced in later trace literature; the coverage conclusion does not rest on a mere title match.

## Value — FAIL

Although the observation closes a recent open-looking channel calculation, the final result is obtained by recognizing the model as the classical projection/history monoid and then applying its standard growth theorem. Under the required bar, that is a renaming/substitution of a known general structure rather than a new mathematical invariant or theorem.

**Residual risk:** The identification may still be pedagogically useful to the coloring-channel community, but utility does not override scientific coverage.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
