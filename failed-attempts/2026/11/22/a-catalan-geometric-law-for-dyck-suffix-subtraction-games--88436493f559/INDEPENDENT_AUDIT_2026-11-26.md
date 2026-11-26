# Independent mathematical audit

## correctness

PASS

Take the longest Dyck suffix and split it at zero returns. Its core cannot itself have a Dyck suffix by concatenation. A legal cut cannot start strictly inside a primitive component because the remainder of that component then has strictly negative net balance, unchanged by later complete components. No cut can start before the maximal suffix. Earlier component counts after a legal deletion cannot acquire extra blocks since reattaching deleted blocks would contradict maximality. Hence the option values are exactly 0,…,k−1 by induction, including the empty word. The primitive series p(z) counts words aDb, and the unique core plus sequence factorization gives B=(1−p)/(1−2z) and F=B/(1−tp). A b-ending core must end at a strict new low: if its final height was visited before, the suffix from the last such visit is Dyck. Reverse these cores and remove their first downstep; the remaining walk is nonpositive, giving the claimed binomial by reflection. Words ending in a contribute 2^(n−1) separately. Minimum component length 2 forces the claimed extremizers and parity, with the empty case handled separately. Under the coupled reversed fair stream, an upstep at zero forbids any longer Dyck extension; each downstep at zero returns almost surely and renews the process. The finite component count stabilizes almost surely to the geometric law with mass 2^(−k−1). Independent bounded replay `python /workspace/review_replay.py 3` used bit-word option searches and mex on 8191 words through length 12, with the length-12 counts 2510,1024,386,130,37,8,1. Supplied checkers and recorded outputs were inspected, not executed; finite checks are not the general proof.

## originality

FAIL

The exact nimber theorem is an immediate restriction of the distinct two-ended Dyck theorem to words starting in b. Its structural decomposition similarly yields the one-sided bivariate generating function and limiting law by conditioning on that initial symbol. The same-date overlap is demonstrable mathematical coverage, not a finding of who had priority or of any copying. The classical Catalan identity, reflection count and iid excursion limit are not separate new claims surviving that coverage.

## value

FAIL

The exact nimber of an infinite word game can be valuable, but here it is inherited wholesale as the zero-left-pile case of the distinct theorem. The GF and limit are a one-letter conditioning and the same Catalan renewal; the sharp extrema, losing count and one-counter description are elementary consequences or restatements of that structure. No independently substantial remaining claim was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
