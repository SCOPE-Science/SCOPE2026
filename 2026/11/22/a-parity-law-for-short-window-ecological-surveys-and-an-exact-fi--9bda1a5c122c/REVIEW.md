# Independent mathematical audit

## correctness

PASS

For stationary equal-rate availability, conditioning on the penultimate selected spin repeatedly pairs the even moments; sign symmetry kills the odd moments. This yields positive exponential terms, including one positive single-gap term for each gap, so the Hessian is positive definite. Reversing the ordered observations leaves the objective unchanged, forcing the unique simplex minimizer to be symmetric even on a coincident-visit boundary. At the origin the derivative in gap j is −(1−q^j)(1−q^(n−j))/4 with q=1−p. The maximal magnitude is central because q^j+q^(n−j) decreases toward the middle and increases afterward. The strict derivative ordering against noncentral gaps persists on a sufficiently small simplex for fixed n,p: shifting a positive noncentral gap toward a central one would strictly decrease the miss probability. The two central gaps tie only in odd n, when reflection enforces equality. The n=3 case has only central gaps. For n=5 the positive factor in the differentiated objective leaves the sign of ρu³+u²−K(u+1). This cubic starts negative at zero, decreases to its unique positive minimum and then strictly increases; it is negative at u=K and has sign 1+ρ−2K at u=1. Thus equality at the stated critical horizon is still the unique endpoint-doublet optimizer. At an interior root K=u²(1+ρu)/(1+u)<u², placing the inner intervals strictly above the outer ones. At p=1 the strictly convex log of the all-unavailable path probability gives uniform spacing. The example's phrase 'five gaps' is editorial: the displayed vector and theorem correctly contain four gaps for five visits.

## originality

PASS

The closest works solve the same detection objective at n=3 or n=4 and are properly overlapping cases. Neither derives the all-count Hessian/short-window parity law nor the exact five-visit transition. Broader asymmetric and adaptive frameworks were not exhaustively excluded.

## value

PASS

The objective separates time spent diversifying latent states from repeat detection chances at one state. Exact clustering by parity for every count and the first nontrivial five-visit threshold furnish a reusable baseline for scheduling, including the equality case and ordering after the threshold. This is a mathematical design benchmark for the stipulated model, not a field recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
