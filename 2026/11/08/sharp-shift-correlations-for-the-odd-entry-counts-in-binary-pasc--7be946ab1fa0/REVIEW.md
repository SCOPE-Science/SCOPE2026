# Scientific review

## Correctness — PASS

The underlying binary row-count identity is classical. For the new claim, the proof enumerates both input digits and both carry states; the resulting two integer matrices give an exact finite cyclic cross-sum, including the outgoing-carry discard at the cyclic boundary. Exact marginal moments give the stated Pearson normalization. The dominant eigenvector limit gives the rational all-lag formula. The componentwise strict comparison \(T_1v<5v\) in its first coordinate, propagated by nonnegative matrices with positive \((0,0)\) entries, gives both the global upper bound and *all* equality cases. A separate matrix with trace \(24\) and determinant \(100\) yields the alternating-shift recurrence and decay to zero. The attached checker was executed on its actual file and independently compared every finite lag up to level eleven. These checks are evidence for arithmetic accuracy, not a substitute for the unrestricted proof.

## Originality — PASS, historically qualified

The 2010 Rowland source and earlier Glaisher/Fine theorems cover the marginal row count, not its shifted Pearson correlations. Full introductory and theorem-level material from Spiegelhofer's 2014 thesis, including the nearby Kummer/Pascal-row discussion, concerns densities of digit-sum *differences* and unit-circle-weight correlations; it does not provide the stated growing weighted joint-product normalization or sharp extrema. Full introductory/theorem sections of Emme–Prikhod'Ko (2015) and Emme–Hubert (2016) likewise study the distribution of \(s_2(n+h)-s_2(n)\), rather than Pearson correlations of \(2^{s_2(n)}\). The comparison is of precise statements and implication, not merely titles. There is residual priority risk from unlocated general weighted digit-correlation theory; failed searches are not proof of global novelty. No exact matching claim was found in the available published-record and archival comparisons.

## Mathematical value — PASS

The problem is the dependence between naturally adjacent or shifted row-count invariants in Pascal's triangle, beyond the classical marginal count. The theorem resolves *all* fixed integer shifts at once, not a single routine example, and classifies both the sharp global correlation extrema and the exact extremizers. The contrast between isolated-bit maximal shifts and alternating-bit vanishing shifts exposes arithmetic carry structure of the whole sequence. The method is elementary but the complete sharp profile is a motivated exact invariant.

## Closest literature and limits

Rowland, arXiv:1001.1783 (2010, historical row-count background); Spiegelhofer, *Correlations for numeration systems* (2014, Chapter 2, related shifted digital correlations); Emme and Prikhod'Ko, arXiv:1504.01701; Emme and Hubert, arXiv:1605.06297 and arXiv:1810.11234 (digit-sum-difference laws). The result is only for binary Pascal rows, with dyadic cyclic normalization and fixed shifts. The possibility of an unlocated result treating unbounded positive digit weights remains a historical-priority risk; external independent mathematical review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
