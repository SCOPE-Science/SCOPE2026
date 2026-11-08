# Scientific review: maximum automorphism groups of simple evolution algebras

## Correctness — PASS

A simple finite-dimensional evolution algebra has an invertible structure matrix, a strongly connected support graph, and monomial automorphisms. The diagonal kernel is injectively determined by its scalar at one vertex. Every closed walk of length \(\ell\) imposes the root condition of order dividing \(2^\ell-1\), so the period \(d\) bounds this kernel by \(2^d-1\). Each graph automorphism induces a common cyclic shift on the \(d\) periodic classes and then at most \(\prod m_i!\) within-class bijections. The combined bound is \(d(2^d-1)(n-d+1)!\). Exact base values at dimensions one through six and an induction for dimensions at least six prove the claimed maximum; explicit cyclic and complete support examples attain both terms. No computational observation replaces the induction.

## Originality — PASS, qualified by historical access

Sriwongsa and Zou (arXiv:2202.01333) already show that perfect evolution algebra automorphisms are monomial and describe maximal diagonal kernels and the cyclic extremal example. Their relevant full HTML sections 2 through 4 were examined. Their Section 4 theorem maximizes the diagonal subgroup, not the full group over all *simple* evolution algebras. Kaygorodov, Martín González and Viruel's survey (arXiv:2610.22248v1, first public October 15, 2026) expressly conjectures the full maximum and reports checking only up to dimension four. The added period-sensitive bound controls diagonal and permutation subgroups together for all dimensions, and proves the conjecture by elementary induction. Searches for exact maximum-order statements and the graph-period combined inequality found no prior covering result. A more general previously published graph-symmetry estimate might nonetheless imply this theorem; priority is not absolutely certified.

## Mathematical value — PASS

A natural quantitative classification invariant is determined exactly for every dimension, proving a published open conjecture without arbitrary parameter restrictions. The period-sensitive inequality also explains structurally why two different examples, cyclic and complete, dominate and why the crossover occurs at dimension six. It is not merely a small finite census or a reformulation of the known maximal diagonal subgroup classification.

## Scope and reproducibility

The result concerns simple complex evolution algebras, not all perfect algebras. `CHECK.py` performs exact integer checks for dimensions up to 100; the proof supplies all-dimensional justification. No independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
