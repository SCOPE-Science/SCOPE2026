# Repeated richness uncertainty peaks from separated species abundances

## Finding

Let \(K_n\) be the number of distinct species seen in \(n\) independent draws with replacement from a fixed community of \(m\) species, each with strictly positive probability. A **strict variance peak** is an integer \(n\ge2\) satisfying
\[
\operatorname{Var}(K_n)>\operatorname{Var}(K_{n-1}),\qquad
\operatorname{Var}(K_n)>\operatorname{Var}(K_{n+1}).
\]

**Theorem.** Every one- or two-species community has at most one strict variance peak. For every integer \(m\ge3\), a strictly positive \(m\)-species probability vector exists for which \(n\mapsto\operatorname{Var}(K_n)\) has at least \(m-1\) distinct strict variance peaks, with consecutive peaks separated by arbitrarily low-variance sampling depths, while each peak has variance arbitrarily close to \(1/4\). Consequently, three is the sharp smallest number of species permitting two strict variance peaks, and the number of peaks has no universal bound independent of richness.

One explicit three-species witness is \((7/15,7/15,1/15)\), with strict variance peaks at sample sizes \(3\) and \(9\).

## Assumptions and scope

The community has finitely many species, \(m\ge1\), with probabilities \(p_i>0\) summing to one. The samples \(X_1,X_2,\ldots\) are iid with \(\Pr(X_t=i)=p_i\), and \(K_n=|\{X_1,\ldots,X_n\}|\) for integer \(n\ge1\). Sampling is with replacement. The theorem concerns the variance across repeated random samples at a fixed sample size, not variance of estimators across spatially dependent quadrats, without-replacement rarefaction, or functional richness.

An **arbitrarily deep valley** in the theorem means: for each fixed \(m\ge3\) and each \(\eta>0\), one may choose a vector admitting \(m-1\) strict peaks, each exceeding \(1/4-\eta\), and find a sample size strictly between each consecutive pair of peaks at which the variance is below \(\eta\). The limiting zero-variance endpoint after the last peak can also be made below \(\eta\). No claim is made that \(m-1\) is an upper bound for arbitrary \(m\)-species probability vectors.

## Proof

**1. Exact variance identity.** Set \(q_i=1-p_i\) and \(I_i(n)={\bf1}\{\text{species }i\text{ is observed by draw }n\}\). Then \(K_n=\sum_i I_i(n)\). The probability that species \(i\) is unseen is \(q_i^n\), and the probability that both distinct species \(i,j\) are unseen is \((1-p_i-p_j)^n\). Consequently,
\[
\begin{aligned}
V_n:=\operatorname{Var}(K_n)
&=\sum_{i=1}^{m}\big[q_i^n-q_i^{2n}\big]\\
&\quad+2\sum_{1\le i<j\le m}
\left[(1-p_i-p_j)^n-(q_iq_j)^n\right]. \tag{1}
\end{aligned}
\]
The last expression is an identity for all positive probability vectors and all integer \(n\ge1\); its covariance terms are nonpositive. It is not a new variance formula.

**2. The sharp small-richness obstruction.** If \(m=1\), \(K_n=1\) deterministically and \(V_n=0\). For \(m=2\) with probabilities \(p,1-p\), write
\[
a_n=\Pr(K_n=2)=1-p^n-(1-p)^n.
\]
The sequence \(a_n\) increases strictly from \(a_1=0\) to one. Moreover \(K_n=1+\operatorname{Bernoulli}(a_n)\), so \(V_n=a_n(1-a_n)\). As this quadratic increases up to \(a_n=1/2\) and decreases thereafter, the sequence has at most one strict local maximum (possibly a two-point plateau). Thus no one- or two-species vector has two strict variance peaks.

