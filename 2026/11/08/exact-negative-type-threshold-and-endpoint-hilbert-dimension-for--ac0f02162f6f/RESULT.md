# Exact negative-type threshold and endpoint Hilbert dimension for alternating six-forms

## Finding

Let \(q\ge2\) be a prime power, \(V=\mathbb F_q^6\), and \(\mathcal A=\operatorname{Alt}_6(\mathbb F_q)\). This is the additive group of all alternating bilinear forms on \(V\); in characteristic two the matrices are symmetric with zero diagonal, while in odd characteristic they are skew-symmetric. It contains \(q^{15}\) elements. Equip it with the rank metric
\[
d(X,Y)=\frac12\operatorname{rank}(X-Y)\in\{0,1,2,3\}.
\]
Define
\[
\Phi_q(\alpha)=(q^5-q^4-q^2-1)
-q^2(q^5-q^4+q^3-q^2-1)2^\alpha+q^6(q-1)3^\alpha.
\]
There is exactly one zero \(\beta_q>0\) of \(\Phi_q\). For each real \(\alpha>0\), the metric has \(\alpha\)-negative type **if and only if** \(\alpha\le\beta_q\), with strict negative type precisely for \(0<\alpha<\beta_q\). Thus \(\beta_q\) is its exact generalized roundness. Define
\[
M_q={6\brack2}_q=\frac{(q^6-1)(q^5-1)}{(q^2-1)(q-1)}.
\]
At \(\alpha=\beta_q\) its distance-power matrix has a zero-sum nullspace of dimension precisely \(M_q q^2(q-1)(q^3-1)\). Consequently the smallest Hilbert-space dimension in an isometric embedding of \((\mathcal A,d^{\alpha/2})\) is \(q^{15}-1\) below the endpoint and exactly
\[
q^{15}-1-M_q q^2(q-1)(q^3-1)
\]
at the endpoint. For \(\alpha>\beta_q\), no such squared-Euclidean embedding exists. The critical exponent has a sharp asymptotic law
\[
\lim_{q\to\infty}q^7\beta_q=\frac1{\log(3/2)}.
\]
This unusually small threshold and the endpoint collapse are properties of the rank geometry of alternating forms, not the unrestricted rectangular matrix rank metric.

## Assumptions and scope

An alternating form has even rank, including in characteristic two. The metric is half this rank; subadditivity of matrix rank verifies the triangle inequality. For a finite metric \(d\), \(\alpha\)-negative type means
\[
\sum_{X,Y\in\mathcal A}c_Xc_Yd(X,Y)^\alpha\le0
\quad\text{for all real }(c_X)\text{ with }\sum_Xc_X=0.
\]
It is strict if equality is possible only for \(c_X=0\) for all \(X\). No claim is made about negative exponents or all alternating dimensions. Use any nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\) and identify the dual of \(\mathcal A\) with \(\bigwedge^2 V\) using the coordinate coefficient pairing. The frequency rank is the alternating rank of the dual bivector. Changing bases preserves its rank. We use the count \({n\brack2}_q=(q^n-1)(q^{n-1}-1)/((q^2-1)(q-1))\).

## Proof

**1. First Fourier shell.** Let \(K_j\) be the characteristic function of the alternating forms of rank \(2j\), for \(j=1,2,3\). Every nonzero rank-two form is a nonzero vector in the one-dimensional space \(\bigwedge^2 L\) for exactly one two-plane \(L\subset V\). The sum of the corresponding character values on \(\bigwedge^2 L\setminus\{0\}\) is \(q-1\) if the dual frequency restricts to zero on \(L\), and \(-1\) otherwise. If the frequency has rank \(r\in\{2,4,6\}\), let \(I_r\) count its totally isotropic two-planes. If its radical dimension is \(t=6-r\), count independent pairs \((u,v)\): when \(u\) lies in the radical, there are \(q^6-q\) choices of \(v\) outside its line; otherwise the orthogonal hyperplane gives \(q^5-q\) choices. Division by \((q^2-1)(q^2-q)\) yields
\[
I_r=\frac{(q^t-1)(q^6-q)+(q^6-q^t)(q^5-q)}{(q^2-1)(q^2-q)}.
\]
With \(M={6\brack2}_q\), the rank-two Fourier coefficient is \(a_r=qI_r-M\), giving
\[
\begin{array}{c|l}
r&a_r\\\hline
2&q^7+q^5-q^4-q^2-1\\
4&q^5-q^4-q^2-1\\
6&-(q^4+q^2+1)
\end{array}
\]
for all prime powers, including characteristic two.

