# A sharp geometric-mean recovery core for open three- and four-member hypercycles

## Finding
Consider the open, equal-dissipation cyclic autocatalysis model
\[
\dot w_i=w_i\bigl(e^{-\gamma S}w_{i-1}-d\bigr),\qquad S=\sum_{i=1}^n w_i,\qquad w_0=w_n,
\]
with \(n\in\{3,4\}\), \(d,\gamma>0\), and \(0<\gamma nd<e^{-1}\). Let \(S_-<\gamma^{-1}<S_+\) be the two positive roots of \(S e^{-\gamma S}=nd\), and let \(G(w)=(\prod_{i=1}^n w_i)^{1/n}\).

**Theorem (sharp recovery core).** For every strictly positive initial vector satisfying
\[
S(0)\le S_+,\qquad G(w(0))>\frac{S_-}{n},
\]
there is a unique global solution and
\[
\lim_{t\to\infty}w_i(t)=\frac{S_+}{n}\quad\text{for every }i=1,\ldots,n.
\]
More quantitatively, with \(P_0=\prod_i w_i(0)\), at every \(t\ge0\),
\[
S(t)\le S_+,\quad \prod_iw_i(t)\ge P_0,\quad
w_i(t)\ge\frac{P_0}{S_+^{n-1}}>0.
\]
The geometric-mean constant is optimal among criteria of the stated form: for any \(c<S_-/n\), some strictly positive data have \(S(0)\le S_+\) and \(G(w(0))>c\) but approach total extinction. For \(n\ge5\), the specific cyclic-quadratic inequality underpinning this recovery certificate fails, explaining the natural three-/four-member scope without asserting that every higher-dimensional trajectory becomes extinct.

## Assumptions and scope
The model is deterministic, finite-dimensional, autonomous, with a cyclic predecessor of exactly one type for each type, a common positive dissipation \(d\), and a common density factor \(e^{-\gamma S}\). The theorem concerns an isolated open hypercycle without a second interacting consumer community, mutation, migration, spatial diffusion, or parameter evolution. Every quantifier refers to real positive parameters and continuous-time solutions; no finite simulation is used to infer infinite-time convergence.

## Proof
**1. The two roots and the two sign regions.** The function \(h(S)=S e^{-\gamma S}\) rises from zero to \((\gamma e)^{-1}\) at \(S=\gamma^{-1}\), then falls to zero. Hence \(0<nd<(\gamma e)^{-1}\) gives exactly \(S_-\) and \(S_+\), with
\[
h(S)>nd\quad\Longleftrightarrow\quad S_-<S<S_+.
\]
The origin and the two equal-coordinate states \(w_i=S_\pm/n\) are equilibria.

**2. Two exact differential identities.** Put \(P=\prod_{i=1}^n w_i\), \(Q=\sum_iw_iw_{i-1}\), and \(\phi=e^{-\gamma S}\). From the equations,
\[
\dot S=\phi Q-dS,\qquad \frac{\dot P}{P}=\sum_i\frac{\dot w_i}{w_i}=\phi S-nd.
\]
For \(n=3\), the identity
\[
\frac{S^2}{3}-Q=\frac{(w_1-w_2)^2+(w_2-w_3)^2+(w_3-w_1)^2}{6}\ge0
\]
holds, with equality only at equal coordinates. For \(n=4\), writing \(p=w_1+w_3\) and \(q=w_2+w_4\), one has \(Q=pq\) and
\[
\frac{S^2}{4}-Q=\frac{(p-q)^2}{4}\ge0.
\]
Thus for either admissible \(n\), \(Q\le S^2/n\), and in particular the vector field at \(S=S_+\) satisfies \(\dot S\le S_+(S_+e^{-\gamma S_+}/n-d)=0\).

**3. An explicit compact invariant core.** Fix initial \(P_0>(S_-/n)^n\). The set
\[
K=\{w_i>0:\ \sum_iw_i\le S_+,\ \prod_iw_i\ge P_0\}
\]
is closed, bounded, and bounded away from every coordinate face because \(w_i\ge P_0/S_+^{n-1}\). It is nonempty because it contains the prescribed initial vector. By the arithmetic–geometric mean inequality,
\[
S\ge nP^{1/n}\ge nP_0^{1/n}>S_-\quad\text{throughout }K.
\]
Therefore on \(K\), \(\dot P=P(h(S)-nd)\ge0\), with equality possible only when \(S=S_+\). The preceding estimate for \(\dot S\) makes the upper face inward pointing, and \(\dot P\ge0\) makes the product face inward pointing. A first-exit argument implies forward invariance of \(K\). Local uniqueness and compactness imply existence for all \(t\ge0\). The quantitative bounds in the theorem follow immediately.

**4. Identification of the only invariant zero-derivative set.** Since \(P\) is increasing and bounded on \(K\), the invariance principle puts the omega-limit set inside the largest invariant subset of \(\{\dot P=0\}\cap K\). Because \(S>S_-\), this subset lies on \(S=S_+\) and necessarily has \(\dot S=0\), hence \(Q=S_+^2/n\).

