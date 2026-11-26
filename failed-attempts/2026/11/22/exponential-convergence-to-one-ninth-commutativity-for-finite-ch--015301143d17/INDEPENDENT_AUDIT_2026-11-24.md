# Independent mathematical audit

## correctness

PASS

The theorem is correct in the two-sign, arbitrary-subset monoid. A rank-r nonzero translation gives r edges on disjoint arithmetic-progression paths, so equality with a partial identity imposes r independent equalities among the n membership bits. Summing the domains over displacement magnitudes and their two signs gives 2 binom(n,r+1); the binomial sum gives M_n. Empty and singleton maps are correctly counted (at n=1 all maps are idempotent). For fixed small nonzero shifts, the central domain tests use two distinct bits from each of two independent domains, even for equal or opposite displacements. Each test holds with probability 5/8; the conflict graph has at most four neighbors per test, and a disjoint family of size at least (n-4h)/5 gives the stated bound. The large-shift geometric tail, union over the two factors, and exact denominator give the displayed error and conditional concentration. The supplied exact transcript through n=9 was inspected, not rerun; it is not evidence for the rate by itself.

## originality

FAIL

There is demonstrable coverage across distinct indexed results, not merely matching titles or a suspected same-day duplicate. The exact mixed fiber is canonically equivalent to the one-sided crossing census in 3f4afe04e35e. Exponential concentration and the 1/9 law already follow from the raw two-nonidempotent count for the whole monoid in f54b34cb7503. The more closely related full-monoid proof in 2523a33ab907 exhibits the same forest and disjoint Bernoulli-test arguments for translation extensions. The precise finite-n upper bound with h=floor(n/8) is not quoted in those records, but the change of cutoff and of constants in the translation part of the same proof is not a distinct surviving scientific claim. The evidence establishes coverage without inferring chronology among the same-day records.

## value

FAIL

The question and forest interpretation are useful, but after the equivalent mixed census and the covered exponential limit are removed, only a choice of constants in a nonsharp upper bound remains. No natural threshold or application requiring that precise bound is given. A sharper intrinsic count or a proven sharp decay rate would be a different result and is not established here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
