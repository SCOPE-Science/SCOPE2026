# A sharp hub–leaf polarization reversal under viral diffusion on stars

## Finding

Consider an undirected weighted star with one hub and \(m\ge1\) leaves, each edge of weight \(w>0\). Start with zero innate opinions. A single initial marketing seed shifts its own innate opinion to \(\varepsilon\in(0,1]\), and every subsequently reached individual makes that same one-time shift. Information spreads by the independent-cascade rule with transmission probability \(p\in[0,1]\) on each directed edge. After the cascade, expressed opinions relax to the Friedkin–Johnsen equilibrium \(z=(I+L)^{-1}s\). Write \(\mathcal P(z)=\sum_v(z_v-\bar z)^2\), and let \(P_H\) and \(P_L\) denote the expected polarization for a hub seed and a leaf seed, respectively.

Define
\[
 A=(1+w)^{-2},\qquad B=\frac{m}{m+1}\bigl(1+(m+1)w\bigr)^{-2}.
\]
Then the exact hub–leaf difference is
\[
 \boxed{P_H-P_L=\frac{\varepsilon^2(m-1)(1-p)^2}{m^2}
 \left[mA\bigl((m-2)p-1\bigr)+B\bigl(m+1-(m-2)p\bigr)\right].}
\]
For \(m=1\), both seed choices are identical. For \(m=2\), a leaf seed has strictly greater expected polarization for every \(0\le p<1\). For every \(m\ge3\), there is a unique threshold
\[
 \boxed{p_*(m,w)=\frac{mA-(m+1)B}{(m-2)(mA-B)}\in(0,1)}
\]
at which the seed rankings reverse: \(P_L>P_H\) for \(0\le p<p_*\), equality at \(p=p_*\), and \(P_H>P_L\) for \(p_*<p<1\). At \(p=1\), both polarizations are zero. For fixed \(w>0\), \(p_*(m,w)\sim1/(m-2)\) as \(m\to\infty\).

By contrast, the hub seed always weakly maximizes expected activation reach among the two single-seed types. Their exact difference in expected numbers of shifted innate opinions is \((m-1)p(1-p)\), strictly positive if \(m>1\) and \(0<p<1\). Thus maximizing reach and maximizing polarization select opposite seed locations below the sharp threshold.

## Assumptions and scope

The graph is the fixed star \(K_{1,m}\) with a common strictly positive undirected social-influence weight \(w\). Each directed infection attempt is independent and succeeds with probability \(p\); the independent cascade has no recovery or repeated attempts. This is the all-spread subcase \(\delta=1\) of the spread–acknowledge mechanism in Tu and Neumann (2022). Every initial seed is counted as having acknowledged the content and receives the specified innate opinion shift. All initial innate opinions are zero, and every activated node receives the same shift \(\varepsilon\). The intervention does not clamp any expressed opinion or change the social graph. The polarization is the unnormalized squared-deviation sum, not the network edge-disagreement statistic or a normalized variance. The expectation is taken over campaign diffusion only; the post-cascade Friedkin–Johnsen equilibrium is deterministic conditional on the cascade.

## Proof

Put \(h=s_H/\varepsilon\in\{0,1\}\), and let \(k\in\{0,\ldots,m\}\) count shifted leaves. The leaf-average component of \(s/\varepsilon\) is \(k/m\). The star Laplacian has eigenvalue \(w\) on the \((m-1)\)-dimensional leaf-difference space and eigenvalue \((m+1)w\) on the centered hub-versus-leaves direction. The latter has squared projection length \(m(h-k/m)^2/(m+1)\). After applying \((I+L)^{-1}\) and removing the constant mode, the orthogonal eigenspaces therefore yield the **exact conditional polarization identity**
\[
 \frac{\mathcal P(z)}{\varepsilon^2}
  = A\left(k-\frac{k^2}{m}\right)+B\left(h-\frac{k}{m}\right)^2.
 \tag{1}
\]
For \(m=1\), the first summand is identically zero and the identity still holds.

