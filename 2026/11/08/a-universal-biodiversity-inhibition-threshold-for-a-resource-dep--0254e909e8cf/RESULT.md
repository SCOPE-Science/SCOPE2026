# A universal biodiversity-inhibition threshold for a resource-dependent consumer guild

## Finding

Consider the finite ecological occupancy process defined below, with positive rates \(c,e,u,v,k\), and \(m\ge 0\) potential specialist consumers. Let \(S_m\) denote the **stationary expected number of present species**, counting the basal resource as one species and each present consumer as one species. Then the sign of every incremental guild-size change is exactly determined by the resource's unaided switching rate \(c+e\):

\[
\operatorname{sign}(S_{m+1}-S_m)=\operatorname{sign}(c+e-k),\qquad m\ge0.
\]

In particular, if \(k<c+e\), richness strictly increases with guild size; if \(k>c+e\), richness strictly decreases; and if \(k=c+e\), **all** guild sizes have identical expected richness \(c/(c+e)\). The threshold does not depend on consumer colonization or individual background-extinction rates \(u,v\).

The limiting richness and a sharp approach law are

\[
\lim_{m\to\infty}S_m=\frac ck, \qquad
S_m-\frac ck\sim\frac{c(k-c-e)}{k}\sqrt{\frac{\pi}{2mku}}
\quad (k\ne c+e).
\]

For every \(m\), the exact stationary resource occupancy and consumer count are obtained from one scalar integral:

\[
L_m=\int_0^\infty e^{-et}s(t)^m\,dt,\qquad
s(t)=\mathbb E\!\left[\exp\left(-k\int_0^t X(r)\,dr\right)\right],
\]

where \(X\) is a single two-state chain starting at zero and switching \(0\to1\) at rate \(u\), \(1\to0\) at rate \(v\). Writing \(p_m\) for stationary resource occupancy and \(q_m\) for stationary number of consumers,

\[
p_m=\frac{cL_m}{1+cL_m},\qquad
q_m=\frac{c(1-eL_m)}{k(1+cL_m)},\qquad
S_m=p_m+q_m=\frac ck+\frac{c(k-c-e)L_m}{k(1+cL_m)}.
\]

The inequalities are strict for each increment away from the equality threshold, including the first consumer added to the consumer-free resource.

## Assumptions and scope

The local food web has exactly one basal resource and \(m\) potential specialist consumer species, each requiring the resource for local persistence. A state is either \(\emptyset\) (resource absent, hence every consumer absent) or \((1,j)\), indicating an occupied resource with \(j\in\{0,\dots,m\}\) present consumers. All rates are in common units of inverse time and \(c,e,u,v,k>0\).

The continuous-time Markov generator has the nonzero transitions

\[
\begin{aligned}
\emptyset&\longrightarrow(1,0)&&\text{at rate }c,\\
(1,j)&\longrightarrow\emptyset&&\text{at rate }e+kj,\\
(1,j)&\longrightarrow(1,j+1)&&\text{at rate }(m-j)u\quad(j<m),\\
(1,j)&\longrightarrow(1,j-1)&&\text{at rate }jv\quad(j>0).
\end{aligned}
\]

Each consumer-induced extirpation of the resource removes that resource and every dependent consumer at once. On resource recolonization, consumers start absent; while it is present, they immigrate and disappear independently at the stated rates. There are no other species, alternative resources, state-dependent immigration rates, density-dependent consumer interactions, or overlapping resource requirements. For every finite \(m\), the chain is irreducible and has one stationary distribution. These are mathematical occupancy probabilities rather than abundances or biomass.

## Proof

**Step 1: an exact resource flux identity.** Let \(p_m=\Pr\{\text{resource present}\}\) and \(q_m=\mathbb E[J]\) in stationarity. Apply stationarity of the generator to the indicator of resource presence. Gains occur at rate \(c(1-p_m)\), losses at rate \(e p_m+kq_m\). Thus

\[
(c+e)p_m+kq_m=c.\tag{1}
\]

Consequently \(S_m=p_m+q_m=c/(c+e)+(1-k/(c+e))q_m\). This already locates the only possible sign threshold; to establish the sign of successive changes requires proving \(q_m\) is strictly increasing with \(m\).

**Step 2: regenerative representation.** Starting from an absent resource, the process waits an independent exponential time of mean \(1/c\) before resource recolonization. Its subsequent occupied episode starts with no consumers. Ignore the extinction events temporarily and construct \(m\) independent two-state consumer chains \(X_i\), each initially zero and with rates \(u,v\). Conditioned on their trajectories, the probability the resource survives through time \(t\) is

\[
\exp\!\left(-et-k\sum_{i=1}^m\int_0^tX_i(r)\,dr\right).
\]

Independence yields the unconditional survival function \(e^{-et}s(t)^m\) and occupied-episode mean \(L_m\) stated above. The renewal reward theorem gives

\[
p_m=\frac{L_m}{1/c+L_m}=\frac{cL_m}{1+cL_m}.
\]

Substitution into (1) proves the exact expressions for \(q_m\) and \(S_m\). For \(m=0\), interpret \(s^0=1\), giving \(L_0=1/e\), \(q_0=0\), and \(S_0=c/(c+e)\).

