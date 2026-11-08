# Review: parity-split Ising antiprism ground states

## Correctness

**PASS.** The theorem is restricted to classical uniform nearest-neighbor antiferromagnetic Ising spins on the \(n\)-gonal antiprism for \(n\ge3\), at zero field. Counting frustrated side triangles yields the parity-dependent sharp energy lower bound. Its equality constraints classify even ring alternations and odd one-defect-per-rim states. A prescribed pair of odd-rim defects determines exactly two states, leading to the complete \(M=0,\pm2\) polynomial and the Curie coefficient through a finite-Gibbs variance identity. The standalone verifier supplies 319 independent exact checks (brute force through \(n=9\), transfer matrix through \(n=80\)), not an infinite proof; the face argument supplies the latter.

## Originality

**PASS on examined evidence, provisional priority.** Antiprism-to-squared-cycle equivalence and the finite-range chain model are standard; neither is claimed as new. The most relevant generalized ladder source, Garuchava (arXiv:2511.05948v2), explicitly distinguishes thermodynamic ground-phase analysis from finite-size constraints, and its examined phase descriptions do not supply the all-size spin-resolved enumeration. Dublenych (institutional preprint posted 2012-02-08) studies ground states of an anisotropic triangular lattice by reduction to infinite finite-range chains; its institutional abstract and PDF cover were examined, but the Ukrainian body was not read completely. Published work on stack triangulations and the standard graph database do not cover the same finite cyclic count. Old one-dimensional transfer-matrix tables and the unexamined older full texts are material historical-priority risks. The actual search comparisons and material inspected are recorded in AUDIT.json; no unsearched-source uniqueness is asserted.

## Mathematical value

**PASS.** This exact all-size classification treats a geometrically natural frustrated triangulated network. Cyclic parity determines not merely ground energy but an unexpected four-versus-quadratic degeneracy and a sharp contrast in the zero-temperature finite-volume magnetic response. Its finite-volume specificity is purposeful; it does not claim a thermodynamic phase transition.

## Limitations

Classical, uniform-coupling, zero-field ground-state problem only; no finite-temperature curve, field-phase classification or relaxation theorem. The Curie limit is at each finite volume, and independent scientific validation is absent.

## Closest primary literature

- https://icmp.lviv.ua/en/preprints/2011/11-11u (2012 public listing; triangular Ising lattice and infinite-chain reduction)
- https://arxiv.org/html/2511.05948v2 (generalized triangular ladder and finite-size caveat)
- https://doi.org/10.1016/j.dam.2014.02.016 (different finite triangulation families)
- https://mathworld.wolfram.com/AntiprismGraph.html (graph identity)

Self-review: passed. Independent audit: not yet performed.
