# Parity and sharp factorial screening of a single adsorption-rate defect on regular trees

## Finding

Let \(\mathbb T_q\) be the infinite regular tree of degree \(q\ge3\). Give one marked vertex a positive exponential arrival rate \(a\), and give every other vertex rate one. Each vertex attempts irreversible monomer adsorption once, at its clock time; acceptance occurs exactly when no neighbor has previously been accepted. For a vertex at distance \(r\ge1\), let \(p_r(a)\) denote its terminal acceptance probability. The undisturbed value is
\[
p_*=\frac{1-(q-1)^{-2/(q-2)}}2.
\]

Set
\[
L=\frac{\log(q-1)}{q-2},\quad h(x)=[1+(q-2)x]^{-1/(q-2)},\quad x(u)=\frac{e^{(q-2)u}-1}{q-2},
\]
\[
g_a(u)=1-\int_0^{x(u)}a(1-s)^{a-1}h(s)^{q-1}\,ds-e^{-u},\qquad (Tf)(u)=\int_0^u f(v)\,dv.
\]
Then for every integer \(r\ge1\),
\[
\boxed{p_r(a)-p_*=(-1)^{r-1}\int_0^L e^{-u}(T^{r-1}g_a)(u)\,du.}
\]
When \(a\ne1\) this difference is nonzero with sign \((-1)^r\operatorname{sgn}(a-1)\), and
\[
\boxed{p_r(a)-p_*=(-1)^r(a-1)\frac{e^{-L}L^{r+1}}{(r+1)!}\left(1+O_{q,a}(r^{-1})\right)}
\qquad (r\to\infty).
\]
The valid all-distance bound \(|p_r(a)-p_*|\le L^r/r!\) also follows. In particular, the perturbation alternates across shells and is screened factorially even on a branching graph.

## Assumptions and scope

The graph is the infinite \(q\)-regular tree for a fixed integer \(q\ge3\). Every vertex has exactly one independent exponential attempt time. The marked root has rate \(a\in(0,\infty)\), and all others have rate one. Accepted monomers are permanent and prohibit acceptance at adjacent vertices. Distance \(r\) is an integer at least one; no asymptotic limit in the rate or degree is assumed. In the sharp large-distance formula, both \(q\) and \(a\) remain fixed. At \(a=1\) the entire difference vanishes exactly.

To see that the process is well-defined despite infinitely many clocks, expose decreasing-priority paths into any given vertex. There are at most \(q(q-1)^{k-1}\) paths of length \(k\). For paths not meeting the marked vertex, the probability of the prescribed strict ordering is \(1/(k+1)!\); when one vertex has a different continuous clock law, conditioning on that clock bounds the corresponding probability by \(1/k!\). The sum over all paths of increasing lengths is finite, ensuring almost-sure finite dependence and consistency of finite-volume evaluations.

## Proof

**Time normalization and directed cavities.** Apply the strictly increasing time transformation \(x=1-e^{-t}\), so that ordinary attempts have independent uniform \((0,1)\) labels, while the marked attempt has density \(a(1-x)^{a-1}\). For a directed branch obtained by deleting its parental edge, let \(h(x)\) be the probability that its ordinary root is not yet accepted by label \(x\). Its \(q-1\) child branches are independent before a root attempt. Therefore
\[
h'(x)=-h(x)^{q-1},\qquad h(0)=1,
\]
which gives the stated \(h\). A full ordinary vertex has acceptance density \(h(x)^q\); hence
\[
p_*=\int_0^1h(x)^q\,dx=\frac{1-h(1)^2}{2}.
\]

**The defect and propagation.** In the directed subtree facing away from a target vertex, the marked vertex has nonacceptance probability
\[
f_0(x)=1-\int_0^x a(1-s)^{a-1}h(s)^{q-1}\,ds.
\]
Let \(f_j\) denote the corresponding directed nonacceptance probability after \(j\) ordinary vertices along the unique path toward the target. Every such vertex has one possibly affected child branch and \(q-2\) ordinary branches, so
\[
f_j'(x)=-h(x)^{q-2}f_{j-1}(x),\quad f_j(0)=1\quad (j\ge1).
\]
The undisturbed message \(h\) satisfies the same identity with \(h\) replacing \(f_{j-1}\). Define \(\delta_j=f_j-h\) and \(u=-\log h(x)\). Since \(du/dx=h(x)^{q-2}\),
\[
\frac{d\delta_j}{du}=-\delta_{j-1},\quad \delta_j(0)=0,\quad
\delta_0(u)=g_a(u).
\]
Thus \(\delta_j(u)=(-1)^j(T^jg_a)(u)\). At a target distance \(r\), one incoming branch has message \(f_{r-1}\) and the other \(q-1\) have message \(h\). Subtracting the homogeneous acceptance integral gives
\[
p_r(a)-p_*=\int_0^1h(x)^{q-1}\delta_{r-1}(x)\,dx
=(-1)^{r-1}\int_0^L e^{-u}(T^{r-1}g_a)(u)\,du,
\]
where \(h^{q-1}\,dx=e^{-u}\,du\). This last Jacobian is essential.

