# Distinct boundary local dimensions for nonresonant random affine interval homeomorphisms

## Finding
For the symmetric Alsedà–Misiurewicz random interval homeomorphisms, stationary mass close to the two endpoints has *exact and generally different* local dimensions \(\kappa_0\) and \(\kappa_1\). The dimensions solve separate explicit characteristic equations. More precisely, the limits in the claim below exist, and each dimension is also the sharp strict threshold for finiteness of the corresponding negative moment. This determines intrinsic boundary statistics not fixed by the measure's global Hausdorff dimension.

## Assumptions and scope
Let \(0<a<1<b\), \(0<p<1\), and \(q=1-p\). Set
\[x_-=(b-1)/(b-a),\qquad x_+=(1-a)/(b-a).\]
Define increasing homeomorphisms of \([0,1]\) by
\[f_-(x)=\begin{cases}ax&0\le x\le x_-,\\1-b(1-x)&x_-<x\le1,\end{cases}\qquad
f_+(x)=\begin{cases}bx&0\le x\le x_+,\\1-a(1-x)&x_+<x\le1.\end{cases}\]
Choose \(f_-\) with probability \(p\) and \(f_+\) with probability \(q\), independently at each time. Assume positive Lyapunov drifts at both endpoints:
\[\Lambda_0=p\log a+q\log b>0,\qquad\Lambda_1=p\log b+q\log a>0.\]
Assume also \(\log a/\log b\notin\mathbb Q\). By the existence, uniqueness, nonatomicity and nonresonant-support results in the cited literature, there is a unique probability \(\mu\) with \(\mu(\{0,1\})=0\) satisfying \(\mu=p(f_-)_*\mu+q(f_+)_*\mu\); its support is all of \([0,1]\). Put
\[\Phi_0(s)=pa^{-s}+qb^{-s},\qquad\Phi_1(s)=pb^{-s}+qa^{-s}.\]
Because \(\Phi_j(0)=1\), \(\Phi'_j(0)=-\Lambda_j<0\), and \(\Phi_j(s)\to\infty\) as \(s\to\infty\), strict convexity gives exactly one positive root \(\kappa_j\) of \(\Phi_j(\kappa_j)=1\). Strict convexity also gives \(\Phi_j(s)<1\) for \(0<s<\kappa_j\), and \(\Phi_j(s)>1\) for \(s>\kappa_j\).

The result is
\[\lim_{r\downarrow0}\frac{\log\mu([0,r])}{\log r}=\kappa_0,\qquad
\lim_{r\downarrow0}\frac{\log\mu([1-r,1])}{\log r}=\kappa_1.\]
For every \(t>0\), the endpoint negative moment \(\int x^{-t}\,d\mu(x)\) is finite for \(t<\kappa_0\) and infinite for \(t>\kappa_0\); analogously \(\int(1-x)^{-t}\,d\mu(x)\) changes at \(\kappa_1\). The borderline moment \(t=\kappa_j\) is not addressed. If \(p>q\) then \(\kappa_0<\kappa_1\); if \(p<q\) then \(\kappa_0>\kappa_1\); they coincide iff \(p=q\).

For the explicit nonresonant example \(a=1/3\), \(b=8\), \(p=11/20\), \(q=9/20\), the endpoint drifts are positive and the two roots are approximately \(0.2817139291\) and \(0.5524212948\). Nonresonance follows because distinct prime-power integers cannot satisfy \(3^m=8^n\) for positive integers \(m,n\).

## Proof
**1. An exact local renewal relation.** Set \(U(r)=\mu([0,r])\), which is continuous by nonatomicity, with \(U(0)=0\), and strictly positive for \(r>0\) by full support. Set \(\varepsilon=\min\{a x_-,b x_+\}>0\). For all \(0<r\le\varepsilon\), the inverse images of \([0,r]\) lie in the first linear branches of both maps, so stationarity gives the *exact* identity
\[U(r)=pU(r/a)+qU(r/b).\tag{1}\]
At the other endpoint \(V(r)=\mu([1-r,1])\) is likewise continuous, zero at \(0\), and positive for \(r>0\). By reflection symmetry the corresponding identity is
\[V(r)=pV(r/b)+qV(r/a)\tag{2}\]
for all \(0<r\le\varepsilon\). These are local identities only; they are not extended into other branches.

**2. A sharp comparison principle.** Let \(F\colon[0,1]\to[0,1]\) be continuous, \(F(0)=0\), \(F(r)>0\) for \(r>0\), and suppose \(F(r)=\sum_i w_i F(r/c_i)\) for all \(0<r\le\varepsilon\), with positive weights summing to one, positive scaling factors \(c_i\), and \(R=\varepsilon/\min c_i\le1\). (If necessary replace \(\varepsilon\) by a smaller positive number to ensure \(R\le1\).) Write \(\Phi(s)=\sum_i w_i c_i^{-s}\). For any \(s>0\) with \(\Phi(s)<1\), choose \(C>0\) such that \(F(r)\le Cr^s\) on \([\varepsilon,R]\). Set \(W(r)=F(r)-Cr^s\). Since \(W(0)=0\) and \(W\le0\) on \([\varepsilon,R]\), if \(W\) attained a positive maximum on \([0,R]\), it would be at some \(r\in(0,\varepsilon)\). But
\[W(r)=\sum_i w_i W(r/c_i)+C(\Phi(s)-1)r^s<\max_{[0,R]}W,\]
a contradiction. Thus \(F(r)\le Cr^s\) for all small \(r\). For \(s>0\) with \(\Phi(s)>1\), choose \(c>0\) such that \(F(r)\ge cr^s\) on \([\varepsilon,R]\) (possible since \(F(r)>0\) there). Then \(W=F-cr^s\) satisfies \(W(0)=0\), \(W\ge0\) on the outer strip, and
\[W(r)=\sum_iw_iW(r/c_i)+c(\Phi(s)-1)r^s.\]
An interior negative minimum would be strictly larger than itself, a contradiction. Consequently \(F(r)\ge cr^s\) for all small \(r\).

Take the smaller \(\varepsilon\) if necessary so that \(\varepsilon/a\le1\). Applying this comparison to (1) and (2) gives, for every \(0<s<\kappa_0<t\), positive constants \(C_s,c_t\) such that
\[c_t r^t\le U(r)\le C_s r^s\quad(r\downarrow0),\]
and similarly with \(V,\kappa_1\). Divide logarithms by \(\log r<0\), let \(r\downarrow0\), then let \(s\uparrow\kappa_0\), \(t\downarrow\kappa_0\). This yields the first limit; the second is identical.

**3. Negative moments.** For any \(t>0\), Tonelli's theorem gives the exact identity (possibly both sides infinite)
\[\int_{(0,1]}x^{-t}\,d\mu(x)=1+t\int_0^1 r^{-t-1}U(r)\,dr.\]
When \(t<\kappa_0\), choose \(s\in(t,\kappa_0)\); the proved upper bound makes the integral finite. When \(t>\kappa_0\), choose \(s\in(\kappa_0,t)\); the proved lower bound makes it infinite. Replace \(U\) by \(V\) for the other endpoint. No assertion at equality is needed.

**4. Strict asymmetry.** For \(s>0\),
\[\Phi_0(s)-\Phi_1(s)=(p-q)(a^{-s}-b^{-s}).\]
Since \(a^{-s}>b^{-s}\) and each \(\Phi_j\) lies strictly above one beyond its positive root, the root ordering is exactly the claimed ordering (with equality when \(p=q\)). This completes the proof.

## Verification
The proof uses exact finite-branch stationarity, a compact-interval maximum/minimum argument, and a Tonelli identity. It proves continuum statements without relying on numerical experiments. A standalone checker in `verify.py` verifies the branch endpoint geometry, positivity of endpoint drifts, strict convexity sign brackets, approximate characteristic roots and their order for illustrative inputs. Run `python3 verify.py`; no nonstandard libraries are required. Numerical checks are not an infinite proof.

## Relationship to prior work
Barański and Śpiewak (arXiv:2208.06394, first public 2022-08-12) establish singularity and global Hausdorff-dimension bounds for an open nonresonant AM parameter regime; they do not state the local endpoint root laws. Their earlier paper (arXiv:1905.11048, 2019-05-27) proves basic stationary-measure results, resonance-dependent support and dimension properties, and a nonquantitative *some-power* endpoint bound (Theorem 3.6, attributed to earlier ergodic work). The present two-root formula and sharp strict negative-moment thresholds do not follow from that existential bound. Bradík and Roth (arXiv:2102.02023, 2021-02-03) study generic singular full-support stationary measures but do not compute these endpoint exponents. These are comparison statements about the inspected work, not claims of absolute publication priority. The characteristic-equation and power-barrier technique is elementary and related general random-renewal principles exist; equivalent formulas elsewhere are a residual novelty risk.

## Limitations
The theorem requires piecewise *exactly affine* endpoint branches, positive endpoint drifts and nonresonant slopes, and concerns the unique no-endpoint-atoms stationary probability. It does not calculate global Hausdorff dimension, an exact asymptotic prefactor \(\mu([0,r])/r^{\kappa_0}\), or behavior at the critical negative moments. Nonresonance is imposed to use the established full-support theorem; the comparison argument may be useful beyond it. Only numerical examples, not the continuum proof, rely on the checker. Independent mathematical audit has not been performed.

## References
1. K. Barański and A. Śpiewak, *On the dimension of stationary measures for random piecewise affine interval homeomorphisms*, arXiv:2208.06394 (first version 2022-08-12), sections 1–2 and 4. https://arxiv.org/abs/2208.06394
2. K. Barański and A. Śpiewak, *Singular stationary measures for random piecewise affine interval homeomorphisms*, arXiv:1905.11048 (2019-05-27), Theorems 2.4, 2.10, 3.6 and Proposition 2.6. https://arxiv.org/abs/1905.11048
3. J. Bradík and S. Roth, *Typical behaviour of random interval homeomorphisms*, arXiv:2102.02023 (2021-02-03), introduction and main genericity results. https://arxiv.org/abs/2102.02023
