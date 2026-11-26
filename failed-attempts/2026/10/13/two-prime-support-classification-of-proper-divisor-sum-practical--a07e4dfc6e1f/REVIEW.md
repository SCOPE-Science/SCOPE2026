# Independent mathematical audit

## correctness

PASS

Divisor multiplicativity gives the displayed F_p(i,j). By the sorted interval criterion, a weight exceeding the previous total plus one leaves that integer missing; otherwise each weight extends the full interval. The small weights exclude a=1 and p>=7, and leave exactly the excluded cases checked for p=3 and p=5. Each of the five base rectangles is complete. In the extension proof each line's last insertion has the largest greedy gap (consecutive gaps differ by the next weight minus twice the current); hence M_R and M_C suffice. Independently rederived the four increment identities using F_p(i,j)=2^i H_j-K_j, including the last column gap H_(b+1)+(a-1)K_(b+1). For b-increments, both exponential coefficients start positive and increase in a; the changes of the numerators in a are positive from the two lower corners and grow with both exponents. The respective lower-corner increments are (29,17) and (82,31); a-increments are positive by the K_j bounds and the proper-divisor lower bound for the added row. Thus the positive base margins propagate for all exponents, not merely tested ones. Fresh direct-divisor corroboration checked five base totals and margins, nine first gaps and 120 bounded triples: python3 /workspace/branches/7f3e37ca-eaa6-4a55-a4f3-1c7106eec84d/record2-independent-check.py. The frozen verifier was read, not executed; its recorded 720 cases and 400 identity checks are finite. Frozen attestation/audit/Lean statuses were not_performed.

## originality

FAIL

Anniek Reuijl's January 2026 Utrecht thesis already proves the full classification for arbitrary two distinct prime factors. Its Theorem 6.11 (printed p. 30; also Theorem 1.9) restricts to 2 and 3 or 2 and 5 and gives exactly the same exponent pairs. This is demonstrated prior theorem coverage, not a missing-source verdict or an inference from a finite table.

## value

FAIL

An all-exponents two-prime classification is mathematically natural, but this Finding recovers an already proved wider theorem with the same boundaries. The new presentation and bounded checks do not supply a distinct useful classification, new application, or a substantiated proof-method contribution; their expository use is not value of the submitted exact finding as independent research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
