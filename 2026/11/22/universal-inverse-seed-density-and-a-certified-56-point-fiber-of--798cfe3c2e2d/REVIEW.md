# Independent mathematical audit

## correctness

PASS

For phase coordinates (p,r)=G(x,y), r−p fixes u=x−y and 1+u²+2(p+r) fixes v² with v=x+y+1. Square membership is exactly |u|−1≤v≤3−|u|. This gives two injective closed sheets meeting at v=0 and determinant −v. Each image has boundary contained in the polynomial images of its finite polygonal edges (the interior has nonzero determinant). Those finitely many rectifiable arcs have an O(h)-area neighborhood at radius h, by covering each with O(1+length/h) disks. Hence lattice-cell discrepancies and the overcount of points with v=0 are O(1/h) uniformly in translations; where both sheets have distinct inverse points they must both be counted, even when images overlap. The integrals of |v| are 1/6 on the negative triangle (integral of the height decreasing linearly from 1 to 0), and 4+1/6=25/6 on the positive sheet by the signed integral. Exactly 2^(2−k) distinct phase-lattice translates of mesh 2π/t give the stated coefficient and O(t) remainder. Continuous weights pull back through each compact-sheet inverse, and shifted grid sums converge on these Jordan-measurable images; the fold contributes negligibly, also for the proportions on either open side. For the exact finite check I independently enumerated all 169 pairs using squared inequalities and rational bounds on π, without floating point, square-root rounding or execution of uploaded code. For α=π/10, d=|m−n| and D=v², (3−dα)²−D=8−[6d+2(m+n)]α and D−(dα−1)²=4 max(m,n)α. Combining these comparisons with signs of the interval endpoints yields 43 positive-sheet interior, 6 positive-sheet boundary and 7 negative-sheet boundary points, none on the fold. The exact boundary index pairs are the two nonpositive coordinate axes truncated at −6. Replay: python3 /workspace/independent_checks/square_fiber.py. The finite certificate does not prove the large-t conclusions.

## originality

PASS

The defining map and the minimum diagonal gain are published; the all-target inverse asymptotic, one-step empirical law and exact zero fiber are distinct on the inspected evidence. The count is exact-real and on the closed square, not a claim about forward distributions, encryption or finite precision.

## value

PASS

The global two-sheet normal form organizes the inverse geometry of a published coupled map. The result is quantitative on all targets (including edges and corners), with a nontrivial spatial asymmetry and a reproducible exact lower-gain baseline including boundary contributions. It is not a randomly chosen finite slice, generic area-formula restatement, or forward dynamical claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
