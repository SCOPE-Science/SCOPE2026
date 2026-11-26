# Opposite-sign outbreak-alarm covariances and separated transmission thresholds on stars

## Finding

**Theorem.** Fix an integer \(m\ge2\). On a star with \(m\) leaves and one hub, retain each edge independently with probability \(p\in(0,1)\); choose one initial outbreak vertex uniformly among all \(m+1\) vertices. A perfect passive monitor at vertex \(v\) alarms if and only if the seed lies in its retained-edge component. Let \(Y_v\) denote this binary eventual-alarm indicator. For any two distinct leaves \(u,v\) and any leaf \(u\) and hub \(h\),

\[
\operatorname{Cov}(Y_u,Y_v)=\frac{1-p}{(m+1)^2}\bigl((m-1)^2p^3+(m+1)p^2-3p-1\bigr),
\]
\[
\operatorname{Cov}(Y_h,Y_u)=\frac{1-p}{(m+1)^2}\bigl(m(m-1)p^2+mp-1\bigr).
\]

Write \(\alpha_m\) for the unique root of the hub–leaf quadratic in \((0,1)\). For \(m\ge3\), write \(\beta_m\) for the unique root of the leaf–leaf cubic in \((0,1)\); for \(m=2\) set the boundary value \(\beta_2=1\). Then

\[
0<\alpha_m<\beta_m\le1.
\]

Both distinct-pair covariance types are strictly negative for \(0<p<\alpha_m\). On \(\alpha_m<p<\beta_m\), hub–leaf alarm covariance is strictly positive while leaf–leaf alarm covariance is strictly negative. For \(m\ge3\) and \(\beta_m<p<1\), both are positive. Each interior threshold gives a zero covariance for exactly the corresponding pair type. For \(m=2\), the distinct-leaf covariance stays negative throughout the interior. For all \(m\ge2\), hub–leaf covariance exceeds distinct-leaf covariance strictly at every interior transmission parameter. The two sign boundaries have different large-star scales:

\[
\lim_{m\to\infty}m\alpha_m=\frac{\sqrt5-1}{2},\qquad
\lim_{m\to\infty}m^{2/3}\beta_m=1.
\]

## Assumptions and scope

This is a one-source bond-percolation outbreak on a finite undirected star \(K_{1,m}\). The single source is selected **uniformly before** independently determining open edges. Monitors do not prevent or change transmission. The outcome is ever reached, not infected at a specified time. Probabilities and covariances average jointly over both the source and edge states. All edges share exactly the same open probability \(p\). The theorem does not assert an equivalence with general continuous-time SIR dynamics, especially when infectious periods create dependent transmissions along incident edges.

## Proof

Put \(n=m+1\). Enumerate the seed position, conditioning on which edges are open. For any specified leaf \(u\), the probability that it is reached from itself, from the hub, or from another leaf is respectively \(1\), \(p\), or \(p^2\), each weighted by the uniform seed probability \(1/n\). For the hub, source at itself succeeds, and each source leaf succeeds with probability \(p\). Hence

\[
\mathbb E Y_u=\frac{1+p+(m-1)p^2}{n},\qquad
\mathbb E Y_h=\frac{1+mp}{n}.
\]

For distinct leaves \(u,v\), both alarms occur with conditional probability \(p^2\) from the hub or either of those two leaves, and with probability \(p^3\) from each of the remaining \(m-2\) leaves. For hub and leaf \(u\), both alarms occur with probability \(p\) from either endpoint, and \(p^2\) from each other leaf. Therefore

\[
\mathbb E (Y_uY_v)=\frac{3p^2+(m-2)p^3}{n},\qquad
\mathbb E(Y_hY_u)=\frac{2p+(m-1)p^2}{n}.
\]

Subtracting products of the marginals and factoring gives exactly the two asserted covariance polynomials. Define

\[
L_m(p)=(m-1)^2p^3+(m+1)p^2-3p-1,\qquad
H_m(p)=m(m-1)p^2+mp-1.
\]

First, \(H_m(0)=-1\), \(H_m(1)=m^2-1>0\), and \(H_m'(p)=2m(m-1)p+m>0\) for \(p\ge0\). Thus \(H_m\) has exactly one root \(\alpha_m\in(0,1)\), with the asserted sign transition. Second, \(L_m(0)=-1\), \(L_m'(0)=-3\), and

\[
L_m''(p)=6(m-1)^2p+2(m+1)>0\qquad(p\ge0).
\]

Consequently \(L_m\) decreases until at most one positive critical point and thereafter strictly increases; it can have at most one positive zero, and crosses only from negative to positive. Its endpoint is

\[
L_m(1)=(m-2)(m+1).
\]

For \(m\ge3\) this is positive and yields exactly one interior positive zero \(\beta_m\). For \(m=2\), direct factorization gives

\[
L_2(p)=(p-1)(p^2+4p+1)<0\quad(0<p<1).
\]

Finally, the quadratic/cubic comparison is

\[
H_m(p)-L_m(p)=p\left[(m+3)+(m^2-2m-1)p-(m-1)^2p^2\right].
\]

