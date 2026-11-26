# Independent mathematical audit

## correctness

PASS

RESULT.md lines 4–83: permutation averaging preserves all constraints and cannot increase the Fourier l1 norm even for complex values. A radial coefficient at layer j gives shell evaluations 1, 1-2j/n, and 1-4j(n-j)/(n(n-1)); at size two the character is negative exactly when one of the two coordinates lies in the subset, with probability 2j(n-j)/(n(n-1)). Hence the three signed moments are (1,0,Q) in (1,j,j(n-j)). Eliminate b_n via the first moment, writing X=(n-r)b_r and Y=(n-r-1)b_{r+1}; the other moments give X+Y=n and rX+(r+1)Y=Q. Thus X=n(r+1)-Q and Y=Q-nr have the stated signs; b_n<=0. The norm 1-2b_n yields the displayed value. At each integer j, the product (j-r)(j-r-1) is nonnegative and its upper bound is the larger convex endpoint value, D, because r<=(n-1)/2. Thus P_r is bounded in modulus by 1, with the required signed contacts; its pairing is exactly the claimed value by the moments, regardless of complex phases. This proves optimality over all admissible extensions, with at most three nonzero layers. Denominators are positive even for n=2. At a switch Q=nr, adjacent affine branches both take 1+2r/(n-r); D decreases across the switch, increasing the slope. A switch at d=2 is not interior, and at d=0 the optimizer is constant. Independent replay `python3 -I /workspace/review-work/replay.py 5` matched 186 exact grid optima through n=11, including switch targets, by enumerating Vandermonde-basis supports for the raw moments (1,0,-Q). For the real linear program split into positive and negative parts, an optimal basic solution has at most three nonzero signed entries, so this is an independent finite computation, not a proof of all dimensions and t. The supplied checker was inspected but not executed.

## originality

PASS

The supported distinction is the explicit exact extension cost and contact staircase on the finite discrete grid, not permutation averaging, Krawtchouk transforms, finite moment duality or the generic existence of an optimizer supported on at most three layers. The closest inspected Hamming-ball, signed moment and analytic-Wiener results change the objective, moment setting or domain. Generic finite c-optimal design supplies an equivalent LP but no available statement identifying these contacts and their floor law.

## value

PASS

For a natural Fourier-algebra interpolation problem on the first Boolean ball with a freely variable second-order profile, the minimum spectral l1 norm is the quantitative cost of enforcing these local data. The exact expression controls both that cost and the changing optimal signed layers, including arithmetic phase boundaries at all dimensions. This is not a single parameter slice or a generic LP existence result. No classification of all optimizers, higher Hamming data, or other alphabets is needed or implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
