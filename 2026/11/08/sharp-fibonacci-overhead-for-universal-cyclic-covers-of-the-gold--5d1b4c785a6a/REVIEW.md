# Research review: Fibonacci overhead for constrained cyclic covers

## Correctness — PASS

The admissible graph consists of **all linear** \(11\)-free length-\(n\) factors, not just those whose individual periodic repetitions avoid \(11\). It is strongly connected for all \(n\ge2\). The total potential drop of the mandatory edges is \(-(F_n-1)\), and each extra edge can make up at most one unit; the explicitly duplicated \(0u0\) edges are balanced and realize this bound. The proof covers \(n=2\) using the empty-sum convention. Standalone verification and exhaustive small cases check the relevant identities but are not substituted for the general proof.

## Originality — PASS, with documented residual risk

Moreno–Matamala (arXiv:0711.1695, Sections 2.1–3) explicitly work with a different, periodically admissible factor set and minimize lexicographic order rather than length with repetitions. Their length-three golden-mean set has four periodic words whereas the present target requires five linear words. Bernardini et al. (CPM 2022, Sections 1–2) treat general de Bruijn Eulerian extensions algorithmically without the stated Fibonacci closed form or explicit potential certificate. Existing mathematical-record searches for golden-mean shortest covering cycles, alternative terminology, de Bruijn edge augmentation, Fibonacci sequences, and restricted universal cycles did not return the exact formula; closely named results concern other word languages, other covering constraints, or existence/lexicographic universality. General algorithms can solve an instance but do not state this symbolic all-length result. Full text of Cazaux–Rivals (2016) was inaccessible; unseen specialized instances and historical tables remain genuine priority risks. These limitations do not constitute evidence of coverage.

## Value — PASS

A shortest constrained universal cyclic sequence is a natural extremal object for testing finite-state encoders and complete-pattern sampling under an adjacent-one prohibition. The theorem gives the exact irreducible overhead relative to the \(F_{n+2}\) required patterns, along with a constructive optimal multiplicity schedule and a matching lower-bound potential for every block length. The nonzero overhead is structurally forced by the difference between linear admissibility and periodic admissibility, not an arbitrary small parameter calculation.

Self-review: passed. Independent audit: not yet performed.
