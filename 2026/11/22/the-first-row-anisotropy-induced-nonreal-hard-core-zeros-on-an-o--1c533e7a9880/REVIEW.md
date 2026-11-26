# Independent mathematical audit

## correctness

PASS

The rung states and their predecessor rules enumerate the weighted independent sets, and row exchange maps (z,t) to (tz,1/t). Independently enumerating two no-adjacent-one rail masks with zero intersection checks every bivariate coefficient through five rungs. I recomputed the discriminants via exact resultants and used exact root counts and gcd checks at t=1 (python3 /workspace/branches/independent_exact.py ladders, SymPy). For t>0 the degree never drops and all coefficients are positive. The first through fourth degrees stay simple and negative by continuity, since their discriminants never vanish. For degree five the normalized discriminant is −G(v), v=(t−1)^2/t; the single sign variation of G and opposite signs at zero and positive infinity give exactly one simple positive root. On t>1 this yields a simple discriminant crossing at T, independently bracketed by 4.01178730250453 and 4.01178730250455. To justify the multiplicity step, the Sylvester determinant of P and its z-derivative would have zero first derivative at any rank defect at least two, so its simple zero forces gcd degree exactly one, hence just one double root. The other three simple real roots persist locally. The sign flip of the discriminant changes the colliding pair to nonreal conjugates; no further collision is possible on that connected outer interval. Reciprocity supplies the other critical point and its outer interval. Strict positivity of the coefficients excludes nonnegative real zeros throughout. Five is the first rung count admitting some positive bias with nonreal zeros, not a claim of nonreal zeros for every bias, every longer ladder or physically positive fugacity.

## originality

PASS

The novelty supported is the all-positive-row-bias boundary, including the first admissible length for nonreal roots and the exact five-rung phase diagram. Scalar recurrence methods cover the symmetric baseline, and claw-free weighted real-rootedness already covers short claw-free cases as far as real-rootedness is concerned. Neither addresses a constrained row-homogeneous bias transition in the clawed ladders.

## value

PASS

Uniform row bias is a natural activity perturbation of a finite-width lattice gas. The sharp first failure shows a genuine gap between isotropic, row-homogeneous and unrestricted-weight real-rootedness; in particular a claw alone does not predict the failure on this slice. The exact location and type of the first collision give a concrete benchmark for zero studies of weighted strips, without making an inference about the thermodynamic limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
