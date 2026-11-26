# Independent mathematical audit

## correctness

PASS

Prefix closure and the unique nontrivial anti-Lyndon sesquipower representation identify the tail event and partition it by root length. Bernoulli weight is rotation-invariant, giving a factor 1/d on each primitive orbit, and the forced extra letters have exactly the continuation weight in (1). For m=n-d at most L=floor(log n/[4 log(1/p_top)]), d is at least n/2 and the all-top-letter block probability is at least n^(-1/4); using disjoint blocks bounds the absence probability by exp(-c n^(3/4)/log n). Independently of this event, the nonprimitive probability is at most d rho^(d/2), by testing proper repeating divisors. The resulting main sum is a geometric series in p_top, with distant terms bounded by rho^m, and n/(n-m) changes the main sum by O(1/n) using summability of m p_top^m. The summable tail error yields the mean constant and stated variance, and the discrete power tail sum gives the strict threshold at 1. An independently written rotation-orbit/suffix enumeration checked identical word sets and unique roots through length 8 over a ternary alphabet with ordered masses (2,5,1)/8, where the top letter is not modal. At length 8 there were 1318 valid prefixes of mass 4053105/16777216. This does not test the infinite limit. Documentation only: RESULT.md names check_inverse.py and check_fkm.py, but the supplied programs are verify_direct.py and verify_fkm.py, correctly named in VERIFICATION.md. The actual finite checks are inspectable and the proof does not depend on the filenames.

## originality

PASS

Best of knowledge, limited to the fixed, nonuniform Bernoulli first-entry law and its moment consequences. The real ingredients are closely related to established weighted primitive-word probabilities and extremal-letter run analysis, not independently new, and the exact uniform result is already classical. The inspected closest papers do not give the summed, weighted sesquipower tail or its error term.

## value

PASS

The statistic is a canonical entry of an existing word array under a natural random-text model, not the outcome of picking an arbitrary small instance. The result gives a precise distributional scale, identifies the ordered extremal letter rather than the modal letter or the entropy as the controlling parameter, and separates almost-sure finiteness from infinite expectation while giving precise truncation scales. Uniform counting alone cannot answer this source-sensitive question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
