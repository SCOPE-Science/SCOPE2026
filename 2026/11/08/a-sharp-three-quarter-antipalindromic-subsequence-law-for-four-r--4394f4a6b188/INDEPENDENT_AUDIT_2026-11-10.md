# Independent mathematical audit

## correctness

PASS

An even-length binary antipalindrome has 2 or 4 output runs when extracted from a rotation of a positive four-run circle (at most five source runs). Two-run outputs produce four bounds from one same-symbol run versus up to both opposite-symbol runs; four-run outputs give two opposite-end matching bounds. Therefore exact six-term formula 2max[min(a,b+d),min(c,b+d),min(b,a+c),min(d,a+c),min(a,d)+min(b,c),min(a,b)+min(c,d)]. For a+c=b+d=N, algebra yields max half-length (N+u+v)/2,N-u,N-v with u=|a-b|,v=|a+b-N|; contradiction inequalities force ≥N-floor(N/4), attained by explicit profiles, with four equality cases if 4|N. Independently computed cyclic dynamic-programming longest antipalindromic subsequences for 81 profiles 1≤a,b,c,d≤3: every case matched; finite examples corroborate, do not establish unbounded claim.

## originality

PASS

Müllner–Ryzhikov 2019 treat antipalindromic circular subsequences and the general 2/3 conjecture, but their inspected full-text sections do not include the six-term four-run length law or sharp balanced extremizers. Generic cyclic LCS algorithms can compute any supplied finite instance but do not imply an explicit all-length extremal characterization without further mathematics. Resultary searches found adjacent four-run combinatorics but not this antipalindrome theorem. PASS with unindexed restricted-family risk.

## value

PASS

A sharp extremal theorem for a natural four-run subfamily of the circular antipalindromic subsequence problem, with a complete length formula and extremizer classification. It gives a constructive 3/4 threshold above the previously studied unrestricted 2/3 benchmark without claiming the unrestricted conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
