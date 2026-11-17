# A two-ray geometric eigenvalue law for a nilpotent rank-one perturbation of a compact quasinilpotent shift

## Finding

For every fixed real \(0<q<1\), the compact quasinilpotent unilateral weighted shift and square-zero rank-one operator constructed below give a compact operator \(T_\alpha\), for *every* \(\alpha\in\mathbb C\setminus\{0\}\), whose nonzero eigenvalues asymptotically occupy exactly two simple conjugate-looking geometric rays. More precisely, set

\[
Q_r=\prod_{m=1}^{r}(1-q^{2m}),\qquad Q_0=1,\qquad Q_\infty=\prod_{m=1}^{\infty}(1-q^{2m})>0.
\]

There exists an integer \(j_0=j_0(q,\alpha)\) such that for every integer \(j\ge j_0\), exactly two eigenvalues, counted with algebraic multiplicity, lie in the annulus

\[
q^{j+1/2}<|\lambda|<q^{j-1/2}.
\]

They are simple and can be uniquely labelled \(\lambda_{j,+}\) and \(\lambda_{j,-}\) by their limiting imaginary directions. With \(c=\alpha^{-1}\), each has the asymptotic expansion

\[
\boxed{\displaystyle
\lambda_{j,\pm}=\mp i q^j
+\frac{(-1)^{j-1}c}{2Q_{j-1}Q_\infty}\,q^{j(j+3)}
+O_{q,c}\!\left(jq^{2j(j+1)+3j}\right).}
\]

In particular, for every positive real \(\alpha\), both eigenvalues at scale \(q^j\) have real part of sign \((-1)^{j-1}\) for all sufficiently large \(j\): the two near-imaginary rays have an alternating, superexponentially small common transverse displacement. If \(N_\alpha(\varepsilon)\) counts nonzero eigenvalues of modulus at least \(\varepsilon\), with algebraic multiplicity, then

\[
\boxed{\displaystyle
N_\alpha(\varepsilon)=\frac{2\log(1/\varepsilon)}{\log(1/q)}+O_{q,\alpha}(1)
\quad(\varepsilon\downarrow0).}
\]

## Assumptions and scope

Work over complex \(H=\ell^2(\mathbb N)\) with the canonical orthonormal basis \((e_j)_{j\ge1}\). Fix \(0<q<1\). Define

\[
Se_j=q^{j/4}e_{j+1}\quad(j\ge1),
\qquad F x=\varphi(x)e_1,
\qquad \varphi(x)=\sum_{k=1}^{\infty}\gamma_{2k+1}x_{2k+1},
\]

with coefficients

\[
\gamma_1=0,\quad\gamma_{2k}=0,\quad
\gamma_{2k+1}=\frac{q^{(2k^2-5k)/4}}{Q_{k-1}}\quad(k\ge1),
\qquad T_\alpha=S+\alpha F\quad(\alpha\ne0).
\]

Since \(Q_{k-1}\ge Q_\infty>0\) and the exponent in \(\gamma_{2k+1}\) grows quadratically, the coefficient sequence is absolutely summable. Thus \(F\) is a bounded rank-one operator; \(\varphi(e_1)=0\) gives \(F^2=0\). The shift \(S\) is compact and quasinilpotent: its powers have the exact norms

\[
\|S^n\|=q^{n(n+1)/8},\quad n\ge1.
\]

No assertion about finite-index exceptional eigenvalues, universal uniformity as \(\alpha\to0\), or optimal constants in the remainder is made.

## Proof

**1. Exact resolvent determinant.** Put \(W_m=\prod_{r=1}^m q^{r/4}=q^{m(m+1)/8}\). The Neumann series is valid for every \(\lambda\ne0\), because \(S\) is quasinilpotent. The rank-one resolvent factorization yields

\[
\lambda\in\sigma(T_\alpha)\setminus\{0\}
\ \Longleftrightarrow\ 1=\alpha\varphi((\lambda I-S)^{-1}e_1)
\ \Longleftrightarrow\ G(\lambda^{-1})=c,
\]

where \(c=\alpha^{-1}\) and

\[
G(z)=\sum_{k=1}^{\infty}W_{2k}\gamma_{2k+1}z^{2k+1}
=\sum_{k=1}^{\infty}\frac{q^{k(k-1)}}{Q_{k-1}}z^{2k+1}.
\]

The series converges everywhere. Euler's product identity, which follows by comparing coefficients in \(P(t)=(1+q^2t)P(q^2t)\) with \(P(0)=1\), gives

\[
\boxed{G(z)=z^3\prod_{m=1}^{\infty}(1+q^{2m}z^2).}
\]

Its zeros are exactly the triple zero at the origin and the simple zeros \(z_j^\pm=\pm iq^{-j}\), \(j\ge1\). Differentiation of the convergent product at either simple zero gives

