# An exponent-four strongly small-2 spectrum with a singular full-support witness

## Finding

Let \(G=(\mathbb Z/4\mathbb Z)^{\mathbb N}\), with normalized Haar measure \(m\), and let \(\Gamma=\widehat G\). There exists an explicit proper spectral subset \(E\subsetneq\Gamma\) and, for every fixed \(0<a\le 1/2\), a finite complex Borel measure \(\mu_a\) with the following properties:

\[
E\cap(-E)=\{0\},\qquad
|\alpha|*|\beta|\ll m\quad\text{for all }\alpha,\beta\in M_E(G),
\]
\[
\mu_a(G)=1,\qquad \mu_a\perp m,\qquad
\operatorname{supp}\widehat\mu_a=E,\qquad
1\le\|\mu_a\|\le e^{a/6},
\]
\[
\mu_a*\mu_a\in L^2(G),\qquad
\|\mu_a*\mu_a\|_2^2
=\prod_{j=1}^{\infty}\left(1+\frac{a^4}{16^j}\right).
\]

Here \(M_E(G)\) is the space of finite complex measures whose Fourier–Stieltjes transform vanishes outside \(E\). In particular, \(E\) is **strongly small-2** but **not a Riesz set**: every pair of spectral measures has absolutely continuous convolution of their total variations, while \(M_E(G)\) contains a nonzero singular measure. This gives such a construction on a compact group of pure exponent four, in contrast to the previously constructed exponent-six and odd-prime-exponent groups.

## Assumptions and scope

For any compact abelian group \(H\), use \(\widehat\sigma(\gamma)=\int_H\overline{\gamma(x)}\,d\sigma(x)\). Write \(\overline\sigma\) for complex conjugation of a measure **without reflection**, and \(|\sigma|\) for its total variation. A Riesz set satisfies \(M_E(H)=L^1_E(H)\); strong small-2 means \(|\alpha|*|\beta|\ll m_H\) for all \(\alpha,\beta\in M_E(H)\).

