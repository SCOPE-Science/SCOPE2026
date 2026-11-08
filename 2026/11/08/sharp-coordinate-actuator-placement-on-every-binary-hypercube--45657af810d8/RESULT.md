# Sharp coordinate-actuator placement on every binary hypercube

## Finding

For every integer \(d\ge1\), consider the binary hypercube \(Q_d\) with vertex set \(\{0,1\}^d\), where two vertices are adjacent if they differ in exactly one coordinate. Let \(L_d\) be the unweighted combinatorial Laplacian. For the continuous-time system
\[
\dot z=-L_dz+B_Su,
\]
where \(B_S\) has one standard coordinate vector for each separately actuated vertex in \(S\), the smallest possible cardinality is
\[
\boxed{\min\{|S|:(-L_d,B_S)\text{ is controllable}\}=\binom d{\lfloor d/2\rfloor}.}
\]
An explicit optimal location set depends on the parity of the dimension:

- When \(d=2k+1\) is odd, take every binary vector of Hamming weight \(k\): \(S=\{x:|x|=k\}\).
- When \(d=2k\) is even, take \(S=\{(y,b):|y|=k-1,\ y\in\{0,1\}^{2k-1},\ b\in\{0,1\}\}\).

The superficially similar choice consisting of all weight-\(k\) vertices in even dimension \(2k\) is *never controllable* for \(k\ge1\): its restriction matrix for eigenvalue \(2k\) has at most half the required rank. This distinguishes a construction that succeeds for every odd-dimensional cube from one that fails for every even-dimensional cube.

## Assumptions and scope

The dimension \(d\) is any integer at least one. Edge weights are exactly one; the graph is undirected; there is no edge-weight uncertainty. Every controlled vertex receives its own scalar input, so the input matrix is precisely the collection of distinct standard basis columns indexed by \(S\). Controllability means ordinary real finite-dimensional Kalman controllability for all initial and final states, equivalently the Popov–Belevitch–Hautus (PBH) eigenvector criterion. No bounded-input, positive-input, approximate, robust or arbitrary-input-matrix assertion is made. The parity constructions are stated in the fixed displayed coordinate labeling; any coordinate permutation or bitwise translation preserves controllability.

For integers \(n\ge1\) and \(0\le j\le n\), let \(V_j\) denote the real vector space of functions on \(j\)-subsets of \([n]\). We identify a binary vertex with the subset of its one-coordinates. The Walsh character for a subset \(T\subseteq[n]\) is
\[
\chi_T(x)=(-1)^{|T\cap x|}.
\]
Here a binomial coefficient with lower index outside its allowed interval is interpreted as zero. The notation \(|x|\) means Hamming weight.

## Proof

**Step 1: sharp lower bound from the actual Laplacian eigenvalues.** The Walsh characters satisfy
\[
L_d\chi_T=2|T|\chi_T.
\]
Consequently, the eigenspace for eigenvalue \(2j\) has dimension \(\binom dj\). If \(B_S\) controls the system, PBH says that restricting Walsh functions in each fixed eigenspace to the rows indexed by \(S\) must be injective. In particular, \(|S|\ge\max_j\binom dj=\binom d{\lfloor d/2\rfloor}\). We will attain this lower bound with coordinate columns, rather than an arbitrary dense input matrix.

**Step 2: harmonic decomposition of a Boolean layer.** Fix an odd dimension \(n=2k+1\). Write \(U_r:V_r\to V_{r+1}\) for the inclusion-up operator
\[
(U_rf)(X)=\sum_{\substack{Y\subset X\\|Y|=r}}f(Y),
\]
and set \(D_{r+1}=U_r^{\!*}\), with \(D_0=0\) and the boundary convention \(U_{-1}D_0=0\). Counting pairs of incidences gives the exact commutator
\[
D_{r+1}U_r-U_{r-1}D_r=(n-2r)I.
\]
Thus, for \(0\le r<k\),
\[
\|U_rf\|^2=\|D_rf\|^2+(n-2r)\|f\|^2,
\]
so \(U_r\) is injective. Put \(H_\ell=\ker D_\ell\) and define, for \(\ell\le j\le k\), the inclusion lift
\[
(E_{j,\ell}h)(T)=\sum_{\substack{R\subseteq T\\|R|=\ell}}h(R).
\]
Because \(V_j=\operatorname{im}U_{j-1}\oplus\ker D_j\), and \(U_{j-1}E_{j-1,\ell}=(j-\ell)E_{j,\ell}\) for \(\ell<j\), induction proves the direct decomposition
\[
V_j=\bigoplus_{\ell=0}^j E_{j,\ell}H_\ell.
\]
The inclusion lifts into \(V_k\) are injective and their harmonic-sector ranges form a direct sum. This establishes the decomposition without assuming a representation-theoretic theorem.

