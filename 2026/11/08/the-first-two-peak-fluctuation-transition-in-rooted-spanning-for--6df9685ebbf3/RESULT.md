# The first two-peak fluctuation transition in rooted spanning forests

## Finding
Consider the weighted three-vertex path with edge conductances \(a,b>0\). A rooted spanning forest \(F\) has probability proportional to \(q^{r(F)}\prod_{e\in F}w_e\), for any root fugacity \(q>0\), with one oriented root in each component. Let \(R_q=r(F)\) and \(V(q)=\operatorname{Var}(R_q)\). Write
\[
c=\sqrt{3ab},\qquad v=\frac{a+b}{\sqrt{3ab}},\qquad u(q)=\cosh\!\left(\log\frac q c\right).
\]
**Complete variance-mode classification.** The exact variance is
\[
V(q)=\frac{1+v u(q)}{(v+u(q))^2}.
\]
If \(5-2\sqrt6\le a/b\le5+2\sqrt6\), the function \(q\mapsto V(q)\) has exactly one maximizer, \(q=c\), with maximum \(1/(v+1)\). At either endpoint, this maximum is quartically flat in \(\log(q/c)\). If \(a/b<5-2\sqrt6\) or \(a/b>5+2\sqrt6\), there are exactly two distinct strict global maximizers
\[
q_\pm=c\exp\left(\pm\operatorname{arcosh}\left(v-\frac2v\right)\right),
\qquad V(q_\pm)=\frac{v^2}{4(v^2-1)},
\]
separated by a strict local minimum \(q=c\), where \(V(c)=1/(v+1)\). Their product is \(q_-q_+=3ab\). The three-vertex path is the smallest connected weighted simple graph on which a fugacity-dependent rooted-forest component-count variance can have two local maxima.

## Assumptions and scope
The graph is the undirected path on three labeled vertices, with strictly positive finite conductances \(a,b\); the oriented rooted-forest ensemble includes every spanning forest, with each component oriented toward one chosen root. All statements hold for every real \(q>0\), including the exact boundary edge ratios. This is a classification of **maxima of variance as a function of fugacity**, not of modes of the root-count probability mass function.

## Proof
An empty edge set gives one forest with three roots; either single edge has two choices of component root, and the two-edge tree has three choices. Thus the partition function and root-count generating function are, without omitted multiplicities,
\[
Z(q)=q^3+2(a+b)q^2+3abq,
\quad
\mathbb E[z^{R_q}]=\frac{q^3z^3+2(a+b)q^2z^2+3abqz}{Z(q)}.
\]
The two nonzero eigenvalues of the usual positive weighted graph Laplacian are
\[
\lambda_\pm=a+b\pm\sqrt{a^2-ab+b^2},\quad
\lambda_-+\lambda_+=2(a+b),\quad\lambda_-\lambda_+=3ab.
\]
Factoring \(Z(q)=q(q+\lambda_-)(q+\lambda_+)\), the generating function becomes
\[
\mathbb E[z^{R_q}]
=z\prod_{\sigma\in\{-,+\}}
\frac{\lambda_\sigma+qz}{\lambda_\sigma+q}.
\]
Hence \(R_q\) equals one plus two independent Bernoulli variables with success probabilities \(q/(q+\lambda_\pm)\), yielding
\[
V(q)=\frac{q\lambda_-}{(q+\lambda_-)^2}
+\frac{q\lambda_+}{(q+\lambda_+)^2}.
\]
Set \(t=\log(q/c)\) and \(h=\tfrac12\log(\lambda_+/\lambda_-)\). Then \(\cosh h=(a+b)/c=v\). The identity \(\frac{q\lambda}{(q+\lambda)^2}=\frac1{2(1+\cosh(\log(q/\lambda)))}\) and the hyperbolic cosine addition formula give
\[
V(q)=\frac12\left(
\frac1{1+\cosh(t-h)}+\frac1{1+\cosh(t+h)}
\right)=\frac{1+v\cosh t}{(v+\cosh t)^2}.
\]
For \(u=\cosh t\in[1,\infty)\), direct differentiation shows
\[
\frac{\partial}{\partial u}\frac{1+vu}{(v+u)^2}
=\frac{v^2-2-vu}{(v+u)^3}.
\]
If \(v\le2\), this derivative is negative for all \(u>1\); therefore \(u=1\), equivalently \(q=c\), is the unique maximum. If \(v>2\), the derivative changes once from positive to negative at \(u_*=v-2/v>1\). The equation \(\cosh t=u_*\) has exactly the two displayed solutions. The center \(t=0\) is then a strict local minimum. Substitution yields the exact peak values and symmetry product. The condition \(v\le2\) is exactly \((a+b)^2\le12ab\), or \(5-2\sqrt6\le a/b\le5+2\sqrt6\). At \(v=2\), Taylor expansion about \(t=0\) yields
\[
V(ce^t)=\frac13-\frac{t^4}{108}+O(t^6),
\]
so the transition is quartically flat, not a plateau. Since the variance tends to zero as \(q\downarrow0\) or \(q\uparrow\infty\), all stated local maxima are global. On a two-vertex connected graph the variance is only \(q\lambda/(q+\lambda)^2\), uniquely maximized at \(q=\lambda\); on a one-vertex graph it is zero. Thus three vertices are minimal.

