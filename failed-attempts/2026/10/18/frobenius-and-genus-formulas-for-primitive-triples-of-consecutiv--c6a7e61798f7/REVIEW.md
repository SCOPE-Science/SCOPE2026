# Independent mathematical audit

## correctness

PASS

The three binomial coefficients are (n+2)/6 times (U,V,W), so clearing the common gcd gives the same primitive integer vector. Taking gcds of the adjacent pairs gives gcd((n+1)gcd(n,3),(n+3)gcd(n+1,3)); its values for residues 0 through 5 are 3,2,3,6,1,6. The specified paired generators have gcd d; the third is coprime to d by primitivity. Substitution verifies all six z representations, including residue 5 with n=6k−1, where (2k−1)(2k)+k(2k+1)=(6k−1)k. For the unique j in [0,d) with x≡jz mod d, membership is equivalent to (x−jz)/d∈⟨u,v⟩: any larger nonnegative coefficient of z is j+ld with l≥0, and lz∈⟨u,v⟩. Taking the largest gap over these residues proves F; reflection about F replaces j by d−1−j and complements the quotient about uv−u−v, proving symmetry and genus. This includes u=1 and the n=2 normalized triple (2,5,10), with F=3 and g=2. Independent replay `python3 /workspace/reproductions/tetrahedral.py` passed 149 direct binomial/table comparisons (n=2–150) and 59 exact Apéry F,g checks (n=2–60); the proof, not these ranges, handles all n. The frozen verifier actually starts from U,V,W and recomputes a decomposition, contrary to the verification note's literal description of reconstruction from binomial coefficients; the separate replay does test the stated table against binomial coefficients.

## originality

FAIL

A distinct indexed Resultary Finding, 33e5bd0eea32, gives the common-gcd-normalized triple on the same domain n≥2, proves symmetry, and gives six Frobenius cases and the resulting genus via an Apéry description. The frozen table is a gluing parametrization of the same two invariants, not a new claim. The index path is dated earlier than the frozen path; the available passages do not establish the historical order of authorship/publication. The failure rests on demonstrated equivalent coverage, not authorship or chronology inferred from paths.

## value

FAIL

The normalized window is a meaningful cofinite object, but its entire symmetry and exact Frobenius/genus law are already supplied by the matching indexed result, which also gives Apéry data. The gluing re-expression of the same invariants does not leave a distinct useful mathematical claim for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
