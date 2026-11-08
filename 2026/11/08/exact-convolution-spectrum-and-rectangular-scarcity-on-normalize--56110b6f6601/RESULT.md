# Exact convolution spectrum and rectangular scarcity on normalized finite-field rank-one matrices

## Finding
Fix a prime power \(q\), integers \(m,n\ge2\), and the additive group \(G=M_{m,n}(\mathbb F_q)\). Let \(S\subseteq G\) be **all rank-one matrices whose total entry sum equals one**, and define the unnormalized convolution \(T f(X)=\sum_{Z\in S}f(X+Z)\). Put \(d=m-1\), \(e=n-1\), and \(k=\min(d,e)\). For each \(0\le r\le k\) define the number of rank-\(r\) matrices \(N_{d,e}(r)\) by
\[
N_{d,e}(r)=\prod_{j=0}^{r-1}\frac{(q^d-q^j)(q^e-q^j)}{q^r-q^j},\qquad N_{d,e}(0)=1.
\]
The **complete singular-value multiset** of \(T\) consists of \(q^{d+e-r}\) with multiplicity \(q^{2r+1}N_{d,e}(r)\) for every \(0\le r\le k\), plus zero with multiplicity
\[
q^{mn}-\sum_{r=0}^k q^{2r+1}N_{d,e}(r).
\]
In fact every nonzero Fourier eigenvalue is a \(p\)-th root of unity times \(q^{d+e-r}\), where \(p\) is the characteristic; for every level \(r\) and every \(p\)-th root, the multiplicity is exactly \(q^{2r+1}N_{d,e}(r)/p\). Thus the positive spectral condition number is exactly \(q^k\). The kernel is nonzero in every allowed dimension.

There is also an exact aspect-ratio law for the **proportion \(\rho_{d,e}\) of nonzero Fourier multipliers**. If \(e=d+h\) with \(h\ge0\), and \(B\) is uniform among \(d\times(d+h)\) matrices, then
\[
\rho_{d,d+h}=q^{-h}\mathbb E\bigl[q^{-2(d-\operatorname{rank}B)}\bigr].
\]
Writing \(\phi_j=\prod_{i=1}^j(1-q^{-i})\), \(\phi_0=1\), and \(\phi_\infty=\prod_{i=1}^\infty(1-q^{-i})\), we have the convergent fixed-width limit
\[
\lim_{d\to\infty}\rho_{d,d+h}=q^{-h}\sum_{s=0}^\infty q^{-2s-s(s+h)}\frac{\phi_\infty}{\phi_s\phi_{s+h}}.
\]
The limiting proportion, multiplied by \(q^h\), tends to one as \(h\to\infty\). For fixed \(q\), square families therefore retain a positive limiting proportion of Fourier modes, whereas families of increasing rectangular excess lose a proportion asymptotic to \(q^{-h}\).

## Assumptions and scope
The prime-power field may have any characteristic, including two. Fix any nontrivial additive character \(\psi\) of \(\mathbb F_q\); the Fourier pairing is \(\psi(\operatorname{tr}(A^\top X))\) on \(G\), with **ordinary matrix trace** (not a field trace). Frequencies are counted with multiplicity over the full complex space of functions on \(G\). Convolution uses counting measure, not probability normalization. An overall Fourier phase convention changes eigenvalue phases but not singular values. The zero matrix is excluded automatically by the total-sum-one condition. No restrictions on the aspect ratio are imposed.

## Proof
**Unique normalized factorization.** If \(X=uv^\top\) has rank one and total entry sum one, then \((\sum_i u_i)(\sum_j v_j)=1\); rescaling the factorization uniquely makes both sums one. Thus \(S\) is parametrized without duplication by \(u\in H_m=\{u: \sum_i u_i=1\}\), \(v\in H_n\), and \(|S|=q^{d+e}\).

**Bilinear character sum.** Choose basepoints \(u_0,v_0\) of these affine hyperplanes and matrices \(U\), \(V\) whose columns are bases of the corresponding zero-sum direction spaces. Write \(u=u_0+Ux\), \(v=v_0+Vy\). For every frequency matrix \(A\), set \(B=U^\top A V\), \(\ell=U^\top A v_0\), \(h=V^\top A^\top u_0\), and \(c=u_0^\top A v_0\). Since both the left and right choices are bases after adjoining the basepoints, the map \(A\mapsto(B,\ell,h,c)\) is a vector-space bijection. Hence the eigenvalue is
\[
\lambda_A=\psi(c)\sum_{x\in\mathbb F_q^d,y\in\mathbb F_q^e}\psi(x^\top By+\ell^\top x+h^\top y).
\]
Summing in \(x\) by additive character orthogonality gives zero unless \(\ell\in\operatorname{im}B\). For such \(\ell\), choose \(y_0\) solving \(By_0=-\ell\); the remaining affine fiber is \(y_0+\ker B\). Summing over this fiber gives zero unless \(h\in\operatorname{im} B^\top\), and otherwise gives exactly
\[
\lambda_A=q^{d+e-r}\psi(c+h^\top y_0),\qquad r=\operatorname{rank}B.
\]
The scalar phase is independent of the chosen \(y_0\), because \(h\) annihilates \(\ker B\).

