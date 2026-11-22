# Independent mathematical audit

## correctness

PASS

On binary words length 2m (odd m>=3) with Hamming weight exactly m, any proper repetition count r divides m, hence is odd >=3 and its fundamental block has length 2a and weight a where a=m/r<=m/3. Therefore excluded periodic words are at most S_m=sum_(a<=floor(m/3))binom(2a,a). Complement x→x+1 preserves both period and central weight and forces W(s)=0 for every odd-weight s. For the FULL central sphere, Krawtchouk duality gives K_m(2j;2m)=(-1)^j binom(2m,m)binom(m,j)/binom(2m,2j), whose minimum absolute even-weight coefficient is M_m=(m+1)/m binom(m,(m-1)/2); the adjacent ratio A_(j+1)/A_j=(2j+1)/(2m−2j−1) proves the minimum. M_m>S_m by exact m=3,5,7,9,11 base cases and the strict growing exponential bound for m>=13, so removing periodic words cannot introduce even-frequency zeros. Thus rank=nullity=2^(2m−1), and image is precisely complement-invariant. For odd prime m=p the only excluded balanced words are the two alternating ones, giving W_p(s)=K_m(|s|;2m)−2epsilon for even |s|, exact epsilon multiplicities from the coefficient of z^(2j) in (1−z)^p(1+z)^p, sharp gap M_p−2 and maximum binom(2p,p)−2. Since S_m=O(4^(m/3))=o(M_m), Stirling yields κ~2^m/sqrt(2). Independent exhaustive direct period filtering and integer FWHT at m=3,5,7 confirmed exact parity support, prime minima 2,10,38 and rank 32,512,8192. These checks corroborate but the full proof handles all odd m.

## originality

PASS

PASS for fixed-weight primitive binary subfamily: unrestricted primitive-word support theorem and full Hamming central-slice Krawtchouk formula are separate facts; neither alone controls Fourier cancellations after deleting exactly the periodic balanced words. The relative deletion gap and sharp prime formula supply the nontrivial connection.

## value

PASS

Half-weight aperiodic binary words are a canonical combinatorial ensemble. The fact that deleting every periodic point preserves ALL parity-allowed Fourier modes is a robust spectral stability result not a routine number count; it gives a complete rank classification at every odd half-length and an exact sharp prime signed-spectrum/conditioning calculation, together with meaningful asymptotic amplification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
