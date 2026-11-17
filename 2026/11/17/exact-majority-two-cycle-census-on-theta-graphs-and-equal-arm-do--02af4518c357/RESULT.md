# Exact majority two-cycle census on theta graphs and equal-arm dominance

## Finding

For any integers \(a,b,c\ge2\), let \(\Theta_{a,b,c}\) be the simple graph formed by three internally vertex-disjoint paths of lengths \(a,b,c\) joining the same two terminals. All vertices update simultaneously by binary strict-neighbor majority, retaining their current bit on a tie. Let \(N_2(a,b,c)\) denote its number of distinct **primitive temporal two-cycle orbits** (two phase configurations are one orbit).

For \(L\ge3\), let \(E_L\) and \(O_L\) count binary words of length \(L-1\) that begin with zero, have no runs of length one (including both endpoints), and end, respectively, in zero and one. Their generating functions are
\[
\sum_{L\ge3}E_Lz^{L-1}=\frac{z^2(1-z)}{(1-z)^2-z^4},\qquad
\sum_{L\ge3}O_Lz^{L-1}=\frac{z^4}{(1-z)^2-z^4}.
\]
For a path of length two, define \((E_{2,p},O_{2,p})=(1,0)\) if \(p=1\), and \((0,0)\) if \(p=0\); for \(L\ge3\), define \((E_{L,p},O_{L,p})=(E_L,O_L)\) for either \(p\). All parities are taken modulo two.

**Exact all-parameter theorem.** For every nonempty subset \(S\) of the three labelled paths with all lengths \(\ell_i\) for \(i\in S\) of common parity \(p\), define the contribution \(H(S)\) as follows, where \(T=\{1,2,3\}\setminus S\):
\[
H(S)=\begin{cases}
1,&|S|=3,\\
2(E_{\ell_k,p}+O_{\ell_k,p}),&|S|=2,\ T=\{k\},\\
2(E_{\ell_j,p}E_{\ell_k,p}+O_{\ell_j,p}O_{\ell_k,p}),&|S|=1,\ T=\{j,k\}.
\end{cases}
\]
Then
\[
\boxed{N_2(a,b,c)=\sum_{\substack{\varnothing\ne S\subseteq\{1,2,3\}\\\ell_i\equiv\ell_j\ (\mathrm{mod}\ 2)\ \forall i,j\in S}}H(S),\quad(\ell_1,\ell_2,\ell_3)=(a,b,c).}
\]
The three summands distinguish the **exact number of internally oscillating paths**. They constitute a complete and disjoint classification of all nonfixed periodic orbits on the graph.

**Equal-arm corollary.** For every \(L\ge3\), with Fibonacci numbers \(F_0=0,F_1=1,F_{k+2}=F_{k+1}+F_k\) and six-periodic \(\delta_L\) taking values \((-1,-1,0,1,1,0)\) at residues \(L\equiv(0,1,2,3,4,5)\pmod6\), the one-, two-, and three-active-path orbit counts on \(\Theta_{L,L,L}\) are respectively
\[
3(F_{L-2}^2+\delta_L^2),\quad 6F_{L-2},\quad 1.
\]
Thus the full orbit count is \(3(F_{L-2}^2+\delta_L^2)+6F_{L-2}+1\), and **the fraction of primitive two-cycle orbits oscillating along just one path tends to one**, with complement \(O(\varphi^{-L})\), where \(\varphi=(1+\sqrt5)/2\). In particular, \(N_2(L,L,L)\sim(3/5)\varphi^{2L-4}\).

Examples: \(N_2(2,2,2)=1\), \(N_2(2,2,3)=4\), \(N_2(3,3,3)=13\), \(N_2(3,4,5)=8\), \(N_2(5,5,5)=25\), \(N_2(5,7,9)=141\), and \(N_2(9,9,9)=589\).

## Assumptions and scope

The graph is simple and each of its three terminal-to-terminal paths has at least two edges; there is **no direct terminal edge**. Path interiors are mutually disjoint. The two degree-three terminals and the degree-two internal vertices are all individually distinguished, and the three paths are distinguished when applying the formula. These are temporal orbits on labelled configurations, **not** configurations modulo spatial graph automorphisms. The local update takes the strict majority among the *open* neighborhood; at degree two it retains the present bit on a one-to-one tie. The count concerns only states already lying on a primitive period-two orbit, not those ultimately attracted to such an orbit.

## Proof

**1. Propagation on degree-two sites.** If a degree-two site flips from \(x\) to \(F(x)\) and back on a two-cycle, both of its neighbors must have the opposite phase value, and therefore must flip also. Iterating along a path shows that any nonfixed two-cycle flips both terminals and makes at least one entire connecting path flip. Every wholly flipping path has spatially alternating bits, uniquely determined by the bit at the first terminal. If the first terminal is in phase zero, the second terminal must have bit \(p\), the parity of that path's length. Multiple flipping paths are possible only when their lengths have the same parity.

**2. Frozen paths.** In an unflipped path of length \(L\ge3\), its \(L-1\) internal sites have constant bits over the two phases. At the first (last) internal site, the terminal flips, hence the adjoining internal bit must agree with it; at each other internal site, at least one of the two adjacent fixed sites must agree. These conditions are exactly that the internal binary word has no singleton run, including at its ends. If \(L=2\), its sole internal site can be frozen precisely when the two terminal phases are opposite (\(p=1\)), since then it sees a permanent tie; its bit is arbitrary. It cannot be frozen for \(p=0\).

