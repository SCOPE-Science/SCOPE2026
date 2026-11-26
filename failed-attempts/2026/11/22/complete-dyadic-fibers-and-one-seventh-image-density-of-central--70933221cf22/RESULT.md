# Complete dyadic fibers and one-seventh image density of central Delannoy numbers

## Finding

For every nonnegative integer \(n\), define the central Delannoy number
\[
D_n=\sum_{j=0}^{n}2^j\binom{n}{j}^{2}.
\]
For every integer \(k\ge4\), let \(T_k=2^{k-2}\), and for each residue \(y\bmod2^k\) define its frequency in one least index period as
\[
N_k(y)=\#\{n:0\le n<T_k,\ D_n\equiv y\pmod{2^k}\}.
\]
Then the following *exhaustive disjoint classification* holds.

1. If \(y\equiv3\) or \(13\pmod{16}\), then \(N_k(y)=1\).
2. For every integer \(r\ge2\) such that \(3r<k\), and every target for which \(\nu_2(y-1)=3r\) or \(\nu_2(y+1)=3r\) modulo \(2^k\), one has \(N_k(y)=2^{2r-2}\). Each of the two valuation conditions occurs for exactly \(2^{k-3r-1}\) target classes.
3. For each of the two targets \(y\equiv\pm1\pmod{2^k}\), one has \(N_k(y)=2^{k-2-\lceil k/3\rceil}\).
4. All other targets have \(N_k(y)=0\).

Consequently, the exact number of distinct attained residues is
\[
I_k=2^{k-3}+\sum_{r=2}^{\lfloor(k-1)/3\rfloor}2^{k-3r}+2.
\]
In the ring of two-adic integers, the closure of the Delannoy values is precisely
\[
\begin{aligned}
\mathcal I={}&(3+16\mathbb Z_2)\cup(13+16\mathbb Z_2)\cup\{-1,1\}\\
&\cup\bigcup_{r\ge2}\{z\in\mathbb Z_2:\nu_2(z-1)=3r\}\\
&\cup\bigcup_{r\ge2}\{z\in\mathbb Z_2:\nu_2(z+1)=3r\}.
\end{aligned}
\]
Its normalized additive Haar measure is exactly
\[
\mu(\mathcal I)=\frac18+\sum_{r=2}^\infty2^{-3r}=\boxed{\frac17}.
\]
The theorem includes the previously conjectured complementary valuation law
\[
\nu_2(D_n+1)=3\nu_2(n+1)\qquad(n\equiv3\pmod4).
\]

## Assumptions and scope

The valuation \(\nu_2\) is normalized by \(\nu_2(2)=1\), and \(\nu_2(0)=\infty\). For a residue \(y\bmod2^k\), the expression \(\nu_2(y\pm1)=a<k\) means that any integer representative has valuation exactly \(a\); if \(y\equiv\mp1\), the valuation is at least \(k\) and the center clause applies instead. The index is nonnegative, and all fiber sizes refer to exactly one least full period. The formula holds for every \(k\ge4\), not just asymptotically. Infinite sums converge in \(\mathbb Q_2\), with no claim of real convergence.

## Proof

**1. Two-adic interpolation and a reflection identity.** Define for \(x\in\mathbb Z_2\)
\[
f(x)=\sum_{j\ge0}2^j\binom{x}{j}^{2}.
\]
Every binomial coefficient is a two-adic integer, so this series converges uniformly and defines a continuous function. At nonnegative integer indices it truncates to \(f(n)=D_n\). Euler's hypergeometric transformation, here equivalently the rational generating-function identity
\[
\sum_{j\ge0}\binom{n+j}{j}^{2}z^j
=(1-z)^{-2n-1}\sum_{j=0}^n\binom{n}{j}^{2}z^j
\]
for each nonnegative integer \(n\), is valid as an identity in \(\mathbb Q[[z]]\). Both sides converge at \(z=2\) in \(\mathbb Q_2\), where \((1-2)^{-2n-1}=-1\), and \(\binom{-n-1}{j}=(-1)^j\binom{n+j}{j}\). Thus \(f(-n-1)=-f(n)\). Density of the nonnegative integers in \(\mathbb Z_2\) and continuity extend this to
\[
\boxed{f(-x-1)=-f(x)\quad(x\in\mathbb Z_2).} \tag{1}
\]

