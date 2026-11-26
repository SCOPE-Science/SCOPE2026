# A sharp boundary-Jacobian criterion for a two-angular-mode Bergman Toeplitz family

## Finding

**Theorem.** On the analytic Bergman space \(A^2(\mathbb D)\) with normalized planar area measure, let \(T_{\varphi}=P(\varphi\cdot)\) and
\[
\varphi(z)=a z^2+bz\overline z^{\,2},\qquad a,b\in\mathbb C.
\]
Then
\[
\boxed{T_{\varphi}\text{ is hyponormal}\quad\Longleftrightarrow\quad 3|b|\le 2|a|.}
\]
The equality case is included, and the answer is independent of the phases of \(a,b\). More precisely, in this polynomial family hyponormality is **equivalent** to the nonnegativity of its boundary complex Jacobian:
\[
T_{\varphi}\text{ is hyponormal}
\quad\Longleftrightarrow\quad
\min_{|z|=1}\left(|\partial_z\varphi(z)|^2-|\partial_{\bar z}\varphi(z)|^2\right)\ge0.
\]
The self-commutator is trace class, and its exact trace is
\[
\operatorname{tr}[T_{\varphi}^{*},T_{\varphi}]=2|a|^2-|b|^2.
\]

## Assumptions and scope

\(A^2(\mathbb D)\) consists of analytic functions with squared norm \(\int_{\mathbb D}|f(z)|^2\,dA(z)/\pi\); \(P\) is the orthogonal Bergman projection. The symbol is exactly the displayed two-term polynomial; no assertion is made for other exponents, general smooth symbols, or nonzero Bergman weights. We use the convention that hyponormality means \([T^*,T]=T^*T-TT^*\succeq0\).

## Proof

**1. Exact angular matrix.** Let \(e_n(z)=\sqrt{n+1}\,z^n\) (\(n\ge0\)) and \(S=T_{z^2}\), \(R=T_{z\bar z^2}\). Direct integration of monomials against normalized area gives
\[
Se_n=A_ne_{n+2},\quad A_n=\sqrt{\frac{n+1}{n+3}},\qquad
Re_n=B_ne_{n-1},\quad B_0=0,\quad B_n=\frac{\sqrt{n(n+1)}}{n+2}\ (n\ge1).
\]
The \(e_{-1}\) term is zero. First suppose \(a\ne0\). Multiplication of the operator by a nonzero scalar and conjugation by a diagonal rotation reduce the self-commutator to that of \(S+tR\), where \(t=|b|/|a|\ge0\). Indeed, every nonzero off-diagonal self-commutator entry couples the indices \(n\) and \(n+3\), and a rotation \(e_n\mapsto e^{in\theta}e_n\) removes the common relative phase.

For \(C_t=[(S+tR)^*,S+tR]\), direct composition gives a real symmetric band matrix:
\[
\begin{split}
\langle C_te_n,e_n\rangle&=D_n+t^2E_n,\\
\langle C_te_n,e_{n+3}\rangle&=tO_n,\\
D_0&=\tfrac13,\qquad D_1=\tfrac12,\qquad
D_n=\frac4{(n+1)(n+3)}\quad(n\ge2),\\
E_n&=-\frac{(n+1)(3n+8)}{(n+2)^2(n+3)^2}\quad(n\ge0),\\
O_n&=\frac{2}{(n+3)(n+5)}\sqrt{\frac{n+1}{n+4}}\quad(n\ge0).
\end{split}
\]
All other entries vanish. In particular \(E_n<0\), \(O_n>0\), and \(O_n\le 2/((n+3)(n+5))\). For a general pair \(a,b\), the diagonal is \(|a|^2D_n+|b|^2E_n\) and the off-diagonal has modulus \(|ab|O_n\).

**2. Sufficiency at the sharp endpoint.** It suffices to prove positivity for \(t=2/3\), because the diagonal \(D_n+t^2E_n\) decreases as \(t\) increases and the off-diagonal absolute value \(tO_n\) increases. Set \(d_n=D_n+(4/9)E_n\) and use \(O_j=0\) when \(j<0\). A row-dominance margin is \(d_n-(2/3)(O_n+O_{n-3})\). For \(n=0,1,2\), the diagonal entries are exactly \(19/81,35/81,11/50\), respectively, and the bound on \(O_n\) gives the strictly positive lower margins
\[
\frac{59}{405},\qquad\frac{61}{162},\qquad\frac{191}{1050}.
\]
For every integer \(n\ge3\), the same upper bound on both off-diagonal entries yields
\[
\begin{aligned}
d_n-\frac23(O_n+O_{n-3})
&\ge D_n+\frac49E_n
-\frac{4}{3(n+3)(n+5)}-\frac{4}{3n(n+2)}\\
&=\frac{4P(n)}{9n(n+1)(n+2)^2(n+3)^2(n+5)},
\end{aligned}
\]
where
\[
P(n)=13n^4+79n^3+89n^2-175n-270.
\]
The all-index positivity is exact, since for \(m=n-3\ge0\),
\[
P(n)=13m^4+235m^3+1502m^2+3896m+3192>0.
\]
Thus every row is strictly diagonally dominant with positive diagonal. For each finitely supported vector \(x\), the inequality \(2|x_nx_{n+3}|\le|x_n|^2+|x_{n+3}|^2\) implies \(\langle C_{2/3}x,x\rangle\ge0\). The self-commutator is bounded, so density extends positivity to all of \(A^2(\mathbb D)\). Monotonicity of the diagonal and of off-diagonal absolute values proves positivity for all \(0\le t\le2/3\).

