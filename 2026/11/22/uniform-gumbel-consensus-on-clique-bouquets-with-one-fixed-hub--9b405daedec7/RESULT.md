# Uniform Gumbel consensus on clique bouquets with one fixed hub

## Finding
For all integers \(m,r\ge1\), let \(G_{m,r}=K_1\vee(mK_r)\) be \(m\) disjoint complete \(r\)-vertex petals attached to one universal hub. In the continuous-time voter model, the hub keeps opinion \(+\) permanently; each other vertex updates at rate one, copying a uniformly selected neighbor, and all other vertices initially have opinion \(-\). Denote the first time all vertices are \(+\) by \(T_{m,r}\). Put
\[
 a_{r,j}=(-1)^{j-1}\frac{2(r!)^2}{(r-j)!(r+j)!},\quad 1\le j\le r,\qquad c_r=\frac{2r}{r+1}.
\]
Then, **without any fixed-petal-size restriction**,
\[
 \Pr(T_{m,r}\le t)=\left(1-\sum_{j=1}^{r}a_{r,j}e^{-j^2t/r}\right)^m,\quad t\ge0.
\]
Equivalently, the independent petal consensus times have the law \(\sum_{j=1}^{r}E_j\), with independent \(E_j\sim\operatorname{Exp}(j^2/r)\). For every integer sequence \(r=r_m\ge1\), including arbitrarily fast-growing and oscillating sequences,
\[
 \frac{T_{m,r_m}}{r_m}-\log(mc_{r_m})\ \Longrightarrow\ G,
 \qquad \Pr(G\le x)=e^{-e^{-x}},
\]
**uniformly** over the petal size in the stronger sense
\[
 \sup_{r\ge1}\left|\Pr\left\{\frac{T_{m,r}}r-\log(mc_r)\le x\right\}-e^{-e^{-x}}\right|\longrightarrow0
\]
for each fixed real \(x\) as \(m\to\infty\). Moreover the means satisfy, uniformly in \(r\ge1\),
\[
 \frac{\mathbb ET_{m,r}}r=\log(mc_r)+\gamma+o(1),
\]
where \(\gamma\) is Euler's constant. In particular \(r=1\) gives the centered star law, while for the friendship graph \(r=2\),
\[
 \Pr(T_{m,2}\le t)=\left(1-\tfrac43e^{-t/2}+\tfrac13e^{-2t}\right)^m,
 \qquad \mathbb ET_{m,2}=2\log(4m/3)+2\gamma+o(1).
\]
Unlike independent rate-one first-passage spreading on the same clique-bouquet geometry, **no** \(\log\log m\) correction occurs, for any petal-size sequence.

## Assumptions and scope
The hub has no update clock (its opinion is fixed), all \(mr\) other sites have independent Poisson clocks of rate one, and when a clock rings its vertex copies exactly one uniformly chosen neighbor. In particular each peripheral vertex has degree \(r\), including the hub neighbor. Time is continuous, not global single-site updates or rate-one-per-edge copying. All vertices except the hub start in the negative opinion. The graph consists of exactly \(m\) disjoint \(r\)-cliques plus hub-to-periphery edges; \(m,r\) are positive integers. No randomness is assumed in the graph.

## Proof
**1. Independent petals.** Because the hub never changes opinion, evolution within distinct petals uses disjoint Poisson processes and independent random choices. Let \(\tau_r\) be the all-positive time of one petal of \(r\) ordinary voters together with the fixed hub. Then \(T_{m,r}\overset d=\max_{1\le i\le m}\tau_{r,i}\), for independent identically distributed \(\tau_{r,i}\).

**2. Exact single-petal law by backward arrows.** Construct the voter model using directed Poisson copying arrows of rate \(1/r\) from each peripheral site to each of its \(r\) neighbors. To decide the opinion of every peripheral site at a fixed time \(t\), follow its arrows backward in time. Ancestral lines coalesce on meeting, and are killed when first reaching the fixed-positive hub. Because every vertex outside the hub initially holds negative opinion, all sites are positive at \(t\) exactly when all \(r\) ancestral lines have been killed by backward time \(t\). Stationarity of the independent arrows implies that this backward process is distributed as a forward system of coalescing rate-one random walks started at all \(r\) peripheral sites with an absorbing hub.

Suppose exactly \(k\) active lines remain, occupying \(k\) distinct peripheral sites. Each of the \(k\) lines attempts to jump at rate one, and each line has exactly \(k\) killing destinations: the hub plus the other \(k-1\) occupied sites. Consequently the total rate of a transition from \(k\) to \(k-1\) lines is \(k^2/r\), independent of the particular occupied sites. Other jumps merely relocate lines. The strong Markov property therefore gives \(r\) independent exponential holding times with respective rates \(r^2/r,(r-1)^2/r,\ldots,1/r\). In particular
\[
 \mathbb E e^{-s\tau_r}=\prod_{j=1}^{r}\frac{j^2}{j^2+rs},\qquad s\ge0.
\]
The poles are distinct. Partial fractions yield
\[
 \Pr(\tau_r>t)=\sum_{j=1}^r\left(\prod_{k\ne j}\frac{k^2}{k^2-j^2}\right)e^{-j^2t/r}.
\]
Using \(\prod_{k\ne j}(k-j)(k+j)=(-1)^{j-1}(r-j)!(r+j)!/(2j^2)\) gives the stated coefficients. Thus the exact distribution of the maximum follows from step 1.

