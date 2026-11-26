# Independent mathematical audit

## correctness

PASS

For n=m+1 the constant vector, the hub-vs-leaves contrast (m,-1,...,-1), and the sum-zero leaf modes are the orthogonal Laplacian spaces for 0,n,1. With a=exp(-t) and b=exp(-nt), the two diagonal values differ by (m-1)(a-b)/m in favor of the leaves. The SPD residual is a Gram compression onto the orthogonal complement of K^(1/2)e_v; its trace error is the common full trace minus the gain K(2t)_vv/K(t)_vv. Clearing the two positive gain denominators and grouping terms gives (m^2-1)[(a-b)-(a^2-b^2)-mab(a-b)]; the sign is minus the sign of mab+a+b-1. This last factor decreases strictly from m+1 to -1, proving all three cases for finite t>0 and failure of the largest-diagonal rule above the threshold. For the asymptotic, at t=c log(m)/m the positive term b(1+ma) is asymptotic to m^(1-c), whereas 1-a is asymptotic to c log(m)/m. Taking c=1 and c=3 brackets the root. With z=m tau, the exact root equation rewrites as z exp(z)=m^2 exp(-2 tau)(1+exp(tau)/m)/[(1-exp(-tau))/tau]; the multiplicative correction is 1+O(log(m)/m) on the bracket. The derivative of W(exp(s)) with respect to s is W/(1+W)<=1, giving the claimed remainder after dividing by m. At fixed t>0, the gain limits are 1 and a, the top eigenspace is uniquely the constants, and diagonal sampling normalizes the hub diagonal by 1+(m-1)a+b, giving the asserted success scales. For sufficiently large m the hub is uniquely optimal and exact expected excess is (1-p_h)(G_h-G_leaf); hence the limit is absolute, not relative or uniform in t. Inspected CHECK.py and its finite checks, not executed.

## originality

PASS

The generic gain identity, pivot rules, uniform rank-one leverage on this eigenspace and a closely related same-star pivot reversal do not merit novelty credit. The exact exponential-kernel transition, Lambert-W asymptotic and quantified large-star separation from the standard first-pivot rules are distinct from the inspected results.

## value

PASS

This is a motivated exact example where largest-diagonal greedy pivoting never picks the trace-optimal column beyond a sharply located time, and two common random rules find that column with vanishing probability while incurring nonvanishing absolute loss. The asymptotic locates the narrowing leaf-optimal regime, and the regret makes the ranking mismatch quantitative. This is useful for single-column trace optimization; it is not evidence about multipivot methods or normalized relative loss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
