# Independent mathematical audit

## correctness

PASS

The determinant is 1 and the three principal order-two minors sum to 6, with trace 8. The cubic changes sign in each of (0,3/10), (1/2,3/5) and (7,8), so exactly one eigenvalue expands. For times n<m and any two selector labels, right multiplication of the two integer observation rows by A^(−n) leaves one coordinate row and one strictly positive row of A^(m−n). Their rank-two integer map onto the two-torus pushes Haar to Haar. Conditioning on labels independent of the Haar state gives the same product law for every label pair; quantizing preserves independence. With four times, each of the at most 81 label choices gives an image torus of dimension at most three, and a finite union of these is Haar-null in dimension four. This does not give a four-symbol digital law. The transform u=−cos(πt) takes the quadratic update to t↦2 min(t,1−t), whose Lebesgue entropy is one bit. Independence of the invariant initial factors gives the sum of their KS entropies; the stationary digit partition entropy rate cannot exceed that sum, including for the noninvertible tent factor. Independently bisecting the cubic with /workspace/review_replay.py gives λ*=7.184210129198181… and 1+log₂(λ*)=3.844829547729213…; λ*<8 already implies the strict <4 bound. M=256 gives exactly eight bits marginally. Neither the script nor the argument measures the exact rate or says anything about finite-precision implementation.

## originality

PASS

The best-supported distinct claim is the joint exact independence, singularity and quantitative entropy-rate comparison for the specific published switched observation scheme. The generator itself, toral/Haar entropy formulas, factor inequality, and generic existence of pairwise-independent low-rate processes are not new. Inspected analogues have differing dynamics or sensors; none supplies the full joint conclusion for this scheme. Absolute priority was not established.

## value

PASS

The exact generator is independently motivated by its published use and empirical correlation tests. Proving that every lag and selector pair gives perfect two-symbol statistics yet the digit process has fewer than half its marginal bits per sample asymptotically gives a quantitative warning against inferring a rate from pair tests. The significance lies in this conjunction under one natural stationary idealization, not in the standard entropy inequality alone, an exact entropy-rate computation, or any claim about practical security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
