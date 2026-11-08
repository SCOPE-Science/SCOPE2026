# Scientific review: magnetic-field Ising-order reversals on a cospectral graph pair

## Correctness — PASS

The two graph definitions are explicit, and each has exactly sixteen vertices, degree six and forty-eight edges. For a subset \(U\) of size \(k\), the cut statistic is \(6k-2e_G(U)\). Two independently coded exhaustive representations—edge-adjacency recurrence and a four-row edge partition—agree on every count of subsets by cardinality and cut size. Both enumerate all \(65536\) states per graph. The difference has exactly thirty-five nonzero integer coefficients, all matching the sixfold binomial factor in `RESULT.md`; direct specialization at zero field matches the established one-variable identity. The remaining proof is analytic: a quadratic in \(s=z^2+z^{-2}\) has two real roots greater than two for antiferromagnetic \(q>1\), and none in the physical domain for ferromagnetic \(0<q<1\). The Boltzmann change of variables, common prefactor, and low-temperature limits were checked explicitly. The scope is finite and no numerical extrapolation is used.

Risk: the exact polynomial is a finite computer-assisted certificate, not a general graph theorem. The two independent finite algorithms, complete loop bounds, and integer arithmetic are included so its crucial coefficient computation is reproducible and inspectable. The analytic proof is independent of sampling.

## Originality — PASS on examined evidence, with residual priority risk

The specific new claim is the **two-variable field-resolved difference** and its exactly two positive-field order reversals for every positive antiferromagnetic coupling and inverse temperature. The earlier zero-field rook-versus-Shrikhande identity is an acknowledged specialization and is not claimed again. An earlier exact rook-graph field diagram supplies only one of the two polynomials; without the Shrikhande field-resolved coefficients, neither the difference factorization nor its crossings follow. The graph pair also has known independence-complex and spectral comparisons, but these do not tabulate the required cuts at every down-spin cardinality.

Primary material checked: Galanis–Štefankovič–Vigoda (arXiv:1203.2226, first 2012-03-10) treats complexity and tree-based transitions in broad two-spin systems; Chelkak–Cimasoni–Kassel (arXiv:1507.08242, first 2015-07-29) develops zero-field graph and surface expansions; Peters–Regts (2019, DOI 10.1112/jlms.12286) studies complex-field zeros across bounded-degree graph classes. Accessible HTML papers were inspected beyond their abstracts, including definitions, main theorems, and pertinent sections, and searched for both specific graph names. Their statements do not provide the ordered comparison for this pair; a general polynomial definition or enumeration procedure is not an explicit evaluated graph-pair identity. A graph catalog for the Shrikhande pair records structure and spectrum, not this bivariate difference.

Risk: an unindexed finite-graph statistical-mechanics table, alternate bivariate graph invariant, or previous unpublished symbolic computation might contain this identity or a stronger equivalent statement. Independent historical-priority examination remains to be done. Negative search results are evidence of noncoverage only in conjunction with the actual theorem scopes examined, not proof of world-wide novelty.

## Mathematical value — PASS

The two graphs form the unique nonisomorphic pair with strongly regular parameters \((16,6,2,2)\). Their matched adjacency spectrum makes them a canonical test case for what spectral data cannot recover about a nonlinear spin partition function. The zero-field ordering was already known to be strict; the newly obtained exact polynomial reveals that **the ordering reverses twice as the field is increased**, at all positive temperatures. The transition fields have rigorously determined low-temperature limits \(J\) and \(3J\), linking a finite-temperature identity to distinct energetic bottlenecks. This is a substantive, physically interpretable separation of field response among cospectral frustrated networks, not a reprint of the zero-field count or a routine change of variables.

The claim is intentionally confined to the sixteen-spin pair. It does not imply a bulk phase transition or a theorem for all strongly regular graphs.

Self-review: passed. Independent audit: not yet performed.
