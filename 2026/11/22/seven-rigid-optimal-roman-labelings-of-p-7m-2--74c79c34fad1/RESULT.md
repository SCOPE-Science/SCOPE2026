# Seven rigid optimal Roman labelings of \(P(7m,2)\)

## Finding

Let \(m\ge1\) be an integer and \(n=7m\). In the generalized Petersen graph \(P(n,2)\), write the outer vertices as \(v_i\), the inner vertices as \(u_i\), and take the edges \(v_iv_{i+1}\), \(v_iu_i\), and \(u_iu_{i+2}\), with indices modulo \(n\). A Roman dominating function assigns \(0,1,2\) to vertices, requires each zero-labeled vertex to have a two-labeled neighbor, and has weight equal to its label sum.

**Theorem.** For every \(m\ge1\), exactly seven Roman dominating functions on \(P(7m,2)\) attain the minimum weight \(8m\). They are the seven cyclic shifts of the following seven-column word, repeated \(m\) times, where each ordered pair gives the labels \((f(v_i),f(u_i))\):

\[
((0,2),(0,2),(1,0),(0,0),(2,0),(0,0),(1,0)).
\]

In particular, every optimum has exactly \(3m\) vertices labeled two and \(2m\) vertices labeled one. All seven optima form one orbit under index rotation and have fundamental period seven.

Let \(T_f=\{x:f(x)=2\}\). In the *support-exchange graph at capacity* \(k\), two distinct optimum functions are adjacent when \(\lvert T_f\setminus T_g\rvert=\lvert T_g\setminus T_f\rvert\le k\); the labels on the remaining vertices are recomputed according to the corresponding optimum. Then this graph is \(7K_1\) for \(k<2m\), is \(C_7\) for \(2m\le k<3m\), and is \(K_7\) for \(k\ge3m\). Hence the sharp capacity for connectivity is \(2m\).

## Assumptions and scope

The graph is finite, simple, and explicitly labeled as above; \(n=7m\ge7\), so the two inner-neighbor indices are distinct. The count is of *named* functions on the labeled vertex set, not of functions modulo automorphisms. Zero labels must have a neighboring two, but one labels need no such neighbor. The exchange rule replaces an equal number of two-labeled vertices and need not preserve labels at other vertices during a move; only its endpoints must be optimal. No claim is made for cycle lengths not divisible by seven.

## Proof

**1. Exact finite-state encoding.** A column is the pair \((f(v_i),f(u_i))\), encoded by \(a_i=3f(v_i)+f(u_i)\in\{0,\ldots,8\}\). Construct a directed graph \(D\) on all \(9^4=6561\) four-column words. For a state \((a,b,c,d)\) and appended column \(e\), draw the arc

\[
(a,b,c,d)\longrightarrow(b,c,d,e)
\]

precisely when both zero-label constraints at the middle column \(c\) hold. Writing \(o(x)=\lfloor x/3\rfloor\), \(t(x)=x\bmod3\), these constraints are

\[
\begin{aligned}
o(c)=0&\implies\bigl(o(b)=2\ \lor\ o(d)=2\ \lor\ t(c)=2\bigr),\\
t(c)=0&\implies\bigl(t(a)=2\ \lor\ t(e)=2\ \lor\ o(c)=2\bigr).
\end{aligned}
\]

Assign the arc the integer cost \(c_{ab cde}=7(o(c)+t(c))-8\). The location of the center column makes this a sliding five-column test. For \(n\ge7\), valid length-\(n\) cyclic label words are in bijection with length-\(n\) closed walks whose starting state is fixed by the four labels at indices \(0,1,2,3\). The total arc cost along the walk is exactly \(7w(f)-8n\).

**2. A finite, replayable potential certificate.** The file `verification/potential.txt` lists an integer \(h(s)\) for each state, in base-nine lexicographic order. The standalone `verification/verify_potential.py` reconstructs all arcs, verifies

