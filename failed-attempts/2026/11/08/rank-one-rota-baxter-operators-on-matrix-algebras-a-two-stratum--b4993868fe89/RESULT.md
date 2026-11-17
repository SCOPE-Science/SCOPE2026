# Rank-one Rota–Baxter operators on matrix algebras: a two-stratum classification and exact finite-field census

## Finding

Let \(k\) be any field, and let \(A=M_n(k)\), \(n\geq1\). A weight-zero Rota–Baxter operator is a linear map \(R:A\to A\) satisfying
\[
R(X)R(Y)=R(R(X)Y+XR(Y))\qquad(X,Y\in A).
\]
Here rank one means \(\dim_k\operatorname{im}R=1\), **not** the rank of the matrices in its image. Every nonzero rank-one operator admits a factorization
\[
R_{B,C}(X)=\operatorname{tr}(CX)\,B,\qquad B,C\in M_n(k)\setminus\{0\}.
\]
The following gives a disjoint, complete classification with no restriction on characteristic.

**Type N (square-zero image).** \(B^2=0\) and
\[
BC=CB=0.
\]
For every nonzero square-zero \(B\), the allowed \(C\)'s form the nonzero vectors in a space of dimension \((n-r)^2\), where \(r=\operatorname{rank}B\).

**Type P (idempotent image line).** The image line contains a unique nonzero idempotent \(P\), which we use as \(B=P\). With \(r=\operatorname{rank}P\), necessarily \(1\le r<n\); relative to \(k^n=\operatorname{im}P\oplus\ker P\), the allowed \(C\)'s are exactly the nonzero matrices in one of the two *disjoint* off-diagonal spaces
\[
C=\begin{pmatrix}0&U\\0&0\end{pmatrix}
\quad\text{or}\quad
C=\begin{pmatrix}0&0\\V&0\end{pmatrix}.
\]
Each off-diagonal space has dimension \(r(n-r)\).

In both types, \(R^2=0\). There are no other nonzero rank-one weight-zero Rota–Baxter operators.

Over \(k=\mathbb F_q\), write
\[
\binom{m}{r}_q=\prod_{i=0}^{r-1}\frac{q^{m-i}-1}{q^{r-i}-1},
\qquad
g_r(q)=\prod_{i=0}^{r-1}(q^r-q^i),
\]
with the empty products equal to \(1\). The exact number **including the zero operator**, denoted \(T_n(q)\), is
\[
\boxed{
T_n(q)=1+
\sum_{r=1}^{\lfloor n/2\rfloor}
\frac{\binom{n}{r}_q\binom{n-r}{r}_qg_r(q)}{q-1}
\left(q^{(n-r)^2}-1\right)
+
2\sum_{r=1}^{n-1}
\binom{n}{r}_q q^{r(n-r)}
\left(q^{r(n-r)}-1\right).
}
\]
The first sum counts Type N by matrix rank \(r\); the second counts Type P by idempotent rank \(r\). For example,
\[
T_1(q)=1,\qquad T_2(q)=2q^3+q^2-2q,
\]
and
\[
T_3(q)=1+(q^2+q+1)(q+1)(q^4-1)
+4(q^2+q+1)q^2(q^2-1).
\]
Thus \(T_2(2)=16\), \(T_2(3)=57\), \(T_3(2)=652\), and \(T_3(3)=7905\).

For fixed \(n\) and \(q\to\infty\) through prime powers there is a sharp change in the dominant geometric stratum:
\[
T_2(q)\sim 2q^3,\qquad
T_n(q)\sim q^{n^2-2}\quad(n\ge3).
\]
For \(n=2\), the leading contribution is Type P; for every \(n\ge3\), it is precisely the Type N subfamily whose image generator has matrix rank one.

## Assumptions and scope

The theorem concerns arbitrary fields for the classification, and finite fields of cardinality \(q\) for the exact census. No characteristic restrictions are imposed. Operators are counted as distinct linear functions on the labeled matrix algebra, not modulo conjugacy, transpose, or nonzero scalar rescaling. The zero operator is counted separately. The variable \(r\) always denotes the ordinary rank of the *image matrix* \(B\) or \(P\), while the operator \(R\) has linear rank one.

## Proof

1. **Reduce the identity to a quadratic image condition.** A nonzero rank-one linear operator has the displayed form by nondegeneracy of the trace pairing. Put \(f(X)=\operatorname{tr}(CX)\). Its Rota–Baxter identity is equivalent to
\[
f(X)f(Y)B^2=
\big(f(X)f(BY)+f(Y)f(XB)\big)B.
\]
Choose \(X,Y\) with \(f(X)=f(Y)=1\). Then \(B^2=\lambda B\) for a unique \(\lambda\in k\). The identity further implies that the linear forms \(Y\mapsto f(BY)\) and \(X\mapsto f(XB)\) vanish on \(\ker f\): choose the other variable in \(\ker f\) and the remaining variable with \(f=1\). Consequently there exist \(u,v\in k\) with
\[
f(BY)=u f(Y),\quad f(XB)=v f(X),\quad u+v=\lambda.
\]
Via the trace pairing, this is exactly
\[
CB=uC,\qquad BC=vC.
\]

2. **Classify the two types.** If \(\lambda=0\), both operators \(C\mapsto CB\) and \(C\mapsto BC\) square to zero, so their eigenvalues \(u,v\) must vanish because \(C\ne0\). Thus \(B^2=BC=CB=0\), Type N. Conversely these equations immediately give the Rota–Baxter identity.

