# Universal failure of summatory superadditivity for nonextremal binary blocks

## Finding
For every integer \(h\ge3\), each length-\(h\) binary word beginning with \(1\) other than the extremal words \(10^{h-1}\) and \(1^h\) has a summatory occurrence-counting function that is **not superadditive**. Indeed, if \(H=2^h\) and \(v\) is the word's integer value, then for \(H/2<v<H-1\), setting \(m=v+1\), \(n=H+v+1\) gives
\[
F_w(m)=1,\qquad F_w(n)=4,\qquad F_w(m+n)=4.
\]
Thus \(F_w(m+n)-F_w(m)-F_w(n)=-1\). The theorem eliminates \(2^{h-1}-2\) of the \(2^{h-1}\) length-\(h\) words beginning with \(1\) as candidates for a universal Graham-style superadditivity inequality.

## Assumptions and scope
A binary expansion is canonical (no leading zeros); the expansion of zero is the one-digit word \(0\). Let \(c_w(t)\) be the number of overlapping occurrences of the word \(w\) in the expansion of nonnegative integer \(t\), and define \(F_w(N)=\sum_{t=0}^{N-1}c_w(t)\), with \(F_w(0)=0\).

Fix \(h\ge3\), \(H=2^h\), and an integer \(v\) with \(H/2<v<H-1\). Let \(w\) be its unique length-\(h\) expansion. This leading-one assumption means that an occurrence at bit position \(j\ge0\) of \(t\) is equivalent to the exact low-to-high bit window condition \(\lfloor t/2^j\rfloor\bmod H=v\). No leading-zero convention enters.

## Proof
**Occurrence intervals.** For each \(j\ge0\), the integers whose digit window at position \(j\) is \(w\) are exactly the disjoint intervals
\[
I_{j,q}=\big[2^j(Hq+v),\;2^j(Hq+v+1)-1\big]\cap\mathbb Z,
\qquad q=0,1,2,\ldots.
\]
Each \(t\) contributes one occurrence for every interval \(I_{j,q}\) containing it. Consequently \(F_w(N)\) counts, with multiplicity, all such interval elements less than \(N\).

Put \(m=v+1\) and \(n=H+v+1\). Since \(H/2+1\le v\le H-2\) and \(H\ge8\), we can count without overlaps being confused with multiple windows.

For \(N=m\), exactly \(t=v\) from \(I_{0,0}\) is below \(N\). The next offset-zero occurrence is \(H+v\), whereas the first offset-one occurrence is \(2v\ge m\); for offsets \(j\ge2\) the initial occurrence is at least \(4v\). Thus \(F_w(m)=1\).

For \(N=n\), the offset-zero intervals contribute exactly \(t=v,H+v\), and the offset-one interval \(I_{1,0}\) contributes exactly \(t=2v,2v+1\) because \(2v+2\le H+v+1=n\). The next offset-one interval begins at \(2(H+v)>n\). For \(j\ge2\), the first possible occurrence is at \(4v\ge n\), using \(v\ge H/2+1\). Hence \(F_w(n)=4\).

Finally let \(N=m+n=H+2v+2\). The offset-zero intervals again contribute exactly \(t=v,H+v\), since the next start \(2H+v\ge N\) follows from \(v\le H-2\). The offset-one window again contributes exactly \(t=2v,2v+1\); its next start \(2H+2v>N\) follows from \(H>2\). All offset-\(j\) intervals with \(j\ge2\) start at or above \(4v\ge N\), by \(v\ge H/2+1\). Therefore \(F_w(m+n)=4\).

Subtracting the three exact values produces the claimed defect \(-1\) for every integer \(h\ge3\) and every strict interior word \(w\). There are exactly \(2^{h-1}-2\) such words. The two omitted endpoints correspond to \(v=H/2\) and \(v=H-1\), where the bounding inequalities excluding extra occurrences no longer apply. This proof asserts no behavior for them.

## Verification
The Python 3 script `verify.py` implements two independent definitions of \(c_w\): a direct canonical-string substring count and a bit-shift/modulus count. It checks their equality and the exact three summatory identities for every interior word with lengths \(3\le h\le10\). It is supplemental finite verification; the preceding interval proof covers all lengths.

Run `python3 verify.py`; the expected last line is `PASS all nonextremal words of lengths 3..10`.

## Relationship to prior work
Sobolewski and Spiegelhofer, *Block occurrences in the binary expansion* (first posted 31 August 2023, arXiv:2309.00142v1), study the arithmetic of binary block-counting under addition and provide the primary number-theoretic motivation. Their main central-limit theorem concerns the distribution of \(c_{11}(t+s)-c_{11}(t)\), not the superadditivity of the summatory functions for arbitrary words.

Allouche and Stipulanti, *Summing the sum of digits* (arXiv:2311.16806, first posted 28 November 2023), explicitly ask whether analogues of Graham-type sum-of-digits inequalities hold for other block-counting functions. The present result gives a uniform negative obstruction for every strictly interior leading-one binary word. A separately published result on summatory all-one blocks gives a positive statement for the endpoint \(1^h\); it does not cover the interior obstruction. Work by Sobolewski in arXiv:2412.15851 (first posted 20 December 2024) establishes Gaussian laws for individual block-count changes, which have different quantifiers and do not force the claimed finite exact failures.

## Limitations
This is a negative theorem for all strict interior leading-one words, not a classification for all binary words. In particular it does not prove or disprove superadditivity for the exceptional word \(10^{h-1}\), and it does not address leading-zero words, whose occurrence convention requires care. The verifier only tests finite lengths; the theorem relies on the exact interval argument. The literature search does not prove global uniqueness, and an unindexed equivalent obstruction is a residual originality risk.

## References
1. B. Sobolewski and L. Spiegelhofer, *Block occurrences in the binary expansion*, arXiv:2309.00142v1 (2023). https://arxiv.org/abs/2309.00142
2. J.-P. Allouche and M. Stipulanti, *Summing the sum of digits*, arXiv:2311.16806 (2023). https://arxiv.org/abs/2311.16806
3. B. Sobolewski, *On the behavior of binary block-counting functions under addition*, arXiv:2412.15851 (2024). https://arxiv.org/abs/2412.15851
