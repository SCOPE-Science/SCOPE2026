# Joint multiplication-rank spectra of finite Alexander-quandle algebras

## Finding

Let \(p\) be a prime, \(m\geq1\), \(G=\mathbb F_p^m\), and \(\varphi\in\operatorname{GL}(G)\). Let \(k=\mathbb F_q\) be a finite field satisfying \(p\mid(q-1)\). The Alexander-quandle algebra \(A=k[\operatorname{Alex}(G,\varphi)]\) has basis \(e_g\) and multiplication
\[
e_xe_y=e_{\varphi x+(I-\varphi)y}.
\]
For \(v\in A\), define \(L_v(w)=vw\) and \(R_v(w)=wv\). Let
\[
h=\operatorname{rank}_{\mathbb F_p}(I-\varphi),\qquad
 d=h-\operatorname{rank}_{\mathbb F_p}((I-\varphi)^2),\qquad
 t=p^{m-h},\qquad j=p^d.
\]
The square denotes composition of the linear map with itself. In particular \(0\leq d\leq\min(h,m-h)\). Then \(t\) divides \(\operatorname{rank}_k R_v\) for every \(v\), and the complete *joint* rank enumerator is
\[
\boxed{\mathcal J_{\varphi,q}(X,Y):=
\sum_{v\in A}X^{\operatorname{rank}_k R_v/t}Y^{\operatorname{rank}_k L_v}
=(1+(q^t-1)Y)^{p^h-p^{h-d}}
\left[1+Y\left(q^{t-j}(1+(q-1)X)^j-1\right)\right]^{p^{h-d}}.}
\]
The formula is valid for every such prime, dimension, automorphism and coefficient field, including \(I-\varphi=0\) and \(I-\varphi\) invertible. The marginal rank laws are
\[
\mathcal J_{\varphi,q}(X,1)=q^{p^m-p^h}(1+(q-1)X)^{p^h},\qquad
\mathcal J_{\varphi,q}(1,Y)=(1+(q^t-1)Y)^{p^h}.
\]
Thus the separate left- and right-multiplication rank distributions depend only on \(m,h,q\), whereas the joint distribution detects \(d\). In fact
\[
[X^1Y^1]\mathcal J_{\varphi,q}=p^h(q-1)q^{t-p^d}.
\]
The integer \(d\) is exactly the dimension of \(\ker(I-\varphi)\cap\operatorname{im}(I-\varphi)\), equivalently the number of nontrivial Jordan blocks at eigenvalue one (Jordan blocks of length at least two, over a splitting field).

For a concrete distinction, take \(p=2\), \(m=3\), \(q=3\). Let \(\varphi_U\) send the coordinate basis \((u_1,u_2,u_3)\) to \((u_1,u_1+u_2,u_2+u_3)\), and let \(\varphi_S\) send it to \((u_1,u_3,u_2+u_3)\). Both have \(h=2,t=2\), but \(d_U=1\), \(d_S=0\). Their separate rank distributions coincide, while
\[
\mathcal J_{\varphi_U,3}=(1+8Y)^2(1+Y(4X+4X^2))^2,\qquad
\mathcal J_{\varphi_S,3}=(1+Y(2+6X))^4.
\]
In particular their \(X^1Y^1\) coefficients are respectively \(8\) and \(24\). This separates two different interactions between annihilator dimensions that cannot be separated by either one-sided rank census.

## Assumptions and scope

The coefficient field must contain every \(p\)-th root of unity and have characteristic different from \(p\); writing it as \(\mathbb F_q\), the condition \(p\mid(q-1)\) is necessary and sufficient. No restriction on the Jordan form or fixed-point space of \(\varphi\) is imposed. All ranks in the exponents are ranks of \(k\)-linear operators on the \(p^m\)-dimensional algebra. The symbol \(\mathcal J\) is a polynomial over the ordinary integers whose coefficients count algebra elements, not a polynomial identity inside the generally nonassociative algebra.

## Proof

**1. Fourier diagonalization of the bilinear product.** The character group \(T=\widehat G=\operatorname{Hom}(G,k^\times)\) is an \(m\)-dimensional \(\mathbb F_p\)-space. For \(u=\sum_{g\in G}u_ge_g\), put \(\widehat u(\chi)=\sum_gu_g\chi(g)\). The character table is invertible because the field contains primitive \(p\)-th roots and \(p\) is nonzero in \(k\). Fourier coordinates therefore identify \(A\) linearly with all \(k\)-valued functions on \(T\).

Write \(S\colon T\to T\) for the dual automorphism \(\chi\mapsto\chi\circ\varphi\) and \(B=I-S\). The basis multiplication gives, by direct separation of the two sums,
\[
\widehat{uv}(\chi)=\widehat u(S\chi)\widehat v(B\chi).
\]
As \(S\) is invertible and commutes with \(B\), the dimensions \(\operatorname{rank}B=h\) and \(\dim(\ker B\cap\operatorname{im}B)=d\) agree with the corresponding dimensions for \(I-\varphi\). Indeed, transpose preserves ranks of every power, and \(\dim(\ker B\cap\operatorname{im}B)=\operatorname{rank}B-\operatorname{rank}B^2\).

**2. Right rank.** Fix \(v\). The operator \(u\mapsto uv\) is a permutation of Fourier input coordinates followed by a diagonal map with diagonal \(\widehat v(B\chi)\). Put \(H=\operatorname{im}B\), \(K=\ker B\). Each element of \(H\) has \(t=|K|=p^{m-h}\) preimages, so
\[
\operatorname{rank}R_v=t\,\#\{\eta\in H:\widehat v(\eta)\neq0\}.
\]
This proves divisibility and identifies the exponent of \(X\).

