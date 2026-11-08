# Exact hub advantage and fixation law for context-dependent voting on stars

## Finding

**Theorem.** Consider asynchronous, binary, context-dependent opinion adoption on the star with one hub and \(m\geq1\) leaves. Let \(\alpha_{01},\alpha_{10}\in(0,1]\) be, respectively, the acceptance probabilities for a transition from opinion \(0\) to opinion \(1\), and from opinion \(1\) to opinion \(0\), after sampling a neighbor of the opposite opinion. Put
\[
r=\frac{\alpha_{01}}{\alpha_{10}},\qquad q_m=\frac{mr+1}{r(m+r)},\qquad Z_m=q_m^m+\frac rm\sum_{j=1}^m q_m^j.
\]
If the initial hub has opinion \(0\) and exactly \(k\) leaves have opinion \(1\), write \(F_k\) for the probability of eventual all-\(1\) consensus. If the hub has opinion \(1\), write \(G_k\). Then for **every** \(0\le k\le m\),
\[
\boxed{F_k=\frac{r}{mZ_m}\sum_{j=1}^k q_m^j,\qquad
G_k=F_k+\frac{q_m^k}{Z_m}.}
\]
For a fixed seed budget \(1\le k\le m\), placing one of the \(k\) initial opinion-\(1\) agents at the hub is strictly better than placing all \(k\) on leaves whenever \(m>1\):
\[
\boxed{G_{k-1}-F_k=\frac{q_m^{k-1}}{Z_m}\frac{m^2-1}{m(m+r)}>0.}
\]
For a **single** initially positive agent, hub and leaf fixation probabilities obey the exact ratio
\[
\boxed{\frac{G_0}{F_1}=\frac{m(m+r)}{mr+1}.}
\]
At fixed \(r>0\), define \(c=r^{-1}-r\) and
\[
\Phi(r)=\left(e^c+r\int_0^1 e^{ct}\,dt\right)^{-1}.
\]
Then \(G_0\to\Phi(r)>0\), whereas \(mF_1\to r\Phi(r)\), as \(m\to\infty\). More generally, whenever \(k/m\to\theta\in[0,1]\),
\[
F_k\longrightarrow r\Phi(r)\int_0^\theta e^{ct}\,dt,\quad
G_k\longrightarrow \Phi(r)\left(e^{c\theta}+r\int_0^\theta e^{ct}\,dt\right).
\]
All expressions include the unbiased case \(r=1\), where \(F_k=k/(2m)\) and \(G_k=1/2+k/(2m)\).

## Assumptions and scope

The contact graph is the finite, simple, undirected star with one hub and \(m\) distinct leaves. Each agent activates at rate one in continuous time, independently samples a uniformly random neighbor, and, if that neighbor has the opposite opinion, copies it with probability \(\alpha_{01}\) or \(\alpha_{10}\) according to the direction of the proposed change; otherwise the state is unchanged. Equivalently, select one agent uniformly at each discrete update and apply the same rule: fixation probabilities are identical because the nontrivial state-transition rates differ by a common factor. The acceptance probabilities are fixed, strictly positive, and do not depend on vertices, time, or the numbers of adopters. The definition of \(F_k\) and \(G_k\) uses the number of positive leaves, **not** the total number of positive agents. All leaf subsets of a given size are equivalent by graph symmetry.

## Proof

**Absorption and uniqueness.** The configurations of unanimous opinion \(0\) and unanimous opinion \(1\) are absorbing. From every other configuration, a finite sequence of legal, positive-rate copying moves reaches either unanimous configuration; for example, convert the hub as needed and then each disagreeing leaf. Consequently the finite Markov chain has no other closed communicating class and reaches consensus almost surely. Its all-\(1\) hitting probability is the unique function harmonic for the generator on nonabsorbing states with boundary values \(F_0=0\) and \(G_m=1\).

**Two recurrences.** If the hub holds \(0\), each of the \(k\) positive leaves can become negative at rate \(\alpha_{10}\); the hub becomes positive at rate \(\alpha_{01}k/m\). Cancelling the positive factor \(k\) in the generator equation yields, for \(1\le k\le m\),
\[
F_k-F_{k-1}=\frac rm(G_k-F_k).
\]
If the hub holds \(1\), each of the \(m-k\) negative leaves becomes positive at rate \(\alpha_{01}\); the hub becomes negative at rate \(\alpha_{10}(m-k)/m\). For \(0\le k<m\),
\[
G_{k+1}-G_k=\frac{1}{rm}(G_k-F_k).
\]
The boundary equations at \(k=m\) in the first recurrence and at \(k=0\) in the second are included: their denominators are nonzero under the stated assumptions.

**Geometric difference.** Put \(D_k=G_k-F_k\). Combine the two recurrences at successive indices:
\[
\left(1+\frac rm\right)D_{k+1}
=\left(1+\frac{1}{rm}\right)D_k,
\qquad 0\le k<m.
\]
Thus \(D_k=q_m^kD_0\), where \(q_m=(mr+1)/(r(m+r))>0\). As \(F_0=0\), summing the first recurrence gives \(F_k=(r/m)D_0\sum_{j=1}^k q_m^j\). The second boundary condition \(G_m=F_m+D_m=1\) forces \(D_0=1/Z_m\), proving the all-state formula. Positivity of \(Z_m\) also makes the expression well defined even when \(q_m=1\).

