# Independent mathematical audit

## correctness

PASS

With r=n−k+1 overlapping linear reads, the t-th offset count is the source sum over [t,t+r−1], so neighboring offset counts differ by w_(t+r)−w_t. Each residue chain with any nonzero difference is fixed by that difference and propagation in both directions. For k>k*, integer rounding gives n≥4r−1, so at most one chain has length three and every other chain has length ≥4 (for r=1 the sole chain has n≥8 sites). A constant chain of at least four sites cannot contain ones, and the remaining weight determines the only possible constant length-three chain. At the claimed boundary, n=hr+b, h=2 or 3, 0≤b<r. In the h=2 branch there are b≥2 valid weight-three phases: n≥4r−5 gives b≥2r−5 for r≥4, and n≥8 gives b≥2 for r=3. For h=3 there are r−b≥2 valid phases since n≤4r−2. A phase change permutes the r read-start residues, so the entire ordered-within-read multiset agrees even though the linear words differ. This proves the last ambiguity, not all smaller lengths. An independent direct enumeration of the 56 weight-three words at n=8 found ambiguities at k=1,2,3,4,6 and injectivity at k=5,7,8, supporting the remark about nonmonotonicity. The two frozen verification ranges are only checks of the proof, not its basis; the uploaded code was read, not run.

## originality

PASS

Supported distinct content is the sharp last collision for linear weight-three words from one exact contiguous read length, together with the stronger offset-marginal sufficiency above that collision. Strongly related contiguous cyclic and weight-two results and fixed-weight results for other deck channels do not give this conclusion under the same assumptions.

## value

PASS

Three markers are a natural fixed-sparsity test for reconstructing a linear word from its contiguous reads. The exact last ambiguous length is useful because smaller read lengths need not behave monotonically. The offset-marginal result is a substantive reduction in required data, and the periodic full-deck witnesses show that the upper guarantee cannot be improved even when the complete ordered contents of all reads are available.

The dated certificate retains the supplied scientific assessment, sources and limitations.
