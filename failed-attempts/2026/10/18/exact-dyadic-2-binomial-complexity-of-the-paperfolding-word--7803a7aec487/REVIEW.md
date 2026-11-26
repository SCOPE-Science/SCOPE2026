# Independent mathematical audit

## correctness

PASS

For equal lengths, c and omega determine every scattered pair count by [01]=omega-binomial(c,2). Separating absolute even and odd positions gives exactly the two onto interleavings in Proof §1; the inserted 1's have spacing four and the two parity classes differ by m in each positional constant. The length-four table is correct. For m divisible by four, the predecessor outer counts are odd, so the new even-start and odd-start moments have opposite parity, while within each transform the predecessor start parities are separated modulo four. For the central layer the two predecessor moment sets agree, and the images are identical progressions for the two new parities after adjoining the translate by m. This proves the full claim by induction, including k=2. Allouche's theorem confirms the separate 4n ordinary complexity benchmark. Independent exact check: `python /workspace/checks.py 5` counts scattered 01 directly for n=4,...,512 dyadic and compares all claimed conditional layer properties (totals 11,20,37,70,135,264,521,1034). Starts through 8n exhaust these lengths: for a fixed start residue modulo 2n only its single index divisible by n can vary, and four successive representatives realize both values (for odd multiples the bits alternate; for even multiples it reduces to four consecutive paperfolding bits). The theorem for all k rests on induction, not these finite checks.

## originality

FAIL

A distinct indexed result gives the same total, tier sizes and central progression and directly implies the parity refinement. This is equivalent mathematical coverage, not a priority finding against the Oct. 18 frozen record: the matching entry has a Nov. 2 date-key, and derivation/priority is not inferred from the catalog dates.

## value

FAIL

The invariant is well-motivated, but the audited claim supplies no independently needed remaining invariant after the distinct exact classification. The same numerical data follow, and the phase refinement follows immediately from injectivity and reverse-complementation of the indexed templates. The dyadic induction is an alternate proof, not a separately established substantive scientific gain over that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
