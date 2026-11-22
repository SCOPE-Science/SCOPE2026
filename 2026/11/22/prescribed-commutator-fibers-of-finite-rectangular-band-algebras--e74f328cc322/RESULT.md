# Prescribed-commutator fibers of finite rectangular-band algebras

## Finding
For all integers \(m,n\ge1\), prime powers \(q\), and matrices \(Z\in M_{m\times n}(\mathbb F_q)\), determine the number
\[
 F(Z)=\#\{(X,Y)\in A^2:X\star Y-Y\star X=Z\},
 \quad A=\mathbb F_q[[m]\times[n]],
\]
where the rectangular band has product \((i,j)(k,l)=(i,l)\). Put \(h=(m-1)(n-1)\), let \(r(Z)=Z\mathbf1_n\) and \(c(Z)=\mathbf1_m^\mathsf TZ\), and let \(R=\operatorname{rank}Z\) mean *ordinary coefficient-matrix rank*. For every nonzero \(Z\) with \(\mathbf1_m^\mathsf TZ\mathbf1_n=0\), the **complete nonzero-target fiber census** is
\[
\boxed{
\begin{array}{c|c|c}
R&\text{conditions on }(r(Z),c(Z))&F(Z)\\\hline
1&(0,0)&(q^2-1)q^{2h}(q^{m-1}+q^{n-1}-q)\\
1&(\ne0,0)&(q^2-1)q^{2h+m-1}\\
1&(0,\ne0)&(q^2-1)q^{2h+n-1}\\
2&(0,0)&q^{2h}(q^2-1)(q^2-q)\\
2&(\ne0,\ne0)&q^{2h}q(q^2-1)
\end{array}}
\]
All unlisted nonzero targets have **zero** representations: in particular, a rank-two target with just one of \(r(Z),c(Z)\) zero never occurs. Rank exceeding two or nonzero total sum also prevents representation. Empty strata in small dimensions are harmless: the displayed rules apply to targets that exist.

For completeness, the zero fiber is
\[
\begin{split}
F(0)&=q^{2h}K,\\
K&=q^{m+n-1}+(q^{n-1}-1)q^{n-1}+(q^{m-1}-1)q^{m-1}\\
&\quad+q\bigl(q^{m+n-1}-q^{m-1}-q^{n-1}+1\bigr).
\end{split}
\]
The zero-fiber and rank-aggregated count were previously known; the claim of a new result concerns the **nonzero prescribed-target fiber classes, their exact values, and the resulting image criterion**, not those prior aggregate counts.

## Assumptions and scope
The algebra \(A\) is the (possibly nonunital) associative semigroup algebra over \(\mathbb F_q\) of the *labelled* rectangular band \([m]\times[n]\). The coefficient-array identification with \(M_{m\times n}(\mathbb F_q)\) is fixed. The product \(\star\) is induced by the rectangular-band multiplication, **not** ordinary matrix multiplication. All \(q\) are prime powers, including even characteristic. Both \(X,Y\) range over the entire \(q^{mn}\)-element algebra. No algebraic-closure point count or quotient by automorphisms is intended.

## Proof
**Linear reduction.** Write \(p(X)=X\mathbf1_n\in\mathbb F_q^m\), \(b(X)=\mathbf1_m^\mathsf TX\in\mathbb F_q^n\), and \(\ell\) for coordinate sum. The band rule gives
\[
 X\star Y=p(X)b(Y),\qquad [X,Y]=p(X)b(Y)-p(Y)b(X).
\]
The map \(X\mapsto(p(X),b(X))\) surjects onto the hyperplane \(W=\{(p,b):\ell(p)=\ell(b)\}\) of dimension \(m+n-1\), with every fiber of size \(q^h\). Surjectivity follows by freely assigning a first row and column and then solving for the corner entry. Therefore every admissible ordered quadruple of sum vectors has exactly \(q^{2h}\) lifts to \((X,Y)\).

