# A sharp four-frame time arrow for a one-defect molecular-motor ring

## Finding
A four-state biased Markov motor, observed only as a binary indication of which *half* of its ring it occupies, has a complete and unexpectedly selective time-reversal signature. It can carry nonzero microscopic circulation while its entire binary path law is reversible. When time reversal is visible, exactly four equally spaced observations suffice, and their total-variation asymmetry admits a sharp joint optimum.

For any \(0<s\leq1\), \(p,q\geq0\), and \(0<u=p+q<1\), let \(X_k\in\{0,1,2,3\}\) be the stationary Markov chain on the cyclic four-state ring, with clockwise step probability \(c_i p\), counterclockwise step probability \(c_i q\), and stay probability \(1-c_i(p+q)\) from state \(i\), where \(c_0=s\) and \(c_1=c_2=c_3=1\). Observe only \(Y_k=0\) at states \(0,1\) and \(Y_k=1\) at states \(2,3\). Every observation time is an integer step.

Write \(\mathcal L_4\) for the law of \((Y_0,Y_1,Y_2,Y_3)\) and \(\mathcal L_4^{\leftarrow}\) for the law of its reversed tuple. Then
\[
\boxed{\|\mathcal L_4-\mathcal L_4^{\leftarrow}\|_{\mathrm{TV}}=\frac{4pqs|p-q|(1-s)}{1+3s}.}
\]
The **full stationary binary process** is reversible if and only if \(pq(p-q)(1-s)=0\). Its microscopic stationary clockwise edge current is \(J=s(p-q)/(1+3s)\), so the observable four-frame asymmetry is exactly \(4pq(1-s)|J|\). In particular, a homogeneous ring \((s=1)\) or an entirely one-way ring \((pq=0)\) can have nonzero hidden current while remaining *completely* time-reversible under this binary observation.

At every prescribed hopping activity \(0<u<1\), the exact best achievable four-frame total variation over \(0<s\leq1\) and \(p,q\geq0\) with \(p+q=u\) is
\[
\boxed{\max\|\mathcal L_4-\mathcal L_4^{\leftarrow}\|_{\mathrm{TV}}=\frac{2u^3}{27\sqrt3}.}
\]
Its only maximizers (interchanging clockwise and counterclockwise directions) are \(s=1/3\) and \(p,q=u(1\pm1/\sqrt3)/2\). Equivalently, the optimal nonzero directional rate ratio is \(2+\sqrt3\) or its reciprocal.

These are sharp minimal observation counts: all stationary binary processes have reversible blocks of lengths at most three (known general no-go theorem), and every deterministic binary observation of an irreducible Markov chain with at most three hidden states has a reversible full path law. This four-state motor realizes the first possible finite-state exception.

## Assumptions and scope
The latent chain has four states and precisely the transition probabilities specified above. The stay probability at every site is positive because \(0<p+q<1\), including at the slowed site. The stationary law is unique, and no hidden dwell times, directed hops, or finer state labels are observed. The observable \(Y_k\) is a deterministic state labeling; time reversal reverses the sequence without changing its binary labels. The result concerns discrete-time trajectories at consecutive integer steps, not a continuous-time generator sampled at arbitrary lags or transition-detection experiments. The contrast parameter satisfies \(0<s\leq1\); no claim is made for faster-than-baseline defects. For one-way motion \(p=0\) or \(q=0\), the chain remains irreducible because the ring can be traversed in one direction.

## Proof
**Stationarity and microscopic circulation.** Balance across every edge follows from \(\pi_i c_i=s/(1+3s)\), giving the normalized stationary row vector
\[
\pi=\frac{(1,s,s,s)}{1+3s}.
\]
The net clockwise flux across every edge is therefore
\[
J=\pi_iP_{i,i+1}-\pi_{i+1}P_{i+1,i}=\frac{s(p-q)}{1+3s}.
\]
For \(p,q>0\), the microscopic stationary entropy production per step is \(4J\log(p/q)\), which is positive whenever \(p\ne q\).

**The entire four-frame law.** Put \(E_0=\operatorname{diag}(1,1,0,0)\), \(E_1=\operatorname{diag}(0,0,1,1)\), and let \({\bf1}\) be the all-ones column. For every word \(w=(w_0,w_1,w_2,w_3)\in\{0,1\}^4\), its exact probability is
\[
P_Y(w)=\pi E_{w_0}P E_{w_1}P E_{w_2}P E_{w_3}{\bf1}.
\]
Define \(\delta=pqs(p-q)(1-s)/(1+3s)\). Direct multiplication, without approximation, gives the following six reversal-pair discrepancies \(P_Y(w)-P_Y(w^{\mathrm{rev}})\):

| Word / reversed word | Discrepancy |
|---|---:|
| `0001` / `1000` | \(0\) |
| `0010` / `0100` | \(\delta\) |
| `0011` / `1100` | \(-\delta\) |
| `0101` / `1010` | \(\delta\) |
| `0111` / `1110` | \(0\) |
| `1011` / `1101` | \(\delta\) |

The other four words are palindromes. Each nonpalindromic pair contributes its absolute discrepancy to the total-variation distance; exactly four pairs contribute. Therefore \(\|\mathcal L_4-\mathcal L_4^{\leftarrow}\|_{\mathrm{TV}}=4|\delta|\). The standalone checker independently expands all 16 word probabilities from rational path enumerations.

