# Sharp half-filling current bound for asymmetric exclusion on branched rings

## Finding

**Theorem.** Let a periodic backbone have \(L\ge3\) sites, and attach any finite family of rooted trees with a total of \(M\ge0\) off-backbone sites. Suppose \(L+M=2N\) and exactly \(N\) indistinguishable exclusion particles are present. Backbone transitions occur clockwise at rate \(h_f\) and anticlockwise at rate \(h_b\), where \(h_f>h_b\ge0\). On tree \(i\), outward and inward nearest-neighbour transitions have positive constant rates \(h_{t,i}\) and \(h_{r,i}\), and their ratio is \(q_i=h_{t,i}/h_{r,i}>0\).

If **all** tree ratios satisfy \(q_i\ge1\), or **all** satisfy \(q_i\le1\), the stationary current across every backbone bond satisfies
\[
0<J\le (h_f-h_b)\frac{N}{2(2N-1)}.
\]
Equality holds exactly when **at most one** off-backbone vertex has nonunit stationary activity \(q_i^{d_i(v)}\). Thus, for any branch system with at least two nonneutral off-backbone vertices, the inequality is strict. In particular, for homogeneous \(q_i=q\neq1\) and \(M\ge2\), the unbiased \(q=1\) choice is the unique current maximizer within the common-ratio family.

The common-side condition is sharp: for a four-site backbone with two depth-one trees at different backbone roots, activities \(2\) and \(1/2\), and three particles, the normalized current is \(J/(h_f-h_b)=7/23\), exceeding the unbiased \(3/10\) by \(1/230\).

## Assumptions and scope

Each tree root is a backbone vertex, which carries unit stationary activity. A tree site \(v\) at positive depth \(d_i(v)\) carries activity \(a_v=q_i^{d_i(v)}\). Branches may differ in size, position and topology; rates need only be homogeneous along each tree's edges in the outward/inward sense. The finite graph is connected through the ring. Currents are stationary mean signed flows, not current fluctuations. The theorem is finite-volume and requires exactly half of **all** sites occupied, not half of backbone sites.

More generally the bound holds for any factorized canonical stationary measure having unit activity on all backbone sites and all remaining site activities on the same side of one. This broader formulation is used in the proof but is not claimed to hold for networks lacking that stationary measure.

## Proof

**1. Stationarity and bond current.** For a configuration \(\eta\in\{0,1\}^{L+M}\) with \(\sum_v\eta_v=N\), define \(w(\eta)=\prod_{v\text{ off backbone}}a_v^{\eta_v}\). The normalized canonical measure \(w(\eta)/Z_N\) is stationary. Indeed, each tree edge separately satisfies detailed balance, since outward occupation increments depth by one and multiplies the weight by \(q_i=h_{t,i}/h_{r,i}\). On the backbone, every configuration of a ring has the same number of \(10\) and \(01\) adjacent pairs; their weighted incoming/outgoing imbalance cancels because backbone moves do not change \(w\). Positivity of the tree rates and \(h_f>0\) gives irreducibility for \(0<N<L+M\). Thus this stationary measure is unique.

Every backbone site has activity one, so \(\Pr(10)=\Pr(01)\) on any ordered adjacent backbone pair, even if the attached trees vary by site. Consequently \(J=(h_f-h_b)\Pr(10)\).

**2. Exact coefficient representation.** Put \(m=N-1\). Remove two adjacent backbone sites, leaving \(2m\) sites with activities \(z_1,\ldots,z_{2m}\). Write \(E_k=e_k(z_1,\ldots,z_{2m})\) for elementary symmetric functions, with \(e_k=0\) outside its natural degree range. The normalizing coefficient is \(Z_N=E_{m-1}+2E_m+E_{m+1}\), and exactly one chosen orientation of the pair has numerator \(E_m\). Therefore
\[
\frac{J}{h_f-h_b}
=\frac{E_m}{E_{m-1}+2E_m+E_{m+1}}. \tag{1}
\]
At unit activities, this equals \(J_0/(h_f-h_b)=(m+1)/(2(2m+1))\).

