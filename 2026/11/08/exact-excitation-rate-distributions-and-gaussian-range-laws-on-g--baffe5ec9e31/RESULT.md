# Exact excitation-rate distributions and Gaussian range laws on generalized theta graphs

## Finding

Let \(r\ge3\), and let \(\ell_1,\ldots,\ell_r\ge2\) be integers. Form the simple connected graph \(\Theta(\ell_1,\ldots,\ell_r)\) from two distinguished vertices joined by \(r\) internally vertex-disjoint paths, the \(i\)-th with \(\ell_i\) edges. Its number of vertices is \(V=2+\sum_i(\ell_i-1)\).

For each initial three-coloring, run separately either synchronous three-color cyclic cellular automaton (CCA), or synchronous three-state Greenberg–Hastings excitation (GHM). Let \(\alpha_{\mathrm C}\) denote the limiting per-vertex frequency of color advances under CCA, and \(\alpha_{\mathrm G}\) the frequency of resting-to-excited transitions under GHM. For the **same initial coloring**, the exact identity is
\[
\alpha_{\mathrm C}=3\alpha_{\mathrm G}.
\]

Define the trinomial coefficients
\[
 A_m(t)=[z^t](z^{-1}+1+z)^m,\qquad A_m(t)=0\quad\text{for }|t|>m.
\]
For every nonnegative rational \(a\), the number of initial colorings with \(\alpha_{\mathrm C}=a\) (equivalently, \(\alpha_{\mathrm G}=a/3\)) is **exactly**
\[
 N_{\boldsymbol\ell}(a)=3\!\sum_{\substack{t_i\in\mathbb Z,\ |t_i|\le\ell_i\\ t_1\equiv\cdots\equiv t_r\pmod3\\
 \max_{i<j}\frac{|t_i-t_j|}{\ell_i+\ell_j}=a}}
 \prod_{i=1}^{r}A_{\ell_i}(t_i).
\]
The sum is zero if its conditions have no solutions. The coefficients sum to \(3^V\), so this is the **complete labelled initial-configuration activity distribution**, not a temporal primitive-cycle count.

In particular the number of colorings that eventually synchronize is
\[
 E_{\boldsymbol\ell}=N_{\boldsymbol\ell}(0)
 =3\sum_{t\in\mathbb Z}\prod_{i=1}^{r}A_{\ell_i}(t).
\]
Both models have the same synchronization subset, not merely the same number of synchronizing states.

For equal paths \(\ell_1=\cdots=\ell_r=n\ge2\), **every** rate
\[
 \alpha_{\mathrm C}=\frac{3k}{2n},\qquad
 \alpha_{\mathrm G}=\frac{k}{2n},\qquad
 0\le k\le\left\lfloor\frac{2n}{3}\right\rfloor
\]
occurs, and there are no other rates. A one-dimensional finite-sum formula computes its exact population: put \(w_c(j)=A_n(3j+c)\) and \(W_c(p,q)=\sum_{j=p}^{q}w_c(j)\), with \(W_c(p,q)=0\) if \(p>q\). The population at index \(k\) is
\[
 3\sum_{c=0}^{2}\sum_{m\in\mathbb Z}\left[
 W_c(m,m+k)^r-W_c(m+1,m+k)^r
 -W_c(m,m+k-1)^r+W_c(m+1,m+k-1)^r\right].
\]
Only finitely many terms are nonzero. This gives a polynomial-time arithmetic computation without enumerating \(3^V\) configurations.

For fixed \(r\) and path lengths \(\ell_i=\ell_i(n)\) satisfying \(\ell_i/n\to\lambda_i\in(0,\infty)\), uniformly random initial colors have the **sharp synchronization law**
\[
 \Pr(\alpha_{\mathrm C}=0)=\Pr(\alpha_{\mathrm G}=0)
 \sim \frac{(27/(4\pi))^{(r-1)/2}}
 {\sqrt{\sum_i\lambda_i^{-1}}\,\prod_i\sqrt{\lambda_i}}
 n^{-(r-1)/2}.
\]
Writing \(Z_1,\ldots,Z_r\) for independent standard normal random variables, their rescaled activity converges in distribution:
\[
 \sqrt n\,\alpha_{\mathrm C}\ \Longrightarrow\
 \sqrt{\frac23}\max_{i<j}
 \frac{|\sqrt{\lambda_i}Z_i-\sqrt{\lambda_j}Z_j|}{\lambda_i+\lambda_j},
 \qquad \sqrt n\,\alpha_{\mathrm G}=\tfrac13\sqrt n\,\alpha_{\mathrm C}.
\]
For equal lengths the first limiting variable is \((\max_i Z_i-\min_i Z_i)/\sqrt6\), and the synchronization probability is asymptotic to \((27/(4\pi))^{(r-1)/2}/\sqrt r\) times \(n^{-(r-1)/2}\).

