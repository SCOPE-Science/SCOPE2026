# Sharp fixed-accuracy Schmidt-rank profile of an integrable brickwork circuit

## Finding

For the four-state Yang–Baxter brickwork circuit of Pozsgay and the specified one-site sector-changing operator, the **entire optimal single-cut Schmidt-compression curve** has an explicit Gaussian limit. Let \(p_1(t)\ge p_2(t)\ge\cdots\) be the normalized squared operator-Schmidt coefficients at integer time \(t\), with \(\sum_jp_j(t)=1\), and put

\[
F_t(r)=\sum_{j=1}^{\min\{r,\operatorname{OSR}(t)\}}p_j(t).
\]

For **every fixed real** \(a\ge0\),

\[
\boxed{\displaystyle\lim_{t\to\infty}F_t\bigl(\max\{1,\lfloor e^{a\sqrt t}\rfloor\}\bigr)
=\operatorname{erf}\!\left(\frac{a}{\log2}\right).}
\tag{1}
\]

Equivalently, for every fixed squared Hilbert–Schmidt approximation-error tolerance \(0<\varepsilon<1\), the optimal single-cut Schmidt rank

\[
\chi_\varepsilon(t)=\min\{r\ge1:F_t(r)\ge1-\varepsilon\}
\]

has the **exact stretched-exponential coefficient**

\[
\boxed{\displaystyle\lim_{t\to\infty}\frac{\log\chi_\varepsilon(t)}{\sqrt t}
=(\log2)\operatorname{erf}^{-1}(1-\varepsilon).}
\tag{2}
\]

For example, the coefficients in (2) at squared errors \(\varepsilon=0.5\), \(0.1\), and \(0.01\) are approximately \(0.3305870352\), \(0.8061905813\), and \(1.2624888255\). These are **single-cut** optimal-rank statements, not a claim of an optimal uniform bond dimension across every cut of a globally approximating matrix-product operator.

## Assumptions and scope

Each site has a sector bit \(s\in\{A,B\}\) and a colour bit \(a\in\mathbb F_2\), so its Hilbert space is \(\mathbb C^4\). On two sites the permutation gate is the linear extension of

\[
R|s,a;\tau,b\rangle=|\tau,a+(s+\tau)b;\ s,b\rangle,
\]

with bit operations in \(\mathbb F_2\). One period is the product of alternating even and odd brickwork layers. In the infinite chain consider the one-site operator \(O_\times=|B,0\rangle\langle A,0|\) initially at the site adjacent to the cut between sites \(0\) and \(1\). Normalize the operator by its Hilbert–Schmidt norm after integer time \(t\), take infinite volume at fixed \(t\), and then let \(t\to\infty\). The normalized Hermitian operator \((O_\times+O_\times^\dagger)/\sqrt2\) has the same Schmidt spectrum, by the source's exact folded-gate argument, and therefore satisfies the same result.

The spectral decomposition below is on the left/right bipartition induced by this specified cut. Let \(M_t\) be its coefficient matrix in orthonormal bases resolving the output sector counts, with \(\|M_t\|_{\mathrm{HS}}=1\). We use natural logarithms, and \(\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x e^{-u^2}\,du\).

## Proof

**1. The precise input supplied by the source.** Pozsgay's main text and Supplementary equations (S22) and (S38) establish, using a folded permutation circuit, that for \(t\ge1\),

\[
M_t=\sum_{k=0}^{t-1}\sum_{\ell=0}^{t}M_{k\ell},\qquad
M_{k\ell}=P_kM_tQ_\ell,
\]

where the families \(\{P_k\}\) and \(\{Q_\ell\}\) are mutually orthogonal projectors onto output sector-count spaces. Define

\[
\pi_{k\ell}=2^{-(2t-1)}\binom{t-1}{k}\binom{t}{\ell},\qquad
 g(d)=\left|d-\tfrac12\right|-\tfrac12
 =\begin{cases}d-1,&d\ge1,\\-d,&d\le0.\end{cases}
\]

Every nonzero squared singular value of the individual matrix \(M_{k\ell}\) is exactly \(\pi_{k\ell}2^{-g(\ell-k)}\), repeated exactly \(2^{g(\ell-k)}\) times. It follows, **without assuming Schmidt orthogonality between blocks sharing one count**, that

