# Independent mathematical audit

## correctness

PASS

On a 3-periodic trajectory the delay coordinate x_(n−2) equals x_(n+1), giving the reverse cyclic scalar iteration q_c(u)=c−u² after division by 1+b; conversely a scalar primitive three-cycle gives one full-map primitive cycle. The census can also be checked without the sextic discriminant. With s²=4c−7 and w=2u, the factors of 64D_c(w/2) are the monic cubics H_s and H_−s, where H_s=w³−(1+s)w²+(−s²+2s−9)w−s²+1+s(s²+7). Expansion verifies the factorization; their difference for s≠0 is −2s[w²−2w−(s²+7)], and reduction of either cubic modulo the bracket leaves 8, so they have no common root. For imaginary nonzero s they are conjugates and hence neither has a real root. For real s their cubic discriminant is 64(s²−s+7)²>0. The trace w+Q(w)+Q²(w), Q(w)=(s²+7−w²)/2, reduces to 1+s modulo H_s, so for s≠0 each factor groups a cyclic orbit, as q_c preserves the orbit trace and no real fixed point is a dynatomic root (1+q_c′+q_c′²>0). At s=0 there are exactly three distinct roots and hence one cycle. The scalar multiplier is the constant term of H_s, 1−s²+s(s²+7); t=√(4c−7) gives the two reported branches. Direct differentiation of the full return gives P(λ)=(λ+b)^3−Mλ, M=(1+b)^3m. Cubic Schur inequalities require M<(1+b)^3 from +1, M<(1−b)^3 from −1, and M>−(1−b²)^3 from the last Jury condition; |b³|<1 is automatic. The −1 constraint dominates +1. The plus branch m>1 has a real multiplier >1 by P(1)<0; the minus branch strictly decreases through the two bounds. At birth λ=1; at the lower stability boundary P′(−1)=(1−b)^2(2+b), and dλ/da=λM′/P′>0 there. At the upper boundary the claimed factorization gives a distinct unit pair since 0<3b−b³<2, and the real eigenvalue u=−b³ has P′(u)>0. Its derivative with respect to a is positive, so the squared pair modulus −b³/u increases through one. Expanding the lower right-hand side of φ(t_−) gives 6b+O(b²); near b=1 the two right-hand sides differ by (9/8)(1−b)^3+o((1−b)^3), yielding both stated physical-a scales and the checked numerical constants. The submitted symbolic script was inspected, not executed. No nonlinear endpoint or global basin result is inferred.

## originality

PASS

The distinct result is the global orientation-reversing three-cycle sink interval and its two Floquet mechanisms and endpoint laws. The scalar census and much of the method are already known; the exact theorem for positive last-coordinate coupling does not give the negative-coupling stability boundaries. This conclusion is a best-of-knowledge statement, not a priority certificate.

## value

PASS

The sign selects a different first loss/gain mechanism despite the same scalar orbit census. A sharp global sink interval for a studied generalized Hénon family, a rigorous counterpoint to equating period-three birth with stability, and the two distinct endpoint scales are meaningful analytic distinctions. They specify exactly where a locally stable orbit can occur, without mistaking unit-modulus Floquet crossings for nonlinear bifurcations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
