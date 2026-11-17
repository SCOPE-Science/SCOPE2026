# Finite-rank rigidity for harmonic exponential-type Fock Toeplitz products

## Finding

**Theorem (complete finite-rank dichotomy).** Let \(N\ge 1\) and let \(\varphi_j=f_j+\overline{g_j}\) for \(1\le j\le N\), where all \(f_j,g_j\) are entire functions of exponential type on \(\mathbb C\). On the common invariant domain \(\mathcal E_1\) of entire functions of exponential type in the Gaussian Fock space, form the ordered product
\[
P=T_{\varphi_1}T_{\varphi_2}\cdots T_{\varphi_N}.
\]
Then \(P\) has finite-dimensional range **if and only if** at least one symbol \(\varphi_j\) is identically zero. In that event \(P=0\). If every symbol is nonzero, the range of \(P\) is infinite-dimensional. In particular, if this product admits a bounded extension to the Gaussian Fock space, that extension cannot be a nonzero finite-rank operator.

More precisely, for every such nonzero product there exists a radius \(R>0\) and an infinite sequence \((w_k)_{k\ge 1}\subset\mathbb C\), with \(|w_j-w_k|>2R\) for \(j\ne k\), such that the images
\[
P(e^{w_k z}),\qquad k=1,2,\ldots,
\]
are linearly independent. The estimate \(R\) may depend on the symbols and the number of factors. No uniform finite bound on the number of independent coherent-state images is imposed.

## Assumptions and scope

Use the standard Gaussian Fock space
\[
\mathcal F^2(\mathbb C)=\left\{h\in\mathcal O(\mathbb C):\frac1\pi\int_{\mathbb C}|h(z)|^2e^{-|z|^2}\,dA(z)<\infty\right\}.
\]
An entire function \(h\) has **exponential type** here if \(|h(z)|\le C e^{a|z|}\) for some positive constants \(C,a\). Denote this vector space by \(\mathcal E_1\). It is a dense common invariant domain for the Toeplitz operators with the displayed harmonic symbols, and it contains every unnormalized coherent state \(e^{wz}\), \(w\in\mathbb C\). The Toeplitz operator is the Gaussian Fock projection of multiplication by the symbol, restricted to this invariant domain; no boundedness of the individual factors on the entire Hilbert space is asserted.

The domain rank of \(P\) is the dimension of \(P(\mathcal E_1)\), possibly infinite. Since the source theorem is one-variable, the statement is not asserted on Fock spaces of higher complex dimension. Symbols are allowed to have cancelling constant analytic and anti-analytic parts; the condition \(\varphi_j\not\equiv0\) concerns the actual harmonic function, not the particular representation of its two parts.

## Proof

**Step 1: nonzero entire kernel amplitude.** Let \(\mathcal E_2\) denote the entire functions on \(\mathbb C^2\) of joint exponential type. A result of Liu, Qin, and Huang [1, Sections 2–4] provides a two-variable function \(V\in\mathcal E_2\) such that
\[
(Pe^{w(\cdot)})(z)=e^{wz}V(z,w)\qquad(z,w\in\mathbb C).
\]
For clarity, their explicit construction is
\[
V_{N+1}=1,\qquad
V_j=f_j(z)V_{j+1}+\sum_{k=0}^{\infty}\frac{G_j^{(k)}(w)}{k!}\,\partial_z^k V_{j+1},\qquad G_j(w)=\overline{g_j(\overline w)},
\]
with \(V=V_1\). The series remain in \(\mathcal E_2\). Their Proposition 3.1 proves injectivity of each recursion step when \(\varphi_j\not\equiv0\), because \(f_j(z)+G_j(w)\not\equiv0\). Starting from \(V_{N+1}=1\), one therefore has \(V\not\equiv0\) if all symbols are nonzero. This nonvanishing is the established zero-product theorem [1]; we use its proved kernel representation and cancellation lemma as inputs, not as a new assertion.

