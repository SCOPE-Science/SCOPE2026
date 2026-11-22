# Simultaneous opposite-product fibers of minimal nilpotent matrices

## Finding
Let \(k=\mathbb F_q\) for an arbitrary prime power \(q\), let \(n\ge2\), and let
\[
\mathcal N_{n,q}=\{X\in M_n(k):\operatorname{rank}X=1,\ X^2=0\}.
\]
For *every* prescribed ordered pair \((P,Q)\in M_n(k)^2\), the number of ordered pairs \((X,Y)\in\mathcal N_{n,q}^2\) satisfying \(XY=P\) **and simultaneously** \(YX=Q\) has exactly the following four cases:
\[
F_{n,q}(P,Q)=
\begin{cases}
Z_{n,q},&P=Q=0,\\
K_{n,q},&P\ne0,\ P^2=0,\ \operatorname{rank}P=1,\ Q=0,\\
K_{n,q},&Q\ne0,\ Q^2=0,\ \operatorname{rank}Q=1,\ P=0,\\
q-1,&\operatorname{rank}P=\operatorname{rank}Q=1,\quad
 \operatorname{tr}P=\operatorname{tr}Q\ne0,\quad PQ=QP=0,\\
0,&\text{otherwise},
\end{cases}
\]
where, with \(L_j=(q^j-1)/(q-1)\),
\[
N_{n,q}=L_n(q^{n-1}-1),\quad
K_{n,q}=q^{n-1}(q^{n-2}-1),\quad
Z_{n,q}=N_{n,q}\big[(q^{n-1}-1)+(L_{n-1}-1)(q^{n-2}-1)\big].
\]
For \(n=2\), the two one-sided nilpotent cases have zero multiplicity. All other displayed positive multiplicities occur for their specified target classes.

For every nonzero, mutually annihilating rank-one pair \((P,Q)\) of equal nonzero trace, its factorization set is a canonical one-parameter multiplicative torsor after choosing image-line representatives: there are exactly \(q-1\) factorizations. The number of such prescribed ordered target pairs is
\[
H_{n,q}=(q^n-1)q^{2n-3}L_{n-1}.
\]
Thus the total number of joint target pairs occurring is \(1+2N_{n,q}+H_{n,q}\) for \(n\ge3\), and \(1+H_{2,q}\) for \(n=2\). Their total weighted mass is
\[
Z_{n,q}+2N_{n,q}K_{n,q}+H_{n,q}(q-1)=N_{n,q}^2.
\]

A particularly useful equivalent interpretation holds in odd characteristic. Define the **unnormalized** Jordan product \(J=XY+YX\) and Lie bracket \(C=XY-YX\). The complete prescribed joint \((J,C)\)-fiber law is obtained by putting \(P=(J+C)/2\) and \(Q=(J-C)/2\) in the formula above. In its rank-two stratum, \(J\) is a nonzero scalar multiple of a rank-two projection and \(C\) is split semisimple with eigenvalues \(\lambda,-\lambda\) on the same image plane. Every admissible ordered pair \((J,C)\) has **exactly \(q-1\) witnesses**, while a rank-two Jordan target alone has \(q(q^2-1)\) witnesses and a rank-two Lie-bracket target alone has \(2(q-1)\). These marginals do not themselves determine the stated joint fiber law.

## Assumptions and scope
All matrices act on \(k^n\), rank and trace are computed over \(k\), the factors have rank exactly one (neither zero nor arbitrary square-zero rank), and all pairs are *ordered*, both in the domain and among prescribed output products. Nothing is counted modulo simultaneous similarity. No restriction on the characteristic is used in the opposite-product theorem; the Jordan–Lie change of variables is asserted only when \(2\) is invertible. We count the literal unnormalized Jordan product, not half of it.

## Proof
**1. Parametrization and normalization.** Every \(X\in\mathcal N_{n,q}\) is \(X=u\varphi\) for nonzero \(u\in k^n\) and nonzero \(\varphi\in(k^n)^*\) with \(\varphi(u)=0\). Fixing one nonzero representative on each image line makes the covector unique. There are \(L_n\) image lines and \(q^{n-1}-1\) nonzero annihilating covectors per line. Consequently \(|\mathcal N_{n,q}|=N_{n,q}\).

