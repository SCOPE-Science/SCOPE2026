# Independent mathematical audit

## correctness

PASS

The binary, linear, contiguous setting makes the two length-minus-one factors necessary and sufficient tests for minimality of an absent word. The allowable exponent domain for 01-oriented two-run factors is the union of two anchored rectangles; its nonboundary minimal holes are the two conditional corners. The 10 orientation has a single rectangle and yields the two axis overruns when the other pure run permits them. For three runs the interior exponent either undershoots (both outer runs must be singletons), matches (only the permissible boundary overrun can survive), or overshoots (one of the shortened words remains absent). For four runs in the 01 orientation, a shortened prefix with three runs forces the ones exponent to be b, and a shortened suffix with three runs forces the zeros exponent to be c. The frozen 'respectively' at RESULT.md line 48 reverses these labels, but the earlier factor-shape lemma gives the correct constraints and the stated four-run exclusion. The opposite orientation needs both endpoint runs singleton and yields only 10^c1^b0 with a>=c and d>=b. At five runs one shortened word would have the impossible four-run orientation; at six or more there are too many runs even after shortening. Families 6/7 supply one word if d>=b, and 9/10 supply one otherwise. Beyond that one, families 4, 5 and 8 supply the two strict-comparison indicators and their product, giving the exact factorized excess. I inspected verify.py and VERIFICATION.md; the Python 3 checker tests full sets over finite ranges and is corroboration, not part of the proof. No script was executed.

## originality

FAIL

The whole frozen claim has demonstrable equivalent indexed coverage, not merely a related enumeration algorithm: a distinct record on the same positive four-run linear word prints precisely the same conditional ten families and cardinality. Another distinct entry has the same count and regrouped classification. The stronger indexed claim also gives a generating function and extremal result, neither of which is a distinct contribution in the frozen claim. Both matching entries have later catalog dates than the frozen one; this finding of existing coverage is not a finding of chronological precedence, dependence or authorship.

## value

PASS

A complete symbolic antidictionary for a natural run-compressed family is useful separately from its originality: it classifies all minimal obstructions, treats equality boundaries, and explains a missing excess value, none of which follows merely from running a finite census. This judgment about the mathematical problem does not leave any distinct scientific claim beyond the indexed coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