Fix \((p,b)\in W\). The linear map in the sum vectors of \(Y\), written \((s,d)\in W\), is \(L_{p,b}(s,d)=p d^\mathsf T-s b^\mathsf T\). Its rank and kernel dimension follow by cases. If \(p=b=0\), it is zero. If \(p=0,b\ne0\), its image consists of all matrices \(-s b^\mathsf T\) with arbitrary \(s\), and its kernel size is \(q^{h+n-1}\); dually, for \(p\ne0,b=0\), the kernel size is \(q^{h+m-1}\). If both are nonzero, the kernel is the one-dimensional family \((s,d)=\lambda(p,b)\), hence kernel size \(q^{h+1}\). This also produces \(K\) by summing the four possibilities: there are respectively \(1\), \(q^{n-1}-1\), \(q^{m-1}-1\), and \(q^{m+n-1}-q^{n-1}-q^{m-1}+1\) sum-vector pairs of the four types.

**Rank-one targets.** Let \(Z=z w^\mathsf T\ne0\). A rank-one matrix lies in \(\operatorname{im}L_{p,b}\) for \(p,b\ne0\) exactly when either \(p\) is proportional to \(z\) and \(\ell(w)=0\), or \(b\) is proportional to \(w\) and \(\ell(z)=0\). Indeed, reduction modulo the span of \(p\), or modulo the span of \(b\), forces one of these proportionalities. Substituting the proportional factorization into \(p d^\mathsf T-s b^\mathsf T=zw^\mathsf T\), the common-total constraint \(\ell(s)=\ell(d)\) yields precisely the stated zero-sum condition. If \(p=0,b\ne0\), membership is equivalent simply to \(b\) being proportional to \(w\), with \(\ell(b)=0\); the dual one-sided case requires \(p\) proportional to \(z\) and \(\ell(p)=0\).

For \(\ell(z)=0\), \(\ell(w)\ne0\) (equivalently \(r(Z)\ne0,c(Z)=0\)), there are \((q-1)q^{m-1}\) admissible pairs \(p,b\ne0\) with \(b\) proportional to \(w\), and \(q-1\) additional pairs with \(p\ne0,b=0\), \(p\) proportional to \(z\). Accounting for \(q^h\) lifts of \(X\) and the just-computed kernels for \(Y\) gives
\[
(q-1)q^{m-1}q^{2h+1}+(q-1)q^{2h+m-1}
=(q^2-1)q^{2h+m-1}.
\]
The case \(\ell(z)\ne0,\ell(w)=0\) is transposed. If both sums vanish, the number of pairs \(p,b\ne0\) meeting either proportionality condition is
\[
(q-1)\bigl((q^{m-1}-1)+(q^{n-1}-1)-(q-1)\bigr).
\]
The one-sided cases contribute \((q-1)(q^{m-1}+q^{n-1})q^{2h}\) after the correct kernel factors, and the two-sided cases contribute \((q-1)(q^{m-1}+q^{n-1}-q-1)q^{2h+1}\). Their sum simplifies to the listed \((q^2-1)q^{2h}(q^{m-1}+q^{n-1}-q)\). As \(\ell(z)\ell(w)=0\) is necessary for a nonzero commutator, these exhaust rank one.

