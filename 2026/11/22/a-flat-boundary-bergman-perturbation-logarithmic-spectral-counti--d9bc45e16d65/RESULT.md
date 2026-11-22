# A flat-boundary Bergman perturbation: logarithmic spectral counting and Bessel hyponormality collapse

## Finding
Let \(A^2(\mathbb D)\) be the standard analytic Bergman space with normalized area measure. Let \(S=T_z\), and for \(a>0\) let \(D_a=T_{q_a}\), where
\[
q_a(z)=\exp\!\left(-\frac{a}{1-|z|^2}\right),\qquad V_{a,c}=S+cD_a\quad(c\in\mathbb C).
\]
Define \(J_a\) on \(\ell^2(\mathbb N_0)\) by its zero diagonal and positive symmetric adjacent entries
\[
(J_a)_{k,k+1}=(J_a)_{k+1,k}=w_k(a),\quad
w_k(a)=a(k+1)\sqrt{(k+2)(k+3)}\int_0^1\frac{u^{k+1}}{1-u}e^{-a/(1-u)}\,du.
\]
Every \(J_a\) is compact and belongs to \(\mathcal S_p\) for **every** \(p>0\), has infinitely many strictly positive and negative eigenvalues, and satisfies the sharp logarithmic counting law
\[
\lim_{\lambda\downarrow0}\frac{N(\lambda;|J_a|)}{[\log(1/\lambda)]^2}=\frac1{4a},\qquad
\lim_{n\to\infty}\frac{-\log s_n(J_a)}{\sqrt n}=2\sqrt a.
\]
Here \(N(\lambda;|J_a|)\) counts singular values strictly greater than \(\lambda\), with multiplicities; the positive and negative eigenvalue counting functions each have coefficient \(1/(8a)\).

The perturbation \(V_{a,c}\) is hyponormal **exactly** when \(|c|\le \|J_a\|^{-1}\). As \(a\downarrow0\), this allowable coupling collapses at the sharp rate
\[
\lim_{a\downarrow0}a\|J_a\|=\mathcal C
=\frac{y_*^4 K_0(y_*)}{4}=0.7353491542\ldots,\qquad
\|J_a\|^{-1}\sim\frac a{\mathcal C}=1.3598982120\ldots a.
\]
\(K_\nu\) is the standard modified Bessel function of the second kind and \(y_*>0\) is the unique solution of \(y_*K_1(y_*)=4K_0(y_*)\) (numerically \(y_*=3.5282705520\ldots\)). Thus \(D_a\to I\) strongly as \(a\downarrow0\), even though for every fixed nonzero \(c\), \(V_{a,c}\) eventually fails to be hyponormal. At \(a=0\), interpreted as \(D_0=I\), all \(S+cI\) are hyponormal.

## Assumptions and scope
Only the standard one-variable analytic Bergman space, real \(a>0\), and arbitrary complex \(c\) are considered. The positive operator-ideal exponent \(p\) may be below one. All eigenvalue-counting limits are at fixed \(a>0\); the coupling limit is instead \(a\downarrow0\). No uniform assertion interchanging these two limits is made.

## Proof

**1. Exact normalized commutator.** With \(e_k=\sqrt{k+1}z^k\), write \(Se_k=\alpha_k e_{k+1}\), \(\alpha_k=\sqrt{(k+1)/(k+2)}\). Then \([S^*,S]e_k=d_k e_k\), where \(d_k=1/[(k+1)(k+2)]>0\). Radial Toeplitz compression gives \(D_a e_k=b_k e_k\), with
\[
b_k=(k+1)\int_0^1u^k e^{-a/(1-u)}\,du.
\]
Integration by parts, using the vanishing endpoint value of the flat symbol, yields the exact positive difference
\[
b_k-b_{k+1}=a\int_0^1\frac{u^{k+1}}{1-u}e^{-a/(1-u)}\,du.
\]
Consequently the finite quadratic forms of \([V_{a,c}^*,V_{a,c}]\), after congruence by \(\operatorname{diag}(d_k^{-1/2})\), are those of \(I-|c|J_a\), up to a diagonal phase unitary. The congruence is only used on finitely supported vectors: the inverse diagonal is unbounded. Since \(J_a\) is bounded (proved below), positivity on that dense form core is equivalent to \(I-|c|J_a\ge0\). The parity unitary \(e_k\mapsto(-1)^ke_k\) sends \(J_a\) to \(-J_a\); hence \(\max\sigma(J_a)=\|J_a\|\), proving the stated if-and-only-if hyponormality criterion.