**3. Separated-abundance construction.** Fix an integer \(m\ge3\). For \(0<\varepsilon<1/3\), define
\[
p_0=1-\sum_{i=1}^{m-1}\varepsilon^i,\qquad
p_i=\varepsilon^i\quad(1\le i\le m-1).
\]
All \(m\) probabilities are strictly positive because \(\sum_{i\ge1}\varepsilon^i<1/2\). For \(1\le j\le m-1\), put
\[
h_j(\varepsilon)=\left\lfloor\frac{\log 2}{\varepsilon^j}\right\rfloor,
\qquad
v_j(\varepsilon)=\left\lfloor\varepsilon^{-(j+1/2)}\right\rfloor,
\qquad v_0=1.
\]
For small enough \(\varepsilon\), these integers satisfy
\[
v_0<h_1<v_1<h_2<v_2<\cdots<h_{m-1}<v_{m-1}.
\]
For any fixed \(j\), at depth \(h_j\), the common species \(0\) and rarer-indexed species \(1,\ldots,j-1\) have been observed with probability tending to one, because \(h_jp_i\to\infty\) for \(i<j\). No species \(i>j\) has been observed with probability tending to one, since \(h_jp_i\to0\); this follows by the union bound \(\Pr(I_i(h_j)=1)\le h_jp_i\). At the marginal species \(j\),
\[
\Pr(I_j(h_j)=0)=(1-\varepsilon^j)^{h_j}\longrightarrow 1/2.
\]
Therefore \(K_{h_j}\) converges in distribution to \(j+\operatorname{Bernoulli}(1/2)\) as \(\varepsilon\downarrow0\). Since \(1\le K_n\le m\), moments also converge and
\[
V_{h_j}\longrightarrow1/4.\tag{2}
\]
At depth \(v_j\), for \(i\le j\) one has \(v_jp_i\to\infty\), whereas for \(i>j\), \(v_jp_i\to0\). Hence \(K_{v_j}\) converges in probability to the deterministic value \(j+1\), for every \(1\le j\le m-1\) (the final case means every species has appeared). Therefore
\[
V_{v_j}\longrightarrow0,\qquad V_{v_0}=V_1=0.\tag{3}
\]
Fix \(\eta\in(0,1/10)\). The finitely many limits (2) and (3) show that for every sufficiently small \(\varepsilon>0\), all \(m-1\) high points satisfy \(V_{h_j}>1/4-\eta\), and all the intervening low points satisfy \(V_{v_j}<\eta\). Every finite integer interval \([v_{j-1},v_j]\) therefore has an interior variance maximizer, and the intervals have disjoint interiors. This gives \(m-1\) separated local maxima, which we next ensure are strict.

**4. Strictness is achievable.** For fixed positive integer \(n\), formula (1) makes \(V_{n+1}(\varepsilon)-V_n(\varepsilon)\) a polynomial in \(\varepsilon\) with integer coefficients. For fixed \(n\ge2\), as \(\varepsilon\downarrow0\), the species with probability \(\varepsilon\) is the only rare species seen to first order. The event that it is present alongside the dominant species has probability \(n\varepsilon+O(\varepsilon^2)\); the event of three or more observed species has probability \(O(\varepsilon^2)\). Thus \(V_n=n\varepsilon+O(\varepsilon^2)\) for \(n\ge2\), while \(V_1=0\). In particular,
\[
V_2-V_1=2\varepsilon+O(\varepsilon^2),\qquad
V_{n+1}-V_n=\varepsilon+O(\varepsilon^2)\ (n\ge2).
\]
No one of these difference polynomials is identically zero. Choosing \(\varepsilon\) transcendental and sufficiently small therefore makes \(V_{n+1}\ne V_n\) for every integer \(n\ge1\), simultaneously. Every interior maximizer from step 3 must then exceed both its immediate neighbors strictly. This establishes the arbitrary multiplicity and valley-depth claims, not merely the existence of many non-strict plateaus.

