# Independent mathematical audit

## correctness

PASS

The setting is four distinct integer residues modulo nine and unweighted rows multiplied by 1/2, so if D is the unscaled determinant its squared modulus is divided by 256. With w_j=z^(2λ_j), substitute the four-root monic polynomial for w_j^4 in the last column of the alternant (1,w,w³,w⁴); after removing repeated columns and swapping the last two one obtains the Vandermonde times e_2. I independently enumerated all 126 cases with a subset-DP determinant in the group ring of Z/9, cyclic autocorrelation for D times its conjugate, and reduction by z^6+z^3+1. This reproduced the entire 14-row orbit list including all three optimizing representatives, the class counts 18,27,27,27,27, and the squared value 81/256 for each of the four restricted digit towers. Translates preserve modulus by row phases and act freely: any nontrivial stabilizing translation partitions the set into orbits of size 3 or 9, impossible for size 4. In the exact cyclotomic field t=z+z^(-1), its cubic x³−3x+1 is increasing for x>1 and t is the root with 3/2<t<8/5. The stated ordering follows by comparing 0,2−t,4−t²,3,t+t². The maximum is the positive square root of its squared class, with decimal 0.6396513989643324… and ratio sqrt((t+t²)/3) to the tower value 9/16. Replay: python3 /workspace/branches/recheck_1.py. The submitted checker was inspected but not executed. No statement is made about real frequencies, conditioning or higher depths.

## originality

PASS

The supported contribution is the nonzero determinant-magnitude stratification with exact multiplicities and the complete unrestricted optimum and optimizer classification at this depth, together with the resulting strict comparison to the already-known restricted benchmark. The alternant, non-full-spark fact, tower value, and rank/zero information are not credited as independent novelties. The strongest same-grid positional-incidence prior mechanically covers the zero stratum through its all-mask rank computation, but that computation returns ranks, not positive determinant magnitudes.

## value

PASS

This is the first nontrivial Cantor depth at which the natural digit-tower restriction can be tested against all integer-grid frequency sets; at depth one every two-element frequency set reduces by translation to a binary one-digit choice. The depth-two census gives a sharp strict counterexample to extending tower optimality to unrestricted designs and classifies all winners, not just a single computed improvement. The four positive volumes and their counts add determinant information beyond the existing ranks and are useful as a finite benchmark without claiming an infinite-frame consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
