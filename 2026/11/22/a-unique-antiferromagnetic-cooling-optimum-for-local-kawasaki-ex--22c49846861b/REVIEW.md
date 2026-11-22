# Self-review

## Correctness — PASS

The detailed proof derives the two hub-energy levels from the Hamiltonian, fixes the per-edge heat-bath rate normalization, and obtains the full, not lumped, generator. Its incidence-matrix singular decomposition uses the Boolean-lattice raising/lowering identity and gives every spectral family; the first nonzero lower eigenvalue is exactly the stated gap, with endpoint-sector exceptions handled separately. The derivative sign and zero-crossing argument proves the unique antiferromagnetic maximum and the monotone ferromagnetic regime, including the balanced case and all size boundaries. Independent full-state numerical diagonalization agrees in 165 finite tests; it is evidence rather than a substitute for the exact proof.

## Originality — PASS on examined evidence

The closest inspected full-length source, Grynberg, *Revisiting Kawasaki dynamics in one dimension* (arXiv:1009.4511), concerns local Kawasaki evolution on one-dimensional chains, not the exact star-family gap and its temperature maximum. Caputo–Liggett–Richthammer (arXiv:0906.1238) give the symmetric interchange spectral comparison but cannot determine the energy-biased rates away from infinite temperature. The more recent bounded-degree Kawasaki mixing results use a different graph and update regime. Direct searches for star Kawasaki spectral gaps, Johnson incidence spectra and temperature-dependent maximizers found no established covering theorem. These searches do not establish universal priority; a less discoverable equivalent formulation remains a real risk. The Boolean-lattice singular-value lemma itself is classical and not claimed new.

## Mathematical value — PASS

An exact finite-temperature optimizing inverse temperature for conservative relaxation is a qualitative, physically interpretable effect absent in the infinite-temperature random-exchange benchmark. The result separates interacting fillings from both dilute endpoints and the balanced flat sector, gives an explicit full-generator answer at all sizes and temperatures, and exhibits a nontrivial finite-size optimum at four leaves. It is an exact natural dynamical classification, not a routine numerical gap recomputation or an unsupported claim of a bulk transition.

## Scope and residual risks

Only continuous-time local heat-bath Kawasaki exchange on Ising stars is treated; global exchanges and general graphs differ. Floating-point checks are limited; the infinite family is proved analytically. Historical-priority search is necessarily incomplete and no independent scientific audit has occurred.

Self-review: passed. Independent audit: not yet performed.
