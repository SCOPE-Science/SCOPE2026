# Complete endomorphism-rank census and a two-scale limit law for standard filiform Lie algebras

## Finding
For any prime power \(q\) and integer \(n\ge4\), let \(L_n(q)\) be the \(n\)-dimensional Lie algebra over \(\mathbb F_q\) with ordered basis \(e_1,\ldots,e_n\), and nonzero basis brackets
\[
[e_1,e_i]=e_{i+1}\qquad(2\le i<n),
\]
with alternation and all other basis brackets zero. Write \(E_{n,q}(z)=\sum_{\varphi\in\operatorname{End}_{\mathrm{Lie}}(L_n(q))}z^{\operatorname{rank}(\varphi)}\). Then the *complete labeled endomorphism-rank polynomial* is
\[
\boxed{\begin{aligned}
E_{n,q}(z)={}&1+(q+1)(q^n-1)z\\
&+\left[q^{2n-2}+(q^3-q^2-2q)q^{n-1}+q\right]z^2\\
&+(q-1)^2(q+1)q^n z^3\\
&+\sum_{r=4}^n(q-1)^2q^{n+r-3}z^r.
\end{aligned}}
\]
Here rank is vector-space image dimension, not a rank of the adjoint action. Consequently,
\[
\big|\operatorname{End}_{\mathrm{Lie}}(L_n(q))\big|=q^{2n-1}+(q-1)q^{n+2},
\qquad
\big|\operatorname{Aut}(L_n(q))\big|=(q-1)^2q^{2n-3}.
\]
There is a two-scale asymptotic law. For a uniformly sampled endomorphism \(\Phi_n\) and each **fixed** finite-field size \(q\),
\[
\lim_{n\to\infty}\Pr(\operatorname{rank}\Phi_n=2)=\frac1q,
\quad
\lim_{n\to\infty}\Pr(\operatorname{rank}\Phi_n=n-d)=\frac{(q-1)^2}{q^{d+2}}
\quad(d=0,1,2,\ldots).
\]
The second mass series sums to \(1-1/q\), while all other fixed small ranks receive asymptotically zero mass. Thus a positive fraction of endomorphisms retain a two-dimensional image even though the remaining mass lives at bounded corank.

## Assumptions and scope
All fields \(\mathbb F_q\) of prime-power order, including characteristic two, are allowed. The bracket above is alternating, including in characteristic two. Maps are all \(\mathbb F_q\)-linear Lie algebra homomorphisms from \(L_n(q)\) to itself, counted individually, not up to conjugation. No injectivity or surjectivity is assumed. The dimension lower bound \(n\ge4\) excludes the three-dimensional Heisenberg case, for which the relation used below changes. Limits are at fixed \(q\), with \(n\) tending to infinity.

## Proof
Write \(H=\langle e_2,\ldots,e_n\rangle\), an abelian ideal of codimension one, and let \(N\) shift \(e_i\) to \(e_{i+1}\) for \(2\le i<n\), with \(Ne_n=0\). Every endomorphism is determined by its two generating images
\[
u=\varphi(e_1)=a e_1+\sum_{i=2}^n u_ie_i,\qquad
v=\varphi(e_2)=A e_1+\sum_{i=2}^n v_ie_i,
\]
because \(\varphi(e_j)=(\operatorname{ad}_u)^{j-2}v\) for \(3\le j\le n\).

For \(w=[u,v]\), the coefficient of \(e_j\) (\(3\le j\le n\)) is \(a v_{j-1}-A u_{j-1}\). Every \(\varphi(e_j)\) for \(j\ge3\) lies in \(\langle e_3,\ldots,e_n\rangle\), on which \(\operatorname{ad}_u\) is multiplication by \(aN\). Hence all defining relations except the commutation among \(e_2,\ldots,e_n\) hold automatically. That last family holds if and only if \([v,w]=0\): if \(A=0\), the images \(v,w,\ldots\) lie in \(H\); if \(A\ne0\), the condition \([v,w]=0\) forces \(w\in\mathbb F_q e_n\) and all later images vanish. Equivalently, the only restriction on the two free generating images is
\[
\boxed{A(a v_i-Au_i)=0\qquad(2\le i\le n-2).}
\]
We now enumerate four disjoint cases, keeping the actual ranks.

**Case \(a=A=0\).** Both generators map into \(H\) and all later images vanish. The independent ordered pairs in an \((n-1)\)-space give ranks zero, one and two, with counts respectively
\[
1,\qquad(q^{n-1}-1)(q+1),\qquad(q^{n-1}-1)(q^{n-1}-q).
\]

**Case \(A=0\), \(a\ne0\).** There are \((q-1)q^{n-1}\) choices of \(u\). If \(v=0\), rank is one. Otherwise let \(j\ge2\) be the least index with \(v_j\ne0\). The \(N\)-chain \(v,Nv,\ldots\) has length \(n-j+1\), with successive distinct leading coordinates, and is independent of the \(e_1\)-component of \(u\). Therefore the image has rank \(r=n-j+2\). For every \(2\le r\le n\), the count is exactly \((q-1)^2q^{n+r-3}\); the rank-one count is \((q-1)q^{n-1}\).

