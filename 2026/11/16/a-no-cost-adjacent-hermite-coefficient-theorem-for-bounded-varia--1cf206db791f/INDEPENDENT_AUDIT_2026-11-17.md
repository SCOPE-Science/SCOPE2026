# Independent mathematical audit

## correctness

PASS

Rodrigues and Stieltjes integration by parts give a linear map from df to the primitive vector v=(phi He_{n-1}/sqrt(n!),phi He_n/sqrt((n+1)!)); its BV→Euclidean norm equals sup_x ||v(x)||, attained by a unit jump. Let y=phi He_{n-1}/sqrt(n!), then y′=-phi He_n/sqrt(n!), y″+xy′+ny=0. The energies F=y²+y′²/(n+1), H=y²+y′²/n satisfy F<=H and H′=-2x y′²/n, making H strictly decrease away from 0. For odd n, He_n(0)=0 gives unique F maximum at 0. For even n, Hermite even root product and sum reciprocal squares imply He_{n-1}(x)/He_n(x)<-x on (0,r_1), so F′>0 until first root; outside, F<=H<H(r_1), giving exactly ±r_1. Triangle-equality supports classify all positive variation extremizers, with opposite jumps at even ±r_1. At those roots He_{n+1}=-nHe_{n-1}≠0, so third component increases the sharp norm. Recomputed root-maxima/third-block strictness n=1..16; not a proof of all n. Checker itself uses sympy/numpy/scipy, contrary to any expectation of standard-library-only replay.

## originality

PASS

BV duality for vector blocks is a standard reduction, yet the exact global 2-mode Euclidean maximum and its largest zero-root support are additional Hermite inequalities. The existence of an older Sonin two-mode identity remains an equivalence risk. A generic vector-valued primitive supremum principle alone does not solve exact finite Hermite optimization. The sharp joint theorem and block-length threshold were not shown by inspected scalar sources, but an older energy reinterpretation might. The joint no-cost estimate and abrupt three-mode obstruction refine prior individual sharp bounds. Even if the vector primitive formula is textbook duality, identifying precisely the minimizing parity-root locations and equality structure uses nontrivial Hermite analysis.

## value

PASS

A sharp infinite-degree simultaneous coefficient bound for a natural Gaussian orthogonal basis requires no loss relative to one mode, classifies all extremizing jumps and shows precise failure at the next mode. This is a concrete, non-textbook, useful boundary of BV coefficient control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
