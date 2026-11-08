# Exact Fourier-algebra norm of the complete square set on odd prime-power cyclic groups

## Finding
For an odd prime \(p\) and integer \(k\geq 1\), let \(G_k=\mathbb Z/p^k\mathbb Z\) and let \(Q_k=\{u^2:u\in G_k\}\), including zero and all nonunit squares. Let \(P_k\) be the Fourier projection on \(\ell^2(G_k)\) with multiplier \(\mathbf1_{Q_k}\). Its sharp endpoint norms are equal:
\[
\Lambda_{p,k}=\|P_k\|_{\ell^\infty\to\ell^\infty}=\|P_k\|_{\ell^1\to\ell^1}=\|\mathbf1_{Q_k}\|_{A(G_k)}.
\]
They have the following explicit **all-depth finite formula**. Put
\[
E_k=\{m\in\{1,\ldots,k\}:m\equiv k\pmod2\},\qquad
T_p=\begin{cases}\sqrt p,&p\equiv1\pmod4,\\i\sqrt p,&p\equiv3\pmod4,\end{cases}
\]
and, for \(0\le v<k\),
\[
B_{k,v}=1+\frac{p-1}{2}\sum_{\substack{m\in E_k\\m\le v}}p^{m-1},\qquad
J_{k,v}^{\pm}=\begin{cases}
B_{k,v}+\frac{p^v}{2}(-1\pm T_p),&v+1\in E_k,\\
B_{k,v},&v+1\notin E_k.
\end{cases}
\]
Define \(H_{p,k}=1+\frac{p-1}{2}\sum_{m\in E_k}p^{m-1}\). Then
\[
\boxed{\displaystyle
\Lambda_{p,k}=\frac{H_{p,k}}{p^k}+\frac{p-1}{2}\sum_{v=0}^{k-1}p^{-v-1}\bigl(|J_{k,v}^{+}|+|J_{k,v}^{-}|\bigr).
}\tag{1}
\]
This formula uses at most \(k\) elementary real square roots and determines the exact sharp projection norm for all odd primes and all depths.

More strikingly, for every **fixed** odd prime \(p\), as the depth increases,
\[
\boxed{\displaystyle\Lambda_{p,k}=\sigma_p k+O_p(1),\qquad
\sigma_p=\frac{p-1}{4(p+1)}+\frac{p-1}{4p}
\begin{cases}
\sqrt p,&p\equiv1\pmod4,\\
\sqrt{p+\frac{p^2}{(p+1)^2}},&p\equiv3\pmod4.
\end{cases}}
\tag{2}
\]
In particular, the algebra norm grows linearly with the prime-power depth, despite the fact that the corresponding projection onto **unit** quadratic residues has a norm independent of depth. The two different slopes arise from real versus imaginary quadratic Gauss sums.

## Assumptions and scope
All groups are additive and all squares are **distinct residue classes**, not a multiset counted with square-root multiplicity. The set includes \(0\) and nonunits of even \(p\)-adic valuation. Fourier characters are \(\psi_t(x)=\exp(2\pi i tx/p^k)\); the projection is \(P_k f(y)=p^{-k}\sum_{t\in G_k}K_k(t)f(y-t)\), where \(K_k(t)=\sum_{a\in Q_k}\psi_t(a)\). Absolute norms use the standard unnormalized \(\ell^1\) and \(\ell^\infty\) spaces. The algebra norm is \(\|\mathbf1_{Q_k}\|_{A(G_k)}=p^{-k}\sum_t|K_k(t)|\). The parameter \(k\) is arbitrary but finite; the stated asymptotic holds with \(p\) fixed. No assertion is made for \(p=2\), for arbitrary composite moduli, or for intermediate \(\ell^r\) projection norms.

## Proof
**1. The complete valuation decomposition.** Every nonzero square modulo \(p^k\) has even valuation \(2j<k\), and its unit part is a square modulo \(p^{k-2j}\). For odd \(p\), a unit is a square modulo every \(p^m\) precisely when its reduction is a quadratic residue modulo \(p\): this follows inductively by lifting a root, since the derivative \(2u\) is invertible modulo \(p\). Thus the nonzero squares split **disjointly** into the subsets \(p^{2j}U_m\), with \(m=k-2j\in E_k\), where \(U_m\) is the group of unit quadratic residues modulo \(p^m\). Consequently
\[
K_k(t)=1+\sum_{m\in E_k}R_m(t),\qquad
R_m(t)=\sum_{a\in U_m}\exp(2\pi i at/p^m),
\]
and \(|Q_k|=H_{p,k}\), because \(|U_m|=(p-1)p^{m-1}/2\).

