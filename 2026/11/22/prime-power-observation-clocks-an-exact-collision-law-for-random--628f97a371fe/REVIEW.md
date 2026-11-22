# Mathematical review

## Correctness — PASS

The central reduction follows from the exact identity \((I-S)^{p^a}=I-S^{p^a}\), not a heuristic finite simulation. On each residue class the kernel consists of sequences with vanishing \(\ell\)-th difference, and evaluations at up to \(p\) distinct positions have Vandermonde rank \(\min(c_r,\ell)\) because \(\ell\le p\). The bilateral recurrence proves surjectivity, turning the kernel trace calculation into a statement about **all target configurations and all observed symbol patterns**. Exact finite generating functions enumerate subsets without replacement, and factorial moments plus a high-occupancy tail yield the Poisson and sharp-threshold assertions. The included independent test script checks 7,080 finite rank instances and all small-subset enumerators. Tests do not establish the infinite proof; the mathematical steps above do.

## Originality — PASS within inspected evidence

The closest primary paper, Haugland et al., *Locally eventually onto cellular automata* (arXiv:2610.33131v1, especially Section 5, Theorem 5.4, and appendix), provides qualitative criteria and finite tests for eventual onto behavior. It neither computes the all-subset modular-rank profile nor the sampled-covering clock. Henze's generalized birthday result concerns independent placements and their multiple-occupancy Poisson limit, so the probabilistic mechanism is credited, not represented as an original occupancy theorem. Quantitative results for regular arithmetic-progression cylinder supports and two-block supports cover different geometries and do not imply the arbitrary-subset identity. Searches for equivalent finite-field interpolation formulations, stronger general linear-automaton rank results, exact databases, and prior implications found no directly covering statement in inspected evidence. A finite search cannot establish global historical priority; prior coding-theory or occupancy equivalents remain a live risk.

## Value — PASS

The question quantifies a natural invariant underlying locally eventually onto dynamics: how quickly a cylinder with randomly and irregularly placed observations loses **every** constraint on its image. The answer is a full finite-size clock law for every support size, a rank deficiency distribution (not just a probability of success), and a hierarchy of sharp transition exponents with explicit Poisson parameters. This distinguishes geometric observation collisions from deterministic block-length bounds, providing structural information and finite-time design guidance unavailable from the qualitative existence theorem.

## Sources and limitations

Primary source: https://arxiv.org/abs/2610.33131 (first public October 23, 2026). Classical occupancy comparator: https://publikationen.bibliothek.kit.edu/16098 (full text not inspected; repository abstract read). The scope is fixed prime, the two-sided difference rule, bounded-capacity random supports in a prime-power window, and sampled multiples of the prime power. No assertion addresses all integer iterate times or nonlinear rules. Independent audit has not been undertaken.

Self-review: passed. Independent audit: not yet performed.
