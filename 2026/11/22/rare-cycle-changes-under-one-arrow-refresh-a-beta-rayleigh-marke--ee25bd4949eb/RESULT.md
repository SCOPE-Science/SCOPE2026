# Rare cycle changes under one-arrow refresh: a beta–Rayleigh marked law

## Finding
Let \(F:[n]\to[n]\) be a uniformly random mapping, with all \(n\) images independent and uniform. Independently choose a uniform vertex \(v\), replace just \(F(v)\) by a fresh uniform image, and denote the resulting mapping by \(F'\). Let \(C(F)\) count directed cycles (one per weak component) and \(\Delta=C(F')-C(F)\).

Remove the arrow leaving \(v\), leaving its other \(n-1\) arrows fixed. Let \(B\) be the set of vertices whose resulting trajectory reaches the sink \(v\), and write \(K=|B|\). When \(|\Delta|=1\), let \(L\) be the length of the unique directed cycle born or destroyed by the update. The simultaneous finite-size law, for \(1\le k<n\), \(1\le\ell\le k\), and \(\sigma\in\{-1,+1\}\), is

\[\boxed{\Pr(\Delta=\sigma,K=k,L=\ell)=b_{n,k}\frac{k(n-k)}{n^2}\,a_{k,\ell-1}}\]
where
\[b_{n,k}=\frac{\binom{n-1}{k-1} k^{k-2}(n-k)^{n-k}}{n^{n-1}},\qquad a_{k,h}=\frac{(h+1)(k-1)_{h}}{k^{h+1}}.\]
Here \((m)_h=m(m-1)\cdots(m-h+1)\) is the falling factorial, with \((m)_0=1\); the isolated case \(k=1\) uses \(k^{k-2}=1\). The remaining mass is \(\Pr(K=n)=1/n\), for which \(\Delta=0\).

Let \(S\) be a fair sign, \(U\sim\operatorname{Beta}(1/2,3/2)\), and \(R\sim\operatorname{Rayleigh}(1)\), mutually independent. Then
\[\boxed{\Pr(|\Delta|=1)\sim\sqrt{\frac{\pi}{2n}},\qquad (\Delta,K/n,L/\sqrt n)\mid\{|\Delta|=1\}\ \xrightarrow{d}\ (S,U,\sqrt U\,R).}\]
In particular \(\sqrt n\Pr(\Delta=1)\to\sqrt{\pi/8}\). The conditional law of the sign is exactly symmetric and independent of \((K,L)\) at every finite \(n\).

## Assumptions and scope
Every mapping \([n]\to[n]\) has equal probability \(n^{-n}\). Images are independent and may be self-images. The resampled image is independent and may equal its former value; the distinguished vertex is independently uniform. The update concerns precisely one coordinate. We assert the law for every integer \(n\ge2\), with weak convergence as \(n\to\infty\). In the limit, the beta density is \((2/\pi)u^{-1/2}(1-u)^{1/2}\) on \((0,1)\), and the Rayleigh density is \(r\exp(-r^2/2)\) for \(r>0\).

## Proof
**1. Surgery.** By exchangeability fix \(v=1\). Freeze all other outgoing arrows, obtaining a partial mapping \(g\) with one sink. Exactly one rooted in-tree \(B\) drains into \(v\); all other vertices belong to closed functional components. An arrow from \(v\) into \(B\) closes exactly one cycle, while an arrow from \(v\) outside \(B\) joins an existing cyclic component and creates no new cycle. If \(a\) and \(b\) are respectively old and fresh independent uniform targets, then pathwise
\[\Delta=\mathbf 1_{\{b\in B\}}-\mathbf 1_{\{a\in B\}}.\]
It follows that \(\Pr(\Delta=+1\mid g)=\Pr(\Delta=-1\mid g)=K(n-K)/n^2\). On a nonzero jump the target in \(B\) is uniform in \(B\), regardless of its sign. This proves the exact sign independence and reduces the mark \(L\) to one plus the target's distance to \(v\).

**2. Sink-basin size.** A fixed choice of \(k-1\) other basin vertices supports \(k^{k-2}\) directed rooted Cayley trees toward \(v\) (one tree when \(k=1\)). The \(n-k\) vertices outside must map exclusively outside, giving \((n-k)^{n-k}\) functions, with the usual empty-function convention. Since the \(n-1\) frozen arrows have \(n^{n-1}\) equiprobable configurations, the formula for \(b_{n,k}\) follows. At \(k=n\) the entire partial mapping is one rooted tree, yielding \(b_{n,n}=1/n\).

**3. Exact tree-distance mark.** Conditional on \(K=k\), the basin is a uniform labelled rooted Cayley tree with specified root. For \(h=0\), the uniform target equals the root with probability \(1/k\). For \(1\le h<k\), fix a nonroot target and order its \(h-1\) intermediate path vertices: \((k-2)_{h-1}\) choices. Each of the other vertices can be assigned in the rooted forest feeding into the \(h+1\) ordered path vertices in precisely \((h+1)k^{k-h-2}\) ways (the classical rooted-forest enumeration). Dividing by the \(k^{k-2}\) total rooted trees and then averaging over the \(k-1\) nonroot targets gives
\[a_{k,h}=\frac{(h+1)(k-1)_h}{k^{h+1}},\quad 0\le h<k.\]
Together with the surgery factor this proves the marked finite law.