\[
\|M_{k\ell}\|_{\mathrm{HS}}^2=\pi_{k\ell},\quad
\operatorname{rank}(M_{k\ell})=2^{g(\ell-k)},\quad
\|M_{k\ell}\|_{\mathrm{op}}=\pi_{k\ell}^{1/2}2^{-g(\ell-k)/2}.
\tag{3}
\]

Because the projections are orthogonal in the Hilbert–Schmidt inner product, the whole set of count blocks is Hilbert–Schmidt orthogonal. The weights sum to one.

**2. Exact finite-time low/high difference splitting.** For a real cutoff \(b\ge0\), write \(G_t=g(L_t-K_t)\), where \(K_t\sim\operatorname{Bin}(t-1,1/2)\) and \(L_t\sim\operatorname{Bin}(t,1/2)\) are independent, and set \(q_t(b)=\Pr\{G_t\le b\sqrt t\}\). Split \(M_t=S_t(b)+T_t(b)\) with

\[
S_t(b)=\sum_{g(\ell-k)\le b\sqrt t}M_{k\ell},\qquad
T_t(b)=\sum_{g(\ell-k)>b\sqrt t}M_{k\ell}.
\]

Equation (3), Hilbert–Schmidt orthogonality and rank subadditivity give the *exact mass* and the *deterministic rank budget*

\[
\|S_t(b)\|_{\mathrm{HS}}^2=q_t(b),\qquad
\|T_t(b)\|_{\mathrm{HS}}^2=1-q_t(b),\qquad
\operatorname{rank}S_t(b)\le t(t+1)2^{b\sqrt t}.
\tag{4}
\]

The high-difference part has a **small operator norm**, which is the key additional estimate needed to handle coherence between different count blocks. Since \(\pi_{k\ell}\le1\), the triangle inequality and (3) yield

\[
\boxed{\|T_t(b)\|_{\mathrm{op}}\le t(t+1)2^{-b\sqrt t/2}.}
\tag{5}
\]

The harmless polynomial prefactor is crucially subexponential on the \(\sqrt t\) scale.

**3. A sharp finite-rank two-sided estimate.** Eckart–Young's variational characterization, for every positive integer \(r\), is

\[
\sqrt{F_t(r)}=\sup_{\substack{\operatorname{rank}Y\le r\\\|Y\|_{\mathrm{HS}}=1}}
|\operatorname{tr}(Y^\dagger M_t)|.
\]

Using \(\|Y\|_*\le\sqrt r\|Y\|_{\mathrm{HS}}\), Hilbert–Schmidt Cauchy–Schwarz on \(S_t(b)\), and trace/operator duality on \(T_t(b)\), one obtains

\[
\boxed{
\sqrt{F_t(r)}\le\sqrt{q_t(b)}+\sqrt r\,t(t+1)2^{-b\sqrt t/2}.
}
\tag{6}
\]

Conversely, the rank bound in (4) and the Eckart–Young characterization of best approximation imply

\[
\boxed{r\ge t(t+1)2^{b\sqrt t}\quad\Longrightarrow\quad F_t(r)\ge q_t(b).}
\tag{7}
\]

These estimates are valid at **every** finite integer time. In particular, neither requires a false assumption that different count differences have orthogonal Schmidt bases.

**4. Half-Gaussian limit and sharp coefficient.** The centered binomial difference satisfies

\[
\frac{L_t-K_t}{\sqrt t}\ \xrightarrow{\mathrm d}\ N(0,1/2).
\]

Since \(|g(d)-|d||\le1\), the continuous mapping theorem gives

\[
\lim_{t\to\infty}q_t(b)=\Pr\{|N(0,1/2)|\le b\}=\operatorname{erf}(b)
\qquad(b\ge0).
\tag{8}
\]

Fix \(a>0\), and put \(r=\max\{1,\lfloor e^{a\sqrt t}\rfloor\}\). For any \(b>a/\log2\), the second term in (6) tends to zero, hence \(\limsup F_t(r)\le\operatorname{erf}(b)\); let \(b\downarrow a/\log2\). For any \(0\le b<a/\log2\), the rank condition in (7) holds for all sufficiently large \(t\); hence \(\liminf F_t(r)\ge\operatorname{erf}(b)\); let \(b\uparrow a/\log2\). At \(a=0\), the upper-bound argument with arbitrary \(b>0\) gives limit zero directly. This proves (1).

