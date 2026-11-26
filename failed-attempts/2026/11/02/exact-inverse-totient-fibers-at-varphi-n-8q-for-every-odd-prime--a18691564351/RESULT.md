# Exact inverse-totient fibers at \(\varphi(n)=8q\) for every odd prime \(q\)

## Finding

For every odd prime \(q\), set
\[
\mathcal X_{8q}:=\{n\in\mathbb Z_{>0}:\varphi(n)=8q\},\qquad
r_i:=2^i q+1\quad(i=1,2,3).
\]
Write \([P]S=S\) when proposition \(P\) holds and \([P]S=\varnothing\) otherwise. Then the **complete inverse-totient fiber** is
\[
\boxed{\mathcal X_{8q}=\begin{cases}
\{35,39,45,52,56,70,72,78,84,90\},&q=3,\\
\{41,55,75,82,88,100,110,132,150\},&q=5,\\
[r_2\text{ prime}]\{3r_2,4r_2,6r_2\},&q\ge7,\ q\equiv1\pmod3,\\
[r_1\text{ prime}]\{5r_1,8r_1,10r_1,12r_1\}
\cup[r_3\text{ prime}]\{r_3,2r_3\},&q\ge7,\ q\equiv2\pmod3.
\end{cases}}
\]
The unions are disjoint. In particular, for \(q\ge7\),
\[
|\mathcal X_{8q}|=\begin{cases}
3\,\mathbf 1_{\{4q+1\text{ prime}\}},&q\equiv1\pmod3,\\
4\,\mathbf 1_{\{2q+1\text{ prime}\}}+2\,\mathbf 1_{\{8q+1\text{ prime}\}},&q\equiv2\pmod3.
\end{cases}
\]
The attainable fiber sizes in the whole prime family are \(0,2,3,4,6,9,10\). Their positive nonexceptional values are exactly \(2,3,4,6\), conditional on the indicated primality tests. This determines every solution, not just the size of the fiber.

## Assumptions and scope

The variable \(q\) ranges over all odd rational primes. The function \(\varphi\) is Euler's totient, with \(\varphi(1)=1\), and the inverse fiber consists of **positive integers**. No primality or congruence assumption is imposed on any auxiliary \(r_i\); each conditional set is included only when its specified candidate is prime. The exceptional sets at \(q=3,5\) are included for completeness, but these individual small totient fibers were already tabulated in the 2025 paper cited below. The unrestricted classification for primes \(q\ge7\), not those tabulated exceptions, is the contribution.

## Proof

**Prime support for \(q\ge7\).** Fix such a prime and suppose \(\varphi(n)=2^3q\). If a prime \(\ell\mid n\), then \(\ell-1=\varphi(\ell)\) divides \(\varphi(n)=8q\). Every divisor of \(8q\) is among \(1,2,4,8,q,2q,4q,8q\). The candidate \(q+1\) is even and greater than two, and the candidate \(9\) is composite. Therefore the actual primes dividing \(n\) lie in
\[
\{2,3,5\}\cup\{r_i:1\le i\le3,\ r_i\text{ prime}\}.
\]
For \(\ell=3\), a squared factor would make \(\varphi(9)=6\mid8q\), impossible since \(q\ne3\). Similarly \(\ell=5\) cannot occur squared because \(\varphi(25)=20\nmid8q\) when \(q\ne5\). Each prime \(r_i\), when present, occurs only to exponent one: a square would require \(r_i\mid8q\), whereas \(r_i=2^iq+1\) is an odd prime larger than \(q\). Thus uniquely
\[
n=2^u3^a5^b\prod_{i=1}^3r_i^{e_i},\qquad
u_2(\varphi(2^u))=h(u):=\begin{cases}0,&u=0,1,\\u-1,&u\ge2,\end{cases}
\]
where \(u\ge0\), \(a,b,e_i\in\{0,1\}\), and \(e_i=0\) whenever \(r_i\) is composite. All factors in this decomposition are distinct primes except the displayed power of two.

**The exact valuation equations.** Multiplicativity and \(\varphi(r_i)=2^iq\) give
\[
\varphi(n)=2^{h(u)+a+2b+e_1+2e_2+3e_3}\,q^{e_1+e_2+e_3}.
\]
Comparing the exact \(q\)-adic valuation yields
\[
e_1+e_2+e_3=1.
\]
Thus precisely one prime \(r_i\) occurs, and the remaining equation is
\[
h(u)+a+2b=3-i.
\]
For \(i=1\), its complete solution set gives multipliers \(2^u3^a5^b\) equal to \(5,8,10,12\). Indeed, either \(b=1,h=a=0,u\in\{0,1\}\), or \(b=0\) with \((h,a)=(2,0)\) or \((1,1)\). For \(i=2\), the complete multiplier set is \(3,4,6\): here \(b=0\), and \((h,a)=(0,1)\) or \((1,0)\). For \(i=3\), the complete multiplier set is \(1,2\): all of \(h,a,b\) vanish. Each multiplier is coprime to its corresponding prime \(r_i>5\), so the displayed products have the required totient; the preceding valuation argument excludes every other possibility.

