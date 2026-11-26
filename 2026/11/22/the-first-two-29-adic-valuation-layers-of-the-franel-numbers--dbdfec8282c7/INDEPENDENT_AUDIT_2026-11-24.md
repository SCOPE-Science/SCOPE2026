# Independent mathematical audit

## correctness

PASS

I reconstructed the unrestricted congruence independently of the named theorem. For p=29 write the binomial arguments as pm+d and pq+s. Terms with s>d are zero after cubing modulo p^2 by Lucas. For s<=d, factor the factorials into p-multiples and p-free factors. Every complete unit block has the same product (p-1)! mod p^2 because the sum of inverses of 1,...,p-1 vanishes mod p; the numbers of blocks cancel. The partial blocks give binom(pm+d,pq+s) = binom(m,q)binom(d,s)[1+p(m H_d-q H_s-(m-q)H_(d-s))] mod p^2, where H_i=sum of 1/j for j=1,...,i. Cubing and using s↔d-s symmetry gives F_(pm+d) = F_m[F_d+pm·3 sum_s binom(d,s)^3(H_d-H_s)] mod p^2. This also treats m=0; cancellation did not assume binom(m,q) is a unit. Replay python3 /workspace/branches/reproduce_franel.py: direct binomial sums for every two-digit index, and independent harmonic coefficients, give Z={12,14,16}, (c,b)=(7,3),(2,4),(5,18), and normalized roots 17,14,11. Histogram for n<841 is (676,154,11). Mod p, iteration makes F_n a unit exactly when T=0. Peeling a non-Z digit preserves the mod-p^2 valuation class since its multiplying factor is a unit. At the first Z digit the higher factor is divisible if another Z digit occurs, forcing p^2. With a unique Z digit the higher factor is a unit; the root 14 at digit 14 would create a second Z digit. At the leading digit the neighbor is zero, not a root. The two remaining forbidden pairs are therefore exactly in least-to-more significant order as stated. Every allowed highest-position exception gives 3·26^(L-1) words; any other position gives (3·26−2)·26^(L−2), and complement counts the ≥2 class. This proves all index lengths, including the stated L=1 base, not the exact valuations in the ≥2 stratum.

## originality

PASS

The supported distinct contribution is the explicit 29-specific valuation-one language, including two genuine neighbor obstructions and the exact length enumerator. The general Gessel–Lucas congruence and the mod-p Lucas mechanism are prior work, and the selection of 29 as type III is already known. The new conclusion requires computing the local zero/derivative data, analyzing the roots under the single-exception condition and counting the resulting language.

## value

PASS

The prime is structurally motivated by the known type-III example. The exact first shell supplies a nontrivial neighbor test that simple counting of exceptional digits cannot give, and yields precise frequencies at every digit length without computing growing-index Franel integers. This is useful even without resolving higher valuation strata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
