# Independent mathematical audit

## correctness

PASS

Condition on q and rotate the left Gaussian sketch into the orthonormal basis (q,q⊥). With row coefficients p=qᵀB, r=q⊥ᵀB the sketched response is Up+Vr with independent standard U,V. Conditional on U and q, the cross term has mean zero and UᵀV has variance W=||U||². The right Gaussian angle gives E q₁²=a/(a+b) (integrate via tan θ), so A=E||p||²=a²−ab+b² and D=E||r||²=ab. The conditional-on-U loss after averaging V and q is D+(Aλ²+DW)/(W+λ)². Its gap to the value at λ*=D/A is A W(λ−λ*)²/[(W+λ)²(W+λ*)], proving strict global optimality including the extended-risk endpoint λ=0. For zero ridge the squared loss is ||r||²(1+Z²/W) with independent normal Z and chi-square W; the density at zero yields the stated moment cutoff and E[1/W]=1/(s−2) when s>2. Positive ridge bounds √W/(W+λ), giving every positive error moment. For B=tI the mixed row term is traceless, so the trace shortfall is t(2−W/(W+λ)), strictly increasing from t. The isotropic beta tail follows from independent one- and s-degree chi-square terms.

## originality

FAIL

The deterministic ridge is an exact specialization of the classical one-regressor bias–variance rule, not a new sketch-count independence mechanism. Condition on the normalized design U; the response is additive centered noise with second-moment trace D per left row and the coefficient has mean squared norm A independent of U. The standard scalar ridge risk and optimizer therefore apply at every U before averaging over its length. The ratio D/A uses the elementary two-dimensional Gaussian projection baseline. The indexed unregularized Gaussian reconstruction law already gives the tail mechanism, and on the identity the ridged approximation is the unregularized approximation multiplied by W/(W+λ), making the trace comparison immediate. No claim is made that a prior source prints the entire averaged formula in this notation.

## value

FAIL

The benchmark clarifies that two losses need not agree and illustrates why QR normalization matters. In this rank-one isotropic-noise setting, however, the supposedly distinguishing exact penalty is the routine scalar ridge rule after inserting known or elementary projection energies, and the identity trace loss worsens by scalar shrinkage alone. The package does not establish a non-mechanical phenomenon beyond those textbook mechanisms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
