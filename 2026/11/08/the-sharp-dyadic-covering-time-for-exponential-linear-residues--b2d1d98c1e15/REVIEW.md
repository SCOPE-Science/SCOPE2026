# Independent mathematical audit

## correctness

PASS

For odd a, n−t odd implies parity mismatch, n−t even with v2(n−t)=v ensures a^(n−t)−1 divisible by 2^(v+2); hence v2[(a^n+bn)−(a^t+bt)]=v2(n−t), giving a residue permutation in the first m terms. For even a, a^n≡0 mod2^k for n>=k, so m consecutive indices from k provide universal upper bound m+k−1. Sharpness avoids the one missing residue b(k−1) among indices through m+k−2: small k verified explicitly; for k>=7 random a=2u and C2×C_{2^(s−2)} power-map fibers give union bound 2^(2−k) Σ_{n<=floor(log2(k−2))}n2^n<1, hence an even sharp witness. Independently exhausted every a mod2^k, odd b mod2^k for k<=8 with exact pow modular arithmetic, finding maxima 2,5,10,19,36,69,134,263 and no bad odd-base cases. Infinite theorem rests on proof, not finite tests.

## originality

PASS

Sun proves coverage in first m² terms for coprime b, a substantially weaker and more general modulus theorem. Rivest studies permutation polynomials, not exponential-plus-linear words. Earlier power-of-two exact worst-case m+log2(m)−1 covering was not found in searched sources and is not an immediate corollary of general Sun bound.

## value

PASS

Exact optimal horizon and unavoidable delay for modular exponential-linear sequences in a natural dyadic regime, with clean odd/even phase distinction and all-k proof. Useful for arithmetic covering and residue sequence structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
