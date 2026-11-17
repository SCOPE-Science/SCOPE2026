# Independent mathematical audit

## correctness

PASS

For every integer L>=5, the actual unit-edge graph C_(2L)+{0,2}+{L,L+2} has a reflection-even positive rank-two perturbation of the bare-cycle adjacency matrix and reflection-odd nonpositive perturbation. The cycle resolvent G(k)=(q^k+q^(2L-k))/[(q^(-1)-q)(1-q^(2L))], lambda=q+1/q>2, yields independent symmetric/antisymmetric scalar Birman-Schwinger equations F(q)(1±q^(L-2))/(1∓q^L)=1. Their monotonicity in lambda and the antisymmetric threshold (L-2)/2>1 prove exactly two simple adjacency eigenvalues above 2. Expansion at q_*^3+q_*^2+q_*-1=0 gives the claimed C_*q_*^L splitting; conjugacy of MERW P to A/lambda_1 gives the exact positive-mode time. Bare-cycle and one-chord comparisons use interlacing, and uniformly bounded degrees plus a sine test function give ordinary-walk gap Theta(L^-2). Independent NumPy eigensolutions and separate scalar-root bisections on L=5,6,9,12,20,30 matched both top roots within 1e-9, no third eigenvalue exceeded 2, and L=20/30 gap/C_*q_*^L approached 1. Finite tests do not prove every L.

## originality

PASS

The established MERW framework, defect localization and even exponential trapping in *other* graphs are previous work. Novelty survives only for the sharp comparison on an otherwise simple cycle with two added span-two chords, exactly two above-band states, explicit algebraic splitting prefactor, and bounded-versus-exponential-versus-diffusive positive-mode contrast. No inspected earlier primary result directly entails those fixed-cycle formulas; this is a best-of-knowledge verdict.

## value

PASS

Two edges of fixed local span, at opposite ends of a natural cycle, change the positive subleading MERW spectral time from the one-edge bounded regime to exponential in separation; removing both edges gives diffusive L². The full asymptotic prefactor and exactly-two-bound-states proof make a useful elementary benchmark for localized-state tunneling and distinguish entropy-weighted walks from degree-normalized walks. This is a motivated sharp graph-family boundary rather than an arbitrary finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
