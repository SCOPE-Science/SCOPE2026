# Scientific review: Poisson founder-quorum activation thresholds

## Correctness

PASS. The proof explicitly fixes continuous mean-intensity allocation, independent Poisson receipts, integer quorum \(r\ge2\), and finite identical sites. It eliminates unequal positive coordinates through a strict pairwise improvement argument, proves decreasing Poisson-tail elasticity by an absolutely convergent positive-coefficient series, and obtains one adjacent crossing from a strictly decreasing ratio. Interlaced crossing intervals prove all-budget optimality without skipping. The Poisson central limit theorem plus unique crossing proves the Gaussian-quantile asymptotic. A standalone standard-library script passed 15,753 finite diagnostic assertions. No finite experiment is used as an infinite proof.

## Originality

PASS with specific historical-priority risk. A general identical-sigmoid optimization reduction is already known from Srivastava and Bullo's Corollary 5 and is **not claimed as a contribution**. A previously recorded two-founder Poisson habitat theorem already supplies the full \(r=2\) activation staircase (including its large-site-count asymptotic); that case is covered and is not independently new. The new assessment is restricted to the genuine extension to all higher integer founding quorums \(r\ge3\) and, crucially, to the Gaussian-quantile **high-quorum** asymptotic. Inspected external literature and published mathematical results did not establish those general claims. Shea and Possingham study a distinct state-dependent, multi-period biological-control management problem, albeit also with an established-sites objective. Goodsman and Lewis give a spatial founding-threshold formula rather than a release allocation law. Grevstad's and Ağralı–Geunes's accessible abstracts and Ginsberg's bibliographic record are insufficient to exclude similar unexamined historical results; full texts are recorded as unresolved priority risks. A pre-existing numerical exponential root for \((r,m)=(2,1)\) is excluded from any novelty assertion. Failure to retrieve those sources is not evidence of their absence or mathematical noncoverage.

## Value

PASS for the sharp order and asymptotic, not for a generic identical-sigmoid reduction. Although the two-founder case was previously obtained, raising the biological minimum to arbitrary larger quorums changes the Poisson curve and admits a new large-quorum asymptotic regime, rather than merely replacing a numeral in the conclusion. The establishment objective is the number of habitats meeting a founding quorum, a natural measure when a program seeks multiple occupied introduction sites. Instead of requiring comparison of all \(n\) candidate supports at each budget, one knows the exact sequence of \(n-1\) adjacent phase boundaries, strict uniqueness except for two-way boundary ties, and an explicit Gaussian-quantile law for high quorums. These resolve a parameterized qualitative question whose answer is not supplied by the generic equal-positive reduction. Biological interpretation is limited by idealized Poisson founders, common habitat quality, continuous mean effort and absence of post-establishment dynamics.

## Closest literature and residual limits

- The previously recorded two-founder Poisson habitat theorem: entire \(r=2\) staircase, including its large-site asymptotic, is covered; it is not asserted novel.
- Srivastava and Bullo (2014), author full manuscript, §3 and Corollary 5: general identical-sigmoid support reduction, covered baseline rather than the claimed new phase ordering.
- Shea and Possingham (2000), full article methods and results: dynamic biological-control release decisions, partially overlapping motivation but different state, action and mathematical conclusions.
- Grevstad (1999), available abstract only: Allee-type founding threshold and release strategy background; uninspected full text.
- Ağralı and Geunes (2009), abstract only, and Ginsberg (1974), bibliographic/secondary description only: uninspected earlier S-curve resource allocation theorems, potentially important for historical priority.
- Duncan et al. (2014), full article, and Goodsman and Lewis (2016), full article: foundation-size/establishment modeling, not an exact Poisson allocation phase diagram in inspected portions.

Self-review: passed. Independent audit: not yet performed.
