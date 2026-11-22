# Exact terminal-wave rarity on complete branching trees

## Finding
Fix integers \(b\ge2\) and \(h\ge0\). Let \(T_{b,h}\) denote the finite complete rooted \(b\)-ary tree of height \(h\), with \(N=(b^{h+1}-1)/(b-1)\) vertices. Under the three-state, threshold-\(b\) Greenberg–Hastings cellular automaton, let \(\tau(x)\) be the first time an initial coloring \(x\in\{0,1,2\}^{V(T_{b,h})}\) reaches the all-zero configuration.

The sharp global extinction time is \(h+2\). The number \(M_{b,h}\) of **labelled initial colorings** attaining this sharp time is exactly
\[
M_{b,h}=\begin{cases}
1,&h=0,1,\\
2^{b^{h-2}}3^{(b^{h-2}-1)/(b-1)},&h\ge2.
\end{cases}
\]
For \(h\ge2\), the maximizing colorings admit a coordinatewise description: leaves must initially be excited (state \(1\)); vertices one edge above the leaves must initially be at rest (state \(0\)); vertices two edges above the leaves may initially be in state \(0\) or state \(2\); and all higher vertices may initially have **any** of the three states, independently.

For uniform independent initial colors the exact terminal-shell probability is
\[
\Pr\{\tau=h+2\}=\left(\frac{2}{3^{b^2+b+1}}\right)^{b^{h-2}},\qquad h\ge2.
\]
Thus, for fixed branching \(b\), this probability has exact \(b\)-fold exponentiation from one height to the next, \(p_{b,h+1}=p_{b,h}^{\,b}\) for \(h\ge2\): the maximal clock is attained, but its attraction mass decays doubly exponentially in tree height. For \(h=0,1\) the probabilities are \(1/3\) and \(3^{-(b+1)}\), respectively.

## Assumptions and scope
The graph is precisely the unweighted, undirected, simple tree \(T_{b,h}\). Its root has \(b\) children for \(h\ge1\), each other nonleaf vertex has one parent and \(b\) children, and every leaf is at distance \(h\) from the root. All vertices are distinguished, so the count is **not** modulo tree automorphisms. Time is discrete and updates are synchronous. At a vertex, state \(0\) changes to \(1\) exactly when at least \(b\) distinct neighbors are currently in state \(1\); otherwise it stays \(0\). States \(1\) and \(2\) always change to \(2\) and \(0\), respectively. There is no repeated external stimulation, stochastic coupling, self-neighbor, or alternate tie convention. All probabilities are for independent uniform initial colors on the three states.

Define the *height above the leaves* of a vertex as its distance to a descendant leaf. On this perfect tree every vertex has a well-defined height above the leaves, between \(0\) and \(h\).

## Proof
**1. Causal branching bound.** An excitation at a vertex at time \(t\ge1\) requires \(b\) distinct excited neighbors at time \(t-1\). An excited vertex cannot again be excited one or two updates later, since it must pass through state \(2\) and then state \(0\). Recursively select \(b\) predecessors for each positive-time excitation. A backwards causal path cannot traverse an edge and immediately return: that would require the same vertex excited at times differing by two. On a tree all nonbacktracking walks are self-avoiding, and distinct predecessor branches cannot meet. Thus an excitation at time \(t\) entails an embedded complete rooted \(b\)-ary subtree of height \(t\), with \((b^{t+1}-1)/(b-1)\) distinct vertices. Hence \(t\le h\) everywhere on \(T_{b,h}\), and the process is all-zero by update \(h+2\).

**2. The last excitation must be at the root.** To have \(\tau=h+2\), an excitation must occur at time \(h\), since an excitation no later than \(h-1\) (or an initially refractory vertex) cannot remain nonzero past \(h+1\). A witness of height \(h\) contains every vertex of \(T_{b,h}\). Its root is necessarily the global root: if the witness were rooted at a vertex at positive depth \(d\ge1\), then because \(b\ge2\) there is an original leaf in a different first-generation branch at graph distance \(h+d>h\) from that vertex. A spanning witness of depth \(h\) cannot contain such a leaf, a contradiction. The witness therefore consists of every parent-to-child edge. Therefore every vertex of height \(j\) is excited at absolute time \(j\). In particular, all leaves initially have state \(1\), all height-one vertices must initially have state \(0\) (to be excited at time one), and every height-two vertex must initially avoid state \(1\) (because initial state \(1\) would force state \(2\) at time one and state \(0\) at time two). These are exactly the stated restrictions. When \(h=0\), the one vertex must be initially excited; when \(h=1\), the root must initially be resting and all leaves excited.

**3. The restrictions are sufficient, despite arbitrary parent feedback.** Induct upward on vertex height \(j\). Leaves are excited at \(t=0\). A height-one vertex is initially resting and has \(b\) excited children, so it becomes excited at \(t=1\). A height-two vertex begins in state \(0\) or \(2\). Since each child has height one and begins in state \(0\), the vertex has at most one initially excited neighbor (its parent), and is at rest at time one. Its \(b\) children are all excited at time one, so it becomes excited at time two.