**Rank-two targets.** Let \(Z\) have rank two. Every representation must have both \((p,s)\) and \((d,b)\) linearly independent. Set \(U=(p,s)\) and \(V=(d,-b)\), so \(Z=UV^\mathsf T\). The common-total restrictions translate to
\[
\mathbf1_m^\mathsf TU=(a_1,a_2),\quad
\mathbf1_n^\mathsf TV=(a_2,-a_1)=(a_1,a_2)J,
\quad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Choose a full-rank factorization \(Z=U_0V_0^\mathsf T\). All such ordered full-rank factorizations are uniquely \((U_0G,V_0G^{-\mathsf T})\) for \(G\in\mathrm{GL}_2(q)\). Let \(a=\mathbf1_m^\mathsf TU_0\), \(b=\mathbf1_n^\mathsf TV_0\). The zero-total condition is \(a b^\mathsf T=0\). Furthermore \(r(Z)=U_0 b^\mathsf T\) and \(c(Z)=aV_0^\mathsf T\), so their vanishing is equivalent to \(b=0\), respectively \(a=0\).

If \(a=b=0\), all \(|\mathrm{GL}_2(q)|=(q^2-1)(q^2-q)\) factorizations satisfy the sum restrictions. If exactly one vanishes, none does. If both are nonzero, orthogonality in dimension two gives a unique \(\lambda\ne0\) with \(b=\lambda aJ\). Under the basis change, the restriction becomes \(\det(G)=\lambda\), since \(GJG^\mathsf T=(\det G)J\). This has exactly \(|\mathrm{SL}_2(q)|=q(q^2-1)\) solutions. Finally multiply by \(q^{2h}\) for the independent lifts of \(X,Y\). No rank above two is possible by the factorization, and all image restrictions have now been established.

## Verification
Run the standalone Python 3 script `verify_rectfib.py` with no third-party packages. It directly expands the rectangular-band product in coefficient arrays, enumerates every ordered pair and every prescribed target at \((m,n,q)=(2,2,2),(2,3,2),(3,2,2),(2,2,3),(3,3,2)\), and compares each exact fiber against the displayed formula; all five configurations pass. The largest checks \(512^2\) pairs and includes rank-two targets with both total vectors zero. The captured program output is in `verification_output.txt`. These finite checks are corroboration only; the foregoing parameter-and-fiber argument proves the formulas for all finite fields and dimensions.

## Relationship to prior work
Choi, Gourdeau and White (arXiv:1004.2301, first posted 2010-04-14) give the rectangular-band framework and calculate homological invariants of band semigroup algebras; their §§2 and 7 do not give nonzero finite-field commutator fibers. Livshits, MacDonald, Mathes and Radjavi (2001) study band algebras and their commutator structure in operator theory. The earlier exact **rank-aggregated** census *Commutator-rank census of finite rectangular-band semigroup algebras* (published-finding corpus identifier `2026/11/2/SCOPE-commutator-rank-census-of-finite-rectangular-band-semigroup-alge--6f0f9b3726a9`) already gives \(F(0)\) and all numbers of pairs having commutator rank zero, one, or two. We take that work as prior and do not attribute its aggregate result to this finding. The current prescribed-target formulas distinguish the support geometry and different nonzero fibers *within the same rank*, which aggregate rank counts and element centralizer dimensions alone do not specify.

## Limitations
Only this rectangular-band semigroup algebra, with its canonical coefficient array, is treated; the theorem is not asserted for arbitrary Rees sandwich matrices, nonrectangular bands, or full matrix algebras. The unproved extrapolation to arbitrary associative semigroup algebras is not made. Prior literature can contain implicit equivalent formulas not indexed by our search terms. The computations cover only indicated prime fields and dimensions, not all prime powers; the field-independent proof supplies the infinite statement. Independent validation has not been performed.

## References
1. Y. Choi, F. Gourdeau, M. C. White, *Simplicial cohomology of band semigroup algebras*, arXiv:1004.2301, first posted 2010-04-14, https://arxiv.org/html/1004.2301v2.
2. L. Livshits, G. MacDonald, B. Mathes, H. Radjavi, *On band algebras*, Journal of Operator Theory 46 (2001), 545–560, https://jot.theta.ro/jot/archive/2001-046-003/2001-046-003-005.pdf.
3. *Commutator-rank census of finite rectangular-band semigroup algebras*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-commutator-rank-census-of-finite-rectangular-band-semigroup-alge--6f0f9b3726a9/RESULT.md.
4. MSC2020, *16S36: Ordinary and skew polynomial rings and semigroup rings*, https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=16-04.
