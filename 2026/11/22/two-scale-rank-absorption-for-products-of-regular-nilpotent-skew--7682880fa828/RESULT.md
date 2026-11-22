# Two-scale rank absorption for products of regular nilpotent skew matrices over finite fields

## Finding

Let \(q\) be an odd prime power. Define \(\mathcal N=\{S(v):v\in\mathbb F_q^3\setminus\{0\},\,v\cdot v=0\}\), where
\[
S(v)=\begin{pmatrix}0&-v_3&v_2\\v_3&0&-v_1\\-v_2&v_1&0\end{pmatrix}.
\]
Each factor has rank two and Jordan partition \((3)\), and \(|\mathcal N|=q^2-1\). For independent uniform factors \(S(v_1),\ldots,S(v_k)\), form \(P_k=S(v_1)\cdots S(v_k)\). Classify a nonzero product as \(D\) if its rank is two, \(I\) if its rank is one and a nonzero row has zero norm, and \(R\) if its rank is one and a nonzero row has norm equal to a negative nonzero square; set \(Z\) for a zero product. These four states are exhaustive on the product support, and are independent of the choice of nonzero row.

**Theorem.** The state process is a time-homogeneous Markov chain with initial state \(D\) and transition matrix, in state order \(D,I,R,Z\),
\[
T_q=\begin{pmatrix}
\frac q{q+1}&\frac1{q+1}&0&0\\
0&0&\frac q{q+1}&\frac1{q+1}\\
0&\frac2{q+1}&\frac{q-1}{q+1}&0\\
0&0&0&1
\end{pmatrix}.
\]
The exact probabilities at every positive integer length \(k\) are the four entries of \(e_D T_q^{k-1}\); in particular,
\[
\Pr(\operatorname{rank}P_k=2)=\left(\frac q{q+1}\right)^{k-1}.
\]
If \(d_k,i_k,r_k,z_k\) are the numbers of ordered factor words in the four states, start with \((d_1,i_1,r_1,z_1)=(q^2-1,0,0,0)\) and use
\[
\begin{aligned}
d_{k+1}&=q(q-1)d_k,\\
i_{k+1}&=(q-1)(d_k+2r_k),\\
r_{k+1}&=(q-1)(q i_k+(q-1)r_k),\\
z_{k+1}&=(q-1)i_k+(q^2-1)z_k.
\end{aligned}
\]
For \(h=(q+1)^{-1}\) and \(a=qh\), the exact generating function of the rank-one probability is
\[
\sum_{n\ge0}\Pr(\operatorname{rank}P_{n+1}=1)z^n
=\frac{hz(1+hz)}{(1-az)(1-(q-1)hz-2qh^2z^2)}.
\]
If \(K=\min\{k\ge1:P_k=0\}\), then \(K\) is almost surely finite and
\[
\mathbb E K=1+\frac{(q+1)(q+4)}2.
\]
In the limit over odd prime powers \(q\to\infty\), for fixed \(t>0\) and \(k=\lfloor tq\rfloor\), the distribution of \(\operatorname{rank}P_k\) on \((2,1,0)\) tends to \((e^{-t},1-e^{-t},0)\). For fixed \(s>0\) and \(k=\lfloor sq^2\rfloor\), it tends to \((0,e^{-2s},1-e^{-2s})\).

## Assumptions and scope

All fields have odd characteristic; the standard dot product and cross product on \(\mathbb F_q^3\) use the displayed matrix and fixed coordinate basis. There is no need to choose a square root of \(-1\). The factor distribution is uniform on **nonzero isotropic** cross-product matrices, not on all alternating matrices and not on all rank-two matrices. Multiplication is ordinary associative matrix multiplication, with factors appended on the **right**. The two row-norm classes are well-defined since multiplying a nonzero row by a scalar multiplies its squared norm by a square. The theorem counts ordered words, not similarity classes of their products or prescribed-output fibers.

## Proof

**1. Nilpotent factor orbit and the conic.** The standard vector triple-product identity gives \(S(v)^2=vv^{\mathsf T}-(v\cdot v)I\). For an isotropic nonzero \(v\), this is \(vv^{\mathsf T}\ne0\), whereas \(S(v)^3=0\), and \(\ker S(v)=\langle v\rangle\), \(\operatorname{im}S(v)=v^\perp\). A nondegenerate ternary quadratic form over an odd finite field has a nonsingular projective conic with exactly \(q+1\) rational points. Each such line has \(q-1\) nonzero representatives, yielding \(q^2-1\) distinct matrices.

**2. Rank-two transition.** Suppose \(P_k\) has rank two. All factors and their partial products must have rank two (rank cannot rise), so its kernel is exactly the kernel \(\langle v_k\rangle\) of the last factor. For any new isotropic \(v\), the rank of \(P_kS(v)\) is one precisely when \(\operatorname{im}S(v)=v^\perp\) meets \(\ker P_k=\langle v_k\rangle\) nontrivially, equivalently \(v\cdot v_k=0\). Distinct rational points of a nonsingular ternary conic cannot be orthogonal: otherwise the span of their vectors would be a totally isotropic two-plane, impossible for Witt index one. Thus the rank falls only for \(\langle v\rangle=\langle v_k\rangle\), one of \(q+1\) possible lines. Write \(P_k=A S(v_k)\) for its prefix \(A\); then \(P_kS(v)=c A vv^{\mathsf T}\) for a nonzero scalar \(c\), so the nonzero row is proportional to the isotropic vector \(v\). This proves the first transition row.

