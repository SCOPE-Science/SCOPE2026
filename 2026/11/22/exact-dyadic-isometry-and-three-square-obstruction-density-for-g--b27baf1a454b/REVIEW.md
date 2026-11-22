# Scientific review — dyadic generalized derangements at parameter two

## Correctness: PASS
The claim's integral normalization is fixed by \(G_0=1\), \(G_1=2\). The recurrence and ordinary-derangement identity agree algebraically and against independent finite evaluation. The two restricted power series are coefficientwise convergent; explicit reductions modulo eight establish integral affine leading terms, whose one-Lipschitz corrections give an exact global two-adic isometry. Legendre's theorem, uniqueness of each index antecedent modulo powers of two, and a geometric-tail count prove the disjoint obstruction progressions and density \(1/6\) with \(O(\log X)\) error. A standalone finite checker corroborates the critical congruences and all small power-modulus fibers, without being mistaken for an infinite proof.

## Originality: PASS within the inspected sources
Ulas's 2023 article (online 2024-09-10) explicitly asks for even-parameter three-square obstruction sets and the existence of their density. Its even-parameter results give only congruence inclusions and lower density bounds. The present result for parameter two proves a stronger exact isometry, a complete class decomposition, and an exact density. Combinatorial generalized-derangement identities from Ferrari–Munarini–Zagaglia Salvi and the abstracted classical-derangement results from Miska do not explicitly cover these claims in the material examined. Published modular residue results for ordinary derangements concern parameter zero, with nonuniform fibers, and cannot directly imply parameter-two isometry. Search negatives alone do not prove novelty; equivalence in unexamined generalized-derangement arithmetic remains a risk.

## Value: PASS
This addresses a named outstanding number-theoretic question for the smallest untreated even generalized-derangement parameter, replacing a known lower bound \(1/8\) by an exact obstruction density \(1/6\) and identifying every obstructed index class. The distance-preservation theorem also gives a strong standalone structural characterization at every dyadic precision.

## Limitations and evidence
The result does not address arbitrary even parameters or the count of square representations, and the date of the original issue is less precise than the verified publisher online date. The arithmetic proof is fully given in RESULT.md. Finite reproducibility checks are in verify.py. Potential implicit earlier results in only partially accessible arithmetic literature are a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
