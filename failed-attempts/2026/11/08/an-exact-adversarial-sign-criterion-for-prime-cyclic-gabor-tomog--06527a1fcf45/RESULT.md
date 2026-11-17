# An exact adversarial-sign criterion for prime-cyclic Gabor tomography

## Finding

Let \(p\) be an odd prime and let \(\varnothing\ne S\subsetneq\mathbb F_p\). For each signing \(\varepsilon:S\to\{-1,1\}\), define a window \(g_\varepsilon(x)=\varepsilon(x)\) for \(x\in S\) and \(g_\varepsilon(x)=0\) otherwise. Write
\[
\lambda_S(u)=|S\cap(S-u)|,\qquad u\in\mathbb F_p.
\]
Consider the \(p^2\) Gabor measurement projectors \(P_{t,k}=v_{t,k}v_{t,k}^*\), where \(v_{t,k}(x)=\zeta_p^{kx}g_\varepsilon(x-t)\), \(\zeta_p=e^{2\pi i/p}\). Their complex-linear span is all \(p\times p\) matrices **for every signing** \(\varepsilon\) if and only if
\[
\boxed{\lambda_S(u)\text{ is odd for every }u\in\mathbb F_p^\times.}
\]
Equivalently, every signing yields an injective **matrix-level** Gabor intensity lifting precisely under this parity condition. In the robust case, complete matrix reconstruction also gives phase retrieval for every complex signal up to global phase. If one overlap count is even (including zero), an explicit signing with a vanishing self-ambiguity coefficient can be constructed, proving failure of complete matrix tomography; this does **not** by itself prove failure of signal phase retrieval for that signing.

The same characterization entails a sharp universal support obstruction. If every signing is informationally complete and \(k=|S|\), then
\[
\boxed{k(k-1)\ge p-1.}
\]
Equality occurs exactly when \(S\) is a cyclic planar difference set (every nonzero difference occurs once). For example \(S=\{1,2,4\}\subset\mathbb F_7\) and \(S=\{0,1,3,9\}\subset\mathbb F_{13}\) attain the bound and remain informationally complete under **every** one of their \(2^k\) sign assignments. More generally, every cyclic planar difference set in prime order has this sharp sign-robust property. The quadratic-residue set in every prime \(p\equiv7\pmod8\) is another (nonminimal) family, with all nonzero overlap counts equal to \((p-3)/4\), an odd integer.

## Assumptions and scope

The ambient cyclic group has **odd prime** order. The support is nonempty and proper. The window entries are independently chosen from \(\{-1,+1\}\) on that support and exactly zero elsewhere. "Every signing" means a single support must work under all \(2^{|S|}\) independent assignments. The lifting is the complex-linear map
\[
\mathcal L_{g}(H)_{t,k}=\operatorname{tr}(H P_{t,k}),
\qquad H\in\mathbb C^{p\times p}.
\]
No assumption is made about difference-set regularity, and no claim is made for arbitrary nonbinary complex phases, composite cyclic orders, or uniform conditioning.

## Proof

**Step 1: Weyl diagonalization.** For an arbitrary window \(g\), define the unnormalized self-ambiguity array
\[
A_g(u,v)=\sum_{x\in\mathbb F_p}g(x+u)\overline{g(x)}\zeta_p^{-vx},
\qquad u,v\in\mathbb F_p.
\]
The \(p^2\) Weyl shift-modulation matrices form an orthogonal Hilbert--Schmidt basis. Conjugating a Weyl matrix by the time-frequency shift of \(g\) multiplies its measurement coefficient by a character of \((t,k)\). Fourier orthogonality therefore diagonalizes the lifting, whose singular values, in the unnormalized convention used here, are precisely \(\sqrt p\,|A_g(u,v)|\), with multiplicity. This is the standard Gabor lifting identity in Bojarovska--Flinth [1]. Thus the projector span is complete if and only if every \(A_g(u,v)\) is nonzero.

**Step 2: All nonzero modulation frequencies.** For a signed window, the coefficient row \(c_x=g(x+u)g(x)\) is in \(\{-1,0,1\}\) and has support \(S\cap(S-u)\). The proper-support assumption guarantees at least one zero coefficient for every \(u\). For \(v\ne0\), if \(\sum_xc_x\zeta_p^{-vx}=0\), then the degree-at-most-\(p-1\) polynomial in \(\mathbb Q[X]\) formed by these coefficients is divisible by the irreducible polynomial \(\Phi_p(X)=1+X+\cdots+X^{p-1}\). Hence all \(p\) coefficients are equal. Since one coefficient is zero, they are all zero. Consequently
\[
A_g(u,v)\ne0\ (v\ne0)\quad\Longleftrightarrow\quad\lambda_S(u)>0.
\]
For \(u=0\), \(A_g(0,0)=|S|>0\) and the same cyclotomic argument gives \(A_g(0,v)\ne0\) for \(v\ne0\), because \(g(x)^2=\mathbf1_S(x)\) is nonconstant.

