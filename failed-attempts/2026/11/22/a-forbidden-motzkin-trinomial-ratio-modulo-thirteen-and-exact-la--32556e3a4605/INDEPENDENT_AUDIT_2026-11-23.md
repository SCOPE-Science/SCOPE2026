# Independent mathematical audit

## correctness

PASS

The Lucas step is valid because the exponents in the digit polynomial lie in [−d,d] with d<p; its zero-degree term is the only one that can cancel a multiple-of-p exponent. Zero-free digits make all denominators units. The odd prime p=3 is excluded by T₂=3; the last-digit identity thus gives c=±1. At the first nonmaximal digit s above j trailing maximal digits the successive T ratio is c^j v_s, including all-maximal written strings by padding with a zero. Summing p^(−j−1) over the two parities gives the stated masses. Taking X integer and truncating at J=ceil(log_p(X+1)) leaves no actual index with j>J, while the discarded density times X is O(1); each retained cylinder has count error at most one. For R the three offsets cross a digit boundary only for d=p−2,p−1, giving the two stated affine maps; splitting the cutoff by final digit proves the discrepancy. For p=13 an independent calculation used w_d=sum_j binom(d,2j)binom(2j,j) mod 13, and independently formed T(n) mod 13 from its digits and R from (3T(n)+2T(n+1)−T(n+2))/(2T(n)). This reproduced the published F,G,E and all histogram entries for cutoffs 13,169,2197,28561. In particular the limiting numerators are (2,26,2,4,3,24,2,26,26,2,2,0,37); f⁻¹(11)=4 and g⁻¹(11)=6 are absent from the eight carry ratios. At every level L=k−1 each (j,s) cylinder with j<L has 13^(L−j−1) elements, and the unique all-maximal prefix gives U=1. This supplies the all-level proof, not extrapolation from finite computation. The stated blocks are specifically [0,13^k); the theorem does not establish a prefix-independent histogram for arbitrary translated blocks.

## originality

FAIL

Kohen's published Lemmas 1 and 2 already give the all-index classification and full natural-density formula for zeros of arbitrary fixed linear combinations of offsets of a symmetric degree-one constant-term sequence. Each quotient residue is exactly one such zero family: R_p(n)=r iff b_n=(3−2r)T_n+2T_{n+1}−T_{n+2}=0 mod p, since T_n is a unit and p is odd. Taking h=2 and α=(3−2r,2,−1) in those lemmas gives the pointwise rule, image test and density in the submission for every r. The missing 11 and exact densities are a finite specialization of this stronger earlier result, even though they are not tabulated there. The block and cutoff counts require only counting the very same congruence classes already given by the prior proof; no new restriction or carry classification is needed.

## value

FAIL

The quotient is a natural statistic and the omitted ratio is correct, but the exact statement is an immediate finite evaluation of a published general classification of the same zero sets. The power-block correction and logarithmic error use only elementary counting of those known suffix classes. This is a useful illustration of Kohen's lemma, not a surviving independently valuable new finding under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
