# Self-review

**Correctness: PASS.** The full covariance expansion and finite-sum identities are algebraic. The proof of strict global optimality of \(B_6\) handles all unbounded integer windows by proving that the positive terms of the consecutive-difference numerator decrease strictly beyond \(m=6\); a finite test list alone would not suffice. Exact rational inequalities certify the local-trap example. Run `python3 verify.py` for supplementary checks.

**Originality: PASS on inspected evidence.** Hartley and Wilson (2023) already introduce and empirically optimize comparison-star temporal binning, including a noise threshold, and that contribution is acknowledged. Their observed-condition pipeline neither states nor implies the exact half-life covariance-model rational threshold across every odd bin. The inspected AR(1) literature and retrieved research records did not imply it. Generic linear shrinkage can be superior but is outside the strictly unit-weight choice set. Historical priority beyond inspected sources is not guaranteed.

**Value: PASS.** This is a sharp global design and reference-inclusion cutoff in an experimentally motivated differential-photometry workflow; at \(\eta=13/4\), local window search can select a detrimental correction. The canonical half-life and strict boxcar/unit-weight assumptions delimit applicability; there is no claim of empirical telescope optimization.

**Closest literature and limits.** Hartley and Wilson, MNRAS 526 (2023), DOI 10.1093/mnras/stad2964, inspected in sections 2.5, 3.2 and results 5; Bergmans et al., Water Resources Research (2005), DOI 10.1029/2004WR003726 for classical AR(1) background; published AR(1) research records in the private provenance. This analytical model neither recalibrates observed photometry nor applies to unrestricted Wiener filters, time-varying atmospheres, or off-centre windows. Independent expert historical checking remains useful.

Self-review: passed. Independent audit: not yet performed.
