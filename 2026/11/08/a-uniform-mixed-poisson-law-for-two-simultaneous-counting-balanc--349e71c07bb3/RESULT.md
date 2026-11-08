# A uniform mixed-Poisson law for two simultaneous counting balances on dense random digraphs

## Finding

Let \(G_n\) be a loopless directed random graph on \([n]\), with every off-diagonal arc independently present with probability \(1/2\). At every vertex independently sample the truth values of four unary predicates \(p,q,r,s\), each fair. Fix root \(o=1\). In the counting modal language, the operator \(\#\chi\) counts out-neighbors satisfying \(\chi\), and equality abbreviates two opposite integer counting comparisons. Define
\[
\theta=(\#p=\#q)\wedge(\#r=\#s),\qquad
\Phi_t=(\#\theta\ge t),\qquad Z_n=\#\theta\text{ at }o.
\]
**Theorem.** As \(n\to\infty\),
\[
Z_n\ \xrightarrow{\mathrm d}\ Z,\qquad
Z\mid\Lambda\sim\operatorname{Poisson}(\Lambda),\qquad
\Lambda\sim\operatorname{Uniform}\left(0,\frac2\pi\right).
\]
Consequently, for each fixed integer \(j\ge0\), with \(a=2/\pi\),
\[
\lim_{n\to\infty}\Pr(Z_n=j)=\frac1a\int_0^a e^{-\lambda}\frac{\lambda^j}{j!}\,d\lambda
=\frac1a\left(1-e^{-a}\sum_{h=0}^{j}\frac{a^h}{h!}\right),
\]
and, in particular,
\[
\lim_{n\to\infty}\Pr(G_n,o\models\Phi_1)
=1-\frac{1-e^{-a}}a
=1-\frac\pi2\left(1-e^{-2/\pi}\right).
\]
Furthermore, for each fixed positive integer \(k\), the factorial moments converge:
\[
\lim_{n\to\infty}\mathbb E(Z_n)_k=\frac{a^k}{k+1}.
\]
Thus \(\mathbb EZ=1/\pi\) and \(\operatorname{Var}(Z)=1/\pi+1/(3\pi^2)\), larger than the mean: this is a genuine non-Poisson limit. The root formula \(\Phi_1\) has modal depth two.

## Assumptions and scope

For each \(n\), the sample space consists of all \(n(n-1)\) ordered off-diagonal arc bits and all \(4n\) independent unary truth bits, each independent and fair; no conditions are imposed on the root's unary bits. The root is fixed rather than sampled and all limits refer to labelled structures. The two inner balancing tests use disjoint *pairs* of unary letters; a vertex is allowed to satisfy both. No claim is made for sparse edges, undirected edges, or logical formulas other than the specified fixed formula family.

## Proof

**1. Condition on the colors.** Put
\[
d_w=(\mathbf1_{p(w)}-\mathbf1_{q(w)},\ \mathbf1_{r(w)}-\mathbf1_{s(w)})\in\{-1,0,1\}^2,
\qquad M_n=\sum_{w=1}^{n}d_w.
\]
The vectors \(d_w\) are independent and identically distributed, have mean zero, and satisfy
\(\mathbb E(d_wd_w^\top)=\frac12 I_2\). The two coordinates are independent. Consequently,
\[
M_n/\sqrt n\ \xrightarrow{\mathrm d}\ G,
\qquad G\sim N_2(0,\tfrac12 I_2).
\]
Conditional on all the \(d_w\), each outgoing arc row remains independently fair. For each \(v\ne o\), let \(Q_{n,v}\) be the probability, conditional on the colors, that \(v\models\theta\). With \(A_{vw}\) the arc indicators, this is
\[
Q_{n,v}=\Pr\left(\sum_{w\ne v}A_{vw}d_w=(0,0)\ \middle|\ (d_w)_{w=1}^n\right).
\]
The conditional mean of this sum is \(m_{n,v}=\frac12\sum_{w\ne v}d_w\) and its covariance is \(V_{n,v}=\frac14\sum_{w\ne v}d_wd_w^\top\). The weak law of large numbers and boundedness of \(d_v\) imply uniformly in \(v\) that \(V_{n,v}/n\to\frac18 I_2\) in probability and \(m_{n,v}=M_n/2+O(1)\).

**2. Uniform conditional lattice local limit.** The Fourier inversion formula for the integer-lattice sum is
\[
Q_{n,v}=\frac1{(2\pi)^2}\int_{[-\pi,\pi]^2}
\prod_{w\ne v}\frac{1+e^{i\langle t,d_w\rangle}}2\,dt.
\]
For each \(d\in\{(1,0),(0,1)\}\), the probability that \(d_w=d\) is \(1/8\). Hence, with probability tending to one exponentially fast, each of these two coordinate-basis types occurs at least \(n/16\) times. After omission of one vertex they still occur with positive linear frequency. The factors associated with them bound the modulus of the characteristic function by
\(\lvert\cos(t_1/2)\cos(t_2/2)\rvert^{c n}\) for a fixed \(c>0\). On the entire fundamental square this has a unique modulus-one point at \(t=0\), so there is no hidden periodic lattice coset or second saddle. Outside an \(n^{-2/5}\)-neighborhood of the origin its Fourier integral is \(o(n^{-1})\), uniformly in \(v\).

Inside that neighborhood, for bounded \(d\),
\[
\log\frac{1+e^{i\langle t,d\rangle}}2
=\frac i2\langle t,d\rangle-\frac18\langle t,d\rangle^2
+O(\|t\|^4).
\]
The total remainder is \(O(n\|t\|^4)=o(1)\). Rescaling \(t\) by \(n^{-1/2}\) gives the normal local-density integral and establishes, uniformly over all \(v\ne o\) on color configurations with \(\|M_n\|/\sqrt n\) bounded and empirical second moment near its limit,
\[
Q_{n,v}=\frac{1}{2\pi\sqrt{\det V_{n,v}}}
\exp\!\left(-\tfrac12 m_{n,v}^{\top}V_{n,v}^{-1}m_{n,v}\right)
+o(n^{-1})
=\frac4{\pi n}\exp\left(-\frac{\|M_n\|^2}{n}\right)+o(n^{-1}).
\]
The bound above also yields \(Q_{n,v}\le C/n\) uniformly in \(v\) on the exponentially likely basis-type event, without any condition on \(M_n\). By tightness of \(M_n/\sqrt n\), the uniform asymptotic is valid in probability.

**3. Independent rows give conditional rare events.** For each \(v\ne o\), the event \(A_{ov}=1\) uses the root's outgoing row, whereas \(v\models\theta\) uses outgoing row \(v\). Since all directed arcs are independent and distinct ordered rows have disjoint arc variables, the events \(\{A_{ov}=1, v\models\theta\}\) are conditionally independent across \(v\ne o\). Conditional on all colors they are Bernoulli with success probabilities \(b_{n,v}=Q_{n,v}/2\). Hence \(Z_n\) is conditionally Poisson-binomial, with conditional intensity
\[
\lambda_n=\sum_{v\ne o}b_{n,v}
=\frac2\pi\exp\left(-\frac{\|M_n\|^2}{n}\right)+o_{\Pr}(1).
\]
Moreover, the usual elementary coupling/Le Cam inequality bounds the conditional total variation distance to \(\operatorname{Poisson}(\lambda_n)\) by \(2\sum_{v\ne o}b_{n,v}^2=o_{\Pr}(1)\), since the basis-type event implies all \(b_{n,v}=O(n^{-1})\). Bounded convergence removes the conditioning.

**4. Identify the environment distribution.** If \(G=(G_1,G_2)\sim N_2(0,\frac12 I_2)\), then \(\|G\|^2\) is exponential with mean one: for \(t\ge0\), \(\mathbb Ee^{-t\|G\|^2}=1/(1+t)\). Therefore \(U=e^{-\|G\|^2}\) is uniform on \([0,1]\). Slutsky's theorem and continuity of Poisson probabilities in their parameter give \(\lambda_n\Rightarrow(2/\pi)U\) and the asserted mixed-Poisson convergence. Integrating over the uniform intensity yields the displayed mass and threshold formulas.

**5. Factorial moments.** For fixed \(k\), conditional independence gives
\(\mathbb E[(Z_n)_k\mid(d_w)]=k!\sum_{v_1<\cdots<v_k}\prod_{i=1}^kb_{n,v_i}\).
On the exponentially likely basis-type event, every \(b_{n,v}\le C/(2n)\), so these conditional factorial moments are uniformly bounded and converge in probability to \(\lambda_n^k\). The complement has probability \(e^{-\Omega(n)}\), while \((Z_n)_k\le n^k\), so it contributes \(o(1)\). Hence
\[
\lim_{n\to\infty}\mathbb E(Z_n)_k
=\mathbb E\Lambda^k=\frac{(2/\pi)^k}{k+1}.
\]
In particular, the limit variance is the sum of \(\mathbb E\Lambda\) and \(\operatorname{Var}\Lambda=(2/\pi)^2/12\), as stated. This completes the proof.

## Verification

The standalone `checker.py` uses exact rational arithmetic and enumerates the nine possible two-dimensional color-difference types, weighted by their true multiplicities. It independently evaluates every root-exclusion probability and the first two factorial moments for \(n=2,3,4\), then directly enumerates all directed arc assignments for \(n=3\) to check the first method. The independent outdegree conditioning identity
\[
\mathbb EZ_n=\frac{n-1}{2}\mathbb E\left[\left(4^{-K}\binom{2K}{K}\right)^2\right],
\qquad K\sim\operatorname{Bin}(n-1,1/2),
\]
is verified at the finite tested sizes and numerically at \(n=300\). These checks corroborate the normalization but do not replace the local-limit theorem or the infinite Poisson-mixture argument. Run using `python checker.py` (Python 3 standard library only).

## Relationship to prior work

Ghosh and Schwarzentruber (2026, arXiv:2610.26187v1) define the counting modal formalism, compute elementary pointed-graph proportions, and analyze convergence on uniformly branching trees; their Section 7 explicitly identifies extension to general graphs as future work. Their tree experiment has independent descendant subtrees. In contrast, the present uniform labelled dense-digraph model has shared color counts \(M_n\) across vertices, giving a random intensity and a non-Poisson mixture. Classical central and local limit results, Poisson-binomial approximation, and the Gaussian-to-exponential transformation are acknowledged as ingredients, not claimed new in isolation. Adam-Day, Benedikt, Ceylan and Finkelshtein (2024) establish asymptotic constancy for GNNs with mean aggregation; their aggregate-elimination result does not supply a limit for these exact unnormalized integer-count equalities. Tousinejad and Koponen (2026, arXiv:2606.23715) analyze first-order convergence in colored digraphs generated by a Markov logic network, with one unary predicate and a different language; the particular two-pair counting-modal root law is not a specialization of the first-order results shown there. Earlier independent-tree Poisson computations do not imply a deterministic intensity here.

## Limitations

The theorem treats exactly one explicit depth-two family, four independent fair unary predicates, directed independent arcs of probability one-half and a fixed root. The global-color conditioning would need modification for undirected graphs (opposite rows share edge variables), correlated colors, and biased or sparse ensembles. It does not prove full convergence for all formulas of counting modal logic, nor does a search establish historical priority. Independent mathematical verification has not been performed.

## References

1. A. Ghosh and F. Schwarzentruber, *On Counting Graphs for Modal Logic with Counting*, arXiv:2610.26187v1 (first public October 19, 2026), https://arxiv.org/abs/2610.26187.
2. S. Adam-Day, M. Benedikt, İ. İ. Ceylan, B. Finkelshtein, *Almost Surely Asymptotically Constant Graph Neural Networks*, arXiv:2403.03880 (2024), https://arxiv.org/abs/2403.03880.
3. Y. Tousinejad and V. Koponen, *Random coloured digraphs defined by a Markov logic network*, arXiv:2606.23715 (2026), https://arxiv.org/abs/2606.23715.
4. M. Cordonnier, N. Keriven, N. Tremblay and S. Vaiter, *Convergence of Message-Passing Graph Neural Networks with Generic Aggregation on Large Random Graphs*, JMLR 25(406):1–49 (2024), https://jmlr.org/papers/v25/23-0965.html.
