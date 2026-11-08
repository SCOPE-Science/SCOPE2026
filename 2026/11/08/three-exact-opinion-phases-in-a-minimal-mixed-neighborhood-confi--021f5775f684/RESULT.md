# Three exact opinion phases in a minimal mixed neighborhood-confidence network

## Finding

**Theorem (oscillation, random polarization, and complete freezing).** Fix any homogeneous confidence bound \(0<\varepsilon\le1/4\). On the static three-vertex path, run the asynchronous neighborhood Deffuant–Weisbuch (NDW) rule of Krishnagopal and Porter, with one edge chosen independently and uniformly at each step, compromise strength \(\rho=1/2\), no rewiring, and initial opinion vector \((0,1/2,1)\). Let \(\sigma\in[0,1]\) be the weight of direct, rather than neighborhood-mediated, opinion similarity, and let \(H_t\) denote the center opinion after \(t\) edge selections. The leaf opinions remain \(0\) and \(1\) forever, and the following three regimes are exact:

1. **Persistent oscillation:** for \(0\le\sigma\le\varepsilon\), the law of \(H_t\) is uniform on the \(2^t\) dyadic midpoints \(\{(2k+1)/2^{t+1}:0\le k<2^t\}\). Almost surely \(\liminf_{t\to\infty}H_t=0\) and \(\limsup_{t\to\infty}H_t=1\); the laws converge weakly to uniform Lebesgue measure on \([0,1]\).
2. **Random polarization:** for \(\varepsilon<\sigma<2\varepsilon\), there is an almost surely finite time after which the center accepts influence from at most one leaf; its opinion thereafter converges almost surely to \(0\) or \(1\), each with probability \(1/2\).
3. **Complete freezing:** for \(2\varepsilon\le\sigma\le1\), no agent ever changes opinion: \(H_t=1/2\) for all \(t\).

In every regime \(\mathbb E H_t=1/2\). The exact limiting variance is the discontinuous, nonmonotone step function
\[
\lim_{t\to\infty}\operatorname{Var}(H_t)=
\begin{cases}
1/12,&0\le\sigma\le\varepsilon,\\
1/4,&\varepsilon<\sigma<2\varepsilon,\\
0,&2\varepsilon\le\sigma\le1.
\end{cases}
\]
Consequently both thresholds, including their equality conventions, are sharp throughout the natural confidence range \(0<\varepsilon\le1/4\).

For example, at \(\varepsilon=1/5\), the two transitions occur at \(\sigma=1/5\) and \(\sigma=2/5\). At \(\sigma=3/10\), the first edge selection commits the center to one side, and for every integer \(t\ge1\) its variance is exactly
\[
\operatorname{Var}(H_t)=\frac14-\frac14\left(\frac34\right)^{t-1}+\frac1{16}\left(\frac58\right)^{t-1}.
\]

## Assumptions and scope

The graph consists of two leaves \(L,R\) adjacent only to a center \(H\), with node opinions in \([0,1]\). For a selected directed incidence \(i\leftarrow j\) (an undirected edge is selected, but each endpoint independently tests receptiveness), denote the mean of the *full open neighborhood* of \(j\) by \(\overline x_{N(j)}\), including the opinion of \(i\). The direction-specific NDW update is
\[
x_i^+=x_i+\frac12(x_j-x_i)\,\mathbf1\left\{\sigma|x_i-x_j|+(1-\sigma)|x_i-\overline x_{N(j)}|<\varepsilon\right\}.
\]
Both endpoints use the **pre-update** profile for the single selected edge. There is exactly one uniformly selected edge per discrete time; selections are independent. The analysis applies to the fixed-topology, no-rewiring version of the model, with homogeneous confidence and the strict inequality prescribed by the defining rule. It is not a claim for arbitrary starting opinions, higher-order network adaptation, or other update frequencies.

## Proof