For \(L\ge3\), fixing the first internal bit at zero, each word is a composition of \(L-1\) into runs of lengths at least two, with alternating run colors. An odd number of runs ends with zero (count \(E_L\)); an even number ends with one (count \(O_L\)). The generating function for one run is \(R(z)=z^2/(1-z)\). Consequently \(\sum E_Lz^{L-1}=R/(1-R^2)\) and \(\sum O_Lz^{L-1}=R^2/(1-R^2)\), which yield the stated rational functions. Complementing all bits gives the same two counts when the first bit is one.

**3. Majority at the terminals.** Suppose exactly \(r\in\{1,2,3\}\) paths flip. At each terminal, each flipping path's adjacent site has the opposite phase bit. For \(r\ge2\), those votes provide the strict majority on both phases, regardless of the remaining stationary neighbor. For \(r=1\), the two fixed-path neighbors of **each** terminal must have opposite stationary bits, giving one supporting vote for each of the two phases. No terminal can flip if \(r=0\). Therefore a one-active-path orbit requires each of the two fixed words' first bits to be opposite and their last bits to be opposite.

**4. Exact counting and no omissions.** Choose the phase with first-terminal bit zero; the opposite phase with bit one is uniquely the other state of the same temporal orbit. For three active paths, all three lengths must have equal parity, and there is one orbit. For two active paths of common parity \(p\), the third path may be any permitted frozen word, counted as \(2(E_{L,p}+O_{L,p})\). For one active path of parity \(p\), each of the other two frozen paths has prescribed equal or different terminal word-end colors. Summing over the two choices of the first fixed word's initial bit, and requiring opposite end bits at *both* terminals, yields \(2(E_{L,p}E_{M,p}+O_{L,p}O_{M,p})\). All constructed states satisfy the local update rule by steps 1–3. Conversely, every primitive two-cycle belongs to one of the enumerated support classes. Distinct support classes are disjoint, proving the formula.

**5. Equal-arm entropy and dominance.** The run-composition functions imply \(E_L+O_L=F_{L-2}\), while \(E_L-O_L\) has generating function \(z^2/(1-z+z^2)\) and is precisely the asserted six-periodic \(\delta_L\). On three equal arms of length \(L\ge3\), summing across the three choices of one active path gives \(6(E_L^2+O_L^2)=3(F_{L-2}^2+\delta_L^2)\); the two-active classes give \(6(E_L+O_L)=6F_{L-2}\), and all three active give one. As \(F_{L-2}\sim\varphi^{L-2}/\sqrt5\), the one-active family has quadratic Fibonacci order, and the other classes only linear Fibonacci order, giving the stated asymptotics.

## Verification

The package includes two separate executable checks. Compile `theta_bruteforce.cpp` with `g++ -std=c++17 -O3 theta_bruteforce.cpp -o theta_bruteforce` and execute `./theta_bruteforce`. This directly checks \(F(F(x))=x\ne F(x)\) over **all binary configurations** of 77 nondecreasing parameter triples with at most 19 vertices, covering 5,294,176 configurations, and separately checks six named triples including a 20-vertex case. This checker computes its own formula from an independent run-composition recursion.

Run `python3 theta_construct.py`. It independently constructs two-cycles from alternating paths and legal frozen words, confirms the local transition and orbit counts for 113 parameter triples, and checks all listed larger examples. Its formula implementation and its constructive word generator are separate code paths. Standard output from the two successful runs is included. Neither finite check is used in place of the universal argument in the Proof section.

## Relationship to prior work

Goles and Olivos (1980) established that finite symmetric threshold systems have no eventual periods greater than two. Benjamini, Chan, O'Donnell, Tamuz, and Tan (arXiv:1405.2486v1, 11 May 2014) study majority dynamics on finite/infinite and random graphs and state the general period-two theorem. Tosic and Agha (2004) analyze simple threshold cellular automata and the one-dimensional majority rule. None of these results, by itself, counts the individual period-two orbits on three-path theta graphs. The local no-singleton-run constraint is familiar from one-dimensional majority automata; it is **not** claimed as a new combinatorial sequence.

Published mathematical records on a singly chorded cycle concern a direct terminal edge, whereas the present theta family forbids a direct edge and has three interior paths; subdividing that chord changes the majority network's degree-two dynamics. Published records on three-color excitable theta networks use a different, three-state update rule and concern primitive three-cycles. Their theorems do not imply the present formula without a new reduction. No direct equivalent all-parameter majority-theta orbit census was identified in the specified searches.

## Limitations

The theorem does not classify fixed configurations, attraction basins, first-entry times, finite-time convergence bounds, or generalized theta graphs with more than three paths. It does not assert priority against literature that has not been located or inspected. The supporting computational checks cover only finite samples; the all-parameter conclusion rests entirely on the proof. No independent external audit has been performed.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: https://doi.org/10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11. https://arxiv.org/abs/1405.2486.
3. P. T. Tosic and G. A. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI 2004, Lecture Notes in Computer Science 3305, 861–870. https://osl.cs.illinois.edu/publications/conf/acri/TosicA04.html.
