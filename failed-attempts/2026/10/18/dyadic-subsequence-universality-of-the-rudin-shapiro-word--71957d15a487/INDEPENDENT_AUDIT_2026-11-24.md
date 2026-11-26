# Independent mathematical audit

## correctness

PASS

Greedy arches give both a witness for universality and an absent word one letter longer (take the successive arch-ending letters and then a letter missing from the remainder). Appending binary digits gives the four-state substitution in the record. The level-four transfer table reproduces the two empty-state counts, the effects of the three incoming states, and the common outgoing state for each block type. Concatenation gives a_(k+1)=a_k+b_k+e_k, b_(k+1)=a_k+b_k+1-e_k and e_(k+1)=1-e_k; solving gives the exact parity correction. Aligned blocks at each scale j>=4 contribute at most one unit of error from 5*2^j/16 even when a symbol is pending. The combined lower scales have length at most 15, so the log bound also covers N<16. Separately, an independent bounded script confirmed the transfer through level 17, compared the two word constructions through length 131072, checked the bound on every prefix through that length and exhaustively compared subsequence universality through length 16. Replay: branches/7abd93d6-5bec-4a48-b94b-8f9bd4a25f3a/independent_check.py. The frozen checker was inspected, not executed; finite checks corroborate rather than replace the induction.

## originality

FAIL

The frozen mathematical claim is covered in the inspected published catalog: the uniform Rudin–Shapiro factor theorem gives the identical dyadic formula and a logarithmic discrepancy bound on the larger domain of all factors, and a separate published record also gives the same dyadic index. There is no distinct result left in the frozen statement relative to that coverage. Both catalog dates are later than the frozen record's date; this is a finding of claim coverage, not an inference that those records were first or that this proof was copied.

## value

PASS

The exact parity correction and the uniform prefix error quantify a natural scattered-subsequence invariant of a classical automatic word. They are not routine consequences of letter frequencies or abelian complexity; the transfer analysis needs control of the state across block boundaries. The result is useful mathematically even though the same claim is now covered by the published catalog.

The dated certificate retains the supplied scientific assessment, sources and limitations.