**2. Exact Fourier values on the valuation strata.** Write \(\chi\) for the Legendre character modulo \(p\), extended by zero at zero. On units modulo \(p^m\) the indicator of \(U_m\) equals \((1+\chi(a))/2\). Hence
\[
R_m(t)=\frac12\sum_{a\in(\mathbb Z/p^m\mathbb Z)^\times}
(1+\chi(a))e^{2\pi iat/p^m}.
\]
For \(t\not\equiv0\pmod{p^m}\), write \(v=v_p(t)<m\). Sum first over the \(p^{m-1}\) lifts of the residue \(a\pmod p\). Lift orthogonality makes \(R_m(t)=0\) if \(v<m-1\). If \(v=m-1\), put \(w=t/p^v\pmod p\), obtaining
\[
R_m(t)=\frac{p^{m-1}}2\left(-1+\chi(w)T_p\right).
\]
Here \(\sum_{a=1}^{p-1}e^{2\pi iwa/p}=-1\) and the classical quadratic Gauss sum is \(\sum_{a=1}^{p-1}\chi(a)e^{2\pi iwa/p}=\chi(w)T_p\), with \(T_p=\sqrt p\) or \(i\sqrt p\) according to \(p\pmod4\). If \(v\ge m\), then \(R_m(t)=|U_m|\). These three cases prove \(K_k(0)=H_{p,k}\) and, for a nonzero \(t\) of valuation \(v\),
\[
K_k(t)=J_{k,v}^{\chi(t/p^v)}.
\]
Exactly \((p-1)p^{k-v-1}/2\) residues of valuation \(v\) have each Legendre sign, since each unit residue modulo \(p\) has \(p^{k-v-1}\) lifts. Summing their absolute values gives (1).

**3. Why the projection constant is sharp.** Fourier inversion yields convolution by \(p^{-k}K_k\). The triangle inequality bounds each endpoint operator norm by \(p^{-k}\sum_t|K_k(t)|\). Equality for \(\ell^\infty\) follows by choosing the input at index \(-t\) to have the conjugate phase of \(K_k(t)\); equality for \(\ell^1\) follows by applying the projection to a point mass. Thus (1) is the actual sharp operator norm, not merely a kernel estimate.

**4. Linear depth asymptotics.** In a valuation stratum of type \(v+1\notin E_k\), one has \(v\equiv k\pmod2\), so a finite geometric sum gives
\[
\frac{B_{k,v}}{p^v}=\frac{p}{2(p+1)}+O_p(p^{-v}).
\]
In the other type, \(v+1\in E_k\), one has
\[
\frac{B_{k,v}}{p^v}=\frac1{2(p+1)}+O_p(p^{-v}),\qquad
\frac{J_{k,v}^\pm}{p^v}= -\frac{p}{2(p+1)}\pm\frac{T_p}{2}+O_p(p^{-v}).
\]
These estimates are uniform in \(k>v\), including the smallest nonempty layers. In formula (1), a nonboundary stratum contributes
\[
\frac{p-1}{2(p+1)}+O_p(p^{-v}),
\]
whereas a boundary stratum contributes
\[
\frac{p-1}{4p}\left(\left|-\frac p{p+1}+T_p\right|+
\left|-\frac p{p+1}-T_p\right|\right)+O_p(p^{-v}).
\]
The sum of the two absolute values equals \(2\sqrt p\) for \(p\equiv1\pmod4\), because \(\sqrt p>p/(p+1)\), and equals \(2\sqrt{p+p^2/(p+1)^2}\) for \(p\equiv3\pmod4\). Half the valuations of \(0\le v<k\), up to a discrepancy of one, belong to each class. Summing the exponentially summable errors gives \(O_p(1)\); the zero-frequency term \(H_{p,k}/p^k\) is also bounded. The average of the two displayed stratum contributions is exactly \(\sigma_p\), proving (2).

**5. The role of nonunit squares.** If one projects only onto the **unit** square residues, that set is the full inverse image of \((\mathbb F_p^\times)^2\) under reduction modulo \(p\). Its projection kernel is supported on frequencies divisible by \(p^{k-1}\), and its normalized absolute kernel mass equals the corresponding prime-field norm for all \(k\). The additional even-valuation square shells in \(Q_k\) generate the linearly many nontrivial frequency strata in (1). This establishes the claimed structural contrast.

