# Exact nullity and sharp Schatten boundary for mixed harmonic Bergman monomial commutators

## Finding

For each real \(\alpha>-1\) and distinct positive integers \(m,n\), let \(T_k\) denote the harmonic Bergman Toeplitz operator with symbol \(z^k\), and put
\[
C_{m,n}=T_m^*T_n-T_nT_m^*.
\]
Then \(C_{m,n}\) is a nonzero compact infinite-rank operator, with **exact kernel dimension**
\[
\dim\ker C_{m,n}=\operatorname{codim}\overline{\operatorname{Ran}C_{m,n}}=|m-n|+1.
\]
Its nonzero singular values occur in equal pairs and satisfy the **sharp asymptotic law**
\[
\lim_{N\to\infty}N^2s_N(C_{m,n})=4(\alpha+1)mn.
\]
Consequently, for every real \(p>0\),
\[
C_{m,n}\in\mathcal S_p\quad\Longleftrightarrow\quad p>\tfrac12,
\qquad C_{m,n}\in\mathcal S_{1/2,\infty}\setminus\mathcal S_{1/2},
\]
and its critical logarithmic singular-value sum has the exact limit
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{k=1}^N s_k(C_{m,n})^{1/2}
=2\sqrt{(\alpha+1)mn}.
\]
The theorem includes all unequal monomial degrees and all standard radial power weights. It does not include the equal-degree selfcommutator case.

## Assumptions and scope

Let \(\mathbb D\) be the unit disk, let \(dA(z)/\pi\) be normalized Euclidean area, and equip the complex-valued harmonic Bergman space \(h^2_\alpha\) with the probability measure
\[
d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dA(z)/\pi,
\quad \alpha>-1.
\]
Denote the orthogonal projection from \(L^2(\mu_\alpha)\) onto \(h^2_\alpha\) by \(Q_\alpha\). For \(k\ge1\), define \(T_k=Q_\alpha M_{z^k}|_{h^2_\alpha}\). All these operators have norm at most one. Write \(s_N\) for the singular values in nonincreasing order, each counted with multiplicity, and \(\mathcal S_p\) for the Schatten ideal (a quasi-ideal if \(0<p<1\)). The weak ideal \(\mathcal S_{1/2,\infty}\) means \(\sup_{N\ge1}N^2s_N<\infty\).

Let \(a_r=\Gamma(\alpha+2)\Gamma(r+1)/\Gamma(r+\alpha+2)\) for nonnegative integers \(r\), so \(a_0=1\). An orthonormal basis, indexed by all integers, is
\[
e_j=\begin{cases}z^j/\sqrt{a_j},&j\ge0,\\
\overline z^{-j}/\sqrt{a_{-j}},&j<0.\end{cases}
\]
For integers \(j\) and \(k\ge1\), set
\[
w_j^{(k)}=\begin{cases}
\sqrt{a_{j+k}/a_j},&j\ge0,\\
\sqrt{a_{-j}/a_{-j-k}},&j\le-k,\\
a_k/\sqrt{a_{-j}a_{j+k}},&-k<j<0.
\end{cases}
\]
The exact singular values are the positive members, with multiplicity, of \(\{|c_j|:j\in\mathbb Z\}\), where
\[
c_j=w_j^{(n)}w_{j+n-m}^{(m)}-w_{j-m}^{(m)}w_{j-m}^{(n)}.
\]
This coefficient formula makes the statement fully computationally reproducible for any specified parameters.

## Proof

**1. A bilateral weighted-shift identity.** Orthogonality of the Fourier frequencies of the radial measure and the monomial norms \(\|z^r\|^2=a_r\) show directly that
\[
T_ke_j=w_j^{(k)}e_{j+k}.
\]
For \(-k<j<0\), the Fourier frequency changes sign; its projection coefficient is \(a_k/\sqrt{a_{-j}a_{j+k}}\), establishing the middle case rather than extrapolating either outer formula. Taking adjoints gives
\[
C_{m,n}e_j=c_j e_{j+n-m}.
\]
Thus \(C_{m,n}^*C_{m,n}\) is diagonal with eigenvalues \(|c_j|^2\), so these coefficients determine **all** singular values and the kernel exactly. Moreover, the closure of the range is spanned by the output basis vectors with nonzero coefficients, so its codimension is the same as the kernel dimension.

