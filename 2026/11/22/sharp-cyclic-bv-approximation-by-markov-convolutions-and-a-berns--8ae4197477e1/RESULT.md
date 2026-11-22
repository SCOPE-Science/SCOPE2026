# Sharp cyclic BV approximation by Markov convolutions and a Bernstein heat-error law

## Finding

**Theorem (universal cyclic convolution law and heat specialization).** Let \(n\ge3\), let the vertex set be \(\mathbb Z/n\mathbb Z\), and let \(p=(p_0,\ldots,p_{n-1})\) be an arbitrary probability vector. Define the circulant Markov convolution
\[
(P_pf)(i)=\sum_{d=0}^{n-1}p_d f(i+d\bmod n),\qquad
V(f)=\sum_{i=0}^{n-1}|f(i+1)-f(i)|.
\]
Write \(h_n(d)=\min\{d,n-d\}\) for \(0\le d<n\). With counting \(\ell^1\) on vertices, the exact sharp quotient norm is
\[
\boxed{\sup_{V(f)>0}\frac{\|f-P_pf\|_{\ell^1}}{V(f)}
=\sum_{d=0}^{n-1}p_d h_n(d).}\tag{1}
\]
Every real two-level signal whose high-level set is a contiguous cyclic arc of \(\lfloor n/2\rfloor\) or \(\lceil n/2\rceil\) vertices attains this value. If \(p_d>0\) for every \(1\le d<n\), these are **all** nonconstant equality signals, up to addition of a constant and multiplication by a nonzero real scalar. In particular, neither reversibility nor symmetry of \(p\) is needed for (1).

