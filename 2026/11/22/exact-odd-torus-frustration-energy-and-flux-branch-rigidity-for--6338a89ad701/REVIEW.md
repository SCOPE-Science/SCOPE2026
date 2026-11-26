# Independent mathematical audit

## correctness

PASS

On each periodic ij plane all links cancel in the product, including at side length 2. For even area A, the unique way to minimize the plane sum is P=-1. For odd A write P=-exp(i delta); the principal deviation magnitudes sum to at least pi. Scaling to sum pi can only decrease the excess sum(1-cos delta), strictly unless already at pi. On that simplex, averaging unequal entries x,y with x+y<pi strictly lowers the excess by 2 cos((x+y)/2)(1-cos((x-y)/2)); a vertex first averages to (pi/2,pi/2,0,...) at equal cost and then improves strictly. Thus equality requires equal magnitudes pi/A and, by the product parity, a common sign. The three separate ij seam fields in the proof have curl phi_ij off the seam and on its noncorner plaquettes, and phi_ij-phi_ij L_i L_j at the corner; quantization makes the corner agree, and fields from other pairs give zero ij curl. This attains the summed lower bound for every sign combination. Equality in every plane leaves possible transverse sign changes only. In the cube identity the three signed principal increments total at most 3(2 pi/9)<2 pi, hence sum to zero in R; each depends on a different coordinate, so each is constant and periodic telescoping forces zero. Relative to any reference realization a second realization differs by a flat connection. Its gauge class is determined by the three independent coordinate transports, with arbitrary phases; the branch is a U(1)^3 torsor. Expansion of 3g L^3(1-cos(pi/L^2)) gives 3g pi^2/(2L)+O_g(L^-5) on odd cubes, and zero excess on even cubes. An independent integer-turn computation checked 5,892 plaquettes on nine tori for all allowed signs, plus gauge invariance and the energy. Replay: python /workspace/branches/21fef21b-84b8-4571-add2-e8a1119902a0/independent_flux_check.py.

## originality

PASS

Credit established overlap for the fully frustrated even periodic background. The supported distinct contribution is the sharp odd-area penalty on rectangular three-tori together with the exhaustiveness and independence of the constant minimizing branches, not uniform-flux quantization, an even background, or the general classification of flat connections. No inspected statement or necessary implication covers that distinct result.

## value

PASS

Strict periodicity and a locally favored minus-one plaquette compete on odd coordinate areas. The sharp excess is a usable finite-size benchmark, including its parity dependence and leading 1/L correction, and the constant-pattern rigidity separates the true minimizing branches from flux fields that are only kinematically possible. These are natural variational and classification questions rather than an arbitrary enumeration of small tori.

The dated certificate retains the supplied scientific assessment, sources and limitations.