For \(n=3\), equality in the identity of Step 2 forces \(w_1=w_2=w_3=S_+/3\).

For \(n=4\), equality yields \(p=q=S_+/2\). Define \(u=w_1-w_3\) and \(v=w_2-w_4\). Direct subtraction of the original differential equations gives
\[
\dot p-\dot q=-\phi uv-d(p-q),\quad
\dot u=\frac\phi2(uq-pv)-du,\quad
\dot v=\frac\phi2(qu+pv)-dv.
\]
An orbit remaining on \(S=S_+\), \(p=q\) has \(uv=0\) at every time and, since \(\phi S_+/4=d\), its remaining dynamics obey \(\dot u=-dv\), \(\dot v=du\). No nonzero rotating solution can have \(uv\equiv0\); thus \(u=v=0\) and all four concentrations equal \(S_+/4\). The largest invariant subset is therefore the singleton upper coexistence equilibrium for both \(n=3\) and \(n=4\). The omega-limit set is that singleton, proving convergence of every coordinate.

**5. Sharpness of the geometric-mean threshold.** Choose any \(c<S_-/n\), and take an equal-coordinate initial vector \(w_i(0)=r\) with \(\max\{c,0\}<r<S_-/n\). It has \(S(0)=nr<S_-<S_+\) and \(G(w(0))=r>c\). The diagonal stays invariant and obeys
\[
\dot r=r\bigl(r e^{-\gamma nr}-d\bigr)<0\quad\text{for }0<r<S_-/n.
\]
Its only possible limit is zero. Thus no uniformly smaller geometric-mean bound can guarantee recovery under the same upper biomass cap.

**6. Natural dimension boundary for this certificate.** For \(n=5\), the positive vector \((3,2,1,1,2)\) has \(S=9\) and \(Q=17>81/5=S^2/5\). More generally small positive first-Fourier-mode perturbations of the equal vector yield \(Q>S^2/n\) for any \(n\ge5\), since \(\cos(2\pi/n)>0\). This only shows that the particular universal quadratic barrier in Step 2 is specific to \(n\le4\); it does not classify higher-dimensional basins.

## Verification
The accompanying `check_hypercycle.py` replays the two polynomial identities by exact symbolic arithmetic, evaluates the five-member counterexample exactly, locates the two roots for representative positive parameters, and numerically checks the forward bounds and diagonal extinction/recovery behavior. All asymptotic and all-parameter statements follow from the proof, not from the finite computations. To run: `python check_hypercycle.py`. Required packages: Python 3 standard library only.

## Relationship to prior work
Bratus, Drozhzhin and Novozhilov (arXiv:2511.06509v1, Section 2, Proposition 2.4 and Appendix) formulate the exact open system, its positive equilibrium condition, and local stability for three and four types. They describe the global basin separation as numerically suggested rather than proved. Pavlovich and Bratus (2012) analyze stability and parameter phase portraits for open cyclic replication. Benaïm, Hofbauer and Sandholm (2008) describe global coexistence in the *closed, normalized* three-/four-member classical hypercycle; normalized permanence does not supply the present absolute-population threshold with its competing extinction equilibrium. The present result asserts an explicit full-dimensional, forward-invariant *sufficient* recovery set, convergence throughout that set, and optimality of its geometric-mean constant. It does not claim an exact characterization of the entire recovery basin.

## Limitations
The certificate is sufficient rather than necessary for survival. Its exact optimality applies only to the class of uniform geometric-mean lower bounds combined with the stated biomass upper cap. The theorem assumes strictly positive data and equal dissipation, and only covers three or four cyclic types. It does not prove claims for general interaction matrices, higher-dimensional cycles, mutations, or stochastic extinction. Priority against unpublished or inaccessible historical results is not certified; especially the 2012 open-cyclic paper warrants further expert comparison because its accessible representation has imperfect mathematical extraction. No independent mathematical validation has been performed.

## References
1. A. S. Bratus, S. V. Drozhzhin, A. S. Novozhilov, *A mathematical framework of consumer–resource dynamics: How to incorporate interactions between interactions in evolutionary process*, arXiv:2511.06509v1, first posted 2025-11-09, https://arxiv.org/abs/2511.06509.
2. E. N. Pavlovich, A. S. Bratus, *Studying the Dynamics of Open Cyclic Replication Systems*, Moscow University Computational Mathematics and Cybernetics 36 (2012), 137–144, https://doi.org/10.3103/S0278641912030077.
3. M. Benaïm, J. Hofbauer, W. H. Sandholm, *Robust permanence and impermanence for stochastic replicator dynamics*, Journal of Biological Dynamics 2 (2008), 180–195, https://doi.org/10.1080/17513750801915269.
4. J. Hofbauer, J. Mallet-Paret, H. Smith, *Stable periodic solutions for the hypercycle system*, Journal of Dynamics and Differential Equations 3 (1991), 423–436, https://doi.org/10.1007/BF01049740.
