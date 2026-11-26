# Independent mathematical audit

## correctness

PASS

Moving the leftmost 1 repeatedly deletes the first min(k, total ones) original 1s and appends them. For m<=n-k, if the first m+k original symbols have at least k ones, deleting the first k leaves precisely m prefix symbols; otherwise at least m zeros remain there. This gives the positive-part formula for Q_m. The appended suffix, or the entirely sorted word when fewer than k ones exist, gives the second case. For irrational mechanical factors each prefix count has a unique phase cut c_j. Q_n always jumps at c_n, and a cut c_j with j<n survives exactly when j*alpha>k. No image can recur after a jump because all output prefix counts are nondecreasing in phase. Thus the image count is 2+max(0,n-1-floor(k/alpha)), including k>n where both weight classes are sorted, and the last length of agreement with Abelian complexity is floor(k/alpha)+1.

## originality

FAIL

A distinct indexed finding proves the exact image formula and exact Abelian-agreement cutoff for the same operator and all irrational slopes, n>=1 and k>=2. Its proof uses transformed zero positions and adjacent swaps rather than output prefix counts; this is a different proof of the same claim, not distinct coverage. This is a coverage decision, not a finding about first authorship, priority or dependence.

## value

PASS

The mathematical statement is useful: it answers the motivating Sturmian question for the entire family, identifies the exact transition from the two weight classes to linear growth, and relates all transitions to the slope. The binary finite-word prefix identity is a concise proof device. This intrinsic value does not supply distinct coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
