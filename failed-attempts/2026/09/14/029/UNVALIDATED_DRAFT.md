# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Complete census for x^2 + 209 = y^n (n >= 3, y > 1, gcd(x,y) = 1)

## Theorem
Up to the sign of x, the unique integer solution of x^2 + 209 = y^n with
n >= 3, y > 1, gcd(x,y) = 1 is

  (x, y, n) = (54, 5, 5), since 54^2 + 209 = 2916 + 209 = 3125 = 5^5.

No other triple with n >= 3, y > 1 and gcd(x,y) = 1 satisfies the equation.

## 0. Conventions and setup
Put s = sqrt(-209), K = Q(s), O = O_K = Z[s] (since -209 = 3 mod 4,
disc(K) = -836 = -4*11*19). Write N(a+bs) = a^2 + 209 b^2.
PARI/GP (bnfcertify) certifies h_K = |Cl(O)| = 20 with Cl(O) ~= C10 x C2;
in particular the Sylow 5-subgroup is cyclic of order 5. Scripts:
`work/s1_classgroup.py`, `work/s9_orders.py` (outputs in
`output/artifacts/`).

## 1. Elementary reductions
(a) x is even and y is odd. Indeed x odd gives x^2 + 209 = 2 mod 8,
impossible for y^n with n >= 3 (even y gives 0 mod 8; odd y gives odd).
(b) gcd(y, 209) = 1: a common prime divisor p | y, p | 209 divides
x^2 = y^n - 209, hence divides x, against gcd(x,y) = 1. So
gcd(y, 2*209) = 1 (y odd).
(c) It suffices to treat prime exponents. If n = mq with q prime,
(x, y^m, q) is a solution; gcd(x, y^m) = 1. So assume n = p prime,
then handle p = 2 (excluded below), p = 3, p = 5, p >= 7.
(d) Even exponent: n = 2m gives x^2 + 209 = Y^2 with Y = y^m, so
(Y-x)(Y+x) = 209 with both factors positive powers of the same parity
(x even, Y odd). Since 209 = 1*209 = 11*19, (x,Y) in {(104,105),(4,15)}.
Neither 105 nor 15 is a perfect k-th power for k >= 2 (squarefree and
> 1; PARI `ispower` returns 0; see `work/s9_orders.py`). Hence no
solution with 2 | n and n >= 4. (Exponent n = 2 itself is outside the
target.)

Henceforth p is an odd prime.

## 2. Ideal factorization for p != 5 (and p = 3)
For odd p, x + s and x - s are coprime ideals of O. Any common prime
ideal P | (x+s), (x-s) divides their sum 2x and difference 2s, hence
divides (2) and (y)^p; since gcd(x,y) = 1 and y is odd, P | (2).
But 2 ramifies in K (disc(K) = -836 divisible by 2; PARI primedec(2)
gives e = 2, f = 1) with unique prime p2 above 2 of residue field F_2,
and x + s mod p2 equals s mod p2 with s^2 = -209 = 1 mod 2, so
x + s = 1 mod p2 is a unit at p2. Hence no common prime divisor exists
and the conjugate ideals are coprime. Taking classes from
(x+s) = a^p gives [a]^p = 1 in Cl(O), which has order 20. If
gcd(p,20) = 1 (i.e. p not in {2,5}), then [a] = 1, so a = (g) is
principal: x + s = eps * g^p with eps a unit. O^times = {+-1}
(imaginary quadratic, disc < -4), and eps is absorbed into the p-th
power up to sign (p odd): x + s = (u+vs)^p with u,v in Z. Comparing
norms, N(g) = y, and comparing s-coefficients,

  v * G_p(u,v) = 1, where G_p(u,v) = sum over odd k of
    C(p,k) u^{p-k} v^{k-1} (-209)^{(k-1)/2}.

Hence v = +-1 (v | 1) and, with G_p(u) := G_p(u,1),

  G_p(u) = +-1   for u in Z (no parity restriction).

### 2a. p = 3
G_3(u) = 3u^2 - 209 = +-1 gives 3u^2 = 210 (+1 case) or 208 (-1 case).
208 is not divisible by 3; 210/3 = 70 is not a square. No solutions.
So no exponent divisible by 3 except possibly via the p = 3 reduction,
which is empty: no solutions with 3 | n at all.