**Step 2: a separation lemma for joint exponential type.** We prove the following independent assertion. Suppose \(V\in\mathcal E_2\) is nonzero. There exist constants \(M,R>0\) such that
\[
\big|\partial_z^m\partial_w^n V(0,0)\big|\le M R^{m+n}\qquad(m,n\ge0).
\]
Indeed, this follows from the exponential-type derivative bound [1, Lemma 2.1], and \(R\) may be increased without affecting it. Define \(h_w(z)=V(z,w)\) and \(F_w(z)=e^{wz}h_w(z)\). Then, for every fixed \(w\), Taylor expansion in the second variable gives
\[
\big|h_w^{(m)}(0)\big|
\le M R^m e^{R|w|}\qquad(m\ge0).
\]
For \(|\xi-w|>R\) define the analytic function
\[
B_w(\xi)=\sum_{m=0}^{\infty}\frac{h_w^{(m)}(0)}{(\xi-w)^{m+1}}.
\]
It decays like \(O(1/|\xi|)\) at infinity. If \(h_w\not\equiv0\), then \(B_w\) cannot extend holomorphically across its entire excluded closed disk \(\overline D(w,R)\): otherwise it would extend to an entire function vanishing at infinity, hence would be zero by Liouville's theorem. Successive Laurent coefficients would then give \(h_w^{(m)}(0)=0\) for every \(m\), a contradiction.

The precise relation to \(F_w\) is the exponential-translation identity for the formal Borel series:
\[
\sum_{n=0}^{\infty}\frac{F_w^{(n)}(0)}{\xi^{n+1}}
=\sum_{m=0}^{\infty}\frac{h_w^{(m)}(0)}{(\xi-w)^{m+1}}
=B_w(\xi),\qquad |\xi|>|w|+R.
\]
To prove it, substitute
\(F_w^{(n)}(0)=\sum_{m=0}^{n}\binom{n}{m}w^{n-m}h_w^{(m)}(0)\), use absolute convergence in the indicated region, and sum
\(\sum_{j\ge0}\binom{m+j}{m}t^j=(1-t)^{-m-1}\). This establishes the identity without any distributional or boundary-value assumption.

Fix distinct parameters \(w_1,\dots,w_s\) satisfying
\[
|w_i-w_j|>2R\quad(i\ne j),\qquad h_{w_i}\not\equiv0.
\]
Suppose \(\sum_{i=1}^s c_iF_{w_i}\equiv0\). Equality of derivatives at zero and the Borel identity show \(\sum_i c_i B_{w_i}=0\) near infinity. Each \(B_{w_i}\) is analytic on the connected domain
\[
\Omega=\mathbb C\setminus\bigcup_{i=1}^s\overline D(w_i,R),
\]
so the identity theorem extends this equality throughout \(\Omega\). If \(c_i\ne0\), then
\[
B_{w_i}=-c_i^{-1}\sum_{j\ne i}c_j B_{w_j}
\]
on \(\Omega\). The right side is holomorphic on a neighborhood of \(\overline D(w_i,R)\), because all the other excluded disks are disjoint from this one. It consequently provides a holomorphic continuation of \(B_{w_i}\) through its entire disk, contradicting the previous paragraph. Therefore every \(c_i=0\). This proves independence of every such finite family, for arbitrary \(s\).

**Step 3: infinitely many separated nonzero fibers.** Since \(V\not\equiv0\), choose \(z_0\in\mathbb C\) for which the one-variable entire function \(w\mapsto V(z_0,w)\) is not identically zero. Its zero set is discrete. In particular, one can choose infinitely many \(w_k\) with mutually separated distances larger than \(2R\), avoiding that zero set. Then \(h_{w_k}\not\equiv0\). Step 2 yields linear independence of all corresponding coherent-state images \(F_{w_k}=Pe^{w_kz}\). Thus \(P(\mathcal E_1)\) has infinite dimension.

