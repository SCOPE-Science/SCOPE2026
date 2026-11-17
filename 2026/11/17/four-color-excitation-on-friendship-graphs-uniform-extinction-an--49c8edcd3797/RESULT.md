# Four-color excitation on friendship graphs: uniform extinction and four limiting terminal shells

## Finding

For every integer \(k\ge1\), let \(F_k=K_1\vee(kK_2)\) be the labelled friendship graph with one common hub and \(k\) otherwise disjoint triangles. Let \(G_k\) be the synchronous four-state, threshold-one Greenberg–Hastings map. All \(4^{2k+1}\) initial configurations reach the all-resting configuration within seven updates. The bound is sharp for \(k\ge2\), while for \(k=1\) the sharp bound is five.

Let \(\tau(x)\) be the least \(t\ge0\) with \(G_k^t(x)\) all resting. Define \(E_t(k)=\#\{x:\tau(x)=t\}\). The entire exact labelled extinction-time distribution, for every integer \(k\ge1\), is

\[
\begin{aligned}
E_0(k)&=1,\\
E_1(k)&=2\cdot4^k-1,\\
E_2(k)&=3\cdot9^k-2\cdot4^k,\\
E_3(k)&=2\cdot14^k-9^k,\\
E_4(k)&=16^k-9^k+6^k-1,\\
E_5(k)&=16^k-14^k+12^k-6^k-5^k+3^k,\\
E_6(k)&=16^k-10^k-9^k+5^k-3^k+1,\\
E_7(k)&=16^k-14^k-12^k+10^k.
\end{aligned}
\]

These quantities sum to \(4\cdot16^k\) exactly. More specifically, \(\tau(x)=7\) if and only if the hub starts in state \(3\), at least one triangle has peripheral endpoint colors \(\{0,1\}\), and a *different* triangle has endpoint colors \(\{1,2\}\) or \(\{1,3\}\). Consequently, for independently uniform initial colors,
\[
\tau(X_k)\ \xrightarrow[k\to\infty]{\mathrm{law}}\ \operatorname{Uniform}\{4,5,6,7\}.
\]
Every nonzero periodic orbit is excluded: the all-resting point is the unique recurrent configuration.

## Assumptions and scope

The vertices are distinctly labelled \(h,u_1,v_1,\ldots,u_k,v_k\), with edges precisely \(hu_i\), \(hv_i\), and \(u_iv_i\) for \(1\le i\le k\); triangles do not share edges. Each vertex has state in \(\{0,1,2,3\}\), where \(0\) is resting and \(1\) is excited. At each simultaneous update, \(1\to2\to3\to0\) unconditionally, and \(0\to1\) if and only if some adjacent vertex is currently in state \(1\); otherwise \(0\to0\). There is no spontaneous excitation, no stochastic forcing, and no quotient by graph automorphisms. Death is the first time the *whole graph* is resting, not the first absence of currently excited vertices.

## Proof

**1. An exact universal 4092-case reduction.** Associate to each triangle the *unordered* pair of its two peripheral endpoint colors. There are ten possible unordered types
\[
\mathcal T=\{(a,b):0\le a\le b\le3\}.
\]
For each initial configuration, record its hub color \(h\) and the nonempty support \(S\subseteq\mathcal T\) of peripheral types, disregarding the multiplicities of types. The next hub color depends only on \(h\) and whether any type in \(S\) contains color \(1\). For a peripheral pair \((a,b)\), the next pair is determined only by \((h,a,b)\), followed by sorting; exchanging the endpoints does not affect the sorted result. Thus the next \((h,S)\) is a deterministic function of the current \((h,S)\), and this reduction is **exact for every \(k\)**. Every initially represented type remains represented by at least one pair at every later time, so support reduction cannot prematurely declare extinction.

There are exactly \(4(2^{10}-1)=4092\) hub/support cases. The finite, exhaustive certificate `finite_certificate.py` lists the ten types in lexicographic order, constructs their local successor maps directly from the stated update rule, and follows **all** nonempty support cases. It verifies that every case becomes \((0,\{(0,0)\})\) within seven updates, and tests the exact logical equivalence
\[
\tau=7\quad\Longleftrightarrow\quad h=3,\quad (0,1)\in S,\quad S\cap\{(1,2),(1,3)\}\ne\varnothing.
\]
Since the reduction is complete and deterministic, these 4092 finite checks prove the all-size extinction assertion. It also excludes nonresting cycles: all states reach an absorbing rest configuration. The witness criterion is realizable at \(k=2\), so the seven-step bound is sharp for all \(k\ge2\) by duplicating any initial peripheral type. For \(k=1\), direct inspection of the certificate's singleton supports yields maximum five.

**2. Exact support-to-labelled count.** The number of **ordered** peripheral color assignments corresponding to unordered type \(p=(a,b)\) is \(w_p=1\) if \(a=b\), and \(w_p=2\) otherwise. In total \(\sum_{p\in\mathcal T}w_p=16\). For a prescribed hub color \(h\) and a prescribed nonempty support \(S\), inclusion–exclusion gives the number of labelled \(k\)-petal words using *every* type of \(S\) and no others:
\[
N_k(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}\biggl(\sum_{p\in T}w_p\biggr)^k.
\]
The empty inner sum is zero because \(k\ge1\). Therefore
\[
E_t(k)=\sum_{h=0}^{3}\ \sum_{\substack{\varnothing\ne S\subseteq\mathcal T\\ \tau(h,S)=t}}N_k(S).
\]
The certificate evaluates the complete finite double sum **symbolically as a signed integer combination of power functions**, not by interpolating finite values of \(k\). Its eight coefficient dictionaries, for time \(t=0,\ldots,7\), are precisely the eight displayed formulas. The code computes these coefficients directly using weighted subset inclusion–exclusion over every possible \(h,S,T\); it asserts equality with the displayed dictionaries and conservation of total mass. This is a finite exact computation combined with an all-size combinatorial identity.

**3. The final layer and the limiting law.** The seven-step support criterion requires at least two distinct peripheral types, so its population is zero for one triangle. When the hub is state \(3\), each peripheral pair has \(16\) ordered assignments. Exactly \(2\) have unordered type \((0,1)\), and exactly \(4\) have unordered type \((1,2)\) or \((1,3)\); these categories are disjoint. Requiring both categories to appear in \(k\) labelled petals gives
\[
E_7(k)=16^k-(16-2)^k-(16-4)^k+(16-2-4)^k,
\]
proving the fourth-term formula independently of symbolic coefficient collection. Dividing the full eight formulas by \(4\cdot16^k\), the leading \(16^k\) term appears exactly once in each of layers four through seven. All other bases are strictly smaller than sixteen. Hence the claimed four-point uniform weak limit follows, with exponential error.

## Verification

The self-contained `finite_certificate.py` enumerates all 4092 exact support classes, proves the seven-step predicate for each, and symbolically validates the coefficient dictionary for every one of the eight layers. Reproduction: `python3 finite_certificate.py`; its observed output is `finite_certificate_output.txt`. A wholly separate vertex-neighborhood implementation, `full_state_census.cpp`, directly enumerates and simulates all labelled configurations for each \(1\le k\le5\), comparing every layer against the formulas. Reproduction: `g++ -std=c++17 -O3 full_state_census.cpp -o full_state_census && ./full_state_census`; the observed output is `full_state_census_output.txt`. The latter checks \(4,473,920\) distinct labelled initial configurations. Direct simulation at finite sizes is a cross-check, while the exact support lemma and its full finite-state enumeration supply the all-size proof.

## Relationship to prior work

Gravner, Lyu and Sivakoff [3] give the general \(\kappa\)-state Greenberg–Hastings update definition (their equation (1)), but their main graph-wide circulation and synchronization theorems explicitly specialize to **three colors**. Their results do not determine the four-color friendship-graph extinction layers. The published three-color friendship-graph classification [5] finds genuine primitive three-cycles, a four-step entrance cutoff and a different limiting law; it does not cover the additional refractory state. The four-state complete-tripartite theorem [6] treats a different class of graphs, with primitive four-cycles; for \(k\ge2\) the friendship graph is not a complete tripartite graph. The three-state square-bouquet theorem [7] is likewise different both in graph girth and refractory length. Garcia and collaborators [2] analyze short-loop excitable pacemakers but do not give the stated all-size four-state windmill shell census. These published statements do not imply the new eight-layer formula or its four-point limiting law. Earlier lattice work [1] establishes historical model context, not an equivalent calculation on labelled friendship graphs.

## Limitations

The theorem is only about finite friendship graphs, synchronous threshold-one *four-state* excitation, and independently uniform colors for the distributional corollary. Neither variable higher refractory lengths nor altered thresholds nor general cactus graphs are classified. The 4092-case proof has an executable exact finite computation as a critical lemma, without an externally certified formal proof; both scripts require their indicated language runtimes. The earliest cited public archival model source [1] was accessible as an abstract and date record, not as a complete full-text priority comparison. Unindexed earlier work could affect historical novelty. No independent mathematical audit has been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, public abstract dated 1993-03-22. https://arxiv.org/abs/patt-sol/9303002
2. G. C. Garcia, A. Lesne, M.-T. Hütt and C. C. Hilgetag, *Building Blocks of Self-Sustained Activity in a Simple Deterministic Model of Excitable Neural Networks*, Frontiers in Computational Neuroscience 6 (2012), 50, first published 2012-08-06. https://doi.org/10.3389/fncom.2012.00050
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, public 2016-10-24, particularly equation (1) and Theorem 3. https://arxiv.org/pdf/1610.07320
4. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126. https://doi.org/10.25088/ComplexSystems.27.2.101
5. *Shared three-cycle skeleton and unequal stopping-time laws for excitation on friendship graphs*, published-finding corpus, public 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-shared-three-cycle-skeleton-and-unequal-stopping-time-laws-for-e--e79c2691fb75
6. *Four-state excitation on tripartite graphs: identical four-cycle orbits, different transients, and exact extinction*, published-finding corpus, public 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-four-state-excitation-on-tripartite-graphs-identical-four-cycle--6411c0882be0
7. *Uniform six-step entrance and exact excitation waves on bouquets of squares*, published-finding corpus, public 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-uniform-six-step-entrance-and-exact-excitation-waves-on-bouquets--15a728a38ba4
