# Independent mathematical audit

## correctness

PASS

For every coprime positive p,q with q>=2, write n=qk+r. The Bezout matrix [[U,V],[-p,q]] is unimodular and converts gcd(n,floor(pn/q)) to gcd(k+Ur+V floor(pr/q), pr mod q). Nonzero residual values permute 1,...,q-1 and each divides L=lcm(1,...,q-1), so every qL-block has per-fiber counts (L/d)Σ_{j<=floor((q-1)/d)}φ(j)/j. The r=0 fiber contributes indicator(BL<d<=(B+1)L), since gcd(qk,pk)=k. Averaging blocks yields delta_q and lost mass 1/q; Möbius inversion gives fixed-d limit 1/(ζ(2)d²) with O(log q/(dq)). Independently enumerated q=5 reduced numerators and B=0,1,2 with exact agreement.

## originality

PASS

The unimodular residue-class reduction yields exact numerator-independent full gcd histograms on every block of q*lcm(1,...,q-1), including escaping 1/q mass. Prior literature supplies irrational polynomial coprimality densities and p=1 gcd=1 tables; those cannot imply every positive gcd value for every numerator on every finite block.

## value

PASS

The full finite-block gcd histogram of the natural correlated pair (n,floor(pn/q)) is a motivated exact arithmetic invariant: the SL2Z invariance explains why every reduced numerator has identical counts, and the pointwise density loses exactly 1/q mass despite approaching the zeta coprimality profile as q grows. Previous gcd-one tables neither determine every fiber nor the mass-escape mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
