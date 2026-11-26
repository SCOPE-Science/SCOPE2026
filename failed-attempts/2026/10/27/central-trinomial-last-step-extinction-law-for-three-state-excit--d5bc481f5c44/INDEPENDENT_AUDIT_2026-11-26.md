# Independent mathematical audit

## correctness

PASS

For the stated synchronous three-state rule on open labelled paths (n>=2), the oriented 01-minus-10 edge indicator changes in an update by the difference of the two 0-to-1 firing indicators. The closed-neighborhood maximum consequently propagates the integrated height, or equivalently the firing-count recurrence in the proof. On a tree the walk integral is its endpoint path integral; at t=n-1 the only potentially new paths of that length are the two endpoint paths. A firing at that time is necessary and sufficient for first rest at n+1. The two endpoint events are disjoint strict terminal extrema. Symbol exchange alone takes the right-endpoint event to positive prefixes; reverse and exchange takes the left-endpoint event to positive prefixes. Thus the wording suggesting one identical operation for both events should be read with the preceding reflection argument. Each positive-prefix word starts 01, and 01 followed only by 2s shows sharpness at every length. To check the kernel solution, subtract U=1/(1-3z) from each continuation series and use the small root rho of z^3*rho^2-(1-3z+2z^3)*rho+z^3=0. The correction for final letter 0 at height h is -U*rho^h and for final letter 1 is -U*rho^(h-1)*[z(1-z)+z^2*rho]/(1-2z); eliminating the final-letter-2 series verifies the recurrences and the boundary. Their coefficients are unique by length. This gives the stated square root, trinomial sum and dominant singular coefficient 2/(3*sqrt(3)). A separate synchronous simulation over all words for n=2..8 gave sharp counts 2,4,10,26,70,192,534, each twice the separately counted positive-prefix population. The frozen package's verify.py and verification_output.txt describe further bounded checks; the supplied script was inspected, not executed. The finite reproduction does not prove the general formula.

## originality

FAIL

A distinct indexed record, A square-root law for maximal extinction times in three-state excitation on finite paths, explicitly gives the same sharp time, counts, generating function and asymptotic under identical open-boundary dynamics, with the additional n=1 case. This is duplicate coverage at review, not evidence of earlier priority: the comparator is dated 2026-11-08 UTC, later than the assigned record's dated path. OEIS establishes much older coverage of the pure integer sequence and its formula, not by itself the dynamical interpretation.

## value

FAIL

The exact sharp-time stratum is a meaningful dynamical invariant, but the assigned record adds no distinct result beyond the already indexed dynamical statement. Its alternative consecutive-trinomial expression is the known sequence identity applied to that same series.

The dated certificate retains the supplied scientific assessment, sources and limitations.
