# Independent mathematical audit

## correctness

PASS

With probability surface measure, T_s acts as s^n on exact degree n. Multiplication by a coordinate links only degrees n−1 and n+1, since the Laplacian of its product with a homogeneous harmonic H_n is twice the directional derivative of H_n, and subtracting |x|² times that derivative divided by 2n+d−2 gives a harmonic. Degree zero links only to degree one, also on the circle. Thus on each allowed block s^(2m)+s^(2n)=(s+s⁻¹)s^(m+n). This gives T_s[aI+(s+s⁻¹)M_v]T_s, and comparison of continuous kernels gives the bridge moment. The multiplier has minimum a−(s+s⁻¹)||v||, so a nonnegative minimum suffices for finite Gram positivity. If the multiplier is negative in a cap, approximate a nonzero test function supported there by a spherical polynomial and invert T_s on that polynomial. Its integral quadratic form is negative, which continuity transfers to a finite Gram witness by quadrature. At a nonzero admissible parameter the multiplier is positive almost everywhere, including at equality when it vanishes at just one pole. Smoothing a nonzero atomic finite measure by T_s cannot identically vanish: it multiplies each harmonic moment by the nonzero s^n, and polynomial density separates measures. This proves finite-site strictness for distinct sites and the zero-kernel exception. Independently checked a negative direct Gram form on the circle at r=1/4, a=1, ||v||=9/20, with 101 distinct sites and Fourier-polynomial weights; its high-precision numerical value is −0.0384615384615384615384615, consistent with the exact continuum witness −1/26. The finite test is not used for the general cone.

## originality

FAIL

The distinct indexed axial-tilt finding 2c30314f81a3 covers exactly the nontrivial normalized cone, the bridge factorization, and strict finite-site positivity on every sphere of intrinsic dimension at least two; it additionally proves universality, stronger than the asserted strictness. To compare parameters, write the current sphere S^(d−1) as S^q with q=d−1, and for a>0 and v≠0 set u=v/||v|| and ε=||v||/a in that work. Its kernel multiplied by a is exactly the present kernel, with threshold a≥(1+r)||v||/√r. For a<0 the current diagonals fail somewhere, a=0 and v≠0 also fails, and v=0 is just a scalar Poisson kernel. The vector bridge identity follows by subtracting the Poisson semigroup term and comparing the coefficient of ε for each unit u. The present circle case lies outside the literal statement of the indexed result, but its proof carries over by substituting the Fourier eigenvalues s^|n| and the shifts n→n±1 for coordinate multiplication. Each such shift changes |n| by one, and all the density, cap, and strictness arguments apply unchanged. Thus this is material demonstrated coverage and an elementary adaptation, not an adverse inference from an unavailable source or from index ordering alone.

## value

FAIL

A sharp PSD cone and its boundary strictness are meaningful covariance questions, but the frozen record adds no independently valuable scientific remainder to the existing exact normalized classification. Scaling and isolating the bridge coefficient restate its result; the circle addendum is the identical adjacent-degree calculation with basic Fourier modes and has neither a new cutoff nor a new critical phenomenon. The finite circle example illustrates already established necessity rather than resolving a distinct, motivated finite-site question. A presentation clarification or narrower scope would not supply a surviving distinct valuable claim, so no repair is delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