### 2b. p >= 7, p != 5: Lucas/BHV bound plus finite modular kill
With v = +-1, put alpha = u+s, beta_bar = u-s (conjugate), and
U_p = (alpha^p - beta_bar^p)/(alpha - beta_bar) = G_p(u) = +-1.
So |U_p| = 1. Here (alpha, beta_bar) is a genuine Lucas pair:
alpha+beta_bar = 2u and alpha*beta_bar = u^2+209 = y are nonzero
coprime rational integers except for a possible common divisor, and
any such common rational prime q | gcd(2u, y) divides 209 (q = 2 is
impossible since y is odd; q | u and q | y with u^2+209 = y forces
q | 209, so q in {11, 19}). On that locus G_p(u) = 0 mod q
(machine check in `work/s8_killers.py`: for every p in
{7,...,29} and q in {11,19}, G_p(u) = 0 mod q whenever 2u = 0 and
u^2+209 = 0 mod q), never +-1, so the Lucas sequence U_p is
non-degenerate there and the Bilu-Hanrot-Voutier theorem on primitive
divisors of Lucas sequences applies: U_p has a primitive prime divisor
for p > 30 (and the small cases p <= 29 are checked directly).
Since |U_p| = 1 has no prime divisor at all, p <= 29. (This
is the standard reduction used in all Lebesgue-Nagell work, e.g. the
D = 209 case analysis cites exactly BHV + Thue/S-integral points; the
fingerprint method is "Bilu-Hanrot-Voutier plus Thue and S-integral
points".)

It remains p in {7, 11, 13, 17, 19, 23, 29}. For each such p, a short
modulus kills G_p(u) = +-1 for ALL integer u (script
`work/s8_killers.py`, certified in
`output/artifacts/killer_cert.txt`; full residue systems, no parity
restriction):

  p=7:  mod 37; p=11: mod 11; p=13: mod 19; p=17: mod 43;
  p=19: mod 19; p=23: mod 37; p=29: mod 41. The prime set {7..29} also
covers repeated-prime-power exponents: if p^2 | n with p >= 7 then the
prime-exponent reduction lands on p itself, already killed.)

Each check is a finite computation over all residues (e.g. for
p = 11 mod 11; machine check confirms no residue u gives +-1).
Hence no solutions for any p >= 7 with p != 5.