**3. Rank-one transitions.** Write \(P_k=u w^{\mathsf T}\), with \(u,w\ne0\). Since \(w^{\mathsf T}S(v)\) is the cross product of \(w,v\) up to sign, it vanishes precisely when \(v\parallel w\). A rank-one product with isotropic row \(w\) therefore vanishes at the unique corresponding conic line. For all other isotropic lines, the identity
\[
(w\times v)\cdot(w\times v)=(w\cdot w)(v\cdot v)-(w\cdot v)^2=-(w\cdot v)^2
\]
shows the new row is nonisotropic of negative-square norm: because distinct conic points are not perpendicular, \(w\cdot v\ne0\). Hence \(I\to Z\) for one line and \(I\to R\) for the other \(q\) lines. For \(R\), \(w\cdot w\) is a negative square. The binary quadratic space \(w^\perp\) is then hyperbolic, so it contains exactly two isotropic projective lines. These two choices make \(w\times v\) nonzero isotropic; the remaining \(q-1\) conic lines keep the row in \(R\). Neither can produce zero, since \(w\) itself is anisotropic. This is the complete claimed transition matrix. All choices of nonzero representatives of each conic line have equal size, so the transition probabilities are exact.

**4. Enumeration, generating function, and absorption.** Multiplying the stochastic matrix by \(q^2-1=(q-1)(q+1)\) proves the integer recurrence and the formula for rank two. Restricting the transient transition block to \(I,R\) gives \(\begin{psmallmatrix}0&qh\\2h&(q-1)h\end{psmallmatrix}\), which has characteristic polynomial \(\lambda^2-(q-1)h\lambda-2qh^2\). Standard resolvent inversion with entrance probability \(h\) from \(D\) yields the displayed generating function. For the expected remaining number of appended factors from state \(I\), let \(E_I,E_R\) satisfy
\[
E_I=1+qh E_R,\qquad E_R=1+2h E_I+(q-1)h E_R.
\]
Solving gives \(E_I=(q+2)(q+1)/2\); the waiting time in \(D\) has mean \(q+1\). Therefore \(\mathbb E(K-1)=q+1+E_I=(q+1)(q+4)/2\). Absorption is almost sure because every transient state has a positive-probability path to \(Z\).

**5. Two timescales.** The transient \(I,R\) eigenvalues are
\[
\lambda_{\pm}=\frac{q-1\pm\sqrt{q^2+6q+1}}{2(q+1)};
\qquad \lambda_+=1-2q^{-2}+O(q^{-3}),\quad\lambda_-=O(q^{-1}).
\]
At \(k=\lfloor tq\rfloor\) the probability remaining in \(D\) tends to \(e^{-t}\), while the probability of absorption tends to zero: the expected number of visits to \(I\) up to time \(O(q)\) is \(O(1)\), and every visit has absorption probability \(h\). At \(k=\lfloor sq^2\rfloor\), the contribution from \(D\) and the subdominant eigenvalue is negligible; the leading eigenprojection has total rank-one mass tending to one, and \(\lambda_+^k\to e^{-2s}\). The zero mass is the complement. This proves the limits.

## Verification

The accompanying `nilpotent_checker.py` independently constructs each matrix and each product, computes matrix rank by Gaussian elimination, independently computes the norm of a nonzero row of every rank-one product, and compares the four category counts to the recurrence. Exhaustive enumerations were performed over prime fields of sizes \(3,5,7\) and the quadratic extension field of size \(9\): through word length \(5,4,3,2\), respectively. The output `nilpotent_checker_output.txt` records every checked count. Finite experiments cannot establish the infinite all-fields/all-length claim; that is established by the preceding geometric proof. The expected-time identity and probability-generating function were separately checked by symbolic matrix algebra.

## Relationship to prior work

Gow and Laffey (1984) classify matrices expressible as products of **two arbitrary** skew-symmetric factors through elementary divisors and alternating-form theory. That factorization *support* theorem neither restricts factors to the nonzero nilpotent conic nor supplies the all-length counting/probability transition. Fulman and Goldstein (original public preprint November 2, 2012) derive rank distributions for individually sampled finite-field alternating/skew matrices, not products conditioned to lie on the regular nilpotent conic. Existing finite-field matrix-product rank results under **uniform projective kernel lines** do not imply this theorem: here the kernel is uniform only on the \(q+1\) points of a conic, rather than on all \(q^2+q+1\) projective lines, and the isotropic/anisotropic rank-one distinction is essential. Results on rank-one square-zero nilpotent factor products also concern a different orbit and cannot yield these rank-two factor transitions.

## Limitations

The result is confined to three-dimensional standard orthogonal space in odd characteristic, to independent uniform nonzero regular nilpotent factors, and to rank and row-norm state counts; it does not claim individual output-matrix fiber counts, arbitrary factor distributions, arbitrary dimensions, or characteristic two. The literature comparison does not prove historical uniqueness; an equivalent earlier unindexed computation could exist. An earlier factorization article has a verified publication year 1984 but no verified exact first-public calendar date; the recorded dated archival anchor is the 2012-11-02 source, not a claim that the 1984 work postdates it.

## References

1. R. Gow and T. J. Laffey, *Pairs of alternating forms and products of two skew-symmetric matrices*, Linear Algebra and its Applications **63** (1984), 119–132. DOI: https://doi.org/10.1016/0024-3795(84)90139-3 . Section 2, Theorems 5–6 and Lemma 8 (general two-factor support).
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504, first posted 2012-11-02, https://arxiv.org/abs/1211.0504 . Journal version: Annals of Probability **43** (2015), 1274–1314, DOI: https://doi.org/10.1214/13-AOP889 . Section 5 (single alternating-matrix rank distribution).