Finally, \(\operatorname{erf}\) is continuous and strictly increasing on nonnegative arguments. Fix \(0<\varepsilon<1\) and bracket its unique \((1-\varepsilon)\)-quantile between any two nearby positive rank exponents. Applying (1) to those exponents and taking the bracket width to zero proves (2), with no unstated uniformity in \(\varepsilon\).

## Verification

The accompanying `verify.py` independently implements the 16-state *folded* two-site permutation on ket and bra, builds the complete finite packets from the normalized identity vectorizations and the explicit matrix-unit source, and uses exact integer Gram identities to verify the source's critical flat-count-block spectra for times \(t=1,2,3\). Running `python verify.py` requires only Python's standard library and produces `PASS 2736`; it checks every available count block and its multiplicity at these times. The proof of (4)–(8) is algebraic/probabilistic and applies to all positive integer times; these finite tests are not presented as a proof of the asymptotic claim. The source's supplementary sections and each critical matrix-norm step were checked separately.

## Relationship to prior work

The gate, folding construction, binomial weights, and individual count-block flatness are **not** claimed as new. Pozsgay's first public preliminary manuscript appeared on September 4, 2026, followed by arXiv:2609.39401. Its Supplementary Section V proves that every fixed error requires at least \(\exp(c_\varepsilon\sqrt t)\) Schmidt rank for *some unspecified* positive \(c_\varepsilon\); it gives neither a matching upper exponent nor the limiting optimal retained-weight function. The present result computes both by a new low-/high-count-difference operator-norm split and uses the full Gaussian quantile. In particular, the source's bound (S55) has a \(r^2\) factor and alone does not give the sharp constant.

A separately published analysis of this **same circuit** determines a sharp high-index Rényi logarithmic coefficient; it is not ignored. Its \(\alpha>1\) moment asymptotics are dominated by a narrow, near-balanced part of the spectrum and do **not** determine the optimal mass captured by \(e^{a\sqrt t}\) Schmidt modes. Conversely, the present typical-weight limit does not determine high-index Rényi moments. Broader Yang–Baxter-gate entanglement bounds and general operator-entropy/simulability implications do not supply the present exact model-specific compression profile.

## Limitations

The result is for a fixed cut, fixed \(a\) or fixed \(\varepsilon\), the specified local operator and the prescribed infinite-volume-first dynamics. It does not establish a globally optimal matrix-product-operator approximation uniformly over all spatial cuts, a full pointwise Schmidt eigenvalue distribution, a nonasymptotic optimal-rank formula, or a noise-robust simulation theorem. The public September 4 preliminary manuscript's original PDF was not inspected; its current public description reports the qualitative growth law, leaving residual priority risk of an unexamined equivalent. The result is a quantitative mathematical extension of publicly known exact branch spectra and warrants external independent review.

## References

1. B. Pozsgay and I. Vona, *Square-root growth of operator entanglement in an integrable brickwork circuit*, public preliminary manuscript, Zenodo 22306151, published September 4, 2026. https://doi.org/10.5281/zenodo.22306151
2. B. Pozsgay, *Square-root growth of operator entanglement in an integrable brickwork circuit*, arXiv:2609.39401, first submitted September 30, 2026, especially Supplemental (S22), (S38), and (S53)–(S58). https://arxiv.org/abs/2609.39401
3. *The exact high-index Rényi coefficient in an integrable brickwork circuit*, published-finding corpus public research record, October 12, 2026, identifier `2026/10/12/SCOPE-the-exact-high-index-r-nyi-coefficient-in-an-integrable-brickwor--308ff33614b5`. https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-the-exact-high-index-r-nyi-coefficient-in-an-integrable-brickwor--308ff33614b5/RESULT.md
4. B. Pozsgay, *On the growth of operator entanglement in brickwork circuits with Yang–Baxter gates*, arXiv:2609.05121, September 2026. https://arxiv.org/abs/2609.05121
5. N. Dowling, *Classical Simulability from Operator Entanglement Scaling*, arXiv:2603.05656, March 2026. https://arxiv.org/abs/2603.05656
