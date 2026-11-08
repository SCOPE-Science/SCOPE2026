# Modular Jordan collapse for differentials of bounded nilpotent matrix powers

## Finding

Let \(k\) be **any field of positive characteristic** \(p\), let \(d\ge3\), and let \(N\in M_n(k)\) satisfy \(N^d=0\). Consider the linear differential of the power map at \(N\),
\[
\mathcal D_{N,d}(X)=\sum_{j=0}^{d-1}N^j XN^{d-1-j},\qquad X\in M_n(k).
\]
If the Jordan partition of \(N\) has \(m_a\) blocks of length \(a\), define \(h_i=\sum_{a\ge i}m_a\) for \(1\le i\le d\), and
\[
R=\sum_{i=1}^d h_i h_{d+1-i}=\sum_{a,b=1}^d m_a m_b\max(0,a+b-d),
\qquad S=\begin{cases}0,&p\mid d,\\m_d^2,&p\nmid d.\end{cases}
\]
Then \(\mathcal D_{N,d}\) has only Jordan blocks of sizes one, two, or three; their exact respective multiplicities are
\[
\boxed{\#J_1=n^2-2R+S,\quad\#J_2=R-2S,\quad\#J_3=S.}
\]
In particular, when \(p\mid d\), the differential is **square-zero** with exactly \(R\) two-blocks, whereas when \(p\nmid d\) it has \(m_d^2\) three-blocks. For \(m_d>0\), this is a sharp modular change in nilpotency index, not just an abstract rank bound.

## Assumptions and scope

The field may be infinite or finite, but has positive prime characteristic. The integer \(n\ge1\) is arbitrary, \(d\ge3\), and all Jordan blocks of \(N\) have length at most \(d\). Because \(N\) is nilpotent, the Jordan form exists over \(k\) without requiring that \(k\) be algebraically closed. No restriction on whether \(p\) divides \(d\) is imposed. The result describes the **linear differential** on the vector space \(M_n(k)\), not the Jordan type of \(N\) itself and not the nonlinear powers of arbitrary matrices.

For any finite field \(k=\mathbb F_q\), a consequence is that the number of first-order lifts \(N+\varepsilon B\) over \(k[\varepsilon]/(\varepsilon^2)\) with \((N+\varepsilon B)^d=0\) equals \(q^{n^2-R}\). This is a fixed-residue fiber count, not an assertion about the entire nilpotent cone or all jet schemes.

## Proof

**1. A nilpotency identity valid in every characteristic.** On \(M_n(k)\), define commuting endomorphisms \(L(X)=NX\) and \(T(X)=XN\). Both satisfy \(L^d=T^d=0\). Put
\[
h(s,t)=\sum_{j=0}^{d-1}s^jt^{d-1-j};\qquad\mathcal D_{N,d}=h(L,T).
\]
In the quotient ring \(k[s,t]/(s^d,t^d)\), expand \(h(s,t)^2\). Of its monomials, only \(s^{d-1}t^{d-1}\) can have both exponents smaller than \(d\); it occurs in exactly \(d\) ordered products. Consequently,
\[
h(s,t)^2=d\,s^{d-1}t^{d-1},\qquad h(s,t)^3=0.
\]
It follows without any division that
\[
\boxed{\mathcal D_{N,d}^{\,2}(X)=d\,N^{d-1}XN^{d-1},\qquad \mathcal D_{N,d}^{\,3}=0.}
\]
Thus \(\operatorname{rank}(\mathcal D_{N,d}^2)\) is zero when \(p\mid d\); otherwise it is \((\operatorname{rank}N^{d-1})^2=m_d^2=S\).

**2. Exact rank of the first differential.** Decompose \(N\) into its nilpotent Jordan blocks. The endomorphism space splits as a direct sum of rectangular matrix blocks of shape \(a\times b\), one for every ordered pair of Jordan blocks. On such a block, left and right multiplication are represented, after choosing the standard reversed-chain basis if necessary, by multiplication by \(s\) and \(t\) in
\[
A_{a,b}=k[s,t]/(s^a,t^b).
\]
The differential on this summand is multiplication by \(h(s,t)\). The polynomial identity
\[
(s-t)h(s,t)=s^d-t^d=0\qquad\text{in }A_{a,b}
\]
shows that every multiple of \(h\) equals a linear combination of the monomials \(s^rh\), for \(r\ge0\). Such a monomial is nonzero exactly when \(0\le r\le a+b-d-1\). Indeed, it contains the term \(s^{d-b+r}t^{b-1}\) whenever this range is nonempty (adjusting to a surviving term in the stated bounds); all of its terms have coefficient one and distinct monomial exponents. The surviving \(s^rh\) have different total degrees, hence are independent in \(A_{a,b}\). Therefore the rectangular summand contributes exactly
\[
\operatorname{rank}(h:A_{a,b}\to A_{a,b})=\max(0,a+b-d).
\]
Summing over all ordered pairs gives \(\operatorname{rank}\mathcal D_{N,d}=R\). The alternative expression in terms of the column lengths follows from
\[
\max(0,a+b-d)=\#\{i\in\{1,\ldots,d\}:i\le a,\ d+1-i\le b\}.
\]

**3. Jordan multiplicities.** A nilpotent linear map \(U\) with \(U^3=0\), with ranks \(r_1=\operatorname{rank}U\) and \(r_2=\operatorname{rank}U^2\), has \(r_2\) Jordan three-blocks, \(r_1-2r_2\) Jordan two-blocks and \(\dim U-2r_1+r_2\) Jordan one-blocks. Inserting \(r_1=R\), \(r_2=S\), and \(\dim M_n(k)=n^2\) proves the theorem.

**4. The finite-field lift corollary.** Modulo \(\varepsilon^2\), binomial expansion of a noncommuting matrix sum gives
\[
(N+\varepsilon B)^d=N^d+\varepsilon\,\mathcal D_{N,d}(B).
\]
The allowable \(B\)'s form \(\ker\mathcal D_{N,d}\), a vector space of dimension \(n^2-R\). Hence there are exactly \(q^{n^2-R}\) lifts.

## Verification

The included two independent Python programs use exact arithmetic in finite prime fields and no external dependencies. The first directly computes first-order dual-number products and compares counts with the rank formula (exhaustively for small matrix sizes); the second forms the full \(n^2\times n^2\) derivative matrix from matrix products and checks the ranks of its first, second and third powers. The latter verifies the predicted Jordan signature for all nilpotent \(3\times3\) matrices over \(\mathbb F_2\) and \(\mathbb F_3\), as well as further characteristic and dimension cases. The logs accompany the programs. Tests corroborate the proof; finite enumeration is not a proof for unbounded \(n\), \(d\), or fields.

For example, at \(d=3\) with a single length-three block, the Jordan block counts \((\#J_1,\#J_2,\#J_3)\) are \((4,1,1)\) in characteristic two and \((3,3,0)\) in characteristic three.

## Relationship to prior work

Kressner (2014), Section 5, identifies the Fréchet derivative of a matrix function through divided differences, providing the bivariate-operator framework. Moreau and Yu (first posted 24 November 2014) study complex jet schemes of nilpotent-orbit closures, including their first jets; their scope is a different geometric problem over \(\mathbb C\). Noferini (first posted 9 December 2025) establishes Jordan forms for Fréchet derivatives of matrix polynomials over algebraically closed fields of **characteristic zero**. His discussion explicitly identifies positive-characteristic extensions as a direction not addressed there. Thus no novelty is claimed for characteristic-zero Jordan-form theory. The present precise claim is the uniform **positive-characteristic**, characteristic-divisibility-sensitive Jordan type for derivatives of powers at matrices annihilated by that power. The possibility of an earlier encompassing modular theorem, especially in older tensor-polynomial literature, remains a historical-priority risk.

## Limitations

The formula applies to the differential of a single monomial power at a nilpotent input with \(N^d=0\), not arbitrary matrix polynomials, general bivariate matrix functions, or higher-order lift equations. It classifies the Jordan type, not the conjugacy orbit of the differential inside \(M_{n^2}(k)\). The finite-field lift count fixes the residue \(N\). No independent audit of the argument or exhaustive historical-priority verification has been performed.

## References

1. D. Kressner, *Bivariate matrix functions*, Operators and Matrices **8** (2014), 449–466, DOI:10.7153/oam-08-23, especially Section 5. https://files.ele-math.com/articles/oam-08-23.pdf
2. A. Moreau and R. W. T. Yu, *Jet schemes of the closure of nilpotent orbits*, arXiv:1411.6427 (first posted 2014-11-24), especially Sections 1–2 and 6. https://arxiv.org/abs/1411.6427
3. V. Noferini, *The Jordan canonical form of the Fréchet derivative of a matrix function and the bivariate Jordan problem*, arXiv:2512.08399 (first posted 2025-12-09), especially Sections 1, 4, and 5. https://arxiv.org/abs/2512.08399
4. C. W. Norman, *On the Jordan form of a family of linear mappings*, Linear Algebra and its Applications **257** (1997), 225–241. Historical priority not resolved from its full text.
