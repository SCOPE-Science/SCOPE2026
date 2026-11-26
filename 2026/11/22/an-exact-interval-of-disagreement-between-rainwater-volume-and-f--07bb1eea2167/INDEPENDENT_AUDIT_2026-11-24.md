# Independent mathematical audit

## correctness

PASS

Independently reconstruct the full range from frozen RESULT.md lines 7–11. End-of-day storage is always at most 3, so a dry day never meets demand and resets storage to zero. Both six-unit days meet demand. The low-rain day can become the third full day only immediately after a six: if that six is preceded by another six it leaves 3, otherwise the first six leaves 2 (the low-rain day is still ahead and the only remaining predecessor is the dry day). Thus the low-day thresholds are respectively z=1 and z=2; a first or post-dry low day is never full. In 1≤z<2 only (0,6,6,z) and (6,6,z,0) meet three full days. Each spills one unit on the second six; the former retains z−1 at the end and supplies 12, the latter drains on the final dry day and supplies 11+z. In particular the one-unit overflow in both is not a one-unit volume deficit in both. Conservation gives V≤12+z, attained for all z by (6,z,6,0), which has 2 full days before z=2 and 3 thereafter. For z<1 that order also attains the maximum of two full days, including the z=0 duplicate-rain case. This proves the exact window and both endpoint decisions without relying on rational sample points. Replays against frozen RESULT.md lines 13–35; VERIFICATION.md and check.py were inspected, not executed.

## originality

PASS

Two reliability metrics and the yield/spillage timing issue are established, and permutation sensitivity is also known in related storage models. The supported distinction is the exact optimizer-disjointness interval and penalty under this specified empty-start, fixed-demand update. No inspected primary or indexed statement supplies that benchmark directly or via a stronger applicable theorem.

## value

PASS

The practical mathematical question is whether optimizing one standard reliability measure can serve as a proxy for optimizing the other on the same inflow data. This small exact counterexample makes that distinction auditable: it isolates how consecutive wet days trade spillage for a third full day, gives a nondegenerate sharp interval with different decisions at its two boundaries, and quantifies the best penalty. This is useful as an analytical benchmark for dual-criterion implementations and timing conventions, not as an instruction to reorder natural rainfall or a general sizing result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