If some symbol is zero, its Toeplitz operator vanishes on the invariant domain and hence \(P=0\). These two implications give the exact dichotomy. Finally, an everywhere-defined bounded extension has a range containing \(P(\mathcal E_1)\); it cannot have finite rank unless the product is zero. \(\square\)

## Verification

The proof depends on the separately checked kernel representation and injectivity statement of [1] and on the explicit Borel identity and singularity-separation argument proved above. The latter requires no compactness, numerical convergence extrapolation, or approximation by finite-dimensional matrices. A standalone exact-arithmetic script, `verification.py`, checks a nontrivial two-factor polynomial-symbol example and the Borel coefficient identity for finitely many indices; those checks are illustrations and are not used to infer the all-symbol, infinite-dimensional theorem.

To reproduce the finite checks, run `python3 verification.py` with the standard Python library. To reproduce the mathematical argument, use the derivative-bound definition of \(\mathcal E_2\) from [1, Lemma 2.1], its kernel recursion [1, equations (4.2)–(4.3)], and the full separation proof given above.

## Relationship to prior work

Liu, Qin, and Huang [1] prove that a finite product of Toeplitz operators with harmonic entire exponential-type symbols vanishes exactly when a factor vanishes. Their paper supplies the crucial entire kernel amplitude and its nonvanishing, but it does not state that every nonzero product has infinite-dimensional range or provide separated coherent-state witnesses. The present statement rules out **all positive finite ranks** for such products, not just rank zero.

Borichev and Rozenblum [2] prove a finite-rank theorem for a single Fock Toeplitz operator under broad symbol assumptions, but the product here is not generally itself a Toeplitz operator with a function symbol. Bauer and Le [3] address finite rank and algebraic identities for other Segal–Bargmann Toeplitz classes, including restricted zero-product situations; their results do not yield this exact arbitrary-length exponential-type harmonic product classification. A publicly available finite-frequency exponential-polynomial result from 2026 gives a zero-divisor-free algebra in a smaller symbol class; it does not establish the all-exponential-type rank dichotomy. The new mechanism uses disjoint Borel singularity regions for the entire two-variable kernel amplitude.

## Limitations

The assertion is specifically for **one complex variable**, **harmonic symbols with entire exponential-type parts**, and the **natural common invariant dense domain**. Products may be unbounded on the ambient Fock Hilbert space; no universal bounded extension is claimed. The conclusion excludes finite nonzero rank but does **not** exclude compact infinite-rank products, nor does it determine singular-value decay, essential norms, or multi-dimensional cases. The step establishing that \(V\not\equiv0\) relies on the cited 2026 theorem [1]. Although searches found no equivalent all-rank product theorem, older results under an alternative analytic- or functional-calculus formulation may still cover the claim; independent priority review is not asserted.

## References

1. Y. Liu, J. Qin, and S. Huang, *Finite zero products of Toeplitz operators with harmonic symbols*, arXiv:2610.30209v1 (first submitted 2026-10-21). https://arxiv.org/abs/2610.30209. See Theorem 1.2, Lemma 2.1, Proposition 3.1, and equations (4.2)–(4.3).
2. A. Borichev and G. Rozenblum, *The finite rank theorem for Toeplitz operators on the Fock space*, Journal of Geometric Analysis 25 (2015), 347–356. https://doi.org/10.1007/s12220-013-9432-7.
3. W. Bauer and T. Le, *Algebraic properties and the finite rank problem for Toeplitz operators on the Segal–Bargmann space*, Journal of Functional Analysis 261 (2011), 2617–2640. https://doi.org/10.1016/j.jfa.2011.07.006.
4. H. R. Cho, J. D. Park, and K. Zhu, *Products of Toeplitz operators on the Fock space*, Proceedings of the American Mathematical Society 142 (2014), 2483–2489. https://arxiv.org/abs/1212.0045.