**3. Necessity from long alternating angular chains.** The exact formulas imply
\[
\lim_{n\to\infty}n^2D_n=4,\qquad
\lim_{n\to\infty}n^2E_n=-3,\qquad
\lim_{n\to\infty}n^2O_n=2.
\]
For integers \(N\ge1\), \(L\ge2\), let
\[
v_{N,L}=\frac1{\sqrt L}\sum_{j=0}^{L-1}(-1)^j e_{N+3j}.
\]
For each fixed \(L\) and \(t\ge0\), substitution into the band matrix gives
\[
\lim_{N\to\infty}N^2\langle C_tv_{N,L},v_{N,L}\rangle
=4-3t^2-4t\left(1-\frac1L\right).
\]
If \(t>2/3\), then \(4-3t^2-4t=-(3t-2)(t+2)<0\). Choose \(L\) large enough that the limit displayed above is negative, and then choose \(N\) large enough that the actual quadratic form is negative. Consequently \(C_t\not\succeq0\). When \(a=0\) and \(b\ne0\), \([R^*,R]\) is diagonal with strictly negative entries \(E_n\); when \(a=b=0\), the operator is zero. This proves the full classification, including all boundary cases.

**4. Boundary Jacobian and trace.** The complex derivatives are
\[
\partial_z\varphi=2az+b\bar z^2,
\qquad\partial_{\bar z}\varphi=2bz\bar z.
\]
Since the phase difference winds three times on \(|z|=1\),
\[
\min_{|z|=1}(|\partial_z\varphi|^2-|\partial_{\bar z}\varphi|^2)
=(2|a|-|b|)^2-4|b|^2
=4|a|^2-4|a||b|-3|b|^2.
\]
This is nonnegative exactly when \(3|b|\le2|a|\), with the zero-symbol case included.
Finally, \(D_n,E_n,O_n=O((n+1)^{-2})\) apart from the finitely many initial indices. Hence the band matrix defines a trace-class self-commutator. Telescoping \(\sum_{n\ge0}(A_n^2-A_{n-2}^2)=2\) and \(\sum_{n\ge0}(B_n^2-B_{n+1}^2)=-1\), where absent negative-index terms are zero, gives the trace formula above.

## Verification

All identities and bounds are explicit rational or elementary square-root expressions. The standalone `check_toeplitz.py` uses only the Python standard library and can be run with `python3 check_toeplitz.py`. It checks thousands of exact fraction identities, the endpoint row bounds, direct operator-action comparisons and negative finite angular-chain witnesses. The infinite-dimensional positivity and necessity do not depend on the finite computations. The decisive all-index certificate is the positive-coefficient expansion of \(P(n)\) after the substitution \(m=n-3\).

## Relationship to prior work

Fleeman and Liaw (first public 30 July 2017) established general sufficient comparisons for opposite-angular nonharmonic Bergman Toeplitz binomials, including the framework of their Theorem 9 in the 2019 journal version. Those inequalities do not state this exact all-coefficient boundary, its necessity, or the boundary-Jacobian equivalence. The endpoint proof above verifies an infinite family of inequalities with one explicit all-index polynomial certificate. Kim and Lee (2021), especially Theorem 2.9, give necessary bounds for the same index configuration in a larger family but no sharp equivalence; the 2022 weighted-space paper and 2023 follow-up address related nonharmonic binomials under other index restrictions or sufficiency hypotheses. The present result is a narrow exact classification of one natural mixed-angular family, not a replacement for those general investigations. Standard facts about angular Toeplitz matrices and boundary Jacobians are used without novelty claims.

## Limitations

The theorem is restricted to the classical unweighted analytic Bergman disk and the explicitly stated two-term symbol. It does not classify three-term symbols, arbitrary exponents, other radial weights, or general Toeplitz operators. A general earlier sufficient inequality may recover the endpoint after nontrivial specialization; historical priority of the evaluated exact boundary is therefore qualified. No independent mathematical audit has been performed; the supplementary finite tests are not an infinite proof.

## References

1. M. Fleeman and C. Liaw, *Hyponormal Toeplitz operators with non-harmonic symbol acting on the Bergman space*, first public arXiv:1707.09677 (30 July 2017), later *Operators and Matrices* **13** (2019), 61–83, https://doi.org/10.7153/oam-2019-13-04.
2. B. Simanek, *Hyponormal Toeplitz operators with non-harmonic algebraic symbol*, arXiv:1807.00356 (1 July 2018), later *Analysis and Mathematical Physics* **9** (2019), 1613–1626, https://doi.org/10.1007/s13324-018-00279-2.
3. S. Kim and J. Lee, *Hyponormality of Toeplitz operators with non-harmonic symbols on the Bergman spaces*, first public 7 April 2021, https://doi.org/10.1186/s13660-021-02602-1.
4. S. Kim and J. Lee, *Hyponormal Toeplitz operators with non-harmonic symbols on the weighted Bergman spaces*, first public 4 December 2022, https://doi.org/10.1007/s43034-022-00241-1.
5. S. Kim and J. Lee, *Remarks on hyponormal Toeplitz operators with nonharmonic symbols*, *Open Mathematics* **21** (2023), https://doi.org/10.1515/math-2023-0114.