**2. The regular index balls.** A known sharp dyadic first-shift identity, also obtainable by Vandermonde expansion of the defining sum, states for \(4\mid h\), \(a=\nu_2(h)\ge2\), and every nonnegative \(n\),
\[
D_{n+h}-D_n\equiv2^{a+2}\left(n+\binom n2\right)\pmod{2^{a+3}}.\tag{2}
\]
For completeness: expand both binomial factors of \(D_{n+h}\) by Vandermonde. A term with exactly one positive shift index contributes modulo \(2^{a+3}\) only when its binomial-index pair is \((1,1)\) or \((2,2)\), giving \(4hn+8\binom h2\binom n2\); all terms with two positive shift indices vanish by their valuation bounds, except for \(a=2\), where the \((j,i,\ell)=(2,2,2)\) and \((4,4,4)\) exceptions both equal \(16\pmod{32}\) and cancel. Substituting \(h=2^a\) times an odd integer gives (2). The same elementary argument is fully detailed in the earlier dyadic-shift study cited below; it is not claimed as a new lemma.

When \(n,m\equiv1\pmod4\), or \(n,m\equiv2\pmod4\), the factor \(n+\binom n2=n(n+1)/2\) is odd; applying (2) to the positive difference between the indices gives
\[
\nu_2(D_n-D_m)=\nu_2(n-m)+2.\tag{3}
\]
As \(D_1\equiv3\) and \(D_2\equiv13\pmod{16}\), (3) yields two surjective two-adic isometries from the respective index balls onto \(3+16\mathbb Z_2\) and \(13+16\mathbb Z_2\). Surjectivity follows because an isometry on \(\mathbb Z_2\) induces an injection, hence a permutation, on each finite ring \(\mathbb Z/2^j\mathbb Z\). Thus each of those target classes has exactly one preimage in the least period.

**3. A critical cubic normal form with controlled unit.** The identity \(\sum_{j\ge1}2^j/j^2=0\) holds in \(\mathbb Q_2\): the formal dilogarithm identity
\[
\operatorname{Li}_2(z)+\operatorname{Li}_2\!\left(\frac{z}{z-1}\right)=-\tfrac12\log^2(1-z)
\]
can be evaluated at \(z=2\), since both dilogarithmic series converge two-adically and \(\log(-1)=0\). Set
\[
P_j(x)=\prod_{i=1}^{j-1}\left(1-\frac xi\right)^2
=\sum_{m=0}^{2j-2}p_{j,m}x^m.
\]
For nonnegative integers, \(\binom{x}{j}^2=(x^2/j^2)P_j(x)\), with terms beyond \(j=x\) zero. Continuity extends the identity to \(4\mathbb Z_2\). Subtracting the preceding zero sum and dividing by the cubic factor produces
\[
f(x)-1=x^3U(x),\qquad
U(x)=\sum_{j\ge1}\frac{2^j}{j^2}\sum_{m=1}^{2j-2}p_{j,m}x^{m-1} \quad(x\in4\mathbb Z_2).\tag{4}
\]
The convergent series in (4) satisfies the *stronger coefficient statement*
\[
\boxed{U(4u)=c_0+\sum_{\ell\ge1}c_\ell u^\ell,\quad c_0\in\mathbb Z_2^\times,\ c_\ell\in2\mathbb Z_2\quad(\ell\ge1),}\tag{5}
\]
with coefficients tending two-adically to zero. The details are included to make the nonstandard analytic step auditable.