**2. Stretched-exponential weights.** Set
\[
I_k(a)=\int_0^1t^{-1}(1-t)^{k+1}e^{-a/t}\,dt,\qquad
w_k(a)=a(k+1)\sqrt{(k+2)(k+3)}I_k(a).
\]
Since \((1-t)^{k+1}\le e^{-(k+1)t}\),
\[
I_k(a)\le\int_0^\infty t^{-1}e^{-(k+1)t-a/t}\,dt=2K_0(2\sqrt{a(k+1)}).
\]
The standard large-argument integral estimate for \(K_0\) gives \(\limsup_{k\to\infty} k^{-1/2}\log I_k(a)\le-2\sqrt a\). For the converse, restrict the integral to \(t\in[(1-\varepsilon)\sqrt{a/k},(1+\varepsilon)\sqrt{a/k}]\); on this interval the exponent \((k+1)\log(1-t)-a/t\), divided by \(\sqrt{k}\), approaches \(-\sqrt a(s+s^{-1})\) after writing \(t=s\sqrt{a/k}\). Shrinking \(\varepsilon\) proves the reverse bound by Laplace's principle. The polynomial prefactor in \(w_k\) does not change the logarithmic limit:
\[
\lim_{k\to\infty}\frac{-\log w_k(a)}{\sqrt k}=2\sqrt a.\tag{1}
\]
Furthermore, \(I_{k+1}(a)/I_k(a)\to1\): the normalized integral measure defining \(I_k\) concentrates at \(t=0\), since each fixed \(t\ge\delta>0\) contributes an exponentially small amount compared with the saddle lower bound \(e^{-O(\sqrt k)}\). Thus \(w_{k+1}(a)/w_k(a)\to1\). Equation (1) gives compactness and \(\mathcal S_p\) membership for all \(p>0\) by writing \(J_a=B_a+B_a^*\), where \(B_ae_k=w_k(a)e_{k+1}\). Since all weights are positive, the compact Jacobi operator has infinite rank and parity symmetry, hence infinitely many eigenvalues of each sign.

**3. Exact logarithmic spectral counting.** We use the following elementary slow-bond lemma, proved here. If a zero-diagonal self-adjoint Jacobi matrix has positive off-diagonal entries \(v_k\), with \(v_{k+1}/v_k\to1\) and \(-\log v_k\sim Ck^\delta\) for \(C>0\) and \(0<\delta<1\), then
\[
N(\lambda;|J|)\sim C^{-1/\delta}[\log(1/\lambda)]^{1/\delta}.\tag{2}
\]
For the upper bound let \(R=(\log(1/\lambda)/C)^{1/\delta}\), and truncate after \((1+\varepsilon)R\) coordinates. By the logarithmic assumption, the remaining Jacobi tail has norm at most twice its largest bond, which is \(o(\lambda)\). The crossing has rank at most two, so \(N(\lambda;|J|)\le(1+\varepsilon)R+O(1)\). For the lower bound restrict to coordinates between \(\eta R\) and \((1-\varepsilon)R\). Uniformly throughout this interval \(\lambda/v_k\to0\). Partition it into long blocks of length \(L_R\to\infty\), chosen so slowly that \(L_R\sup_{k\ge\eta R}|\log(v_{k+1}/v_k)|\to0\) and \(L_R/R\to0\). Cutting interblock bonds changes rank by \(O(R/L_R)\). Each block, divided by its first bond, differs in operator norm by \(o(1)\) from the constant-bond path with eigenvalues \(2\cos(j\pi/(L_R+1))\). Its proportion of singular values at most \(\lambda\) is \(o(1)\); Weyl inequalities and the rank perturbation bound therefore give at least \((1-\varepsilon-\eta)R-o(R)\) singular values above \(\lambda\). Let \(\varepsilon,\eta\downarrow0\). This proves (2). Apply it with \(C=2\sqrt a\) and \(\delta=1/2\). Parity symmetry yields equal positive and negative counts, and inversion of the counting law yields the stated logarithmic singular-value law.

