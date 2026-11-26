# Independent mathematical audit

## correctness

PASS

Digit concatenation gives S(bx)=BS(x) at every nonnegative integer cutoff, since b=-1 modulo n. For z an nth root of unity, B takes the z Fourier mode to the z^{-1} mode with factor (1-z^{-1})/(1+z). Hence B² has eigenvalue -((z-1)/(z+1))²; odd n prevents a zero denominator, including when n is composite. The odd part of the binomial expansion kills every nonconstant mode because ((1+u)/(1-u))^n=z^n=1, while P_n(0)=n on the constant mode. This proves P_n(B²)=J_n, then the residue identities. Pairing 2k with 2k+1 gives cancellation with no carry in the even base, including the empty x=0 case. The proof is independent of the finite checks. The inspected verify.py implements exact Horner tests through n=41 and direct digit tests only for residue zero at n=3,5,7; VERIFICATION.md gives expected output, not an independent execution. No uploaded code was run.

## originality

FAIL

A distinct published Resultary record already contains both exact claims, including the matrix identity with the same entries and normalization, every odd modulus, all residues and x=0. The distinct record establishes coverage, not a conclusion about who first proved it. The 2012 works supply important antecedents, but they are not the basis of the duplicate decision.

## value

FAIL

A uniform proof of the Shevelev–Moses conjectures is intrinsically worthwhile, but this record supplies no additional theorem, parameter range, or independent method beyond the matching spectral-projector record. The finite verifier does not add a new mathematical claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
