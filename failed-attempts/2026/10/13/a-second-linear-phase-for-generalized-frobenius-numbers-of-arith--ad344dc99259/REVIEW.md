# Independent mathematical audit

## correctness

PASS

For s=y+2z and t=x+y+z, the allowed z are precisely max(0,s−t) through floor(s/2). Sorting by s modulo a gives the finite representation count. At the proposed G the first two rows give h+1 and p−h−1 and all later rows vanish. Each successor below G+a has the unique form G+aj−dv with 1≤v<a and j=ceil(dv/a)≥1; coprimality makes this a bijection with the nonzero offsets. The first two rows give p+j−δ, with δ the second-row saturation correction. If δ>0, the raw third-row count minus δ−j+1 is h−d+j−ceil(v/2)≥0, since d(a−v)/a<(a−v)/2. The nonnegative third-row count therefore supplies any deficit. At G+a the second row gains one entry even at the upper endpoint, giving at least p+1. Adding one a-coin then propagates the bound to every larger integer. The rechecked independent three-coin dynamic program (check_record4.py and check_record4_output.txt) found exactly p at all 30,750 boundaries and at least p+1 at all 1,940,622 successors for odd a≤83; it also found D(74)=8 and D(75),…,D(79)=9 for (5,3), which proves the stated out-of-range example by residue monotonicity. The supplied code and output are recorded corroboration, not an infinite proof or executed in this review.

## originality

FAIL

The frozen mathematical claim is demonstrably covered by distinct indexed results, not by Komatsu–Ying's published first phase. The later-dated Resultary records state exactly the same affine value on d=1 (including the boundary multiplicity), on d≥2 and p≥h+2, and on d≥3 at p=h+1. The remaining corner d=2, p=h+1 follows directly from the inspected first-post-range proof: for odd a it uses only k=−1,0 and the exclusion of higher rows works for every d>0. The sharp affine proof counts exactly p bases before the maximizing threshold, so its overlap includes D(G)=p. Thus no separate affine-phase or exact-boundary claim survives the statement-level coverage check. This finding concerns coverage in the inspected record set; the covering records have later catalogue dates, and this review does not infer that they were antecedents to the frozen work, nor make a priority or authorship ruling.

## value

PASS

Resolving an entire affine phase after the end of the first established phase for a natural generator family, and proving exact attainment, is structurally useful mathematics. The independent value of knowing such a formula is separate from the demonstrated coverage of this frozen claim. The out-of-range example illustrates a real domain restriction but does not alone leave a distinct valuable repaired claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