## Verification
The companion standalone standard-library script `artifacts/verify.py` checks the disjoint square-set decomposition, the predicted Fourier values for every residue, Parseval and orthogonality identities, and the exact endpoint norm against direct finite root-of-unity sums for \((p,k)\in\{(3,1),(3,2),(3,3),(3,4),(3,5),(5,1),(5,2),(5,3),(5,4),(7,2),(7,3),(11,2)\}\). It independently computes the general formula for large depths and checks the predicted linear slope numerically. Run `python3 artifacts/verify.py` at the package root. These are finite corroborations, not a replacement for the valuation, Gauss-sum and geometric-series proof.

## Relationship to prior work
Green and Sanders [1] establish a general quantitative structure theorem for idempotent Fourier multipliers in finite abelian groups; it does not give the sharp norm of the complete square set or its growth coefficient. Konyagin and Shkredov [2] study Wiener norms of subsets of prime cyclic groups and give general lower bounds, whereas the present object includes nonunit squares on composite-order prime-power cyclic groups. Stangl [3] counted distinct squares modulo prime powers; knowing only this cardinality does not determine their Fourier-algebra norm. The classical quadratic Gauss sum [4] evaluates the individual multiplicative-character fibers used in the proof but does not itself state the multiscale projection norm or its linear-depth coefficient. These standard ingredients and their priority are acknowledged.

A published computation of the cubic-residue projection norm on prime cyclic groups [5] treats a different multiplier and no valuation tower. A published theorem on Fourier concentration between two valuation shells [6] concerns the singular spectrum of a time-frequency restriction, not the absolute kernel mass of their union into all quadratic residues. A half-density Fourier-algebra extremal theorem [7] is over odd-order groups but concerns subsets of size exactly half the group and their universal maximal bound; it does not imply (1) for the complete square set at depth \(k\ge2\). Comparisons are by implication, not merely by titles. No known comparison located the exact statement (1)–(2), although an older unindexed cyclotomic Wiener-norm identity remains possible.

## Limitations
The novelty assessment is bounded by searches and accessible primary sources. The original text of Stangl [3] was not accessible during comparison; published bibliographic and formula evidence identify its square-counting result, not an exact Fourier norm. Classical cyclotomy could contain an equivalent all-depth formula under another terminology. The \(O_p(1)\) error is not optimized, the prime \(2\) is excluded, and no interior \(\ell^r\) operator norm is asserted. Numerical checks cover only their enumerated finite cases; the all-depth assertion is proved analytically. No independent mathematical validation has been performed.

## References
[1] B. Green and T. Sanders, *A quantitative version of the idempotent theorem in harmonic analysis*, arXiv:math/0611286v1 (first public 2006-11-09), https://arxiv.org/abs/math/0611286.

[2] S. V. Konyagin and I. D. Shkredov, *On Wiener norm of subsets of Z_p of medium size*, arXiv:1403.8129v1 (first public 2014-03-31), https://arxiv.org/abs/1403.8129.

[3] W. D. Stangl, *Counting Squares in Z_n*, Mathematics Magazine 69 (1996), 285–289, DOI 10.1080/0025570X.1996.11996456.

[4] Classical quadratic Gauss-sum evaluation, e.g. B. C. Berndt, R. J. Evans, K. S. Williams, *Gauss and Jacobi Sums*, Wiley (1998), Chapter 1.

[5] *Exact cubic-residue Lebesgue constants from Gaussian period arithmetic*, published result ID 2026/10/11/SCOPE-exact-cubic-residue-lebesgue-constants-from-gaussian-period-arit--36f40db19f8d, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-cubic-residue-lebesgue-constants-from-gaussian-period-arit--36f40db19f8d.

[6] *Exact Fourier concentration spectrum between valuation shells on Z/p^n Z*, published result ID 2026/10/11/SCOPE-exact-fourier-concentration-spectrum-between-valuation-shells-on--ccd67aef93b8, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fourier-concentration-spectrum-between-valuation-shells-on--ccd67aef93b8.

[7] *Exact half-density Fourier-algebra deficit and difference-set stability*, published result ID 2026/10/11/SCOPE-exact-half-density-fourier-algebra-deficit-and-difference-set-st--c366350c5366, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-half-density-fourier-algebra-deficit-and-difference-set-st--c366350c5366.
