# Exact symmetric-tensor Hilbert series on decomposable elliptic ruled surfaces

## Finding
Let \(E\) be a smooth complex elliptic curve, let \(L\) be a line bundle of degree \(-d\), with integer \(d\geq1\), and set \(M=\mathbb P_E(\mathcal O_E\oplus L)\), using the quotient convention. For every integer \(m\geq0\),
\[
\boxed{h^0(M,\operatorname{Sym}^m T_M)=1+d\binom{m+2}{3}.}
\]
Consequently the Hilbert series of the algebra \(R=\bigoplus_{m\geq0}H^0(M,\operatorname{Sym}^m T_M)\) is
\[
\boxed{H_R(t)=\frac1{1-t}+\frac{dt}{(1-t)^4}.}
\]
For \(\zeta=c_1(\mathcal O_{\mathbb P(T_M)}(1))\), this implies the numerical contrast
\[
\boxed{\operatorname{vol}(\zeta)=d>0,\qquad \zeta^3=0.}
\]
The algebra \(R\) is known to be non-finitely generated; the exact graded dimensions and the resulting volume are the assertions established here.

## Assumptions and scope
All varieties and bundles are over \(\mathbb C\). The projectivizations parametrize one-dimensional quotients. The result holds for every elliptic curve \(E\), every degree-\(-d\) line bundle \(L\), every positive integer \(d\), and all symmetric exponents \(m\geq0\). The stated volume is the ordinary volume of the tautological divisor on the threefold \(\mathbb P(T_M)\), defined by \(\limsup_{m\to\infty}6h^0(m\zeta)/m^3\). It is not the top intersection number, because \(\zeta\) is not nef.

Write \(f:M\to E\) for the ruling and \(C_-\), \(C_+\) for the disjoint sections with \(C_-^2=-d\), \(C_+^2=d\), and \(\mathcal O_M(C_+-C_-)=f^*L^{-1}\). Let \(\mathscr F_2\) be Atiyah's nonsplit rank-two extension of \(\mathcal O_E\) by \(\mathcal O_E\).

## Proof
**1. Transfer to an elementary transform.** Let \(i:C_-\hookrightarrow M\). The differential of the ruling yields \(T_M|_{C_-}\simeq\mathcal O_{C_-}\oplus L\). Take the rank-two locally free elementary transform \(\mathcal F=\ker(T_M\to i_*L)\). The geometric calculations of Denisi--Höring, cited below, establish
\[
0\longrightarrow\mathcal O_M(C_+)\longrightarrow\mathcal F\longrightarrow\mathcal O_M\longrightarrow0,
\quad \mathcal F|_{C_-}\simeq\mathscr F_2.
\]
They also establish that \(H^0(M,\operatorname{Sym}^m T_M)\simeq H^0(M,\operatorname{Sym}^m\mathcal F)\) for every \(m\). Here is an explicit fixed-divisor explanation of this last fact. Let \(C_0\subset\mathbb P(T_M)\) be the curve of quotient lines \(T_M|_{C_-}\twoheadrightarrow L\), and blow it up, with exceptional divisor \(D\). The conormal bundle of \(C_0\) is \(L^{-1}\otimes\mathscr F_2\), while the tautological divisor \(\zeta\) pulls back to the tautological divisor on \(\mathbb P(\mathcal F)\) plus \(D\), on the common elementary-transform resolution. For each \(0\leq j<m\), the restriction of \(m\zeta-jD\) to \(D\) has direct image to \(C_0\) equal to \(L^{m-j}\otimes\operatorname{Sym}^j\mathscr F_2\). Its degree is negative and the symmetric factor is semistable of degree zero, so its space of sections is zero. Inductively every section of \(m\zeta\) has at least \(mD\) as a fixed part. Removing this part gives the claimed isomorphism of global sections; multiplication is preserved. The conormal and elementary-transform identities can also be checked directly using the normal sequences and the quotient projective-bundle convention.

**2. Compute the cohomology after removal of the negative section.** Taking the \(m\)-th symmetric power of the displayed extension of \(\mathcal F\), and twisting by \(\mathcal O_M(-C_-)\), gives a filtration of
\(\operatorname{Sym}^m\mathcal F(-C_-)\) with successive quotients \(\mathcal O_M(jC_+-C_-)\), for every integer \(0\leq j\leq m\). For \(j=0\), \(\mathcal O_M(-C_-)\) has degree \(-1\) on each ruling fiber, hence all of its cohomology vanishes. For \(j\geq1\), the direct-image calculation for the split projective bundle gives
\[
f_*\mathcal O_M(jC_+-C_-)\simeq\bigoplus_{i=1}^{j} L^{-i},
\qquad R^1f_*\mathcal O_M(jC_+-C_-)=0.
\]
Each summand has positive degree \(id\) on the elliptic curve, so Riemann--Roch gives \(h^0=id\), \(h^1=0\). Applying the long exact sequences along the filtration proves
\[
H^1(M,\operatorname{Sym}^m\mathcal F(-C_-))=0,
\quad h^0(M,\operatorname{Sym}^m\mathcal F(-C_-))
=d\sum_{j=1}^{m}\sum_{i=1}^{j}i=d\binom{m+2}{3}.
\]