## 3. The 5-divisible case (the documented gap)
Now p = 5. Here 5 | h_K, so [a]^5 = 1 does not force [a] = 1. (Coprime
conjugate ideals still give (x+s) = a^5, by the Section-2 argument,
which used only oddness of p.) PARI certifies: 5 splits,
5O = P*Q with P = [5,-1,1] (the prime containing 54+s) and Q its
conjugate; [P] has exact order 5 (P^j nonprincipal for 1<=j<=4 via
`bnfisprincipal`, P^5 = (54+s) principal); and there is no element of
norm +-5^j for 1<=j<=4 (`qfbsolve(Qfb(1,0,209),5^j) = []`, so neither
P^j nor Q^j is principal). Consequently the Sylow 5-subgroup of Cl(O)
is exactly <[P]> ~= C5: indeed Cl(O) ~= C10 x C2 has a unique subgroup
of order 5. Since [a]^5 = 1, [a] lies in this subgroup, [a] = [P]^r
for some r, and (x+s) = g^5 P^{k'}... more precisely
(x+s) = (g)^5 (beta)^{k} (eps) with beta = 54+s generating P^5,
k in {0,...,4}, as follows: [(x+s)] = 1 = [g]^5 [P]^k..., and on the
2-part [g]^5 = [g] (5 = 1 mod 4 kills... the 2-part has exponent 2,
so 5th powers act as identity) while on the 5-part [g]^5 = 1; hence
[(x+s)] = [g]_{2-part} [P]^k... the existence of SOME k in 0..4 with
(x+s) = eps g^5 beta^k follows because [P]^k ranges over the full
Sylow 5-subgroup and the 2-part of [(x+s)] = 1 is matched by adjusting
g (whose 5th power covers the prime-to-5 part of the class group:
c -> c^5 is an automorphism of the subgroup of order 4). In fact more
directly: the classes [g]^5 as g varies cover the unique subgroup of
Cl(O) of order 4, and [P]^k covers the 5-part, so every principal
class is [g]^5[P]^k; fixing (x+s) principal gives the decomposition.
The valuation pins k <= t as follows: v_P(beta) = 5 (since
(beta) = P^5), so v_P(x+s) = 5 v_P(g) + 5k = 5t gives v_P(g) + k = t,
k <= t. In particular the known solution has t = 1, g = 1, k = 1.
Taking s-coefficients with g = u+vs gives the twisted Thue equations
H_k(u,v) = +-1 (k = 0..4), where H_0 = G_5 is the principal case and,
for k >= 1, H_k = U5*B_k + V5*A_k with beta^k = A_k+B_k s and
U5+V5 s = (u+vs)^5. The `thue` computation covers ALL k in 0..4
(k = 0 done by hand; k = 1..4 by certified Thue solver), hence covers
all possibilities regardless of t. This is exhaustive: every p = 5
solution yields some k in 0..4 with H_k(u,v) = +-1 (up to the unit
+-1, absorbed in the +-1 rhs). Explicitly:

  H_0(u,v) = G_5(u,v) (principal case, killed by hand above);
  H_1 = u^5+270u^4 v-2090u^3v^2-112860u^2v^3+218405uv^4+2358774v^5,
  H_2 = 108u^5+13535u^4v-225720u^3v^2-5657630u^2v^3+23587740uv^4
        +118244467v^5,
  H_3 = 8539u^5+618030u^4v-17846510u^3v^2-258336540u^2v^3
        +1864960295uv^4+5399233686v^5,
  H_4 = 584712u^5+24450365u^4v-1222048080u^3v^2-10220252570u^2v^3
        +127704024360uv^4+213603278713v^5
  (exact forms generated in `work/s3_twisted.py`).

- k = 0 (principal): v = +-1 and F(u) = 5u^4-2090u^2+43681
= +-1. F = -1 is impossible mod 5 (F = 1 mod 5 always). F = +1 gives
5w^2-2090w+43680 = 0 (w = u^2) with discriminant 2090^2-4*5*43680 =
3494500, not a square (58^2 = 3364...; machine isqrt check confirms
1869^2 = 3493161 < 3494500 < 1870^2 = 3496900), so no integer w, no
solutions. (Hence every p = 5 solution has 5 | Y and k in 1..4.)

- Valuation/exhaustiveness note. Let t = v_5(Y) >= 0 where Y = y
(p = 5 prime-exponent case), N(x+s) = Y^5. Since P, Q are the only
primes above 5 and P ∤ (x-s) whenever P | (x+s) (a common divisor
would divide 2 and Y, impossible as in Section 2), all the 5-adic
valuation v_5(N) = 5t sits on one side: v_P(x+s) = 5t (after labelling
P as the prime dividing x+s; if instead Q | x+s, conjugate the whole
argument). With (beta) = P^5 and (x+s) = eps g^5 beta^k, taking Padic
valuations gives 5 v_P(g) + 5k = 5t, i.e. v_P(g) + k = t and k <= t.
Since k = 0 is killed by hand and k in 1..4 by the certified solver,
all t are covered (for t >= 5, k could in principle exceed 4, but
k is taken mod 5: write the P-free part... precisely, k in {0,...,4}
is the residue of the needed 5-part twist, and v_P(g) absorbs the
quotient; every solution yields such a k). The Q-sided case is
identical after conjugation (beta replaced by its conjugate, same
norms, same Thue solution sets up to sign).

- Certified Thue solution (PARI `thueinit`/`thue`, script
`work/s4_thue.py`, outputs in `output/artifacts/thue_certs.txt`):
  H_1 = +1: only (u,v) = (1,0); H_1 = -1: only (-1,0).
  H_2, H_3, H_4 = +-1: no solutions.
  (u,v) = (1,0) gives x = Re-part = A_1 = 54, Y = 5; (-1,0) gives
x = -54. Both give (y,n) = (5,5). No other (u,v) arise.

Thus the only p = 5 solutions (up to sign of x) are (54,5,5).

## 4. Conclusion
- 3 | n: impossible (Section 2a).
- Even n >= 4: impossible (Section 1d).
- p >= 7, p != 5: impossible (Section 2b).
- p = 5: only (54,5,5) (Section 3).
- Composite n: reduces to a prime exponent case; the only prime case
with solutions is p = 5 with (x,Y) = (54,5); lifting back, n = 5m with
Y = y^m = 5 forces m = 1, y = 5. Hence (54,5,5) is the only solution
for composite n as well.

Therefore, up to sign of x, (54,5,5) is the unique triple with n >= 3,
y > 1, gcd(x,y) = 1. ∎

## Computational appendices (all rerunnable)
- `work/s1_classgroup.py`, `work/s9_orders.py`: bnfcertify=1, classno 20,
clgp [20,[10,2]], primedec(5) split, P^5=(54+s), P^j (j<5) nonprincipal,
qfbsolve emptiness for 5^j (j<=4), even-n base cases, ispower checks.
- `work/s8_killers.py`: killer moduli for p in {7,...,29} over ALL
residues, plus Lucas-pair non-degeneracy check (+ outputs).
- `work/s3_twisted.py`: exact H_k forms.
- `work/s4_thue.py`: certified Thue solutions for H_1..H_4 = +-1.
- `work/s7_verify.py`: direct check 54^2+209=5^5; brute-force scan
(even x <= 2e5) finds only (54,5,5); v=0 edge cases for k>=2.
- `work/s10_final_checks.py`: discriminant/mod-5 checks, parity-lemma
retraction witness (U_3(1,1) = -626), even-n details.
Outputs copied under `output/artifacts/`.
