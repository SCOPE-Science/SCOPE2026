# Independent mathematical audit

## correctness

PASS

Conjugating by H^(1/2) reduces exact line minimization to rank-one orthogonal projections. Reflection removes off-diagonal expectations. With t=√κ, W=t²/(t²+X²) for standard Cauchy X satisfies EW=t/(t+1) and E[W(1−W)]=t/[2(t+1)²] by differentiation. In the independent case conditioning on the first direction gives diag(t²+t+2,t(2t²+t+1))/(2(t+1)³). For the paired case I checked the printed partial fraction and both overlap moments symbolically via a two-parameter Cauchy resolvent and differentiation before substituting the reciprocal parameter (/workspace/independent_checks.py). These give precisely the stated scalar multiple of the independent matrix. Its second diagonal entry is largest since the unnormalized difference is 2(t³−1); both bounds are attained on the smaller-eigenvalue mode. At t=1 the paired projections are complementary and the iid result is 1/4; at t=2 the factors are 11/27 and 11/75. The statement about not preserving first-line optimality is generic, not a claim that special realizations such as Hessian-eigenvector lines lose it. No higher dimension or inexact search is verified.

## originality

FAIL

Indexed record d73676e44901 is a distinct published record with the same initial-error quantifier, planar SPD quadratic, two sequential exact line solves and coupling law. Its proof gives both full expected error matrices, not just a comparison of scalar bounds, and the same scalar relation. The sharp factors of the frozen record are exactly its larger diagonal entries, so giving them as separate scalars adds no mathematical result. Verified equivalent coverage is decisive here; the indexed record's November path date does not establish chronology of discovery or dependence. The general RSN and random-pursuit literature was relevant background, not the basis of the failure.

## value

FAIL

A sharp, all-start comparison with equal costs and equal one-direction marginals is independently useful in principle, but the checked index record already delivers it including the full matrices. Restating the same laws as sharp contraction constants is a direct consequence and does not add a scientifically distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
