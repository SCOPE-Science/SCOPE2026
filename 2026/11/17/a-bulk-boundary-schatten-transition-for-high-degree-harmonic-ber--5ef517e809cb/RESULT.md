# A bulk–boundary Schatten transition for high-degree harmonic Bergman Toeplitz commutators

## Finding

Let \(\alpha>-1\), put \(\beta=\alpha+1\), and let \(C_m=[T_z,T_{z^m}]\) on the complex harmonic Bergman space with the normalized radial beta weight, for integers \(m\ge1\). The entire singular-value multiset of \(C_m\) is given by the absolute values of \(m\) explicit coefficients. Consequently, the asymptotic Schatten mass \(S_{m,p}=\|C_m\|_{\mathcal S_p}^{p}\) has the following sharp regimes, for every fixed \(p>0\).

Define
\[
I_{\alpha,p}=\beta^p2^{p(1-\alpha)-1}
 B\!\left(\frac{p+1}{2},1-\frac{p(1-\alpha)}2\right),
\qquad
b_{\alpha,q}=\frac{\beta}{q+\beta}
 \sqrt{\frac{\Gamma(q+\beta+1)}{\Gamma(q+1)}}.
\]
Here \(B\) denotes Euler's beta function. If \(\alpha\ge1\), then for every \(p>0\),
\[
\lim_{m\to\infty}m^{p-1}S_{m,p}=I_{\alpha,p}.
\]
If \(-1<\alpha<1\), set \(p_c=2/(1-\alpha)\). Then
\[
\begin{array}{ll}
0<p<p_c:&\displaystyle\lim_{m\to\infty}m^{p-1}S_{m,p}=I_{\alpha,p},\\[4pt]
p=p_c:&\displaystyle\lim_{m\to\infty}\frac{m^{p-1}}{\log m}S_{m,p}=2\beta^p,\\[6pt]
p>p_c:&\displaystyle\lim_{m\to\infty}m^{p\beta/2}S_{m,p}
=2\sum_{q=1}^{\infty}b_{\alpha,q}^{p}.
\end{array}
\]
The series in the last line converges. These regimes reflect a transition from a continuum of bulk angular modes to a pair of summable boundary layers, with a harmonic borderline. In the unweighted case \(\alpha=0\), \(p_c=2\); at \(p=2\), \(S_{m,2}\sim2\log(m)/m\), whereas for \(p>2\), \(m^{p/2}S_{m,p}\to2(\zeta(p/2)-1)\).

## Assumptions and scope

On the open unit disk \(\mathbb D\), use \(dA=\pi^{-1}\,dx\,dy\) and \(dA_\alpha=(\alpha+1)(1-|z|^2)^\alpha dA\). Write \(h^2_\alpha\) for the complex Hilbert space of harmonic elements in \(L^2(dA_\alpha)\), \(Q_\alpha\) for its orthogonal projection, and \(T_f=Q_\alpha M_f|_{h^2_\alpha}\) for a bounded symbol \(f\). The commutator convention is \([A,B]=AB-BA\). For every integer \(j\ge0\), set
\[
\mu_j=\int_{\mathbb D}|z|^{2j}dA_\alpha
=\frac{\Gamma(\beta+1)\Gamma(j+1)}{\Gamma(j+\beta+1)}.
\]
The normalized Fourier-harmonic basis has \(e_j=z^j/\sqrt{\mu_j}\) for \(j\ge0\) and \(e_{-j}=\overline z^{\,j}/\sqrt{\mu_j}\) for \(j\ge1\). Schatten exponents \(p<1\) are interpreted using the usual Schatten quasi-norm and its \(p\)-power sum. The limits hold with \(\alpha\) and \(p\) fixed while \(m\to\infty\).

## Proof

**Exact finite-rank reduction.** For \(r\ge1\) and signed integer \(j\), both the input and output of \(T_{z^r}e_j\) have a single angular frequency \(j+r\). The coefficient is
\[
T_{z^r}e_j=\begin{cases}
\sqrt{\mu_{j+r}/\mu_j}\,e_{j+r},&j\ge0,\\
\sqrt{\mu_{-j}/\mu_{-j-r}}\,e_{j+r},&j<-r,\\
\mu_r(\mu_{-j}\mu_{r+j})^{-1/2}e_{j+r},&-r\le j<0.
\end{cases}
\]
These are exact orthogonal-projection integrals. The moments satisfy \(\mu_n/\mu_{n-1}=n/(n+\beta)\). Applying the displayed rule twice shows that \(C_me_j=0\) unless \(-m\le j\le-1\). For \(1\le q\le m\), subtraction and the moment ratio give
\[
C_me_{-q}=c_{m,q}e_{m+1-q},\qquad
c_{m,q}=\frac{\beta\mu_m(m+1-2q)}
{(q+\beta)(m-q+1+\beta)\sqrt{\mu_q\mu_{m-q+1}}}.
\]
The input and output vectors in this formula are orthonormal families. Therefore the complete singular-value multiset, including any zero, is exactly \(\{|c_{m,q}|:1\le q\le m\}\), and \(C_m^2=0\). The coefficients are paired by \(q\mapsto m+1-q\). Hence \(\operatorname{rank}C_m=m\) when \(m\) is even and \(m-1\) when \(m\) is odd. In particular \(C_1=0\).

