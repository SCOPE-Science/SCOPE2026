# Independent mathematical audit

## correctness

PASS

After rescaling the Berger measure and n-tilting, the first moments are 1,u,uv and the tail weights squared divided by M^2 are moment ratios. Nonnegative variance and t^2<=t imply u<=v<=1. Matching 1,u,uv identifies the endpoint law (1-p)delta_x+p delta_1. For the analytic certificate, the polynomial part of t^ell/[(t-1)(t-x)^2] is the displayed P_ell, from expanding (1-1/t)^(-1)(1-x/t)^(-2) in inverse powers of t. Hence Q_ell is the quadratic remainder, and P_(ell+1)-P_ell is termwise nonnegative. For the ratio majorant, P_(k+1)-R_k P_k is nonnegative and strictly positive when x>0, so matching the quadratic moments proves the bound, with equality only for the stated law in the nondegenerate regime. Independently, the same Q_k bounds m_k by the endpoint moment m_k*. The probability law (1-t)dnu/(1-u) has mean x; Jensen gives m_k-m_(k+1)>=(1-u)x^k. At the endpoint law this is equality, giving the ratio bound by division using m_k<=m_k*. Inverse tilting works at every n for x>0, with norm equal to M because the upper atom persists. If u<v=1 then the tilt must be supported on {0,1} with positive zero mass; this is possible only at n=0. The equal pairs follow from zero variance or support bounded by one. The logistic expression follows by dividing by p; at fixed u, p=u delta/((1-u)^2+u delta) and x=u-u delta/(1-u), yielding the stated K asymptotic.

## originality

FAIL

The simultaneous upper envelope is already an exact consequence of Resultary b6e42f10def5, Finding and Proof §§1–3, 5. The positive-support restriction in that theorem does not create a new comparison problem at zero. Given the present normalized tilted law nu, apply the older theorem at index zero to its pushforward by t -> epsilon+(1-epsilon)t, for 0<epsilon<1. This law has support in [epsilon,1], and defines a subnormal shift by its positive moment ratios. Its mean is u_e=epsilon+(1-epsilon)u and its variance is (1-epsilon)^2 u(v-u). The older upper atom is 1, its lower atom is c_e=u_e-Var_e/(1-u_e)=epsilon+(1-epsilon)x, and its upper mass is p_e=(u_e-c_e)/(1-c_e)=p. Every finite moment and each positive-denominator ratio converges as epsilon tends to zero. Thus the existing upper bound gives precisely R_k for every k, including the cap-only hypothesis and the nonflat x=0 case. For x>0 the existing simultaneous two-atom extremizer and inverse-tilt construction apply verbatim with any positive lower support bound <=x. At x=0 the extremizer at index zero is the same limiting two-atom law and has strictly positive moments; positive-index tilt cannot charge zero. The logistic identity and logarithmic scale are direct algebra and asymptotics of the prior closed profile, not a distinct surviving theorem under the stated standard.

## value

FAIL

The cap-conditioned upper profile is a natural question, but its mathematical part is already covered by an exact two-sided continuation result and an elementary support regularization. The zero-endpoint exception is forced by the tilt and the apparent near-flatness delay is an immediate expansion of the prior two-atom ratio. This is a useful interpretation of an existing formula, not an independently valuable new mathematical remainder warranting a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