For the constant term, \(p_{j,1}=-2\sum_{i=1}^{j-1}1/i\), so its \(j\)-summand has valuation at least
\[
j+1-2\nu_2(j)-\lfloor\log_2(j-1)\rfloor.
\]
All these summands are even except \(j=4\), whose exact contribution is \(-11/3\), a two-adic unit; the finite cases \(2\le j\le15\) and the bound for \(j\ge16\) prove this assertion.

For \(m\ge2\), sort the multiset \(\{\nu_2(i),\nu_2(i):1\le i<j\}\) decreasingly as \(v_1\ge\cdots\). The coefficient of \(u^{m-1}\) from index \(j\) in (4) has valuation bounded below by
\[
E(j,m)=j-2\nu_2(j)+2(m-1)-\sum_{h=1}^{m}v_h.
\]
The uniform lower bound
\[
B(j)=j-2\nu_2(j)-2-2\sum_{h\ge3}\left\lfloor\frac{j-1}{2^h}\right\rfloor
\le E(j,m)
\]
is at least four for \(9\le j\le31\) and greater than one for \(j\ge32\). For \(2\le j\le8\), the minimum of \(E(j,m)\) over \(m\ge2\) is, in order, \(2,3,0,3,2,5,0\). The only potentially odd coefficients are the two terms \((j,m)=(4,2),(8,2)\), both multiplying \(u\); their sum is
\[
\frac{193}{9}+\frac{2105161}{11025}\in2\mathbb Z_2,
\]
so it too is even. Since \(B(j)\) grows linearly, the displayed bounds establish uniform convergence and (5) without illegitimate interchange of series. The finite bounds and exceptional coefficients are independently checked in the accompanying exact-arithmetic program.

It follows from (5) that \(U(x)\) is odd for every \(x\in4\mathbb Z_2\), and
\[
\nu_2(U(x)-U(y))\ge\nu_2(x-y)-1\quad(x,y\in4\mathbb Z_2).\tag{6}
\]
Let \(r\ge2\), \(x=2^ru\), \(y=2^rv\) with both \(u,v\) odd and \(x\ne y\). The factor \(x^2+xy+y^2\) has valuation exactly \(2r\), while (6) shows
\[
\nu_2\bigl(x^3(U(x)-U(y))\bigr)\ge3r+\nu_2(x-y)-1
> 2r+\nu_2(x-y).
\]
Consequently, from (4),
\[
\boxed{\nu_2(f(x)-f(y))=2r+\nu_2(x-y),\qquad\nu_2(f(x)-1)=3r.}\tag{7}
\]
For each fixed \(r\), the normalized map \(u\mapsto (f(2^ru)-1)/2^{3r}\) is therefore an isometry of the odd units onto the odd units. Indeed it permutes every finite odd residue quotient, so its image is the entire odd unit ball by compactness. Hence the exact image on the valuation-\(r\) index shell is precisely \(\nu_2(z-1)=3r\), with a uniquely determined normalized odd index at every level.

**4. The reflected singular branch.** Equation (1) maps \(x\equiv3\pmod4\) onto the branch \(-x-1\in4\mathbb Z_2\), replacing \(f(x)\) by \(-f(-x-1)\). Therefore (7) gives \(\nu_2(f(x)+1)=3\nu_2(x+1)\) and identical isometric fibers near the output center \(-1\). This proves the complementary valuation law, including the 2021 conjecture, with no assumption that it was previously settled.