## Assumptions and scope

Every graph vertex has one of the colors \(0,1,2\). In CCA a vertex advances by one modulo three iff it has a neighbor in its successor color, otherwise it holds. In GHM a vertex in color \(1\) or \(2\) advances unconditionally, while a color-\(0\) vertex advances iff a neighbor is in color \(1\). Updates are synchronous. The activity of CCA counts all advances; the activity of GHM counts only \(0\to1\) transitions. Random-coloring statements use the product-uniform measure on the \(3^V\) labelled initial states. The limiting activity exists because the graph is finite, and its relation to cycle integrals is the established general theorem of Gravner, Lyu and Sivakoff (2018, Theorem 3). This result concerns activity rates and synchronization populations, not a census of primitive temporal periods or first-entry times.

## Proof

**1. Established circulation theorem and the local coboundary identity.** For adjacent colors \(a,b\in\{0,1,2\}\), the CCA edge increment \(d_{\mathrm C}(a,b)\) is the representative of \(b-a\pmod3\) in \(\{-1,0,1\}\). The GHM increment \(d_{\mathrm G}(a,b)\) is \(1\) for \((a,b)=(0,1)\), \(-1\) for \((1,0)\), and zero otherwise. Put \(h(0)=0\), \(h(1)=-2\), \(h(2)=-1\). Checking all nine ordered pairs gives
\[
 d_{\mathrm C}(a,b)=3d_{\mathrm G}(a,b)+h(b)-h(a).
\]
The potential difference telescopes around each closed walk, so each CCA cycle integral is three times the corresponding GHM integral. By the cited general theorem, each activity is the maximum signed cycle integral divided by its cycle length, and fixation occurs exactly when all cycle integrals vanish. It follows that the two activities differ by factor three and their synchronization subsets coincide. Neither this general criterion nor this elementary coboundary relation is claimed as an independently new general-graph theorem.

**2. Paths and exact populations.** Orient every path from one distinguished endpoint \(u\) to the other \(v\). Let \(t_i\) be the sum of CCA increments along path \(i\). Every increment is one of \(-1,0,1\), and its choice uniquely determines the next vertex color from the current color. Hence, for a fixed color at \(u\), the number of increment sequences with sum \(t_i\) is \(A_{\ell_i}(t_i)\). A common terminal color at \(v\) exists iff all \(t_i\) are congruent modulo three. Exactly three choices remain for the initial color at \(u\). Every simple cycle in this graph consists of one path traversed forward and another backward, so its integral is \(t_i-t_j\) and its length is \(\ell_i+\ell_j\). Every closed walk decomposes into simple cycles; its mean integral cannot exceed the maximum simple-cycle mean. Substituting into the general activity theorem proves the rate formula and its multiplicities. All integrals vanish exactly when all \(t_i\) are equal, giving the extinction/synchronization formula.

**3. Equal lengths and the fast census.** With every length equal to \(n\), the maximum ratio is \((\max_i t_i-\min_i t_i)/(2n)\). A common residue forces the range to be a multiple of three. It is at most \(2n\), so the listed indices are exhaustive. For every permitted \(k\), choose two sums \(-n\) and \(-n+3k\), with the remaining sums equal to the first; each is attainable by a sequence of \(n\) increments. Thus every rate occurs. To count vectors with minimum \(m\) and maximum \(m+k\), take the number of all path sums in that closed interval, subtract the choices missing the lower endpoint and those missing the upper endpoint, and restore those missing both. The displayed inclusion–exclusion formula follows.