**Exact multiplicities.** There are \(N_{d,e}(r)\) rank-\(r\) choices of \(B\), \(q^r\) permitted choices of each of \(\ell,h\), and \(q\) choices of \(c\). Exactly \(q^{2r+1}N_{d,e}(r)\) frequencies have that nonzero modulus. The character \(\psi\) takes each characteristic-prime root exactly \(q/p\) times as \(c\) varies, proving the complex-eigenvalue multiplicities. Fourier characters diagonalize \(T\) unitarily. As \(r\) ranges from zero to \(k\), the largest and smallest positive singular values are \(q^{d+e}\) and \(q^{d+e-k}\); their quotient is \(q^k\). For \(B=0\) and \(\ell\ne0\) the multiplier is zero, so the kernel is nontrivial.

**Rectangular limit.** Divide the nonzero-frequency count by \(q^{(d+1)(e+1)}\), and count \(B\) uniformly to obtain \(\rho_{d,e}=\mathbb E_B[q^{2\operatorname{rank}B-d-e}]\). With \(e=d+h\) and rank deficit \(s=d-\operatorname{rank}B\), use the exact rank-counting product to get
\[
\Pr(s)=q^{-s(s+h)}\frac{\phi_d\phi_{d+h}}{\phi_s\phi_{s+h}\phi_{d-s}},\quad 0\le s\le d.
\]
At fixed \(s,h\), this converges to \(q^{-s(s+h)}\phi_\infty/(\phi_s\phi_{s+h})\). Because \(\phi_j\ge\phi_\infty>0\), the probabilities are uniformly bounded by \(\phi_\infty^{-3}q^{-s(s+h)}\), which is summable; dominated convergence proves the displayed limit. Finally \(\Pr(s=0)\to\phi_\infty/\phi_h\to1\) as \(h\to\infty\), and \(0\le q^{-2s}\le1\) controls the remainder. This proves the rectangular asymptotic.

## Verification
The accompanying standalone `checker.py` enumerates complete Fourier spectra in multiple binary and odd-prime small cases, verifies the predicted positive/zero multiplicities and the phase-resolved multiplicities, and verifies the exact count of normalized rank-one matrices. It is finite corroboration; the proof above establishes all prime powers and dimensions.

## Relationship to prior work
Delsarte's rank-metric association scheme gives classical Fourier spectral information for **unrestricted rank orbits** of finite matrices; Orel studies the rank-one **symmetric** matrix adjacency spectrum. Neither statement directly yields the present spectrum after imposing a nonzero total-entry-sum constraint. That constraint selects an affine Segre patch, is not invariant under the rank-metric association scheme's general linear actions, and creates the two independent row/column solvability conditions \(\ell\in\operatorname{im} B\), \(h\in\operatorname{im} B^\top\). The claimed contribution is their exact complete harmonic spectrum and the rectangular Fourier-support law, not the classical character-orthogonality or matrix rank-counting ingredients. Closely related algebraic Fourier literature could still imply the special case indirectly.

## Limitations
The operator is singular; the reported condition number \(\kappa_+\) concerns only its nonzero singular spectrum, **not** an inverse on all functions. No claim of optimal recovery after adding further observations is made. The fixed-width asymptotic assumes fixed \(q\), \(h\) as \(d\to\infty\); the subsequent \(h\to\infty\) limit is sequential, not a uniform joint limit. The priority comparison is bounded and not an independent literature certification.

## References
1. P. Delsarte, Bilinear forms over a finite field, with applications to coding theory, J. Combin. Theory A 25 (1978), 226–241, doi:10.1016/0097-3165(78)90015-8 (first-public-date evidence: 1978-11-01).
2. M. Orel, Adjacency preservers, symmetric matrices, and cores, J. Algebraic Combin. 35 (2012), 633–647, doi:10.1007/s10801-011-0318-0 (online 2011-10-08).