**Step 3: an all-degree, nonvanishing Walsh restriction on the odd middle layer.** Fix the row layer \(\mathcal S_k=\{x\subseteq[n]:|x|=k\}\). For \(0\le j\le k\), define
\[
(W_{k,j}f)(x)=\sum_{|T|=j}(-1)^{|x\cap T|}f(T),\qquad |x|=k.
\]
We claim that for every \(0\le\ell\le j\le k\) and \(h\in H_\ell\),
\[
W_{k,j}E_{j,\ell}h=\alpha_{k,j,\ell} E_{k,\ell}h,
\quad
\alpha_{k,j,\ell}=(-2)^\ell(-1)^{\lfloor(j-\ell)/2\rfloor}\binom{k-\ell}{\lfloor(j-\ell)/2\rfloor}.
\]
Here is a derivation. Expand \(E_{j,\ell}h\) and fix an \(\ell\)-subset \(R\). Writing \(t=|x\cap R|\), the sum of the Walsh signs over all \(j\)-subsets containing \(R\) equals
\[
F(t)=(-1)^t[z^{j-\ell}](1-z)^{k-t}(1+z)^{k+1-\ell+t}.
\]
On the integers \(0\le t\le\ell\), Newton interpolation gives \(F(t)=\sum_{i=0}^\ell\binom ti(\Delta^iF)(0)\). The defining relation \(D_\ell h=0\), iterated, implies \(\sum_{R\supseteq I,\ |R|=\ell}h(R)=0\) for every \(|I|<\ell\). Thus every term with \(i<\ell\) cancels when summing \(h(R)F(|x\cap R|)\) over \(R\), leaving \((\Delta^\ell F)(0)E_{k,\ell}h(x)\). The binomial theorem computes
\[
\begin{aligned}
(\Delta^\ell F)(0)
&=(-2)^\ell[z^{j-\ell}](1-z)^{k-\ell}(1+z)^{k+1-\ell}\\
&=(-2)^\ell[z^{j-\ell}](1-z^2)^{k-\ell}(1+z)\\
&=(-2)^\ell(-1)^{\lfloor(j-\ell)/2\rfloor}
\binom{k-\ell}{\lfloor(j-\ell)/2\rfloor},
\end{aligned}
\]
proving the claim. Since \(0\le j-\ell\le k-\ell\), the binomial coefficient is strictly positive, and hence every factor \(\alpha_{k,j,\ell}\) is nonzero. The harmonic decomposition and independent target sectors imply \(W_{k,j}\) has full column rank \(\binom nj\) for every \(0\le j\le k\).

For \(j>k\), complement each column subset \(T\) to \(T^c\). Every row \(x\in\mathcal S_k\) then satisfies \(\chi_T(x)=(-1)^k\chi_{T^c}(x)\). Thus \(W_{k,j}\) is a signed column permutation of \(W_{k,n-j}\) and again has full column rank. PBH proves controllability of all weight-\(k\) vertices in \(Q_{2k+1}\). Their number \(\binom{2k+1}k\) attains the lower bound.

**Step 4: even dimensions by a one-bit Cartesian product.** Write \(d=2k\) and \(m=2k-1\). Let \(T\) be the optimal weight-\((k-1)\) row layer in \(Q_m\) just proved. Identify \(Q_{2k}=Q_m\square K_2\) and take \(S=T\times\{0,1\}\). This has
\[
|S|=2\binom{2k-1}{k-1}=\binom{2k}k.
\]
Each level-\(j\) Walsh eigenspace of \(Q_{2k}\) is the direct sum of characters independent of the final bit, with degree \(j\) on \(Q_m\), and characters multiplied by the final-bit sign, with degree \(j-1\) on \(Q_m\). Applying the invertible two-point Hadamard transform to the two rows \((y,0),(y,1)\) for every \(y\in T\) block-diagonalizes the restriction map into twice the restriction matrices for degrees \(j\) and \(j-1\) on \(T\). Step 3 says each block has full column rank (empty boundary blocks contribute nothing). Consequently every eigenlevel restriction is injective. The even-dimensional construction is controllable and attains the universal lower bound.

