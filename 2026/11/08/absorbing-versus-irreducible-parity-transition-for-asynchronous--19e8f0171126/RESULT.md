# Absorbing-versus-irreducible parity transition for asynchronous minority on \(C_n^2\)

## Finding
For every integer \(n\ge5\), let \(C_n^2\) be the simple labelled graph with vertices \(\mathbb Z/n\mathbb Z\), adjacent at cyclic distances one or two. In discrete time, independently choose one vertex uniformly, update it to the minority bit in its **closed** five-site neighborhood, and retain its old bit in a tie. A recurrent class means a closed communicating class of this finite Markov chain. Let \(R_n\) be the number of recurrent states and \(K_n\) the number of recurrent classes.

**Theorem.** Every initial binary configuration reaches a maximum cut of \(C_n^2\) almost surely. The set of all maximum cuts is *exactly* the union of the recurrent classes, with
\[
R_n=\begin{cases}
4,&n\equiv0\pmod4,\\
 n(n^2+23)/12,&n\equiv1\pmod4,\\
 n^2/2,&n\equiv2\pmod4,\\
2n,&n\equiv3\pmod4,
\end{cases}
\qquad
K_n=\begin{cases}4,&4\mid n,\\1,&4\nmid n.\end{cases}
\]
If \(4\mid n\), the four recurrent states are individually absorbing. Otherwise, all maximum-cut configurations form one irreducible nonabsorbing class, with the uniform stationary law. The exact maximum cut size is \(n+k_n\), where \(k_n\) is the largest integer \(k\le\lfloor n/2\rfloor\) such that \(k\equiv n\pmod2\).

The striking feature is the absence of nonoptimal recurrent traps for **every** circumference, with a sharp reversal between four frozen states and a single mobile recurrent family as the circumference leaves the zero residue class.

## Assumptions and scope
The graph is simple, undirected and labelled; the bound \(n\ge5\) ensures four distinct neighbors per site. The random choice is independent and uniform at each integer time. A selected spin flips if at least two of its four *other* neighbors agree with its current spin; this follows from minority voting in a five-site closed neighborhood. Thus all legal flips leave the number of cut edges unchanged or increase it. Both states of a cut (a binary configuration and its bitwise complement) are counted separately. No rate or mixing-time bound is asserted.

## Proof
**1. Bond coordinates and energy.** For any spin word \(x=(x_i)\), define \(z_i=\mathbf1_{\{x_i=x_{i+1}\}}\), indices modulo \(n\). The parity condition \(\sum_i z_i\equiv n\pmod2\) is necessary and sufficient for a bond word to lift to a cyclic spin word; each admissible bond word has exactly two complementary lifts. Put \(Z=\sum_i z_i\) and \(J=\sum_i z_i z_{i+1}\). The number \(C(x)\) of disagreeing edges of the squared cycle is
\[
C(x)=(n-Z)+\sum_i(z_i\mathbin{\oplus}z_{i+1})=n+Z-2J.
\]
Flipping vertex \(i\) complements \(z_{i-1},z_i\). Writing its local bond block as \((a,b,c,d)=(z_{i-2},z_{i-1},z_i,z_{i+1})\), direct subtraction gives
\[
\Delta C=4ab-2a+4cd-2d.
\]
The selected spin flips under the stated minority rule exactly when \(\Delta C\ge0\). The strict inequality gives an improvement, while equality gives a reversible move. In particular, flipping a pair of adjacent particles \((b,c)=(1,1)\) erases them and changes the cut by \(2a+2d\ge0\).

**2. Global reachability.** Repeatedly erase adjacent bond particles until no two ones are adjacent. Every such operation is an allowed move. The resulting independent bond word has \(k\) particles, with \(k\equiv n\pmod2\), and cut size exactly \(n+k\). Let \(k_n\) be the largest feasible such \(k\). It follows immediately that no cut exceeds \(n+k_n\), and isolated-particle words with \(k_n\) particles attain equality.

If the resulting independent word has \(k<k_n\), its particles can be slid by reversible updates: a particle moves to an adjacent empty bond position precisely when that position's other neighbor is empty. Such moves connect all size-\(k\) independent sets of a cycle whenever \(k<n/2\). This can be seen by recording the positive vacancy gaps between successive particles: moving a particle transfers one vacancy between neighboring gaps, and these transfers connect every positive composition, while a packed block can be translated around the ring.

Use these slides to pack the particles at positions \(0,2,\ldots,2k-2\). This leaves \(n-2k+1\ge5\) consecutive empty bond sites whenever \(k\le k_n-2\). Inside five empty sites the two legal updates
\[
00000\ \longrightarrow\ 01100\ \longrightarrow\ 01010
\]
first preserve and then increase the cut by two, adding two isolated particles. Iterate until \(k=k_n\). Thus from **every** configuration a finite positive-probability update sequence reaches a maximum cut. Since the state space is finite, no nonmaximum closed class exists, and the chain hits the maximum-cut set almost surely.