**Bulk and boundary asymptotics.** The gamma ratio gives \(\mu_j\sim\Gamma(\beta+1)j^{-\beta}\), with two-sided bounds \(\mu_j\asymp_\beta(j+1)^{-\beta}\). For each fixed \(t\in(0,1)\), uniformly over compact subintervals, the coefficients satisfy
\[
m\,c_{m,\lfloor mt\rfloor}\longrightarrow
\beta(1-2t)[t(1-t)]^{\beta/2-1}.
\]
For every fixed positive integer \(q\),
\[
m^{\beta/2}c_{m,q}\longrightarrow b_{\alpha,q}.
\]
The paired right endpoint has the same absolute value. More importantly, the moment bounds applied to the exact coefficient give, with a constant depending only on \(\beta\),
\[
|c_{m,q}|\le C_\beta m^{-\beta/2}(q+1)^{\beta/2-1},
\quad 1\le q\le m/2.
\]
The same estimate holds with \(q\) replaced by \(m+1-q\) on the other half.

If \(1+p(\beta/2-1)>0\), the displayed estimate makes the rescaled mass of \(q\le\varepsilon m\) bounded by a constant times \(\varepsilon^{1+p(\beta/2-1)}\). The middle is a Riemann sum. Thus
\[
m^{p-1}S_{m,p}\to \beta^p\int_0^1 |1-2t|^p
[t(1-t)]^{p(\beta/2-1)}dt.
\]
The substitution \(x=|1-2t|\) evaluates the integral as \(I_{\alpha,p}\). This covers all \(p>0\) for \(\beta\ge2\), and precisely \(p<p_c\) when \(0<\beta<2\).

If \(0<\beta<2\) and \(p>p_c\), the endpoint bound is summable after multiplication by \(m^{p\beta/2}\), since \(p(\beta/2-1)<-1\). Dominated convergence on the two symmetric halves gives exactly \(2\sum_{q\ge1}b_{\alpha,q}^p\). The asymptotic \(b_{\alpha,q}\sim\beta q^{\beta/2-1}\) proves convergence and shows why the threshold is sharp.

Finally let \(p=p_c\), so \(p\beta/2=p-1\). For \(1\ll q\le\varepsilon m\) and fixed small \(\varepsilon>0\), the exact formula, uniformly in that range, yields
\[
m^{\beta/2}|c_{m,q}|=(1+O_\beta(\varepsilon)+o_m(1))b_{\alpha,q}.
\]
Since \(b_{\alpha,q}^p\sim\beta^p/q\), one endpoint contributes \(\beta^p\log(m)(1+O_\beta(\varepsilon))+o(\log m)\). The central range \(\varepsilon m<q<(1-\varepsilon)m\) contributes \(O_{\beta,p,\varepsilon}(1)\) after multiplication by \(m^{p-1}\), and the opposite endpoint has the same coefficient. Taking first \(m\to\infty\) and then \(\varepsilon\downarrow0\) proves the critical limit.

For \(\alpha=0\), \(\mu_j=1/(j+1)\) and the coefficient simplifies to \((m+1-2q)/((m+1)\sqrt{(q+1)(m-q+2)})\), giving \(b_{0,q}=(q+1)^{-1/2}\). This gives the stated zeta expression. In fact, an exact finite identity is
\[
\|C_m\|_{\mathcal S_2}^2
=\frac{2(m+3)(H_{m+1}-1)-4m}{(m+1)^2},
\qquad H_n=\sum_{j=1}^n \frac1j,
\]
which independently confirms the critical factor \(2\).

## Verification

The included standalone `checker.py` computes both ordered Toeplitz products directly on every signed Fourier mode in a finite window, rather than using the asserted commutator formula. It checks the formula at six positive beta parameters, degrees \(1\) through \(80\), and the exact unweighted Hilbert–Schmidt identity for degrees \(1\) through \(200\). It records 28,280 passed assertions. These are finite diagnostic checks; the limits and the three regimes are established by the estimates in the proof, not inferred from numerical experiments. Run using `python3 checker.py` with the Python standard library.

## Relationship to prior work

Cui, Huang, Lu and Zu (2026) characterize finite-rank harmonic Bergman Toeplitz commutators with bounded harmonic symbols, including analytic pairs, and prove their square-zero property. Their statement does not quantify the singular-value mass as monomial degree grows or consider the weighted beta family here. Dong and Zhou (2014) determine canonical finite-rank formulas and ranks for quasihomogeneous Toeplitz commutators on the unweighted harmonic Bergman space; the exact unweighted finite-rank mode formula here is not asserted as an independent discovery of finite-rank structure. The new classification concerns the weight-dependent high-degree bulk/boundary Schatten asymptotics, including sharp logarithmic critical behavior. Other fixed-degree harmonic Bergman self-commutator results concern non-finite-rank selfadjoint operators, and do not imply the growing-degree three-regime mass law. The literature comparison is a best-knowledge priority assessment, not an absolute novelty guarantee.

## Limitations

The sharp limits require fixed \(\alpha\) and \(p\); no uniform joint asymptotic is claimed as either approaches the critical curve. All individual operators in this family are finite rank, so each belongs to every \(\mathcal S_p\): the critical exponent describes *large-degree growth of Schatten mass*, not individual operator membership. This work does not classify symbols beyond the chosen monomial pair, establish rates in \(m\), or claim priority over any inaccessible equivalent formulation. Independent mathematical audit has not been performed.

## References

1. P. Cui, Z. Huang, Y. Lu, C. Zu, *Finite-rank Toeplitz commutators on the harmonic Bergman space*, arXiv:2611.08988v1 (first public November 6, 2026), https://arxiv.org/html/2611.08988v1.
2. X.-T. Dong, Z.-H. Zhou, *Ranks of Commutators and Generalized Semicommutators of Quasihomogeneous Toeplitz Operators*, arXiv:1411.0213v3, https://arxiv.org/abs/1411.0213.
3. Y. Chen, H. Koo, Y. J. Lee, *Ranks of commutators of Toeplitz operators on the harmonic Bergman space*, Integral Equations Operator Theory 75 (2013), 31–38, DOI:10.1007/s00020-012-2020-6.
