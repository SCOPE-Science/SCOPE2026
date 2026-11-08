# Self-review

## Correctness — PASS

The proof derives the exact quotient Frobenius formula, rather than assuming it from a similar formula for consecutive generators. It verifies the Sylvester gap-symmetry identity for \(\langle a,a+h\rangle\), computes the least semigroup representative of the Frobenius residue modulo \(p\), establishes that this representative lies below the classical Frobenius number, and obtains the constituent polynomial. The zero-residue branch is unique by the explicit modular congruence at lengths \(p-1\) and \(p-2\); the Chinese remainder theorem then excludes every proposed period not divisible by \(p\), including on the restricted coprime domain. Independent finite exact membership checks match \(1{,}920\) cases. These checks are corroboration, not a proof of infinitely many cases.

## Originality — PASS (qualified)

Liu's July 2026 formula covers \(\langle a,a+1\rangle/p\), not the family of fixed gaps \(h\ge2\). The April 2026 work assumes the quotient divisor divides a generator in its general setting and does not supply the moving-residue formula. An earlier exact-period theorem for the consecutive-generator case is a strict boundary case and neither supplies nor implies the asserted fixed-gap classification. Targeted searches for fixed-gap quotients, quasi-period collapse, residue formulas, and equivalent constructions identified no stronger covering statement. The literature is not exhaustive; priority remains provisional.

## Mathematical value — PASS

The first fixed-gap extension beyond consecutive generators addresses a natural parameter in the established quotient Frobenius problem. It supplies a finite computable residue classification for every fixed coprime gap, plus the **sharp minimal** quasi-period rather than merely an available upper period. The exact period controls the complexity of eventual polynomial descriptions and excludes artificial period collapse when domain coprimality constraints are imposed. Both the structural rigidity and broad parameter range distinguish it from a one-case calculation.

## Limits and closest literature

The result is confined to fixed \(p,h\) with \(\gcd(p,h)=1\) and sufficiently large \(a\) satisfying \(\gcd(a,h)=1\). No assertion is made that the lower bound on \(a\) is optimal, nor that the theorem resolves the general three-variable Frobenius quotient problem. Closest references: Liu (2026), arXiv:2607.23076v1 and arXiv:2604.26415v1. Nonindexed equivalent work cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
