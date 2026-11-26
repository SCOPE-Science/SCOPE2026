# Sharp five-step extinction for threshold-two excitation on circular prisms

## Finding
For every integer \(n\ge3\), let \(G_n=C_n\square K_2\) be the simple graph with vertices \((j,r)\), \(j\in\mathbb Z/n\mathbb Z\), \(r\in\{0,1\}\), and three distinct neighbors \((j-1,r),(j+1,r),(j,1-r)\). Consider synchronous three-state Greenberg–Hastings dynamics: \(1\mapsto2\mapsto0\); a resting vertex \(0\) becomes \(1\) precisely when **at least two distinct neighbors** are in state \(1\), and otherwise remains \(0\). Let \(F_n\) denote the global update.

For every initial configuration \(x\), \(F_n^5(x)=\mathbf0\). The sharp maximum first hitting time of the all-rest configuration is
\[
T_n=\max_x\min\{t\ge0:F_n^t(x)=\mathbf0\}=\begin{cases}4,&3\le n\le5,\\5,&n\ge6.\end{cases}
\]
Consequently \(\mathbf0\) is the unique recurrent state, and all nontrivial periodic orbits are absent.

## Assumptions and scope
All graphs are simple, undirected and have a two-row circular prism structure. The model is deterministic, synchronous, ternary and has threshold two in the **open** neighborhood. Initial configurations may contain states \(0\), \(1\) and \(2\) arbitrarily. The result covers all circumferences \(n\ge3\) and does not claim extinction on arbitrary cubic graphs or on prisms of more than two rows.

Write each column as the integer \(a+3b\in\{0,\ldots,8\}\), where \(a,b\in\{0,1,2\}\) are the upper and lower vertex states. Define \(g(u,v,w)\) as the next column from western, current and eastern columns according to the rule above. This yields an exact radius-one cellular automaton on a nine-symbol alphabet.

## Proof
**Local language reduction.** Let \(\mathcal P\subseteq\{0,\ldots,8\}^2\) consist of all pairs \((g(a,b,c),g(b,c,d))\), for \(a,b,c,d\in\{0,\ldots,8\}\). Every adjacent pair in any configuration after one update belongs to \(\mathcal P\), regardless of the circumference. Direct enumeration of the \(9^4=6561\) quadruples gives \(|\mathcal P|=50\).

For each seven-column word \(w=(w_0,\ldots,w_6)\) whose six adjacent pairs belong to \(\mathcal P\), perform three successive radius-one updates, keeping only the interior columns at each step. The lengths reduce as \(7\to5\to3\to1\). The exact enumeration in the accompanying standalone verifier finds \(589781\) such words and gives the following final central-column distribution: output \(0\) occurs \(589585\) times, output \(2\) occurs \(98\) times, and output \(6\) occurs \(98\) times; all other outputs occur zero times. Since columns \(0,2,6\) contain no excited vertex, an arbitrary configuration has **no excited vertex after four steps**. All refractory vertices necessarily become resting on the next update, proving \(F_n^5\equiv\mathbf0\). This exhaustiveness is a finite local implication, not an inference from finitely many graph sizes: each site at time four depends on seven columns at time one, and every adjacent pair there lies in \(\mathcal P\).

**Sharpness.** For \(n=6\), the cyclic column configuration \((1,3,0,3,0,3)\) contains an excited vertex after three updates, hence a refractory vertex after four, and first reaches all-rest at time five. For every \(n\ge7\), the first seven columns \((1,3,0,3,0,3,1)\), followed by zero columns, likewise create an excited upper vertex at column \(3\) after three updates. Its backward dependence cone meets only those seven columns; this remains true for circumference seven, and for every longer circumference. Thus \(T_n=5\) for all \(n\ge6\).

For the three remaining circumferences \(n=3,4,5\), direct exact enumeration of every initial configuration (respectively \(9^3\), \(9^4\), \(9^5\) cases) gives sharp maximum hitting time four. The standalone program enumerates all \(66339\) such initial configurations and tests the hitting times.

## Verification
Compile `verify.cpp` as ISO C++17, for example with `g++ -std=c++17 -O2 verify.cpp -o verify`, then execute `./verify`. The verifier recomputes \(g\), constructs \(\mathcal P\), exhaustively enumerates all length-seven words satisfying the pair restrictions, checks the complete local output distribution, exhausts initial states for the three small graphs and tests explicit sharpness witnesses through circumference 80. Its supplied recorded output ends in `VERIFY_OK`. The proof for arbitrarily large circumferences is the bounded-dependence argument, not the finite list of larger witness tests.

## Relationship to prior work
The Greenberg–Hastings and cyclic automaton families, including integer contact thresholds and spatial wave dynamics, were studied by Fisch, Gravner and Griffeath [1]. Gravner, Lyu and Sivakoff [2] studied three-color excitability on general graphs but explicitly use **one excited neighbor**, not the present two-neighbor threshold. The present statement is a sharp *uniform extinction-time* result for a particular unbounded two-row graph family. The nearest threshold-one results and broad lattice phase-diagram statements do not imply this precise finite-time bound. Prior methodology and model definitions are not claimed as new.

## Limitations
The mathematical proof uses exhaustive verification of an exact finite local language identity; the accompanying program is needed to replay that finite check. The result concerns only the stated threshold, state count and graph family. Searches and source inspections do not establish absolute historical uniqueness. No independent external audit has been performed.

## References
[1] R. Fisch, J. Gravner, D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing 1 (1991), 23–39. Dated arXiv deposit 1993-04-02, https://arxiv.org/abs/patt-sol/9304001 ; open full text https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf .

[2] J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, Annals of Applied Probability 28 (2018), 3324–3357, https://arxiv.org/abs/1610.07320 ; full text https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