**Best position and single-seed ratio.** With \(k\) initially positive agents, the two inequivalent placements are \((\text{hub}=1,k-1)\) and \((\text{hub}=0,k)\). The recurrence gives
\[
G_{k-1}-F_k=D_{k-1}-\frac rmD_k
=\frac{q_m^{k-1}}{Z_m}\left(1-\frac rm q_m\right)
=\frac{q_m^{k-1}}{Z_m}\frac{m^2-1}{m(m+r)}.
\]
This is positive for \(m>1\), and zero for \(m=1\). For a single positive agent, \(G_0=1/Z_m\), while \(F_1=rq_m/(mZ_m)\), giving the asserted exact ratio.

**Large-star limit.** At fixed \(r>0\), direct algebra gives
\[
q_m=1+\frac{r^{-1}-r}{m+r}=1+\frac{c}{m}+O(m^{-2}).
\]
Consequently \(q_m^{\lfloor m t\rfloor}\to e^{ct}\), uniformly for \(t\in[0,1]\), and ordinary Riemann sums imply
\[
\frac1m\sum_{j=1}^{\lfloor m\theta\rfloor}q_m^j
\longrightarrow\int_0^\theta e^{ct}\,dt.
\]
Therefore \(Z_m\to e^c+r\int_0^1e^{ct}dt>0\), which gives all claimed limits; the formula for \(mF_1\) follows because \(q_m\to1\). At \(r=1\), \(q_m=1\) exactly and \(Z_m=2\), yielding the explicitly stated neutral formulas. No other parameter scaling is claimed.

## Verification

The standalone `verify.py` uses exact `fractions.Fraction` arithmetic to construct the full \(2^{m+1}\)-state continuous-time Markov generator for stars with \(1\le m\le6\), eliminates the two absorbing states, solves the resulting rational Dirichlet system by an independent dense Gaussian-elimination routine, and checks every nonabsorbing state's probability against the formula. It separately tests strict hub placement for each budget when \(m>1\) and both absorbing boundaries. Four rational acceptance-rate pairs are tested for each size, producing \(1092\) checked equalities/inequalities. Run from the extracted package with `python verify.py`. These finite tests are corroboration, not the proof for arbitrary \(m\); the proof above covers all stated positive parameters and sizes.

For illustration, \(m=4\) and \(r=2\) give \(G_0=512/687\), \(F_1=64/229\), and hub-to-leaf ratio \(8/3\).

## Relationship to prior work

Becchetti, Bonifaci, Cruciani, and Pasquale (2023) define precisely the context-dependent adoption model and prove exact biased fixation probabilities on **regular** graphs (their Theorem 3 and Appendix F); their nonregular general-topology problem is explicitly identified as difficult. Stars with \(m>1\) are nonregular, and their regular-graph formula does not give the two-state star law here. Czaplicka, Charalambous, Toral, and San Miguel (2022) study bias in copying on complete and random graphs, but not this exact finite-star law. Durocher, Karras, Pavlogiannis, and Tkadlec (2022) study a different *fitness-normalized neighbor-choice* death–birth voter process, whereas the present process samples a neighbor **uniformly**, followed by a direction-dependent accept/reject step. Similarly, the star Moran birth–death/death–birth formulas of de Souza and Neves (2020) concern fitness-dependent reproduction/death draws rather than the stated uniform-neighbor-and-acceptance process. Their formulas cannot be substituted without a demonstrated transition-kernel equivalence, which is absent in the compared material.

## Limitations

The result applies to undirected stars and fixed positive acceptance probabilities, not arbitrary nonregular graphs, time-dependent preferences, synchronous parallel updating, or multiple opinions. It determines fixation **probabilities**, not exact absorption-time distributions or conditional fixation times. The infinite-leaf limits hold with the acceptance ratio \(r\) held fixed, and do not address bias varying with graph size. No independent external audit or definitive global publication-priority certificate has been obtained.

## References

- L. Becchetti, V. Bonifaci, E. Cruciani, F. Pasquale, *On a Voter Model with Context-Dependent Opinion Adoption* (first public preprint 2023-05-12), https://arxiv.org/abs/2305.07377 ; complete manuscript https://arxiv.org/html/2305.07377v2 .
- A. Czaplicka, C. Charalambous, R. Toral, M. San Miguel, *Biased-voter model: how persuasive a small group can be?* (2022), https://arxiv.org/abs/2203.05376 .
- L. Durocher, P. Karras, A. Pavlogiannis, J. Tkadlec, *Invasion Dynamics in the Biased Voter Process* (2022), https://arxiv.org/abs/2201.08207 .
- E. P. de Souza, A. G. M. Neves, *Exact fixation probabilities for the Birth-Death and Death-Birth frequency-dependent Moran processes on the star graph* (2020), https://arxiv.org/abs/2003.05462 .
