# Independent mathematical audit

## correctness

FAIL

The reciprocal lower bound ||T_Gamma||²≥1/A and single-atom counterexample to the printed A are correct. But the claimed universal attainment by a continuous K-g dual is FALSE: Douglas factorization produces a bounded H→L² operator, not necessarily the analysis operator of a family of pointwise bounded coefficient maps. Rigorous counterexample: set H=l²(N), Omega=N disjoint-union T with counting plus normalized Lebesgue measures, fiber C, c=1/2 and a_n=2^-n. Let g_n be the unit basis function at the nth counting atom, h_n(t)=exp(2*pi*i*n*t), u_n=c*g_n+sqrt(1-c²)*h_n. Then the u_n are orthonormal in L²(Omega). Define Lambda_omega e_n=a_n*u_n(omega), K e_n=a_n e_n. Each Lambda_omega is a bounded functional because (a_n) is square summable, and ||T_Lambda* f||²=||K*f||², so the optimal lower bound is A=1. There EXISTS a genuine continuous dual Gamma with Gamma_omega e_n=g_n(omega)/c (at circle points zero), ||T_Gamma||=1/c, and T_Lambda T_Gamma*=K. For any dual C=T_Gamma*, the equations imply P_span(u_n) C e_n=u_n, so C=J+Q, J e_n=u_n, ran(Q) orthogonal to ran(J), and ||C||²=1+||Q||². Attaining squared norm 1 would force Q=0 and C=J. But at every t in T the coefficients of J e_n(t)=sqrt(1-c²)*exp(2*pi*i*n*t) are not an l² sequence, so no bounded pointwise functional Gamma_t on l² can implement J outside a common null set. Thus NO genuine pointwise bounded continuous dual attains norm²=1/A, although the family has a bona fide dual. The source has no hypothesis ensuring representability of its Douglas reduced solution. Hence its universal attainment assertion, indispensable to the final theorem, is false, while its separate lower bound and scalar correction survive.

## originality

PASS

Read the original preprint Theorems2.2 and2.3: original proof correctly derives universal lower bound 1/A, then prints inconsistent identity inf μ=A and asserts an attained bound A. The scalar witness and corrected value apply directly to this exact theorem. Nearby published correction for a *discrete* K-frame and nonunique duals is an analogous error but not a theorem for continuous K-g families, so it does not automatically cover this distinct source-specific finding.

## value

PASS

The claimed sharp extremal norm in a published dual c-K-g-frame theorem is numerically false and contradicts its accompanying lower estimate. Correcting it and giving a forced one-atom counterexample prevents misuse of the minimum dual synthesis bound; this is a motivated theorem correction with exact immediate consequence, even though Douglas factorization is standard. The field-realization obstruction is itself a substantive limitation, not an automatic correction of the invalid universal attained theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