We first construct on the equivalent compact product
\[
G'=\prod_{j\ge1}H_j,\qquad H_j=(\mathbb Z/4\mathbb Z)^{2j+1},
\]
then reindex the countably many order-four coordinates to identify \(G'\) with \(G\). The construction depends only on the chosen real constant \(a\in(0,1/2]\); no positivity is claimed for the complex witness \(\mu_a\).

## Proof

**1. An explicit reversible flat sign on sixteen points.** Let \(W=(\mathbb Z/4\mathbb Z)^2\) and set
\[
D=\{(0,0),(0,1),(0,3),(1,0),(3,0),(2,2)\},\quad
b=1-2\mathbf1_D:W\to\{\pm1\}.
\]
The set \(D\) is invariant under negation. For \((u,v)\in W\), its unnormalized character sum equals
\[
T(u,v)=1+(-1)^{u+v}+2\cos(\pi u/2)+2\cos(\pi v/2).
\]
If \((u,v)=(0,0)\), this equals six. For any other pair it equals \(2\) or \(-2\): if exactly one of \(u,v\) is odd, the first two terms cancel and one cosine term is \(\pm2\); if both are odd the sum is two; if both are even but not both zero the sum is \(2\) or \(-2\). Hence the normalized Fourier transform of \(b\) obeys
\[
\widehat b(u,v)=\frac{16\mathbf1_{(u,v)=(0,0)}-2T(u,v)}{16}
\in\left\{-\frac14,\frac14\right\},
\quad \widehat b(-u,-v)=\widehat b(u,v)\in\mathbb R.
\]
Its value at zero is \(1/4\). This is the only finite combinatorial ingredient needed.

**2. Flat real tensor factors.** Put \(W_j=W^j\cong(\mathbb Z/4\mathbb Z)^{2j}\), \(q_j=4^j\), and
\[
b_j(w_1,\ldots,w_j)=\prod_{\ell=1}^j b(w_\ell).
\]
Every normalized Fourier coefficient of \(b_j\) is \(s_j(z)/q_j\), with \(s_j(z)\in\{\pm1\}\) satisfying \(s_j(-z)=s_j(z)\) and \(s_j(0)=1\). In particular \(|W_j|=q_j^2\) and \(b_j^2=1\).

**3. Local cancellation and an antipodal-free spectrum.** Regard \(H_j=(\mathbb Z/4\mathbb Z)\times W_j\) and write a point as \((t,w)\). Define
\[
\begin{aligned}
g_j(t,w)&=a\,b_j(w)\cos(\pi t/2),\\
p_j(t,w)&=1+g_j(t,w),\\
h_j(t,w)&=a q_j\mathbf1_{\{0\}}(w)\sin(\pi t/2),\\
f_j(t,w)&=p_j(t,w)+i h_j(t,w).
\end{aligned}
\]
The density \(p_j\) is strictly positive, since \(p_j\ge1-a\), and both \(p_j\) and \(f_j\) have Haar mean one. Exact averaging gives
\[
\|f_j-p_j\|_{L^1(H_j)}=\frac{a}{2q_j},\quad
\int g_j\,dm_j=0,\quad
\int g_j^2\,dm_j=\frac{a^2}{2}.
\]
The Fourier transform of the sine in the order-four coordinate is \(1/(2i)\) at frequency \(1\) and \(-1/(2i)\) at frequency \(-1\). Because the normalized transform of \(\mathbf1_{\{0\}}\) on \(W_j\) is \(q_j^{-2}\), cancellation gives, for every \(z\in\widehat W_j\),
\[
\widehat f_j(1,z)=\frac{a}{2q_j}\bigl(s_j(z)+1\bigr),\qquad
\widehat f_j(-1,z)=\frac{a}{2q_j}\bigl(s_j(z)-1\bigr).
\]
All remaining nonconstant coefficients are zero and \(\widehat f_j(0,0)=1\). Thus
\[
S_j:=\operatorname{supp}\widehat f_j
=\{(0,0)\}\cup\{(s_j(z),z):z\in\widehat W_j\},
\quad \widehat f_j(s_j(z),z)=\frac{a}{q_j}s_j(z).
\]
Here \(s_j(z)\) is interpreted as the residue \(1\) or \(-1\) modulo four. Since \(s_j(-z)=s_j(z)\) and \(1\not\equiv-1\pmod4\), we have \(S_j\cap(-S_j)=\{0\}\). In addition,
\[
\sum_{\gamma\in\widehat H_j\setminus\{0\}}|\widehat f_j(\gamma)|^4
=q_j^2\left(\frac a{q_j}\right)^4=\frac{a^4}{q_j^2}.
\]

**4. Singular infinite product with exact full Fourier support.** Let \(m_j\) be Haar probability on \(H_j\) and put
\[
\rho=\bigotimes_{j\ge1}p_jm_j,\qquad m'=\bigotimes_{j\ge1}m_j.
\]
Under either probability, the bounded observables \(g_j\) are independent. Their means are zero under \(m'\), but \(a^2/2\) under \(\rho\), because \(\int g_jp_j\,dm_j=\int g_j^2\,dm_j\). Chebyshev's inequality and the first Borel–Cantelli lemma on dyadic partial-sum lengths imply that the averages \(2^{-k}\sum_{j\le2^k}g_j\) tend almost surely to these different constants. Thus \(\rho\perp m'\).

As \(\sum_j\|f_j-p_j\|_1=(a/2)\sum_{j\ge1}4^{-j}=a/6\), the densities \(R_n=\prod_{j=1}^n f_j/p_j\) form a Cauchy sequence in \(L^1(\rho)\). Indeed, expanding consecutive differences and using independence bounds their total \(L^1\) variation by the summable perturbations times \(\prod_j(1+a/(2q_j))\le e^{a/6}\). Let \(R\) be the limit and \(\mu_a=R\rho\). Its first \(n\) block marginals have densities \(\prod_{j=1}^n f_j\); hence \(\mu_a(G')=1\), \(\mu_a\ll\rho\perp m'\), and \(1\le\|\mu_a\|\le e^{a/6}\).

Define
\[
E=\left\{\gamma\in\bigoplus_{j\ge1}\widehat H_j:
\gamma_j\in S_j\ \text{for every }j\right\}.
\]
For each finitely supported \(\gamma\), product-factorization of its Fourier coefficient gives \(\widehat\mu_a(\gamma)=\prod_j\widehat f_j(\gamma_j)\), so its **exact** nonzero Fourier support is \(E\). Since each \(S_j\cap(-S_j)=\{0\}\), \(E\cap(-E)=\{0\}\); properness follows, for instance, because a nonzero local frequency \((2,0)\) never belongs to \(S_j\). Finally, Tonelli and Parseval give
\[
\sum_{\gamma\in\Gamma}|\widehat\mu_a(\gamma)|^4
=\prod_{j\ge1}\left(1+\frac{a^4}{16^j}\right)<\infty.
\]
The Fourier coefficients of \(\mu_a*\mu_a\) are \(\widehat\mu_a(\gamma)^2\). The \(L^2\) Fourier synthesis theorem and uniqueness for finite measures therefore show that \(\mu_a*\mu_a\in L^2(G')\) with precisely the displayed norm.

**5. Strong small-2 for every spectral measure.** Fix \(\gamma\in\Gamma\). If \(\eta\in E\cap(\gamma-E)\), then at every block where \(\gamma_j=0\), both \(\eta_j\) and \(-\eta_j\) lie in \(S_j\), forcing \(\eta_j=0\). There are only finitely many remaining blocks and finitely many choices within them. Thus \(E\cap(\gamma-E)\) is finite.

For arbitrary \(\alpha,\beta\in M_E(G')\), the Fourier support of \((\chi_u\alpha)*(\chi_v\overline\beta)\) lies in the finite intersection \((u+E)\cap(v-E)\), for each pair of characters \(u,v\). A measure with finite Fourier support is a trigonometric polynomial times Haar measure, by Fourier uniqueness. Approximate the polar factors needed to recover \(|\alpha|\) and \(|\beta|\) with trigonometric polynomials in their respective variation-measure \(L^1\) spaces. Finite linear combinations of these character-twisted convolutions converge in total variation to \(|\alpha|*|\beta|\). Since \(L^1(G')m'\) is closed in the measure norm, \(|\alpha|*|\beta|\ll m'\). On the other hand, \(\mu_a\in M_E(G')\) is nonzero and singular, so \(E\) is not Riesz. Reindexing coordinates transfers everything to \(G\). \(\square\)

## Verification

The standalone Python 3 program `CHECK.py` uses only integer/Gaussian-integer arithmetic. It verifies the explicit sixteen-point difference set and its real flat Fourier sign, then computes **every** Fourier coefficient of the local complex density \(f_j\) for \(j=1,2,3\) (a total of 17,472 local frequencies) at \(a=1/2\), and checks exact support and antipodal symmetry. Run `python3 CHECK.py` in the directory containing this file. Expected output:

```text
CHECK_OK difference_set_order=16 exact_factor_levels=3 gaussian_integer_Fourier_coefficients=17472
```

These are finite checks of the explicit local identity. Infinite-product convergence, singularity, and the universal strong small-2 property are proved above, not inferred from tests.

## Relationship to prior work

Ohrysko, *Strongly small-2 sets which are not Riesz sets*, arXiv:2609.12628 (first posted September 11, 2026), proves the finite-intersection criterion and the summably perturbed product-measure mechanism used here. Its displayed examples have ambient groups \((\mathbb Z/6\mathbb Z)^{\mathbb N}\) and \((\mathbb Z/p\mathbb Z)^{\mathbb N}\) with odd prime \(p\). The present contribution is the **pure exponent-four case**, supplied by an explicit reversible flat sign on \((\mathbb Z/4\mathbb Z)^2\) that permits the same antipodal cancellation without any odd-order factor. This case is not implied by a change of coordinates in those ambient groups: they have different character-group torsion.

Lau and Ülger, *Small-2 Sets Are Riesz Sets*, arXiv:2606.30570 (first posted June 29, 2026), asserts a universal implication that is challenged by Ohrysko's explicit examples. The proof here does not use that assertion, and supplies independent details for the exponent-four finite factor and the relevant infinite construction. Reversible Hadamard difference sets are a classical combinatorial topic; the sixteen-point sign is verified directly rather than presented as a newly discovered difference set.

## Limitations

This is an existence theorem for the countable product of cyclic groups of order four. It does not establish such an example on the exponent-two Walsh group, and does not classify all strongly small-2 subsets of the order-four product. Its singular witnesses are complex, not positive probability measures. The general product-perturbation and finite-intersection principles, as well as the general notion of a reversible Hadamard difference set, predate this result. Earlier unindexed constructions under different terminology remain an originality risk; no independent audit or publication-priority certificate is claimed.

## References

1. P. Ohrysko, *Strongly small-2 sets which are not Riesz sets*, arXiv:2609.12628, first public version 2026-09-11, https://arxiv.org/abs/2609.12628.
2. A. To-Ming Lau and A. Ülger, *Small-2 Sets Are Riesz Sets*, arXiv:2606.30570, first public version 2026-06-29, https://arxiv.org/abs/2606.30570.
3. J. A. Davis, *Almost Difference Sets and Reversible Divisible Difference Sets*, Archiv der Mathematik 59 (1992), 595–602, https://doi.org/10.1007/BF01194853. Background for reversible difference sets, not required by the proof.
4. H. A. MacLean, *Riesz sets and a theorem of Bochner*, Pacific Journal of Mathematics 113 (1984), 115–135, https://doi.org/10.2140/pjm.1984.113.115. Earlier spectral-intersection context, via reference [1].
