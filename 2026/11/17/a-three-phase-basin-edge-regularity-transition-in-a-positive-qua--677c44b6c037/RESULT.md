# A three-phase basin-edge regularity transition in a positive quadratic map

## Finding

**Theorem (sharp pure-axis boundary regularity).** Fix real parameters \(a,b>0\) satisfying \(a<2b\) and \(b<2a\). Consider the quadratic map on the nonnegative quadrant
\[
 H(x,y)=\left(\frac a2 x(x+2y),\frac b2 y(y+2x)\right).
\]
For each composition \(s\in[0,1]\), a unique critical total mass \(R(s)>0\) separates convergence to zero from escape to infinity along the ray \((x,y)=t(1-s,s)\). On the critical curve with \(0<s<1\), the orbit converges to the unique positive fixed point
\[
 E=\left(\frac{2(2a-b)}{3ab},\frac{2(2b-a)}{3ab}\right).
\]
The endpoints of this curve are \((2/a,0)\) and \((0,2/b)\). These global separator and convergence facts are used as background and reconstructed below; the contribution here is the following **sharp endpoint classification**.

At the first endpoint write \(s\downarrow0\), define the invasion multiplier \(\lambda=2b/a\in(1,4)\), and put
\[
 \Delta(s)=\log\frac{R(0)}{R(s)},\qquad R(0)=\frac2a.
\]
There are three mutually exclusive laws:
\[
 \boxed{\begin{array}{ll}
 1<\lambda<2:&\displaystyle\lim_{s\downarrow0}\frac{\Delta(s)}s=\frac{\lambda}{2-\lambda},\\[6pt]
 \lambda=2:&\displaystyle\lim_{s\downarrow0}\frac{\Delta(s)}{s\log(1/s)}=\frac1{\log2},\\[6pt]
 2<\lambda<4:&\displaystyle 0<\liminf_{s\downarrow0}\frac{\Delta(s)}{s^{\alpha}}
 \le\limsup_{s\downarrow0}\frac{\Delta(s)}{s^{\alpha}}<\infty,
 \quad\alpha=\frac{\log2}{\log\lambda}\in(0,1).
 \end{array}}
\]
Here the third assertion is **two-sided sharp power comparability**, not a claim that the normalized quotient converges. At the second endpoint use \(1-s\downarrow0\) and exchange \(a,b\), so its multiplier is \(2a/b\). The same three alternatives hold there. Since \(R(0)-R(s)=R(0)\Delta(s)(1+o(1))\), these laws also give the actual radial deficit of the basin boundary.

In particular, for unequal positive coefficients exactly one pure-axis endpoint has a finite, nonzero one-sided radial derivative and the other has a sharp non-Lipschitz fractional-power edge. For equal coefficients both endpoints are non-Lipschitz with the universal logarithmic correction. The threshold between these geometries is the coincidence of the transverse and radial multipliers \(\lambda=2\) at a pure-axis fixed point.

## Assumptions and scope

The map acts on \(\mathbb R_{\ge0}^2\), and all statements use **discrete iteration time**. The coefficient chamber \(a<2b,\ b<2a\) is precisely the chamber with a strictly positive interior fixed point. The radial coordinate \(t=x+y\) is total mass, not Euclidean norm. The edge coordinate \(s=y/(x+y)\) is the fraction of the second component. The quantities \(\Delta(s)\) and the right-end analogue are measured along the basin separator, not arbitrary trajectories.

The last case determines the exact local scaling exponent but does not assert an exact leading coefficient or the absence of possible log-periodic modulation. No claim is made about the parameter-boundary cases \(a=2b\) or \(b=2a\), signed states, or perturbations of the quadratic map. The global radial-separator formula is known from earlier published work and is not claimed to be a new discovery.

## Proof

**1. Exact mass–composition decomposition.** For \(x+y=t>0\) put \(x=t(1-s)\), \(y=ts\), and define
\[
 h(s)=\frac12\left[a(1-s^2)+bs(2-s)\right],\qquad
 f(s)=\frac{bs(2-s)}{a(1-s^2)+bs(2-s)}.
\]
Direct substitution gives \(t'=h(s)t^2\), \(s'=f(s)\). The positive function \(h\) is bounded above and away from zero on \([0,1]\), and \(f(0)=0\), \(f(1)=1\). Its unique interior fixed composition is
\[
 s_*=(2b-a)/(a+b)\in(0,1).
\]
Indeed, the sign of \(f(s)-s\) is the sign of \((s_*-s)\) for \(0<s<1\); furthermore \(f\) is strictly increasing since, after setting \(r=s/(1-s)\), the ratio update is \(r\mapsto(b/a)r(r+2)/(1+2r)\), which has positive derivative. Consequently \(f^n(s)\to s_*\) for every \(0<s<1\).

