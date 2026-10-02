# Prime-length weight-three conflict-avoiding codes through subgroup index 3200

## Statement

For an odd prime \(p>3\), let
\[
H_p=\langle -1,2\rangle\le \mathbb F_p^\times,\qquad
\ell(p)=[\mathbb F_p^\times:H_p].
\]
Then the Ma--Zhao--Shen generator-coset conjecture (equivalently the Hsia--Li--Sun twisted-Fermat formulation) holds for every prime \(p\) with
\[
\boxed{\ell(p)\le 3200}.
\]

Consequently, if \(M(p)\) denotes the maximum size of a length-\(p\), weight-three conflict-avoiding code, then for every odd prime \(p>3\) with \(\ell=\ell(p)\le3200\),
\[
\boxed{
M(p)=
\begin{cases}
\dfrac{p-1}{4},&4\mid \operatorname{ord}_p(2),\\[5pt]
\dfrac{p-1-2\ell}{4}+\left\lfloor\dfrac{\ell}{3}\right\rfloor,
&4\nmid \operatorname{ord}_p(2).
\end{cases}
}
\]
The second line extends the previously published uniform subgroup-index range from \(\ell\le3000\) to \(\ell\le3200\).

## Context

Hsia, Li and Sun (2023) reformulated the relevant construction problem as follows. For
\(H=\langle-1,2\rangle\) and \(\ell=[\mathbb F_p^\times:H]\), it is enough to find a primitive root \(g\) and elements
\[
b\in gH,\qquad c\in g^2H
\]
with
\[
1+b+c=0.
\]
Equivalently, the diagonal equation
\[
g^2X^\ell+gY^\ell+1=0
\]
has an \(\mathbb F_p\)-solution for some primitive root \(g\). Their Theorem 5.2 proves this for every \(\ell\le3000\). Their general sufficient bound is
\[
B(\ell)=\left(2^{\omega(\ell)}(\ell-3-\delta)+2\right)^2-2,
\qquad
\delta=\mathbf 1_{4\mid\ell},
\]
and therefore covers every \(p\ge B(\ell)\). They also cite the earlier computation of Ma--Zhao--Shen verifying the conjecture for primes \(p\le2^{30}\).

A separate 2024 result of Hsia, Li and Sun proves the generator-coset conjecture whenever \(\ell\) is an odd prime, while explicitly identifying composite \(\ell\) as the obstacle for that method.

## Proof

For \(3001\le\ell\le3200\), the 2023 Theorem 5.1 already covers every \(\ell\) having at most three distinct prime divisors: throughout this interval its stated thresholds
\[
\ell<16411\;(\omega=1),\qquad
\ell<8197\;(\omega=2),\qquad
\ell<4100\;(\omega=3)
\]
all apply.

Thus only the following twenty indices remain:
\[
\begin{aligned}
&3003,3010,3030,3036,3045,3060,3066,3080,3090,3094,\\
&3102,3108,3120,3135,3150,3162,3180,3190,3192,3198.
\end{aligned}
\]
Each has four distinct prime divisors.

For each such \(\ell\), primes outside the finite interval
\[
2^{30}<p<B(\ell)
\]
are already covered: the lower side by the Ma--Zhao--Shen computation as reported in the later literature, and the upper side by the Hsia--Li--Sun sufficient bound. It remains only to inspect primes in this interval satisfying
\([\mathbb F_p^\times:\langle-1,2\rangle]=\ell\).

The exhaustive enumeration gives the following numbers of such gap primes:

| \(\ell\) | count | \(\ell\) | count |
|---:|---:|---:|---:|
|3003|5|3102|4|
|3010|5|3108|11|
|3030|5|3120|20|
|3036|13|3135|5|
|3045|13|3150|8|
|3060|14|3162|4|
|3066|2|3180|17|
|3080|11|3190|3|
|3090|3|3192|16|
|3094|5|3198|1|

There are \(165\) gap primes in total.