**2. Restriction on opposite products.** Write \(X=u\varphi\), \(Y=s\psi\), put \(a=\varphi(s)\) and \(b=\psi(u)\), and calculate
\[
P=XY=a u\psi,\qquad Q=YX=b s\varphi.
\]
If \(a=b=0\), both products vanish. If exactly one is nonzero, the corresponding product has rank one and square zero, since its trace is \(ab=0\). If both are nonzero, \(P,Q\) have rank one and equal nonzero trace \(\lambda=ab\). Also \(PQ=XY^2X=0\) and \(QP=YX^2Y=0\). These are the only possibilities.

**3. Both opposite products nonzero: exact factor reconstruction.** Conversely fix rank-one matrices \(P,Q\) with \(\operatorname{tr}P=\operatorname{tr}Q=\lambda\ne0\) and \(PQ=QP=0\). Choose once and for all nonzero \(u\in\operatorname{im}P\) and \(s\in\operatorname{im}Q\), and uniquely write \(P=u\rho\), \(Q=s\sigma\). The two image lines are distinct: if they coincided, \(PQ=0\) would contradict the nonzero trace of \(Q\). Mutual annihilation and trace give
\[
\rho(u)=\sigma(s)=\lambda,\qquad \rho(s)=\sigma(u)=0.
\]
For each \(a\in k^\times\), set
\[
X_a=u\,(a\sigma/\lambda),\qquad Y_a=s\,(\rho/a).
\]
Then \(X_a^2=Y_a^2=0\), both matrices have rank one, and \(X_aY_a=P\), \(Y_aX_a=Q\). Conversely every factor pair has the same image lines and must have this form with \(a=\varphi(s)\in k^\times\). The parameter \(a\) is unique; hence the fiber has size \(q-1\). This simultaneously proves the classification's converse and the reconstruction assertion.

**4. Exactly one product nonzero.** Fix \(P=u\rho\ne0\) with \(\rho(u)=0\). Normalize the image of \(X\) to \(u\) and let the image of \(Y\) run through lines \(ks\) inside \(\ker\rho\) other than \(ku\). There are \(L_{n-1}-1\) such lines. For a fixed nonzero representative \(s\), exactly \((q-1)q^{n-2}\) covectors \(\varphi\) satisfy \(\varphi(u)=0\), \(\varphi(s)\ne0\). Once \(\varphi\) is chosen, \(\psi=\rho/\varphi(s)\) uniquely defines \(Y=s\psi\), and \(YX=0\) automatically. Therefore
\[
F_{n,q}(P,0)=(L_{n-1}-1)(q-1)q^{n-2}=K_{n,q}.
\]
Swapping \(X,Y\) proves the symmetric case. When \(n=2\), no eligible line exists, so the count is zero.

**5. Both products zero.** Fix \(X=u\varphi\). For \(XY=YX=0\), the image line \(ks\) of \(Y=s\psi\) must lie in \(\ker\varphi\), while \(\psi\) annihilates \(ks\) and \(ku\). If \(ks=ku\), there are \(q^{n-1}-1\) nonzero choices of \(\psi\). For each of the remaining \(L_{n-1}-1\) lines of \(\ker\varphi\), the space spanned by \(u,s\) has dimension two and admits \(q^{n-2}-1\) nonzero annihilating covectors. This yields \(Z_{n,q}\) after multiplying by the \(N_{n,q}\) choices of \(X\).

**6. Exact joint target population and normalization.** Every rank-one matrix with nonzero trace can be chosen by selecting its image line, selecting its nonzero trace, and selecting a covector taking that trace on the image representative. Hence the number of possibilities for the first nonzero product \(P\) is \((q^n-1)q^{n-1}\). For a fixed \(P\) of trace \(\lambda\), the image line of an eligible \(Q\) can be any one of the \(L_{n-1}\) lines of \(\ker P\); for each, its covector is uniquely constrained on that line and on \(\operatorname{im}P\), leaving \(q^{n-2}\) choices. Consequently there are exactly \(H_{n,q}\) eligible ordered nonzero-product target pairs. The three disjoint regimes count all factor pairs. Direct expansion of their weighted total gives the asserted identity \(N_{n,q}^2\); this is also forced by the partition into fibers.