**Step 3: strict monotonicity.** For every \(t>0\), positive \(u\) and \(k\) imply a positive probability that the single consumer has occupied a nonzero interval before \(t\). Therefore \(0<s(t)<1\). It follows that

\[
0<L_{m+1}<L_m\qquad(m\ge0).
\]

The function \(L\mapsto c(1-eL)/(k(1+cL))\) has derivative \(-c(c+e)/(k(1+cL)^2)<0\), hence \(q_{m+1}>q_m\). Equation (1) now establishes all three phase cases for \(S_m\), including equality at \(k=c+e\).

**Step 4: limit and sharp asymptotics.** For fixed \(t>0\), \(s(t)^m\to0\). Since \(e^{-et}s(t)^m\le e^{-et}\) and \(e>0\), dominated convergence gives \(L_m\to0\), and the exact expression for \(S_m\) yields \(S_m\to c/k\).

The two-state Feynman–Kac equation gives \(s(0)=1\), \(s'(0)=0\), and \(s''(0)=-uk\); therefore

\[
\log s(t)=-\frac{uk}{2}t^2+O(t^3)\quad(t\downarrow0).
\]

Fix a sufficiently small \(\varepsilon>0\). On \([0,\varepsilon]\), use \(t=z/\sqrt m\) and the quadratic expansion, bounded above by \(\exp(-a z^2)\) for some \(a>0\), to apply dominated convergence to the rescaled integral. On \([\varepsilon,\infty)\), monotonicity of \(s\) and the factor \(e^{-et}\) bound the contribution by \(s(\varepsilon)^m e^{-e\varepsilon}/e\), which is exponentially small. Thus

\[
L_m\sim \sqrt{\frac{\pi}{2muk}}.
\]

Expanding \(S_m-c/k=c(k-c-e)L_m/[k(1+cL_m)]\) now gives the stated sharp asymptotic. At \(k=c+e\), the difference is exactly zero for every \(m\), so an asymptotic equivalence to a zero expression is not asserted.

## Verification

The self-contained file `verify.py` uses exact rational Gaussian elimination independently on (a) the full \((m+2)\)-state stationary generator and (b) the \((m+1)\)-state killed consumer-count resolvent for the resource-occupied period. It checks both occupancy means, the exact balance identity, the exact richness expression, and strict consecutive-guild monotonicity. The output obtained with `python3 verify.py` was:

```text
PASS: 66 exact stationary/renewal comparisons; 60 strict monotonicity comparisons
large-guild L_m*sqrt(m)/sqrt(pi/(2*k*u)): [(100, 0.99480264), (400, 0.99872427), (1600, 0.99968423)]
```

The large-guild figures are corroboration only; the limit and rate are proved analytically in Step 4. The code tests a finite family of rational choices and does not certify all positive real parameters by enumeration.

## Relationship to prior work

Lafferty and Dunne (2010) introduce stochastic ecological network occupancy models with resource-dependent colonization, background extirpation, secondary extinction, and consumer-driven extirpation. Their open full text identifies consumers that are net biodiversity contributors or inhibitors using finite simulation examples. The present result concerns the restrictive but exactly solvable one-basal-resource, exchangeable-specialist submodel and provides an all-parameter, all-guild-size stationary phase classification plus an explicit many-consumer asymptotic; that classification is not established in the source's inspected model, example, results, or discussion.

Brockwell, Gani, and Resnick (1982) provide important general population-dependent catastrophe-process theory, and Chao and Zheng (2003) study a different immigration/birth/death process with total catastrophes. General stationary Markov balance and renewal methods are acknowledged as standard prior mathematics. The present conclusion is not a claim to invent these tools. The mathematical distinction is the finite pool of independently arriving specialists, explicit off-resource regeneration, the exact guild-size ordering of total species richness, and the universal threshold and asymptotic limit. Full text for Brockwell et al. was not accessible in this inspection; that is a concrete priority limitation, not evidence of absence.

## Limitations

This is an exact result only for one resource with symmetric, independent potential consumers and additive impacts \(kj\) on resource extirpation. The number \(m\) counts *potential distinct species*, not individuals. The universal sign law can fail under consumer interactions, generalists, resource-conditional immigration, or nonlinear attack. The large-guild limit sends \(m\to\infty\) while holding all five per-species rates fixed; it is not an ecological scaling prediction for a finite community. No field data or conservation benefit was tested. Literature priority remains provisional, particularly for historical population-dependent-catastrophe work that was not fully accessible. Independent validation has not been performed.

## References

1. Lafferty, K. D., and Dunne, J. A. (2010), *Stochastic ecological network occupancy (SENO) models: a new tool for modeling ecological networks across spatial scales*, Theoretical Ecology 3, 123–135. First published online 5 June 2010. https://doi.org/10.1007/s12080-010-0082-0
2. Brockwell, P. J., Gani, J., and Resnick, S. I. (1982), *Birth, immigration and catastrophe processes*, Advances in Applied Probability 14, 709–731. https://doi.org/10.2307/1427020
3. Chao, X., and Zheng, Y. (2003), *Transient analysis of immigration birth–death processes with total catastrophes*, Probability in the Engineering and Informational Sciences 17, 83–106. https://doi.org/10.1017/S0269964803171057