**2. Symmetry, the exact zero interval, and strict signs.** The weights satisfy
\[
w_j^{(k)}=w_{-k-j}^{(k)},\qquad c_{m-n-j}=-c_j.
\]
The first identity follows directly in each of the three cases defining \(w\), and substitution proves the second. This zero-reflection phenomenon is closely related to the known symmetry-number result for quasihomogeneous commutators; the present proof also establishes the strict signs and exact nullity.

It is enough to take \(1\le m<n\), and put \(d=n-m\). For \(-d\le j\le0\), both products in the definition of \(c_j\) equal
\[
\frac{a_n}{\sqrt{a_{-j}a_{d+j}}};
\]
hence \(c_j=0\). For \(1\le j<m\), a direct substitution yields
\[
c_j=\frac{a_{j+n}a_{m-j}-a_m a_n}
{a_{m-j}\sqrt{a_j a_{j+d}}}.
\]
For \(j\ge m\), it yields
\[
c_j=\frac{a_{j+n}a_{j-m}-a_j a_{j+d}}
{a_{j-m}\sqrt{a_j a_{j+d}}}.
\]
The function \(F(x)=\log\Gamma(\alpha+2)+\log\Gamma(x+1)-\log\Gamma(x+\alpha+2)\) has
\[
F''(x)=\psi_1(x+1)-\psi_1(x+\alpha+2)>0,
\qquad x\ge0,
\]
because the trigamma function \(\psi_1\) decreases strictly on the positive axis and \(\alpha+1>0\). In each of the two displayed numerators, the first two indices and the last two have the same sum, but the first pair is strictly more spread out. Strict convexity of \(F\) therefore makes both numerators positive. We conclude \(c_j>0\) for \(j\ge1\), while reflection gives \(c_j<0\) for \(j\le-d-1\). Hence the *only* zero indices are \(-d,-d+1,\ldots,0\), exactly \(d+1\) of them, and every nonzero singular value occurs twice. For \(m>n\), use \(C_{m,n}=C_{n,m}^*\): then precisely \(j=0,\ldots,m-n\) are zeros, with the same multiplicity conclusion. This proves the nullity and strict nonvanishing.

**3. Sharp coefficient decay.** Take \(1\le m<n\), \(d=n-m\), and \(j\ge m\). The preceding formulas can be rearranged as
\[
c_j=\frac{\sqrt{a_ja_{j+d}}}{a_{j-m}}
\left(\exp[ F(j+n)+F(j-m)-F(j)-F(j+d)]-1\right).
\]
For fixed \(m,n,\alpha\), asymptotics of the gamma and trigamma functions give
\[
F''(x)=\frac{\alpha+1}{x^2}+O(x^{-3}),
\]
and a Taylor expansion with the cancellation of linear terms yields
\[
F(j+n)+F(j-m)-F(j)-F(j+d)
=\frac{(\alpha+1)mn}{j^2}+O(j^{-3}).
\]
The prefactor tends to \(1\), whence
\[
\lim_{j\to\infty}j^2c_j=(\alpha+1)mn>0.
\]
By exact reflection there are two such positive-modulus tails. Equivalently, their distribution function satisfies
\[
\#\{j:|c_j|>t\}\sim2\sqrt{(\alpha+1)mn/t}
\qquad(t\downarrow0).
\]
This counting asymptotic uses only upper and lower comparisons to \(\bigl((\alpha+1)mn\pm\varepsilon\bigr)/j^2\), so it does not assume eventual monotonicity. Inverting it proves \(N^2s_N\to4(\alpha+1)mn\). The case \(m>n\) follows from taking adjoints.