For \(m\ge2\), the bracket is a concave quadratic in \(p\) with endpoint values \(m+3>0\) at \(p=0\) and \(m+1>0\) at \(p=1\). A concave function lies above its endpoint chord, so the bracket is strictly positive throughout \([0,1]\). Therefore \(H_m>L_m\) on \((0,1)\), the hub–leaf covariance always exceeds the distinct-leaf covariance, and \(H_m(\beta_m)>0\) whenever \(\beta_m\) is interior. Thus \(\alpha_m<\beta_m\); for \(m=2\), \(\alpha_2<\beta_2=1\). This proves the complete phase diagram.

For the asymptotics, substitute \(p=x/m\) into \(H_m\):

\[
H_m(x/m)=\frac{m-1}{m}x^2+x-1\longrightarrow x^2+x-1.
\]

Its unique positive root is \((\sqrt5-1)/2\), and monotonicity plus convergence at fixed values on either side of that root squeezes \(m\alpha_m\) to this limit. For the leaf–leaf threshold put \(p=x/m^{2/3}\). For every fixed \(x>0\),

\[
L_m(x/m^{2/3})=\frac{(m-1)^2}{m^2}x^3
+\frac{m+1}{m^{4/3}}x^2-\frac{3x}{m^{2/3}}-1
\longrightarrow x^3-1.
\]

For every fixed \(\epsilon\in(0,1)\), the two values at \(x=1-\epsilon\) and \(x=1+\epsilon\) have opposite signs for sufficiently large \(m\). The unique positive crossing hence lies between them; \(m^{2/3}\beta_m\to1\). No finite computation is used for the unbounded-\(m\) conclusions.

For a concrete four-vertex example, \(m=3\), \(p=1/2\), and exact substitution yields

\[
\operatorname{Cov}(Y_h,Y_u)=\frac1{16}>0,\qquad
\operatorname{Cov}(Y_u,Y_v)=-\frac1{32}<0.
\]

## Verification

Run `python verify.py` in the directory containing this document. This standalone standard-library checker exhausts all binary edge states and all uniformly chosen source positions on stars with \(2\le m\le8\) for six rational probabilities, and independently checks the two joint moments and both marginal formulas against the stated symbolic expressions. It also reproduces the four-vertex exact covariances, and tests polynomial endpoint/order identities using exact rational arithmetic for \(2\le m\le1000\). The separate `certificate.json` reports the counts and output values. In the completed check, 42 parameter combinations covered 24,552 weighted source/edge outcomes. These finite tests are reproducibility checks, not substitutes for the infinite algebraic proof.

## Relationship to prior work

Kenah and Robins (arXiv first submitted 2006-10-30) distinguish valid epidemic-percolation constructions from naive undirected bond-percolation replacements for general SIR models. Leskovec and coauthors (2007) frame network sensor placement as maximizing outbreak detection, but the inspected methods do not give a pair-type covariance sign diagram or the two separated threshold exponents. The present statement is confined to a finite star with one uniform source, independent undirected open edges, and eventual detection; it is not inferred from those broader frameworks.

Donnelly's 1993 abstract discusses positive association for epidemic models, including generalized Reed–Frost dynamics. The full text was not available in the present literature examination, so assumptions on the initial infection law and their relationship to exactly-one-uniform-source mixing could not be checked from that paper. Positive-association results conditional on a prescribed or independently generated initial infection set do not, by themselves, cover an exactly-one-source mixture, which is the source of possible negative covariance here. The 2018 Rodriguez–Roldán-Correa–Valencia counterexample concerns **simultaneous infection status at a time** in continuous-time SIR rather than final component-membership alarms. These distinctions are mathematical comparisons of assumptions and observables, not claims that all other published results have been exhaustively excluded.

## Limitations

The result is a classification for one family of graph geometries and one precise outbreak model, not a universal covariance sign law on general contact graphs. Uniformity of the source and the distinction between ever infected and infected at a fixed time matter. Transmission heterogeneity, multiple independently seeded outbreaks, directed contact mechanisms, and stochastic infectious durations with shared transmission dependence are outside the theorem. A directly equivalent earlier star-graph covariance formula under another terminology cannot be absolutely excluded without further bibliography access. No independent review or validation has been performed.

## References

1. Kenah, E., and Robins, J. M., *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057, first posted 2006-10-30; Phys. Rev. E **76**, 036113 (2007). https://arxiv.org/abs/q-bio/0610057
2. Leskovec, J., Krause, A., Guestrin, C., Faloutsos, C., VanBriesen, J., and Glance, N., *Cost-effective Outbreak Detection in Networks*, CMU-ML-07-111 (June 2007), ACM KDD 2007. https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf
3. Donnelly, P., *The correlation structure of epidemic models*, Mathematical Biosciences **117**, 49–75 (1993), DOI:10.1016/0025-5564(93)90017-5. https://pubmed.ncbi.nlm.nih.gov/8400584/
4. Rodriguez, P. M., Roldán-Correa, A., and Valencia, L. A., *Comment on “Nodal infection in Markovian ...”*, arXiv:1807.06909 (2018). https://arxiv.org/abs/1807.06909
