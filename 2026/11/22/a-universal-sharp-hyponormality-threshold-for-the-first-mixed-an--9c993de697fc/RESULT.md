# A universal sharp hyponormality threshold for the first mixed-angular Bergman Toeplitz pair

## Finding

Let \(A^2_\alpha(\mathbb D)\) be the analytic Bergman space with normalized measure \((\alpha+1)(1-|z|^2)^\alpha dA(z)\), where \(\alpha>-1\) and \(dA\) is normalized planar area. For all complex \(a,b\), the Toeplitz operator with the nonharmonic polynomial symbol
\[
\varphi_{a,b}(z)=az+bz\overline z^{\,2}
\]
is hyponormal **if and only if**
\[
\boxed{|a|\ge 3|b|.}
\]
The constant \(3\) is sharp, the equality case is included, and the criterion is independent of the Bergman weight \(\alpha\). In particular, for \(b\ne0\), the weaker asymptotic diagonal self-commutator test \(|a|^2\ge3|b|^2\) does not characterize hyponormality; the angular off-diagonal interactions impose the larger exact condition.

## Assumptions and scope

Here \(T_\varphi f=P_\alpha(\varphi f)\), where \(P_\alpha\) is the weighted Bergman orthogonal projection. Hyponormal means \(T_\varphi^*T_\varphi-T_\varphi T_\varphi^*\succeq0\). All weights \(\alpha>-1\), including negative weights, and all complex coefficients are allowed. No restriction on their phases is necessary. This is a statement about analytic Bergman spaces, not harmonic or polyanalytic Bergman spaces.

Write \(q=\alpha+1>0\), let \(e_n\) denote the normalized monomials, and set
\[
x_n=\frac{n+1}{n+q+1}\quad(n\ge0),\qquad x_{-1}=0.
\]
Define positive numbers \(u_n=\sqrt{x_n}\) and \(v_n=x_n\sqrt{x_{n-1}}\), with \(v_0=0\). Direct weighted Bergman projection gives
\[
T_{z}e_n=u_ne_{n+1},\qquad
T_{z\overline z^{\,2}}e_n=\begin{cases}v_ne_{n-1},&n\ge1,\\0,&n=0.\end{cases}
\]

## Proof

**1. Exact self-commutator.** Let \(H=T_{\varphi_{a,b}}^*T_{\varphi_{a,b}}-T_{\varphi_{a,b}}T_{\varphi_{a,b}}^*\), and define for every \(n\ge0\)
\[
A_n=x_n-x_{n-1}=\frac{q}{(n+q)(n+q+1)},\quad
B_n=x_n^2x_{n-1}-x_{n+1}^2x_n,
\]
\[
C_n=\sqrt{x_nx_{n+1}}\,(x_{n+2}-x_{n+1})
=\sqrt{x_nx_{n+1}}\,A_{n+2}>0.
\]
The only nonzero matrix entries of \(H\) occur on the diagonal and the two diagonals at distance two. In the convention \(\langle H e_n,e_{n+2}\rangle\), they are
\[
\langle He_n,e_n\rangle=|a|^2A_n+|b|^2B_n,
\qquad
\langle He_n,e_{n+2}\rangle=a\overline b\,C_n.
\]
The reverse off-diagonal is its complex conjugate.

**2. Uniform positivity at and above the threshold.** The exact rational identity
\[
3A_n+B_n=\frac{q\,P(n,q)}{(n+q)(n+q+1)^2(n+q+2)^2}
\]
holds, where
\[
\begin{aligned}
P(n,q)={}&6n^2q+4n^2+9nq^2+23nq+12n\\
&+3q^3+15q^2+20q+8.
\end{aligned}
\]
Every displayed coefficient of \(P\) is nonnegative and its constant term is positive. Thus \(B_n>-3A_n\). Furthermore, \(0<x_n<1\) and \(A_{n+2}<A_n\). Extending \(C_j=0\) for negative indices, we have
\[
0\le C_n+C_{n-2}<A_{n+2}+A_n<2A_n,
\]
with the analogous inequality for \(n=0,1\) because the absent term is zero. When \(b\ne0\) let \(t=|a|/|b|\). For \(t\ge3\), every row satisfies the strictly positive diagonal-dominance estimate
\[
\begin{aligned}
|a|^2A_n+|b|^2B_n-|ab|(C_n+C_{n-2})
&>|b|^2(t^2-3-2t)A_n\\
&=|b|^2(t-3)(t+1)A_n\ge0.
\end{aligned}
\]
The elementary bound \(2|v_n v_{n+2}|\le |v_n|^2+|v_{n+2}|^2\) then proves \(\langle Hv,v\rangle\ge0\) for every finitely supported vector; boundedness of \(H\) extends the result to the whole Hilbert space. If \(b=0\), the operator is a scalar multiple of analytic multiplication and is hyponormal, including \(a=b=0\).

