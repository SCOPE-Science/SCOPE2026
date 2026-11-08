# Scientific assessment

## Correctness — PASS
For any collision between indices \(a<b\), the difference factors as \(2(T(b)-T(a))=(b-a)(a+b-1)\), where the two positive factors have opposite parity. Splitting off the odd part of the modulus yields a sharp lower bound on their sum, while an odd divisor and the complementary even factor construct a pair attaining it with exact difference \(m\). Equality throughout proves uniqueness of the first witness. The prime-power formulas follow from a monotonic finite difference. The direct-enumeration verifier checks all moduli through 9999 but is not needed for the infinite proof.

## Originality — PASS (priority qualified)
The closest published work studies triangular sequence discriminators, optimizing the modulus for a prescribed prefix, or full modular periods and first returns of zero. Those results do not directly specify the exact first collision index and the unique witness for **every fixed modulus**, nor do they imply these conclusions without the new divisor-pair argument. Accessible full primary material and targeted literature searches were inspected. The 2022 modular-structure article could be read only in indexed passages because full-text access returned a rate-limit response, leaving a concrete priority risk. No claim of uniqueness within the literature is made.

## Value — PASS
The maximal injective prefix at a **given** modulus is the inverse discriminating question needed when the modulus is predetermined, and the theorem gives its exact universal classification rather than only upper bounds or experimentally observed cases. The unique first witness and exact difference identify the arithmetic obstruction, while explicit prime-power cutoffs expose a parity transition in the exponent. This does not determine general fibers or every possible later collision.

### Prior literature and limits
Sun (2013, arXiv:1304.5988) motivates collision-free triangular residues; Haque (2017, Chapter 5) analyzes triangular discriminators; Ulness (2022, DOI 10.3390/appliedmath2030020) covers modular structure and periods. Priority comparisons are not exhaustive, and the 2022 article's full text was not fully examined.

Self-review: passed. Independent audit: not yet performed.