**4. Exact large-length behavior.** Let \(p_m(t)=A_m(t)/3^m\). It is the distribution of a sum of \(m\) independent uniform \(\{-1,0,1\}\) variables, each of variance \(2/3\). Direct cancellation of the total-state powers gives
\[
 \Pr(\alpha=0)=3^{r-1}\sum_{t\in\mathbb Z}\prod_i p_{\ell_i}(t).
\]
Fourier inversion with one-step characteristic function \((1+2\cos\theta)/3=1-\theta^2/3+O(\theta^4)\) yields the lattice local central limit approximation
\[
 p_{\ell_i}(t)=\sqrt{\frac{3}{4\pi\ell_i}}
 \exp\left(-\frac{3t^2}{4\ell_i}\right)+o(n^{-1/2})
\]
uniformly on bounded \(t/\sqrt n\) ranges when \(\ell_i/n\to\lambda_i>0\). Gaussian tail bounds and the uniform bound \(\sup_t p_{\ell_i}(t)=O(n^{-1/2})\) control the complementary ranges. The resulting Riemann sum evaluates exactly to the displayed synchronization constant.

For the activity limit, select a common terminal-color difference modulo three uniformly; independently choose the first \(\ell_i-1\) increments of each path uniformly, then choose each last increment uniquely to meet that residue. This samples the initial colorings uniformly after choosing the root color, and each last increment is bounded by one. The multivariate central limit theorem therefore gives independent limits \(t_i/\sqrt n\Longrightarrow\sqrt{2\lambda_i/3}\,Z_i\). Continuity of the finite maximum of normalized pairwise differences proves the asserted Gaussian-range law.

## Verification

Two independent finite computations accompany this statement. `exact_coefficients.py` performs exact trinomial recursion, a full residue-conditioned sum, and the equal-arm minimum/maximum inclusion–exclusion count. `direct_trajectories.py` instead enumerates all initial states, constructs the functional graph of each update rule, peels its transient trees, and measures the excitation frequency along every remaining directed cycle. `replay_checks.py` compares both computations without numerical tolerance. All three are standalone Python standard-library programs with outputs supplied alongside them. Full initial-state checks include nine path-length tuples, with \(243\) through \(177147\) labelled configurations per model. They agree in every tested activity class and verify the factor-three relation. Large-length numerical checks illustrate, but do not replace, the proved limiting law.

## Relationship to prior work

Gravner, Lyu and Sivakoff (2018, Theorem 3 and equations (2.2)–(2.8)) already prove the general finite-graph circulation criterion and maximum-cycle-mean activity identity for both models; those foundations are expressly prior results. The present claim is the closed exact **initial-configuration distribution** for all multi-theta path lengths, its one-dimensional equal-arm census, and its explicit Gaussian-range and rare-synchronization asymptotics. Durrett and Griffeath (1993) develop the foundational excitable-media models and large-lattice phase behavior, not these finite-network enumerations. Searches for the same exact probability formulas, path-sum aliases, Gaussian range laws, and earlier generalized-theta activity tables found no covering statement in the inspected material. This is a qualified literature comparison, not proof of absolute historical priority.

## Limitations

No primitive temporal orbit counts, first-entry-time classifications, mixing claims, or infinite-graph activity claims are asserted. The general graph-activity theorem is used as a previously published premise, not reproved from first principles. Numerical experiments verify only the stated finite samples, while the general claims follow from the mathematical proof. Published or unindexed equivalent formulae may exist beyond the inspected primary material; independent external validation has not been performed.

## References

1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, Annals of Applied Probability **28** (2018), 3324–3357, DOI: 10.1214/17-AAP1350; first public preprint arXiv:1610.07320 (2016-10-24). Author-hosted full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, Experimental Mathematics **2** (1993), 183–208, DOI: 10.1080/10586458.1993.10504277; arXiv:patt-sol/9303002 (first public preprint 1993-03-22). Author-hosted full text: https://sites.math.duke.edu/~rtd/reprints/paper79.pdf .
3. M. Müller-Linow, C. Marr and M.-T. Hütt, *Topology regulates the distribution pattern of excitations in excitable dynamics on graphs*, Physical Review E **74** (2006), 016112, DOI: 10.1103/PhysRevE.74.016112 (contextual network-activity study; abstract examined).