**3. Uniform one-petal extreme tail.** Write \(Y_r=\tau_r/r\). For \(r\ge1\) and all \(y\ge0\),
\[
 \Pr(Y_r>y)=c_re^{-y}+R_r(y),\qquad
 |R_r(y)|\le2\sum_{j=2}^{\infty}e^{-j^2y}.
\]
Indeed \(|a_{r,j}|=2\prod_{k=1}^j(r+1-k)/(r+k)\le2\) and \(a_{r,1}=c_r\in[1,2)\). For \(y>0\), since \((j+1)^2-j^2\ge5\) for \(j\ge2\),
\[
 |R_r(y)|\le\frac{2e^{-4y}}{1-e^{-5y}}.
\]
For each fixed \(x\), choose \(y=\log(mc_r)+x\). The bound is \(O_x(m^{-4})\) uniformly over all \(r\), so
\[
 \sup_{r\ge1}\left|m\Pr(Y_r>\log(mc_r)+x)-e^{-x}\right|=O_x(m^{-3}).
\]
Independence and \((1-p)^m\to e^{-mp}\) prove the uniform Gumbel limit. It needs no regularity of \(r_m\).

**4. Uniform first moment.** For \(x\ge0\) and all large \(m\), the bound in step 3 with \(y=\log(mc_r)+x\) gives
\[
 \Pr\{T_{m,r}/r>\log(mc_r)+x\}\le C(1+e^{-3x})e^{-x},
\]
with an absolute constant \(C\). Conversely \(Y_r\) contains an independent \(\operatorname{Exp}(1)\) summand, so \(\Pr(Y_r>y)\ge e^{-y}\) for every \(y\ge0\). Therefore for \(x\ge0\), setting \(y=\log(mc_r)-x\), the probability of the centered maximum falling below \(-x\) is at most \(\exp(-e^x/2)\) when \(y\ge0\), and zero otherwise. These integrable bounds establish uniform integrability of the centered maxima. Integrating their tails, using the uniform pointwise convergence from step 3, gives the Gumbel mean \(\gamma\) uniformly in \(r\), proving the assertion.

**5. Topological comparison.** In first-passage bond flooding on these same graphs, the single-clique completion time is a sum of independent exponentials with rates \(j(r+1-j)\); for \(r\ge2\), the slowest rate is repeated twice, so the maximum needs a \(\log\log m\) centering. In the present coalescent voter clock, the rates \(j^2/r\) have a unique smallest value for every \(r\), and the prefactor \(c_r\) is uniformly bounded. The absence of a double logarithm here is therefore a proved mechanism difference, not a rephrasing of the flooding formula.

## Verification
The accompanying standard-library program `verify_voter_clique.py` constructs an independent forward birth-death voter generator using the number of negative peripheral sites and checks its exact rational resolvent against the coalescent product transform for \(r=1,\dots,10\) and four nonzero Laplace arguments. It also checks characteristic polynomials, mean hitting times and pole residues, with 155 exact rational checks. It deliberately does not treat finite calculations as proof of the uniform all-size limit, which is established analytically above.

## Relationship to prior work
Holley and Liggett (1975) and Aldous and Fill's discussion of voter/coalescing-walk duality establish the underlying graphical method; that duality is not new. Fudolig and Esguerra (2014) obtain mean consensus times for zealots on a single complete graph, not this full distribution on independent clique petals and not a uniform two-parameter extreme-value limit. Prior exact work on the permanently fixed center of a **star** establishes the \(r=1\) boundary case. Prior clique-bouquet first-passage papers obtain a \(\log\log m\) shift for a different edge-infection process and give a useful physical contrast. The new assertion concerns the full law for all \(m,r\) and a Gumbel approximation uniform in the unrestricted integer petal size, with the exact residue \(2r/(r+1)\). It is not asserted that classical duality, partial fractions, or Gumbel maxima themselves are new.

## Limitations
The model requires exactly one fixed hub, uniform degree-normalized copying, and initially negative nonhub opinions. It is not a general graph theorem, does not cover voter models in which the hub changes opinion, multiple conflicting zealots, or arbitrary initial opinion patterns. The uniform Gumbel conclusion requires the number of petals \(m\to\infty\) but allows any integer petal size. It is possible that an unlocated general spectral extreme-value theorem implies this specialization; no independent historical-priority or correctness audit has been performed.

## References
1. R. A. Holley and T. M. Liggett, *Ergodic theorems for weakly interacting infinite systems and the voter model*, Annals of Probability 3 (1975), 643–663. First reported publication date 1975-08-01. https://doi.org/10.1214/aop/1176996306
2. D. Aldous and J. A. Fill, *Reversible Markov Chains and Random Walks on Graphs*, section 14.3, *Coalescing random walks and the voter model*. https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch14.S3.html
3. M. I. D. Fudolig and J. P. H. Esguerra, *Analytic treatment of consensus achievement in the single-type zealotry voter model*, Physica A 413 (2014), 626–634. https://doi.org/10.1016/j.physa.2014.07.033
4. *Zealot placement changes star-network voter consensus from Gumbel to exponential*, publicly accessible research result. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-zealot-placement-changes-star-network-voter-consensus-from-gumbe--2551722f2bda
5. *Clique-bouquet flooding: a sharp \(\log\log n\) shift and a harmonic source penalty*, publicly accessible research result. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-clique-bouquet-flooding-a-sharp-log-log-n-shift-and-a-harmonic-s--b342e8b97dcd
6. *A uniform double-logarithmic Gumbel law for first-passage flooding on clique bouquets*, publicly accessible research result. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-uniform-double-logarithmic-gumbel-law-for-first-passage-floodi--b38bb38e62e1
