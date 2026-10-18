# Independent mathematical audit

## correctness

PASS

The cohomological ring scaling from Buch–Kresch–Tamvakis maps τ_λ to 2^(−ℓ_t(λ))σ_λ, the nonmaximal hyperplane τ_1 to σ_1 because ℓ_t((1))=0, and top-class τ_ρ to 2^(−r)σ_ρ because top t-strict index has r parts above t. Comparing h^(D−|λ|) products proves the exact 2-power degree ratio. The ambient Weyl-dimension formula checker inspected in artifacts/verify.py covers n=2..18 and is corroboration only. The geometric normalization r<n is essential; r=1 reduces to a quadric degree two vs projective degree one.

## originality

FAIL

The primary Buch–Kresch–Tamvakis 2009 paper already establishes the complete type B/type C Schubert structure-constant equivalence, formula (12), and explicitly identifies the rational ring homomorphism τ_λ↦2^(−ℓ_t(λ))σ_λ (Section 2.2, source lines 380–390). Their special class and top-class facts give every degree by the definition of a Schubert top intersection. Therefore the entire claimed degree dictionary follows as an immediate corollary of a stronger primary theorem: absence of the exact printed degree formula does not confer originality. This is decisive prior implication, not a failure of keyword search.

## value

FAIL

Projective degrees are natural invariants, but the full claimed family is a one-line extraction from a published complete Schubert ring isomorphism. There is no new enumerative algorithm, nonstandard argument, boundary structure, independent classification or exact invariant beyond what the existing ring multiplication already determines. As a standalone contribution it is a routine rephrasing/corollary; O and V fail notwithstanding correct algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
