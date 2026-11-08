# The sharp dyadic covering time for exponential-linear residues

## Finding

For integers \(k\ge1\), \(a\in\mathbb Z\), and odd \(b\in\mathbb Z\), define \(m=2^k\) and
\[
T_k(a,b)=\min\left\{N\ge1:\{a^n+bn\bmod m:1\le n\le N\}=\mathbb Z/m\mathbb Z\right\}.
\]
The minimum always exists. The exact **worst-case first-coverage time** is
\[
\boxed{\max_{a\in\mathbb Z}T_k(a,b)=2^k+k-1.}
\]
For odd \(a\), one has the stronger \(T_k(a,b)=2^k\): the first \(2^k\) terms form a complete residue system. For even \(a\) the bound above is universal and attained by at least one even \(a\), for every odd \(b\) and every \(k\).

## Assumptions and scope

The exponent \(n\) always starts at \(1\), and \(a\) may be any integer (including \(0\) or negative integers). All exponentials use nonnegative integer exponents; no choice of a rational or \(2\)-adic exponential for negative exponents is needed. The coefficient \(b\) must be odd. The extremizing base \(a\) is allowed to depend on \(k\) and \(b\). No assertion is made for odd moduli or even \(b\).

## Proof

**1. Odd bases are isometries.** Put \(f(n)=a^n+bn\), and take distinct positive integers \(n>t\). Write \(d=n-t\). If \(d\) is odd, \(a^n-a^t\) is even, whereas \(bd\) is odd. Thus \(\nu_2(f(n)-f(t))=0=\nu_2(d)\). If \(d\) is even, write \(d=2^v u\) with \(v\ge1\) and \(u\) odd. Every odd integer \(a\) satisfies \(a^2\equiv1\pmod8\); repeated squaring gives \(a^{2^v}\equiv1\pmod{2^{v+2}}\). Hence \(a^d\equiv1\pmod{2^{v+2}}\) and \(a^t(a^d-1)\) is divisible by \(2^{v+2}\). Since \(\nu_2(bd)=v\),
\[
\nu_2(f(n)-f(t))=v=\nu_2(n-t).
\]
This also holds when \(a=\pm1\), when some differences \(a^d-1\) vanish. In particular, distinct \(n,t\) in an interval of \(2^k\) consecutive integers give distinct outputs modulo \(2^k\). This proves \(T_k(a,b)=2^k\) for odd \(a\).

**2. Universal upper bound for even bases.** If \(a\) is even, \(a^n\equiv0\pmod{2^k}\) for all \(n\ge k\). The \(2^k\) consecutive indices
\[
k,k+1,\ldots,k+2^k-1
\]
therefore produce the \(2^k\) residues \(bn\pmod{2^k}\), all distinct because \(b\) is odd. Consequently \(T_k(a,b)\le2^k+k-1\).

**3. An extremizing even base exists.** Set \(m=2^k\). Among the indices \(k,k+1,\ldots,m+k-2\), the affine values \(bn\pmod m\) run through every residue except \(b(k-1)\pmod m\). It suffices to choose \(a\) even so that
\[
a^n\not\equiv b(k-1-n)\pmod{2^k}\qquad(1\le n\le k-1).\tag{1}
\]
For \(k=1,2,3,5,6\), the choice \(a=2\) works for every odd \(b\). For \(k=4\), take \(a=6\) when \(b\equiv1\pmod8\), and \(a=2\) otherwise. This checks all small cases directly; the finite verification script independently tests them.

For \(k\ge7\), choose an integer \(u\) uniformly among odd residues modulo \(2^{k-1}\), and set \(a=2u\). For \(n=k-1\), the right-hand side of (1) is zero, whereas \(\nu_2(a^{k-1})=k-1\), so equality cannot hold. For \(1\le n\le k-2\), equality in (1) is possible only if
\[
\nu_2(k-1-n)=n,
\]
since \(b\) and \(u\) are odd. The latter forces \(2^n\le k-2\), hence \(n\le L=\lfloor\log_2(k-2)\rfloor\). Whenever this valuation constraint holds, equality would require
\[
u^n\equiv \frac{b(k-1-n)}{2^n}\pmod{2^{k-n}}.\tag{2}
\]
Because \(n\le L\), the exponent \(s=k-n\) is at least \(3\). The unit group modulo \(2^s\) has the structure \(C_2\times C_{2^{s-2}}\); therefore every fiber of the power map \(u\mapsto u^n\) contains at most
\[
\gcd(2,n)\gcd(2^{s-2},n)\le2n
\]
units. As \(u\) is uniform, the probability of any specified congruence (2) is at most \(2n/2^{s-1}=n2^{n+2-k}\). A union bound thus gives
\[
\Pr(\text{at least one equality in (1)})\le
2^{2-k}\sum_{n=1}^L n2^n.
\]
At \(k=7,8\), one has \(L=2\), and this upper bound is respectively \(10/32\) and \(10/64\), both less than one. For \(k\ge9\), using \(2^L\le k-2\) and \(L\le k-2\) gives
\[
2^{2-k}\sum_{n=1}^L n2^n
<2^{3-k}L(k-2)\le 2^{3-k}(k-2)^2<1.
\]
The last inequality holds at \(k=9\), where it reads \(49<64\), and persists for all larger integers by comparing successive terms. Thus a choice of \(u\) avoids all equalities in (1). For that even \(a=2u\), residue \(b(k-1)\) does not occur among the first \(2^k+k-2\) terms, whereas it does occur at the next index. This proves \(T_k(a,b)=2^k+k-1\) and establishes the theorem. \(\square\)

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. The program exhaustively checks every base residue \(a\), every odd coefficient residue \(b\), and every exponent \(1\le k\le8\); it tests the universal bound and identifies a sharp even-base witness for each coefficient. It also exercises the large-exponent construction for selected odd coefficients at \(9\le k\le16\). Finite computation is corroboration, not the argument for unbounded \(k\).

## Relationship to prior work

Zhi-Wei Sun's 2013 paper *On \(a^n+bn\) modulo \(m\)*, Theorem 1.1, proves coverage by the first \(m^2\) terms for every modulus and every coefficient coprime to \(m\). Sun's Conjecture 1.1 proposes a much shorter general bound for the special coefficients \(b=\pm1\). The present result obtains the **optimal uniform bound** \(m+\log_2 m-1\) for every power-of-two modulus, simultaneously for all odd \(b\), and distinguishes odd bases (exact permutations) from even bases (sharp delays). This sharp worst-case result does not follow from the \(m^2\) theorem.

Rivest's 2001 paper classifies permutation *polynomials* modulo powers of two. It provides broader permutation context but does not establish the present exponential-plus-linear first-covering-time formula; the odd-base isometry here is not claimed as an entirely new technique.

## Limitations

This is a complete theorem only for powers of two and odd linear coefficient. It does not solve Sun's conjecture for general moduli. The witness for every large \(k\) is proved to exist by a counting argument, and the proof does not designate one uniform fixed base \(a\) that works for every \(k\). Historical priority for equivalent results in older work on modular exponential maps cannot be ruled out by searches alone. No independent mathematical audit has been performed.

## References

1. Z.-W. Sun, *On \(a^n+bn\) modulo \(m\)*, arXiv:1312.1166v1, first submitted 2013-12-04; Theorem 1.1 and Conjecture 1.1. https://arxiv.org/abs/1312.1166
2. R. L. Rivest, *Permutation Polynomials Modulo \(2^w\)*, *Finite Fields and Their Applications* **7** (2001), 287–292. https://people.csail.mit.edu/rivest/pubs/Riv01c.pdf
