# Independent mathematical audit

## correctness

PASS

Read RESULT.md blob 5b93c8c64a722d1d110d46afd4ce97f7c00d10d5 and both exact/auxiliary verifiers. Formula (5) gives nonnegative hollow X with each row and column sum 1 even k=1,n. On positive positions P-X equals u_i+u_j with potentials u_F=-(k+2)/(2D), u_M=k/(2D); on every zero allowed cell P-X<=u_i+u_j. Therefore <P-X,Y-X><=0 for every feasible Y and strict Euclidean projection uniqueness follows; exact squared norm produces f_n(k). Direct differentiation yields f_n increasing on 0..n; k=n-1 impossible, k=n-2 transpositions and f(n)-f(n-2)=2. Convexity under Birkhoff decomposition gives the unique full-body Frobenius farthest point. Conjugation-average of any hollow feasible X is U=(J-I)/(n-1); restriction of P-U to 1-perp has singular values |lambda+1/(n-1)|, at most n/(n-1) with all equal only at P=I, proving Schatten formula and finite-p uniqueness. For 1<p<infinity strict convexity gives U; operator-norm equality requires vanishing skew part and U; trace-nuclear equality for I-X requires PSD, equivalent to X symmetric, producing affine dimension n(n-3)/2. Independent rational KKT implementation checked all permutations n=3..6; does not replace n-general inequalities. No claim for spectral farthest-point uniqueness or continuous-body gap.

## originality

PASS

Best-of-knowledge originality; four explicit comparisons and actual primary-source material inspections below. The old fixed derangement-to-center radius is numerically different from the present identity-to-face Hausdorff radius. Neither contains the exact universal KKT projection formula or nuclear nearest-point locus.

## value

PASS

The crown-graph perfect-matching polytope is a canonical restrictive face of the Birkhoff polytope. A full vertex-to-face metric spectrum, exact worst-case Hausdorff separation across Schatten norms, sharp discrete separation of the first two assignment classes and a nontrivial nuclear optimizer polytope are natural reusable geometry; this is not only a restatement of derangement counting or an enclosing radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
