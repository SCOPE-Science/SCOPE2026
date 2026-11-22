# Independent mathematical audit

## correctness

PASS

With m=n-f even and m>=4, cardinality N(n,f)=n!/(f!2^(m/2)(m/2)!). A one-descent involution swaps two adjacent blocks of length m/2 and fixes the other f positions; there are f+1 such involutions. The published fixed-f single-ascent formula alternatively yields P(local descent)=(n²-f²)/(2n(n-1)) and mean (n²-f²)/(2n). Consequently the exact lower-tail ratio for f versus f+2 is m/((f+2)(f+3)), while the f-stratum has strictly greater mean. If m>(f+2)(f+3), the CDF at one descent reverses and the strict mean excludes dominance the other way. For f=0 the ratio exceeds one exactly when even n>=8; n=2,4,6 CDFs are explicitly checked and show domination. Independently reimplemented recursive involution generation to n=12, exact histograms/CDFs and mean/f+1 checks, plus symbolic rational threshold checks through n=100: 4,949 passed assertions. Independently recomputed all seven listed Git blob entries into the source tree SHA 8a899cd9e19852c0df367e5c9558a634954e86a2, exactly matching assigned tree. Finite enumeration is corroboration; the unrestricted result follows from the class count, structural one-descent classification, mean and ratio.

## originality

FAIL

The new words "stochastic incomparability" do not isolate a new unknown distributional fact. The all-size, all-f, all-descent-count probability law is already given by Gessel–Zhuang (2020) Corollary 5.5, itself equivalent to older Désarménien–Foata/Gessel–Reutenauer formulas. Extracting the t² coefficient immediately gives the f+1 one-descent count. The earlier published fixed-f descent-indicator result gives the mean (n²-f²)/(2n). Their class-size quotient then yields the submitted quadratic reversal and the exact f=0 versus 2 n=8 onset after trivial n=2,4,6 CDF evaluation. This is direct mathematical implication by stronger exact coverage, not merely a title mismatch. Although no prior source explicitly titles the same stochastic-order obstruction, the claimed new theorem is an elementary corollary of those earlier exact facts; originality FAIL under corollary/stronger-coverage rule.

## value

FAIL

The question of whether adding two fixed points stochastically reduces the descent count is natural and the n=8 first reversal is a clear illustration. But this submitted contribution does not supply a new structural probabilistic law or unknown exact invariant: all conditional distributions and the relevant first moments are already determined by earlier papers with the same objects and parameters. The quadratic threshold is the sign of a one-line rational quotient of already known inputs, and the small n comparisons are known-enumerator evaluation. This is an instructive consequence but, as a standalone mathematical finding, falls on the routine specialization/known-data deduction side of the same value standard. Neither correctness nor reproducibility alone establishes new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
