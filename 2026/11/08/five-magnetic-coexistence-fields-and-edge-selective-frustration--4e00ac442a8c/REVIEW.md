# Self-review: Chvátal three-color Potts field census

Opaque finding ID: `4e00ac44-2a8c-4269-b05a-1ed6845481a7`.

## Correctness — PASS

The graph and Hamiltonian are explicitly defined in `RESULT.md`. The delivered verifier uses two distinct exhaustive, bijective representations of all \(3^{12}=531441\) spin assignments. It reproduces each of the thirteen exact minimum monochromatic-bond counts and their multiplicities, and all twenty-four single-defect edge counts. Integer successive sector slopes \((-1,-1,-1,0,0,1,3,3,4,4,4,4)\) are monotone, proving the all-real-field envelope with five crossings and all six open branches. Rational arithmetic gives coexistence degeneracies \(256,504,160,832,929\). The field-independent graph identity was also cross-checked against a standard Chvátal graph generator. No infinite-system conclusion is inferred from finite enumeration.

## Originality — PASS on examined evidence, provisional

Full accessible primary text of Shrock–Xu (arXiv:1009.1182) and Björklund–Husfeldt–Kaski–Koivisto (arXiv:0711.2585), plus graph-specific original-construction citations and a directly relevant color-stability paper, were compared with the precise evaluated claim. Generic graph partition-function and Tutte algorithms permit computation but do not present the explicit Chvátal occupancy energy envelope or exact spatial profile of the unique frustrated bond. Dutton–Brigham (2017), citing earlier graph work, already show the existence of a noncritical Chvátal edge. This existence is NOT claimed as new. The new exact finding is the full \(24\)-edge profile, \(13\)-sector minima and magnetic field diagram. Specific searches for exact constants and aliases, and accessible previous results for other 3-color graph magnets, showed no implication covering these values. No uniqueness claim is based on the search absence alone.

The earliest verifiable full-date focal methodological reference was made public 2007-11-16; Chvátal's 1970 graph article is older, but its exact publication day was not verified and its complete text was inaccessible. Residual originality risk: a historical Chvátal coloring/edge-deletion table or unindexed Potts enumeration may already contain parts of the census.

## Mathematical value — PASS

The graph's minimal triangle-free, degree-four, four-chromatic nature makes it a canonical smallest frustrated three-color Potts cluster. The exact five-field, six-phase finite magnetization profile and the surprising localization obstruction for a uniquely violated bond are natural model characteristics rather than arbitrary slices or a routine small-parameter increment. They form an independently reproducible finite magnetic benchmark and are not implied by the graph's chromatic number alone. The analysis makes no claim of thermodynamic phase transitions or general lattice universality.

## Evidence and remaining limitations

Reproduction: `python3 verify.py` with standard Python 3, alongside `SECTOR_COUNTS.csv` and `EDGE_DEFECT_COUNTS.csv`. Checked primary and reference sources: https://arxiv.org/abs/1009.1182, https://arxiv.org/html/0711.2585v4, https://bica.the-ica.org/Volumes/79/Reprints/m-and-M-small-Reprint.pdf, DOI:10.1016/S0021-9800(70)80057-6, https://mathworld.wolfram.com/ChvatalGraph.html and NetworkX Chvátal documentation. The original 1970 article could not be fully read, and no independent verification of historical priority has been performed.

Self-review: passed. Independent audit: not yet performed.