**3. Necessity and sharpness.** Suppose \(b\ne0\) and \(0\le t<3\). As \(n\to\infty\),
\[
\frac{n^2A_n}{q}\to1,\qquad
\frac{n^2B_n}{q}\to-3,\qquad
\frac{n^2C_n}{q}\to1.
\]
Choose a positive integer \(L\) so large that \(L(t^2-3)-2t(L-1)<0\). For large \(N\), take the vector supported on \(e_N,e_{N+2},\ldots,e_{N+2(L-1)}\), with consecutive coefficients of modulus one and phase chosen so that every off-diagonal contribution \(2\operatorname{Re}(a\overline b C_n v_n\overline{v}_{n+2})\) is negative. Then
\[
\lim_{N\to\infty}\frac{N^2}{q|b|^2}\langle Hv^{(N)},v^{(N)}\rangle
=L(t^2-3)-2t(L-1)<0.
\]
Consequently \(H\) is not positive semidefinite. When \(a=0\), the same argument works with no phase choice. This establishes necessity for every \(\alpha>-1\) and proves sharpness at \(3\).

## Verification

The accompanying `CHECK.py` uses only the Python standard library. It checks the exact rational polynomial identity and strict diagonal inequalities at multiple rational weights and degrees; compares independently computed operator forms with the derived band formula; and constructs explicit finite-support negative quadratic-form tests below the threshold. Run `python3 CHECK.py` in the directory containing the script. These finite checks are auxiliary; the inequalities and limits above provide the proof for all allowed real weights, coefficient phases and indices.

## Relationship to prior work

Fleeman and Liaw's 2017 preprint (published 2019) investigated hyponormal Bergman Toeplitz operators with nonharmonic polynomial symbols and emphasized the decisive role of mixed cross terms. Kim and Lee (2021) obtained general necessary conditions for two opposing-angular monomial terms. Kim and Lee (2022 prepublication / 2023 volume) extended necessary conditions to every weighted analytic Bergman space; their Theorem 2.8 suppresses cross terms when deriving scalar diagonal restrictions and does not imply the sharp sufficiency or the full sharp necessity here. Kim and Lee (2023) study additional necessary and sufficient regimes under different degree/phase hypotheses. None of those inspected statements supplies the universal exact \(3\)-threshold for \(az+bz\bar z^2\). The distinction is not a change of notation: the asymptotic two-step off-diagonal contribution changes the scalar diagonal bound to a strictly stronger all-vector bound.

## Limitations

The result covers this minimal opposite-angular two-term symbol, not arbitrary bivariate polynomials or higher monomial degrees. The proof establishes hyponormality, not subnormality or complete self-commutator spectral formulas. Bibliographic noncoverage was checked against identified relevant literature and published summaries, but an unindexed equivalent or a theorem in an undiscovered source remains possible. No independent mathematical audit has been performed.

## References

1. M. Fleeman and C. Liaw, *Hyponormal Toeplitz operators with non-harmonic symbol acting on the Bergman space*, arXiv:1707.09677, first public 30 July 2017; *Operators and Matrices* **13** (2019), 61–83. https://arxiv.org/abs/1707.09677
2. S. Kim and J. Lee, *Hyponormality of Toeplitz operators with non-harmonic symbols on the Bergman spaces*, *Journal of Inequalities and Applications* **2021**, 67, first public 7 April 2021. https://doi.org/10.1186/s13660-021-02602-1
3. S. Kim and J. Lee, *Hyponormal Toeplitz operators with non-harmonic symbols on the weighted Bergman spaces*, *Annals of Functional Analysis* **14** (2023), article 14, first public 4 December 2022. https://doi.org/10.1007/s43034-022-00241-1
4. S. Kim and J. Lee, *Remarks on hyponormal Toeplitz operators with nonharmonic symbols*, *Open Mathematics* **21** (2023), 20230114, public 2 September 2023. https://doi.org/10.1515/math-2023-0114
