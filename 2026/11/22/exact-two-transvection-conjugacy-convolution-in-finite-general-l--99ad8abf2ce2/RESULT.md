# Exact two-transvection conjugacy convolution in finite general linear groups

## Finding
Let \(q\) be any prime power, \(n\ge2\), and \(G=\mathrm{GL}_n(\mathbb F_q)\). Write \(\mathcal T\) for the conjugacy class of nonidentity transvections. Its order is
\[
T=|\mathcal T|=\frac{(q^n-1)(q^{n-1}-1)}{q-1}.
\]
For independent uniform \(A,B\in\mathcal T\), the probabilities that \(AB\) lies in the indicated \(G\)-similarity class are the following numerators \(N\) divided by \(T\):

| Similarity class of \(AB\) | Numerator \(N\) | Domain |
|---|---|---|
| \(I_n\) | \(1\) | All \(n\ge2\) |
| \(J_2(1)\oplus I_{n-2}\) | \(2q^{n-1}-q-2\) | All \(n\ge2\) |
| \(J_3(1)\oplus I_{n-3}\) | \(2(q^{n-1}-q)q^{n-2}\) | \(n\ge3\) |
| \(J_2(1)\oplus J_2(1)\oplus I_{n-4}\) | \(\dfrac{(q^{n-1}-q)(q^{n-2}-q)}{q-1}\) | \(n\ge4\) |
| \(I_{n-2}\oplus C(h_t)\) for each \(t\in\mathbb F_q^\times\) | \(q^{2n-3}\) | All \(n\ge2\) |

Here \(h_t(X)=X^2-(2+t)X+1\), and \(C(h_t)\) is its companion matrix. The second row is empty only if \(q=n=2\). The third and fourth rows are absent below their stated dimension bounds. All listed positive-numerator rows are distinct similarity classes, including in characteristic two. Every other similarity class has probability zero.

Consequently \(\mathcal T^2\) contains exactly \(q+3\) conjugacy classes for \(n\ge4\), exactly \(q+2\) for \(n=3\), and exactly \(q+1\) for \(n=2,q>2\); for \(q=n=2\) it contains two classes. All nonzero trace-shift parameters \(t\) are **equally likely**, irrespective of whether \(h_t\) splits over the field.

