# Independent mathematical audit

## correctness

PASS

The exact telescoping identity μ^(-n)z_n=z_0+sum_{j<n} μ^(-j-1)c_j has a tail uniformly bounded by μ^(-n)(|α|+B)/(μ-1) for n≥2 because x_n=sin z_(n-2), y_n=sin z_(n-1) there. This proves global continuity, the stated unscaled remainder and H∘F=μH. Compare same-(x,y) orbits with e_0=z'_0-z_0>0: e_1≥(μ-|δ|)e_0, e_2≥(μ-|δ|)e_1-|γ|e_0≥(μ-B)e_1, and for n≥2 the three sine differences are bounded by e_n,e_(n-1),e_(n-2), respectively. Induction gives growth by μ-B>1. The ordered phases cannot coincide: equal H would make their difference bounded by twice the uniform remainder. On each fiber H-z is bounded, locally uniformly over the base, giving surjectivity and joint continuity of the inverse by sequential compactness and uniqueness. H=0 is exactly boundedness; the one-sided backward recurrence on bounded sequences is a contraction of factor (1+B)/μ, and its smooth sine substitution has uniform Fréchet derivatives on bounded sequences, so I-DT is invertible and the implicit function theorem applies; the stated graph Lipschitz bound follows by comparing fixed sequences. The fixed-point equation is strictly increasing in s and tends to opposite infinities. On the graph one can also check exponential convergence directly without invertibility or a stable-manifold theorem: for E_n=sup_{j≥n}|z_j-s| the bounded future series gives E_n≤[B/(μ-1)]E_(n-2) for n≥2, hence geometrical decay (and exact agreement of z after step 2 for B=0). The Jacobian polynomial in the record is correct; on the homotopy a unit root would imply μ≤1+tB by taking absolute values after division by ξ². Fully invariant compact sets admit bounded bilateral trajectories through every point, and the bilateral contraction is unique, hence there is only the equilibrium singleton. Poincaré recurrence for the possibly noninvertible map rules out invariant probabilities on points tending to infinity or tending to a different point. The witness α=β=γ=0, δ=B gives (μ-1)s=B sin s with opposite signs of the difference near 0 and at π, hence at least three equilibria for each 1<μ<1+B. The invariant zero graph is forward-invariant, not in general mapped onto itself, in agreement with Step 3. At equality the witness has unit multiplier, not three distinct equilibria. check.py was read, not executed.

## originality

PASS

Best of inspected evidence for the concrete strong-feedback all-state coordinate, vertical-fiber conjugacy and sharp uniform threshold for the dynamical collapse, not for the standard scalar variation-of-constants series or a general invariant-manifold theorem. The numerical originating work, earlier stable-manifold theory and the checked global linearization framework do not supply this combination. The elementary sine fixed-point equation is not credited as new in isolation.

## value

PASS

For a published map known from bifurcation plots, a coefficient-uniform threshold that classifies every real orbit and all compact recurrence addresses a natural asymptotic question. The homeomorphic scalar coordinate offers more than a local stability test: it locates the exceptional graph and fixes the sign and amplitude of all other trajectories' escape with a uniform additive error. The scalar witness shows that a uniformly lower threshold cannot give that collapse. This mathematical value is independent of any application of the maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