**4. Schatten and critical summation.** Since the coefficients are nonzero on both infinite tails and \(s_N\sim4(\alpha+1)mn/N^2\), the operator is compact, nonzero, of infinite rank, and belongs to \(\mathcal S_p\) exactly for \(2p>1\). At \(p=1/2\), the weak ideal bound holds but the strong sum diverges. Finally,
\[
s_N^{1/2}=\frac{2\sqrt{(\alpha+1)mn}+o(1)}{N},
\]
and Cesàro–harmonic summation gives the asserted logarithmic coefficient. No finite truncation is used to prove the infinite statements.

## Verification

The proof can be reproduced with the displayed gamma-moment and weighted-shift formulas, strict convexity of \(F\), and counting-function inversion. The separately embedded `CHECK.py` evaluates these formulas without outside numerical libraries, testing multiple nonintegral weights and unequal degree pairs for the exact zero indices, signs, index-reflection symmetry, and large-index coefficient. It is a finite diagnostic, not a substitute for the infinite proof. Additional high-precision tests used noninteger weights close to \(-1\) and randomly varied degrees; they are not part of the mathematical proof.

As an elementary check at \(\alpha=0\) and \(1\le m<n\), the strictly positive upper coefficients simplify to
\[
c_j=\begin{cases}
\dfrac{j(j+n-m)\sqrt{(j+1)(j+n-m+1)}}{(j+n+1)(m+1)(n+1)},&1\le j<m,\\[4pt]
\dfrac{mn}{(j+n+1)\sqrt{(j+1)(j+n-m+1)}},&j\ge m.
\end{cases}
\]
This independently exhibits the sharp \(mn/j^2\) tail constant when \(\alpha=0\).

## Relationship to prior work

Tian, Wang, and Zhao (2026) prove qualitative rigidity of commuting analytic and co-analytic Toeplitz operators on the unweighted harmonic Bergman space; the present result is a quantitative mixed-monomial counterpart, including weighted spaces. Dong and Zhou (2012/2013) establish a symmetry-number theorem for quasihomogeneous commutators, and Dong and Zhou (2014) classify certain finite-rank commutators. The reflection of possible zero indices and finite-rank questions are therefore **not claimed as new in isolation**. Kong, Qu, and Tong (2021) treat commutation and semicommutation on the weighted harmonic Bergman space, including normality questions. The exact unequal-degree nullity, all-coefficient strict sign determination, full paired singular-value description, sharp \(N^{-2}\) constant, and \(p=1/2\) boundary are the proposed additions. A classical general commutator-symbol theorem may imply portions of the asymptotic; no publication-priority guarantee is made.

## Limitations

The theorem concerns one complex variable, power-weight harmonic Bergman spaces, and two **distinct positive monomial degrees**. It does not classify general analytic symbols, higher-dimensional domains, arbitrary radial weights, or the equal-degree selfcommutator case. The leading singular-value asymptotic is proved, not a uniform remainder bound in \(\alpha,m,n\). The qualitative zero-set symmetry was known; only the specific stated refinement is advanced as new. Publication priority requires independent literature assessment.

## References

1. Xianchi Tian, Jiawei Wang, Xianfeng Zhao, *Commuting analytic and co-analytic Toeplitz operators on the harmonic Bergman space*, arXiv:2609.14635 (first public September 13, 2026), primary MSC2020 47B35; https://arxiv.org/abs/2609.14635 .
2. Xing-Tang Dong and Ze-Hua Zhou, *Commuting Quasihomogeneous Toeplitz Operators on the Harmonic Bergman Space*, Complex Analysis and Operator Theory 7 (2013), 1267–1285; published online February 22, 2012; DOI:10.1007/s11785-012-0223-0 .
3. Xing-Tang Dong and Ze-Hua Zhou, *Ranks of Commutators and Generalized Semicommutators of Quasihomogeneous Toeplitz Operators*, arXiv:1411.0213 (2014); https://arxiv.org/abs/1411.0213 .
4. Linghui Kong, Shuang Qu, Shan Tong, *Commuting and semi-commuting Toeplitz operators on the weighted harmonic Bergman space*, Operators and Matrices 15 (2021), 163–174; DOI:10.7153/oam-2021-15-12 .