For every one of these 165 primes, `artifacts/verify.py` deterministically constructs a primitive root \(g\) and explicit \(b,c\) satisfying
\[
b\in gH,\qquad c\in g^2H,\qquad 1+b+c=0.
\]
Hence the generator-coset conjecture holds for every gap prime as well. Combining the four ranges proves the first boxed statement.

For the CAC-size corollary, when \(4\nmid\operatorname{ord}_p(2)\), the Fu--Lo--Shum upper bound is
\[
M(p)\le
\frac{p-1-2\ell}{4}+\left\lfloor\frac{\ell}{3}\right\rfloor.
\]
The generator-coset witness supplies the required \(\lfloor\ell/3\rfloor\) non-equi-difference codewords, after which the standard construction fills the remaining available differences with equi-difference codewords, attaining the bound. When \(4\mid\operatorname{ord}_p(2)\), the classical equi-difference construction already gives \(M(p)=(p-1)/4\).

## Verification

`artifacts/verify.py` independently reproduces and checks all finite claims. It:

1. derives exactly the twenty indices not covered by the cited 2023 analytic conditions in \(3001\le\ell\le3200\);
2. exhaustively enumerates all primes \(2^{30}<p<B(\ell)\) having subgroup index \(\ell\);
3. confirms that exactly 165 such primes occur;
4. constructs and verifies a primitive-root coset witness for every one, and hashes the canonical 165-record witness list.

The recorded output is:

```text
exceptional_indices = [3003, 3010, 3030, 3036, 3045, 3060, 3066, 3080, 3090, 3094, 3102, 3108, 3120, 3135, 3150, 3162, 3180, 3190, 3192, 3198]
gap_prime_count = 165
all_gap_primes_exhaustively_enumerated = True
all_primitive_root_coset_witnesses_verified = True
canonical_witness_sha256 = edbab2e80086c6b2231061e9b0e1d1c3b7590cd99690696826735ad05f16dcc7
```

The verifier uses only exact integer arithmetic. Its Miller--Rabin test uses the deterministic bases \(2,7,61\) in the 32-bit range containing all enumerated candidates.

## Limitations

The new part is a finite certified extension of the subgroup-index range, not a proof of the full generator-coset conjecture for arbitrary composite \(\ell\). It relies on the previously reported verification for primes at most \(2^{30}\) and on the published Hsia--Li--Sun sufficient bound above \(B(\ell)\).

Originality is asserted only to the best of our knowledge. The directly matching 2023 paper states the uniform range \(\ell\le3000\); the 2024 cyclotomic-number paper proves all odd-prime indices but does not subsume the twenty composite indices above. No later source was located that extends the full consecutive index range beyond 3000. The full text of Ma--Zhao--Shen (2014) was not directly inspected here; the precise \(p\le2^{30}\) verification statement is taken from the later Hsia--Li--Sun papers, which explicitly attribute it to that work.

## References

1. H.-L. Fu, Y.-H. Lo, S. W. Shum, *Optimal conflict-avoiding codes of odd length and weight three*, Designs, Codes and Cryptography 72 (2014), 289--309. https://doi.org/10.1007/s10623-012-9764-5
2. W. Ma, C. Zhao, D. Shen, *New optimal constructions of conflict-avoiding codes of odd length and weight 3*, Designs, Codes and Cryptography 73 (2014), 791--804. https://doi.org/10.1007/s10623-013-9827-2
3. L.-C. Hsia, H.-C. Li, W.-L. Sun, *Certain diagonal equations and conflict-avoiding codes of prime lengths*, Finite Fields and Their Applications 92 (2023), 102298. https://doi.org/10.1016/j.ffa.2023.102298
4. L.-C. Hsia, H.-C. Li, W.-L. Sun, *Conflict-Avoiding Codes of Prime Lengths and Cyclotomic Numbers*, IEEE Transactions on Information Theory 70 (2024), 6834--6841. https://doi.org/10.1109/TIT.2024.3439714