**1. Exact receptiveness geometry.** Write the current profile as \((0,h,1)\). If the center is selected with leaf \(0\), the center assesses the neighbor mean of that leaf, which equals \(h\). Its score is exactly \(\sigma h\). When selected with leaf \(1\), its score is \(\sigma(1-h)\). In contrast, each leaf tests the mean of the center's neighborhood, which equals \(1/2\). The score for leaf \(0\) is \(\sigma h+(1-\sigma)/2\), and for leaf \(1\) it is \(\sigma(1-h)+(1-\sigma)/2\).

If \(\sigma<2\varepsilon\), then \(\sigma<2\varepsilon\le1-2\varepsilon\), so \((1-\sigma)/2>\varepsilon\) (with non-strict inequality sufficient at the limiting boundary). Thus both leaves are unresponsive for all \(h\in[0,1]\). If \(\sigma\ge2\varepsilon\) and the starting profile is \((0,1/2,1)\), both center scores are \(\sigma/2\ge\varepsilon\), while both leaf scores equal \(1/2>\varepsilon\). Therefore that initial profile is absorbing. This proves the third regime and shows in the first two regimes that the leaves remain exactly fixed. The hub then satisfies the scalar random iteration
\[
H_{t+1}=H_t+\frac12(Z_t-H_t)\,\mathbf1\{\sigma|H_t-Z_t|<\varepsilon\},
\qquad \mathbb P(Z_t=0)=\mathbb P(Z_t=1)=1/2,
\]
with independent \(Z_t\), and \(H_0=1/2\).

**2. Oscillatory phase and full finite-time law.** If \(\sigma\le\varepsilon\), both influence tests pass for every center opinion strictly between \(0\) and \(1\), because \(\sigma h<\varepsilon\) and \(\sigma(1-h)<\varepsilon\). Starting at \(1/2\), the center remains in this open interval at every finite time. The recursion becomes \(H_{t+1}=(H_t+Z_t)/2\), so its law at time \(t\) is uniform on the stated dyadic midpoints. In particular,
\[
\mathbb E H_t=\frac12,\qquad
\operatorname{Var}(H_t)=\frac{1-4^{-t}}{12}.
\]
The mesh tends to zero, proving weak convergence to the uniform distribution. For each positive integer \(m\), a block of \(m\) successive selections of leaf \(0\) forces the center below \(2^{-m}\), and an analogous block of selections of leaf \(1\) forces it above \(1-2^{-m}\). Independent nonoverlapping blocks of either type occur infinitely often almost surely. Taking the countable intersection over \(m\) proves the asserted liminf and limsup, not merely nonconvergence in distribution.

**3. Polarizing phase and finite commitment.** Let \(\varepsilon<\sigma<2\varepsilon\) and write \(r=\varepsilon/\sigma\in(1/2,1)\). Leaf \(0\) influences the center if and only if \(h<r\); leaf \(1\) influences it if and only if \(h>1-r\). Within the open overlap interval \(I=(1-r,r)\) both directions are active. At and below its left endpoint only leaf \(0\) is active, and at and above its right endpoint only leaf \(1\) is active. Once outside \(I\), the center cannot return to \(I\) because each subsequently accepted move is toward the corresponding endpoint.

Choose a positive integer \(m\) for which \(2^{-m}<1-r\). From any state in \(I\), \(m\) successive selections of leaf \(0\) move the center below \(1-r\), unless it has already exited \(I\); the analogous run of leaf \(1\) moves it above \(r\). Each disjoint block of \(m\) edge selections has probability \(2^{1-m}\) of being constant, independently of previous blocks. If \(T\) is the first exit time from \(I\), then
\[
\mathbb P(T>jm)\le(1-2^{1-m})^j\quad\text{for integers }j\ge0.
\]
Thus \(T<\infty\) almost surely. Following exit, the only receptive leaf is selected infinitely often almost surely, so repeated halving of the distance to its opinion proves \(H_t\to0\) or \(H_t\to1\). Interchanging the two leaf labels maps the process to its reflection \(h\mapsto1-h\) and preserves the initial center \(1/2\), implying the two probabilities are each \(1/2\). The same reflection symmetry at each finite time gives \(\mathbb E H_t=1/2\). Bounded convergence gives the limiting variance \(1/4\).

