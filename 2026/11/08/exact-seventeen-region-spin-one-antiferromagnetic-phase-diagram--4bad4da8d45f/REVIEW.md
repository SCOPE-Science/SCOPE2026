# Review of the truncated-tetrahedral spin-one ground-state diagram

## Correctness — PASS

The final claim is a finite twelve-site theorem for spin values \(\{-1,0,1\}\), antiferromagnetic \(J>0\), and independently arbitrary real \(h,D\). The graph has four triangle cliques and six reversal edges. The packaged verifier exhaustively enumerates all \(3^{12}=531441\) states twice, in mathematically different decompositions, and checks equality of the entire exchange/magnetization/occupancy density of states. All ninety-one magnetization/occupancy minima and their multiplicities are verified. Seventy-four rational convex-domination certificates reduce the complete energy envelope to seventeen entries. Seventeen exact strict supporting-field witnesses show that all seventeen are genuinely open regions. The verifier checks the 1577-fold ground-state degeneracy at \((h/J,D/J)=(1,1)\). Every step is an exact finite computation or rational inequality; neither a floating-point hull nor a finite sample of fields is used to prove the final all-parameter result.

## Originality — PASS on examined sources; historical priority remains provisional

The closest same-graph primary text is Coffey–Trugman, arXiv:cond-mat/9206011, including its complete model description, quantum and classical sections, and conclusion. It treats Heisenberg vectors or spin-one-half operators, two bond constants, and correlations, not the discrete vacancy-bearing spin-one Blume–Capel exchange plus independent \(h,D\) parameters. Fytas, arXiv:1011.4780, treats a ferromagnetic triangular lattice and thermal behavior rather than the twelve-vertex frustrated cluster. Krčmár–Gendiar–Nishino, arXiv:1512.09059, concerns twelve spin directions at each square-lattice site, not a twelve-site truncated-tetrahedral graph. These full-model differences exclude direct reductions. Earlier research claims concerning three-color Potts interactions on this graph and spin-one Ising models on other graphs do not imply these values. A searchable published-record comparison found related topology or polytope records, not a matching spin-one ground-state statement. Unindexed or differently named historical cluster tables are an explicit residual risk, so no global uniqueness claim is made.

## Mathematical value — PASS

The complete finite field diagram solves a natural two-control-parameter question for a highly frustrated twelve-site fullerene-proxy graph studied in the physical literature. Unlike a single arbitrary field slice, it captures all seventeen open occupancy/magnetization regions, exhibits vacancy-induced plateaus invisible on the zero-crystal-field line, and identifies a high-multiplicity exact coexistence point of degeneracy \(1577\). The exact sector counts, rational certificates and lightweight reproducible program provide a reference benchmark for finite frustrated spin-one models. No thermodynamic phase transition or direct material prediction is claimed.

## Limitations and comparison risks

No finite-temperature or quantum assertion is established. Uniform coupling and the specified graph are essential. The same-geometry Heisenberg primary source and a misleadingly similar title for a different lattice model were materially inspected; a comprehensive priority guarantee across all unindexed finite-cluster literature is impossible from the available coverage. The independent audit channel is not assessed here.

Self-review: passed. Independent audit: not yet performed.
