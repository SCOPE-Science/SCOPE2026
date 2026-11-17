# Exact entrance-time census and logarithmic settling for cyclic majority dynamics

## Finding
Consider the synchronous radius-one binary majority rule (elementary cellular automaton 232) on a labelled cyclic ring of \(n\ge3\) sites. Let \(T(x)\) be the least nonnegative time at which the trajectory beginning at \(x\in\{0,1\}^n\) is periodic. All trajectories other than the two perfectly alternating configurations (which exist only for even \(n\)) eventually become fixed; those two alternating configurations are already in one primitive two-cycle.

For any integer \(t\ge0\), set \(L=2t+1\) and define an integer matrix \(M_L\) indexed by pairs \((k,p)\), with \(0\le k\le L\) and \(p\in\{0,1\}\). The only nonzero directed transitions from \((k,p)\) are \((k,p)\to(0,p)\) with weight one and, if \(k<L\), \((k,p)\to(k+1,1-p)\) with weight one; coincident transitions are counted with multiplicity. The exact number of configurations periodic by time \(t\) is

\[
\boxed{\#\{x:T(x)\le t\}=\operatorname{tr}(M_{2t+1}^{\,n})+2\mathbf 1_{\{2\mid n\}}.}
\]

Thus the number with exact positive first-entry time \(t\) is the difference of the displayed expressions for \(t\) and \(t-1\), while time zero is given directly. The sharp maximum first-entry time and number of maximizing configurations are

\[
\boxed{\max_x T(x)=\left\lfloor\frac{n-1}{2}\right\rfloor,\qquad
\#\{x:T(x)=\lfloor(n-1)/2\rfloor\}=2n.}
\]

For a uniformly random initial configuration, the first-entry time satisfies the sharp logarithmic scale

\[
\boxed{\frac{T(x)}{\log_2 n}\ \xrightarrow[n\to\infty]{\mathbb P}\ \frac12.}
\]

These are one compound entrance-time census theorem: the matrix formula gives every finite-size temporal layer; the extremal and typical-time assertions describe its boundary and asymptotic scales.

## Assumptions and scope
The vertices are \(\mathbb Z/n\mathbb Z\), with three distinct sites in each closed radius-one neighborhood since \(n\ge3\). The map \(F\) is defined by

\[
(Fx)_i=\operatorname{majority}(x_{i-1},x_i,x_{i+1}),\qquad i\in\mathbb Z/n\mathbb Z,
\]

where indices are reduced modulo \(n\). Every update is simultaneous and deterministic. Periodic means \(F^p(y)=y\) for some \(p\ge1\); the first-entry time is \(T(x)=\min\{t\ge0:F^t(x)\text{ is periodic}\}\), so an initially alternating two-cycle has time zero rather than one. All counting is for labelled sites, not binary necklaces.

Define an **equal bond** at edge \(i\) when \(x_i=x_{i+1}\), and a **different bond** otherwise. Write \(b_i(x)=1\) or \(0\), respectively. If at least one equal bond is present, let \(g(x)\) be the maximum length of a cyclic run of consecutive different bonds between equal bonds, counting a zero-length gap when two equal bonds are adjacent. Then the sharper pointwise identity underlying the theorem is

\[
\boxed{T(x)=\left\lfloor\frac{g(x)}2\right\rfloor.}
\]

If no equal bond is present, the configuration is one of the alternating period-two states, so \(T(x)=0\) (this case requires even \(n\)).

## Proof
**1. Local edge dynamics.** A site changes value under three-site majority if and only if it differs from *both* its neighbors. In bond notation this occurs exactly when the two incident bonds are different bonds. Any equal bond is permanent: its two endpoints agree with each other, so neither can change. For a currently different bond \(i\), the left endpoint flips exactly if the preceding bond is different; the right endpoint flips exactly if the following bond is different. Consequently the new bond becomes equal if and only if exactly one of those adjacent bonds is equal. In formulas, with \(b_i\in\{0,1\}\),

\[
 b_i(Fx)=\begin{cases}1,&b_i=1,\\ b_{i-1}\oplus b_{i+1},&b_i=0.\end{cases}
\]

Here \(\oplus\) denotes exclusive OR. Thus between two equal bonds a run of \(g\) different bonds evolves by turning its two end bonds equal when \(g\ge2\); a run of length one stays different because both its endpoints are already supported by equal bonds. A run of length zero stays empty. The simultaneous update therefore replaces the lengths \(g\) of all zero-bond gaps by \(\max\{g-2,0\}\) if \(g\) is even, or by \(\max\{g-2,1\}\) if \(g\) is odd. No new gaps arise elsewhere. A vertex flips precisely when it is incident to two consecutive different bonds. Hence, after exactly \(\lfloor g(x)/2\rfloor\) updates, all zero-bond gaps have length zero or one and no vertex flips. Before this time the longest remaining gap has length at least two, so at least one vertex flips. This proves the pointwise first-entry formula and fixation for any configuration with an equal bond. If all bonds differ, the sites strictly alternate, which is possible only for even \(n\); every site flips every update and these two configurations form one primitive two-cycle.

**2. Parity and matrix count.** Traversing the cycle, each different bond toggles the bit. A cyclic bond word \(b\in\{0,1\}^n\) is therefore compatible with an underlying vertex configuration if and only if it has an even number of zero entries. Each compatible word has exactly two inverse vertex configurations (choose one starting bit). When \(b\) contains at least one one, \(T(x)\le t\) is equivalent to every run of zeros having length at most \(L=2t+1\).

The transfer matrix \(M_L\) keeps two coordinates: \(k\), the length of the current zero-bond run, and \(p\), the parity of the number of zeros already traversed. Writing a one-bond resets \(k\) to zero without changing \(p\); writing a zero-bond increases \(k\) and reverses \(p\), unless doing so exceeds \(L\). Every cyclic bond word containing a one and having zero-runs of length at most \(L\) determines a unique closed sequence of run lengths at its labelled positions. Its parity state closes after \(n\) transitions exactly when its number of zeros is even, and in that case there are precisely two closed parity-state assignments. Hence \(\operatorname{tr}(M_L^n)\) equals twice the number of compatible bond words with at least one one and maximum zero-run at most \(L\), exactly the number of corresponding labelled vertex configurations. The all-zero bond word is never counted by the finite run-length matrix, but for even \(n\) corresponds to the two initially alternating configurations. Adding those two gives the displayed census for every \(n\ge3,t\ge0\). The difference of cumulative counts gives every exact first-entry layer.

**3. Sharp maximum and maximizing count.** If \(n\) is odd, the even-zero parity condition forces an odd number of equal bonds, hence at least one. The longest gap has at most \(n-1\) zeros, and equality is necessary to attain \(\lfloor(n-1)/2\rfloor\). Thus a maximizer has exactly one equal bond, chosen in \(n\) ways; the compatible cyclic vertex word has two choices. If \(n\) is even and there is any equal bond, parity forces an even number of equal bonds, hence at least two. The longest possible zero gap has length \(n-2\); attaining the maximum \((n-2)/2\) forces precisely two adjacent equal bonds. There are \(n\) positions for their adjacent pair and two compatible vertex words for each. The all-different-bond alternating two-cycle has first-entry time zero and does not maximize for \(n\ge4\). Thus the maximum is sharp with exactly \(2n\) maximizers in both parities, including \(n=3\) and \(n=4\).

**4. Typical-time asymptotics.** A uniformly random vertex word induces a uniformly random bond word conditioned on having an even number of zeros, because there are exactly two vertex lifts of every such bond word. An unconditioned random bond word is an i.i.d. fair Bernoulli word. Let \(G_n\) be the maximum length of a cyclic all-zero run, treating the all-zero word separately. For \(k=\lceil(1+\varepsilon)\log_2 n\rceil\), a union bound gives \(\Pr(G_n\ge k)\le n2^{-k}\) without parity conditioning; conditioning costs at most a factor of two. For \(k=\lfloor(1-\varepsilon)\log_2 n\rfloor\), partition the first \(n\) positions into \(\lfloor n/k\rfloor\) disjoint blocks of length \(k\); the probability no block is all zero is at most \(\exp[-\lfloor n/k\rfloor2^{-k}]\), which tends to zero, and the parity condition again costs at most a factor of two. The exceptional all-zero bond word has conditional probability \(2^{1-n}\) when \(n\) is even and zero otherwise. Therefore \(G_n/\log_2 n\to1\) in probability. Using \(T=\lfloor G_n/2\rfloor\) outside that negligible exception proves the logarithmic law.

## Verification
Run the dependency-free script `python3 verify_rule232.py`. It independently simulates the three-input majority rule for all \(2^n\) labelled initial states at each \(3\le n\le18\), calculates first-entry times by checking both one- and two-step returns, independently predicts first entry from the initial bond pattern, and compares the exact transfer-matrix trace with all cumulative first-entry counts at every permissible time. It checks all \(524280\) configurations across those lengths, including the special already-periodic alternating states. The captured output is `verify_rule232.log` and ends with `VERIFY_OK`. The program does not constitute a proof for unbounded \(n\); the preceding four deductions do.

For example, for \(n=10\), the populations in first-entry layers \(t=0,1,2,3,4\) are respectively \(124,590,230,60,20\), totaling \(1024\). Of the 124 initially periodic states, two form one primitive two-cycle.

## Relationship to prior work
The update is the classical elementary cellular automaton Rule 232. Fuks (1997) uses this rule after Rule 184 for density classification and analyzes special preimage families and a uniform time bound; neither the labelled all-initial-state first-entry distribution nor its complete transfer census is stated in the inspected article. Inokuchi and Sato (2000) study threshold rules with *fixed* end boundary conditions, distinct from the periodic ring here. Tosic and Agha (2004), and Tosic (2016), characterize recurrent states and count or estimate fixed-point populations rather than their full temporal preimage layers. Nakar and Ron (2022) give a more general structural classification of fixed and two-periodic configurations for cyclic radius-\(r\) majority dynamics. Their general structural results imply the classification of recurrent types used here, but the full first-entry census, sharp maximizer count, and typical settling-time law are not stated in the inspected material. The mere fact that a trajectory eventually settles, or that fixed points can be counted, does not imply these quantitative initial-time layers. The classical recurrent classification, the local majority rule, and previously known bounded-settling facts are not claimed as new.

## Limitations
The claim applies only to radius one, binary states, synchronous updates and labelled finite periodic rings with \(n\ge3\). It does not extend as stated to fixed-end boundaries, other threshold rules or arbitrary graphs. The empirical checks cover only finite sizes. Novelty is best-knowledge relative to accessible literature and research records, not a guarantee of priority: an unindexed exact first-entry enumeration could exist. The formula's already-periodic \(t=0\) specialization overlaps earlier fixed-state enumeration; originality rests on the *joint all-time* distribution and its extremal and typical-time consequences.

## References
1. H. Fuks, *Solution of the Density Classification Problem with Two Cellular Automata Rules*, arXiv:comp-gas/9703001v1 (March 7, 1997), https://arxiv.org/pdf/comp-gas/9703001 .
2. S. Inokuchi and T. Sato, *On Limit Cycles and Transient Lengths of Cellular Automata with Threshold Rules*, Bulletin of Informatics and Cybernetics 32 (2000), 23–60, https://doi.org/10.5109/13492 .
3. P. T. Tosic and G. A. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI 2004, pp. 861–870, https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf .
4. P. T. Tosic, *On Enumerating Stable Configurations of Cellular Automata with the MAJORITY Update Rule*, 2016 public manuscript, https://www.researchgate.net/publication/310515639_On_Enumerating_Stable_Configurations_of_Cellular_Automata_with_the_MAJORITY_update_rule .
5. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972 (May 18, 2022), https://arxiv.org/pdf/2205.08972 .