**4. Rare-jump intensity and beta basin.** Stirling's formula, uniformly when \(k/n\) stays in compact subsets of \((0,1)\), gives
\[n^{3/2}b_{n,k}\longrightarrow\frac{u^{-3/2}(1-u)^{-1/2}}{\sqrt{2\pi}},\qquad u=k/n.\]
After multiplying by \(k(n-k)/n^2\), the Riemann-sum intensity for one jump sign has normalized continuum weight \(u^{-1/2}(1-u)^{1/2}/\sqrt{2\pi}\). Its integral is
\[\frac{1}{\sqrt{2\pi}}B(1/2,3/2)=\sqrt{\pi/8}.\]
Standard factorial/Stirling bounds yield a uniform summand bound proportional to \(n^{-3/2}u^{-1/2}(1-u)^{1/2}\). The mass with \(u<\varepsilon\), after multiplication by \(\sqrt n\), is \(O(\sqrt\varepsilon)\), and that with \(u>1-\varepsilon\) is \(O(\varepsilon^{3/2})\). Thus the endpoint masses vanish, establishing both the probability asymptotic and \(K/n\Rightarrow\operatorname{Beta}(1/2,3/2)\) conditional on a jump.

**5. Joint Rayleigh cycle mark.** For large \(k\), put \(h=\lfloor r\sqrt k\rfloor\) in the exact depth law. On compact positive ranges of \(r\),
\[\sqrt k\,a_{k,\lfloor r\sqrt k\rfloor}\longrightarrow r e^{-r^2/2}.\]
The product expression gives the accompanying sub-Gaussian tail bound for \(h/\sqrt k\). Hence the uniform-target depth divided by \(\sqrt k\) converges to a unit Rayleigh variable, uniformly for \(k\) tending to infinity. Since the conditional basin fraction stays away from both endpoints in probability, conditioning on \(K\) yields asymptotic independence of \(K/n\) and \(L/\sqrt K\), and therefore \(L/\sqrt n\Rightarrow\sqrt U\,R\). The exact finite sign symmetry gives the stated three-coordinate joint convergence. All steps concern the entire infinite sequence, not merely tested values.

## Verification
`verify.py` reproduces the exact finite joint law by exhaustive enumeration of all frozen maps and old/new targets for \(n=2,3,4,5\). It independently checks the root-distance law over all Prüfer-coded trees through six vertices, and evaluates the rate and conditional basin mean at three larger sample sizes using stable log-gamma formulas. Run with `python3 verify.py`; only the Python standard library is required. These finite checks corroborate, but do not replace, the analytical limit proof. For example the exact one-sign probabilities for \(n=2,3,4,5\) are respectively \(1/8\), \(4/27\), \(39/256\), and \(472/3125\).

## Relationship to prior work
The static random-mapping distribution and its component structures are classical; the work of Flajolet and Odlyzko and Hansen and Jaworski motivates using Cayley-rooted trees and predecessor sizes. The present claim instead concerns the *coupled before/after cycle count* under refreshing a single arrow, including the probability of a nonzero cycle change and its joint sign, basin-fraction, and created/destroyed-cycle-length marks. Static precursor distributions alone do not state this joint refresh law; no priority claim is made for the underlying Cayley formula, beta distributions, or Rayleigh depth limits. Relevant historical predecessor analyses may entail portions of the finite tree-count calculation, so the precise coupled theorem should be compared against their full statements before any stronger priority claim.

## Limitations
The theorem is for uniform independent images and a single independently resampled outgoing arrow; it does not cover preferential target probabilities, simultaneous multiple-arrow resampling or time-process convergence. Broader existing random-mapping perturbation results might imply this law, even when their titles differ; historical priority is therefore not certified. Selected older predecessor papers were available only in abstract form, and the available material was not used to infer full-text noncoverage. The asymptotic result is mathematically derived; finite checks do not certify infinity.

## References
- Hansen, J. C., and Jaworski, J., *A new random mapping model*, arXiv:math/0603529 (first public arXiv version 2006-03-22), https://arxiv.org/abs/math/0603529 .
- Flajolet, P., and Odlyzko, A. M., *Random Mapping Statistics*, in *Advances in Cryptology—EUROCRYPT '89*, 1990, https://www-users.cse.umn.edu/~odlyzko/doc/arch/random.mappings.pdf .
- Baron, G., Drmota, M., and Mutafchiev, L., *Predecessors in Random Mappings*, *Combinatorics, Probability and Computing* 5 (1996), 317–335, https://doi.org/10.1017/S0963548300002091 .
- Hansen, J. C., and Jaworski, J., *Predecessors and successors in random mappings with exchangeable in-degrees*, *Journal of Applied Probability* 50 (2013), 721–740, https://doi.org/10.1239/jap/1378401232 .
- Hansen, J. C., and Jaworski, J., *Structural Transition in Random Mappings*, *Electronic Journal of Combinatorics* 21 (2014), P1.18, https://doi.org/10.37236/3572 .