**3. Classification of maximum cuts.** For a nonconstant bond word with \(r\) circular runs of ones, \(J=Z-r\) and hence \(C=n+2r-Z\). At equality \(C=n+k_n\), the inequalities \(r\le Z\) and \(r\le n-Z\) yield
\[
k_n\le r\le\left\lfloor\frac{n+k_n}{3}\right\rfloor.
\]
For residues \(0,2,3\pmod4\), the two bounds force \(r=k_n\), \(Z=k_n\): exactly the independent \(k_n\)-sets occur. In residue \(1\pmod4\), either this case occurs or \(r=k_n+1\), \(Z=k_n+2\), which is one adjacent pair of ones together with isolated ones and single zero separators. There are exactly \(n\) cyclic words of the latter type. The number of independent size-\(k\) sets on a labelled cycle is \(\frac{n}{n-k}\binom{n-k}{k}\). Multiplying by the two spin lifts yields the stated four-residue formula for \(R_n\), including the additional \(2n\) states for residue one.

**4. Number of communicating classes.** A neutral update is reversible. If \(4\mid n\), maximal bond words alternate strictly and none admits a neutral flip. Their two bond patterns yield four absorbing spin configurations.

Otherwise, \(k_n<n/2\), and the independent size-\(k_n\) bond words are connected by neutral hard-core particle slides. The two spin lifts also connect. For odd \(n\), \(k_n\) is odd: translate the packed independent particle block one site at a time, moving particles from right to left at each translation, for a full \(n\) translations. Each spin vertex is updated exactly \(k_n\) times, yielding the complementary spin word. For \(n\equiv2\pmod4\), put \(k=k_n\), so \(n=2k+2\). Starting with particles at \(0,2,\ldots,2k-2\), slide the last one two steps to \(2k\), then all the others two steps in decreasing position order, and finally move the last one two steps through \(2k+1\) to \(0\). This closed bond walk updates **every spin exactly once**, again reaching the complementary lift. The remaining maximum-cut words in residue one, which have one adjacent pair, are reversibly connected to an independent maximum-cut word by erasing that pair. Hence all maximum-cut states form one communicating class when \(4\nmid n\).

Uniform site selection and reversibility of every neutral flip make transitions within that class symmetric, giving its unique uniform stationary distribution.

## Verification
The standalone programs `check_transition_graph.py`, `check_bond_identity.py`, and `check_monodromy.py` are included. Run each with Python 3, without third-party packages. The first enumerates all \(131040\) spin states for lengths \(5\) through \(16\), checks the exact maximum-cut counts, verifies all-state reverse reachability of the maximum-cut set, and tests its communicating-class structure. The second checks the sixteen local four-bond identities and enumerates all \(131056\) parity-admissible bond words for lengths \(5\) through \(17\). The third constructs and verifies explicit complementing neutral update loops for every non-four-divisible length from \(5\) to \(25\). Recorded outputs are supplied alongside the scripts. These checks are finite corroborations; the all-length result follows from the constructive proof.

## Relationship to prior work
Rouquier, Regnault and Thierry's *Stochastic Minority on Graphs*, arXiv:1011.5119v1 (2010), defines the precise closed-neighborhood asynchronous rule and proves its cut-energy monotonicity (Section 3); it analyzes cliques and ordinary degree-two cycles and paths (Section 4.1). Its general energy lemma is used here, but it does not itself imply either maximum-cut reachability on the four-regular squared cycles or the residue-class communicating-class census.

Dhar, Shastry and Dasgupta, arXiv:cond-mat/0004207v1 (2000), study the one-dimensional axial next-nearest-neighbor Ising chain at the *different* coupling ratio \(J_1=2J_2\), and use conservative two-spin Kawasaki dynamics rather than the single-spin zero-temperature flips here. Pini and Rettori, arXiv:0707.1953v1 (2007), investigate finite-temperature Glauber response using an approximate closure; the exact finite-ring recurrent-class statement is not implied by their stated results. The particle representation, symmetric transition argument and standard independent-set enumeration are not claimed to be new individually.

## Limitations
The theorem covers exactly the equal-weight distance-one and distance-two cycle, at zero temperature, with a *self-inclusive*, single-site minority rule. It does not claim mixing rates, hitting-time estimates, external perturbation stability, or a corresponding result for all range-two interaction strengths. Historical priority is not absolutely certified: the most relevant 2010 and 2000 articles were inspected in their pertinent mathematical sections, but not every historical finite-volume zero-temperature study could be examined in full. Independent external validation has not been performed.

## References
- J.-B. Rouquier, D. Regnault, E. Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119v1, first public arXiv version November 23, 2010, https://arxiv.org/abs/1011.5119.
- A. Dhar, B. S. Shastry, C. Dasgupta, *Equilibrium and dynamical properties of the ANNNI chain at the multiphase point*, arXiv:cond-mat/0004207v1, April 13, 2000, https://arxiv.org/abs/cond-mat/0004207.
- M. G. Pini, A. Rettori, *Effect of antiferromagnetic exchange interactions on the Glauber dynamics of one-dimensional Ising models*, arXiv:0707.1953v1, July 13, 2007, https://arxiv.org/abs/0707.1953.
