# Independent mathematical audit

## correctness

PASS

The affine reduction from any parallelogram to a square preserves independent uniform side parameters. Direct shoelace computation gives T=[1+(U-W)(V-Z)]/2; independent differences have triangular densities 1-|x|. The exact product convolution integrates to f_T(t)=-4(1+|2t-1|)log|2t-1|-8(1-|2t-1|). Integrating the density yields the stated survival function and centered moments. Independently expanding the exact survival in SymPy gives 4 eps^4/3+32 eps^5/15+16 eps^6/5+O(eps^7), confirming both stated tail coefficients. Conditioning on T>1-eps forces X,Y same sign near ±1; four endpoint deficits, scaled by 2eps, lie in the region sum_i x_i-2eps(x1+x2)(x3+x4)<1. Dominated convergence of constant density on the bounded region gives the uniform 4-simplex and five-part Dirichlet(1,1,1,1,1) slack law. Reflection swaps signs with exact 1/2 probability. Package verify.py source checked: Monte Carlo/endpoint-bias diagnostics only; none are used as infinite proof.

## originality

PASS

Fresh best-of-knowledge primary-source and published-mathematics comparison of the exact final theorem, not a claim of exhaustive historical priority. Knowing the first two moments does not imply a probability density or endpoint tail. General polygon iteration convergence does not imply either asymptotic conditional shape theorem.

## value

PASS

The exact full area distribution, shape-independent logarithmic singularity and marked conditional rare-event geometry of a natural one-point-per-edge random polygon are mathematically motivated distributional invariants. The fifth-order endpoint coefficient and five-dimensional Dirichlet mark carry information not supplied by the classical mean or variance alone, and are useful for geometric probability and subdivision models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