The uniformly convergent weighted series
\[
 R(s)=\exp\left[-\sum_{j=0}^{\infty}2^{-j-1}\log h(f^j(s))\right]
\]
defines a positive continuous function on \([0,1]\) satisfying \(R(f(s))=h(s)R(s)^2\). Thus
\[
 t_n=R(f^n(s))\left[\frac{t_0}{R(s)}\right]^{2^n}.
\]
As \(f^n(s)\to s_*\), the critical case \(t_0=R(s)\) converges to total mass \(R(s_*)=1/h(s_*)\), which gives the displayed positive fixed point \(E\). The inequalities on either side give zero and infinity respectively. Since \(h(0)=a/2\), \(h(1)=b/2\), the boundary values are \(R(0)=2/a\), \(R(1)=2/b\). This reconstructs, but does not newly claim, the previously known global separator.

**2. An exact discounted edge series.** Write \(s_j=f^j(s)\) and
\[
 g(u)=\log\frac{h(u)}{h(0)},\qquad
 \Delta(s)=\sum_{j=0}^{\infty}2^{-j-1}g(s_j).
\]
At the first endpoint direct Taylor expansion gives
\[
 f(u)=\lambda u\left(1+O(u)\right),\qquad
 g(u)=\lambda u+O(u^2),\qquad \lambda=2b/a>1.
\]
The function \(g\) is bounded on \([0,1]\). Fix sufficiently small \(\delta\in(0,s_*)\) and set \(N=N(s)\) to be the first integer for which \(s_N\ge\delta\). Since \(s_j\nearrow s_*\) from \(0<s<\delta\), this index is finite and \(s_N\in[\delta,f(\delta)]\).

**3. Subresonant edge \(1<\lambda<2\).** Choose \(\Lambda\) with \(\lambda<\Lambda<2\) and \(\delta\) small enough that \(s_{j+1}\le\Lambda s_j\) until the first exit. For \(j<N\), the normalized summands are bounded by \(C(\Lambda/2)^j\), because \(|g(s_j)|\le Cs_j\). For each fixed \(j\), \(s_j/s\to\lambda^j\) as \(s\downarrow0\). Also \(\delta\le s_N\le\Lambda^N s\) implies \(2^{-N}=O(s^p)\) for \(p=\log2/\log\Lambda>1\); the post-exit series is therefore \(o(s)\). Dominated convergence for the pre-exit sum yields
\[
 \lim_{s\downarrow0}\frac{\Delta(s)}s
 =\sum_{j\ge0}2^{-j-1}\lambda^{j+1}
 =\frac\lambda{2-\lambda}.
\]
This coefficient remains valid even when \(g\) changes sign away from the endpoint.

**4. Resonance \(\lambda=2\).** Here \(a=b\). Choose \(\delta\) sufficiently small that \(s_{j+1}\ge\eta s_j\) before exit for some \(1<\eta<2\). Then \(\sum_{j<N}s_j=O(\delta)\), uniformly as \(s\downarrow0\). Summing \(\log[f(s_j)/(2s_j)]=O(s_j)\) gives, uniformly for \(j\le N\),
\[
 s_j=2^j s\left(1+O(\delta)\right),\qquad
 N=\frac{\log(1/s)}{\log2}+O_\delta(1).
\]
Because \(g(u)=2u+O(u^2)\), each pre-exit term \(2^{-j-1}g(s_j)\) equals \(s(1+O(\delta))\). The post-exit tail is \(O(2^{-N})=O_\delta(s)\). Therefore
\[
 \Delta(s)=Ns\left(1+O(\delta)\right)+O_\delta(s).
\]
First let \(s\downarrow0\) and then \(\delta\downarrow0\): the normalized limit equals \(1/\log2\).