**7. Simultaneous Jordan–Lie reconstruction.** For odd \(q\), the equations \(J=P+Q\), \(C=P-Q\) are invertible, so the preceding cases are an exact **joint**, not merely marginal, \((J,C)\)-classification. In the nonzero-product case put \(P=\lambda E\), \(Q=\lambda F\); the rank-one idempotents \(E,F\) satisfy \(EF=FE=0\). Thus \(E+F\) is a rank-two projection, \(J=\lambda(E+F)\), and \(C=\lambda(E-F)\). For fixed rank-two \(J\), there are \((q+1)q\) ordered decompositions of its image plane into two different lines and consequently \((q+1)q\) choices of compatible \(C\). For fixed rank-two \(C\), there are precisely two compatible \(J\) (choose which eigenline carries the positive scalar). Multiplying these counts by the common joint-fiber cardinality \(q-1\) gives the marginal numbers. At rank one \(J=C\) or \(J=-C\), and at zero both vanish. This proves all assertions.

## Verification
The self-contained `verify_joint_products.py` generates every rank-one square-zero matrix by a unique normalized outer-product representation and uses **two literal matrix multiplications** to form \((XY,YX)\). It checks every attained ordered output target, its exact multiplicity, its rank, trace and mutual product equations, the number of admissible target pairs and the total pair mass. Its reproducible output is included in `checks.txt`. Exhaustive factor enumeration was executed for \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(3,5),(4,2)\). All seven cases passed. The program enumerates prime fields; the proof applies independently to every prime-power field.

## Relationship to prior work
Zoque's 2009 study of almost commuting nilpotent matrices treats geometric components of rank-at-most-one *commutator* equations and not the joint prescribed opposite products of two minimal nilpotent factors. Li, Šemrl and Sze (2007) study product-nilpotency preservers and rank-one nilpotent operators, but not finite-field joint multiplication fibers. More closely, the published *Complete multiplication fibers of the minimal nonzero nilpotent orbit over finite fields* determines each individual \(XY\)-fiber and an implication when the reversed product vanishes; *Exact Lie-bracket fibers of the minimal nonzero nilpotent orbit over finite fields* determines every fiber of \(XY-YX\). Both individual marginal results and their overlap are explicitly acknowledged. Neither statement alone specifies the joint output \((XY,YX)\); in particular, their marginal fiber counts do not recover the explicit \(q-1\)-element reconstruction for each ordered orthogonal-idempotent target pair. The present proof makes the dependence between the two outputs explicit and derives the simultaneous Jordan–Lie law in odd characteristic. In characteristic two, the Jordan and Lie combinations coincide, and no separate characteristic-two Jordan novelty is claimed.

## Limitations
The theorem concerns exactly two ordered, nonzero rank-one square-zero factors. It does not cover arbitrary square-zero factors, all nilpotent matrices, longer words, or arbitrary ring coefficients. The exact formulas are proved, but the finite checker is illustrative and not a proof for all prime powers. The two marginal distributions are known and are not claimed as independent discoveries; the proposed novelty is the full target-by-target **joint** law, factor reconstruction and Jordan–Lie coupling. A previously unnoticed orbital-convolution identity or a simultaneous-product theorem could imply this joint law; priority therefore remains provisional pending broader independent comparison. No independent mathematical validation has been performed.

## References
1. E. Zoque, *On the variety of almost commuting nilpotent matrices*, arXiv:0903.2032v1, first public version 2009-03-11. https://arxiv.org/abs/0903.2032
2. C.-K. Li, P. Šemrl and N.-S. Sze, *Maps preserving the nilpotency of products of operators*, Linear Algebra and its Applications 424 (2007), 222–239. Accessible author manuscript: https://cklixx.people.wm.edu/nilpot.pdf
3. *Complete multiplication fibers of the minimal nonzero nilpotent orbit over finite fields*, publicly available result and proof: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-complete-multiplication-fibers-of-the-minimal-nonzero-nilpotent--1bce20858de2/RESULT.md
4. *Exact Lie-bracket fibers of the minimal nonzero nilpotent orbit over finite fields*, publicly available result and proof: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-lie-bracket-fibers-of-the-minimal-nonzero-nilpotent-orbit--ad422a937f4d/RESULT.md