**4. Sharp small-parameter norm.** Write \(x=a(k+1)\). The substitution \(t=av\) in \(I_k(a)\) and dominated convergence show that, locally uniformly for \(x\in(0,\infty)\),
\[
a w_k(a)\longrightarrow F(x):=2x^2K_0(2\sqrt x)\quad\text{whenever }a\downarrow0,\ a(k+1)\to x.
\]
The previous Bessel upper bound gives \(a w_k(a)\le2a^2(k+1)\sqrt{(k+2)(k+3)}K_0(2\sqrt{a(k+1)})\). Since \(x^2K_0(2\sqrt{x})\to0\) at both \(x=0\) and \(x=\infty\), this bounds both tails uniformly and proves \(a\sup_kw_k(a)\to\max_{x>0}F(x)\). The Jacobi row bound yields \(a\|J_a\|\le2a\sup_kw_k(a)\). Conversely choose blocks of length \(L(a)\to\infty\) with \(aL(a)\to0\) around an index with \(a(k+1)\) near an argmax of \(F\). On such blocks all rescaled bonds tend uniformly to \(\max F\); the normalized constant vector has Rayleigh quotient tending to \(2\max F\). Hence \(\lim_{a\downarrow0}a\|J_a\|=2\max F\).

Writing \(y=2\sqrt x\), we have \(2F(x)=y^4K_0(y)/4\). Its stationary points obey \(yK_1(y)=4K_0(y)\). The function \(yK_1(y)/K_0(y)\) increases strictly from zero to infinity, because its derivative equals \(y[(K_1/K_0)^2-1]>0\) and \(K_1>K_0>0\). Thus the stationary point is unique and is the global maximum. Finally, \(b_k(a)\to1\) for each fixed \(k\) as \(a\downarrow0\) by dominated convergence; hence \(D_a\to I\) strongly, completing the assertion.

## Verification
The supplementary checker `check_flat_toeplitz.py` independently constructs the Bergman shift and radial moments, tests the derived Jacobi off-diagonal formulas, diagonal phase spectral symmetry and finite-compression norms. It computes the Bessel stationary equation and checks convergence of \(a\|J_a\|\) at several positive values of \(a\). These finite tests provide consistency checks only. The infinite counting law and the small-parameter limit follow from the analytic arguments above, not from finite enumerations.

## Relationship to prior work
Le–Simanek (2020) provides the general Jacobi-operator criterion for hyponormality of a shift plus a radial diagonal Toeplitz perturbation, and Simanek (2020) studies power radial symbols. Their criteria determine whether an individual perturbation is hyponormal once the Jacobi norm is known, but do not compute the norm's singular boundary-flat limit or the flat perturbation's logarithmic spectral counting constant. Pushnitski (2017) gives banded-matrix power-decay spectral asymptotics and Koita–Kupin–Naboko–Touré (2020) gives logarithmic-decay ones; the present off-diagonal weights instead decay as \(e^{-2\sqrt{ak}+o(\sqrt k)}\). El-Fallah–El Ibbaoui (2021) studies polynomially controlled inverse-eigenvalue regimes for positive Toeplitz operators, not the signed normalized Jacobi operator here. The slow-bond lemma is included to avoid relying on an unverified extension of those spectral laws.

## Limitations
Historical priority for special flat boundary symbols has not been exhaustively established. The proof concerns the standard Bergman norm, not arbitrary Bergman weights or other analytic disk spaces. No uniform two-parameter singular-value law across \(a\downarrow0\) and \(n\to\infty\) is claimed. The exact finite-\(a\) norm is given by the compact Jacobi operator, not by an elementary closed form; only its sharp small-\(a\) coefficient is established. Numerical consistency tests do not constitute independent validation.

## References
- Trieu Le and Brian Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Spaces*, arXiv:2003.07330 (first posted 16 March 2020), https://arxiv.org/abs/2003.07330.
- Brian Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Space*, arXiv:2001.07823 (first posted 22 January 2020), https://arxiv.org/abs/2001.07823.
- Alexander Pushnitski, *Spectral asymptotics for a class of Toeplitz operators on the Bergman space*, arXiv:1710.02652 (first posted 7 October 2017), https://arxiv.org/abs/1710.02652.
- M. Koita, S. Kupin, S. Naboko and B. Touré, *On spectral properties of compact Toeplitz operators on Bergman space with logarithmically decaying symbol and applications to banded matrices*, arXiv:2006.02586 (first posted 3 June 2020), https://arxiv.org/abs/2006.02586.
- Omar El-Fallah and Mohamed El Ibbaoui, *Trace estimates of Toeplitz operators on Bergman spaces and applications to composition operators*, arXiv:2101.12268 (first posted 28 January 2021), https://arxiv.org/abs/2101.12268.
