# Sharp negative type and endpoint Hilbert dimension of rank-three bilinear-form graphs

## Finding

Let \(q\ge2\) be any prime power and \(m\ge3\) an integer. On the additive group \(V=M_{m,3}(\mathbb F_q)\), equip pairs of matrices with the rank metric \(d(X,Y)=\operatorname{rank}(X-Y)\). Define \(Q=q^m\), \(a=q^2+q+1\), and
\[
\Phi_{q,m}(t)=(Q-a)+(qQ-q^3)3^t-\bigl((q+1)Q-qa\bigr)2^t.
\]
There is exactly one positive zero \(\beta_{q,m}\) of \(\Phi_{q,m}\), and \(0<\beta_{q,m}<1\). The metric has \(t\)-negative type **if and only if** \(0\le t\le\beta_{q,m}\); it has strict \(t\)-negative type for \(0\le t<\beta_{q,m}\). At the critical exponent, only the rank-two additive Fourier sector becomes null.

Write
\[
R_2(q,m)=\frac{(q^3-1)(q^3-q)(q^m-1)(q^m-q)}{(q^2-1)(q^2-q)}.
\]
For every \(0<t<\beta_{q,m}\), the smallest real Euclidean dimension realizing squared distances \(d(X,Y)^t\) is \(q^{3m}-1\). At \(t=\beta_{q,m}\) it is exactly
\[
q^{3m}-1-R_2(q,m).
\]
The threshold also has two sharp asymptotic laws:
\[
\lim_{m\to\infty}q^m\beta_{q,m}=\frac{1}{q\log3-(q+1)\log2}\quad(q\text{ fixed}),
\]
\[
\lim_{q\to\infty}q^{m+1}\beta_{q,m}=\frac{1}{\log(3/2)}\quad(m\ge3\text{ fixed; prime powers }q).
\]

## Assumptions and scope

The field may have arbitrary prime-power order, including characteristic two. The integer \(m\) is at least three, so all ranks \(0,1,2,3\) occur. The underlying metric space has \(q^{3m}\) points. For \(t>0\), \(t\)-negative type means that for every finite family of **real** coefficients \((c_X)_{X\in V}\) with \(\sum_Xc_X=0\),
\[
\sum_{X,Y\in V}c_Xc_Yd(X,Y)^t\le0.
\]
Strictness means equality only when all coefficients vanish. At \(t=0\), define the powered kernel as one for unequal points and zero on the diagonal. Euclidean dimensions concern an **exact** representation \(\|u_X-u_Y\|_2^2=d(X,Y)^t\); no assertion about unsnowflaked \(d\) embedding is made.

## Proof

**1. Fourier-sector reduction.** Fix any nontrivial additive character \(\psi\) of \(\mathbb F_q\). For each \(A\in V\), define \(\chi_A(X)=\psi(\sum_{i,j}A_{ij}X_{ij})\). Since the powered distance kernel depends only on \(X-Y\), every \(\chi_A\) is an eigenvector of convolution by \(X\mapsto\operatorname{rank}(X)^t\); its real eigenvalue depends only on \(s=\operatorname{rank}(A)\). The constant sector \(s=0\) is irrelevant to negative type. Fourier orthogonality makes the negative-type condition exactly the nonpositivity of the three nonconstant eigenvalues.

**2. A direct subspace transform.** For each integer \(0\le j\le3\), put
\[
h_j(X)=\#\{U\le\mathbb F_q^3:\dim U=j,\ U\subseteq\ker X\}={3-\operatorname{rank}(X)\brack j}_q,
\]
where \({n\brack k}_q\) is the Gaussian binomial coefficient, taken as zero outside \(0\le k\le n\). When \(A\) has rank \(s\), summing first over \(U\) and then over the \(q^{m(3-j)}\) linear maps vanishing on \(U\) gives
\[
\sum_{X\in V}\chi_A(X)h_j(X)=
\begin{cases}
q^{m(3-j)}{3-s\brack j-s}_q,&j\ge s,\\
0,&j<s.
\end{cases}
\]
Indeed, the inner character sum survives exactly when the rowspace of \(A\), regarded as a subspace of \(\mathbb F_q^3\), lies in \(U\). This argument is valid for every prime power \(q\).

**3. Exact powered-distance Fourier multipliers.** For \(t>0\), set \(f_t(X)=\operatorname{rank}(X)^t\), with \(f_t(0)=0\). Evaluating successively at ranks \(3,2,1,0\) yields the unique expansion \(f_t=\sum_{j=0}^3 c_jh_j\), where
\[
\begin{aligned}
c_0&=3^t,\\
c_1&=2^t-3^t,\\
c_2&=1+q3^t-(q+1)2^t,\\
c_3&=-a+qa2^t-q^33^t.
\end{aligned}
\]
The nonconstant eigenvalues, indexed by frequency rank, are consequently
\[
\begin{aligned}
F_1(t)&=Q^2c_1+Q(q+1)c_2+c_3,\\
F_2(t)&=Qc_2+c_3=\Phi_{q,m}(t),\\
F_3(t)&=c_3.
\end{aligned}
\]
The formulas extend to \(t=0\) under the off-diagonal-one convention. In particular, \(F_1(0)=F_2(0)=F_3(0)=-1\).

