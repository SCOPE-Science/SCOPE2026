# Independent mathematical audit

## correctness

PASS

The odds rewrite gives 0<z<w<=1 and R_x>1, R_x>R_y and R_x R_y>1, proving strict order preservation on both branches, including a tie. Before entry, r'-1=(r-1)(1+r/(1+w)) >= 3(r-1)/2, and r>=alpha forces R_y<1; this proves the stated ceiling bound even when it is zero. At or after entry, the denominator-minus-numerator identity for R_y' is at least alpha-2>0. The proposed fixed point has w_*=1/(alpha-1), z_*<w_* and R_y=w_*<1. The two log-odds deviations satisfy u'=u-av and v'=bu-v; the mean-value bounds a>=1/2 and b>=1-1/alpha make N nonincreasing and bound |u'-v'| by qN, q=1/2+1/alpha. At the second step each of the first two components puts weight at least 1/2 on that tightened bound, giving (1+q)/2; the difference component is bounded by qN. This proves the rate from T, not a sharp asymptotic multiplier or a contraction during the transient. RESULT.md §§1–4 and CHECK.py were inspected, not executed; the finite checker's entry-time ceiling uses floating-point logarithms even in its rational map checks. No computation is needed for the analytic proof.

## originality

PASS

Credit existing same-map global convergence and eventual branch selection for alpha>=4, and credit Satur for the fixed points, order preservation and local stability. The supported distinct claim is global attraction down to every 2<alpha<4, together with the specific explicit entry-time and log-odds estimates for all alpha>2. No equivalent coverage of this stronger parameter-and-estimate statement was identified in the sources checked.

## value

PASS

The extension reaches arbitrarily close to the bifurcation threshold where the local theorem and numerical evidence did not settle the basin. The absorbing branch and explicit transient estimate give a structural reason for winner–loser selection; the two-step estimate then supplies a uniform bound even for points that enter far from the fixed point. This is not a recomputation of the fixed point or a merely local multiplier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