The table also determines the exact factorization multiplicity of **every prescribed** \(g\in G\). If \(g\) lies in a class \(\mathcal C\) with numerator \(N_{\mathcal C}\), then
\[
\#\{(A,B)\in\mathcal T^2:AB=g\}=\frac{T N_{\mathcal C}}{|\mathcal C|};
\]
otherwise it is zero. Class sizes may be evaluated without further enumeration by \(|\mathcal C|=|G|/|C_G(g)|\). For a unipotent Jordan partition \(\lambda\) of \(n\), the familiar centralizer expression is
\[
|C_G(g)|=q^{\sum_j (\lambda'_j)^2}\prod_{r\ge1}\prod_{i=1}^{m_r(\lambda)}(1-q^{-i}),
\]
where \(\lambda'\) is the conjugate partition and \(m_r(\lambda)\) counts its parts equal to \(r\). For nonzero \(t\), the centralizer is \(|\mathrm{GL}_{n-2}(q)|c_t\) (with \(|\mathrm{GL}_0(q)|=1\)), where \(c_t=q^2-1\) if \(h_t\) is irreducible, \(c_t=(q-1)^2\) for distinct rational roots, and \(c_t=q(q-1)\) for a repeated root. Such a repeated-root case occurs only at \(t=-4\) in odd characteristic, and the block is nonsemisimple.

For fixed field size \(q\), as \(n\to\infty\), the masses of the identity and rank-one-unipotent classes vanish. The rank-two unipotent classes \(J_3\) and \(J_2\oplus J_2\) tend to \(2(q-1)/q^2\) and \(1/q^2\), while each of the \(q-1\) nonzero-\(t\) classes has limiting mass \((q-1)/q^2\). These limits sum to one.

## Assumptions and scope
All fields are finite, including nonprime extension fields and characteristic two; all dimensions \(n\ge2\) are included. A transvection is \(I+u\varphi\), where \(u\in\mathbb F_q^n\setminus\{0\}\) and \(\varphi\in(\mathbb F_q^n)^*\setminus\{0\}\) satisfy \(\varphi(u)=0\). Each transvection has precisely \(q-1\) such factorizations by scaling \(u\) and \(\varphi\) inversely. The two factors are independent and uniform among actual transvection matrices, not among chosen factorizations. Similarity means conjugacy under \(G\), not under its determinant-one subgroup; the number and sizes of conjugacy classes in the latter may differ.

## Proof
**Step 1 (fix the first factor).** All nonidentity transvections form one \(G\)-conjugacy class. Fix \(A=I+u\varphi\) with \(u=e_1\) and \(\varphi=e_2^*\). Write \(B=I+v\psi\), with both \(v\) and \(\psi\) nonzero and \(\psi(v)=0\), and set \(a=\varphi(v)\), \(b=\psi(u)\), and \(t=ab\). Direct multiplication gives
\[
K=AB-I=u\varphi+v\psi+a u\psi,
\quad
\operatorname{tr}(AB)=n+t,
\quad
\det(XI-AB)=(X-1)^{n-2}h_t(X).
\]
For the last identity, apply the matrix determinant lemma to the rank-two update, or restrict to the invariant span of \(u,v\). The number of possible \(B\) equals \(T\), since choosing \(v\) and nonzero \(\psi\) annihilating it gives \((q^n-1)(q^{n-1}-1)\) presentations, each counted \(q-1\) times.

**Step 2 (nonzero trace shift).** Fix \(t\ne0\). Then \(a,b\ne0\). There are \((q-1)q^{n-1}\) choices of \(v\) with \(\varphi(v)\ne0\). Once \(v\) is fixed, \(\psi(v)=0\) and \(\psi(u)=t/a\) are independent linear constraints, hence yield \(q^{n-2}\) choices. Dividing by the \(q-1\) presentations per transvection gives \(q^{2n-3}\) factors \(B\). Moreover \(\operatorname{rank}K=2\), \(h_t(1)=-t\ne0\), and on the invariant plane \(\langle u,v\rangle\), the product is cyclic. If its two eigenvalues coincide, its restriction cannot be scalar because the product of two nonidentity 2-dimensional transvections cannot be \(-I\) in odd characteristic: otherwise \(B|_{\langle u,v\rangle}=-A^{-1}|_{\langle u,v\rangle}\), whose eigenvalue is \(-1\) rather than \(1\). Thus the stated companion class, even at a repeated root, is unique.

**Step 3 (rank-one products).** The rank of \(K\) is at most one precisely if \(v\in\langle u\rangle\) or \(\psi\in\langle\varphi\rangle\), as follows from the two-term expression \(K=u(\varphi+a\psi)+v\psi\) and independence of the two vectors and two covectors otherwise. For fixed \(A\), there are \(q^{n-1}-1\) transvections of either kind and \(q-1\) in their overlap. Hence exactly \(2q^{n-1}-q-1\) choices yield rank zero or one. Exactly one is \(B=A^{-1}\), giving \(K=0\). All remaining \(2q^{n-1}-q-2\) satisfy \(K^2=0\) and have the \(J_2(1)\) similarity type. This count vanishes only at \((q,n)=(2,2)\).

**Step 4 (rank-two unipotent products).** Assume \(t=0\) and \(\operatorname{rank}K=2\). If \(a=0,b\ne0\), then \(v\in\ker\varphi\setminus\langle u\rangle\); there are \(q^{n-1}-q\) such vectors. The constraints \(\psi(v)=0\), \(\psi(u)\ne0\) admit \((q-1)q^{n-2}\) covectors. After dividing by \(q-1\), this gives \((q^{n-1}-q)q^{n-2}\) transvections. The opposite case \(a\ne0,b=0\) gives the same number. In each, \(K^2\ne0\), hence the unique possible unipotent type of rank two is \(J_3(1)\oplus I_{n-3}\). Finally, for \(a=b=0\) and rank two, choose \(v\in\ker\varphi\setminus\langle u\rangle\) and \(\psi\in\operatorname{Ann}\langle u,v\rangle\setminus\langle\varphi\rangle\), giving \((q^{n-1}-q)(q^{n-2}-q)/(q-1)\) factors. Here \(K^2=0\) and the type is \(J_2(1)\oplus J_2(1)\oplus I_{n-4}\). All cases are disjoint and exhaustive. Their numerators, together with the \(q-1\) nonzero trace shifts, sum to \(T\).

**Step 5 (individual target fibers and limiting masses).** The probability law is conjugation invariant, so within a class \(\mathcal C\) it is constant; the class contains \(|\mathcal C|\) matrices, and has probability \(N_{\mathcal C}/T\). Multiplying by \(T^2\), the total number of ordered pairs, yields \(T N_{\mathcal C}/|\mathcal C|\) factorizations for each matrix. The standard unipotent primary centralizer formula, and the centralizer of the cyclic 2-dimensional companion block, give the displayed explicit class-size computations. Divide the class numerators by \(T\sim q^{2n-1}/(q-1)\) to obtain the fixed-field limits.

## Verification
The accompanying standalone file `check_transvections.py` enumerates every nonzero vector and nonzero annihilating covector over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_9\) in fifteen dimension/field configurations. It implements finite-field operations explicitly, reconstructs each product's rank and squared nilpotent part, and checks each proposed row and each nonzero trace parameter. The captured output is `CHECK_OUTPUT.txt` and ends `ALL PASS 15 cases`. The second standalone file `check_target_fibers.py` independently enumerates **both** factors in five small configurations and checks that every individual resulting matrix has the same product-fiber size within its predicted similarity type; its captured output in `TARGET_CHECK_OUTPUT.txt` ends `ALL FULL-PAIR CHECKS PASS`. The first enumeration fixes one factor by conjugacy, and both checkers are exhaustive only in their enumerated finite instances; the preceding argument establishes all dimensions and fields.

## Relationship to prior work
Hildebrand (1992) investigates long random-transvection walks and mixing on the special linear group, giving the probabilistic setting but not this evaluated two-step conjugacy table. Adan-Bante and Harris (2009) prove a general lower bound of \(q-1\) conjugacy classes in products of two noncentral \(\mathrm{GL}_n(q)\) classes; the present precise first-conjugacy-class self-product count \(q+3\) (for \(n\ge4\)), and its full class-wise weights, are more specialized and stronger than that bound. Diaconis, Ram and Simper (2022) analyze the random-transvection walk projected onto Bruhat double cosets, whereas the present census concerns conjugacy (similarity) classes in the original matrix group. Standard rational canonical classifications and centralizer formulas are used, not claimed as new. Earlier structural two-transvection rank criteria also do not give this class-weight formula.

## Limitations
This is an exact **two-step** convolution law, not a theorem about arbitrary convolution powers or a new mixing cutoff. It treats \(\mathrm{GL}_n(q)\) conjugacy; it does not classify the possible splitting into \(\mathrm{SL}_n(q)\) conjugacy classes. The component ingredients are elementary and standard, and an unindexed prior evaluation of this precise distribution remains possible. The work has not received independent mathematical validation; finite checks alone do not prove the general result.

## References
1. M. Hildebrand, *Generating Random Elements in \(\mathrm{SL}_n(\mathbb F_q)\) by Random Transvections*, Journal of Algebraic Combinatorics 1 (1992), 133–150. https://doi.org/10.1023/A:1022472220105
2. E. Adan-Bante and J. M. Harris, *On Conjugacy Classes of \(\mathrm{GL}(n,q)\) and \(\mathrm{SL}(n,q)\)*, arXiv:0904.2152, first version 2009-04-14. https://arxiv.org/abs/0904.2152
3. P. Diaconis, A. Ram and M. Simper, *Double Coset Markov Chains*, arXiv:2208.10699, first version 2022-08-23. https://arxiv.org/abs/2208.10699
4. J. Fulman, *Random Matrix Theory over Finite Fields*, survey of classical conjugacy cycle indices. https://dornsife.usc.edu/jason-fulman/wp-content/uploads/sites/224/2023/06/cycle2.pdf
