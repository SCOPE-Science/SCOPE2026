# Scientific review: superposed-successor short cycles

## Correctness — PASS

A proper subset of a prescribed directed cycle decomposes into directed paths, so its probability in one uniformly random linear order is exactly the reciprocal falling factorial of its edge count. Two applications of inclusion–exclusion establish the exact finite-size expectation. For disjoint cycles, every arc-color assignment is feasible except one that makes a cycle monochromatic. Proper assignments yield the leading \(n^{-L}\) term, while multiply colored arcs cost an additional factor of \(n^{-1}\). Families of distinct cycles with overlapping vertices have more arcs than vertices and therefore contribute only \(O(n^{-1})\) to each fixed joint factorial moment. This proves the stated independent-Poisson limit. Exact exhaustive checks for four parameter pairs confirm the finite-size identity, not the infinite theorem.

## Originality — PASS within inspected evidence

The two closely related October 2026 papers by Jeż–Michaliszyn–Witkowski and Michaliszyn–Witkowski treat satisfiability and realization of designated successor relations, rather than probabilities of cycles in their uncolored union. Cohen–Fachini–Körner (2015) treats extremal Hamiltonian-path families separated by short cycles, rather than random independent-path distributions. Frieze (2001) treats union of random permutations with global Hamiltonicity questions, and random-regular-graph Poisson laws apply to different graph ensembles. A previously established two-path reciprocal-edge statistic already covers the length-two case with two orders; the distinct claimed content here is the simultaneous arbitrary-short-length law, exact finite-size formula, and fixed arbitrary number of orders.

A residual priority risk is that an earlier probabilistic treatment of superposed Hamiltonian paths could imply this law without the present terminology. The 2001 article was available via its bibliographic abstract, not inspected in complete text. No claim of independent priority certification is made.

## Mathematical value — PASS

This is a natural exact statistic for the independent finite successor structures motivating recent satisfiability results. It identifies a persistent local first-order signal of the global acyclicity of **each** path: removing monochromatic colored cycles decreases the mean by exactly \(r/k\), unlike a sparse independent-edge model with the same expected degree. The complete joint short-cycle profile and exact finite-size expectation determine the limiting directed-girth distribution and a nontrivial family of first-order limiting probabilities; the result is not merely a small-case count or a renaming of a standard random-regular-graph theorem.

## Limitations

The theorem does not establish an all-sentence first-order limit law, growing-length Poisson approximation, or independence at finite size. Specialist literature could contain an equivalent conditioning or factorial-moment result. Independent mathematical and historical-priority verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
