# Independent mathematical audit

## correctness

PASS

For residue r, any representation ua+vb has v congruent to tau_r modulo a, hence v>=tau_r for its least nonnegative lift. Thus tau_r b is the minimum, and the membership threshold at heights j is k_r=f_q(tau_r)=q tau_r+floor(d tau_r/a). Every gap block is between consecutive multiples of a, and its two boundary positions must be nongaps. With k_0=k_a=0 (the right endpoint is the next multiple of a), a window beginning at residue r contributes exactly max(0,min k_inside−max k_boundary) heights, with no overlap among maximal runs. Strict monotonicity of f_q for q>=1 makes eligibility independent of q and yields the two nonnegative coefficients. For length a−1 there is one window with minimum rank 1 and boundary rank 0, giving count q even for a=2. An independent way to check the (8,3) example is to start with occupied residues {0,8} and insert 3,6,1,4,7,2,5 in turn; each row's run polynomial persists for q+floor(3(t+1)/8)−floor(3t/8) heights after t insertions. The added floor increments occur after t=2 and 5, contributing respectively z+2z² and 2z, while summing the seven row polynomials gives 9z+4z²+z⁴+z⁷. The genus and exact frequency identities thus have a uniform proof, not an inference from finite tests.

## originality

PASS

The new scope supported by the comparison is the simultaneous all-residue, all-length affine frequency law, explicit coefficients and invariant length support, not fixed-instance computability or the maximal length. Moree gives membership-transition data, the maximum length and an affine total count. Singh–Ram give the isolated-gap count and its underlying gaps. The same-day binary-cyclotomic spacing record is a genuinely equivalent frequency result on two residue families after using semigroup symmetry, but does not cover arbitrary residues. The earlier a=dt+1 record covers a q=1 slice, not the full parameter law. The inspected antecedents do not establish eligibility and coefficientwise affineness uniformly over all unit residue classes; this conclusion requires grouping and comparing threshold ranks, even when started from older semigroup data.

## value

PASS

Deserts encode the distribution of consecutive nonrepresentables, finer than the classical genus, number of deserts, and maximum desert length. For each coprime residue class of b, the result determines all frequencies at every positive quotient from two coefficient lists, with an exact no-exception statement and no need to enumerate gaps as b grows. The length-support rigidity is not contained in the affine total count and is not a small numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
