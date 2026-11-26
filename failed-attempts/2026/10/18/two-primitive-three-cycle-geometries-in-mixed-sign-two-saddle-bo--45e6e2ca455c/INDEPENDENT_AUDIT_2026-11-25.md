# Independent mathematical audit

## correctness

PASS

The affine fixed points have x=1/(1-tau+delta); the domain puts the left one strictly left and the right one strictly right. The characteristic polynomial signs at 0 and 1 (left), or at -1, 0 and 1 (right), give multipliers respectively in (0,1),(1,infinity) and (-infinity,-1),(0,1). Thus neither branch derivative cubed has eigenvalue 1, and a word using only that branch gives only the original affine fixed point. The only remaining primitive length-three necklaces are LLR and LRR. Independent elimination uses x_(i+1)=tau_i*x_i-delta_(i-1)*x_(i-1)+1 with indices mod 3; the coefficient matrices for (x_0,x_1,x_2) have rows (-a,1,d),(b,-a,1),(1,b,-c) for LLR and (-a,1,d),(b,-c,1),(1,d,-c) for LRR. Their determinants and the three column replacement determinants with RHS (1,1,1) are, respectively, (D_L;K,J,Q_L) and (D_R;Q_R,J,K), by expansion. The multiplied Cramer identities also hold for every solution of a singular system, so positivity of the appropriate Q excludes a solution when D=0. Q_L>0 by a>1+b>1 and b^2-b+1>0; Q_R=(c+(d+1)/2)^2+3(d-1)^2/4>0. The strict signs and uniqueness follow from the coordinate ratios, and y_i=-delta_(i-1)*x_(i-1). For LLR the return has determinant b^2*d<0 and characteristic polynomial positive at 1, yielding one positive multiplier below one and one negative multiplier; the sign at -1 is S_L and gives the three stated alternatives. For LRR the polynomial is positive at 0 and negative at 1, with leading coefficient +1, so both roots are positive with one on each side of 1. Substitution along (5/4,1/5,-5,d) gives the two factored denominators and S_L=-(484d+2425)/400. The exact threshold lies within (-6,0), and at d=-11/2 both cycles are strict and the LLR return is Schur-stable, proving open coexistence by continuity. Neutrality is only a simple multiplier statement, not a flip theorem. Read frozen verify.py and VERIFICATION.md; no source script executed. Its bounded rational checks do not establish the strict sign and singular-case claims, which follow from the proof. No switching-line, global basin or higher-period claim is accepted.

## originality

FAIL

A distinct same-date Resultary theorem already gives the attracting criterion in a broader two-saddle parameter region. More decisively, its proof gives the unrestricted algebraic LLR coordinates and both products' trace/determinant data. The remaining strict census and multiplier classifications follow directly by swapping the matrices in those pre-admissibility formulas, using the determinant signs, and applying the strict branch signs. Even the established attracting example of that source is in the same mixed-sign sector and mechanically gives coexistence. The particular new rational slice does not supply an independent nonroutine contribution. This is a coverage finding, not an inference about chronology or attribution from the shared date.

## value

PASS

A full strict-cycle count and stability classification on a natural noninvertible saddle sector would be useful for understanding coexistence and reading parameter diagrams, even without a global-attractor theorem. After the coverage comparison, neither an alternative rational witness nor specializing the already available stability polynomial to its slice is a valuable standalone remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
