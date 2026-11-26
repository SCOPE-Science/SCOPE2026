# Independent mathematical audit

## correctness

PASS

The carry/parity state gives a bijection with the accepted positive-step progressions: trailing and internal zero runs are checked at the next one, leading zeros are irrelevant at termination, and the final carries detect overflow. I independently constructed the ten-state matrix and solved the formal system, obtaining the stated rational series and matching direct counts through L=12 (python /workspace/branches/independent_frozen_checks.py 4). The separate induction is global: an odd step hits residue 2 mod 4; an even step allows (n−1)/2 on odd terms or n/4 on even terms, strictly decreasing the step. The witness (1,4,7) and its dilations are valid.

## originality

FAIL

The principal results are mathematically covered by the distinct published fibbinary progression census below, via an exact dyadic affine decomposition. No chronological priority between the two same-day records is inferred. To see the implication, write E for the no-adjacent-ones integers and E_r=E∩[0,2^r). The numbers whose 1-runs are all even are precisely 3m with m∈E: pair consecutive ones within each run from the low end, or use m+2m with no carry. For L≥2, complement the L-bit representation of n∈A. If the ignored padding has even length, all 1-runs in the complement are even, so n=2^L−1−3m with m∈E_{L−1}. If the padding has odd length, delete the most significant one of the complement (subtract 2^{L−1}); the remaining 1-runs are even, so n=2^{L−1}−1−3m with m∈E_{L−2}. Both converses hold; the convention at zero agrees. The two images are disjoint residue classes mod 3, so every 3- or 4-AP in their union stays in one image (otherwise the first three terms use all three residues), and reflection and scaling preserve APs. Thus T_L=A_{L−1}+A_{L−2} for the published census A_r of E. The levels L=0,1 are zero. The published GF and global four-term exclusion give both frozen claims, with length three attained already by the transferred E_2 triple (0,1,2) at L=3. The frozen dilation witness is the same triple (1,4,7) followed by the standard multiplication-by-four closure.

## value

FAIL

The maximal progression problem and exact count are natural, but the frozen result is a second calculation of an exact invariant mechanically obtainable from the published fibbinary theorem. The alternate carry certificate is valid but does not, as stated, provide an independently useful new structural claim beyond the covered conclusions. No repair is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