**Step 5: parity obstruction for an even middle layer.** If instead \(S=\{x\in\{0,1\}^{2k}:|x|=k\}\), then the complement of every selected vertex belongs to the same set. For any character with \(|T|=k\),
\[
\chi_T(x^c)=(-1)^k\chi_T(x).
\]
Consequently the rows of the middle-eigenspace restriction matrix occur in proportional antipodal pairs, giving rank at most \(\tfrac12\binom{2k}k\), whereas the eigenspace has dimension \(\binom{2k}k\). PBH rules out controllability for every \(k\ge1\). This is an actual parity obstruction, not merely a failure to locate a suitable determinant.

Steps 1–5 prove all claims. For \(d=1\), the proof uses \(k=0\) and the one-vertex input location; for \(d=2\) it gives two adjacent controlled vertices. No unproved asymptotic or finite-enumeration inference is needed.

## Verification

The separate, dependency-free `verify.py` computes exact modular ranks of every Walsh eigenspace restriction in odd dimensions \(1,3,5,7,9\) and even dimensions \(2,4,6,8\). It also checks middle-layer rank deficiency in all four even cases; 2,309 exact-integer evaluations of the harmonic intertwining equation in odd dimensions \(3,5,7,9\); and 2,924 nonzero coefficient instances for \(1\le k\le24\). This covers 54 full-rank eigenspace cases. Run it with `python verify.py`. The proof above, not the finite computer tests or finite-field rank results, establishes the all-dimensional statement; rank over the tested finite field is used only as a reproducible corroboration.

## Relationship to prior work

Yuan, Zhao, Di, Wang and Lai (2013) establish the general PBH maximum-eigenvalue-multiplicity principle for an unrestricted control matrix and network dynamics. That theorem supplies the natural lower bound but does not by itself establish injectivity of every coordinate-row Walsh restriction for the concrete vertex sets here. Monshizadeh, Zhang and Camlibel (2014) analyze the much stronger requirement of controllability for entire qualitative matrix classes via zero forcing; their family-wide criterion is not equivalent to controllability for this one fixed Laplacian. Distance-regular multi-leader criteria in Zhang, Camlibel and Cao (2011) and the general critical-set method of Dai (2023) provide additional context but do not give this explicit all-dimensional parity pair in the inspected descriptions. The harmonic-slice representation of Filmus (2014) and Filmus–Mossel (2015) supplies prior general Boolean-layer foundations; their uniqueness of harmonic representation on a slice is not the same as injectivity of each *single homogeneous Walsh eigenlevel* on that slice. The new scalar calculation is the substantive step needed here. No novelty is claimed for PBH, Walsh diagonalization, or incidence operators individually.

## Limitations

The classification is only of the optimum number of coordinate actuators and of the stated explicit attaining and failing families: it does not enumerate all optimal placements. The edge weights must be uniform, and all selected vertices must be actuated independently; an arbitrary generic input matrix is a different design problem. The literature comparison is conditional on available searchable and inspected sources. Additional specialist work on Walsh restrictions or hypercube control could imply part or all of this construction; independent publication-priority review remains appropriate. Computational verification at finitely many dimensions cannot certify the universal proof.

## References

1. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, *Exact controllability of complex networks*, Nature Communications 4, 2447 (first published 12 September 2013), https://doi.org/10.1038/ncomms3447 ; lawful preprint https://arxiv.org/abs/1310.5806 .
2. N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868 (19 March 2014), https://arxiv.org/abs/1403.4868 .
3. S. Zhang, M. K. Camlibel and S. Cao, *Controllability of diffusively-coupled multi-agent systems with general and distance regular coupling topologies* (2011), https://research.rug.nl/en/publications/controllability-of-diffusively-coupled-multi-agent-systems-with-g/ .
4. L. Dai, *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, first published 29 October 2022, IET Control Theory & Applications 17 (2023), https://doi.org/10.1049/cth2.12385 .
5. Y. Filmus, *An orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (first posted June 2014), https://arxiv.org/abs/1406.0142 .
6. Y. Filmus and E. Mossel, *Harmonicity and invariance on slices of the Boolean cube*, arXiv:1507.02713 (first posted July 2015), https://arxiv.org/abs/1507.02713 .