**5. Superresonant edge \(2<\lambda<4\).** In this case \(b>a\), and
\[
 h(u)-h(0)=\frac u2\bigl[2b-(a+b)u\bigr]>0\qquad(0<u\le1).
\]
Thus \(g(u)>0\) throughout the positive composition interval. Fix \(\eta\) with \(2<\eta<\lambda\), and take \(\delta\) so that \(s_{j+1}\ge\eta s_j\) before exit. Since \(\sum_{j<N}s_j=O(\delta)\), the expansion of \(f\) shows
\[
 s_N=\lambda^N s\exp\!\left(O\left(\sum_{j<N}s_j\right)\right)
      =\lambda^N s\exp(O(\delta)).
\]
Because \(s_N\in[\delta,f(\delta)]\), it follows that
\[
 2^{-N}\asymp s^\alpha,\qquad \alpha=\log2/\log\lambda.
\]
For the upper bound on \(\Delta\), use \(g(s_j)\le Cs_j\) before exit and \(s_j\le s_N\eta^{-(N-j)}\); the pre-exit sum is bounded by
\[
 C2^{-N}s_N\sum_{k\ge1}(2/\eta)^k=O(2^{-N}).
\]
The boundedness of \(g\) makes the entire post-exit tail \(O(2^{-N})\). For the lower bound, the single term with index \(N\) is at least \(2^{-N-1}\min_{u\in[\delta,f(\delta)]}g(u)>0\). Hence \(0<c s^\alpha\le\Delta(s)\le C s^\alpha\) for all sufficiently small \(s\), with constants depending on \(a,b\), proving the sharp exponent. Since \(\alpha<1\), the radial threshold cannot be Lipschitz at this endpoint.

**6. Opposite endpoint and consequences.** Interchanging the two species amounts to replacing \(s\) by \(1-s\) and swapping \(a,b\). This conjugates the formula for \(R\) and yields all three laws at the other endpoint. Under unequal coefficients, one of \(2b/a\) and \(2a/b\) exceeds two and the other lies below two. Under equality both equal two. Finally \(\Delta(s)\to0\) implies \(R(0)-R(s)=R(0)(1-e^{-\Delta(s)})\sim R(0)\Delta(s)\); the corresponding statement holds at the other endpoint. This completes the proof.

## Verification

The companion standard-library checker `check_boundary.py` verifies the mass/composition factorization using exact fractions, tests the exact radial functional identity at high precision, and compares the three edge regimes at successively smaller compositions. Run `python3 check_boundary.py` after extracting the package. The symbolic factorization can also be checked directly from the two displayed rational formulas. The checker is corroborating finite computation only: the uniform convergence, limiting constants, and all-parameter sharp power bounds are proved analytically above.

## Relationship to prior work

Shoyimardonov and Rozikov (arXiv:2409.13450, first posted 2024-09-20) introduced this exact quadratic operator. Their Theorem 9 gives a qualitative extinction/escape separating curve through the two axial fixed points and the interior saddle. Their invariant-manifold discussion gives a tangent at the interior saddle and an illustrative polynomial curve approximation, not the endpoint regularity of the boundary.

Two later published mathematical findings go further: *An exact global separatrix and water-filling convergence for a positive quadratic map* establishes the same critical-radius series and global convergence for every finite dimension and all positive coefficients; *A computable global extinction–escape separatrix for a homogeneous quadratic population map* establishes the series and sharp **interior balanced-composition curvature** in a higher-dimensional positive chamber. The exact radial series, global basin classification, and uniform convergence are explicitly credited as established prior results here. Neither statement provides the present **three-way pure-axis regularity theorem**, whose new content is the exact subresonant slope, the universal resonant logarithm, and the superresonant sharp fractional exponent. These require a multiscale exit-time argument rather than just continuity or an explicit evaluation formula.

The general local theory of invariant manifolds and nonlinear Perron–Frobenius maps supplies background, but generic stable-set existence or projective convergence does not by itself state the exact axis-specific coefficients or the logarithmic resonance for this map. Priority against unindexed equivalent edge analyses is not certified.

## Limitations

The sharp power-law branch proves positive finite liminf/limsup, not convergence of the normalized quotient; possible log-periodicity is not resolved. The theorem is confined to the two-dimensional positive coexistence chamber, with the radial coordinate fixed to \(x+y\). The shape of the global curve away from the endpoints and behavior on the parameter-boundary equalities are not newly classified. The proof is mathematical, but independent validation and journal-priority review have not been performed.

## References

1. S. K. Shoyimardonov and U. A. Rozikov, *Discrete-Time Dynamical Systems Generated by a Quadratic Operator*, arXiv:2409.13450v1, 2024-09-20. https://arxiv.org/html/2409.13450v1
2. S. K. Shoyimardonov and U. A. Rozikov, *Discrete-Time Dynamical Systems Generated by a Quadratic Operator*, *Russian Journal of Nonlinear Dynamics* 21 (2025), 399–418, DOI:10.20537/nd250803. https://nd.ics.org.ru/nd250803/
3. *An exact global separatrix and water-filling convergence for a positive quadratic map*, published mathematical note (2026). https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-an-exact-global-separatrix-and-water-filling-convergence-for-a-p--9175d180eec2/RESULT.md
4. *A computable global extinction–escape separatrix for a homogeneous quadratic population map*, published mathematical note (2026). https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-computable-global-extinction-escape-separatrix-for-a-homogeneo--00331e65c7d9/RESULT.md
