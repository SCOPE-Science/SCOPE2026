# Independent mathematical audit

## correctness

PASS

The cubic is the fixed SSPRK(3,3) end-step for a linear generator, with row sum one since Q1=0. Expanding Q as a forward cyclic shift with rate weights minus the diagonal exit-rate matrix, a predecessor entry gets its quadratic term xy and its cubic term −xy(x+y+z); a successor gets x, −x(x+y), x(x²+xy+y²). On a diagonal the cubic return walk gives +abc in addition to −x³. The successor quadratic multiplier has negative discriminant, predecessors become strictly negative together after H=3/S, and r′<0 makes the maximum-rate diagonal the minimum for all h>0. Independently of the Bernstein proof, set z=Mh and k=abc/M³: G(h)/z³=z⁻³−z⁻²+1/(2z)−(1−k)/6 has derivative −((z−2)²/2+1)/z⁴. Thus G can cross only once and does so strictly when G(H)<0. If G(H)=0 the endpoint is still admissible. When rates are equal, H=1/M; otherwise H>1/M and all entries are strictly positive at 1/M, including G=1/3+abc/(6M³). The t-family polynomial follows by substitution and has exactly one crossing for t≥1 since its derivative increases there, changing sign once, while the polynomial starts negative and diverges to +∞.

## originality

PASS

The distinct finding is an all-positive-rate necessary and sufficient endpoint horizon with an explicit branch criterion for the three-cycle. The fixed polynomial, the general SSP guarantee, and the known fastest-exit idea alone are not priority claims. The closest inspected fixed-RK3 directed-cycle theorem excludes n=3 for a reason the algebra makes material: a length-three diagonal return adds an abc term absent for n≥4.

## value

PASS

A three-cycle is the smallest closed one-way Markov network with a missing reverse edge and a full three-step return. This makes it a motivated test of when stage-independent SSP bounds are conservative. The result gives the exact completed-step positivity limit for arbitrary heterogeneity, distinguishes return-diagonal and reverse-edge obstructions, and proves why the answer cannot be obtained simply from the SSP bound or the longer-cycle formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
