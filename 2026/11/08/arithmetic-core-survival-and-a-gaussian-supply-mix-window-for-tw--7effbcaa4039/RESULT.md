# Arithmetic core survival and a Gaussian supply-mix window for two-quota matroid packing games

## Finding

Fix distinct integers \(r,s\geq2\). Resources have two types, \(A\) and \(B\). One complete productive bundle requires exactly \(r\) resources of type \(A\) and \(s\) of type \(B\); disjoint bundles generate one unit of transferable worth each. The owners of the individual resources form a cooperative game. For fixed numbers \(a\geq r\) and \(b\geq s\) of resources, write
\[
q=\min\{\lfloor a/r\rfloor,\lfloor b/s\rfloor\}.
\]
**Deterministic arithmetic criterion.** A core allocation exists precisely when \(a=qr\) or \(b=qs\). If \(q=1\), the entire core consists of nonnegative, unit-sum allocations supported on the resource types with equality. If \(q\geq2\), every core allocation pays zero to all nonsaturated types and pays a constant \(\lambda_A/r\) to each \(A\)-resource when \(a=qr\), and a constant \(\lambda_B/s\) to each \(B\)-resource when \(b=qs\). Here the nonnegative coefficients for saturated types sum to one. This is a complete description, including the one-bundle exception.

**Random supply law.** Independently classify \(m\) labeled resources as type \(A\) with probability \(p_m\) and type \(B\) otherwise; condition on at least \(r\) type-\(A\) and at least \(s\) type-\(B\) resources. Define
\[
p_0=\frac{r}{r+s},\qquad \sigma=\sqrt{p_0(1-p_0)}=\frac{\sqrt{rs}}{r+s}.
\]
If \(p_m=p_0+\beta/\sqrt m+o(m^{-1/2})\) for fixed real \(\beta\), the probability of a nonempty core converges to
\[
\boxed{\frac{\Phi(-\beta/\sigma)}{r}+\frac{\Phi(\beta/\sigma)}{s}},
\]
where \(\Phi\) is the standard-normal distribution function. In particular, when \((r,s)=(2,3)\), the critical curve is
\[
\frac13+\frac16\Phi\left(-\frac{5\beta}{\sqrt6}\right),
\]
and its central value is \(5/12\). With any fixed \(p<p_0\), the probability instead converges to \(1/r\); with fixed \(p>p_0\), it converges to \(1/s\). Thus the transition occurs on the \(m^{-1/2}\) supply-mix scale and retains nontrivial arithmetic randomness even far from the balance point.

The exact finite probability is specified under **Verification** below, with no asymptotic approximation needed.

## Assumptions and scope

Each resource belongs to a distinct player. For a coalition \(S\), let \(a(S)\) and \(b(S)\) count its resources of types \(A\) and \(B\). Define
\[
v(S)=\min\left\{\left\lfloor\frac{a(S)}r\right\rfloor,\left\lfloor\frac{b(S)}s\right\rfloor\right\}.
\]
This is the base-packing game of the two-block partition matroid with quotas \(r,s\), provided the full ground set has at least \(r\) and \(s\) elements of the respective types. A payoff vector \(x\) belongs to the core when \(x_i\geq0\), \(\sum_i x_i=v(N)=q\), and \(\sum_{i\in S}x_i\geq v(S)\) for every coalition \(S\). There are no side payments outside this game and no correlations in the random type assignments. The quota pair is fixed as \(m\to\infty\), rather than growing with \(m\).

## Proof

**1. Reduction to base constraints.** A base is any subset containing exactly \(r\) elements of type \(A\) and \(s\) of type \(B\). Every coalition of value \(k\) contains \(k\) disjoint bases. Therefore nonnegativity, total payoff \(q\), and the inequalities \(x(B)\geq1\) for all bases \(B\) are equivalent to the complete set of core inequalities.

**2. Saturation criterion and full core geometry.** Let \(w_A,w_B\) denote the sums of the proposed nonnegative payoffs within the two types. Choose a base uniformly among all \(\binom ar\binom bs\) bases. By symmetry,
\[
\mathbb E[x(B)]=\frac r a w_A+\frac s b w_B
\leq \frac{w_A+w_B}{q}=1.
\]
The core inequalities demand \(x(B)\geq1\) for every base, hence equality throughout. Each type with \(a>qr\), respectively \(b>qs\), has strict coefficient \(r/a<1/q\), respectively \(s/b<1/q\), and therefore must receive total payoff zero. At least one type must be saturated or all payoffs would vanish, contrary to \(w_A+w_B=q\geq1\).

Moreover, every base must have payoff exactly one. If \(q\geq2\), a saturated type contains more than its quota, so replacing one resource by another of the same type in a base proves that all resources of that type have equal payoffs. Writing these common payoffs as \(\lambda_A/r\) and \(\lambda_B/s\), the base equality gives \(\sum\lambda_j=1\) over the saturated types. If \(q=1\), each saturated type contains exactly its quota, so all its resources occur in every base; no within-type equalization follows. Any nonnegative unit-sum payoff supported on the saturated types then pays every base one. Finally, every vector so described pays at least one per disjoint base, proving all coalition inequalities. This proves necessity and sufficiency, including the full core description.

