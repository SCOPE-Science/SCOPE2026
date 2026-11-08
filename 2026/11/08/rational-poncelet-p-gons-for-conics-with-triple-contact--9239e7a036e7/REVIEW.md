# Scientific review: rational Poncelet polygons for triple-contact conics

## Correctness — PASS

The result is stated for every odd prime power \(q=p^r\) and every ordered pair of distinct smooth conics of geometric intersection type \((3,1)\). Frobenius fixes the unique triple-contact and residual intersection points; a rational projective normalization is therefore valid. Restriction of conic equations to the standard \(\mathbb P^1\) proves every such pair is projectively equivalent over the base field to \(XZ-Y^2=0\) and \(XZ-Y^2+YZ=0\). For these equations, direct tangent substitution gives the exact incidence flag parameter \(t=-u^2\), \(s=u-u^2\). The geometric Poncelet step is the translation \(u\mapsto u-1\). Translation orbits are the \(\mathbb F_p\)-cosets, and precisely the prime-field coset has repeated vertices. Reversal interchanges distinct nondegenerate cosets \(u+\mathbb F_p\) and \(-u+\mathbb F_p\). This proves the count \((q-p)/(2p)\) without extrapolation. The two independent programs check the polynomial identities and directly enumerate rational flags in representative prime and quadratic extension fields; both return their expected completion markers.

Limitation: finite computational checks do not prove the all-field statement; the normal-form and orbit argument do. The statement expressly excludes the different intersection type \((4)\) and characteristic two.

## Originality — PASS with historical-priority uncertainty

Jow and Liang (arXiv:2112.11770, Theorem 3.1 and Proposition 2.8) establish geometric \(p\)-periodicity for osculating conics and identify the cuspidal incidence correspondence. Those are stronger general geometric statements, but they do not count simple \(\mathbb F_q\)-rational polygons for a fixed pair or give the failure of rational simple polygons over \(\mathbb F_p\). The new claim concerns rational flags, the unique bad translation orbit, and exact reversal quotient, none of which follows from geometric closure alone without additional rational-flag and simplicity analysis.

Hungerbühler and Kusejko (2020) consider nested, mutually disjoint conics in a special diagonal pencil; their period and pair-count results do not apply to intersecting \((3,1)\)-pairs. Radnović and Ragas (arXiv:2511.06347, sections 2–3) enumerate *conic pairs* satisfying geometric triangle/tetragon conditions, expressly using algebraic-closure periodicity; their framework does not enumerate fully rational simple polygons for a fixed triple-contact pair. Chipalkatti (arXiv:1604.00436) assumes transverse intersection. Semantic mathematical-record searches and the accessible historical claim ledger produced no implication of the exact finite-field polygon-count theorem. An older equivalent finite-geometric treatment under other terminology remains a residual historical-priority risk.

## Mathematical value — PASS

For an entire geometric projective-equivalence class of pairs of smooth conics, the theorem gives a uniform arithmetic count for all finite extensions in odd characteristic, including a sharp prime-field nonexistence phenomenon despite geometric Poncelet periodicity. It separates geometric closure from the existence of a simple rational configuration, identifies the exact arithmetic obstruction, and classifies all rational simple polygons. This is a natural enumeration problem arising directly from the established geometric porism, not an arbitrary parameter slice or a finite experiment. No claim is made about other contact types or arbitrary conic pencils.

Self-review: passed. Independent audit: not yet performed.
