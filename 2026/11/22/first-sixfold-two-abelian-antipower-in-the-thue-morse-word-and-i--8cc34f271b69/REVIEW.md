# Independent mathematical audit

## correctness

PASS

I reconstructed the finite-to-infinite reduction using t_(128q+r)=t_q XOR t_r for 0≤r<128. Every queried window, of length at most 35, lies in the two tiles determined by (t_q,t_(q+1)); each of the four digrams occurs in the first eight letters, so enumerating all 128 start phases per digram is both exhaustive and realizable. I generated the tiles directly by integer bit parity at scale 128 and classified using endpoints and the four digram counts. In the compressed signature the omitted 01 and 10 counts are uniquely determined by adjacent-count total and 01−10=last−first. The computation reproduced all five rows of the factor-count table and M=(2,4,4,4,6); no larger exponent can exist once M+1 is ruled out, since dropping blocks preserves distinctness. At L=5 all six factor signatures appear among the twelve qualifying factors, out of 90 length-30 factors, and the complete twelve spellings and first stated witness agree with the original. For the exact frequency, paired starts at even positions always have unlike symbols, and an odd-start pair has equal symbols precisely when its source pair is unequal. Primitive substitution gives existence of the frequencies, so e=(1−e)/2 for the equal-pair frequency. The two opposite transitions have equal frequency by telescoping, and the two same-symbol frequencies agree because they arise at odd positions from the respective opposite transitions. Thus the digram weights are 1/6,1/3,1/3,1/6. Each factor's frequency is its count over the 128 phases weighted by those source frequencies and divided by 128; at scale 128 each qualifying spelling has integer weight 8 on denominator 768, exactly 1/96. The good spellings are disjoint events at each start, so the density is 12/96=1/8. Replay: python3 /workspace/review_evidence/thue_morse.py; see thue_morse.log. I inspected both supplied certificates without executing them; the audit uses no empirical prefix frequency extrapolation and asserts no larger block lengths or other words.

## originality

PASS

Best-knowledge pass for the exact consecutive-block thresholds and joint census of the twelve qualifying factors and their prevalence. The overall 2-Abelian complexity and Thue–Morse individual-factor frequency machinery are known. In particular the no-seven conclusion at L=5 has a direct prior complexity proof, and the individual frequencies can be mechanically evaluated from known formulas once the spellings have been selected. The distinctive content is the adjacency-constrained selection and resulting threshold and conditional prevalence, not a new frequency law for Thue–Morse factors in general.

## value

PASS

The first block length at which six fully distinguishable adjacent blocks can coexist is a natural contrast with the known number of individually available signatures, which by itself predicts neither consecutivity nor prevalence. The threshold and complete first occurrence layer in this canonical automatic word are precise benchmarks for studying how local profile complexity constrains nearby blocks. The exact 1/8 prevalence measures the selected event, not merely a known single-factor frequency; the five-length scope is tied to the first sixfold event, not a claim about general length spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
