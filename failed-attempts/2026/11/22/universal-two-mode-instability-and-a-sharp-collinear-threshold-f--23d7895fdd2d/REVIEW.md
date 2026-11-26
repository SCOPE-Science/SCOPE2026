# Independent mathematical audit

## correctness

PASS

In the common rotating frame the active radii cancel the on-site scalar linear term, leaving the real symmetric operator Jv=(-2k w_j w_j^T v_j+c sum_l v_l)_j. In radial and tangential coordinates the Hessian -J is a strictly positive radial form minus c times the squared norm of the full sum. At a noncollinear polygon the tangential sum map surjects onto R^2. A linear shift of the tangential coordinates absorbs the radial sum and leaves M positive squares, two negative squares and M-2 free coordinates for -J. These free coordinates are exactly the kernel of the closure differential on the product of circles, which has rank two. In the collinear case the perpendicular block of J has rank one and is positive semidefinite; the parallel block is congruent to -I+cqq^T with q_j=(2a_j)^(-1/2). Its only sign change is at c||q||^2=R=1, including precisely one additional zero at equality. Thus the four claimed inertias, tangent interpretation and linear-only threshold hold. The frozen symbolic checker differentiates the vector field and checks five examples. Separate finite checks reproduced (2,3,1), (2,4,2), (1,4,3), (1,3,4), (2,3,3); replay /workspace/branches/1fdfdf28-6543-4ca2-93aa-cb0f3659855d/reproduce_inertia.py. The examples are not the universal certificate.

## originality

FAIL

A distinct published Resultary record already proves both the noncollinear and full collinear formulas in a broader active/inactive formulation. The entire frozen mathematical contribution is its all-active specialization, not merely a coincident count or an analogous result for another coupling.

## value

FAIL

A full instability index and a degenerate collinear threshold are useful invariants, but the frozen version adds neither a new regime nor a new conclusion. Its all-active restriction in a different notation carries no demonstrated independent contribution beyond the already available broader analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
