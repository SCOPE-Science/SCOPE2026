# A unique fractional Markov-repair exponent for signed cycles with one antagonistic edge

## Finding
For every integer \(n\ge4\) and every negative closing-edge conductance of magnitude \(a\in(0,1/(n-1))\), the stable signed cycle obtained by adding a negative edge between the endpoints of the unit-conductance path \(P_n\) has a **unique fractional Markov-repair exponent** \(\alpha_*(n,a)\in(0,1)\). With \(L_{n,a}\) the signed combinatorial Laplacian, the following is an if-and-only-if characterization, with quantifiers over *all positive times*:

\[
\left[e^{-tL_{n,a}^{\alpha}}\right]_{ij}>0\quad
(\forall\,i,j,\ \forall\,t>0)
\quad\Longleftrightarrow\quad 0<\alpha\le\alpha_*(n,a),\qquad 0<\alpha<1.
\]

For \(\alpha>\alpha_*\), the endpoint-to-endpoint transition is negative for all sufficiently small positive times; all entries eventually become positive permanently. The threshold is strictly decreasing and continuously differentiable in \(a\), and
\[
\lim_{a\downarrow0}\alpha_*(n,a)=1,
\qquad
\lim_{a\uparrow1/(n-1)}\alpha_*(n,a)=0.
\]

The threshold is the **unique** root \(\alpha\in(0,1)\) of the explicit one-dimensional integral
\[
\int_0^\infty
\frac{s^{\alpha}[1-aU_{n-2}(1+s/2)]}
{sU_{n-1}(1+s/2)\left[1-\frac{2a(U_{n-1}(1+s/2)-U_{n-2}(1+s/2)-1)}{sU_{n-1}(1+s/2)}\right]}\,ds=0,
\]
where \(U_k\) is the Chebyshev polynomial of the second kind. This improper integral is convergent for every \(0<\alpha<1\) and the stated stable range of \(a\).

## Assumptions and scope
Vertices are labelled \(0,1,\ldots,n-1\). Each path edge \(\{i,i+1\}\) has conductance \(1\), and the closing edge \(\{0,n-1\}\) has conductance \(-a\). The matrix is
\[
L_{n,a}=L_{P_n}-a bb^{\mathsf T},\qquad b=e_0-e_{n-1}.
\]
Here \(L_{P_n}\) is the usual nonnegative combinatorial path Laplacian. Matrix powers are defined by the real symmetric spectral functional calculus, with \(0^{\alpha}=0\). The heat kernel is the matrix exponential in the original standard coordinatewise cone (no switching of vertex signs). Strictly positive means every entry is strictly positive. Markov means nonnegative entries and row sums one. A selfadjoint matrix \(L_{n,a}\) has row sums zero; the range \(0<a<1/(n-1)\) guarantees that zero is its sole zero eigenvalue.

For notational convenience, \(U_{-1}=0\), \(U_0=1\), and \(U_{k+1}(x)=2xU_k(x)-U_{k-1}(x)\).

## Proof
**1. Stability of the signed cycle.** The path's effective resistance between endpoints is \(n-1\). For any vector \(x\), Cauchy--Schwarz along the path gives
\[
|x_0-x_{n-1}|^2\le(n-1)\sum_{j=0}^{n-2}|x_j-x_{j+1}|^2.
\]
Consequently \(x^{\mathsf T}L_{n,a}x\ge[1-a(n-1)]x^{\mathsf T}L_{P_n}x\), with equality only on the constants in the stated open parameter range. Thus \(L_{n,a}\succeq0\) and \(\ker L_{n,a}=\mathrm{span}\{\mathbf1\}\).

**2. Exact path resolvent and endpoint extremality.** Fix \(s>0\), write \(x=1+s/2\), \(A_s=sI+L_{P_n}\), \(G_s=A_s^{-1}\), and let \(p_k=U_k(x)-U_{k-1}(x)\). Continuant inversion of the Jacobi matrix gives, for \(0\le i\le j<n\),
\[
(G_s)_{ij}=\frac{p_i p_{n-1-j}}{D_n},\qquad
D_n=\det A_s=sU_{n-1}(x).
\]
Here \(p_0=1\), and \(p_{k+1}>p_k\) for \(s>0\); hence \((G_s)_{0,n-1}=1/D_n\) is the strictly smallest off-diagonal path resolvent entry. Moreover the components \(v_i=(G_sb)_i=(p_{n-1-i}-p_i)/D_n\) decrease from \(v_0=(p_{n-1}-1)/D_n\) to \(-v_0\). Thus \(|v_i|\le v_0\).

