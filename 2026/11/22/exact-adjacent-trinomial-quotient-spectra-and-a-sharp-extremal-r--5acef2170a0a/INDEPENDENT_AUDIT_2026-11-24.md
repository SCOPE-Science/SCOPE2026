# Independent mathematical audit

## correctness

PASS

The exact ratio a/(b+1) and unit status force equal valuations j, with j<r since both a and b+1 are below p^r. Below j Lucas's no-carry criterion forces digits (0,p−1,0). At j the positive digits x of a and y of b+1 give quotient x/y and third digit in [0,p−x−y]; above j the digit triples are unchanged and there are Q_p choices per place. These conditions are sufficient too: the two decisive digit sums coincide, and the carry-free digits ensure n<p^r. This gives the geometric factor and, by stars and bars, the total binom(p+1,3)S_r. On replacing y by p−t, the permutation displacement formula gives N_p=p−1+sum(π(t)−t−1)_+. For multiplier −u other than 1, t=1 witnesses strictness if its representative is at least 3; t=2 witnesses it for representative 2 when p>=5. Away from u=−1, reflection pairs opposite nonzero displacements, giving N_p=(p−1)/2+F(π)/2. Summing crossings over all cuts bounds F by 2m² for m=(p−1)/2; saturation at the middle cut forces the halves to exchange, which then saturates every cut. This implies u stabilizes the lower half, whose sum is −1/8 mod p, so u=1. Direct p=3 gives the tie. In the binary restriction c=0, only x+y<=p matters: every y works at u=−1 and exactly one of each reflected pair works otherwise, so the reversal comparison is correct. My independent bounded Pascal recurrence builds the full trinomial rows modulo p and forms quotients from actual nonzero residues. All tested histograms match, including p=5,r=3 and p=11,r=2.

## originality

PASS

The evidence supports a distinct three-coordinate weighted quotient spectrum and sharp unique reversal; the carry-free criterion, standard cut bound and binomial transfer case are not new. No inspected separate result supplies the ternary weighting and its pair of unique extrema. Identical indexing of the assigned record is not independent evidence; same-day overlap in the two-coordinate case gives no priority conclusion.

## value

PASS

Conditioning on units makes the ratio of neighboring coefficients a natural statistic not fixed by single-entry residue laws. The exact spectrum at every depth and the change from unique most-frequent to unique least-frequent at −1 distinguish adding a third coordinate from merely repeating the binary construction. The weighted finite sum and sharp extrema are useful exact benchmarks for analogous digital transfer laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
