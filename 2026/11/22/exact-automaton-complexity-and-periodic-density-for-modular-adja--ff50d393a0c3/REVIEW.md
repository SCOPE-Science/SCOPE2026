# Scientific review

## Correctness

**PASS.** The principal all-modulus step is the modular Euler-trail realization lemma. It explicitly constructs an integer nonnegative edge multiset with prescribed residues and exact boundary: first choose residues, then correct their integer divergence with nonnegative edge flows in the complete directed graph, finally add \(m\) copies of every edge to guarantee connectivity. This handles nonprime moduli without invalid field-rank assumptions. The induced incidence map has \(q-1\) independent constraints, and the proof exhibits all accessible states, separating suffixes, and a uniform stationary irreducible periodic chain. Independent state-generation and minimization programs match at four parameter pairs. The universal claim rests on proof, not the tests.

## Originality

**PASS against the material inspected; unindexed overlap is a residual risk.** The closest established theoretical notions are \(2\)-abelian equivalence and word-factor frequency distributions. Karhumäki–Saarela–Zamboni (2013), Lemma 2.3, establishes endpoint information associated with exact factor counts but does not state this modular DFA complexity or periodic length-density theorem. Bell–Burnett–Schulz (2026), Theorem 1.1, bounds numbers of factor frequencies in *infinite* words. Puzynina–Schavelev (2026), Theorems 1–2, concern distributions of *letter* Parikh vectors before factors of morphic words. None of those results implies the present exact state minimum by mere specialization. Comparable modular *scattered*-subsequence monitors involve different updates and incidence constraints. The public theorem deliberately claims neither novelty for the standard incidence identity nor novelty for Euler's criterion or the finite Markov-chain convergence theorem.

## Value

**PASS.** Monitoring all local pair frequencies mod \(m\) is a natural finite-memory analogue of factor-frequency and \(2\)-abelian statistics. The formula shows an exact exponential-in-\(q^2\) memory cost, despite the \(q-1\) conservation constraints, for all alphabet sizes and even composite moduli. The accompanying periodic acceptance law describes how a deterministic arithmetic obstruction survives in long uniform random inputs. Both statements help separate contiguous-factor monitoring from previously studied scattered-pair monitoring.

## Limits and residual risks

The result addresses full contiguous length-two counts with a specified identical start/end symbol; arbitrary factor subsets, longer patterns, other graph supports, and nonuniform moduli are outside scope. Literature and database searches do not prove uniqueness of a mathematical theorem; an unindexed equivalent may exist. The finite computational checks supplement but do not independently certify the all-parameter argument.

Self-review: passed. Independent audit: not yet performed.
