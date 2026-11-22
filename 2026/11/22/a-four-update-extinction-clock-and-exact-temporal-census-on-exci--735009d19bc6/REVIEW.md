# Self-review

## Correctness — PASS
The vertex update is explicitly defined for all \(n\ge3\), including the triangular and four-cycle wraparound cases. Pendant degree one forbids further pendant excitation; the two-neighbour contradiction eliminates all new core excitations at and after time three. The necessary and sufficient five-column core/leaf motif for core excitation at time two is derived from the initial states. Two finite transfer constructions count first-update avoidance and second-update avoidance; their displayed determinants yield the claimed cubic and quintic root-sum formulas. Independent exhaustive graph evolution for \(n=3,4,5,6\), exact characteristic-polynomial calculation and extra transfer checks for \(n\le12\) passed from packaged `VERIFY.py`. The all-size conclusion follows from the local proof, not extrapolation.

## Originality — PASS (best-knowledge comparison)
The 1993 Durrett–Griffeath analysis concerns planar lattice threshold/range phenomena; the 2016-preprinted Gravner–Lyu–Sivakoff arbitrary-graph theorem explicitly studies the threshold-one rule. Published online findings about threshold-two wheels and open ladders concern graphs with genuinely different neighbourhoods, and their quoted cutoffs and populations neither imply nor contain this sunlet first-extinction distribution. Searches for sunlet/corona/pinned-leaf/last-wave aliases and low-degree motif traces found no covering record. The unpublished/unindexed possibility remains real, and accessible web snippets do not justify claims about inaccessible entire papers.

## Value — PASS
Sunlets are a standard unicyclic family with an identical pendant attached to each cycle site; they distinguish local transient amplification from sustained excitation. The result provides a complete natural first-hitting-time classification for every length, rather than a single small numeric cutoff. A local seven-site causal trigger is equivalent to the last extinction layer, leads to two small algebraic transfer spectra, and shows that a very rare finite local event becomes overwhelmingly likely on long rings. This connects topology, refractory dynamics and probabilistic typicality without claiming a general graph theorem.

## Closest literature and residual limits
Durrett and Griffeath (1993), arXiv:patt-sol/9303002, is a historical model source, not a covering sunlet enumeration. Gravner, Lyu and Sivakoff (2018), arXiv:1610.07320, provides a single-contact theory; its hypotheses differ at the threshold. The publicly indexed wheel and ladder studies (links in RESULT.md) do not contain the same graph or stated polynomials. Full text of the latter online records was not accessible, so historical priority is not independently established. All conclusions are restricted to three colours, exact threshold two and synchronous labelled sunlets.

Self-review: passed. Independent audit: not yet performed.
