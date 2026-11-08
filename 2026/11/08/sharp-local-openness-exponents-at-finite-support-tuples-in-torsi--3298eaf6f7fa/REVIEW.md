# Mathematical review

## Correctness — PASS

Finite supports in a torsion abelian group generate a finite subgroup. The primitive character idempotents have unit \(\ell^1\)-norm, sum to the identity and split the **whole** group algebra; this allows arbitrary target perturbations, not only finitely supported ones. Component-wise exact factor construction proves the lower image radius with explicit control, and norm-one character evaluation on the ambient group gives the matching upper exponent. The cases with no common zeros and with a completely zero component are both handled. The finite checker returns `EXACT_FINITE_CONVOLUTION_MODULI_OK 201` but is not the proof of the infinite theorem.

## Originality — PASS (best-knowledge)

Flores, *The convolution product is generally not an open map* (arXiv:2610.38722v1), Theorem 1.2 and §1, leaves infinite torsion abelian groups unresolved and does not classify any sharp local openness exponents for their finitely supported tuples. Draga and Kania, *When is multiplication in a Banach algebra open?* (arXiv:1704.08608v2), Corollary 2.6, deduce topological stable rank one from dense idempotents but explicitly distinguish this from open multiplication; their §3 and §5 do not assert the current full-algebra finite-support local modulus. Kania and Maślany, *Differential embeddings into algebras of topological stable rank 1* (arXiv:2301.02320), Theorems 1.2 and 1.4, address jointly non-degenerate pairs under specified assumptions and non-uniform openness, not arbitrary degeneracy or sharp k-fold rates. Database queries for finite-idempotent and torsion convolution openness did not locate a covering statement. A general coordinate-multiplication argument could occur in older literature; publication priority remains uncertain.

## Mathematical value — PASS

This gives a complete, exact, quantitative openness classification on the natural **dense** family of finitely supported input tuples inside the specific infinite group algebras left unresolved by the initiating paper. Unlike a computation solely inside a finite algebra, the factorization works for every target in the full infinite-dimensional \(\ell^1(G)\). The exponent identifies how many factors vanish simultaneously at a Fourier coordinate and separates linear from higher-order local behavior. The theorem locates any possible failure of global openness at an infinite-support base factor, though it does not solve that problem.

## Limitations and publication-priority risk

Only finitely supported inputs and abelian torsion groups are covered; no uniform constants. Exact arithmetic cannot certify infinite-dimensional statements. The closest remaining originality risk is an earlier general result on local multiplication in Banach algebras spanned by orthogonal idempotents, possibly under other terminology. Human mathematical verification has not occurred.

Self-review: passed. Independent audit: not yet performed.
