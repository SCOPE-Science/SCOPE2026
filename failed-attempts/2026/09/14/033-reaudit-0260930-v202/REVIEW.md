# Review status

Fresh independent audit completed on 2026-10-01 UTC.

Disposition: **failed**.

- Correctness: **PASS** — The archived exact inputs give rank E(Q)=1, twist rank 0, p=5 ordinary and split in Q(sqrt(-11)), a 5-adic regulator with valuation 1, a cyclotomic p-adic L derivative with valuation 1, and a twist central p-adic value that is a unit. Published p-adic Artin formalism supports base-change factorization, and p-adic Gross-Zagier identifies the cyclotomic derivative with the Heegner height up to nonzero normalization. The record correctly avoids identifying PARI ellheegner(E)=[0,0] with the discriminant -11 Heegner point.
- Originality: **PASS** — Best-of-knowledge: the 37a1 p=5 regulator itself is a documented Sage example, but targeted searches did not locate the exact K=Q(sqrt(-11)) Rankin/Heegner specialization or its stated simple-zero/nonzero-height verification.
- Scientific value: **FAIL** — After separating the already-documented 37a1 p=5 regulator from the final conclusion, the remaining K=-11 statement is a parameter-level instantiation of general p-adic Artin formalism and p-adic Gross-Zagier using standard CAS outputs. The record does not identify a boundary phenomenon, new structural lemma, or independent reason a future researcher would need this precise specialization.

See `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json` for structured source comparisons and residual risks.