**3. A coefficientwise positive strict deficit.** First assume \(z_j\ge1\) and set \(t_j=z_j-1\ge0\). Put \(T_k=e_k(t_1,\ldots,t_{2m})\). By selecting the \(t\)-dependent terms in the elementary symmetric polynomial,
\[
E_k=\sum_{r=0}^k {2m-r\choose k-r}T_r.
\]
A direct binomial-coefficient calculation gives the **exact identity**
\[
\begin{split}
D_m&:=(m+1)(E_{m-1}+E_{m+1})-2mE_m\\
&=\sum_{r=2}^{m}
\frac{r(r-1)}{m+1-r}
{2m-r\choose m-r}T_r
+(m+1)T_{m+1}. \tag{2}
\end{split}
\]
The sum is empty if \(m=1\). For \(2\le r\le m\), the coefficient in (2) follows by simplifying \((m+1)[{2m-r\choose m-1-r}+{2m-r\choose m+1-r}]-2m{2m-r\choose m-r}\); the endpoint coefficient at \(r=m+1\) is \(m+1\). Every coefficient on the right is strictly positive, and its first nonzero term occurs at order two. In particular \(D_m\ge0\), with equality precisely if at most one \(t_j\) is positive. Substituting (2) into (1) yields the **exact positive current deficit**
\[
\frac{J_0-J}{h_f-h_b}
=\frac{D_m}
{2(2m+1)(E_{m-1}+2E_m+E_{m+1})}. \tag{3}
\]
This establishes both the sharp upper bound and its equality condition.

**4. Activities below one.** If all \(0<z_j\le1\), complement the occupations on all \(2N\) sites. The half-filling condition preserves particle number, while the canonical weight transforms, up to a configuration-independent factor, to the product of the inverse activities. Complementation interchanges \(10\) and \(01\) on the chosen backbone bond, and these two events have equal probabilities for the canonical measure. Thus the current is unchanged under simultaneous inversion of all activities. Equation (3) applies to the inverse activities, which are at least one; the same equality criterion follows.

**5. Sharp failure for mixed-sign activities.** Take \(L=4\), \(M=2\), \(N=3\), with two unit-depth leaf trees attached to two distinct ring vertices, and their activities \(2\) and \(1/2\). Directly,
\[
Z_N={4\choose3}+
\left(2+\frac12\right){4\choose2}
+{4\choose1}=23,
\]
and the numerator for a backbone \(10\) pair is
\[
{2\choose2}+
\left(2+\frac12\right){2\choose1}
+{2\choose0}=7.
\]
Hence \(J/(h_f-h_b)=7/23>3/10\). This demonstrates that removing the common-side hypothesis invalidates the universal bound.

## Verification

The included standalone Python program `verify.py` uses integer and rational arithmetic only. It independently verifies the coefficient identity (2) for many rational activities and all \(1\le m\le7\), checks the half-filling current and strictness for path branches and a range of exact rational rate ratios, and checks exact global balance on the full configuration graph for a four-site backbone with an attached two-site path and for two attached leaves with opposing biases. It also verifies the mixed-sign witness exactly.

Run `python verify.py` with Python 3.10 or later. Observed result: `PASS: 334 exact certificate, current, and generator checks`. These finite checks are supporting diagnostics: the all-size theorem is proved by the binomial identity and the canonical balance argument.

## Relationship to prior work

Ishiguro and Ando (2026), arXiv:2603.09694v1, establish the canonical factorized stationary distribution for ASEP with tree branches and derive hypergeometric current expressions for two particular geometries. Ezaki and Nishinari (2012), arXiv:1207.3552, describe a broader class of balanced exclusion networks with factorized steady states. The stationary measure used here is credited to that framework. The new mathematical step is the sharp, **all-tree-shapes, half-total-filling**, common-side upper bound with an exact positive coefficient certificate, rigidity condition and opposing-bias witness. It is not a new formula for the stationary distribution.

## Limitations

No assertion is made for arbitrary mixed-sign activities, other densities, current fluctuations, speed of convergence, or the thermodynamic limit. The example shows mixed signs can reverse the bound, not that every mixed-sign choice does so. The exact stationary measure is essential; models whose backbone rates depend on local occupations beyond simple exclusion are outside scope. The result has not undergone independent mathematical audit. A broader earlier inequality in unindexed canonical-lattice-gas literature remains a priority risk.

## References

- Y. Ishiguro and Y. Ando, *Asymmetric simple exclusion process with tree-like network branches*, arXiv:2603.09694v1 (first posted 2026-03-10), https://arxiv.org/html/2603.09694 .
- T. Ezaki and K. Nishinari, *Balance network of asymmetric simple exclusion process*, arXiv:1207.3552 (first posted 2012-07-13), https://arxiv.org/abs/1207.3552 .
- *Exact steady states in the asymmetric simple exclusion process beyond one dimension*, Phys. Rev. Research **6**, 033030 (2024), https://doi.org/10.1103/PhysRevResearch.6.033030 .