**2. Second Fourier shell.** For each alternating form \(X\), let
\[
F(X)=\#\{U\le V:\dim U=2,\;U\subset\operatorname{rad}X\}.
\]
Put \(M_4={4\brack2}_q=(q^2+1)(q^2+q+1)\). The values of \(F\) at ranks \(0,2,4,6\) are respectively \(M,M_4,1,0\). Therefore
\[
K_2=F-M_4K_1-M\mathbf1_{\{0\}}.
\]
For each fixed \(U\), forms with \(U\subset\operatorname{rad}X\) form a six-dimensional linear space, so its character sum is \(q^6\) if the dual bivector projects to zero in \(\bigwedge^2(V/U)\), and zero otherwise. Write \(C_r\) for the number of admissible planes \(U\) when the dual frequency has rank \(r\). Elementary bivector reduction gives
\[
C_2=M-q^4M_4,\qquad C_4=(q+1)(q^2+1),\qquad C_6=0.
\]
Indeed, for a rank-two decomposable bivector one excludes the two-planes disjoint from its two-dimensional support, of which there are \(q^4M_4\); for rank four, the only admissible two-planes are the Lagrangians in its four-dimensional nondegenerate support, counted by \((q+1)(q^2+1)\); a rank-six bivector cannot vanish on a quotient by a two-plane because its rank drops by at most four. Thus the rank-four Fourier coefficients \(b_r=q^6C_r-M_4a_r-M\) are
\[
\begin{array}{c|l}
r&b_r\\\hline
2&q^2(q-1)(q^2+q+1)(q^5-q^4-q^2-1)\\
4&-q^2(q^5-q^4+q^3-q^2-1)\\
6&q^2(q^4+q^2+1).
\end{array}
\]

**3. Third shell and complete Fourier table.** At any nontrivial character, the transforms of the four rank indicators sum to zero. The rank-zero singleton has transform one. Hence \(c_r=\widehat K_3(r)=-1-a_r-b_r\), namely
\[
\begin{array}{c|l}
r&c_r\\\hline
2&-q^6(q-1)^2(q^2+q+1)\\
4&q^6(q-1)\\
6&-q^6.
\end{array}
\]
The distance-power kernel \(d(X,Y)^\alpha\) has Fourier multiplier, at every nonzero rank-\(r\) frequency,
\[
\Lambda_r(\alpha)=a_r+b_r2^\alpha+c_r3^\alpha.
\]
The exact multiplicities of these frequencies for \(r=2,4,6\) are
\[
(q-1)M,\quad Mq^2(q-1)(q^3-1),\quad q^6(q-1)(q^3-1)(q^5-1),
\]
respectively. These follow by choosing the radical and then a nondegenerate alternating form on its complement; with the single rank-zero frequency their sum is \(q^{15}\). All three multipliers start at \(-1\) when \(\alpha=0\).

