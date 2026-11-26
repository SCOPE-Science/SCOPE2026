# Independent mathematical audit

## correctness

PASS

For a nonempty leader set, the grounded principal Laplacian is positive definite. Write u,x,c,y for the neither/core-only/leaf-only/both pair counts. Eliminating the leaves gives the core matrix diag(n on u, n+1 on c) minus the all-ones matrix. Every attached follower leaf contributes 1 plus its core inverse diagonal and every isolated follower leaf contributes 1. This yields (1), including when there are no follower cores. Exchanging a both-and-neither pair for a core-only and leaf-only pair preserves u+x, strictly decreases the other linear and numerator terms and strictly increases the positive denominator. For b<=n one then has u=n-b,y=0. Up to a constant the objective for x core leaders is nx/(n+1)+A/(b+nx), where A=2(n-b)(n+1)/n+b>0. The consecutive differences n/(n+1)-nA/((b+nx)(b+n(x+1))) increase in x and the difference at x=1 is positive for b>=2: A<=2(n+1) and (b+n)(b+2n)>2(n+1)^2. The difference at x=0 reduces to the stated P_n(b) divided by the claimed positive denominator. Modulo n, equality implies n|2b; P_n(n)>0 and P_n(n/2)<0 rule out all candidates. Rescaling the quadratic by n^3 gives the stated positive limiting root. For b>n, u=0 and y=b-n; the derivative with respect to c is -n/(n+1)+1/(n+1-c)^2<0 since c<=n-1, so all leaves are leaders. Substitution gives the costs and permuting pairs gives the counts. The supplied checks are bounded: the symbolic identities use the trace formula, and the small-matrix runs are independent of its derivation. An independent replay, python3 -B /workspace/reproduce_finite.py 4, used exact rational Gauss–Jordan inversion on all 1,338 nontrivial leader sets for n=3,4,5, agreeing on every optimizer and minimum. No supplied script was executed.

## originality

FAIL

A distinct published Resultary record gives the same all-budget solution, including the exact optimizer sets, counts, and costs, for a larger parameter range. The only material sharpening in the assigned statement is ruling out an equality branch of the same polynomial, an immediate modular check. This is present coverage, not a finding that the later-dated record had historical priority or that either record was derived from the other.

## value

PASS

The all-budget closed solution of the grounded trace on a natural two-role graph family is a meaningful exact optimization result. It distinguishes cheap grounding of core-mediated correlations at small budgets from removing noisy leaves at larger budgets, gives all minimizing configurations, and replaces combinatorial search by a quadratic sign test. This assesses the mathematical problem and solution, not novelty. The elementary no-integer-tie refinement is not a separately valuable repair of the overlapping classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
