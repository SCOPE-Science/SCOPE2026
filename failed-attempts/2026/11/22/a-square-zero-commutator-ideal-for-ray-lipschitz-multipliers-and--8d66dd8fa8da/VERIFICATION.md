---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 25–78 on the root-plus-edge norms. In ℂ⊕₁ℓ∞ or ℂ⊕₁c₀ the root is a scalar and C is the right shift on increments. The product rule for increments yields the boundedness criterion sup|φ_n|+sup n|Δφ_n|<∞ by testing one edge and the earlier aligned edges; c₀ is preserved by the vanishing Cesàro mean. For α<1 the printed test f(n)=n is only in the full space; on the little space take f(n)=n^β, α<β<1. It has vanishing increments and its product has edge difference q^n(1-q^(-1))n^(β-α)+O(n^(β-α-1)), so boundedness fails there too. For α>1 the derivative-row norms tend to zero. Commutator words reduce to multiplier-shift words; two commutators put two O(1/n) factors in each symbol. An O(1/n²) multiplier has tail row norms O(1/n) and thus is compact. This passes to the closed ideal and gives a commutative quotient. The binomial differences give, modulo finite initial output rows, B_m=M_a C^m with a_n=Δ^mψ_q(n). In the increment coordinates a_m U_qH, where a_m=(1-q^(-1))^(m+1), agrees with B_m modulo compact operators by an O(1/n) tail-row error. The Hardy rows converge coordinatewise to zero and have ℓ₁ norms tending to one. Finite-row truncations bound the essential norm above; against any compact operator take a converging subsequence of its adjoint output functionals restricted to c₀ and split the limit's ℓ₁ mass at a fixed finite index to get the matching lower bound. This works even on the full space. Square-compactness already follows from the ideal argument; alternatively the bounded geometric partial sums for q≠1 give O(log n/n) row mass for HU_qH. q=1 gives zero Hardy coefficient, and q≠1 gives strictly positive essential norm. The supplied script and verification notes were inspected, not executed; their finite tests cannot certify the essential norm or closure argument.

## originality

FAIL

The core square-zero extension is a direct algebraic corollary of existing graph multiplier boundedness and compactness criteria, with the nonzero witness detected by the same compactness criterion. The sharp numerical norm on the little space specializes an earlier exact general tail-row theorem; on both spaces it specializes a distinct graph multiplier exact formula. The reductions below establish coverage independently of publication order between same-day records. This is not a claim that the four-part statement was previously printed verbatim, and the verdict does not depend on an inaccessible source.

## value

FAIL

A square-zero noncommutative Calkin extension is a natural structural question, but in this record it is immediate from the known multiplier conditions and the elementary symbol/shift product law. Its quantitative witnesses are evaluations of an existing exact norm theorem. The alternate Hardy proof illustrates the mechanism but establishes no separate useful gap beyond the covered structural and numerical conclusions. Thus the audit finds no surviving distinct contribution worth a substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