**3. Left rank.** The Fourier matrix for \(w\mapsto vw\) has column \(\eta\in H\) supported only in the fiber \(B^{-1}\{\eta\}\), with entries \(\widehat v(S\chi)\). Distinct columns have disjoint supports, so the rank counts nonzero columns. Because \(SB=BS\), the sets \(S(B^{-1}\{\eta\})\) as \(\eta\) ranges through \(H\) are exactly the distinct cosets of \(K\). Therefore
\[
\operatorname{rank}L_v=\#\{\text{cosets }C\in T/K:\widehat v|_C\not\equiv0\}.
\]
There are \(p^h\) such cosets, each containing \(t\) characters.

**4. Counting simultaneous supports.** The subspace \(H\) meets exactly \(|H|/|H\cap K|=p^{h-d}\) cosets of \(K\), with \(j=|H\cap K|=p^d\) points of \(H\) in each. The remaining \(p^h-p^{h-d}\) cosets do not meet \(H\). Each Fourier coordinate is an independent element of \(k\), so a coset missing \(H\) contributes \(1+(q^t-1)Y\): the all-zero assignment has weight one, and every nonzero assignment contributes one occupied coset. A coset meeting \(H\) has \(j\) coordinates counted by \(X\) and \(t-j\) others. Its unrestricted weighted sum is \(q^{t-j}(1+(q-1)X)^j\); subtracting the all-zero assignment and assigning weight \(Y\) to all other assignments gives \(1+Y(q^{t-j}(1+(q-1)X)^j-1)\). Multiplication over independent cosets proves the displayed polynomial.

**5. Marginals and identification of \(d\).** Substituting \(Y=1\), respectively \(X=1\), simplifies both factors to the stated marginals. To have exponent \(X^1Y^1\), choose one of the \(p^h\) points of \(H\) as the single nonzero observed coordinate, assign it any of \(q-1\) nonzero values, allow arbitrary values in the other \(t-j\) coordinates of its coset, and set all other cosets to zero. This yields \(p^h(q-1)q^{t-j}\), which determines \(j=p^d\) when \(m,h,p,q\) are known. The example follows by computing ranks of the two displayed binary linear maps and substituting \(p=2,m=3,q=3\). All steps include the boundary cases \(h=0\) and \(h=m\).

## Verification

The standalone Python 3 script `check_joint_ranks.py` computes multiplication directly from the basis rule, constructs both full \(p^m\)-square multiplication matrices for every algebra element in eight explicit binary examples over \(\mathbb F_3\), and performs independent modular Gaussian elimination. It does **not** use Fourier coordinates to obtain the observed ranks. For each case it compares the entire resulting two-variable frequency dictionary with the theorem's exact binomial-factor polynomial. The recorded output `check_joint_ranks.out` reports 33,048 algebra elements and 66,096 exact operator-rank calculations, all agreeing, including two automorphisms with the same \(h\) and different \(d\). Run `python3 check_joint_ranks.py` from the artifact directory. This finite verification is not a proof of the unrestricted theorem.

## Relationship to prior work

Zhang (2026), arXiv:2610.08204v1, transports Alexander-quandle multiplication to a group ring and proves general augmentation-ideal formulas, with a Fourier treatment of idempotents and right Peirce spectra. The group-ring product factorization is a previously available tool; the new object here is an **exact two-sided rank-joint distribution over all algebra elements**, whose dependence on \(\operatorname{rank}(I-\varphi)^2\) is not captured by either marginal. Ta (2026), arXiv:2610.20306v1, studies zero divisors and augmentation questions for medial quandle rings; Churchill–Churchill–Fernando–Kousik (2026), arXiv:2608.09149v1, studies zero-divisor graphs, particularly small extended quandle rings. Neither reviewed source asserts the present all-element joint rank formula. The nearest accessible related research findings involve right Peirce spectra of **idempotents** or defining-characteristic derivations, not arbitrary-element simultaneous multiplication ranks. Prior work on Fourier diagonalization is acknowledged rather than claimed as new.

## Limitations

No claim is made for coefficient characteristic \(p\), for fields lacking \(p\)-th roots of unity, or for non-elementary underlying abelian groups. Marginal rank laws alone cannot distinguish \(d\); the joint enumerator can. The source comparison included detailed available HTML passages and article-level summaries, but intermittent HTML access failures prevented exhaustive re-reading of every section of some plausible sources. This is a historical-priority residual risk, not a mathematical assumption. The correctness of the theorem is proved here; independent validation has not been performed.

## References

- Zhi-Lin Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1 (first posted 2026-10-06), https://arxiv.org/abs/2610.08204 .
- Lực Ta, *The zero divisor and augmentation conjectures for medial quandle rings*, arXiv:2610.20306v1 (first posted 2026-10-14), https://arxiv.org/abs/2610.20306 .
- G. Churchill, I. R. Churchill, N. Fernando, B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149v1 (first posted 2026-08-10), https://arxiv.org/abs/2608.09149 .
- V. G. Bardakov, I. B. S. Passi, M. Singh, *Zero-divisors and idempotents in quandle rings*, Osaka Journal of Mathematics 59 (2022), 611–637; arXiv:2001.06843, https://arxiv.org/abs/2001.06843 .
