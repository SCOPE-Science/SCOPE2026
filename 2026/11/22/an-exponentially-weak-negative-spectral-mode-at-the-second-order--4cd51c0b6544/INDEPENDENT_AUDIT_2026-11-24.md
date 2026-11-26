# Independent mathematical audit

## correctness

PASS

Ma's Theorem 2.3 has exactly the column normalization used here: its order-two defect at alpha=-h is R_h-4h u_h u_h*+3h(1-h^2) w_h w_h*. In particular r_n=1-(n+1-h)(n+2-h)/[(n+3-h)(n+4-h)]. The positive diagonal and positive rank-one term make P_h compact and strictly positive as a form. The negative rank-one direction yields the scalar condition 4h K_h(kappa)=1. The resolvent derivative is strictly negative, the limit at infinity is zero, and the 1/(4n) tail of u_n^2/r_n gives divergence at zero while the Sherman–Morrison term stays bounded. The root is therefore simple and unique for every 0<h<1. Subtracting (4(n+1)(1+kappa(n+1)/4))^(-1) termwise leaves an O((n+1)^(-2)) bound uniform in small h and kappa: split the change in the squared numerator from the change in denominators and use their uniform lower bounds proportional to 1/(n+1). At h=0, r=4u, and the two partial fractions of u give sum(u-1/(n+1))=-2. Thus the subtracted finite part is -1/2 and the comparison sum is (log(4/kappa)+gamma)/4+o(1). The rank-one positive correction is O(h); the root bound kappa<=4h||u_h||^2 permits the joint limit. Inversion gives the asserted 4 exp(gamma-2) prefactor. This concerns the canonical defect, not its congruence by M. The finite-column checker and verification notes were inspected, not executed.

## originality

PASS

The supported distinction is the quantitative eigenvalue scale and exact spectral prefactor for Ma's particular compact canonical interrupter. The decomposition, negative direction, and resulting at-most-one negative count at order two are not independent novelty claims. A generic logarithmic Birman–Schwinger mechanism does not determine this finite part.

## value

PASS

The canonical intertwiner and the sharp sign boundary are fixed by the published operator problem, not by an arbitrary normalization. The prefactor quantifies a first negative mode invisible to every algebraic expansion and distinguishes models that have the same logarithmic tail but different finite parts. It is meaningful as a spectral law for this defect without being a law for the actual self-commutator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
