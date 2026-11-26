# Independent mathematical audit

## correctness

PASS

Independently reconstructed the proof for real SPD K=aI+bvv^T, with unit v and a,b>0. For a k-set I, setting s=sum_{i in I}v_i^2, the residual is zero off the complementary principal block and its trace is a(n-k)+ab(1-s)/(a+bs). This follows by subtracting b^2 s/(a+bs) from the rank-one coefficient b in that block. The trace is strictly decreasing in s. The best subset takes the k largest squared coordinates; their total minus k/n is 1/n times the sum of all top-to-bottom differences. Those differences are nonnegative, and equality forces all coordinates to have the same square because both blocks are nonempty. Flat vectors exist, including with arbitrary signs. The k-DPP residual expectation follows by summing det(K_II) times the individual residual diagonals, which are ratios of bordered principal determinants: each (k+1)-minor is counted k+1 times. Substituting e_j=binom(n,j)a^(j-1)(a+jb/n) reproduces the stated value. The proof covers the entire interior range, not just rational input or sampled orientations. The frozen checker was inspected, not executed; its finite tests are supplementary and not required for the proof.

## originality

PASS

The expectation formula itself and the all-spectra endpoint are prior. The distinct supported finding is exact attainment by the best deterministic subset in the worst orientation at every interior rank of the one-spike class, including its full equality locus. No direct coverage or stronger implication was established by the checked sources.

## value

PASS

The one-spike class is a canonical non-scalar SPD family, not a list of fortuitous numerical examples. Exact sharpness answers an independently posed minimax problem throughout its interior sample-size range on that class. The equality locus identifies precisely when best deterministic landmark choice cannot improve on expected volume sampling in the worst orientation. This supplies a concrete sharp benchmark without claiming to resolve the arbitrary-spectrum problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
