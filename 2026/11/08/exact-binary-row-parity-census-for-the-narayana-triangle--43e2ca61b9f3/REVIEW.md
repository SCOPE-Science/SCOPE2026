# Scientific review

**Correctness — PASS.** The even-row case uses the identity \(N(n,k)=k^{-1}\binom{n-1}{k-1}\binom n{k-1}\) for odd \(k\), Lucas's theorem, and the symmetry \(k\mapsto n+1-k\). The odd-row case reduces parity to two adjacent subset indices and counts the consecutive blocks determined by the terminal binary run. Every dyadic-block multiplicity is then a direct count of independent higher bits. The exact total follows from finite geometric sums. Reproducible finite checks supplement this unrestricted proof.

**Originality — PASS with priority risk.** The publicly accessible OEIS A335965 entry provides a finite list, direct computational definitions, and one special equality statement but not the exact all-row formula or full dyadic-block spectrum. The Eu–Liu–Yeh 2005/2006 article on combinatorial congruences is relevant and is cited by that entry; its abstract names different objects, but its full body was not accessible. Independent searches and available prior research statements did not show coverage of the combined theorem. The unavailable primary full text is a real outstanding priority risk; the absence of a search hit is not a proof of priority.

**Mathematical value — PASS, with narrow scope.** This provides a natural complete classification of the exact odd-entry statistic previously tabulated for a classical Catalan refinement, including the entire spectrum across all dyadic row ranges and an exact cumulative law. The exceptional odd-index dependence on the terminal run of binary ones is structural, not a numerical fit. This is an elementary but unrestricted classification, not a higher-modulus result.

**Closest work and limits.** Eu–Liu–Yeh, doi:10.1111/j.1467-9590.2006.00337.x, and OEIS A335965. No complete claim is made for divisibility by higher powers of two, and historical priority remains qualified by the unavailable article.

Self-review: passed. Independent audit: not yet performed.