**4. The unique crossing.** In the rank-two frequency sector, \(a_2>0\), \(b_2>0\), \(c_2<0\), and \(|c_2|=a_2+b_2+1>b_2\); hence \(\Lambda_2'(\alpha)<0\) for all \(\alpha\ge0\). In the rank-six frequency sector, \(b_6/|c_6|=1+q^{-2}+q^{-4}\le21/16<\log3/\log2\), so \(\Lambda_6'(\alpha)<0\). By contrast, in the rank-four frequency sector \(a_4>0\), \(b_4<0\), \(c_4>0\), with
\[
\frac{|b_4|}{c_4}=1+\frac{q^3-q^2-1}{q^4(q-1)}\le\frac{19}{16}<\frac{\log3}{\log2},
\]
so \(\Lambda_4'(\alpha)>0\) for all \(\alpha\ge0\). It starts at \(-1\) and tends to \(+\infty\), since its \(3^\alpha\) coefficient is positive. Therefore it has exactly one positive zero \(\beta_q\), and is the sole frequency sector that can violate conditional negative definiteness. Finite Fourier diagonalization proves the claimed exact negative-type interval and endpoint nullspace.

**5. Hilbert geometry and asymptotic.** Let \(H\) be orthogonal projection in \(\mathbb R^{q^{15}}\) onto vectors summing to zero. The Schoenberg centered matrix \(B=-\tfrac12H(d(X,Y)^\alpha)_{X,Y}H\) is positive semidefinite exactly in the negative-type interval. Its rank equals the minimal dimension of a Euclidean realization of pairwise squared distances \(d(X,Y)^\alpha\). Below the threshold all nonconstant Fourier modes have positive Gram eigenvalues, giving rank \(q^{15}-1\); at the threshold exactly the rank-four character sector vanishes, giving the advertised strict dimensional drop. The positive eigenvalues are \(-\Lambda_r(\alpha)/2\), with the multiplicities above. At \(\alpha=0\), \(\Lambda_4(0)=-1\), while
\[
\Lambda_4'(0)=q^7\log(3/2)\,(1+O(q^{-1})).
\]
The ratio of its second derivative in a sufficiently short interval around zero to its first derivative stays \(O(1)\) (the positive \(3^\alpha\) term dominates the negative \(2^\alpha\) term). The mean value theorem and monotonicity then yield \(\beta_q=1/(q^7\log(3/2))(1+O(q^{-1}))\), proving the limit. Schoenberg's characterization also gives positive semidefiniteness of every heat kernel \(e^{-t d(X,Y)^\alpha}\) for all \(t>0\) exactly in this interval; this last statement is an equivalent consequence, not separate novelty.

## Verification

Run the included `verify.py` with Python 3 and its standard library. It independently enumerates all \(2^{15}=32768\) alternating six-by-six matrices over \(\mathbb F_2\), computes their ranks by binary elimination, and performs three complete 15-dimensional Walsh transforms, comparing the Fourier multipliers **at every one of the 32768 frequencies**, not merely a sample. The resulting coefficient triples in ranks \(2,4,6\) are \((139,308,-448)\), \((11,-76,64)\), and \((-21,84,-64)\), respectively, with rank-orbit sizes \((651,18228,13888)\). For \(q=2,3,4,5,7,11\), it separately checks exact symbolic shell coefficients, orbit sizes, and numerical root locations. In particular \(\beta_2=0.053341755468\ldots\), and the endpoint embedding dimension at \(q=2\) is exactly \(14539\), versus \(32767\) below it. Finite checks corroborate but do not replace the all-prime-power proof.

## Relationship to prior work

Delsarte and Goethals [1] establish the association-scheme framework for alternating bilinear forms over finite fields. Their general eigenmatrix is relevant prior information; no claim of inventing the underlying Fourier-spherical decomposition is made. Complete original article text was not accessible for an exhaustive statement-by-statement comparison; a prior formula for this exact roundness threshold or stronger covering theorem remains an explicit priority risk. Weston [2] proves general lower bounds on positive negative-type exponents for finite metric spaces, not the exact exponent here. Sánchez [3] gives an arbitrary finite-metric algorithm to obtain the supremal exponent, but it does not state the alternating-six-form formula, endpoint Hilbert rank, or large-field law. The result isolates and proves the closed three-sector crossing for this natural alternating matrix metric. Exact prior-result comparisons and remaining risks are documented in AUDIT.json.

## Limitations

The theorem concerns only alternating \(6\)-dimensional matrices, all finite field orders, and positive powers. It does not determine thresholds in arbitrary alternating dimension, asymptotic bounds at fixed field order and growing dimension, non-Hilbert embeddings, or independent publication priority. The 1975 alternating-form paper is a serious historical overlap risk because its association scheme may give the full Fourier table as a specialization; this proof derives those coefficients independently but does not claim them as novel. External independent mathematical audit has not been performed.

## References

1. P. Delsarte and J. M. Goethals, *Alternating bilinear forms over GF(q)*, *Journal of Combinatorial Theory, Series A* 19 (1975), 26–50, DOI:10.1016/0097-3165(75)90090-4; bibliographic evidence only; full text inaccessible.
2. A. Weston, *Optimal lower bounds on the maximal p-negative type of finite metric spaces*, arXiv:0807.2705v1, first publicly submitted 2008-07-17; full open-access preprint inspected, https://arxiv.org/abs/0807.2705.
3. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, first publicly submitted 2011-08-02; full open-access preprint inspected, https://arxiv.org/abs/1108.0451.
