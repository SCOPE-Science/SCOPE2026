# Unique first collision for triangular residues at every modulus

## Finding
Let \(T(n)=n(n-1)/2\) for every positive integer \(n\). For a fixed modulus \(m\ge1\), define \(L(m)\) as the smallest index \(b\ge2\) for which \(T(b)\equiv T(a)\pmod m\) with some \(1\le a<b\). Factor \(m=2^e w\), where \(w\) is odd. Among the positive divisors \(d\mid w\), exactly one, denoted \(d_*\), minimizes \(d+2m/d\). Then

\[
L(m)=\frac{d_*+2m/d_*+1}{2}.
\]

The first repeated residue has **exactly one earlier occurrence**. More precisely, with \(r=\min(d_*,2m/d_*)\) and \(s=\max(d_*,2m/d_*)\), that earlier index is \(a=(s-r+1)/2\), and the indices obey

\[
T(L(m))-T(a)=m.
\]

Thus, for each \(N\ge1\), the first \(N\) triangular values are distinct modulo \(m\) if and only if \(N<L(m)\). Special cases are

\[
L(2^e)=2^e+1\quad(e\ge0),\qquad
L(p^{2r})=\frac{3p^r+1}{2},\qquad
L(p^{2r+1})=\frac{(p+2)p^r+1}{2},
\]

for every odd prime \(p\) and \(r\ge0\).

## Assumptions and scope
The modulus is any positive integer, including \(m=1\). The indices are positive integers beginning at \(1\), so \(T(1)=0\). A collision means equality modulo a **fixed** modulus, not an equality of integers or the least modulus over all moduli for a fixed prefix. The odd part \(w\) is \(m/2^{\nu_2(m)}\), and the divisors in the minimization are positive. The statements are exact for all moduli, not merely for prime powers or computational ranges.

## Proof
**1. Extract a lower bound from any collision.** Suppose \(1\le a<b\) and \(T(a)\equiv T(b)\pmod m\). Put \(u=b-a\) and \(v=a+b-1\). Then \(u,v\) are positive, \(u<v\), and \(u+v=2b-1\) is odd, while

\[
2\bigl(T(b)-T(a)\bigr)=uv.
\]

Therefore \(2m\mid uv\) and precisely one of \(u,v\) is odd. Call the odd factor \(O\) and the even factor \(E\). Set \(d=\gcd(O,w)\). Since \(w\mid OE\), the coprimality of \(O/d\) and \(w/d\) implies \(w/d\mid E\). Because \(O\) is odd and \(2^{e+1}\mid OE\), also \(2^{e+1}\mid E\). These relatively prime factors give \(2m/d\mid E\). Hence

\[
2b-1=O+E\ge d+\frac{2m}{d}\ge \min_{c\mid w}\left(c+\frac{2m}{c}\right).
\]

**2. Attain the lower bound.** Let \(d_\ast\mid w\) minimize the displayed sum and take \(O=d_\ast\), \(E=2m/d_\ast\). The former is odd and the latter is a positive even integer, so they differ. Put \(r=\min(O,E)\), \(s=\max(O,E)\) and

\[
a=\frac{s-r+1}{2},\qquad b=\frac{r+s+1}{2}.
\]

Both are positive integers, \(a<b\), \(b-a=r\), and \(a+b-1=s\). Their triangular-value difference is \(rs/2=OE/2=m\). This constructs a collision attaining the preceding lower bound; thus the formula for \(L(m)\) follows.

**3. Uniqueness.** If distinct positive divisors \(d_1,d_2\mid w\) have equal objective values, then

\[
(d_1-d_2)\left(1-\frac{2m}{d_1d_2}\right)=0,
\]

so \(d_1d_2=2m\), impossible because their product is odd. Hence the minimizing divisor is unique. For any earlier \(a\) colliding with \(b=L(m)\), all inequalities of Step 1 must be equalities. In particular \(O=d_*\), \(E=2m/d_*\), and \(u,v\) are precisely these two numbers in increasing order. This uniquely fixes \(a\), and the integer difference is exactly \(m\). Minimality of \(b\) gives the injective-prefix characterization.

**4. Prime powers.** For \(m=2^e\), the only odd divisor \(d\) is \(1\), yielding \(L=2^e+1\). For \(m=p^k\), with \(p\ge3\) prime, write \(d=p^j\), \(0\le j\le k\). The objective is \(f(j)=p^j+2p^{k-j}\), and

\[
f(j+1)-f(j)=(p-1)\left(p^j-2p^{k-j-1}\right).
\]

Since \(p>2\), the objective decreases while \(j<k/2\) and increases afterward; its unique minimum is at \(j=\lceil k/2\rceil\). Substitution gives the two prime-power formulas, including \(k=0\).

## Verification
The accompanying standard-library script `verify.py` directly enumerates all triangular residues up to the first repeat for every modulus \(1\le m\le9999\). It compares this direct enumeration with the divisor formula, verifies that the earlier colliding index is unique, and checks that the exact unreduced difference is \(m\). It separately verifies the closed formulas on small prime powers. The finite checks are regression tests; Steps 1–4 prove the unrestricted theorem.

## Relationship to prior work
Zhi-Wei Sun, *The least modulus for which consecutive polynomial values are distinct* (first arXiv version 2013-04-22), studies the **opposite order of optimization**: for a prescribed prefix, minimize the modulus with no collisions. In particular it poses a triangular-number simultaneous-modulus discriminator problem. The result here fixes an arbitrary modulus and instead determines the **maximal collision-free prefix** and its unique first colliding pair. The prior discriminator result does not specify this inverse function at composite moduli.

Sajed Haque's 2017 *Discriminators of Integer Sequences* (Section 5.2.2) determines the optimized discriminator of the triangular sequence; it does not state this per-modulus divisor-minimization/unique-first-witness result. Darin J. Ulness, *Structure of Triangular Numbers Modulo m* (2022), studies periodicity and first return to zero alongside the structure of residue sets. Its full text could not be fully examined for the priority comparison, so an unrecognized equivalent formulation there remains a risk. The present proof is self-contained and does not use a global novelty assumption.

## Limitations
This addresses only the triangular sequence and the **first** repetition of a fixed-modulus prefix, not every repeated-residue fiber or the optimal modulus for each fixed prefix. The proof uses the quadratic factorization particular to triangular numbers; it supplies no claim for higher polygonal polynomials. Historical priority is qualified because an equivalent formulation could exist in older number-theoretic or modular-sequence literature, and the relevant 2022 primary article was not completely inspectable.

## References
1. Zhi-Wei Sun, *The least modulus for which consecutive polynomial values are distinct*, arXiv:1304.5988 (initial public preprint 2013-04-22), https://arxiv.org/abs/1304.5988.
2. Sajed Haque, *Discriminators of Integer Sequences*, master's thesis, University of Waterloo (2017), Section 5.2.2, https://uwspace.uwaterloo.ca/items/8af4dae5-4c03-46a3-b49e-25e93da385f7.
3. Darin J. Ulness, *Structure of Triangular Numbers Modulo m*, AppliedMath **2** (2022), 326–358, https://doi.org/10.3390/appliedmath2030020.