**5. Counting and limiting measure.** The least period is \(T_k=2^{k-2}\) for \(k\ge4\), as proved in the earlier dyadic-period study and also forced by (2) and its sharp witness at index \(1\). Each regular input index ball has \(2^{k-4}\) indices and fills exactly its \(2^{k-4}\) target classes once. On one critical shell \(\nu_2(n)=r\), with \(3r<k\), the index count is \(2^{k-r-3}\), while the output shell has \(2^{k-3r-1}\) targets; (7) makes each fiber exactly their ratio \(2^{2r-2}\). Indices with \(\nu_2(n)\ge\lceil k/3\rceil\) give the center \(1\), and exactly \(2^{k-2-\lceil k/3\rceil}\) indices lie there. The reflection gives the same count at \(-1\). The four types of target sets are disjoint modulo sixteen. Their union exhausts all indices, proving the formula for \(N_k\) and \(I_k\). Taking the decreasing intersection of finite images gives the asserted compact two-adic image. A shell of exact valuation \(3r\) has Haar measure \(2^{-(3r+1)}\); accounting for the two centers gives \(2^{-3r}\). The regular balls have total measure \(1/8\), and the centers have measure zero, proving \(\mu(\mathcal I)=1/7\). \(\square\)

## Verification

Run `python3 delannoy_new_verifier.py` from the directory containing this document and the standalone checker. It uses only the standard library and checks the rational coefficients and valuation bounds needed for (5), full residue-frequency histograms for \(4\le k\le15\), every target congruent to three or thirteen modulo sixteen, sample exact phase shifts, and 2-adic critical-shell isometries. The completed run printed `coefficient bounds: OK`, `finite fiber indices: 16380`, `shift and shell tests: 1525`, and `PASS`. Computation checks finitely many cases and is not offered as a proof for unrestricted indices or moduli.

## Relationship to prior work

Lengyel (2021), sections 2–3, formulates the exact valuation law for the \(-1\) output branch as Conjecture 2 and studies individual Delannoy valuations, not an all-target dyadic fiber distribution. The two accessible published dyadic studies in the references already establish the exact least periods, the regular-index shift phase (2), and the valuation \(\nu_2(D_n-1)=3\nu_2(n)\) when four divides \(n\); these facts are treated as prior, not new. The latter study's proof contains related coefficient bounds used here. The present additional claim is the two-adic reflection, their promotion to an exact shell-by-shell isometry, and the *complete* all-target fiber law and image measure. The known valuation and period statements alone do not specify the numbers of solutions to \(D_n\equiv y\pmod{2^k}\) for arbitrary \(y\); the new proof supplies the needed full-unit surjectivity. Mikić (2023) proves ternary valuations of Delannoy numbers and divisibility by odd parameters, not the asserted binary image. Search completeness is not presumed.

## Limitations

No results are asserted for odd primes, noncentral Delannoy polynomials, or full two-variable Delannoy numbers. The one-seventh density concerns Haar measure of the closure of attained values, not a density of integer indices. The period and regular-shift results and one critical valuation theorem are previously published. Independent historical-priority verification may find equivalent formulations not indexed in the searched literature; portions of this derivation extend coefficient bounds present in prior work, so they are not claimed as entirely new methods.

## References

1. T. Lengyel, *On Some p-adic Properties and Supercongruences of Delannoy and Schröder Numbers*, INTEGERS **21** (2021), #A86, publicly released 2021-08-27, in particular Conjecture 2. https://math.colgate.edu/~integers/v86/v86.pdf
2. J. Mikić, *On new divisibility properties of generalized central trinomial coefficients and Legendre polynomials*, arXiv:2311.14623v1 (2023-11-24), sections 1 and Theorem 5. https://arxiv.org/pdf/2311.14623
3. *Sharp dyadic index shifts and least periods of central Delannoy numbers*, public mathematical note (2026), exact shift phase and periods. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-sharp-dyadic-index-shifts-and-least-periods-of-central-delannoy--3f433f15bf17/RESULT.md
4. *Resolution of the sharp binary valuation conjecture for central Delannoy numbers*, public mathematical note (2026), dyadic valuation and coefficient bounds. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-resolution-of-the-sharp-binary-valuation-conjecture-for-central--2170cbfaeec0/RESULT.md