**The residue-class dichotomy.** Because \(q\ge7\) is prime, \(q\equiv1\) or \(2\pmod3\). If \(q\equiv1\pmod3\), then \(r_1=2q+1\equiv0\pmod3\) and \(r_3=8q+1\equiv0\pmod3\). Both exceed three, hence neither is prime; only the \(i=2\) family can survive. If \(q\equiv2\pmod3\), then \(r_2=4q+1\equiv0\pmod3\) and is composite, leaving independently the \(i=1\) and \(i=3\) families. Since their unique large prime divisors are different, these two families are disjoint. This proves both the set formula and the cardinality formula for every \(q\ge7\).

**Exceptional primes.** For \(q=3\), the divisibility \(\ell-1\mid24\) restricts prime divisors to \(\{2,3,5,7,13\}\). The only possible exponents are \(0\le u\le4\) for \(2\), \(0\le a\le2\) for \(3\), and zero or one for each of \(5,7,13\); these restrictions follow from \(\varphi(2^5)=16\nmid24\), \(\varphi(3^3)=18\nmid24\), and the prime-power totient formula. Solving the finite product equation
\[
\varphi(2^u)\varphi(3^a)\varphi(5^b)\varphi(7^c)\varphi(13^d)=24
\]
under those exponent bounds gives exactly the ten integers in the first line of the theorem. For \(q=5\), prime divisors are among \(\{2,3,5,11,41\}\); allowed exponents are \(u\le4\), exponent of \(3\le1\), exponent of \(5\le2\), and those of \(11\) and \(41\le1\). The analogous product equation with right side \(40\) yields exactly the nine integers in the second line. These small lists are independently known from the published 2025 totient-fiber table; the finite derivation specifies the exhaustion mechanism rather than treating that table alone as an infinite proof.

## Verification

The standalone file `VERIFY.py` implements a standard independent totient sieve. For every odd prime \(q\le2000\), it enumerates the inverse fiber and compares it **as a set** with the closed formula above, including the two exceptional primes. The checked range contains 302 primes, 503 preimages, and all seven allowed size values; it also checks a larger search boundary for the largest prime. The program prints

```text
VERIFY_OK primes=302 q_max=2000 independent_totient_sieve=yes cardinality_histogram=[(0, 158), (2, 33), (3, 52), (4, 40), (6, 17), (9, 1), (10, 1)] checked_preimages=503 enlarged_boundary=yes
```

The finite search bound is justified independently of experimentation: the allowed prime support and the unique occurrence of one \(r_i\) give \(n/\varphi(n)<6\) for \(q\ge7\). The finite exceptional supports yield the same bound for \(q=3,5\). Thus a sieve through \(6(8q)\) really does exhaust each **tested** fiber, although testing finitely many \(q\) does not prove the infinite theorem. The unrestricted proof is the valuation classification above.

## Relationship to prior work

Shannon, Shiue, He and Saito (2025) study inverse totient fibers, including \(\mathcal X_{4q}\) for primes \(q\equiv1\pmod6\) (Theorem 2.3.1), and record the small fibers at totient values \(24\) and \(40\) (Table 1). Their general inverse-totient methods motivate the present exact parametrized classification but do not state its formula for \(\mathcal X_{8q}\) over all odd primes. He (2026), in §5 and Open Problem 16, explicitly treats the whole \(\mathcal X_{2^sq}\) problem for \(s\ge3\) as open; his Table 2 gives some isolated cardinalities for \(s=3\) but no general classification. The present theorem resolves the initial \(s=3\) slice, including simultaneous primality of \(2q+1\) and \(8q+1\) in the \(q\equiv2\pmod3\) branch.

It was already known that an Euler-totient fiber cannot be a singleton when its value is not divisible by \(32\) (the Grosswald divisibility restriction cited in Shannon et al.). Accordingly, the non-singleton consequence for \(8q\) is **not claimed as novel**. What is determined here is the full fiber and its exact multiplicity in each arithmetic case. Generic inverse-totient algorithms and finite sequence tables likewise do not, by themselves, state this parametrized classification.

## Limitations

The theorem gives no classification for \(\varphi(n)=2^s q\) when \(s\ge4\), nor any statement about how frequently the auxiliary expressions are simultaneously prime as \(q\) varies. The conditional cardinalities require only explicit primality tests, not unproved conjectures on primes. Priority cannot be certified by searching a finite collection of sources: a differently worded historical classification or an implicit specialization of an older general theorem remains possible. Independent mathematical review has not been performed.

## References

1. A. G. Shannon, P. J.-S. Shiue, T.-X. He and C. Saito, *On the special cases of Carmichael's totient conjecture*, Notes on Number Theory and Discrete Mathematics 31 (2025), 504–534. DOI: 10.7546/nntdm.2025.31.3.504-534. Online first 2025-08-15. https://www.nntdm.net/papers/nntdm-31/NNTDM-31-3-504-534.pdf
2. T.-X. He, *The Family \(X_{qp^s}\) for Distinct Primes \(q,p\) in Connection with Carmichael's Totient Conjecture*, arXiv:2610.34808v1, submitted 2026-10-26; §5, Proposition 15, Table 2, Open Problem 16. https://arxiv.org/abs/2610.34808
3. OEIS A032447, inverse function of Euler's totient; tabulated sequence values, not an infinite classification. https://oeis.org/A032447
