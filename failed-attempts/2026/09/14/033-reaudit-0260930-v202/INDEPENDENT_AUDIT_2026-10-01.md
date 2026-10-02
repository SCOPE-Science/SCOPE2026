# Independent mathematical audit — SCOPE-20260914-033

Disposition: **failed**.

## Correctness
**PASS** — The archived exact inputs give rank E(Q)=1, twist rank 0, p=5 ordinary and split in Q(sqrt(-11)), a 5-adic regulator with valuation 1, a cyclotomic p-adic L derivative with valuation 1, and a twist central p-adic value that is a unit. Published p-adic Artin formalism supports base-change factorization, and p-adic Gross-Zagier identifies the cyclotomic derivative with the Heegner height up to nonzero normalization. The record correctly avoids identifying PARI ellheegner(E)=[0,0] with the discriminant -11 Heegner point.

## Originality
**PASS** — Best-of-knowledge: the 37a1 p=5 regulator itself is a documented Sage example, but targeted searches did not locate the exact K=Q(sqrt(-11)) Rankin/Heegner specialization or its stated simple-zero/nonzero-height verification.

### Equivalent formulations
Equivalent simple-zero and nonzero-height formulations were compared separately from the already-known regulator example.

### Broader coverage
They cover the mechanism but do not tabulate the record's exact arithmetic specialization.

### Exact database or table
The known regulator component is not novel; the asserted specialization depends additionally on the twist and base-change data.

### Claim versus prior implication
This weakens scientific novelty of method even if the exact instantiated arithmetic fact was not located.

### Source inspections
- **The p-adic Gross-Zagier formula on Shimura curves** (https://arxiv.org/abs/1510.02114): general coverage of mechanism. Formula relates p-adic heights of Heegner points to cyclotomic derivative of a Rankin-Selberg p-adic L-function.
- **Families of Bianchi modular symbols: critical base-change p-adic L-functions and p-adic Artin formalism** (https://arxiv.org/abs/1808.09750): supports p-adic Artin factorization. Authors explicitly prove factorization of base-change p-adic L-functions under Artin formalism.
- **Sage elliptic curves over Q reference manual** (https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html): exact regulator component already public. Documentation prints the same initial 5-adic digits.

## Scientific value
**FAIL** — After separating the already-documented 37a1 p=5 regulator from the final conclusion, the remaining K=-11 statement is a parameter-level instantiation of general p-adic Artin formalism and p-adic Gross-Zagier using standard CAS outputs. The record does not identify a boundary phenomenon, new structural lemma, or independent reason a future researcher would need this precise specialization.

## Residual risks
- No independent PARI/Sage rerun was performed in this environment; the audit checked the archived p-adic expansions and theorem implications rather than re-executing the CAS library.

## Checked sources
- record artifacts/pari_results.json and reproducibility.json
- Sage reference
- arXiv:1510.02114
- arXiv:2001.00045
- arXiv:1808.09750
- Resultary
