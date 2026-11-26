# Independent mathematical audit

## correctness

PASS

Colliding shifted suffixes force complementary feedback bits for states u and u+16. This is sufficient for bijectivity, and checking that the zero state has a 32-element orbit is equivalent to using every length-five window exactly once. The unique zero window gives one root per cycle, with neither reversal nor complement quotiented; primitivity gives 32 distinct traversals each. For the interval recurrence a palindrome omits at least one endpoint if they differ; when they match one can enclose an optimal interior palindrome, and removing the outer pair from any candidate that uses an endpoint bounds its length by the interior optimum plus two. Empty and singleton intervals supply the base cases. An independently written replay at /workspace/branches/c13e1fd2-1bb8-4491-ac22-0524e09b43c5/reproduce.py exhausts 65536 feedback tables, validates distinct windows and all 65536 root values, and agrees byte-for-byte with frozen summary.json (including all 22 supported joint cells, all margins, the optimal-root counts and examples). It also checks both DP values by explicit subsequences through length eight. The cycle-list SHA-256 is e8b5746482780303fec542789b123a2d51a892f460137bb9f8a96c85fec30421. Independent replay uses feedback, not the frozen supplemental Euler-tour DFS, which was inspected but not executed. The reproduced best-root support is 25 through 29, with 76 cycles at 25; the minimum rooted value is 19, so the two deletion bounds are 7 and 13. The frozen code asserts the margins and computes the joint table, rather than asserting every joint cell against a separate hard-coded table; the independent comparison checks the actual supplied artifact.

## originality

FAIL

The October 18 catalogue record 1b65d6c3c2e3 gives the same optimal-root palindrome histogram and the same sharp lower bound on precisely these cycles. Its archived verified exhaustive loop calculates the same palindromic length pp at every one of the 65536 cuts, by both interval DP and LCS. The old CSV saves only the two best-root statistics, not the new tables. Nonetheless all remaining numbers are a mechanical reaggregation of the already computed per-cut quantity: in the very same inner loop count pp and update a minimum, then count the (minimum, existing p) pair at the end of each cycle. No new input, palindrome test, optimization or enumeration is required. This is not a claim that the rooted or worst-root table is printed in the earlier report. The decision rests on exact prior coverage of the headline and the actual archived all-cuts computation, not on the catalogue dates or on the mere availability of a general DP.

## value

FAIL

A census of root sensitivity in the natural order-five family could be useful as a reference. But the headline sharp bound and best-root distribution were already known, and the remaining histograms just change the counters on an existing exhaustive, validated per-root computation. The record shows no substantive new exact investigation or structural insight beyond that reaggregation; independent agreement strengthens reproducibility, not the scientific increment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