**5. Exact three-species witness.** For \(\boldsymbol p=(7,7,1)/15\), formula (1) simplifies to
\[
\begin{aligned}
V_n={}&2(8/15)^n+(14/15)^n+2(1/15)^n+4(7/15)^n\\
&-4(8/15)^{2n}-(14/15)^{2n}-4(112/225)^n.
\end{aligned}
\]
Exact rational evaluation gives
\[
\begin{array}{ll}
V_3-V_2=38864/1265625>0,&V_3-V_4=4074196/284765625>0,\\
V_9-V_8=7455903885441788/6568408355712890625>0,&
V_9-V_{10}=10874721037204676764/36947297000885009765625>0.
\end{array}
\]
Thus the nonadjacent strict maxima at \(n=3\) and \(n=9\) exist with just three species, and step 2 proves that three is minimal. \(\square\)

## Verification

The standalone `checker.py` recomputes the four rational peak inequalities from (1) and independently obtains the same variances by propagating exact probabilities over every observed-species subset for sample sizes \(1\) through \(11\). It additionally tests the multiscale construction at selected sample sizes in four-species communities. The proof of arbitrarily many peaks is analytic; finite numerical tests alone would not establish it. Run using `python3 checker.py` with the Python standard library only.

## Relationship to prior work

Heck, van Belle and Simberloff (1975) derived exact expected richness and variance for finite-collection rarefaction without replacement; no novelty is claimed for indicator-variable moment identities. Ugland, Gray and Ellingsen (2003) developed the sample-based species-accumulation variance formula and discussed spatial sample heterogeneity. Bogachev, Gnedin and Yakubovich (2006) proved deep boundedness and limiting-variance results for infinitely many occupied boxes under iid draws, including oscillatory geometric-frequency regimes. These results motivate the present question but do not explicitly establish the minimum finite support of a double variance peak or the \(m-1\)-peak separated-scale construction with near-\(1/4\) peaks and vanishing valleys. Infinite-frequency nonconvergence may already imply arbitrarily many peaks after finite truncation, so **unbounded finite peak multiplicity alone is not asserted as a new independent contribution**. The claim is the sharper cardinality-resolved, strict, finite-species phenomenon.

The same-species-count expected-richness *ranking reversals* and the *fixed-budget functional-group* uncertainty peaks address different statistics and sampling mechanisms: neither states the above exact observed-richness variance peaks under iid draws. Closely related finite-urn and sampling literature may contain equivalent formulations not located in the inspected sources; historical novelty is provisional.

## Limitations

This is a theoretical iid-with-replacement sampling result. Real ecological samples may be spatially or temporally dependent and have imperfect identifications. The proof supplies neither an upper bound on the total number of strict peaks for an arbitrary fixed \(m\) nor a guarantee of widely separated modes for empirical abundance vectors. The separation construction may require extreme abundance ratios and very large sample sizes. All results remain subject to independent scientific review and broader historical-priority checks.

## References

1. Heck, K. L. Jr., van Belle, G. and Simberloff, D. (1975). *Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size*. Ecology 56:1459–1461. https://doi.org/10.2307/1934716 (first published 1975-10-01; accessible abstract, full text not obtained).
2. Ugland, K. I., Gray, J. S. and Ellingsen, K. E. (2003). *The species–accumulation curve and estimation of species richness*. Journal of Animal Ecology 72:888–897. https://doi.org/10.1046/j.1365-2656.2003.00748.x (first published 2003-08-15; accessible full text and Appendix I).
3. Bogachev, L. V., Gnedin, A. V. and Yakubovich, Yu. V. (2006). *On the variance of the number of occupied boxes*. arXiv:math/0609498 (posted 2006-09-18; accessible full text), https://arxiv.org/abs/math/0609498.
4. Archibald, M., Knopfmacher, A. and Prodinger, H. (2006). *The number of distinct values in a geometrically distributed sample*. European Journal of Combinatorics 27:1059–1081. https://doi.org/10.1016/j.ejc.2006.06.007 (accessible abstract; author-hosted PostScript full text could not be inspected).
