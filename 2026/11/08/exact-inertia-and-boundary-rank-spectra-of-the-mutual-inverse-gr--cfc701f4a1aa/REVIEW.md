# Scientific review

## Correctness — PASS

The claim concerns the adjacency matrix with loops on the mutual-inverse relation, not a simple graph with its diagonal deleted. The intrinsic inverse equations and the crossed-square incidence give the precise operator \(X\mapsto RX^{\mathsf T}R\). A unit lower-triangular minor establishes \(\operatorname{rank}R=p\) for every permitted rank, including \(r=1,n\). An orthogonal singular-value basis then proves the complete list and multiplicities without genericity assumptions. Direct Gram multiplication and tridiagonal diagonalization establish the two boundary-rank closed formulas and determinants. The standalone checker agrees with the formula on 21 Green classes across chain lengths 1–6, with direct inverse-equation tests and exact Gram tests. These finite tests are not substituted for the proof. The critical boundary conventions, real-field normalization, and loop inclusion are stated.

## Originality — PASS (qualified)

The central comparison is to Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings* (arXiv:2610.01912v1, October 1, 2026). Its crossed-square formula and transversal interlacing data are prior results. Its main theorems concern existence of permutation matchings, whereas the present claim determines adjacency inertia and the full spectral factorization, with explicit rank-two and rank-codimension-one spectra. Higgins (2024), *Finite regular semigroups with permutations that map elements to inverses*, treats matching existence and obstructions, not spectral inertia. Searches for inverse-relation graph adjacency spectra, tensor-transpose spectra, exact incidence ranks, and chain-isotone inverse graphs found no covering result. Relevant prior finite-rank involution-matching constructions determine *one choice* of mutual inverse for each element, not every entry of the inverse relation, so do not imply this spectrum. Historic-priority uncertainty remains because the factorization uses familiar singular-value and commutation-operator techniques. No claim is made that the 2026 crossed-square construction itself is new.

## Mathematical value — PASS

Permutation-matching existence is the motivating 2026 question. The full symmetric inverse relation behind a matching is a natural canonical semigroup invariant; its spectrum is not determined by the existence of an admissible permutation. The theorem classifies positive, negative, and zero directions exactly in **every** Green rank and proves an unexpectedly uniform rank law \(p^2\) despite highly nonuniform degrees. It also gives explicit eigenvalue formulae, spectral-radius growth \(\sim n^3/\pi^2\), and exact Gram determinants \(n^{n-2}\) and \(n\) in two natural boundary ranks. This is a complete structural family, not a handful of unrelated finite computations. It does not assert the unresolved involutive-matching question for arbitrary ranks.

## Closest literature and residual limits

Higgins 2026, arXiv:2610.01912v1: full primary mathematical text inspected, including the crossed-square definition and the complete interlacing/deletion incidence proof. Higgins 2024 (DOI 10.1007/s00233-024-10430-0): relevant full-text sections covering finite regular semigroup matching theory and open questions inspected. Higgins 2018 (arXiv:1812.03743): title and abstract checked, broader matching context only. Residual risk: an older spectral treatment of tensor-transpose or interlacing incidence matrices may imply part of the factorization under different language. Searches do not constitute a universal priority proof. Computational inspection stops at \(n=6\), while the proof handles all \(n\).

Self-review: passed. Independent audit: not yet performed.