For the ordinary combinatorial heat semigroup \(H_t=e^{-tL_n}\) on the unit-edge cycle, where
\[
(L_nf)(i)=2f(i)-f(i-1)-f(i+1),\qquad t>0,
\]
the exact sharp coefficient \(C_n(t)=\sup_{V(f)>0}\|f-H_tf\|_{\ell^1}/V(f)\) is
\[
\boxed{C_n(t)=\sum_{d=0}^{n-1}h_n(d)H_t(0,d)
=\frac{\lfloor n^2/4\rfloor}{n}
-\frac2n\sum_{k=1}^{n-1}\frac{a_{n,k}}{\lambda_{n,k}}e^{-\lambda_{n,k}t},}\tag{2}
\]
where \(\lambda_{n,k}=4\sin^2(\pi k/n)\) and
\[
a_{n,k}=\begin{cases}
1-(-1)^k,&n\text{ even},\\
1-(-1)^k\cos(\pi k/n),&n\text{ odd}.
\end{cases}
\]
All \(a_{n,k}\) are nonnegative, and at least one is strictly positive. Thus \(C_n\) is a **Bernstein function** on \((0,\infty)\): for every integer \(r\ge0\),
\[
\boxed{(-1)^r C_n^{(r+1)}(t)=\frac2n\sum_{k=1}^{n-1}a_{n,k}\lambda_{n,k}^{r}e^{-\lambda_{n,k}t}>0.}\tag{3}
\]
It increases strictly and is strictly concave, starts at \(C_n(0)=0\) with \(C'_n(0)=2\), and approaches \(\lfloor n^2/4\rfloor/n\). At every \(t>0\), its complete real equality family consists precisely of nonconstant scalar multiples of balanced cyclic-arc indicators, plus constants.

## Assumptions and scope

The graph has \(n\ge3\) sites and undirected unit edges between neighboring residues, with each edge counted exactly once in \(V\). Signals are real, with no sign or mean restriction. The norm \(\|\cdot\|_{\ell^1}\) is an **unnormalized** sum of absolute vertex values, not the vertex-average norm. The quotient is over \(V(f)>0\), so constant functions are excluded. The general convolution theorem permits nonreversible and directed mixing probability vectors, including zero entries; its *uniqueness* assertion requires every nonzero displacement weight strictly positive. The heat result uses jump rate one in each direction (total rate two), not the degree-normalized heat generator. At \(t=0\) the norm is zero and no uniqueness-of-extremizers claim is made.

## Proof

**1. Cyclic translation inequality.** For an integer displacement \(d\) and any real signal, telescope along a shortest oriented cycle path of length \(h_n(d)\) from \(i\) to \(i+d\). Summing the triangle inequality over \(i\) gives
\[
\sum_i|f(i)-f(i+d)|\le h_n(d)V(f).
\]
The Markov convex combination then gives
\[
\|f-P_pf\|_{\ell^1}\le\sum_dp_d\sum_i|f(i)-f(i+d)|
\le \left(\sum_dp_dh_n(d)\right)V(f).\tag{4}
\]
No symmetry of the kernel was used.

**2. Simultaneous sharpness for every displacement.** Let \(S\) be a consecutive cyclic interval of length \(q\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\), and let \(s=\mathbf1_S\). For each displacement \(d\), the number of selected sites with \(i+d\notin S\) equals
\[
N_d(S)=\min\{d,n-d,q,n-q\}=h_n(d).
\]
Since \(P_p\) is doubly stochastic, its total mass leaving \(S\) equals its total mass entering \(S\). Hence
\[
\|s-P_ps\|_{\ell^1}
=2\sum_{i\in S}\sum_{j\notin S}p_{j-i}
=2\sum_dp_dN_d(S)=2\sum_dp_dh_n(d).
\]
The two boundary edges of \(S\) give \(V(s)=2\). This attains (4), proving (1) for every probability vector.

**3. Complete cut rigidity under full support.** More generally let \(S\) be any nonempty proper subset, with \(b=|\partial S|=2r\) boundary edges. The cyclic translation inequality for its indicator yields
\[
N_d(S)\le r h_n(d).\tag{5}
\]
If its norm quotient equals (1) and every \(p_d>0\) for \(d\ne0\), all inequalities (5) are equalities. Put \(m=\lfloor n/2\rfloor\). At displacement \(m\), we also have \(N_m(S)\le\min\{|S|,n-|S|\}\), hence
\[
rm\le|S|\quad\text{and}\quad rm\le n-|S|,
\quad\text{so}\quad2rm\le n.
\]
For \(n\ge3\), this forces \(r=1\); for even \(n\), \(2m=n\), and for odd \(n\), \(2m=n-1\) with \(n/(2m)<2\). Therefore \(S\) is a single cyclic arc, and \(m\le |S|\le n-m\) forces one of the two balanced lengths. Conversely, Step 2 proves equality for every such arc.

**4. General real-signal equality.** Write the distinct levels of a nonconstant real signal as \(c_0<\cdots<c_q\), and put \(S_j=\{i:f(i)\ge c_j\}\) for \(1\le j\le q\). The exact layer-cake decomposition and graph coarea formula are
\[
f=c_0\mathbf1+\sum_{j=1}^{q}(c_j-c_{j-1})\mathbf1_{S_j},
\qquad V(f)=\sum_{j=1}^{q}(c_j-c_{j-1})|\partial S_j|.
\]
If equality holds in (4), every \(S_j\) must be a balanced arc by Step 3. Moreover, the vector triangle inequality must be an equality. Because all nonzero displacement weights are positive, \((I-P_p)\mathbf1_S\) is strictly positive on \(S\) and strictly negative on its complement for any nontrivial \(S\). If two nested nontrivial superlevel sets are distinct, a vertex in their difference produces opposite strict signs, contradicting equality in the \(\ell^1\) triangle inequality. All \(S_j\) therefore coincide, and \(f\) has exactly two levels. This proves the complete family.

**5. Heat kernel and finite Fourier series.** The cycle Laplacian has Fourier eigenvalues \(\lambda_{n,k}=4\sin^2(\pi k/n)\). Thus its heat kernel is
\[
p_t(d):=H_t(0,d)=\frac1n\sum_{k=0}^{n-1}
 e^{-\lambda_{n,k}t}e^{2\pi ikd/n}.
\]
For \(t>0\), every matrix entry is strictly positive: the continuous-time nearest-neighbor walk can reach any vertex via a positive-probability finite path. Step 4 applies, and the first formula of (2) follows from (1).

**6. Explicit distance transform and Bernstein law.** Let \(h(d)=h_n(d)\), and let \(\Delta h(d)=h(d+1)+h(d-1)-2h(d)\). If \(n=2m\), then \(\Delta h=2\delta_0-2\delta_m\). If \(n=2m+1\), then \(\Delta h=2\delta_0-\delta_m-\delta_{m+1}\). For each nonzero Fourier frequency \(k\), this gives
\[
-\lambda_{n,k}\widehat h(k)=2a_{n,k},
\qquad \widehat h(k)=-\frac{2a_{n,k}}{\lambda_{n,k}},
\]
where \(\widehat h(k)=\sum_{d=0}^{n-1}h(d)e^{-2\pi ikd/n}\) and \(a_{n,k}\) is precisely the parity-dependent coefficient stated in the theorem. The average \(\widehat h(0)/n\) equals \(\lfloor n^2/4\rfloor/n\). Fourier inversion yields (2). For even \(n\), the nonzero \(a_{n,k}\) equal two at odd frequencies and zero at even frequencies; for odd \(n\), every \(a_{n,k}>0\) because \(|\cos(\pi k/n)|<1\). Differentiating the finite sum proves (3), including strict inequalities for all derivative orders. At zero, \(C'_n(0)=\Delta h(0)=2\), and \(C_n(0)=h(0)=0\). This finishes the proof.

## Verification

Run `python3 verify_cycle_heat.py` with Python 3, NumPy and SciPy. The standalone checker verifies the exact-integer displacement inequalities and cut equality implications for \(n=3,\ldots,12\), 3,006 additional exact-integer full-support asymmetric circulant-kernel/cut cases, 32,656 independently exponentiated heat/cut norm inequalities, 40 independent spectral formula evaluations, and 4,000 random real-signal bounds. Its successful diagnostics include `EXACT_GENERAL_CIRCULANT_KERNEL_AND_RIGIDITY_PASS 3006`, `EXACT_INTEGER_CUT_BOUNDS_AND_EQUALITY_PASS 81790`, `MATRIX_EXPONENTIAL_ALL_CUT_PASS 32656`, and `CYCLE_HEAT_BV_CHECKS_PASS`. These checks are finite and do not establish the theorem for every \(n\); Steps 1–6 do.

As transparent normalization examples, \(C_3(t)=\frac23(1-e^{-3t})\) and \(C_4(t)=1-e^{-2t}\). Each has initial derivative \(2\) and the stated long-time limit.

## Relationship to prior work

The cyclic Fourier and Bessel heat-kernel formula is classical. Karlsson and Neuhauser (2006) determine the cyclic heat kernel using a **degree-normalized** Laplacian (one-half the generator here), and Dowker (2012) treats Fourier and image expressions with the same unnormalized convention as here. Those kernel identities are prior art. Neither inspected work supplies (1), the general arbitrary-kernel two-level rigidity, or the positive-measure representation of the **sharp BV-to-counting-\(\ell^1\) approximation-error norm** in (2)–(3).

Related exact results concern different operator norms. The published cycle heat-Lipschitz computation determines \(\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}\), not \(\|I-H_t\|_{\mathrm{TV}\to\ell^1}\). The graph total-variation heat-contractivity theorem determines whether \(V(H_tf)\le V(f)\), not the sharp integrated approximation-error coefficient. Published cyclic two-tap Gini calculations use complete-pair Gini variation rather than adjacent-edge variation or vertex approximation error. The exact finite-path heat error is not a cycle formula: its boundary conditions and extremal cut geometry differ. These results do not imply (1) or (3) without additional arguments. General translation/triangle bounds and the graph coarea representation are standard; the contribution asserted is simultaneous sharpness for **every** cyclic displacement, the complete full-support equality classification, and the heat Bernstein spectrum.

## Limitations

The theorem is for finite cyclic sites with unweighted adjacent variation and counting-\(\ell^1\) error. The norm identity extends to all stochastic cyclic convolutions, but equality uniqueness assumes strictly positive weights at every nonzero displacement. It does not classify all extremizers for sparse-support kernels, weighted/nonuniform cycles, non-circulant matrices, or higher-dimensional tori. The heat specialization uses the unnormalized Laplacian. Historical priority is assessed against accessible records and the material inspected; unindexed equivalents remain possible. No independent mathematical audit is claimed.

## References

1. A. Karlsson and M. Neuhauser, *Heat Kernels, Theta Identities, and Zeta Functions on Cyclic Groups*, Contemporary Mathematics 394 (2006), 177–189. Author manuscript: https://www.unige.ch/math/folks/karlsson/heatcyclicfinal.pdf.
2. J. S. Dowker, *Heat-kernels on the discrete circle and interval*, arXiv:1207.2096v1, first public 2012-07-09. https://arxiv.org/abs/1207.2096.
3. *Exact graph-heat Lipschitz norms on cycles and a four-class short-time law*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-graph-heat-lipschitz-norms-on-cycles-and-a-four-class-shor--3067d825a457.
4. *Cut certificates for graph-variation heat contractivity and a complete unicyclic classification*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-cut-certificates-for-graph-variation-heat-contractivity-and-a-co--486d8f765599.
5. *Sharp cut-deficit and Gini contraction of cyclic two-tap averaging*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-cut-deficit-and-gini-contraction-of-cyclic-two-tap-averagi--100578f5c8f6.
