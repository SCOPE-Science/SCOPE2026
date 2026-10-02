---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

If closed subspaces \(M,N\subseteq\ell_\infty\) have infinite-dimensional reflexive quotients and \(M,N\) are Fredholm equivalent, then the quotients are Fredholm equivalent; consequently the González--Kania kernel family is pairwise inequivalent under arbitrary finite-dimensional stabilization.

## Correctness — PASS

Given a Fredholm U:M→N, choose a complement M=M0⊕ker U and let R=ran U; then U|M0:M0→R is an isomorphism and both ambient quotients by M0 and R remain infinite-dimensional reflexive because they are finite-dimensional extensions of the original quotients. The Lindenstrauss--Rosenthal theorem therefore gives a Fredholm extension on ell_infinity. Since the extension maps M0 onto R, the induced quotient operator has finite-dimensional kernel and cokernel. The canonical maps from the reduced quotients to the original quotients are themselves Fredholm, so transitivity yields the claim.

**Checked sources.** Assigned RESULT.md at tree 5456db5c89645077e4a88206591b45a6be803b8b; González--Kania, Mathematische Nachrichten 2026; Lindenstrauss--Rosenthal extension theorem as quoted in González--Kania

**Residual risks.** No correctness defect was found; the rejection is because the theorem is a routine finite-dimensional stabilization of a classical extension theorem.

## Originality — FAIL

The current González--Kania paper gives the exact Lindenstrauss--Rosenthal input: any isomorphism between subspaces with infinite-dimensional reflexive quotients has a Fredholm extension, and Proposition 2.2 already passes that extension to a Fredholm map between quotients. Replacing a Fredholm map between kernels by its isomorphic finite-codimensional restriction is the standard defining reduction for Fredholm operators. Thus the audited transfer theorem is mechanically implied by the published proposition's argument plus routine finite-dimensional reduction.

### Equivalent formulations

The only change in the audited theorem is replacing an isomorphism by a Fredholm map, which standardly restricts to an isomorphism between finite-codimensional subspaces.

### Broader coverage

The classical extension theorem plus the published proposition's mechanism broadly covers the stable variant.

### Exact database or table

The claim is theorem-level and follows from extension/Fredholm structure; a database/table comparison is genuinely inapplicable.

### Claim versus prior implication

The prior implication is decisive even though the stable variant is not separately named as a proposition.

**Checked sources.** https://onlinelibrary.wiley.com/doi/10.1002/mana.70255; https://doi.org/10.1007/BF02787616

**Residual risks.** The 1969 original was not independently read, but the decisive theorem and its use are fully stated in the accessible 2026 primary paper.

## Value — FAIL

The stable strengthening is a sensible observation, but it is obtained by the textbook finite-dimensional reduction of a Fredholm operator followed by the exact published extension argument. Under the required value bar, that is a routine deduction rather than a new motivated structural gap.

**Residual risks.** The corollary can be useful for stating the construction in stable language, but that utility does not overcome its routine derivation.

## Limitations

- The argument is specific to the Lindenstrauss--Rosenthal extension property in \(\ell_\infty\).
- No converse transfer is claimed.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