If \(\lambda\ne0\), \(P=\lambda^{-1}B\) is the unique idempotent in the line \(kB\). Since \(u^2=\lambda u\) and \(v^2=\lambda v\), and \(u+v=\lambda\), the pairs are exactly \((u,v)=(\lambda,0)\) and \((0,\lambda)\), in every characteristic. Rewriting using \(P\) gives, respectively, \((CP,PC)=(C,0)\) or \((CP,PC)=(0,C)\). These are precisely the two off-diagonal spaces. They intersect only at zero, and neither exists when \(P=I\). Conversely either condition gives the identity. Also \(f(B)=\operatorname{tr}(CB)=0\) in Type N; in Type P, \(f(P)=\operatorname{tr}(CP)=0\) since \(C\) is off diagonal. Hence \(R^2=0\).

3. **Count Type N without overcounting.** Fix a nonzero square-zero \(B\) of ordinary rank \(r\). Its image \(U\) is an \(r\)-space contained in its kernel \(K\), an \((n-r)\)-space. Choose \(U\) in \(\binom{n}{r}_q\) ways and \(K\supseteq U\) in \(\binom{n-r}{r}_q\) ways. The induced map \(k^n/K\to U\) is an isomorphism, chosen in \(g_r(q)\) ways. Thus
\[
\#\{B:B^2=0,\operatorname{rank}B=r\}
=\binom{n}{r}_q\binom{n-r}{r}_q g_r(q).
\]
For a fixed \(B\), \(BC=CB=0\) says exactly that \(C\) factors through \(k^n/\operatorname{im}B\) and takes values in \(\ker B\). This linear space has dimension \((n-r)^2\), with \(q^{(n-r)^2}-1\) nonzero choices. Replacing \((B,C)\) by \((tB,t^{-1}C)\) for \(t\ne0\) does not change the operator. These are exactly the \(q-1\) representations for each Type N operator once its image line is fixed, producing the first sum.

4. **Count Type P without overcounting.** Each idempotent \(P\) of rank \(r\) is determined by its image \(U\) and a complementary kernel \(W\). There are \(\binom{n}{r}_q\) choices for \(U\) and \(q^{r(n-r)}\) complements, so \(\binom{n}{r}_q q^{r(n-r)}\) idempotents. Each gives two disjoint sets of nonzero \(C\)'s, each of cardinality \(q^{r(n-r)}-1\). Distinct \(C\)'s give distinct operators for normalized \(P\), and two distinct idempotents never lie on the same nonzero scalar line. This yields the second sum.

5. **Leading powers.** For fixed \(n,r\), the leading \(q\)-degree of the Type N term is \(n^2-r^2-1\). Thus among Type N ranks, \(r=1\) uniquely has largest degree \(n^2-2\) and leading coefficient \(1\). The Type P term of rank \(r\) has degree \(3r(n-r)\), at most \(3\lfloor n^2/4\rfloor\). For \(n\ge3\), this is strictly less than \(n^2-2\). For \(n=2\), the Type P term leads with degree \(3\) and coefficient \(2\). This proves both asymptotic statements.

## Verification

The attached standalone `verify.py` evaluates the Rota–Baxter identity directly on all pairs of matrix units, independently of the classification criterion. It exhaustively checks every nonzero pair \((B,C)\) over \(M_2(\mathbb F_2)\) and \(M_2(\mathbb F_3)\), comparing the direct identity with the classification equations. It also enumerates all nonzero pairs over \(M_3(\mathbb F_2)\), directly replaying the identity for all classified pairs and a deterministic sample of nonclassified pairs. The computed numbers of operators (including zero) are \(16,57,652\), respectively; all match the formula. Additional integer formula and boundary tests cover \(1\le n\le7\) and \(q\in\{2,3,4,5,7\}\). The script prints `VERIFY_OK_RB_RANK_ONE`. The universal result follows from the proof above, not from these finite experiments.

## Relationship to prior work

Benito–Gubarev–Pozhidaev (2018, §5.1) and Gubarev (2018, Theorem 5.18) already classify the weight-zero operators on \(M_2\) up to conjugacy, transpose, and scalar rescaling over algebraically closed fields. Their rank-one \(2\times2\) cases are **not claimed as new**. The first novel target here is the characteristic-unrestricted, rank-one classification for every matrix size \(n\ge3\), with an exact finite-field count and a change in the dominant type at \(n=3\). Gubarev's general matrix-algebra results analyze Yang–Baxter correspondence, constructions, and nilpotency indices; they do not state the two-stratum finite-field census above. Zhang–Gao–Zheng (2018, Theorem 4.12) establish a bijection between associative Yang–Baxter solutions and Rota–Baxter operators on matrix algebras. This transports the question but does not by itself enumerate rank-one solutions. No definitive priority claim is made: an unidentified broader classification may imply this formula.

## Limitations

The theorem counts only rank-one *linear operators* satisfying the weight-zero equation, not higher-rank Rota–Baxter operators or operators of nonzero weight. It does not count conjugacy orbits or automorphism types. Its asymptotic is for fixed matrix size as the field size tends to infinity. Originality is assessed relative to inspected primary literature and mathematical-record searches, not established by a proof of global literature completeness. Independent audit is not yet performed.

## References

1. P. Benito, V. Gubarev, A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, arXiv:1801.07037, first posted 2018-01-22, particularly §5.1.
2. V. Gubarev, *Rota–Baxter operators on unital algebras*, arXiv:1805.00723, first posted 2018-05-02, particularly §5.4 and Theorem 5.18.
3. Y. Zhang, X. Gao, J.-w. Zheng, *Weighted infinitesimal unitary bialgebras on matrix algebras and weighted associative Yang–Baxter equations*, arXiv:1811.00842, first posted 2018-11-02, particularly Theorem 4.12.
