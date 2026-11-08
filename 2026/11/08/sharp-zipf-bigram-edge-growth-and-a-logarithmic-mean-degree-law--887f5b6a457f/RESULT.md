# Sharp Zipf bigram edge growth and a logarithmic mean-degree law

## Finding

Let \(a>1\), \(\gamma=1/a\), and \(c=1/\zeta(a)\). From independent symbols \(X_1,X_2,\ldots\) with \(\Pr(X_t=i)=c i^{-a}\) for \(i\ge1\), construct the directed range-renewal graph from the distinct consecutive ordered pairs \((X_t,X_{t+1})\), and its undirected projection from unordered pairs. Both graphs retain self-loops. Denote their edge counts after \(n\) symbols by \(E_n^{\to}\) and \(E_n^{\leftrightarrow}\); let \(V_n\) be the number of observed symbols. Let \(\gamma_{\mathrm E}\) be Euler's constant and \(\psi\) the logarithmic derivative of Euler's Gamma function. Then

\[
\mathbb E E_n^{\to}=\Gamma(1-\gamma)c^{2\gamma}n^\gamma\left[\gamma\log n+2\gamma\log c+2\gamma_{\mathrm E}-1-\gamma\psi(1-\gamma)\right]+O_a(n^{\gamma/2}).
\]

For both edge counts, the following limits hold almost surely and in \(L^2\):

\[
\frac{E_n^{\to}}{n^\gamma\log n}\longrightarrow\gamma\Gamma(1-\gamma)c^{2\gamma},\qquad
\frac{E_n^{\leftrightarrow}}{n^\gamma\log n}\longrightarrow2^{\gamma-1}\gamma\Gamma(1-\gamma)c^{2\gamma}.
\]

In particular, the directed and undirected mean degrees diverge at explicit logarithmic rates:

\[
\frac{E_n^{\to}}{V_n\log n}\longrightarrow\gamma c^\gamma,\qquad
\frac{2E_n^{\leftrightarrow}}{V_n\log n}\longrightarrow 2^\gamma\gamma c^\gamma
\quad\text{almost surely}.
\]

This is a joint theorem about the edge counts and the induced mean-degree growth of one and the same sequence-generated graph; the two orientations are not independent models.

## Assumptions and scope

Fix any real \(a>1\) throughout, with the exact normalized Zipf distribution \(\pi_i=c i^{-a}\) on the **infinite** positive-integer alphabet. The graph includes each distinct transition once, even if repeatedly observed. A self-transition adds one loop edge; the undirected projection identifies \((i,j)\) with \((j,i)\). Natural logarithms are used. The asymptotic constants and the \(O_a\)-remainder may depend on \(a\), but not on \(n\). No general regularly varying sampling law, growing exponent, finite-alphabet truncation, central limit theorem, or second-order constant for undirected edges is asserted.

## Proof

**1. A uniform approximation for distinct non-loop directed pairs.** Write \(N=n-1\), \(p_{ij}=\pi_i\pi_j\), and \(N_{ij}=\sum_{t=1}^{N}\mathbf1\{(X_t,X_{t+1})=(i,j)\}\). For \(i\ne j\), indicators at non-neighboring indices are independent, while two neighboring indicators for this *same* ordered pattern cannot both be one. The elementary dependency-graph Stein–Chen Poisson bound gives, for an absolute constant \(C\),

\[
\left|\Pr(N_{ij}>0)-(1-e^{-Np_{ij}})\right|\le C\min(1,(Np_{ij})^{-1})Np_{ij}^2\le Cp_{ij}.
\]

Here the dependency neighborhoods are \(\{t-1,t,t+1\}\), the usual \(b_1\) term is at most \(3Np_{ij}^2\), the \(b_2\) adjacent-joint term is zero, and the long-range \(b_3\) term vanishes. The bound also covers the zero-occurrence probability. Sum over all ordered \(i\ne j\): the aggregate error is bounded because \(\sum_{i,j}p_{ij}=1\). The diagonal loop count in either the true or the Poissonized expression is at most

\[
\sum_{i\ge1}\min(1,N\pi_i^2)=O_a(N^{\gamma/2}).
\]

Consequently, with \(S(t)=\sum_{i,j\ge1}(1-e^{-t\pi_i\pi_j})\),

\[
\mathbb E E_n^{\to}=S(N)+O_a(N^{\gamma/2}+1).
\]

**2. Exact second-order occupancy expansion.** Set \(B=(tc^2)^\gamma\). Group the pairs by their product \(m=ij\). Their multiplicity is the divisor function \(d(m)\), whence