Set \(r(s)=b^{\mathsf T}G_sb=2(p_{n-1}-1)/D_n\). Since \(r'(s)=-\|G_sb\|_2^2<0\) and \(r(0+)=n-1\), the denominator \(1-ar(s)\) is strictly positive. Sherman--Morrison gives
\[
R_s:=(sI+L_{n,a})^{-1}
=G_s+\frac{a}{1-ar(s)}vv^{\mathsf T}.
\]
As \((G_s)_{ij}\ge (G_s)_{0,n-1}\) and \(v_iv_j\ge-v_0^2=v_0v_{n-1}\), we obtain
\[
(R_s)_{ij}>(R_s)_{0,n-1}
\quad(i\ne j,\ \{i,j\}\ne\{0,n-1\}).
\tag{1}
\]
This strict comparison holds at *every resolvent scale* \(s>0\), even when the endpoint resolvent itself is negative.

**3. A single Chebyshev sign change.** Write \(h=(G_s)_{0,n-1}=1/D_n\), \(g=(G_s)_{00}=p_{n-1}/D_n\). The continuant identity
\[
p_{n-1}^2-1=D_nU_{n-2}(x)
\]
yields \(g^2-h^2=hU_{n-2}(x)\). Substitution in Sherman--Morrison gives
\[
(R_s)_{0,n-1}
=\frac{1-aU_{n-2}(1+s/2)}
{sU_{n-1}(1+s/2)[1-ar(s)]}.
\tag{2}
\]
For \(s>0\), \(U_{n-2}(1+s/2)\) is strictly increasing from \(n-1\) to infinity. Since \(a(n-1)<1\), there is exactly one \(s_0>0\) where \(U_{n-2}(1+s_0/2)=a^{-1}\). The endpoint resolvent in (2) is strictly positive on \((0,s_0)\) and strictly negative on \((s_0,\infty)\).

**4. A unique fractional generator transition.** For \(0<\alpha<1\) the spectral integral for matrix fractional powers implies, off the diagonal,
\[
(L_{n,a}^{\alpha})_{ij}=
-\frac{\sin(\pi\alpha)}{\pi}
\int_0^\infty s^\alpha(R_s)_{ij}\,ds.
\tag{3}
\]
The integrals converge: all resolvent off-diagonal entries are \(O(s^{-1})\) near zero and \(O(s^{-2})\) at infinity. In (3), inequality (1) proves that the endpoint entry is strictly the **largest** off-diagonal entry of \(L_{n,a}^{\alpha}\). Define
\[
F_a(\alpha)=\int_0^\infty s^\alpha(R_s)_{0,n-1}\,ds.
\]
Let \(A(\alpha)\) be the integral of its positive integrand on \((0,s_0)\), and \(B(\alpha)\) the integral of the negated integrand on \((s_0,\infty)\). Both are strictly positive. The ratio \(A/B\) is strictly decreasing with \(\alpha\): the logarithmic derivative of its numerator is a weighted average of \(\log s<\log s_0\), whereas that of its denominator is a weighted average of \(\log s>\log s_0\). Thus \(F_a=A-B\) has **at most one root** in \((0,1)\). It has at least one root: as \(\alpha\downarrow0\), \(L_{n,a}^{\alpha}\to I-\mathbf1\mathbf1^{\mathsf T}/n\), so the endpoint entry tends to \(-1/n\); as \(\alpha\uparrow1\), it tends to \((L_{n,a})_{0,n-1}=+a\). Continuity and (3) therefore give a unique \(\alpha_*\in(0,1)\). Furthermore, \((L_{n,a}^{\alpha})_{0,n-1}\le0\) exactly for \(0<\alpha\le\alpha_*\).

At/below the threshold, (1)--(3) imply every other off-diagonal entry of \(L_{n,a}^{\alpha}\) is strictly negative. Hence \(-L_{n,a}^{\alpha}\) is a Metzler matrix with irreducible off-diagonal graph, and its exponential is strictly positive for every \(t>0\). The zero-row-sum property makes that exponential stochastic. Above the threshold, \((L_{n,a}^{\alpha})_{0,n-1}>0\) and
\[
[e^{-tL_{n,a}^{\alpha}}]_{0,n-1}
=-t(L_{n,a}^{\alpha})_{0,n-1}+O(t^2)<0
\]
for small enough \(t>0\). In every case, the strictly positive spectral gap implies \(e^{-tL_{n,a}^{\alpha}}\to \mathbf1\mathbf1^{\mathsf T}/n\) exponentially fast, hence all entries are eventually positive permanently.

**5. Strict conductance dependence.** Equation (2) and \(U_{n-2}(1+s/2)>n-1>r(s)\) give
\[
\partial_a(R_s)_{0,n-1}
=\frac{r(s)-U_{n-2}(1+s/2)}
{sU_{n-1}(1+s/2)[1-ar(s)]^2}<0.
\]
More explicitly, the numerator in this derivative is exactly \(r(s)-U_{n-2}(1+s/2)\), with no other term. Therefore \(\partial_aF_a(\alpha)<0\). At \(\alpha=\alpha_*\), the strict separation of logarithmic weighted averages above shows \(\partial_\alpha F_a(\alpha_*)<0\). The implicit-function theorem proves \(\alpha_*\) is continuously differentiable and \(\partial_a\alpha_*=-\partial_aF/\partial_\alpha F<0\).

At \(a=0\), all path resolvent off-diagonal entries are positive, so all off-diagonal entries of \(L_{P_n}^{\alpha}\) are strictly negative for \(0<\alpha<1\); continuity forces \(\alpha_*\uparrow1\) as \(a\downarrow0\). At \(a=1/(n-1)\), (2) is strictly negative for every \(s>0\), giving a positive endpoint entry of \(L_{n,a}^{\alpha}\) for every fixed \(\alpha>0\). Continuity of spectral powers in \(a\) forces \(\alpha_*\downarrow0\) as \(a\uparrow1/(n-1)\). This establishes all assertions.

## Verification
The accompanying `verify_cycle.py` performs exact rational checks of the Chebyshev continuant identities, resolvent formula and endpoint ordering, followed by finite spectral tests of the fractional-power sign transition. Running `python verify_cycle.py` with NumPy and SciPy installed produced `VERIFICATION_OK rational=1548 spectral=4761 total=6309`. Illustrative root values, computed independently by symmetric eigendecomposition, are \(\alpha_*(4,0.5/3)\approx0.49136513\), \(\alpha_*(8,0.5/7)\approx0.32744512\), and \(\alpha_*(12,0.5/11)\approx0.27121114\). These finite checks are supplementary; steps 1--5 establish the all-size, all-parameter result.

## Relationship to prior work
Chen et al. (2020) give the effective-resistance semidefiniteness condition for one negative edge and characterize eventual exponential positivity of stable signed graph Laplacians; both statements are used here, not claimed new. Benzi and Simunec (2021) analyze fractional graph diffusion for ordinary unsigned graph Laplacians, where fractional powers of singular \(M\)-matrices remain singular \(M\)-matrices. Those hypotheses exclude the present negative-edge Laplacian. Earlier complete-network antagonistic-block calculations include the triangle case; the present theorem is stated for \(n\ge4\), when the path-closure graph has absent non-neighbor edges and is not a complete-network subfamily. Related published work on unsigned complete multipartite networks has a different critical order (one) and does not imply the present signed-cycle formula. The distinguishing contribution is the exact all-scale endpoint resolvent ordering, unique Chebyshev single-crossing threshold, and strict conductance dependence.

## Limitations
The threshold is given by a convergent one-dimensional integral, not in general by a closed elementary expression. The theorem does not identify the last negative-entry time for \(\alpha>\alpha_*\), nor does it classify arbitrary multiple-negative-edge signed cycles, nonuniform positive path conductances, or the critical strength \(a=1/(n-1)\) itself. Historical priority outside the inspected papers and indexed records remains a residual uncertainty. The numerical checker does not prove the assertions for infinitely many sizes or parameter values.

## References
1. W. Chen, D. Wang, J. Liu, Y. Chen, S. Z. Khong, T. Başar, K. H. Johansson and L. Qiu, *On Spectral Properties of Signed Laplacians with Connections to Eventual Positivity*, arXiv:2009.03581, first posted 2020-09-08, especially §IV-B and Theorem 6. https://arxiv.org/abs/2009.03581
2. M. Benzi and I. Simunec, *Rational Krylov methods for fractional diffusion problems on graphs*, BIT Numerical Mathematics 62 (2022), first online 2021-07-01, DOI:10.1007/s10543-021-00881-0, especially §3. https://doi.org/10.1007/s10543-021-00881-0
3. D. Bianchi, M. Donatelli, F. Durastante and M. Mazza, *Compatibility, embedding and regularization of non-local random walks on graphs*, arXiv:2101.00425, first posted 2021-01-02 (abstract consulted; full text not retrieved). https://arxiv.org/abs/2101.00425
