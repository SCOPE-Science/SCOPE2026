# Independent mathematical audit

## correctness

PASS

For the cumulative-indicator particle field, use 2 Cov(I_X,I_Y)=E[(I_X-I_X')(I_Y-I_Y')] with an independent copy of the pair; integrating through the identity integral (I_U-I_V)^2=|U-V| gives the absolute-distance covariance formula. The mean of two fields contributes a cross term m^2/2, and reflection changes the scale of a matched difference from sqrt(2) sigma to 2 sigma, giving the stated m^2/4 coefficient. Differentiation yields the exact curvature switch. Integrating the mixed derivative on each nondegenerate rectangle gives the strict ordered-minus-crossed comparison, so any nonextremizing permutation admits an improving swap in the stated direction. The normalized local exchange converges to minus the curvature, including zero at the boundary. Integrating the strictly positive scale derivative of g gives K>0 and shows K decays at infinity. In the displayed two-particle family the rank gains tend to zero while the crossed gain tends to m^2 K(delta)/4>0. Inspected RESULT.md, VERIFICATION.md and verify.py; the reported 2,492 checks are finite supplementary tests, not a new run or a proof of the infinite claims. The variance comparison uses a cumulative field, not a particle density estimator; a deterministic additive field baseline has no variance.

## originality

FAIL

The principal claimed optimization and zero-ratio conclusion are covered by an earlier indexed result, not merely related via generic Monge theory. At r=1 the earlier horizon kernel and curvature threshold equal the frozen ones exactly, and minimizing variance for a fixed reference is maximizing gain. The complementary minima follow from the same strict exchange, and the earlier loss family already implies the zero infimum. A different example, with positive limiting best gain, does not make the frozen principal claim distinct; later evidence also exhibits a retained positive saving with rank savings vanishing.

## value

PASS

The mathematical question is motivated by an actual rank-based pairing strategy. A proof that it is uniquely best in one regime and uniquely worst in another, with no positive relative guarantee in general, is useful guidance for the one-stage model. In particular the example with one persistently close crossed pair gives a transparent reason for the loss. This scientific relevance does not cure the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