\[
S(t)=\sum_{m\ge1}d(m)\bigl(1-e^{-(B/m)^a}\bigr).
\]

Let \(D(x)=\sum_{m\le x}d(m)\). Dirichlet's hyperbola argument, using \(\sum_{r\le x}r^{-1}=\log x+\gamma_{\mathrm E}+O(x^{-1})\), gives

\[
D(x)=x\log x+(2\gamma_{\mathrm E}-1)x+O(\sqrt x),\quad x\ge1.
\]

For \(g(u)=1-e^{-u^{-a}}\) we have \(-g'(u)=a u^{-a-1}e^{-u^{-a}}\). Stieltjes summation by parts gives

\[
S(t)=\int_0^\infty D(Bu)\bigl(-g'(u)\bigr)\,du.
\]

The contribution from \(Bu<1\) to the displayed main terms is exponentially small; the contribution of the \(O(\sqrt{Bu})\) divisor remainder is \(O_a(B^{1/2})\), since \(\int_0^\infty\sqrt{u}(-g'(u))du<\infty\) when \(a>1\). Substituting \(z=u^{-a}\) yields

\[
\int_0^\infty u(-g'(u))du=\Gamma(1-\gamma),\qquad
\int_0^\infty u\log u(-g'(u))du=-\gamma\Gamma'(1-\gamma).
\]

Thus

\[
S(t)=\Gamma(1-\gamma)B\left[\log B+2\gamma_{\mathrm E}-1-\gamma\psi(1-\gamma)\right]+O_a(B^{1/2}).
\]

Finally \(\log B=\gamma\log t+2\gamma\log c\), and replacing \(t=n-1\) by \(t=n\) perturbs the expression by \(O_a(n^{\gamma-1}\log n)=o_a(n^{\gamma/2})\). This proves the stated directed expectation with its constant-order-in-\(n^\gamma\) term and error estimate.

**3. Undirected orientation merger.** For a fixed \(i<j\), an unordered edge appears whenever either ordered transition occurs. Its indicator at one time has mean \(s_{ij}=2\pi_i\pi_j\); the probability that this edge indicator is one at two successive times equals \(\pi_i\pi_j(\pi_i+\pi_j)\), due exactly to the patterns \((i,j,i)\) and \((j,i,j)\). The same dependency-graph Poisson bound therefore gives

\[
\left|\Pr(\{i,j\}\text{ appears})-(1-e^{-Ns_{ij}})\right|
\le C\min(1,Ns_{ij})(s_{ij}+\pi_i+\pi_j).
\]

For any \(t>0\), the Zipf occupancy estimate

\[
\sum_{j\ge1}\min(1,t\pi_j)\le C_a t^\gamma
\]

follows by splitting the sum at \(j\asymp t^\gamma\), with the small-\(t\) case handled by \(t\le t^\gamma\). Since \(s_{ij}\le\pi_i+\pi_j\) and \(\sum_i\pi_i^{1+\gamma}<\infty\), summing the preceding Poisson errors over \(i<j\) gives \(O_a(N^\gamma)\). Loops contribute only \(O_a(N^{\gamma/2})\). Hence

\[
\mathbb E E_n^{\leftrightarrow}=\frac12 S(2N)+O_a(N^\gamma)
=2^{\gamma-1}\gamma\Gamma(1-\gamma)c^{2\gamma}n^\gamma\log n+O_a(n^\gamma).
\]

**4. A uniform self-bounding variance estimate.** For either choice of orientation, let \(T=T_n\) be the distinct-edge count. Remove from its defining set the at most two transitions touching input position \(r\), and call the resulting count \(T_r\). Then \(T_r\) depends only on the symbols other than \(X_r\), and \(A_r=T-T_r\) satisfies \(0\le A_r\le2\). Moreover, for each distinct edge, all its occurrences can touch at most two common input positions; therefore \(\sum_r A_r\le2T\) *pointwise*. Let \(T^{(r)}\) be obtained by independently resampling \(X_r\). Since both \(T\) and \(T^{(r)}\) contain \(T_r\), and since \((u-v)^2\le4(u+v)\) for \(0\le u,v\le2\), Efron–Stein gives

\[
\operatorname{Var}(T)\le\frac12\sum_r\mathbb E[(T-T^{(r)})^2]
\le4\sum_r\mathbb E A_r\le8\mathbb ET.
\]

This bound is valid for arbitrary i.i.d. symbol distributions, not just Zipf laws. It proves \(L^2\) convergence in the two displayed edge-count laws.

To obtain almost-sure convergence, take \(n_j=\lfloor(1+\varepsilon)^j\rfloor\). The bound above and \(\mathbb ET_{n_j}\asymp n_j^\gamma\log n_j\) make the Chebyshev probabilities summable. Borel–Cantelli gives \(T_{n_j}/\mathbb ET_{n_j}\to1\) a.s. Because both \(T_n\) and its expectation are nondecreasing, interpolation between successive grid points bounds the full-sequence liminf and limsup by \((1+\varepsilon)^{-\gamma}\) and \((1+\varepsilon)^\gamma\). Let \(\varepsilon\downarrow0\) along a countable sequence. This proves the two strong laws.

**5. Degree conversion.** Classical infinite-occupancy asymptotics give \(V_n/(\Gamma(1-\gamma)c^\gamma n^\gamma)\to1\) almost surely, by the standard variance estimate \(\operatorname{Var}(V_n)\le\mathbb EV_n\) and the same monotone-grid argument. Divide the two edge-count laws by this vertex-count law. The undirected mean degree counts each nonloop edge twice; self-loops affect the total degree by \(O(n^{\gamma/2})\), negligible relative to \(n^\gamma\log n\), whatever conventional loop-degree convention is adopted. The displayed mean-degree limits follow.

## Verification

The self-contained `checker.py` enumerates every source word of length up to six on a nonuniform three-symbol alphabet and up to seven on a nonuniform binary alphabet. It checks exact rational first and second moments, exact edge-event expansions, the pointwise deletion inequality, and the variance bound for both directed and undirected counts. Running `python checker.py` produced **17,939 passing exact assertions**. Independent Zipf simulations at \(a=2\), sizes \(10^4\), \(5\cdot10^4\), and \(10^5\), with 18 fixed-seed samples per size, gave directed empirical means approximately 566.2, 1444.5, and 2174.2 versus the corresponding two-term formula 565.0, 1457.3, and 2179.0; these simulations are diagnostics, not proofs. The infinite-alphabet, Poisson-approximation, divisor and almost-sure arguments above are analytic.

## Relationship to prior work

Chen, Xie and Ying (arXiv:1305.1829, first released 2013) establish range and fixed-degree strong laws for the sequence-generated graph. Xie and Zhou (arXiv:2609.05290, first released September 4, 2026, MSC2020 60C05) establish sharp **iterated-limit** degree-distribution tails, but explicitly leave growing-degree windows open and do not state the finite-size edge-count expansion above. Archibald et al. (arXiv:1806.04962) and Louchard, Schachinger and Ward (arXiv:2203.14773) study the *same adjacent-pair observable* for a **geometric**, rather than power-law Zipf, alphabet and do not supply the \(n^\gamma\log n\) law or its Zipf-specific second term. General Stein–Chen word-pattern and infinite-occupancy results are used as known ingredients, not claimed as new. Earlier fixed-degree limits alone cannot be summed over growing degrees without uniformity; the direct product-frequency/divisor argument provides that missing finite-size bridge.

## Limitations

This is not a central limit theorem, a full large-deviation statement, or a result for all regularly varying probabilities. The undirected expectation is known here only through an \(O_a(n^\gamma)\) remainder; its second-order coefficient is not resolved. The second-term directed formula requires exact Zipf probabilities. A broader general theorem for distinct word patterns and heavy-tail alphabets could contain the result; the literature comparisons listed in the accompanying review reduce, but cannot eliminate, that historical-priority risk. Finite enumeration cannot establish the infinite proof.

## References

1. J. Xie and Y. Zhou, *Universal Exponent-Two Degree Laws in Range-Renewal Networks*, arXiv:2609.05290 (first posted 2026-09-04), https://arxiv.org/html/2609.05290.
2. X.-X. Chen, J.-S. Xie and J. Ying, *Range-Renewal Processes: SLLN, Power Law and Beyonds*, arXiv:1305.1829 (2013), https://arxiv.org/html/1305.1829.
3. M. Archibald, A. Blecher, C. Brennan, A. Knopfmacher, S. Wagner and M. D. Ward, *The number of distinct adjacent pairs in geometrically distributed words*, arXiv:1806.04962, https://arxiv.org/pdf/1806.04962.
4. G. Louchard, W. Schachinger and M. D. Ward, *The number of distinct adjacent pairs in geometrically distributed words: a probabilistic and combinatorial analysis*, arXiv:2203.14773, https://arxiv.org/pdf/2203.14773v4.
5. R. Arratia, L. Goldstein and L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Ann. Probab. **17** (1989), 9–25.
6. N. H. Bingham, C. M. Goldie and J. L. Teugels, *Regular Variation*, Cambridge University Press (1987), for occupancy regular variation context.
