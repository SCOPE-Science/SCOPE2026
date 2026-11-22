# An unbounded indecomposable family of locally rigid Zinbiel algebras

## Finding

**Theorem.** Over every field \(K\) of characteristic zero and for each integer \(k\ge1\), there exists a \((4k+1)\)-dimensional indecomposable Zinbiel algebra \(A_k\) with nonzero multiplication and
\[
\operatorname{LocDer}(A_k)=\operatorname{Der}(A_k)
\cong\operatorname{Hom}_K(A_k/A_k^2,\operatorname{Ann}(A_k)),
\qquad \dim_K\operatorname{Der}(A_k)=2k(k+1).
\]
Here \(\operatorname{LocDer}\) denotes *linear* local derivations. In particular, indecomposable locally rigid Zinbiel algebras exist in unbounded dimensions, resolving the existence question explicitly raised in the concluding remarks of [1].

## Assumptions and scope

Fix \(k\ge1\) and a field \(K\) with \(\operatorname{char}K=0\). On the vector space with basis
\[
w,\quad u_i,v_i,t_i,s_i\quad(1\le i\le k)
\]
define a bilinear multiplication whose only nonzero products of basis vectors are, for each \(i\),
\[
u_i u_i=w,\quad v_i v_i=w,\quad u_i v_i=t_i,\quad v_i u_i=-t_i,
\quad u_i t_i=s_i,\quad v_i t_i=w.
\]
Products mixing distinct indices and all unspecified products vanish. Write \(A_k\) for this algebra. A *Zinbiel algebra* satisfies \((xy)z=x(yz+zy)\) for all elements. The two-sided annihilator is \(\operatorname{Ann}(A)=\{a:aA=Aa=0\}\). The power \(A^m\) is the span of all products of at least \(m\) factors with arbitrary bracketings. A derivation obeys \(D(xy)=D(x)y+xD(y)\); a linear local derivation \(L\) has, at each input \(x\), some derivation \(D_x\) with \(L(x)=D_x(x)\). Indecomposable means not isomorphic to a direct sum of two nonzero two-sided ideals.

## Proof

**1. Zinbiel identity and filtration.** Let \(W=\langle w,s_1,\ldots,s_k\rangle\) and \(T=\langle t_1,\ldots,t_k\rangle\). Directly from the multiplication table, \(A_k^2=T\oplus W\), \(A_k^3=W\), \(A_k^4=0\), and \(W\) annihilates on both sides. Every element of \(A_k^2\) annihilates on the left. Furthermore, every symmetrized product \(yz+zy\) belongs to \(W\): the \(t_i\)-terms from \(u_iv_i\) and \(v_iu_i\) cancel. Hence both \((xy)z\) and \(x(yz+zy)\) vanish for all \(x,y,z\), proving the Zinbiel identity. To see that \(\operatorname{Ann}(A_k)=W\), write \(x=\sum_i(a_i u_i+b_i v_i+c_i t_i+d_i s_i)+ew\). If \(x\) annihilates, then \(x u_i=a_iw-b_it_i=0\), giving \(a_i=b_i=0\), and \(u_ix=c_is_i=0\), giving \(c_i=0\).

**2. All derivations are central.** Derivations preserve both \(A_k^2\) and \(W=\operatorname{Ann}(A_k)\). For \(k=1\), \(A_1\) is exactly the five-dimensional algebra in [1, Proposition 4.4], whose direct coordinate derivation calculation gives
\[
\operatorname{Der}(A_1)=\operatorname{Hom}_K(A_1/A_1^2,W).
\]
For \(k\ge2\), let \(D\) be any derivation. Fix distinct \(i,j\). The identities \(u_it_j=v_it_j=0\), together with \(D(t_j)\in A_k^2\), first force the \(u_j,v_j\) components of both \(D(u_i)\) and \(D(v_i)\) to vanish. Indeed, write the \(u_j,v_j\) component of \(D(u_i)\) as \(a u_j+b v_j\), and the \(t_i\) coefficient of \(D(t_j)\) as \(c\). The equation
\[
0=D(u_it_j)=D(u_i)t_j+u_iD(t_j)=a s_j+bw+c s_i
\]
forces \(a=b=c=0\), by independence of \(s_i,s_j,w\). Then \(0=D(v_it_j)\) similarly kills both \(u_j,v_j\) components of \(D(v_i)\). As this holds for every \(j\ne i\), the only potentially non-annihilator components of \(D(u_i),D(v_i)\) are in the span of \(u_i,v_i\) and the \(t_j\).