## Verification
The accompanying standalone `verify.py` reproduces the exact three-outcome rooted-forest distribution from independent edge-set/root counts and checks it against the differentiated partition-function variance. It also checks the reciprocal symmetry \(V(q)=V(3ab/q)\), the hyperbolic identity, and both sides of the bifurcation on numerous positive conductances. The program uses Python's standard library, exact rational arithmetic where possible, and explicit floating tolerances only for hyperbolic checks. Run `python3 verify.py`. Its finite computations are consistency checks; the preceding derivative argument proves the theorem for all positive real parameters.

## Relationship to prior work
Avena, Castell, Gaudillière and Mélot (2018, Section 2.1, equation (19)) give the general Bernoulli spectral law and variance formula for the rooted-forest root count. Avena, Driessen and Koperberg (2021/2023, Section 1) study fugacity monotonicities and cycle-free geometries, explicitly observing that the mean root count increases with fugacity. The determinant/factorization and Bernoulli law used above are **prior results**, not new claims. The additional assertion proved here is the complete first-size classification of the variance's *number of fugacity maxima*, its sharp edge-weight threshold, peak locations and critical quartic behavior. The inspected articles did not present that classification. This is a best-knowledge priority assessment rather than a proof that it appears nowhere else.

## Limitations
The result concerns exactly the weighted three-vertex path, not arbitrary networks or all higher moments. It does not assert that the root-count law itself is bimodal. General spectral variance formulas make the calculation accessible; possible unrecognized prior treatments of two separated Bernoulli logistic variance peaks remain a historical-priority risk. Independent mathematical validation has not occurred.

## References
1. L. Avena, F. Castell, A. Gaudillière and C. Mélot, *Random Forests and Networks Analysis*, Journal of Statistical Physics 173 (2018), 985–1027, DOI: https://doi.org/10.1007/s10955-018-2124-8, especially Section 2.1 and equation (19). First journal publication 2 August 2018.
2. L. Avena, A. Gaudillière, *Two Applications of Random Spanning Forests*, Journal of Theoretical Probability 31 (2018), 1975–2004, DOI: https://doi.org/10.1007/s10959-017-0771-3. First online publication 18 July 2017.
3. L. Avena, J. Driessen and T. Koperberg, *Loop-erased partitioning of a network: monotonicities & analysis of cycle-free graphs*, arXiv:2103.14436, first submitted 26 March 2021; https://arxiv.org/abs/2103.14436.
