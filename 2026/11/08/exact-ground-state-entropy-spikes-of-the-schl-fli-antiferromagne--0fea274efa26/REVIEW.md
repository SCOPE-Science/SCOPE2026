# Scientific review of the Schläfli antiferromagnet ground-state census

## Correctness

PASS. The graph encoding is independently identified by all \((27,16,10,8)\) strongly regular parameters and the known unique-isomorphism-class result. The spectral upper bound \(C(k)\le(2/3)k(27-k)\), cut parity, and a nine-coclique partition prove the exact maximum cut for every cardinality. The resulting concave discrete cut profile yields the five energy branches and four transition fields without computation. Two separately implemented exhaustive integer enumerations verify every one of the \(134,217,728\) spin states and return identical counts by cardinality. The finite verification covers the full stated domain (one fixed graph); it is not an inference from sampling or a claim about other graphs.

## Originality

PASS on material examined, with explicitly limited historical-priority confidence. Brouwer's Schläfli graph description gives the spectrum, maximum cocliques, and nine-coloring. These *do* imply the cut profile and phase boundaries after an elementary spectral calculation and are acknowledged as covering those parts. The claimed additional content is the complete zero-temperature field-resolved **multiplicity** profile, especially the exact critical-field state counts. The primary full texts of Honecker–Schulenburg–Richter (2003) and Schmidt–Richter–Schnack (2005) study different frustrated quantum models, not this classical graph. The Metcalf–Yang (1978) abstract treats infinite square and triangular lattices. Targeted historical, alias, exact-number, and database searches, including published research-index searches, produced no implication covering these graph-specific exact counts. Residual risk: specialist enumerative graph tables could reproduce them under cut-enumerator or independent-triple terminology.

## Mathematical value

PASS. Exact residual ground-state entropy at magnetic transition fields is a natural statistical-mechanical observable, particularly in frustrated systems where degeneracy changes sharply at plateau boundaries. The five noncritical ground-state sectors and their singular multiplicities form a complete physical classification for a canonical \(27\)-vertex symmetric graph. The very large peak \(630,444\) at the first transition is not determined by the spectrum or graph coloring alone; exhaustive counting is mathematically substantive and reproducible. No claim of finite-size critical universality or a bulk phase transition is made.

## Verification and limits

The package's `verify.py` compiles and runs `verify_gray.cpp` and `verify_dp.cpp`, checks the explicit line-model graph and nine-triple construction, and compares all \(28\) exact counts. Both methods passed. The finding depends on exact finite enumeration for degeneracies; human historical-priority review and independent scientific validation have not been performed. A known graph-theoretic cut profile should not be mistaken for a separate priority claim.

Self-review: passed. Independent audit: not yet performed.
