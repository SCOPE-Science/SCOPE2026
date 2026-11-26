# Independent mathematical audit

## correctness

PASS

Squaring the four-class off-diagonal next-generation matrix gives cyclic two-step blocks, so its spectral radius squared equals that of K=(I+mL_h)⁻¹Q. Direct inversion gives Q=c²[[a,bξ²],[bξ⁻²,a]]. For P=p+q and π=(q,p)ᵀ/P one has L_h=P(I−π1ᵀ) and (I+mL_h)⁻¹=(1−w)I+wπ1ᵀ, w=mP/(1+mP). This yields the stated trace and determinant; the positive off-diagonals for n>0 select a simple upper eigenvalue. The characteristic polynomial at any fixed λ is affine in w. If a simple Perron root is stationary, the polynomial at that root and its w-slope both vanish, so it is a root for every w. Strict positivity and simplicity prevent a switch to another root. Hence the Perron branch is constant or strictly monotone. Its endpoint values are c² and 1ᵀQπ=c²(a+bT), and T−1=(ξ²−1)(pξ²−q)/(Pξ²), proving the exact sign and equality, including m=0. For c<1 the root reaches one in finite m iff the far endpoint is above one; equality at infinity does not suffice. The equation (1+mP)det(I−K)=0 gives the displayed m_*; its second eigenvalue there is D_m<1. With n=0, K is c² times a stochastic resolvent so R=c. Direct rational substitution also gives the stated witness and determinant factor. Frozen verify.py was inspected, not run. Its rational trace/determinant checks and floating-point monotonicity samples are not the all-parameter justification.

## originality

PASS

Credit next-generation reduction, the general rank-one perturbation method (which gives the constant-or-strictly-monotone dichotomy here), and the qualitative possibility that movement raises a coupled reproduction number above local values. The supported distinct claim is the explicit stationary-bias sign and equality law, independence of that sign boundary from positive vector-rate magnitude, and the exact unity crossing and single-class invariance for this reciprocal two-class model. The inspected stronger matrix results do not supply that model-specific classification, and none of the compared movement models establishes it under these parameters.

## value

PASS

Equal isolated thresholds leave the sign of the coupled host-rate response undetermined. This is a natural exact three-way classification: the two individual movement blocks preserve the isolated value, yet simultaneous coupling can lead to either sign, exact invariance or a genuine finite crossing, governed by a stationary-weight boundary. It gives a tractable benchmark distinguishing joint effects from known single-class reduction principles. The value is in that explicit model boundary and its hypotheses, not in the determinant identity by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