Now let \(j\ge3\) and suppose the \(b\) children of a height-\(j\) vertex \(v\) are all excited at time \(j-1\). Refractory separation shows that these children are **not** excited at times \(j-2\) or \(j-3\). Hence \(v\) cannot become newly excited at time \(j-2\) or \(j-1\), because in either case it would have at most one excited neighbor (its parent). An initially excited or refractory vertex has also cleared its initial nonresting state by time two, and the argument rules out excitation at time \(j-2\). Therefore \(v\) is at rest at time \(j-1\), irrespective of its initial color or its parent's history. At the following update its \(b\) excited children force it to become excited at time \(j\). This proves the induction, including the freedom to choose all height-at-least-three colors independently. The root is excited at time \(h\), and consequently remains nonzero at \(h+1\) and first vanishes at \(h+2\).

**4. Count and probability.** For \(h\ge2\), exactly \(b^h\) leaves and \(b^{h-1}\) height-one vertices have forced colors; exactly \(b^{h-2}\) height-two vertices have two choices; the number of vertices at heights three through \(h\) is
\[
1+b+\dots+b^{h-3}=\frac{b^{h-2}-1}{b-1}.
\]
Multiplying independent choices yields the displayed formula for \(M_{b,h}\). Dividing by the total \(3^{N}\) initial colorings and using
\[
N-\frac{b^{h-2}-1}{b-1}=(b^2+b+1)b^{h-2}
\]
gives the claimed exact probability. Its next-height exponent is multiplied by \(b\), proving the power recurrence.

## Verification
The standalone C++17 file `verify_extremizers.cpp` simulates the original synchronous local rule directly, with no use of the characterization in its trajectory test. Full enumeration covers all \(3^{15}=14{,}348{,}907\) initial colorings on the height-three binary tree, all \(3^{13}=1{,}594{,}323\) colorings on the height-two ternary tree, and all smaller listed cases. Boundary-conditioned enumeration additionally covers \(3^{15}=14{,}348{,}907\) initial internal colorings on the height-four binary tree and \(3^{13}=1{,}594{,}323\) on the height-three ternary tree. The observed terminal-root populations are respectively \(12,2,432,24\), as predicted.

The independent Python standard-library file `verify_local.py` checks a stronger timing lemma under arbitrary external parent histories, with no assumption that those histories come from the original tree, and tests many independent large-tree assignments. It covers \(1{,}406{,}160\) fully enumerated adversarial local-input cases and 1,400 sampled constrained tree histories, with sizes up to 19,531 vertices. The actual console outputs are bundled as `verify_direct_output.txt` and `verify_local_output.txt`. Reproduction: compile the C++ source using `c++ -O3 -std=c++17 verify_extremizers.cpp -o verify_extremizers` and execute `./verify_extremizers`; run `python3 verify_local.py`. The general infinite-parameter statement rests on the proof, not on finite experiments.

## Relationship to prior work
The classical 1993 work by Durrett and Griffeath formulates Greenberg–Hastings threshold dynamics in excitable media, but does not in its indexed description specify a complete-tree maximal-extinction color count. Gravner, Lyu and Sivakoff (arXiv:1610.07320) analyze three-color dynamics on arbitrary graphs with **one** excited neighbor sufficient for activation, a distinct contact threshold. Bello and Sivakoff (arXiv:2108.06404), Lemma 2.7(ii), prove finite-tree extinction under thresholds at least two. **Their Lemma 4.7 already proves the necessary three lower-layer initial-color restrictions** for any full threshold-branching causal witness, and their proof of Theorem 1.4, at the inequality preceding equation (4.7), multiplies the same per-layer probabilities to obtain an **upper bound** for a given causal subtree. Specializing those necessary conditions to the unique height-\(h\) full subtree in our finite complete graph yields the upper bound on \(M_{b,h}\) of exactly the stated expression, not a novel upper bound. The contribution here is the **converse**: an independent sufficiency lemma showing every permitted coloring, including arbitrary high-level colors and arbitrary parent feedback, actually produces the wave. It proves that the pre-existing upper bound is attained, and supplies the precise if-and-only-if census and sharpness probability for every branching and height. The paper does not state this converse or the finite perfect-tree equality. An earlier *Sharp branching-rank extinction clocks for excitable dynamics on forests* theorem proves the exact maximal time on every forest; it subsumes the \(h+2\) clock here, **which is not presented as new**. The new contribution is the complete if-and-only-if characterization and explicit all-branching count of maximizing **initial** configurations, with its exact rare-tail probability and power law. Published maximal-time counts for finite paths concern a different graph family and do not imply this full-branching count.

## Limitations
The exact extremizer characterization requires a complete regular rooted tree, exactly three states, and a contact threshold equal to the branching factor, with \(b\ge2\). It does not cover incomplete trees, different thresholds, more refractory colors, asynchronous updates, or the full distribution of nonmaximal extinction times. Finite simulation is independent corroboration, not the proof of the all-size formula. Priority searches and targeted full-text inspection do not exclude unindexed equivalent arguments. No independent mathematical audit has been performed.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first posted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (2016-10-24), https://arxiv.org/pdf/1610.07320, especially introduction and Eq. (1).
3. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees*, arXiv:2108.06404 (2021-08-13), https://arxiv.org/pdf/2108.06404, especially Lemmas 2.7(ii) and 4.7 and the inequality preceding Eq. (4.7).
4. *Sharp branching-rank extinction clocks for excitable dynamics on forests*, earlier mathematical manuscript (2026), publication status not verified; establishes sharp times but not counts of maximizing initial colorings.
5. *A square-root law for maximal extinction times in three-state excitation on finite paths*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-square-root-law-for-maximal-extinction-times-in-three-state-ex--2a387c4efac2.
