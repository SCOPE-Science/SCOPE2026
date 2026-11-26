# Independent mathematical audit

## correctness

PASS

For three independently and identically moving individuals, conditioning on a focal individual's site gives u=∑p_m(1−p_m)² for the probability of being alone. Symmetry and row sums imply W_ii=u, W_ij=(1−u)/2 for i≠j. Direct expansion for (a,a,1−2a) yields u=2a−6a³; the two stated values a,b obey a²+ab+b²=1/3, hence have identical u while their s₂=∑p_m² differ. In state j=1,2, the defector strategies earn respectively s₂ and 1−u, by the probability of meeting any cooperator; the cooperator payoff is 51/100 in both states. These payoffs and all required cross transitions are strictly positive for either witness throughout 0<w≤1. Dividing the upward transition by the downward gives F_C/F_(D,j): the shared count j(3−j), W_12 and total fitness cancel. The absorption recurrence then yields 1/(1+r₁+r₁r₂), where r_j=F_(D,j)/F_C. The sign relative to 1/3 is that of w(L+Qw). An independent exact enumeration of all 27 placements, both interior transition equations, and rational endpoint coefficients is replayable with python3 /workspace/evidence/independent_site_volunteer.py. For A, L=−186457/6173100 and L+Q=−757593659/111424455000; for B they are 155543/6173100 and 316099649/12380495000. An affine factor stays strictly of the same sign between these endpoints, proving the continuum assertion; the exact w=1 fractions also agree. With two individuals every focal sees only a solo or a pair, and their probabilities are identified by the diagonal of W, so all anonymous state payoffs and fixation laws agree. For N=3, M=1 is unique and M=2 has u=q(1−q), recovering the common site law up to permutation, including degenerate laws. That proves the stated sharp minima. The uploaded checker was read, not executed; its finite tests are not the reason for the all-intensity or minimality result. The conclusion concerns single rare-cooperator fixation relative to neutrality in pre-averaged BDB, not competing-mutant dominance, other update rules, or w>1.

## originality

PASS

The group-normalized replacement rule, pre-averaged game framework, birth–death formalism, and broad interaction/replacement distinction are existing ingredients. The distinct result is an exact failure of identifiability from the entire weighted replacement matrix within a fixed game and a common independent-site mechanism, with sign separation for every admissible intensity and minimal N=M=3. The closest theoretical setup computes fixation from given site laws but supplies neither a matched full-kernel pair nor these sharp inverse obstructions.

## value

PASS

This shows that even the complete replacement kernel can lose the information needed for a sign verdict in an otherwise specified model. In the example the lost quantity is an observable co-occupation probability. The sharp minimal common-site witness and the absence of a weak-selection-only restriction turn the example into a structural result on which summary information suffices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
