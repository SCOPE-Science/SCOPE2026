# Scientific review

## Correctness — PASS

An exact two-adic expansion of the EGF isolates even-base terms with valuation \(n+1\). For the adjacent first differences, each of two odd-base interpolation branches has a unique lowest-valuation \(j=3\) difference term, giving \(\nu_2(G_\varepsilon(t)-G_\varepsilon(s))=7+\nu_2(t-s)\). The branches therefore bijectively cover exactly the two balls \(110+128\mathbb Z_2\) and \(114+128\mathbb Z_2\). Combining this bijection with the exact error gives all frequencies, least period and sharp starting index; six directly computed early values and inverse limits give the full image and closure. The independent standard-library verification checked every \(7\le k\le15\) and additional valuation comparisons at higher precision.

## Originality — PASS, with explicit historical coverage and residual risk

Poonen's 1988 Theorems 4–6 determine the minimal period of **Fubini numbers themselves** and the point from which that period is valid; those are not newly claimed. His shift congruence has a constant leading term in the index and that leading term cancels on taking consecutive differences; the result does not yield a one-per-residue classification of gap values or their scaled-isometric two-adic graph. Asgari–Jahangiri's 2017 paper treats \(r\)-Fubini periodicity, also not adjacent-gap fibers. Mező and Barsky treat Fubini periodicity and p-adic congruences. The present finding determines the exact image, one-per-residue law and closure for the **separate natural first-difference sequence**. Semantic searches for same objects and aliases revealed no covering result. Diagana–Maïga's 2017 paper was accessible only by abstract, leaving an explicit historical priority risk. Historical uniqueness has not been certified.

## Value — PASS

First differences of ordered Bell numbers measure the arithmetic growth in the number of weak orderings when one labeled element is added. Their complete output residue distribution is a natural invariant that is not determined by the individual Fubini number periods; first differences can collapse leading periodic increments. The sharp period \(2^{k-6}\), two disjoint residue balls, exact frequencies, and six isolated initial gaps form a complete structural classification at every binary precision, not an isolated small congruence.

## Sources and limitations

B. Poonen, Fibonacci Quarterly 26 (1988), Theorems 4–6; D. Barsky, original 1982/1995-revised preprint, Proposition 1; I. Mező, arXiv:1308.1637, Section 1; A. A. Asgari and M. Jahangiri, arXiv:1701.07276, Sections 1 and 4; OEIS A000670. The 2017 Diagana–Maïga full text was not available; its abstract was read. No assertion of priority beyond this comparison is made. Only modulus \(2^k\), \(k\ge7\), is treated.

Self-review: passed. Independent audit: not yet performed.
