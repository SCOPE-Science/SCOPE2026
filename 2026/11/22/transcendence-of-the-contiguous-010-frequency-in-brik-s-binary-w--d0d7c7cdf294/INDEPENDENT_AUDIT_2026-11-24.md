# Independent mathematical audit

## correctness

PASS

With the stated one-based indexing, deleting the first n letters removes the occurrences starting at 1 through n (even at n=1 all these starts fit in B_n). The suffix 01 makes the join contribute exactly 1-b_{n+1}; the final 1 of the left copy cannot start another occurrence. Dividing the count recurrence by 2^n and summing yields the claimed affine binary series by absolute convergence. Independently, if ell_n=|B_n| and F counts infinite-word starts, the telescoping tail gives F(ell_n)-mu ell_n=O(n), since wholly contained counts differ by at most two. For N=ell_n+h<ell_{n+1}, the repeated suffix identifies F(N)-F(ell_n) with F(n+h)-F(n) up to two starts, so the discrepancy reduces to that at n+h<ell_n plus O(n). Iteration gives O((1+log N)^2), proving the all-prefix limit. The lookahead code loses at most two letters from the matching second copy; for L_n>=5 the coded repetitions contain a 3/2-power with bounded preperiod ratio and strictly increasing block lengths. Lemma 13 of Shallit applies to this binary code. The recurring factor 011 gives infinitely many coded zeros, while every 1^j in the source survives the coding. This excludes eventual periodicity and thus rationality; the nonconstant rational-affine map preserves transcendence. The independent bounded check `python3 /workspace/replay/audit_checks.py 2` (output `/workspace/replay/2.txt`) confirms 18 exact recurrences, 14 block comparisons, and the displayed rounded decimal with a rational tail bound. It does not prove the infinite assertions.

## originality

PASS

The prior factor-frequency theorem covers existence and gives a recurrence from which the numerical identity follows by specialization. Credit those as prior or implied. The supported distinct result is the transcendence of the contiguous 010 frequency: it requires identifying and proving nonperiodicity of the particular digit code, not just invoking transcendence of the symbol-1 frequency.

## value

PASS

The shortest-block correlations are natural here: 00 is forbidden and the remaining two-letter frequencies are fixed by the one-letter marginal and stationarity. The 010 frequency is a genuine additional coordinate. Proving its transcendence rather than just computing it or obtaining an existence theorem gives precise arithmetic information not supplied by the letter result. The application of stammering is standard; retaining usable repetitions while excluding periodicity for the particular coded expansion is the substantive step.

The dated certificate retains the supplied scientific assessment, sources and limitations.
