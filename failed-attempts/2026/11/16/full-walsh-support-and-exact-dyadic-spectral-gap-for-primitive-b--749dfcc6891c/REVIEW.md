# Independent mathematical audit

## correctness

PASS

Reconstructed primitive-word indicator via divisor Möbius inversion and subspace orthogonality: W_n(b)=sum_{d|n} mu(n/d)2^d 1_{H_d}(b). With r=rad(n),m=n/r only d=mt with t|r survive; b outside H_m has W=0, inside H_m the isolated d=m term is mu(r)2^m modulo 2^(m+1), giving exact v2=m. The explicit b=e_0+e_m (valid n>=2m) isolates magnitude 2^m, and Fourier support H_m entails translation stabilizer V_m and convolution rank 2^(n-m), pseudoinverse norm 2^(-m). Direct independent brute force primitive indicators plus integer Walsh butterfly checked all multipliers/support/gap for n=2..9; the universal conclusion rests on the proof, not that finite check. RESULT.md and verify.py read at assigned Git tree and their Git blobs and exact tree verified.

## originality

FAIL

The current all-n binary support, gap, convolution rank and stabilizer classification is already a special case of the published all-finite-abelian-alphabet theorem. Its stated general multiplier formula specializes at H=F_2 to exactly W_n and its sharp minimum; the exact dyadic valuation follows immediately from the specialized first nonzero m-term with parity-separated higher powers. Identical scientific content does not become original through a stronger congruence phrasing or numerical verification. Same-day publication implies no personal priority judgment.

## value

FAIL

The full binary theorem has mathematical meaning but is already covered by an explicit stronger all-abelian-alphabet result; its valuation is a short arithmetic consequence of that existing formula. No separate unproved boundary, new classification, or independent exact invariant remains that would supply distinct incremental research value. Correctness and reproducibility cannot substitute for originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