**3. An exact binomial event.** Put \(X_m=a\), \(b=m-a\), and \(\tau_m=mr/(r+s)\). On the conditioning event \(E_m=\{r\leq X_m\leq m-s\}\), the saturation criterion is equivalent to
\[
\big\{X_m\leq\tau_m,\ X_m\equiv0\pmod r\big\}
\ \cup\ 
\big\{X_m\geq\tau_m,\ m-X_m\equiv0\pmod s\big\}.
\]
Indeed, when \(X_m\) is a multiple of \(r\), it is a saturated bottleneck if and only if \(X_m/r\leq(m-X_m)/s\), and similarly for the opposite type. Equality may cause the two events to overlap, but only at the single value \(X_m=\tau_m\).

**4. Modular equidistribution near the binomial threshold.** For a fixed positive integer \(d\), if \(X\sim\operatorname{Binomial}(m,p)\) and \(p\) remains in any fixed compact subinterval of \((0,1)\), then for every integer threshold \(T\) and residue \(c\),
\[
\Pr(X\leq T,\ X\equiv c\pmod d)
=\frac1d\Pr(X\leq T)+O_d(m^{-1/2}).
\]
The analogous assertion holds for an upper tail and for the residue of \(m-X\). For completeness, divide consecutive integers into blocks of length \(d\). The absolute difference between the mass of any fixed residue in a block and one \(d\)-th of that block's total mass is bounded by \(d\) times the variation of the binomial mass across the block. The sum of these variations over complete blocks is bounded by the global total variation of a unimodal binomial mass function, namely at most twice its maximum point mass. The one incomplete block contributes at most \(d\) times the maximum point mass. Stirling's bound gives a uniform \(O(m^{-1/2})\) maximum point mass. This establishes the asserted error.

**5. Gaussian window.** For \(p_m=p_0+\beta/\sqrt m+o(m^{-1/2})\), the triangular-array central limit theorem gives
\[
\Pr(X_m\leq\tau_m)\longrightarrow \Phi(-\beta/\sigma),
\qquad
\Pr(X_m\geq\tau_m)\longrightarrow \Phi(\beta/\sigma).
\]
The potential overlap in Step 3 has probability at most the maximum binomial point mass \(O(m^{-1/2})\). Modular equidistribution makes its two parts asymptotically one \(r\)-th of the lower-tail mass and one \(s\)-th of the upper-tail mass. Since \(p_m\to p_0\in(0,1)\), a binomial large-deviation bound gives \(\Pr(E_m^c)\to0\) exponentially. Conditioning therefore does not change the limit. For fixed \(p\ne p_0\), binomial concentration puts all mass on the appropriate side of \(\tau_m\), and the same modular argument yields \(1/r\) or \(1/s\). This completes the proof.

## Verification

For any finite \(m\geq r+s\) and \(0<p<1\), define \(w_m(a)=\binom ma p^a(1-p)^{m-a}\). The exact conditional nonempty-core probability is
\[
\frac{\displaystyle\sum_{a=r}^{m-s} w_m(a)\mathbf1\!\left[\big(a(r+s)\leq mr\ \land\ a\equiv0\pmod r\big)\ \lor\ \big(a(r+s)\geq mr\ \land\ m-a\equiv0\pmod s\big)\right]}{\displaystyle\sum_{a=r}^{m-s}w_m(a)}.
\]
The event is a union, not a sum of indicators; the exact balance case is counted once. The standalone `verify.py` uses independently enumerated coalition constraints in a linear program, integer event identities, exact rational finite binomial sums, and finite-size asymptotic checks. Running `python verify.py` with SciPy available completed 405 LP core comparisons, 9,612 event equivalences, 38 exact rational probability comparisons, and nine numerical convergence checks. These finite checks corroborate the algebra; they are not the proof of the infinite-population limit.

## Relationship to prior work

Liu, Xiao, Chen and Fang, *Matroid Packing Games: The Core and the Nucleolus* (first public September 29, 2026), define the full deterministic matroid-base-packing cooperative game and prove general core/nonempty-core and nucleolus algorithms. Their general deterministic theorems cover the core decision problem here; the elementary two-quota saturation characterization is a specialization and is not claimed as an independent general algorithmic advance. The additional statement here concerns a randomly generated partition matroid: the exact finite probability and the sharp \(m^{-1/2}\) Gaussian interpolation between distinct arithmetic survival frequencies. These stochastic statements are not provided by the inspected sections of that paper. General results on binomial central limits and modular classes are used explicitly rather than presented as novel lemmas.

## Limitations

The probability law concerns two resource types, fixed integer quotas, independent identically typed resources, and conditioning on the partition matroid having the desired rank. It does not address correlated supply, growing quotas, three or more types, or the distribution of nucleolus payments when the core is empty. The deterministic core characterization follows from a broader published matroid-packing framework; the originality claim is restricted to the exact random-model law and critical supply-mix asymptotics. Search cannot exclude all unindexed equivalent stochastic work, and no independent audit has been performed.

## References

1. P. Liu, H. Xiao, X. Chen, Q. Fang, *Matroid Packing Games: The Core and the Nucleolus*, arXiv:2609.37278, first submitted 2026-09-29, https://arxiv.org/abs/2609.37278.
2. M. Baiou, F. Barahona, *Network strength games: The core and the nucleolus*, Mathematical Programming 180 (2020), 117–136, cited for historical context in arXiv:2609.37278.
3. Standard classical results used: the de Moivre–Laplace binomial central limit theorem, binomial concentration inequalities, and the Stirling point-mass bound.