\[
\boxed{G'(z_j^\pm)=2(-1)^{j-1}q^{-j(j+1)}Q_{j-1}Q_\infty.}
\]

**2. Exactly two solutions of each nonzero level per distant annulus.** For \(j\ge1\), set \(R_j=q^{-j-1/2}\) and \(P_{\rm odd}=\prod_{r=1}^{\infty}(1-q^{2r-1})>0\). On \(|z|=R_j\), use \(|1+u|\ge||u|-1|\), split factors at \(m=j\), and obtain the uniform lower estimate

\[
|G(z)|\ge R_j^3q^{-j^2}
\left(\prod_{r=1}^{j}(1-q^{2r-1})\right)P_{\rm odd}
\ge R_j^3q^{-j^2}P_{\rm odd}^{2}\longrightarrow\infty.
\]

For all sufficiently large \(j\), Rouche's theorem therefore equates the number of zeros, counting multiplicities, of \(G-c\) and \(G\) in \(|z|<R_j\). The latter number is \(3+2j\). Subtraction at consecutive radii yields exactly two roots of \(G(z)=c\) in each annulus \(R_{j-1}<|z|<R_j\).

**3. Localize and expand the two simple roots.** Fix either \(z_j=z_j^\pm\). Set \(H_j(z)=G(z)/(z-z_j)\), analytic and nonvanishing in a disk \(|z-z_j|\le\eta_q q^{-j}\) for a sufficiently small fixed \(\eta_q>0\). The logarithmic derivative can be written as a sum over the other zeros of the product, plus the three contributions from zero, and the elementary separation of the geometric zero sequence yields

\[
\sup_{|z-z_j|\le\eta_q q^{-j}}
\left|\frac{H'_j(z)}{H_j(z)}\right|=O_q(jq^j).
\]

Indeed the \(j-1\) nearer positive- and negative-imaginary zero pairs each contribute at most a constant times \(q^j\); the more distant pairs contribute a convergent geometric tail of order \(q^j\), and the zero and opposite-sign factors contribute \(O(q^j)\). Consequently, for \(|d|\ll q^{-j}\),

\[
G(z_j+d)=G'(z_j)d\,[1+O_q(jq^j|d|)].
\]

Because \(|G'(z_j)|\asymp_q q^{-j(j+1)}\), the radius \(r_j=2|c|/|G'(z_j)|\) lies in this disk for large \(j\), and on \(|d|=r_j\) the linear factor \(G'(z_j)d-c\) has modulus at least \(|c|\). Its nonlinear error is \(o(|c|)\). Rouche's theorem gives precisely one simple root near each \(z_j^\pm\), accounting for both roots from step 2. Solving the local equation gives

\[
\boxed{z_{j,\pm}=\pm iq^{-j}
+\frac{(-1)^{j-1}c}{2Q_{j-1}Q_\infty}q^{j(j+1)}
+O_{q,c}\!\left(jq^{2j(j+1)+j}\right).}
\]

Invert this expansion: \(1/(z_j+d)=1/z_j-d/z_j^2+O(|d|^2|z_j|^{-3})\). Since \(z_j^2=-q^{-2j}\), this is precisely the asserted eigenvalue expansion, including its remainder. The scalar resolvent factor has a simple zero there, so the rank-one resolvent formula shows the eigenvalue has algebraic multiplicity one.

**4. Sign and counting.** When \(\alpha>0\) is real, \(c>0\), and the explicit leading real correction has the claimed alternating sign, since \(Q_{j-1}Q_\infty>0\). Real coefficients make the two roots conjugate for all sufficiently large \(j\). Two roots per annulus and \(|\lambda_{j,\pm}|=q^j(1+o(1))\), with only finitely many other nonzero eigenvalues away from zero by compactness, give the counting formula.

## Verification

The accompanying `verify.py` uses high-precision arithmetic to evaluate Euler-product and series coefficients, independently differentiate the product at its explicit zeros, solve \(G(z)=c\) for three distinct \(q\) values and three scalar levels, compare the exact root displacement with its leading term, and test the predicted annuli. It passed 189 finite checks. These are checks of algebra and sample numerical instances, not exhaustive enumeration or a substitute for the preceding infinite-dimensional argument. Run `python verify.py` with `mpmath` installed.

## Relationship to prior work

Bračič and Kandić, *On operators with many spectral components* (2026), Section 6 and especially Lemma 6.2 and Theorem 6.4, establish the general rank-one spectral equation and infinitely many spectral components for the same class of quasinilpotent shifts and square-zero rank-one perturbations. These are explicitly prior ingredients. Their results do not state a fixed geometric two-ray distribution, simple-eigenvalue-per-annulus count, alternating transverse sign or exact logarithmic eigenvalue-count coefficient.

Tcaciuc's *On quasinilpotent operators and the invariant subspace problem* provides the earlier resolvent criterion and qualitative perturbation trichotomy. Zhang's *On the Zeros of Entire \(q\)-Functions* provides more general growth and zero-spacing bounds for order-zero \(q\)-series, and cites Hayman-type asymptotic zero expansions in a different coefficient setting. Those results inform the method but do not explicitly imply the stated level-set pair count and superexponentially small complex drift for this constructed operator.

The Euler \(q\)-product expansion and Rouche's theorem are classical tools. No novelty is claimed for these tools, the general spectral criterion, or for the unperturbed zeros of the Euler product.

## Limitations

The operator and perturbation are deliberately chosen, not generic. Constants in the large-index estimates depend on the fixed \(q\) and nonzero \(\alpha\). The explicit asymptotic says nothing about all finite-index eigenvalues or uniform behavior as \(q\uparrow1\). The full bibliographic equivalence of this specialized nonzero-level Euler-product problem with all historical entire-function results is not established; older equivalent statements may exist. This is a mathematical result with self-review only; no independent validation or expert certification is asserted.

## References

1. J. Bračič and M. Kandić, *On operators with many spectral components*, arXiv:2611.12208v1 (9 November 2026), Section 6, https://arxiv.org/html/2611.12208v1.
2. A. Tcaciuc, *On quasinilpotent operators and the invariant subspace problem*, arXiv:1805.03277 (2018), especially Lemma 2.1 and Proposition 2.4, https://arxiv.org/abs/1805.03277.
3. R. Zhang, *On the Zeros of Entire \(q\)-Functions*, arXiv:2401.01910v4, Sections 1–2, https://arxiv.org/html/2401.01910v4.