**4. The critical sector and uniqueness.** The coefficient \((q+1)Q-qa\) is positive. Therefore
\[
F_2'(t)=2^t\left[q(Q-q^2)\log3\,(3/2)^t-((q+1)Q-qa)\log2\right].
\]
The bracket is increasing in \(t\ge0\). Its value at zero increases with \(Q\), because \(q\log3-(q+1)\log2>0\) for \(q\ge2\). At \(Q=q^3\), positivity follows from
\[
\frac{q^3-q-1}{q^2(q-1)}\le\frac32<\frac{\log3}{\log2}.
\]
Thus \(F_2\) increases strictly on \([0,\infty)\). Since \(F_2(0)=-1\) and
\[
F_2(1)=(q-1)\bigl[Q-(q^2-1)\bigr]>0,
\]
there is a unique positive root in \((0,1)\).

For \(q\ge3\), the inequality \(a/q^2\le13/9<\log3/\log2\) makes \(F_3'(t)<0\) on \([0,\infty)\), hence \(F_3(t)<0\) there. For \(q=2\),
\[
F_3(t)=-7+14\cdot2^t-8\cdot3^t
\]
has strictly negative second derivative on \([0,\infty)\). Its tangent bound on \([0,1]\) is
\[
F_3(t)\le-1+t(14\log2-8\log3)<0,
\]
because \(14\log2-8\log3=\log(16384/6561)<1\). Thus \(F_3(t)<0\) throughout \([0,1]\) for every \(q\ge2\).

Finally, \(c_2=q(3^t-2^t)-(2^t-1)\le q(3^t-2^t)\) for \(t\ge0\). As \(Q\ge q^3>q(q+1)\),
\[
F_1(t)\le -Q\bigl(Q-q(q+1)\bigr)(3^t-2^t)+F_3(t)<0
\]
for \(0\le t\le1\). Hence all nonconstant Fourier sectors are strictly negative for \(0\le t<\beta_{q,m}\), and at the endpoint exactly rank-two frequencies vanish. For \(t>\beta_{q,m}\), \(F_2(t)>0\), excluding negative type for any larger exponent.

**5. Exact Euclidean dimension.** The double-centered Gram matrix for squared distances \(d^t\) is \(-\tfrac12JD_tJ\), with \(J\) the orthogonal projection onto the real zero-sum subspace. Its eigenvalues there are precisely \(-\tfrac12F_s(t)\), each repeated by the number of rank-\(s\) frequency matrices. At the threshold, the Fourier nullity is the count of rank-two \(m\times3\) matrices, namely \(R_2(q,m)\) from the displayed formula. The Gram rank is the minimum realization dimension, proving both dimension statements.

**6. Asymptotics.** Write \(L_q=q\log3-(q+1)\log2>0\). As \(Q=q^m\to\infty\) with fixed \(q\), the root satisfies \(F_2(\beta)=0\), \(F_2(0)=-1\), and \(F_2'(0)=QL_q+O_q(1)\). The positive increasing derivative shows \(\beta\le1/F_2'(0)\), so \(\beta\to0\) and the mean-value formula gives \(Q\beta\to1/L_q\). Similarly, for fixed \(m\ge3\) as \(q\to\infty\), \(F_2'(0)\sim q^{m+1}\log(3/2)\); its second derivative near zero is \(O(q^{m+1})\). The same mean-value argument gives the second limit.

## Verification

A standalone Python 3 checker is included as `verify.py` and uses no external packages. Running `python3 verify.py` prints `BILINEAR_THREE_NEGATIVE_TYPE_PASS` after exhaustive additive-character Fourier sums for all \(q^{3m}\) matrices in four cases: \((q,m)=(2,3),(2,4),(3,3),(4,3)\). The characteristic-three computation checks cancellation of both nontrivial cubic-character residues exactly; the characteristic-four computation uses arithmetic in \(\mathbb F_4\). It also checks all three sector formulas, integer frequency multiplicities, critical roots with high-precision decimal arithmetic, and additional parameter instances. For \((q,m)=(2,3)\), the critical exponent is \(0.348624200287720629\ldots\), and the minimum Euclidean dimension decreases from \(511\) below the endpoint to \(217\) at the endpoint. For \((q,m)=(3,3)\), these dimensions are \(19682\) and \(11570\), respectively. The all-parameter statements are proved in the preceding sections, not inferred from numerical testing.

## Relationship to prior work

Delsarte's 1978 study of bilinear forms gives the rank-translation association scheme and its generalized Krawtchouk eigenmatrix. It already contains the Fourier-table ingredients but does not state the exponent-dependent negative-type transition, the rank-two endpoint kernel, the sharp Hilbert embedding dimension, or the two scaling laws. Li and Weston (2009) develop the general interval and strictness theory of negative type. Sánchez (2011) gives a general finite-metric criterion, with worked graph applications; the present evaluation exploits the rank-three matrix-space Fourier sectors and adds an explicit all-parameter threshold and critical nullity. A general theorem specialized to this scheme could imply some of these conclusions; exhaustive historical priority is not asserted.

## Limitations

The theorem covers only matrices with one dimension exactly three and other dimension at least three, not arbitrary rectangular dimensions. It determines exact Euclidean embedding dimensions for powered squared distances only within the negative-type range, not least-distortion embeddings for larger powers. Its originality comparison covers identified primary and database sources but cannot establish the absence of all unpublished or differently named prior calculations. No independent mathematical audit has been performed.

## References

1. P. Delsarte, *Bilinear forms over a finite field, with applications to coding theory*, Journal of Combinatorial Theory, Series A **25** (1978), 226–241. DOI: `10.1016/0097-3165(78)90015-8`.
2. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:`0901.0695` (first public version January 6, 2009).
3. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:`1108.0451` (first public version August 2, 2011).
