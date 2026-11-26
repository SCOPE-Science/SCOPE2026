# Independent mathematical audit

## correctness

FAIL

The enumerator and deepest-coset formulas are correct. Internal incidence constraints force arm constants, and endpoint incidence enforces even parity. Nearest distance is the sum of local minority weights, except in the absence of a tied block when the preferred parity is odd: then it costs an extra L−2 max(a_i). Tied words and the two untied parity classes yield the displayed polynomial after division by 2^(m−1). For L=2s a no-tie odd word with deficits t_i=s−a_i≥1 has distance ms−sum(t_i)+2min(t_i)<ms; for L=2s+1 equality at ms+1 in the corresponding bound requires every deficit to vanish. An independently written full-word calculation reproduces all four finite spectra, including coefficient vectors (1,8,13,8,2) and (1,12,66,163,189,81) for (4,2) and (4,3); replay: branches/526dd565-1112-495a-a67c-2114b31e85fc/independent_coset_bruteforce.py (output in the corresponding .out file). The correctness defect is in the unrestricted channel corollary and its proof in RESULT.md lines 31–34 and 83: the claim gives no message distribution and the proof assumes all-zero may be sent without loss for any tie rule. At p=1/2, the valid deterministic ML rule always outputting a fixed codeword has conditional success 1 for that word and 0 for the others, whereas the formula gives 1/|C|. The formula is correct for uniformly averaged block success with arbitrary ML tie-breaking, or conditional on any fixed word with translation-equivariant ML syndrome decoding. The missing qualification does not affect the distance distribution.

## originality

FAIL

The separate 2026-10-13 Resultary record bb986fb5af02 already supplies the entire ambient distance spectrum of the identical code for all the same parameters. Its polynomial is exactly 2^(m−1) times the frozen polynomial. This demonstrates equivalent prior catalogue coverage, not a claim about first historical discovery.

## value

FAIL

The complete distance spectrum is a useful invariant of this natural graph code, but this record's purported addition is a constant normalization of a previously available complete spectrum. The conventional qualified channel corollary and the deepest coefficient do not supply an independently substantive remainder. No repair is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
