# Exponential false metastability but certain ground-state absorption on triangular Ising books

## Finding
For every integer \(n\ge2\), consider the *triangular book* \(B_n=K_2\vee\overline{K_n}\): two adjacent hub vertices joined to all \(n\) mutually nonadjacent peripheral vertices. In the zero-field antiferromagnetic Ising energy \(H(\sigma)=J\sum_{\{u,v\}\in E(B_n)}\sigma_u\sigma_v\) with \(J>0\) and spins \(\sigma_v\in\{-1,+1\}\), define a weak single-spin minimum by \(\Delta_vH\ge0\) at every vertex and a strict one by \(\Delta_vH>0\) everywhere.

The **only two strict minima** are the two ground states with equal hub spins and all peripheral spins opposite to the hubs, each at energy \(J(1-2n)\). Every other weak minimum has opposite hub spins and peripheral magnetization of magnitude at most one; all such states have excited energy \(-J\), separated from the ground by \(2J(n-1)\). The exact number of weak minima is
\[
W_n=\begin{cases}
2+2\binom{n}{n/2},&n\text{ even},\\
2+4\binom{n}{(n-1)/2},&n\text{ odd}.
\end{cases}
\]
Thus \(W_n=\Theta(2^n/\sqrt n)\), while the number of strict minima is constantly two.

Moreover every excited weak minimum has a path consisting of at most one energy-neutral spin flip followed by a strictly energy-decreasing flip. For continuous-time zero-temperature single-spin Glauber dynamics in which each vertex is selected at positive rate, all energy-decreasing flips are allowed with positive rate, energy-increasing flips are forbidden, and energy-neutral flips are allowed with positive rate, **from every initial configuration the process almost surely reaches one of the two ground states**. Hence the exponentially numerous excited weak minima are not absorbing or closed dynamically metastable classes.

## Assumptions and scope
The vertex set consists of labeled hubs \(a,b\) and \(n\) labeled leaves. Edges comprise \(\{a,b\}\) and the \(2n\) hub–leaf edges only; distinct leaves are never adjacent. The exchange constant is uniform and strictly positive; there is no magnetic field. A weak local minimum is an energy condition, not the same as a state absorbing a dynamics that accepts neutral moves. The dynamics is finite-state, uses single-spin updates, and must give each admissible neutral and downhill flip positive transition intensity; arbitrary positive such rates are allowed. No statement about expected absorption time or synchronous/multispin dynamics is made.

## Proof
Let \(s=\sigma_a\), \(t=\sigma_b\), and \(L=\sum_{i=1}^n\sigma_i\). For any vertex \(v\), flipping its spin changes the energy by
\[\Delta_vH=-2J\sigma_v\sum_{u\sim v}\sigma_u.\]
If \(s=t\), each leaf has local field \(2s\); nonincreasing energy under every potential leaf flip (the weak-minimum requirement \(\Delta_iH\ge0\)) forces every leaf to be \(-s\). The resulting energy is \(J(1-2n)\). Each leaf flip costs \(4J\), and each hub flip costs \(2J(n-1)>0\); both configurations are strict minima.

If \(s=-t\), the leaf field is zero and every leaf flip has zero energy cost. The hub flip costs are precisely \(2J(1-sL)\) and \(2J(1+sL)\). Therefore all flips are nonnegative exactly when \(|L|\le1\). For even \(n\) this means \(L=0\), giving \(2\binom{n}{n/2}\) configurations including both hub orientations. For odd \(n\) it means \(L=\pm1\), giving \(4\binom{n}{(n-1)/2}\). All opposite-hub configurations have \(H=-J\), independent of the leaves, and none can be strict because all leaf flips are neutral. This establishes the exhaustive classification. Every nonweak configuration has a downhill flip by the definition of weak stability. The two aligned-hub weak states are the unique minimum-energy configurations: in the aligned case \(H=J+2JsL\ge J(1-2n)\), while opposite hubs always give \(-J>J(1-2n)\) when \(n\ge2\).

For an excited weak minimum and even \(n\), \(L=0\). Flip any leaf at zero energy cost, changing \(|L|\) to two. The hub antiparallel to the resulting majority has negative flip cost \(2J(1-2)=-2J\). For odd \(n\), \(|L|=1\); the hub whose spin has the sign of \(L\) has zero flip cost. Flip it, aligning both hubs in the sign opposite to \(L\). Since \(n\ge3\) and the original leaves had both signs, at least one leaf agrees with these newly aligned hubs and can flip downhill with energy change \(-4J\). These two cases provide an escape from every excited weak minimum using at most two flips, the first neutral.

Finally consider the finite-state continuous-time Markov chain specified in the assumptions. Its energy is nonincreasing along every path. In a closed communicating class, energy must be constant, because any directed cycle cannot contain a strict downward step. If such a class included a state with an available downhill flip, closure would be violated. If it included an excited weak minimum, the preceding neutral-then-downhill path, every step of which has positive rate, would violate closure. Hence every closed class is contained among the two strict ground states, which are singleton absorbing classes. A finite-state continuous-time Markov chain enters some closed class almost surely. The result follows for every initial configuration.

## Verification
The standalone `checker.py` constructs all configurations and every one-spin flip exactly over integer exchange units, independently of the case algebra. For every \(2\le n\le12\) it checks the weak-count formula, the two strict ground states, both energy sectors, and a neutral-then-downhill exit from every excited weak state. These are exhaustive *finite* checks, not a substitute for the all-\(n\) proof above.

## Relationship to prior work
Baek, Ha and Jeong [1] describe zero-temperature Glauber absorbing states and distinguish a neutral-flip *blinker* from genuine absorption, but study random networks with ferromagnetic interaction rather than the deterministic antiferromagnetic book family. The antiferromagnetic triangular-lattice equilibrium analysis of Eggarter [2] concerns a different lattice geometry and equilibrium properties. The present claim is the exact complete weak/strict stability census, explicit two-flip escape, and almost-sure absorption classification for all triangular books. General finite-state Markov-chain absorption theory supplies the last logical step after the book-specific escape lemma; that general principle alone does not supply the classification. Historical priority is not independently certified.

## Limitations
The theorem is specific to zero external field, positive uniform antiferromagnetic coupling, the triangular-book graph, and neutral flips accepted with positive rate. If neutral moves are forbidden, the excited weak minima themselves become absorbing, reversing the dynamical conclusion. Absorption times are not bounded, no finite-temperature statements are made, and no claim of originality beyond examined literature is certified.

## References
[1] Y. Baek, M. Ha, H. Jeong, *Absorbing states of zero-temperature Glauber dynamics in random networks*, arXiv:1112.5927 (first publicly posted 2011-12-27), https://arxiv.org/abs/1112.5927.

[2] T. P. Eggarter, *Triangular antiferromagnetic Ising model*, Physical Review B **12** (1975), 1933–1939, https://doi.org/10.1103/PhysRevB.12.1933. The graph geometry and target results differ from the present theorem.
