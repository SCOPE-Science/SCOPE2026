# Independent mathematical audit

## correctness

PASS

For h≥0 the leaf-difference mode has multiplier f(ah); the hub versus constant-leaf system has multipliers 1 and f((a+mb)h). This yields the hub diagonal and the difference T_jj−T_ij=f(ah) for distinct leaves. Direct multiplication gives T_ij=ab h²[3−(2a+mb)h]/6. At its positive zero h_L one has ah_L<3/2 and T_jj=f(ah_L)>f(3/2)=1/16; monotonicity of the leaf diagonal follows from its nonnegative projector coefficients multiplying the decreasing modes. The two hub–leaf directions are proportional to 1−f((a+mb)h), strictly positive for h>0. The hub diagonal falls from 1 to −∞, and at h_L it has the sign of F(r)=16r³+9r²−3r−4 with r=a/(mb). F'(r)=3(2r+1)(8r−1), F(0)=−4 and F(1)>0 imply precisely one positive zero; exact opposite signs at r=1/2 and 3/5 and bisection confirm the stated crossover. Both limiting entries remain negative once their own cutoff is crossed. Row sums are one, and h=0 is the identity. The finite verifier was inspected, not executed. Its 7,623 figure is the number of matrix entries covered across exact samples; the code compares five representative entries per matrix and checks row sums. No claim about internal stages is established.

## originality

PASS

The supported distinct claim is the two-obstruction independent-rate classification and its crossover, not positivity of a cubic polynomial on a symmetric star or the general existence of root-based invariance tests. The strongest inspected symmetric and quartic results do not imply it.

## value

PASS

The result gives an exact bound and identifies which physically distinct transition fails for every balance of inward flow and aggregate hub outflow; both regimes occur. Independence of the switch from leaf count and permanent sign loss above the bound make this more than an isolated cubic-root calculation. It does not give a bound for accuracy or SSP stage positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