**Case \(a=0\), \(A\ne0\).** The relation gives \(u_2=\cdots=u_{n-2}=0\), and \(v\) is arbitrary with nonzero \(e_1\)-component. Thus \(u=u_{n-1}e_{n-1}+u_ne_n\), while \([u,v]=-A u_{n-1}e_n\), and all later images vanish. The rank-one, rank-two and rank-three counts are respectively
\[
(q-1)q^{n-1},\quad(q-1)^2q^{n-1},\quad(q-1)^2q^n.
\]

**Case \(aA\ne0\).** Put \(c=A/a\). The relation says \(v_i=c u_i\) for \(2\le i\le n-2\). The remaining independent parameters are \(s=v_{n-1}-c u_{n-1}\) and \(t=v_n-c u_n\), so that
\[
v-cu=s e_{n-1}+t e_n,\qquad [u,v]=a s e_n.
\]
The rank is one when \(s=t=0\), two when \(s=0,t\ne0\), and three when \(s\ne0\). Their respective counts are
\[
(q-1)^2q^{n-1},\quad(q-1)^3q^{n-1},\quad(q-1)^3q^n.
\]

Adding these four cases gives the displayed polynomial, including the coefficient of \(z^2\), which simplifies to \(q^{2n-2}+(q^3-q^2-2q)q^{n-1}+q\). Evaluation at \(z=1\) gives the total \(q^{2n-1}+(q-1)q^{n+2}\). Only the full-rank case of \(A=0,a\ne0\) contributes automorphisms, giving \((q-1)^2q^{2n-3}\).

For the two-scale limit, divide each coefficient by the exact total. For fixed \(q\), the denominator equals \(q^{2n-1}(1+O_q(q^{-n+3}))\). The rank-two coefficient is \(q^{2n-2}+O_q(q^{n+2})\). At every fixed corank \(d\ge0\), the large-rank coefficient is \((q-1)^2q^{2n-d-3}\) for all sufficiently large \(n\). Dividing yields the two asserted limits, and the geometric series \(\sum_{d\ge0}(q-1)^2q^{-d-2}=(q-1)/q\) exhausts the mass outside rank two.

## Verification
The standalone `verification/check_filiform.py` is a direct finite-field enumerator independent of the four-case enumeration used above. For each ordered pair of generating images, it constructs every image recursively using the Lie bracket, checks all remaining basis bracket relations, computes the actual matrix rank by modular Gaussian elimination, and compares the entire observed rank table with the closed formula. It exhaustively checked \((n,q)=(4,2),(5,2),(6,2),(7,2),(4,3),(5,3),(4,5)\). All seven cases passed, including all 140625 homomorphisms in the last instance. The captured exact output is `verification/check_output.txt`. Run `python verification/check_filiform.py` with Python 3, without dependencies. The proof, not the finite tests, supports every dimension and prime-power field.

## Relationship to prior work
Bahturin, Goze and Remm (2013, arXiv:1308.2396v1) define and investigate the standard filiform algebra and its automorphisms/gradings, but do not determine its full singular-endomorphism rank census. Avetisyan (2016, arXiv:1610.05365v1), especially Section 4, gives the general almost-Abelian homomorphism framework and automorphism block form; it substantially precedes the elementary generator-compatibility analysis here. Its statements do not provide the finite-field rank-by-rank counts or the split limiting law. Previously published calculations on this same family give adjoint-action ranks and fixed-point-free automorphism multiplicities, which do not determine the singular-endomorphism ranks. Idempotent derivations are a different operator problem. Therefore no novelty is asserted for the Lie algebra definition, general homomorphism compatibility theory, or the automorphism count; only the evaluated complete endomorphism rank polynomial and the two-scale law are proposed as new.

## Limitations
Only the canonical standard filiform family is treated; other filiform deformations, endomorphism composition laws, kernel ideal isomorphism types, and conjugacy-class counts are not classified. Historical priority is provisional: an unindexed earlier calculation or a direct derivation from general homomorphism theory could supersede these formulas. Exhaustive arithmetic checks over prime fields are not a substitute for the proof over every prime-power field. No independent audit or external certification is claimed.

## References
1. Y. Bahturin, M. Goze and E. Remm, *Group gradings on filiform Lie algebras*, arXiv:1308.2396v1, publicly posted 2013-08-11. https://arxiv.org/html/1308.2396v1
2. Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365v1, publicly posted 2016-10-17, Section 4. https://arxiv.org/abs/1610.05365
3. *Adjoint-rank spectra of two maximal-class filiform Lie algebras*, public record 48cdbeaf7d86. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-adjoint-rank-spectra-of-two-maximal-class-filiform-lie-algebras--48cdbeaf7d86
4. *Finite-field fixed-point-free automorphism counts for standard filiform Lie algebras*, public record 5844778e738d. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-finite-field-fixed-point-free-automorphism-counts-for-standard-f--5844778e738d
5. *Idempotent derivation rank spectra of model filiform Lie algebras over finite fields*, public record 165f62a620cd. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-idempotent-derivation-rank-spectra-of-model-filiform-lie-algebra--165f62a620cd
