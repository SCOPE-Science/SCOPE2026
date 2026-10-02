# Review status

Independent mathematical audit: **failed** on 2026-10-01 UTC.

Correctness: PASS. The derivation is mathematically sound. The exponent-three source gives an explicit finite witness bound for non-amalgamation. Local finiteness and the explicit size of free exponent-three Burnside groups make the finite obstruction set and finite amalgamability decidable. Direct products give joint embedding of the universal class, and a model companion of a joint-embedding universal theory is complete. A complete computably enumerable theory is decidable by dovetailing proofs of a sentence and its negation.

Originality: FAIL. Originality fails by implication. Burris, “Decidable Model Companions” (1989), Theorem 1.7 proves decidability from decidable universal theory plus the recursively bounded obstruction property, Lemma 2.2 proves decidability of the universal theory for locally finite finitely axiomatizable universal classes in a finite language, and Theorem 2.3 combines them: such a class has a decidable model companion exactly when its existentially closed class has a recursively bounded obstruction property. The 2026 exponent-three paper supplies precisely an explicit recursive bounded-obstruction theorem. Therefore the audited decidability conclusion is a direct specialization of Burris’s pre-existing general criterion even if the exact exponent-three application had not been written down.

Value: FAIL. Value fails under the stated bar once prior implication is taken seriously. After the 2026 source establishes an explicit recursive bounded obstruction for the locally finite finite-language exponent-three class, Burris’s Theorem 2.3 gives decidability directly. The remaining completeness and proof-enumeration observations are standard. The package is a correct and useful corollary, but not a distinct motivated research gap.

The original package is retained as a failed attempt rather than a validated finding. See `INDEPENDENT_AUDIT_2026-10-01.md`, `INDEPENDENT_AUDIT_2026-10-01.json`, and `FAILED_ATTEMPT.md`.
