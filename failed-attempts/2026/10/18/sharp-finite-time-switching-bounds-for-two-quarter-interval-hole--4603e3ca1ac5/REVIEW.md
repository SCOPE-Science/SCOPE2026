# Independent mathematical audit

## correctness

PASS

Each length-(n+1) cylinder has measure 2^−(n+1), and its word survives exactly when it avoids the designated equal-bit pair at each step. After the first check the sorted terminal counts are (1,2). Thereafter the two updates keep either the smaller or the larger entry and replace the other by the sum. The count is at least n+2, attaining it only when the smaller is always kept (switch the hole); the two entries are bounded respectively by F_(n+1),F_(n+2), with simultaneous equality only when the larger is always kept (repeat the hole). The n=0,1 cases follow directly. For alternation, flipping every second bit converts the restriction to avoiding one directed pair, hence at most one change in the transformed sequence. This gives countably infinitely many eventually period-two survivors and dimension zero. A constant hole gives the Fibonacci subshift, with dimension log(φ)/log(2); removing ambiguous dyadic codings does not change it. The rates then follow from the counts. Independent replay: python -B /workspace/review_replay.py 1 checks all 1,023 schedules through n=9 by applying the map directly to exact dyadic-cylinder midpoints. The all-n claims use induction, not the finite run.

## originality

FAIL

A distinct already-indexed result directly states the same sharp all-schedule finite-time envelopes with both iff equality conditions, and covers the infinite cases. This is a finding of demonstrable coverage in the catalogue, not a finding about first discovery or historical priority: the matching record has a later displayed path date.

## value

FAIL

The sharp optimization is naturally motivated, but the frozen result adds no new exact fact or independently useful remainder to the distinct catalogue result, which gives the same optimization and further implications. The alternate recurrence proof and finite checks do not supply a separate scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