A hub seed has \(h=1\) and \(K\sim\operatorname{Bin}(m,p)\). Using \(\mathbb E K=mp\), \(\operatorname{Var}K=mp(1-p)\) in (1) gives
\[
 \frac{P_H}{\varepsilon^2}
 = A(m-1)p(1-p)
 +B\left((1-p)^2+\frac{p(1-p)}m\right).\tag{2}
\]
With a leaf seed, the hub fails to activate with probability \(1-p\), giving \((h,k)=(0,1)\). Otherwise the hub activates and independently attempts all remaining \(m-1\) leaves, so \((h,k)=(1,1+J)\) with \(J\sim\operatorname{Bin}(m-1,p)\). Consequently
\[
 \begin{aligned}
 \frac{P_L}{\varepsilon^2}={}&(1-p)\left[A\frac{m-1}{m}+\frac{B}{m^2}\right]\\
 &+p\left[A\frac{(m-1)(1-p)(1+(m-2)p)}m\\
 &\qquad+B\frac{(m-1)^2(1-p)^2+(m-1)p(1-p)}{m^2}\right].\tag{3}
 \end{aligned}
\]
The polynomial reduction of (2) minus (3) gives the boxed formula. Its bracket is
\[
 (m-2)(mA-B)p-\bigl(mA-(m+1)B\bigr).\tag{4}
\]
For \(m=2\) this is \(3B-2A<0\), since \(3B=2(1+3w)^{-2}<2(1+w)^{-2}=2A\). For \(m\ge3\), note that \(mA-(m+1)B=m[(1+w)^{-2}-(1+(m+1)w)^{-2}]>0\), and \(mA-B>0\). Furthermore,
\[
 (m-2)(mA-B)-\bigl(mA-(m+1)B\bigr)=m(m-3)A+3B>0.
\]
Thus (4) has exactly one zero in \((0,1)\), at \(p_*\), and its sign proves all asserted rankings for \(p<1\). The prefactor \((1-p)^2\) makes both polarizations equal at \(p=1\). The case \(m=1\) is the reflection symmetry of a single edge. For fixed \(w>0\), \(A\) is constant and \(B=O(m^{-2})\), proving \(p_*\sim1/(m-2)\).

Finally, the hub seed reaches \(1+\operatorname{Bin}(m,p)\) individuals; a leaf seed reaches one individual, plus the hub with probability \(p\), plus an expected \((m-1)p^2\) further leaves. Subtraction gives \((m-1)p(1-p)\). This proves the reach comparison.

## Verification

Run `python3 verify.py` with Python 3 standard library. It uses exact rational Gaussian elimination on \(I+L\) for every reachable binary innate-opinion pattern and separately enumerates the two cascade distributions. It then checks equations (2), (3), the difference formula, the sign law, and the reach identity for \(m=1,\ldots,6\), \(w\in\{1/3,1,2\}\), and \(p\in\{0,1/4,1/2,3/4,1\}\). The result is **180 exact-rational paired formula comparisons**, independent of any floating-point linear solve. The verifier also checks \(p_*(4,1)=5/11\). These finite checks are supplementary: the proof of the theorem for all \(m,w,p\) is algebraic and does not depend on enumeration.

For illustration, with \(m=4\), \(w=1\), and \(\varepsilon=1\), at \(p=1/5\) the exact expected polarizations are \(P_H=152/1125\) and \(P_L=1096/5625\), so a leaf seed gives greater polarization. At \(p=4/5\) they are \(P_H=137/1125\) and \(P_L=1313/11250\), so the hub seed gives greater polarization.

## Relationship to prior work

Tu and Neumann (2022, arXiv:2202.03573) combine independent-cascade spread with Friedkin–Johnsen equilibrium, define the same polarization index, and develop general unbiased index estimators and seed-selection heuristics. Their accessible full-text Sections 3–6 and relevant results do not state the exact star hub–leaf formula or the sharp probability-dependent seed-order reversal. General expressions for quadratic indices do not by themselves provide the explicit optimizer or boundary proved here. Hunter and Zaman (arXiv:1806.11253) study optimal placement of *stubborn agents* with a distinct fixed-opinion mechanism, not random viral activation followed by the above equilibrium. Bhalla, Lechowicz and Musco (arXiv:2111.14020) study changing graph edges with opinion feedback, not single-seed independent-cascade diffusion on a fixed star. These comparisons do not establish exhaustive novelty; related unindexed derivations may exist.

## Limitations

The result assumes identical nonzero changes to initially zero innate opinions, homogeneous edge influence and transmission probabilities, one initial seed, and \(\delta=1\). It makes no claim for heterogeneous initial opinions, weighted or correlated cascade outcomes, multiple seeds, nonlinear opinion updates, or optimization over arbitrary graphs. The baseline polarization is zero, so the objective quantifies the polarization generated by the campaign, not its signed change from a polarized initial state. The formula measures equilibrium polarization and not transient opinion disagreement. Priority relative to inaccessible or unindexed work is a residual uncertainty.

## References

- Sijing Tu and Stefan Neumann, *A Viral Marketing-Based Model For Opinion Dynamics in Online Social Networks*, arXiv:2202.03573, initially public 2022-02-08. https://arxiv.org/abs/2202.03573 ; accessible full-text version https://arxiv.org/html/2202.03573 .
- D. Scott Hunter and Tauhid Zaman, *Optimizing Opinions with Stubborn Agents*, arXiv:1806.11253, 2018. https://arxiv.org/abs/1806.11253 .
- Nikita Bhalla, Adam Lechowicz, and Cameron Musco, *Local Edge Dynamics and Opinion Polarization*, arXiv:2111.14020, 2021. https://arxiv.org/abs/2111.14020 .