\[
7(o(c)+t(c))-8+h(a,b,c,d)-h(b,c,d,e)\ge0
\]

for each arc, and computes the strongly connected components of the directed *tight* subgraph consisting of arcs where equality holds. The check gives **48,681** admissible arcs, **6,099** tight arcs, and precisely one tight directed cycle, of length seven. All other tight strongly connected components are singletons without loops. The unique cyclic component has labels given by the displayed word, up to rotation. The certificate can also be regenerated independently by `verification/derive_potential.cpp`; its listed potential values lie between \(-26\) and \(0\).

**3. Infinite-family optimality and rigidity.** Summing the checked potential inequalities around any closed walk gives \(7w(f)-8n\ge0\). Repetition of the displayed seven-column word satisfies every zero-neighbor condition and has weight \(8m\). Therefore the Roman domination number of \(P(7m,2)\) is \(8m\). For an optimal word, the sum of the nonnegative reduced arc costs is zero, so every traversed arc is tight. Every closed walk of the tight subgraph lies on its unique directed seven-cycle. Consequently its column word is the seven-word repetition, up to one of the seven shifts. All seven are distinct because the word has primitive period seven. This proves the complete classification for every \(m\ge1\), not merely for computationally tested sizes.

**4. Exchange geometry.** In one seven-column period the two-labeled support is \(\{u_0,u_1,v_4\}\). Two shifted supports intersect in one vertex per period for shifts differing by \(1\) or \(-1\) modulo seven, and are disjoint otherwise. Repeating \(m\) periods, their symmetric exchange requirements are respectively \(2m\) and \(3m\) support replacements. Thus the seven-state exchange graph has exactly the three regimes stated in the theorem.

## Verification

Run `python3 verification/verify_potential.py` with the files in their listed relative locations. Its deterministic checks verify the arc count, integer inequalities, tight-cycle uniqueness, critical word, and Roman feasibility of sample repetitions. Separately, `g++ -O3 -std=c++17 verification/derive_potential.cpp -o derive_potential` followed by `./derive_potential > regenerated.txt` reconstructs exactly the supplied integer certificate. The program `verification/enumerate_small.cpp` independently enumerates all potentially optimal two-labeled supports for lengths seven and fourteen, proving that there are exactly seven minima in each case. These small cases are checks, not the basis for extrapolation to arbitrary \(m\).

## Relationship to prior work

Wang, Xu, Yang, and Ji proved the Roman domination number \(\gamma_R(P(n,2))=\lceil8n/7\rceil\) for every \(n\ge5\) in the archival 2011 preprint [1]. Their work is the source of the known optimal *weight*, and its periodic construction motivates the present exact classification. The contribution here is the all-order uniqueness-up-to-seven-shifts theorem and the resulting sharp support-exchange geometry. Shi and Koh [2] gave general algorithms to count minimum Roman dominating functions on arbitrary graphs; their general algorithmic existence does not state the closed seven-function classification on this graph family. An earlier unindexed classification of equality cases is a residual priority risk.

## Limitations

The assertion concerns only the residue class \(n\equiv0\pmod7\) and the specified ordinary Roman labeling convention. The exchange graph has a deliberately defined simultaneous support-change rule; it is not a claim about every possible reconfiguration model. The finite-state proof relies on the supplied integer certificate and its explicitly replayable verifier rather than on an unaided hand enumeration of all states. No independent scholarly validation has been performed.

## References

1. H. Wang, X. Xu, Y. Yang, and C. Ji, *Roman domination number of Generalized Petersen Graphs \(P(n,2)\)*, arXiv:1103.2419, first public version March 12, 2011. https://arxiv.org/abs/1103.2419
2. Z. Shi and K. M. Koh, *Counting the Number of Minimum Roman Dominating Functions of a Graph*, arXiv:1403.1019, March 5, 2014. https://arxiv.org/abs/1403.1019
