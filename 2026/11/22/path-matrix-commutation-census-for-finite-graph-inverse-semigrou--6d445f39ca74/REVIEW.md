# Review: Path-matrix commutation census for finite graph inverse semigroups

## Correctness — PASS

Every nonzero element of a graph inverse semigroup is uniquely a path pair \(\alpha\beta^{-1}\). In a finite acyclic graph, two different paths with the same terminus cannot be prefix comparable. Therefore every nondiagonal path pair squares to zero. The proof distinguishes three exhaustive commuting cases: one element zero, an idempotent commuting with another element, and two nondiagonal elements with both products zero. It proves two nondiagonal elements cannot commute with a nonzero product. Prefix-compatible path counts give every element centralizer; ordered summation over terminal vertices yields the stated path-matrix polynomial. The diagonal and shared-prefix corrections have been independently re-derived. Direct semigroup multiplication and closed formulas agree on all 1099 tested simple acyclic graphs with one to five vertices and 681 tested bounded multigraphs, including a separate total-pair enumeration. The argument handles parallel edges and isolated vertices. Finite tests alone do not prove the general assertion; the symbolic path bijections do.

## Originality — PASS, with residual historical priority risk

The established literature supplies the normal form, Green-class structure, and commuting criteria for distinct inverse semigroups, but the inspected primary accounts do not state the theorem's full \(|C(a)|\) distribution or vertex path-matrix formula for \(K(E)\). Jones–Lawson (arXiv:1106.3644) establishes the object and product; Mesyan–Mitchell (arXiv:1409.4380) treats other structure. Araújo–Bentz–Konieczny (arXiv:1205.1664) study the full symmetric inverse semigroup, whose commuting criterion does not imply the present whole-graph inverse semigroup census without substantial enumeration. Bardyla (arXiv:1806.09671) establishes individual Brandt Green-class behavior, whereas summing those isolated-class counts cannot recover the nonzero cross-class prefix interactions. Searches for graph-inverse-semigroup commuting pairs, centralizers, commutativity probabilities, path-count matrix formulas, aliases, and broader coverage found no direct statement; failed searches cannot prove novelty. Earlier semigroup-enumeration literature could still contain an unlocated equivalent.

## Value — PASS

The count of ordered commuting pairs and entire element-centralizer-size assignment are natural invariants of finite inverse semigroups. Enumerating the path-pair semigroup requires a potentially exponentially large list of graph paths and quadratic enumeration of ordered pairs. The theorem replaces that enumeration with a path-count matrix computed on the original directed acyclic graph, explains exactly how graph topology affects commutation, and includes multigraphs and isolated vertices. The distinction between zero-product nondiagonal commuting pairs and common-prefix idempotent interactions is structural rather than a case-specific numerical improvement.

## Scope and limitations

Finite directed acyclic multigraphs only; counts include zero and are ordered. None of the finite checker enumerations constitutes proof for unbounded graph size. The result does not classify all higher commuting tuples or graph inverse semigroups with cycles. Unknown historical equivalent coverage remains a priority risk, notwithstanding multiple primary full-text inspections.

Self-review: passed. Independent audit: not yet performed.
