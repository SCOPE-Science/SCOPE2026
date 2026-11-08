# Self-review

## Correctness — PASS

The statement identifies the precise family of all derivations of the two-vertex, parallel-arrow path algebra, derives the iterated-power condition from the action on its basis, and computes the full algebra automorphism action. The key quotient is \(\ker T^{p-1}/TV\), which is well-defined because \(T^p=0\). Nilpotent module decompositions and a constructive block-triangular centralizer argument give both necessity and sufficiency of the partition-plus-length orbit labels. The orbit-size and rank polynomials follow by counting individual nilpotent similarity classes and translation cosets. The finite test suite checks the original algebra identities, not only an assumed matrix normal form. Its tested instances match; an arbitrary-field proof is separately supplied.

## Originality — PASS, provisional

Guo–Li [1] establishes the derivation basis and Lie algebra of path algebras and is credited. Achar–Henderson [2] already parametrizes the finer \(\operatorname{GL}(V)\)-orbits on the enhanced nilpotent cone; Sun [3] counts those finite-field orbits. Neither inspected statement directly treats the full automorphism action on derivations, which includes translation by \(TV\), or the \(p\)-nilpotence-constrained partition-plus-length classification, exact automorphism-orbit sizes, and rank generating polynomial. The strongest risk is a general affine-adjoint orbit classification or an unlocated derivation-specific specialization that already supplies these consequences. A search without a match is not proof of historical priority. Independent priority validation has not been performed.

## Value — PASS

Derivations with \(D^p=0\) are the restricted-nilpotent locus of the derivation Lie algebra and correspond to height-one additive infinitesimal actions in characteristic \(p\). A complete classification under actual algebra automorphisms, rather than only arrow-space changes, is a natural invariant. The uniform orbit-series collapse and exact finite-field rank strata quantify a structural distinction between Jordan type and residual derivation direction. The result is not a single small-field census or an arbitrary parameter slice.

## Literature and remaining boundaries

[1] Li Guo and Fang Li, *Structure of Hochschild cohomology of path algebras and differential formulation of Euler's polyhedron formula*, arXiv:1010.1980 (2010), https://arxiv.org/abs/1010.1980, §§2–3.

[2] Pramod N. Achar and Anthony Henderson, *Orbit closures in the enhanced nilpotent cone*, arXiv:0712.1079 (2007), https://arxiv.org/abs/0712.1079, Proposition 2.3 and §5.

[3] Michael Yuan Sun, *Point stabilisers for the enhanced and exotic nilpotent cones*, arXiv:0909.0356 (2009), https://arxiv.org/abs/0909.0356, §2.

This is a classification for the specified quiver and ordinary \(p\)-fold derivation nilpotence; it neither addresses general quivers nor settles orbit-closure geometry. Historical priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
