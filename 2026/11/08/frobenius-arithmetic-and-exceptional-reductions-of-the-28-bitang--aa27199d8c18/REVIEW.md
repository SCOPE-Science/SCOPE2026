# Scientific review: arithmetic of the Fermat-quartic bitangent divisor

## Correctness (C): PASS

The single reviewed claim is the all-odd-characteristic point-count, zeta-function, and exceptional-reduction theorem for the *reduced union* of the \(28\) geometric bitangent lines. The elementary square restriction proves that all listed lines are bitangents, and classical odd theta-characteristics show the explicit list is exhaustive in odd characteristic. All \(378\) line pairs and \(3276\) triples are checked by exact polynomial arithmetic in \(\mathbb Z[t]/(t^4+1)\). The complete set of nonzero determinant norms has odd prime divisors only \(3,5,17\), so checking these exceptional reductions is exhaustive. Direct computation in \(\mathbb F_{p^2}\) fully classifies those exceptional geometric incidences; rational branch counts are determined by Frobenius. The finite-étale normalization identity then yields every field-extension count and zeta factorization. The direct thirteen-prime-field and three quadratic-extension enumeration is a second, separate consistency check and is not treated as an infinite proof. All computations and quantifiers are reproducible using the embedded source files.

## Originality (O): PASS, with historical-priority risk

Janasz--Pokora--Zieliński (arXiv:2308.16514v1, Section 3.2 and Proposition 3.2) already print the \(28\) lines and prove the **complex** \(288\)-double/\(15\)-quadruple incidence pattern; that fact is not new. The available prior computation of splitting behavior of bitangents in the broader Ciani pencil likewise covers the counts of **rational component lines**, not the arithmetic of their reduced union. Betten--Kaplan--Karaoglu's small-field catalogue records \(63\) characteristic-three quadruple points over \(\mathbb F_9\), so that numerical instance is also not new. Dolgachev's discussion of the characteristic-three Hermitian phenomenon does not yield the three-prime classification or the all-extension divisor zeta functions. Searches for finite-field bitangent-union point counts, good-reduction discriminants, and equivalent Frobenius incidence descriptions did not reveal covering results. An unidentified older computation of this specific arithmetic incidence structure remains a genuine priority risk; absence from search results is not uniqueness proof.

## Mathematical value (V): PASS

The rational geometry of a union of nonrational lines is not captured by counting its rational components: rational singularities may have no rational branch. Determining all \(28\)-bitangent divisor point counts is a natural refinement of the published complex incidence table, and the exact set \(\{3,5,17\}\) of odd incidence-degeneration characteristics is a structural arithmetic invariant of its cyclotomic model. The unexpectedly plane-filling reductions over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_9\) are consequences of an all-extension theorem, not isolated small-field experiments. The precise invariant of interest is the Hasse--Weil zeta function of this canonical reduced divisor, for which the finite-étale scissors identity gives a reusable conceptual interpretation.

## Limitations and nearby literature

The theorem does not treat characteristic two, nonreduced bitangent schemes, freeness, fundamental groups, or quartics not projectively equivalent to the Fermat quartic. The two direct programs verify the bounded exhaustive certificate and finite examples but are not an independent mathematical audit. Historical priority is not definitively resolved; the strongest directly relevant published source was read in full in the pertinent section and was found to contain the complex incidence table but not its all-characteristic reduction and Frobenius arithmetic.

Sources: Janasz--Pokora--Zieliński, arXiv:2308.16514v1 (2023-08-31), Section 3.2; Dolgachev, DOI:10.1112/jlms.12905, Section 4; Betten--Kaplan--Karaoglu, *Classification of Quartic Curves Over Small Finite Fields* (2021-10-29).

Self-review: passed. Independent audit: not yet performed.
