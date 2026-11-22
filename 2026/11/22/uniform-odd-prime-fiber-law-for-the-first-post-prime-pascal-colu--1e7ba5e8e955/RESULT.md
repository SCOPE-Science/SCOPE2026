# Uniform odd-prime fiber law for the first post-prime Pascal column

## Finding

Let \(p\ge3\) be a prime and \(h\ge1\) be an integer. Set \(B_p(n)=\binom{n}{p+1}\) for \(n\ge0\), and define the rational \(p\)-adic integer
\[
\alpha_p=\binom{p/2}{p+1}=\frac{(p/2)(p/2-1)\cdots(p/2-p)}{(p+1)!}\in p\mathbb Z_p.
\]
Write \(a_{p,h}\) for the reduction of \(\alpha_p\) modulo \(p^h\). For any modulus \(M\), let \(R_M(z)=\#\{x\bmod M:x^2\equiv z\pmod M\}\), with \(R_1(0)=1\). Then the **exact fiber count in one least period** is
\[
\boxed{\#\{0\le n<p^{h+1}:B_p(n)\equiv y\pmod{p^h}\}=p-1+\begin{cases}
 pR_{p^{h-1}}((y-a_{p,h})/p),&y\equiv a_{p,h}\pmod p,\\
 0,&y\not\equiv a_{p,h}\pmod p.
\end{cases}}
\]
In the first case, the quotient is interpreted modulo \(p^{h-1}\) after subtracting residue representatives, and the period \(p^{h+1}\) is least. Thus all output residues occur, at least \(p-1\) times. Outside the single class \(y\equiv0\pmod p\), every output occurs **exactly** \(p-1\) times, whereas inside that class the extra fibers are governed by square roots modulo \(p^{h-1}\).

More strongly, for each \(r\in\{1,\ldots,p-1\}\), the map \(t\mapsto B_p(r+pt)\) is a \(p\)-adic isometry of \(\mathbb Z_p\) onto itself. For the remaining index progression there exists a bijective \(p\)-adic isometry \(H_p:\mathbb Z_p\to\mathbb Z_p\) for which
\[
B_p(pt)=\alpha_p+pH_p(t)^2.
\]
Consequently the pushforward distribution is a superposition of \(p-1\) uniform fibers and one quadratic critical fiber, valid simultaneously for **every odd prime**.

## Assumptions and scope

The lower index is exactly the prime plus one. A source code's choice of integral representatives in the formula does not alter its residue modulo \(p^{h-1}\). Generalized binomial coefficients at rational arguments are defined by the falling-factorial polynomial. The counts use one entire period of integer indices, including \(n<p+1\), for which the usual binomial coefficient is zero. The result claims exact frequencies, *not* new universality or a new period formula; both are previously established. The exceptional output class is \(0\pmod p\) because \(\nu_p(\alpha_p)=1\).

## Proof

**1. Integral and isometric regular branches.** Put \(F(X)=\binom{X}{p+1}\), regarded as a rational polynomial. As \(\nu_p((p+1)!)=1\), each \(F(r+pt)\) has coefficients in \(\mathbb Z_p\) for \(r=0,\ldots,p-1\). For \(1\le r<p\), only the factor indexed by \(i=r\) among \(r+pt-i\), \(0\le i\le p\), is divisible by \(p\). After cancellation one obtains
\[
F(r+pt)=tU_r(t),\qquad U_r(t)\in\mathbb Z_p[t],\qquad U_r(t)\equiv r\pmod p.
\]
The last congruence also follows by Lucas's theorem, \(\binom{pt+r}{p+1}\equiv rt\pmod p\). Consequently \(F(r+pt)=rt+pQ_r(t)\), where \(Q_r\in\mathbb Z_p[t]\). For any \(s,t\in\mathbb Z_p\), the difference \(Q_r(t)-Q_r(s)\) is divisible by \(t-s\), so
\[
\nu_p(F(r+pt)-F(r+ps))=\nu_p(t-s).
\]
Such a map induces bijections at every modulus \(p^h\), and therefore is an isometric bijection of \(\mathbb Z_p\).

**2. Singular branch and quadratic normal form.** For \(r=0\), the first and last factors of the falling factorial are both divisible by \(p\). Explicitly,
\[
G(t):=\frac{F(pt)}p=t(t-1)\frac{\prod_{i=1}^{p-1}(pt-i)}{(p+1)(p-1)!}\in\mathbb Z_p[t],\quad G(t)\equiv t(t-1)\pmod p.
\]
Because \(p+1\) is even, replacing the argument \(X\) by \(p-X\) permutes the factors of \(F\) with an even number of sign changes. Therefore \(G(t)=G(1-t)\). Put \(s=t-1/2\). Since two is a unit in \(\mathbb Z_p\), there is a polynomial \(W\in\mathbb Z_p[Z]\) such that
\[
G(1/2+s)=G(1/2)+s^2W(s^2),\qquad W(Z)\equiv1\pmod p.
\]
Write \(W(Z)=1+pV(Z)\). The convergent binomial series \(E(s)=\sqrt{1+pV(s^2)}\), taking the square root congruent to one modulo \(p\), is a uniform limit of polynomials over \(\mathbb Z_p\). It has the form \(1+pT(s)\) for a \(1\)-Lipschitz function \(T:\mathbb Z_p\to\mathbb Z_p\). Hence \(\Psi(s)=sE(s)=s+p(sT(s))\) satisfies \(\nu_p(\Psi(s)-\Psi(u))=\nu_p(s-u)\). Each residue-class solution lifts uniquely, so \(\Psi\) is onto and isometric. Taking \(H_p(t)=\Psi(t-1/2)\), the preceding identities give the exact normal form
\[
F(pt)=pG(1/2)+pH_p(t)^2=\alpha_p+pH_p(t)^2.
\]
There are exactly two factors in \(F(p/2)\) divisible by \(p\), namely those with indices zero and \(p\), while its denominator contains precisely one factor of \(p\); thus \(\nu_p(\alpha_p)=1\).

**3. Fibers.** In a full block of \(p^{h+1}\) integers, each input residue \(r\pmod p\) has the form \(r+pt\) with \(t\) running once through \(\mathbb Z/p^h\mathbb Z\). The \(p-1\) regular isometries each contribute exactly one preimage to every output modulo \(p^h\). The singular image is contained in \(\alpha_p+p\mathbb Z_p\). On that class, reduction of the normal form leaves the quadratic congruence \(z^2\equiv(y-\alpha_p)/p\pmod{p^{h-1}}\). Each solution modulo \(p^{h-1}\) has exactly \(p\) lifts modulo \(p^h\). Adding contributions proves the stated formula, including \(h=1\).

**4. Least period.** The coefficient polynomial has only one factor of \(p\) in its denominator, so shifting its integer argument by \(p^{h+1}\) leaves it unchanged modulo \(p^h\). Conversely, \(B_p(1)=0\) and \(B_p(1+p^h)\) has valuation exactly \(h-1\): exactly one factor in its falling factorial has valuation \(h\), with all others prime to \(p\), whereas the factorial denominator has valuation one. Hence \(p^h\) is not a period. Every smaller positive period would divide \(p^{h+1}\), so the least period is \(p^{h+1}\).

## Verification

The included `CHECK.py` uses exact arbitrary-precision integer binomials, rational arithmetic for \(\alpha_p\), and exhaustive quadratic-root counting. It checks all output fibers across one complete period for every pair \(p\in\{3,5,7,11\}\), \(h\in\{1,2,3\}\), as well as the sharp period witness. The computation confirms twelve complete parameter cases, including \(p=11\), \(h=3\), where the period has \(14{,}641\) indices and \(1{,}331\) target residues. This finite check corroborates the unrestricted algebraic argument; it is not an infinite proof.

## Relationship to prior work

Fiorot, Gilblas, and Tonolo (first public preprint 2023-07-05, arXiv:2307.02366) study modular binomial sequences and establish their least periods in Proposition 3.4, with applications to iterated anti-differences. Thus the period assertion here is **known** and used only to normalize the new multiplicity law. Sun and Zhang (arXiv:0812.3089, first public 2008-12-16) prove \(p\)-adic universality for \(\binom{n}{p+1}\), a special case of their Corollary 1.3 and Theorem 1.1. That prior result also provides regular-branch lifting; neither their stated theorems nor the inspected proofs give the single singular-branch quadratic normal form or its all-target fiber formula. The published prime-power fifth-column fiber law for \(\binom n5\) concerns the prime two and a fixed different lower index, not the odd-prime family \(p+1\). The contribution claimed is the uniform **exact fiber distribution for all odd primes and all precisions**, not surjectivity, branch existence, or period alone.

## Limitations

The theorem concerns odd primes and the lower index exactly \(p+1\); the prime two is not included because square-root normalization differs. It provides no general algorithm for arbitrary Pascal columns. The novelty comparison cannot eliminate an unindexed equivalent or an implicit derivation from a stronger published parametrization. Only self-review is reported; independent audit has not been performed.

## References

- L. Fiorot, R. Gilblas and A. Tonolo, *Modular binomials with an application to periodic sequences*, arXiv:2307.02366 (first public 2023-07-05), Proposition 3.4, https://arxiv.org/abs/2307.02366. The revised journal title is *Periodic sequences, binomials modulo a prime power, and a math/music application*.
- Z.-W. Sun and W. Zhang, *Binomial coefficients and the ring of p-adic integers*, arXiv:0812.3089 (first public 2008-12-16); *Proc. Amer. Math. Soc.* **139** (2011), 1569–1577, especially Theorem 1.1 and Corollary 1.3, https://arxiv.org/abs/0812.3089.
- *Exact three-level 2-adic fibers of the fifth binomial column*, published open mathematics record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-three-level-2-adic-fibers-of-the-fifth-binomial-column--68ab08bc975b.
