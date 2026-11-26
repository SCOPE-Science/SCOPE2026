# Independent mathematical audit

## correctness

PASS

The fixed-width signed-digit correspondence includes n=0, and reversal gives E_r(t)=D(2^r+1)-D(2^r-t+1). For r>=8 the extra full endpoint D(2^r+1) is internal to the Stern range, and dropping D(0) loses no value because D(1)=D(0). The binary pair transitions concatenate two ordered blocks; the second block's prefix sums are translated by the first block's total. Independently recomputed all 24 TSV rows using two-bit concatenation: S_5=S_1, U_28=U_16-4, V_28=V_16+4. The total-vector equality propagates by the linear update, and its induced 12-step periodicity makes the min/max updates propagate the constant shifts at all r>=16. Checked each remaining root case r=8..15. Independent signed-digit polynomial convolution mod 5 matched the initial table and sharp r=7 failure (maxima 4 and 9 at widths 7 and 19). The replay is `python3 /workspace/branches/frozen_replay.py 4`.

## originality

FAIL

A distinct 2026-10-25 UTC Resultary entry states exactly the same Stern extrema, both shifts by four after twelve depths for every r>=8, and the same twelve base pairs, using the same finite-state induction. The remaining signed-digit presentation is the direct reversal and endpoint adjustment of those extrema through Monroe's published correspondence. Its specific B table and sharp starting index are consequences of the earlier Stern data/recurrence, not a distinct drift theorem.

## value

FAIL

Resolving the Stern mod-five discrepancy would be worthwhile, but that exact resolution is already documented. The surviving fixed-width formulation is a direct index reversal using a known correspondence, and its table and onset add no independently useful unknown invariant beyond the prior exact recurrence and small endpoint calculation. A second certificate does not supply another finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