**3. Restore the negative section.** Restriction to \(C_-\) gives the exact sequence
\[
0\to\operatorname{Sym}^m\mathcal F(-C_-)\to\operatorname{Sym}^m\mathcal F
\to\operatorname{Sym}^m\mathscr F_2\to0.
\]
In characteristic zero \(\operatorname{Sym}^m\mathscr F_2\simeq\mathscr F_{m+1}\), the indecomposable unipotent bundle of rank \(m+1\), which has precisely one independent global section. The vanishing of \(H^1\) in step 2 therefore yields
\[
h^0(M,\operatorname{Sym}^m\mathcal F)=d\binom{m+2}{3}+1,
\]
including \(m=0\). Step 1 transfers this dimension to \(T_M\). Summing \(\sum_{m\geq0}t^m=(1-t)^{-1}\) and \(\sum_{m\geq0}\binom{m+2}{3}t^m=t(1-t)^{-4}\) gives the Hilbert series.

**4. Compute volume and top self-intersection.** The Hilbert function gives \(\operatorname{vol}(\zeta)=\lim_{m\to\infty}(6/m^3)h^0(M,\operatorname{Sym}^m T_M)=d\). On the other hand \(-K_M=C_-+C_+\), so \(c_1(T_M)^2=(-d)+d=0\); also \(c_2(T_M)=\chi_{\mathrm{top}}(M)=2\chi_{\mathrm{top}}(E)=0\). The rank-two projective-bundle pushforward formula gives \(\zeta^3=c_1(T_M)^2-c_2(T_M)=0\).

## Verification
The independent Hirzebruch--Riemann--Roch calculation for \(\mathcal F\) uses \(c_1(\mathcal F)^2=d\), \(c_2(\mathcal F)=0\), and \(c_1(\mathcal F)\cdot c_1(T_M)=d\). It yields
\[
\chi(M,\operatorname{Sym}^m\mathcal F)=d\frac{m(m+1)(2m+1)}{12}+d\frac{m(m+1)}4=d\binom{m+2}{3}.
\]
This independently checks the polynomial part of the formula; the single additional global section is pinned down by Atiyah's nonsplit restriction, not by Riemann--Roch alone. The accompanying standalone checker performs exact integer checks of the filtration sum, the Hilbert expansion, and the Riemann--Roch identity for specified finite ranges. Those finite tests are consistency checks; the proof above establishes all exponents.

## Relationship to prior work
Kim--Kim determine the bigness threshold for tangent bundles of blow-ups of ruled surfaces, but do not determine the graded symmetric-tensor dimensions of the unblown elliptic family. Denisi--Höring show that for these decomposable elliptic ruled surfaces the symmetric-tensor algebra is not finitely generated and identify it with the section algebra of an elementary transform; their Lemmas 3.3, 3.5, 3.7 and the proof of Theorem 1.4 supply key geometric inputs. The exact Hilbert series, degree-by-degree cohomological calculation, and explicit volume--intersection discrepancy are not stated in those results. Beauville--Liu treat symmetric-tensor algebras in other settings, including ruled surfaces over higher-genus curves; Kim's earlier work determines the bigness criterion for projective bundles over curves. The conclusions here concern the negative-degree split elliptic family rather than the semistable or higher-genus examples in those works.

## Limitations
This result is a Hilbert-function and volume calculation, not a presentation by generators and relations, and it does not classify the minimal new generators in each degree. It relies on the established elementary-transform geometry and Atiyah's classification of degree-zero indecomposable bundles on an elliptic curve. No claim is made in positive characteristic or for nonsplit rank-two bundles defining the ruling. The statement that the algebra is not finitely generated is due to Denisi--Höring, not to this calculation. No independent external audit is claimed.

## References
1. H. Kim and J.-S. Kim, *Bigness of tangent bundles of blow-ups of ruled surfaces*, arXiv:2607.03382v1 (first posted 2026-07-03), Sections 1--3.
2. F. A. Denisi and A. Höring, *Canonical extensions of ruled surfaces over elliptic curves*, arXiv:2610.03048v1 (first posted 2026-10-02), Section 3, particularly Lemmas 3.3, 3.5, 3.7, and Theorem 1.4.
3. M. F. Atiyah, *Vector bundles over an elliptic curve*, Proceedings of the London Mathematical Society, series 3, 7 (1957), 414--452.
4. A. Beauville and J. Liu, *The algebra of symmetric tensors on smooth projective varieties*, arXiv:2309.12888 (first posted 2023-09-22), Section 2.8.
5. J.-S. Kim, *Bigness of the tangent bundles of projective bundles over curves*, arXiv:2206.15413 (first posted 2022-06-30).
