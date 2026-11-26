# Independent mathematical audit

## correctness

PASS

The frozen RESULT theorem is sound; the public SLOGAN overstates it by saying the inequalities involve only the two fastest rates, whereas F and G use all three. For fixed fastest rates a=b=1 and z=8/5, E_{1/2}=1.984 and D_{1/2}=3.2128, so the step is stochastic at c=1/2, whereas D_1=-3.3408, so it fails at c=1. Both replacement files state explicitly that the two largest rates select the inspected entries, not all their coefficients. The repaired RESULT preserves the full theorem and proof; its limitations restate that the interval classification assumes the two largest rates are equal. In the proof, Cayley–Hamilton gives I+FQ+GQ^2, with G>0 at positive h by the quadratic discriminant. The largest pair M+u is present on a directed edge even with ties; its nonnegative test gives F≥(M+u)G and the diagonal difference (M-x)[F-(M+x)G]≥0 for each other rate x, giving the exact all-step equivalence including h=0. In the two-tied-fast family E is strictly decreasing in z and its root increases with r. The independent Sylvester determinant and half-line coefficient checks isolate one simple sextic root in (1/2,1), and D_r(e(r)) changes sign between r=0 and r=1 because the fourth Taylor polynomial of exp(-z) is positive and D_1(2)<0. For r≥1/2, D'_r is negative: up to z=1 use its coefficient signs and for z≥1 it is maximized at r=1/2, where D'_{1/2}/24=-(z-2)^2/4-z^3/8. Concavity in r interpolates between positive D_0 and nonnegative D_{r_*} up to the direct cutoff for r<r_*. This proves both cutoff regimes and no reentry in the stated family only. Replay: python3 /workspace/branches/independent_checks.py 1 confirms all nine polynomial entries, the elimination and sign certificates, r_* and both reported horizon checks. The verification logs are supplementary evidence, not independent formal certification. Complete corrected files: /workspace/repairs/1/RESULT.md and /workspace/repairs/1/SLOGAN.txt. The frozen sources and verification evidence remain unchanged.

## originality

PASS

Best-knowledge pass for the arbitrary-rate two-entry necessity-and-sufficiency result together with the nonreentrant two-tied-fast-rate mechanism switch. The equal-rate cutoff is known and not claimed new; ordinary characteristic-polynomial reduction is a tool, not a separate advance. Clarifying the slogan's rate dependence does not change which theorem is assessed.

## value

PASS

The three-cycle is a natural minimal recurrent one-way network in which RK4 permits wrapped returns. An exact all-rate endpoint test sharply reduces the number of inspected entries, and the algebraic boundary identifies a genuine change from failure of a jump probability to failure of a staying probability. Neither the equal-rate value nor a generic root solver answers that mechanism question. The repaired slogan accurately conveys these uses without promising rate independence, internal-stage validity, or accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
