# Independent mathematical audit

## correctness

PASS

Exact binary16 state encoding comprises 15,361 values x=j/2^24 with normal and subnormal significands. Read staged S and once-round U semantics and exact integer grid rounding, and independently regenerated ALL transitions with NumPy half arithmetic for the stage and binary64 for the exact polynomial (numerator <53 significant binary digits). All 15,361 edges per map agreed with the claimed SHA-256 digests; precisely 2,774 edges differ. Independent complete successor traversal reproduced staged basins (5092,2,10267) with period 40 and U basins (15236,8,117) with period 5, and preperiod maxima 83/109. This is exhaustive evidence for these finite maps, not real logistic dynamics or arbitrary hardware expression semantics.

## originality

FAIL

Decisively covered by the previously published SAME-DATE Resultary theorem Three incompatible complete cycle spectra for half-precision logistic dynamics. Its F map is R(R(4x)*R(1-x)), identical to this S on the specified binary16 domain; its H is R(4x(1-x)), identical to U. That full published RESULT.md gives ALL identical cycle periods and basin sizes, common fixed points, maximum preperiods, and the SHA-256 of BOTH complete successor arrays, not merely a qualitative observation. It additionally includes a third expanded evaluation graph. The separate two-evaluation theorem confirms the 15236/8/117 once-rounded H table. Counting the 2774 differing edges is immediately extractable by comparing the fully published F and H maps and is not a separate substantive new invariant. Same-day intra-day precedence is not fully resolved, but claim-vs-prior implication is decisive for scientific originality at audit time.

## value

FAIL

The staged-versus-single-round exact paired classification is already explicitly printed in the complete published three-graph result. The minor additional 2774 Hamming edge count is a cheap deterministic comparison of complete known successor arrays and has no stated independent structural motivation. Reimplementation is correct and useful verification but not a new mathematically valuable finding under the requested value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
