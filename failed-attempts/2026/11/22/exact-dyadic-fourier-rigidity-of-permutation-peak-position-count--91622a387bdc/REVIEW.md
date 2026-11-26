# Independent mathematical audit

## correctness

PASS

The theorem uses all interior-peak-position profiles with multiplicity and the unnormalized Walsh transform. For prescribed peaks, an adjacent pair makes the event impossible, and maximal chains of peaks two apart force alternating patterns on disjoint windows of independent continuous ranks. Their probabilities are products of E_(2r+1)/(2r+1)!. The tangent differential recurrence divides only by 2r+1, so each probability is in Z_(2). Expanding the character product leaves 1 modulo 2 in Z_(2) after dividing by n!. This proves the exact valuation and rank, including the singleton groups at n=1,2. The sum of all Walsh multipliers is 2^|I_n| f_n(empty)=2^(|I_n|+n-1), since a peak-free permutation decreases up to 1 and then increases. Hence the common gcd has no odd prime factor and has the asserted dyadic part; this does not claim an attained minimum multiplier magnitude. The uploaded checker was inspected, not executed. A separate direct permutation enumeration and integer Walsh transform checked every frequency and the gcd for n=1 through 9; replay: /workspace/branches/cb983fd9-85ae-459d-a9c4-09bca3f58c25/direct_peak_replay.py and direct_replay_n1_9.log in that directory. This is finite corroboration only.

## originality

FAIL

A different indexed Resultary record, e4965c4f4ad5, covers the identical unnormalized all-frequency valuation, nonvanishing and invertibility, on exactly the same profile, including the n=1,2 edge cases. It also establishes singleton sharpness and a determinant valuation. It does not state the exact gcd, but that gcd follows mechanically from its valuation plus the classical peak-free count by the single Walsh row-sum identity. No distinct substantive claim survives. This is a finding of equivalent coverage, not a finding of chronological priority; the record under review is not counted as a duplicate of itself.

## value

FAIL

A structural valuation of the peak-position spectrum would be valuable for explaining invertibility on the Boolean group. That structural theorem is already covered. The only differently stated exact invariant, the gcd, records a one-step consequence of the known valuation and the peak-free count rather than a new obstruction, sharp magnitude, or independent arithmetic classification. No nonroutine surviving value claim is established for this record as a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
