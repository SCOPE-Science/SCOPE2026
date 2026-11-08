# Mathematical review: signed-permutation cubic sampling frames

## Correctness — PASS

The frame/design equivalence is proved by polarization and polynomial factorization, and all invariant moments are normalized using probability surface measure. The moment recurrence, divisibility obstruction and exact endpoint factorization yield all quantified conclusions without extrapolating finite checks. Representative high-precision constructions and rational inequalities are exercised in `verify_design.py`.

## Originality — PASS (provisional priority)

The strongest source comparison is Misawa (2026), which also constructs three-level symmetric-group-orbit simplex cubatures, but for **uniform Dirichlet(1)** rather than the **squared-real-sphere Dirichlet(1/2)** measure, and then uses a separate lift to build spherical seven-designs. Mohammadpour–Waldron (2019) gives general reflection-orbit theory; Bajnok concerns unions of generalized hyperoctahedra; Tanino–Tamaru–Hirao–Sawa studies restricted corner vectors and gives existing seven-design orbits in dimensions sixteen and twenty-three with a zero squared-coordinate level. No inspected result directly implies both the universal impossibility of one/two squared-amplitude levels and this concrete growing-dimensional positive-three-level single-orbit construction. Related general moment methods are not claimed as new. Historical priority is not certified; a more general invariant-cubature result may subsume this specialization.

## Value — PASS

The all-dimensional exclusion and explicit infinite attaining family settle the exact minimum coordinate-amplitude complexity within a natural, symmetry-constrained Parseval sampling problem. The result is meaningful without any small-node or noise-stability claim, and the construction is a fixed simple multiplicity pattern rather than an isolated numerical example.

## Limitations

The attaining family covers dimensions divisible by twenty and at least one hundred, not all dimensions. The orbit can be very large. Computational checks cover finitely many dimensions and supplement the infinite proof. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