**Strict parity.** Couple the marked arrival label at rate \(a\) to the uniform arrival via the same uniform random variable. For \(a>1\), the marked attempt is strictly earlier, and advancing a root attempt in its detached branch cannot reduce the event of that root's acceptance by a given time. Since an interval of early arrival and late neighbors has positive probability, \(f_0(x)<h(x)\) for each \(x\in(0,1]\). For \(0<a<1\), the inequality reverses. Accordingly \(g_a(u)\) has strict sign \(-\operatorname{sgn}(a-1)\) for \(u>0\). Every Volterra integral preserves that strict sign. The displayed response formula yields \(\operatorname{sgn}(p_r-p_*)=(-1)^r\operatorname{sgn}(a-1)\).

**Factorial screening and exact leading constant.** The difference of two nonacceptance probabilities has absolute value at most one. Therefore \(|T^{r-1}g_a(u)|\le u^{r-1}/(r-1)!\), and integrating yields \(|p_r-p_*|\le L^r/r!\). Moreover, by the source density at zero and \(x(u)=u+O(u^2)\),
\[
g_a(u)=-(a-1)u+O_{q,a}(u^2).
\]
Continuity on \([0,L]\) upgrades the remainder to the bound \(C_{q,a}u^2\) over the whole interval. Applying \(T^{r-1}\) gives
\[
(T^{r-1}g_a)(u)=-(a-1)\frac{u^r}{r!}+O_{q,a}\!\left(\frac{u^{r+1}}{(r+1)!}\right).
\]
Finally, integration at the upper endpoint yields \(\int_0^Le^{-u}u^r\,du=e^{-L}L^{r+1}(r+1)^{-1}(1+O_q(r^{-1}))\). The remainder contributes only relative order \(1/r\) when \(a\ne1\), proving the announced asymptotic.

## Verification

For \(q=3\) and \(a=2\), direct integration gives \(g_2(u)=-3+3e^{-u}+2u\) and \(L=\log2\). In particular,
\[
p_1(2)-p_*=\frac58-\log2,\qquad
p_2(2)-p_*=\frac18-\frac12\log2+\frac12(\log2)^2.
\]
With \(p_*=3/8\), the first two affected shell probabilities are approximately \(0.306852819440\) and \(0.393652916679\). The accompanying `verify.py` numerically compares the infinite-tree Volterra representation against a separately formulated finite-depth subtree recursion in the original uniform-time coordinate. It tests fifteen combinations of branching degree, marked rate and distance, with absolute discrepancies below \(1.5\times10^{-7}\). Finite-depth numerics corroborate, rather than certify, the infinite-tree theorem.

## Relationship to prior work

Evans (1984) developed exact empty-cluster shielding equations for translation-invariant irreversible Bethe-lattice filling. Penrose and Sudbury (2005, Theorems 12–13) proved the homogeneous single-site occupation law and all-distance two-site correlations for blocking RSA on regular trees, including the cavity equation used here. Krivelevich, Mészáros, Michaeli and Shikhelman (2023 prepublication; journal 2024) recover homogeneous tree densities via random-greedy independent-set local limits. The present claim concerns an independently variable rate at one fixed site, the *finite-amplitude* response of every other site, and a sharp rate-dependent leading coefficient as graph distance grows. A homogeneous covariance identity does not itself imply these finite-rate formulas. Related periodic, rather than single-site, rate asymmetry has been studied in adsorption percolation. Priority is provisional because additional specialized inhomogeneous adsorption literature may exist.

## Limitations

This is a terminal one-attempt blocking process on an infinite regular tree, not a general statement for finite-girth graphs, general heterogeneous rate fields, repeated-attempt dynamics, or lattice graphs with loops. The result gives one-point responses and not joint defect-response correlations. No uniformity is asserted as \(a\to0\), \(a\to\infty\) or \(q\to\infty\), and no independent external review has been performed.

## References

- J. W. Evans, *Exactly solvable irreversible processes on Bethe lattices*, Journal of Mathematical Physics **25** (1984), 2527–2532.
- M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability **15** (2005), 853–889. https://arxiv.org/abs/math/0503519 ; https://doi.org/10.1214/105051604000000765
- M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms **64** (2024), 986–1015. https://doi.org/10.1002/rsa.21200
- *Percolation of even sites for random sequential adsorption*, Stochastic Processes and their Applications (2012). https://doi.org/10.1016/j.spa.2012.01.007