Next, \(0=D(u_j u_i)\) forces the \(t_j\) coefficient of \(D(u_i)\) to be zero, since \(D(u_j)u_i=0\), while \(u_jD(u_i)\) equals that coefficient times \(s_j\). Likewise, \(0=D(u_jv_i)\) eliminates the \(t_j\) coefficient of \(D(v_i)\). Therefore
\[
D(u_i),D(v_i)\in\langle u_i,v_i,t_i\rangle+W,
\quad D(t_i)\in Kt_i+W.
\]
The latter containment follows either from the preservation of \(A_k^2\) and the previous cross-index equation or from \(t_i=u_iv_i\). The identity \(w=u_i^2\) yields \(D(w)\in Kw+Ks_i\); because \(k\ge2\), intersecting these spaces over distinct indices gives \(D(w)\in Kw\). The relation \(s_i=u_it_i\) gives \(D(s_i)\in Kw+Ks_i\). Hence \(D\) maps the five-dimensional subalgebra \(B_i=\langle u_i,v_i,t_i,s_i,w\rangle\) into \(B_i+W\), with its off-\(B_i\) components lying in the annihilator. Projecting \(D|_{B_i}\) onto \(B_i\) (discarding off-branch annihilator coordinates) therefore preserves the derivation identity on \(B_i\). The multiplication table of \(B_i\) is exactly that of the five-dimensional base in [1, Proposition 4.4]. Its derivation computation forces the \(u_i,v_i,t_i\) coordinates of \(D(u_i),D(v_i)\) to be zero and forces \(D(t_i)=D(s_i)=D(w)=0\). Since this holds for every \(i\), every derivation maps \(A_k\) into \(W\) and annihilates \(A_k^2\).

Conversely, every linear map \(A_k/A_k^2\to W\) lifts to a derivation: its value on each product is zero and its images annihilate all elements. Because \(\dim(A_k/A_k^2)=2k\) and \(\dim W=k+1\), the derivation dimension is \(2k(k+1)\).

**3. Local rigidity.** Let \(L\) be a linear local derivation. Each \(D_x\) annihilates \(A_k^2\) and takes values in \(W\), so \(L(A_k^2)=0\) and \(L(A_k)\subseteq W\). Therefore \(L(xy)=0=L(x)y+xL(y)\). Thus \(L\) is a derivation.

**4. Indecomposability.** Every two-sided ideal \(I\) not contained in \(W\) contains \(w\). Indeed, choose \(x\in I\setminus W\). If a coefficient \(a_i\) of some \(u_i\) is nonzero, then \(v_i(xv_i)=a_i w\in I\). If all \(a_i=0\) but some \(b_i\) of \(v_i\) is nonzero, then \(v_i(xu_i)=-b_iw\in I\). If all these coefficients vanish, some coefficient \(c_i\) of \(t_i\) is nonzero and \(v_ix=c_iw\in I\). Each coefficient is invertible when nonzero, so \(w\in I\).

Suppose \(A_k=I\oplus J\) for nonzero two-sided ideals. Then \(IJ=JI=0\). Both ideals cannot escape \(W\), because both would contain \(w\), contradicting their zero intersection. Assume \(J\subseteq W\). Because \(W\) annihilates, \(A_k^2=I^2\subseteq I\). But \(J\subseteq W\subseteq A_k^2\), forcing \(J=0\), a contradiction. This proves indecomposability, including after any characteristic-zero field extension.

## Verification

A standalone Python checker (`zinbiel_glue_checker.py`, standard library only) constructs each multiplication table, verifies the Zinbiel identity on all ordered basis triples, determines the square and annihilator, and computes the full derivation-constraint matrix rank by exact modular elimination. It reports `ZINBIEL_CENTRAL_AMALGAM_CHECKS_OK` for \(k=1,2,3\) and characteristics \(3,5,101\), with derivation dimensions respectively \(4,12,24\). This is a cross-check of the symbolic all-\(k\) proof, not an exhaustive proof over characteristic zero or arbitrary dimensions. The independent ideal argument above establishes indecomposability without computational extrapolation.

## Relationship to prior work

Abdireymov, Sattarov and Yusupov [1] construct the five-dimensional locally rigid base (their Proposition 4.4) and obtain examples in every dimension at least five by **direct sum with a zero-product space** (their Theorem 4.8). Their Section 7 explicitly observes that these larger examples are decomposable and asks whether indecomposable locally rigid algebras exist in arbitrarily large dimensions. The present construction instead *identifies a common annihilator direction* across arbitrarily many base copies, and the shared nonzero product \(w\) prevents any nontrivial ideal decomposition. The new all-rank derivation calculation verifies that this identification preserves local rigidity. The theorem is not a corollary of the direct-sum construction, which preserves a nontrivial zero-product summand.

## Limitations

The theorem establishes existence in dimensions \(4k+1\), not every possible dimension. It covers *linear* local derivations, not a classification of nonlinear two-local derivations. The argument is stated over characteristic-zero fields; finite-field checker runs in odd characteristic do not assert a theorem in every positive characteristic. Historical priority for the central-amalgam construction remains subject to specialist literature review. No independent mathematical validation is claimed.

## References

[1] A. Abdireymov, A. Sattarov and B. Yusupov, *Local and 2-Local Derivations of Finite-Dimensional Zinbiel Algebras*, arXiv:2611.07863v1, first posted 2026-11-05, https://arxiv.org/html/2611.07863v1 . Relevant material: Proposition 4.4, Theorem 4.8, Section 7.

[2] M. A. Alvarez, T. Castilho de Mello and I. Kaygorodov, *Central extensions of 3-dimensional Zinbiel algebras*, Ricerche Mat. 72 (2023), 921–947. Contextual classification of low-dimensional central extensions, cited in [1].
