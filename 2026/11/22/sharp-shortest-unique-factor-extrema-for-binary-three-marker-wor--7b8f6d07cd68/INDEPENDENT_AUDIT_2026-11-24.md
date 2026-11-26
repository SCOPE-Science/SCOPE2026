# Independent mathematical audit

## correctness

PASS

Factors are contiguous, counted at all positions including overlaps, and the four gaps are nonnegative. In the equal-interior case b=c=t with a,d≤t, zero-only factors are repeated, a unique one-marker factor needs both extra exterior zeros, a unique two-marker factor must extend past one exterior gap, and a three-marker factor includes both interior gaps. These give the common lower bound a+d+3, attained by the four witnesses according as a=t and d=t. If b≠c, the shorter neighboring-pair factor gives ℓ≤min(b,c)+2. For this to reach M=n−2m requires n≡0 mod 4, a=d=0 and gaps 2m−2 and 2m−1; then the longest all-zero factor is unique and has length M−1. If b=c=t and an exterior gap exceeds t, a unique boundary factor has length t+2≤(n+2)/3<M since n−3m>1. In the remaining case t≥ceil((n−3)/4)=m and ℓ=n−2t, with equality exactly at t=m. The endpoint-gap interval is nonempty for n≥5 (0≤n−3−2m≤2m), and counting it gives the displayed small-length counts and eventual 4−(n mod 4). A separate suffix-neighbor computation exhaustively checked the value and complete maximizing set for 58,900 words at lengths 5–35. Replay with python3 -I -B branches/frozen_review_checks.py from /workspace.

## originality

PASS

The distinct claim is the all-length fixed-weight extremum with equality classification, not the definition or general algorithmic computation of a SUS. The closest accessible algorithmic passage and separate fixed-content indexed statements do not supply or mechanically imply this extremal theorem. The assessment is limited to the compared evidence.

## value

PASS

The global SUS is a natural measure of how long a local factor must be to distinguish a location. At weight three the extremal problem is sparse but already has competing adjacent marker-pair matches. The theorem identifies exact worst-case length and an unexpectedly small eventual family of maximizing gap vectors with forced equal interior spacing. This is useful exact structural information not supplied by the ability to compute a SUS for a given word.

The dated certificate retains the supplied scientific assessment, sources and limitations.