**Step 3: Odd overlaps suffice.** If \(u\ne0\), then
\[
A_g(u,0)=\sum_{x\in S\cap(S-u)}\varepsilon(x+u)\varepsilon(x)
\]
is a sum of exactly \(\lambda_S(u)\) signs. It is an odd integer and hence cannot be zero whenever \(\lambda_S(u)\) is odd. Steps 1 and 2 show that all coefficients are then nonzero for every signing.

**Step 4: Even overlaps permit explicit sabotage.** Fix \(u\ne0\) with even \(\lambda_S(u)\). If it is zero, every signing has \(A_g(u,0)=0\). Otherwise view \(\mathbb F_p\) as the cyclic graph with edges \(\{x,x+u\}\). Since \(u\) generates the prime-order cyclic group, these edges form a single cycle of length \(p\). Because \(S\) omits at least one vertex, the induced graph on \(S\) is a disjoint union of paths; its edges are in bijection with the terms of \(A_g(u,0)\). Give exactly half of these edges desired product \(-1\) and half \(+1\). Choose a starting vertex sign on each path and propagate signs to realize every prescribed edge product. Then \(A_g(u,0)=0\), so this signing does not give a complete projector span. This proves the converse.

**Step 5: Optimal-support obstruction and examples.** If all nonzero overlaps are odd, then they are at least one. Counting ordered distinct pairs in \(S\) by their difference gives
\[
k(k-1)=\sum_{u\ne0}\lambda_S(u)\ge p-1.
\]
Equality holds precisely when all \(\lambda_S(u)=1\), the definition of a cyclic planar difference set. Direct subtraction verifies that each of \(\{1,2,4\}\pmod{7}\) and \(\{0,1,3,9\}\pmod{13}\) has every nonzero difference exactly once, giving the claimed sharp families. Classical Singer planar difference sets provide further examples whenever \(p=q^2+q+1\) is prime with \(q\) a prime power [3]. For \(p\equiv3\pmod4\), the nonzero quadratic residues form a Paley difference set with \(\lambda_S(u)=(p-3)/4\) [1, Section 2.3.2]; this is odd exactly when \(p\equiv7\pmod8\). The claims follow.

## Verification

The standalone Python 3 program `verify.py` checks the parity characterization **exhaustively** for every nonempty proper support and every signing on prime groups of orders \(3,5,7\), using exact integer coefficients and the cyclotomic minimal-polynomial test. It further constructs explicit destructive signings along induced path components for every non-robust support, tests \(300\) randomly sampled supports at prime order \(11\) with either destructive signings or independently sampled successful signings, and checks the planar examples at orders \(7,13\) and Paley examples at \(23,31\). Running `python3 verify.py` prints `ROBUST_SIGNING_GABOR_PASS`. The finite tests corroborate but do not replace the proof for all odd primes and supports.

## Relationship to prior work

Bojarovska and Flinth [1, Theorems 2.2--2.3] establish the full nonvanishing-ambiguity criterion and Gabor lifting singular values; [1, Proposition 2.2] shows that *unsigned characteristic functions* of suitable cyclic difference sets work. A published arithmetic classification [2] establishes the much more general proper-support result for **positive rational** windows: the lifting rank is \(p|S-S|\). That classification explicitly depends on positivity at zero modulation and does not imply robustness to signs. The present theorem instead quantifies over **every adversarial sign assignment**, gives an if-and-only-if criterion in terms of parity of every overlap, and constructs failure signings using induced path forests. Singer's planar difference sets [3] and Paley difference sets are classical; their existence is not asserted as new. The derived optimal-support robustness and full-support-independent parity criterion are the claims assessed here.

## Limitations

This is an exact all-signings statement, not a stability theorem: the smallest positive singular value may depend sharply on the support and signs. A particular signing can still have complete matrix lifting when one overlap count is even; the theorem says that **not all** signings do. Failure of the full matrix lifting is not in general equivalent to failure of phase retrieval of individual pure signals. In general, arbitrary complex phases can cancel an odd number of terms, so the result does not extend without change from binary signs to arbitrary phases. The examples based on Singer constructions require their cyclic order to be prime; no infinitude of primes of the form \(q^2+q+1\) is asserted. Historical priority relative to a broader unpublished or differently formulated adversarial-sign theorem cannot be excluded by bounded literature searches.

## References

[1] I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first public version 2015-03-19. https://arxiv.org/abs/1503.05800

[2] *Arithmetic rigidity of prime-cyclic Gabor tomography for positive rational windows*, published research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-arithmetic-rigidity-of-prime-cyclic-gabor-tomography-for-positiv--65df80cb23d5

[3] J. Singer, *A theorem in finite projective geometry and some applications to number theory*, Transactions of the American Mathematical Society **43** (1938), 377--385, https://doi.org/10.1090/S0002-9947-1938-1501951-4 . The Singer difference-set construction is a classical input, not a new claim.