**4. Complete freezing and equality cases.** At \(\sigma=2\varepsilon\), the center's score is exactly its confidence threshold, so the strict inequality blocks both updates. At \(\sigma=\varepsilon\), the center remains strictly between the two extremes for every finite time, and therefore its two strict inequalities still hold. These conventions establish the claimed locations and inclusions of both transitions. For \(\sigma\ge2\varepsilon\), step 1 proves complete freezing.

**5. Explicit intermediate variance.** For \(\varepsilon=1/5\) and \(\sigma=3/10\), the first edge selection makes \(H_1=1/4\) or \(3/4\) with equal probabilities. From the first outcome, all further selected right-leaf edges are rejected, while each selected left-leaf edge halves \(H_t\). With \(N\) binomial with parameters \((t-1,1/2)\), the two equally likely branches have respective opinions \(2^{-2-N}\) and \(1-2^{-2-N}\). Using \(\mathbb E(2^{-N})=(3/4)^{t-1}\) and \(\mathbb E(4^{-N})=(5/8)^{t-1}\) yields the stated exact finite-time variance.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic (Python standard library only). It independently implements both direction-specific endpoint tests, exhaustively branches on all \(2^9\) edge sequences at seven representative dyadic-weight values, and checks leaf invariance, both sharp boundary conventions, the complete dyadic distribution, finite-time variance identities, and an immediate-commitment example. Running `python3 verify.py` prints `VERIFY_OK`. The argument above, rather than the finite-depth computation, proves all almost-sure and limiting statements.

## Relationship to prior work

Krishnagopal and Porter introduced the NDW model with neighborhood-tuning parameter \(\sigma\) and simulated network-based opinion behavior. Their original February 2024 preprint introduces the directional-receptiveness concept, and their subsequent version explicitly displays separate direction-specific update indicators. This theorem treats a fixed three-vertex graph and resolves the entire parameter interval \(\sigma\in[0,1]\) at a fixed small confidence threshold. In particular, it exhibits two sharp switches and a nonmonotone limiting variance that are not established by the cited numerical study.

The purely neighborhood-based special case \(\sigma=0\) already has a Bernoulli-affine description, and Bernoulli affine recurrences themselves are standard; neither is claimed as a new mechanism in isolation. The distinct contribution is the complete mixed-weight phase classification, including the intermediate almost-sure polarization phase and the second threshold at which all updates cease. Zhang, Hong, and Hu (2017) studied fluctuations in another nonlocal bounded-confidence model with explicitly stubborn agents. Their abstract states a confidence-threshold criterion, but the available material does not identify their model with the endogenous, direction-specific NDW gate used here. Full-text comparison with that work remains a publication-priority limitation.

## Limitations

The analysis fixes the graph to the minimal two-edge path, uses exactly one random interaction per step, common confidence and full compromise strength \(1/2\), and fixes the symmetric initial profile. The result does not assert analogous transitions on arbitrary networks, under rewiring, or for arbitrary initial opinions. In the intermediate phase the orientation is fixed after finite random time, but the opinion only approaches its limiting endpoint asymptotically. The full 2017 nonlocal-aggregation article was not available for comparison; equivalent results beyond the material inspected remain possible.

## References

1. S. Krishnagopal and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Neighborhood Effects*, arXiv:2402.05368v1, publicly submitted 2024-02-08; see also arXiv:2402.05368v2, especially the explicitly direction-specific Eq. (3). https://arxiv.org/abs/2402.05368
2. J. Zhang, Y. Hong, and X. Hu, *Multiagent Opinion Dynamics of Bounded Confidence with Nonlocal Aggregative Interaction*, SIAM Journal on Control and Optimization **55** (2017), 2543–2573, DOI:10.1137/16M1083268. https://doi.org/10.1137/16M1083268
3. C. Bernardo, C. Altafini, A. Proskurnikov, and F. Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica **159** (2024), 111302, DOI:10.1016/j.automatica.2023.111302. https://doi.org/10.1016/j.automatica.2023.111302
4. W. Chu and M. A. Porter, *Bounded-confidence opinion models with random-time interactions*, arXiv:2409.15148v1, publicly submitted 2024-09-23. https://arxiv.org/abs/2409.15148
