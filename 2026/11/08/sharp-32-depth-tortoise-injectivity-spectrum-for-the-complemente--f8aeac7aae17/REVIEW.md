# Independent mathematical audit

## correctness

PASS

The length-two language of mu(1)=10,mu(0)=11 is exactly {01,10,11}; for q=ceil(log2 n), every length-n factor is in two adjacent q-superblocks, and every allowed ordered pair occurs. This yields an exact, not sampled, factor-language enumeration. Each length-N prefix contains at least floor(N/2)>=k ones for N>=2k; equal T^k images at n>N would imply equal length-N prefix T^k images and then equal original factors, so injectivity propagates. For each k=1..32 the complete threshold.csv row includes N>=2k; fresh independent superblock enumeration at N-1 and N confirmed the factor counts, an exactly one size-two collision before N and no collision at N. The collision proves sharpness and the lemma proves all n>=N; no assertion is extrapolated to k>32. Read pinned RESULT.md, thresholds.csv and verify.py; the independently constructed finite certificate is sufficient for those fixed 32 depths plus the stated infinite length inheritance.

## originality

PASS

Best-of-knowledge original within the precise domain and invariant, based on actual relevant mathematical comparisons; source access limitations and priority risks are retained.

## value

PASS

The first 32 iterative depths for a canonical automatic word produce an exact and sharply delimited all-length injectivity spectrum with substantial jumps at 9,17,33,65,129. Each row is an infinite length statement, not merely a finite prefix count. The distinct complemented-letter dynamics and boundary collision classification constitute useful quantitative stack-sorting data without claiming an unproved all-depth recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
