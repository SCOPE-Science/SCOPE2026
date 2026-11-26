# Independent mathematical audit

## correctness

PASS

For even inputs the cubic difference is the input difference times an odd factor, so the even inputs give exactly one root for each even target, at finite levels and in Z_2. All outputs are even. In the odd classes centered at 1 and -1 modulo four, the offset y+2 or y-2 factors as (x-1)^2(x+2) or (x+1)^2(x-2). With x displaced from its center by 2^r u, the nonzero offset has valuation 2r and odd part u^2(a+2^r u), with a=3 or -3. Its fixed unit residues modulo eight are 7,1 at r=2 and 3,5 at r>=3, in sign order. On each class of odd u modulo four the normalized output difference gains exactly one valuation relative to u-v, so each class is bijective onto its specified ball. If the offset is zero modulo 2^k, displacement must be divisible by 2^ceil(k/2), giving 2^floor(k/2) inputs for k>=4. At nonzero offset, m=k-2r<=2 requires only the matching fixed unit, yielding 2^(k-r-1) inputs; otherwise each of two classes contributes 2^(r+1), since units are read modulo 2^(k-r) but the required precision within each class is 2^(m-1). Thus the displayed exponent is exact. In Z_2 the sign branches are disjoint modulo sixteen; each noncenter target therein has two odd roots, each center one. Per sign the noncenter balls have measure sum_(r>=2) 2^(-2r-3)=1/96, yielding 1/48 for three roots, 23/48 for one, and 1/2 for none; the two double-root targets have measure zero. Polynomial evaluation gives a period 2^k, and evaluating a candidate period at n=0 shows it must be divisible by 2^k when k>=2: odd T gives F(T)=2 modulo four, while even T has v2(F(T))=v2(T). Modulo two the function is identically zero, of least period one. An independent direct enumerator matched all fibers for k=4 through 12. The uploaded checker was inspected, not executed. Replay: /workspace/branches/3374c2ce-90c9-4a2b-982f-f399c11ba37f/direct_fiber_crosscheck.py and direct-k12.log in that directory. The mathematical arguments, not finite replay, justify the least periods and actual two-adic root counts.

## originality

FAIL

A different indexed record, 5e7f44cf3ca5, gives the identical finite cubic fibers in square coordinates and proves the actual two-adic coordinate bijections. Those bijections immediately imply the additional two-adic root counts and target balls; Haar measure adds the volumes of those balls. The period formula follows directly from the zero-fiber classification. These statements are not explicitly bundled in the counterpart, but are mechanically implied by its result and proof. This comparison establishes equivalent coverage, not chronological precedence. The same-day date and the unresolved published full text do not drive the verdict.

## value

FAIL

The underlying complete local classification is useful, and distinguishing finite multiplicities from actual two-adic point counts matters. Here, however, the counterpart already supplies the coordinate bijections that settle both. The explicitly appended Haar measures and periods follow by adding known ball measures and testing the known zero fiber, respectively. No genuinely separate remainder adds a nonroutine scientific fact beyond the covered classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