**Reversibility on every zero surface.** If \(p=q\), the microscopic stationary chain obeys detailed balance. If \(s=1\), its stationary time reversal exchanges \(p\) and \(q\); the reflection \(i\mapsto1-i\pmod4\) makes precisely that exchange while preserving the two observable sets \(\{0,1\}\) and \(\{2,3\}\). Thus its observed full path law is invariant under reversal, even for \(p\ne q\). If \(pq=0\), the particle proceeds in a single cyclic direction with site-dependent geometrically distributed holding times. Successive binary \(0\)- and \(1\)-runs are independent, alternately repeated renewal blocks: each run comprises two independent geometric residence times and has a distribution depending only on its binary label. Their stationary alternating-renewal law is invariant under time reversal, since reversing any doubly infinite sequence of independent alternating run lengths leaves its law unchanged, including the length-biased stationary run containing the observation origin. Conversely, if none of these conditions holds, \(\delta\ne0\) is a finite-dimensional witness, so the binary process is not reversible.

**Minimality.** Every binary deterministic labeling of a Markov chain with at most three states has either a constant observable or one label class consisting of a single state. In the latter case, successive visits to that singleton regenerate the chain. Its singleton holding times are geometric, and its excursions through the complementary observed class have independent and identically distributed durations, independent of the holding times. The resulting stationary alternating-renewal binary process is reversible by the argument above. Thus a four-state chain is the smallest possible hidden Markov state space that can yield irreversible binary observations. Stationarity also forces equality of reversal-pair probabilities for binary words of lengths one, two, or three: the two nonpalindromic three-letter pairs have equal frequencies by the adjacent two-letter marginal balance. Consequently the four-frame witness is minimal in frame count as well.

**Exact optimum.** Under \(p+q=u\), put \(d=|p-q|\in[0,u]\). The four-frame total variation factors as
\[
\frac{s(1-s)}{1+3s}(u^2-d^2)d.
\]
The derivative of its defect factor equals \((1-2s-3s^2)/(1+3s)^2\), which is positive before \(s=1/3\) and negative after it. The bias factor derivative is \(u^2-3d^2\), which changes sign once at \(d=u/\sqrt3\). Both endpoints of either factor have zero signal, so these two unique interior extrema are the global maxima, yielding the stated value and the two directional maximizers.

## Verification
Run `python check.py` with Python 3.10 or later and SymPy (tested with version 1.13). The code constructs the exact transition matrix and stationary law, expands all six nonpalindromic word pairs symbolically, checks the edge flux and optimization derivatives, and separately enumerates the \(4^4\) microscopic paths for each word using exact `fractions.Fraction` arithmetic at 46 rational parameter triples. It also checks the exact test \(p=3/8\), \(q=1/8\), \(s=1/3\), for which the four-frame total variation is \(1/192\). These computations verify finite identities and spot-check the algebra. The infinite-word reversibility statements and parameter-global maxima follow from the explicit arguments above, not finite sampling.

## Relationship to prior work
Arola-Fernández and Lacasa establish the universal three-frame no-go theorem for binary time-reversal detection and explain how four-symbol reversal pairs first become informative. That theorem is used here rather than asserted as novel. Harunari et al. prove full entropy-production inference from *resolved visible transitions* on unicyclic Markov networks; their observation retains a directed edge event, unlike this binary sampled state readout. Ertel and Seifert analyze entropy bounds from blurred transitions and their waiting times, also a different observation channel. These works motivate exact coarse-resolution inference but do not state the present four-state occupancy-readout factorization or its sharp joint optimization. A related published homogeneous-ring classification establishes invisible binary circulation on rings of up to five states, but excludes nonuniform departure rates; the site defect here changes the model class and permits a four-state witness. Broader hidden-Markov path formulas can in principle reproduce the result by specialization, so claim of first publication would require independent priority review.

## Limitations
The four-frame metric is a *population* total-variation distance, not a finite-sample detection power, a direct measurement of entropy production, or a continuous-time theorem. Maximization holds at fixed single-step total hopping probability, not at fixed entropy production or laboratory energy cost. The renewal argument for unidirectional motion requires a stationary finite-state chain. All signs and optima are exact for the stated four-state nearest-neighbor model, not universal for arbitrary heterogeneous networks or noisy sensors. Mathematical novelty relative to all unpublished or unsurfaced literature is not certified, and independent validation has not occurred.

## References
1. L. Arola-Fernández and L. Lacasa, *Irreversibility of symbolic time series: a cautionary tale*, first arXiv submission 2023-03-21, https://arxiv.org/abs/2303.11868.
2. P. E. Harunari, A. Dutta, M. Polettini and É. Roldán, *What to learn from a few visible transitions' statistics?*, arXiv:2203.07427 (first submitted 2022-03-14); *Physical Review X* 12, 041026 (2022), https://arxiv.org/abs/2203.07427.
3. B. Ertel and U. Seifert, *An estimator of entropy production for partially accessible Markov networks based on the observation of blurred transitions*, arXiv:2312.08246 (first submitted 2023-12-13), https://arxiv.org/abs/2312.08246.
4. J. Degünther, J. van der Meer and U. Seifert, *Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility*, *Physical Review Research* 6, 023175 (2024), https://doi.org/10.1103/PhysRevResearch.6.023175.
