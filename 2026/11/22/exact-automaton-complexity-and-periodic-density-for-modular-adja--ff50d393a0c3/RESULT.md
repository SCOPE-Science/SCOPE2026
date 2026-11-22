# Exact automaton complexity and periodic density for modular adjacent-pair monitors

## Finding

For any integers \(q\ge 2\) and \(m\ge 2\), take the alphabet \(\Sigma=\{0,1,\ldots,q-1\}\). For a word \(w=w_1\cdots w_n\), let \(N_{ab}(w)=|\{i:1\le i<n,\ (w_i,w_{i+1})=(a,b)\}|\), allowing overlapping contiguous occurrences. Define \(L_{q,m}\) to consist of all nonempty words starting and ending in \(0\) and satisfying \(N_{ab}(w)\equiv0\pmod m\) for every ordered pair \((a,b)\in\Sigma^2\), including pairs of equal letters.

**Theorem.** Put \(d=q^2-q+1\). The minimal complete deterministic finite automaton for \(L_{q,m}\) has exactly
\[
\boxed{q m^d+2}
\]
states. For a uniformly sampled word \(W_n\) from \(\Sigma^n\), its acceptance probability is exactly zero unless \(n\equiv1\pmod m\), and
\[
\lim_{\substack{n\to\infty\\ n\equiv1\pmod m}}\Pr(W_n\in L_{q,m})=\frac{1}{q^2m^{d-1}}.
\]
Both assertions hold for composite as well as prime moduli.

## Assumptions and scope

The alphabet is ordered only to identify the distinguished base symbol \(0\); relabeling the alphabet along with the distinguished symbol leaves the conclusions unchanged. The empty word is rejected. A one-symbol word \(0\) is accepted. Input is read left to right, and automata are complete (a rejecting sink is counted). The test uses simultaneous residues of **all** contiguous bigrams, not scattered length-two subsequences and not merely the number of distinct bigrams.

Regard the complete directed graph with loops on \(\Sigma\) as having edge set \(E=\Sigma\times\Sigma\), one edge \(a\to b\) for every pair. Write \(e_{ab}\) for its standard edge basis, and write \(\partial e_{ab}=e_a-e_b\) in the vertex module. All modular vectors below are in \((\mathbb Z/m\mathbb Z)^E\), except when explicitly identified as integer lifts.

## Proof

**1. Modular path realization.** For arbitrary vertices \(s,t\in\Sigma\) and vector \(r\in(\mathbb Z/m\mathbb Z)^E\), there is a directed walk starting at \(s\), ending at \(t\), and using edge \(ab\) a number of times congruent to \(r_{ab}\pmod m\), if and only if
\[
\partial r=e_s-e_t\pmod m.
\]
Necessity is telescoping. For sufficiency, choose the representatives \(c_{ab}\in\{0,\ldots,m-1\}\). The vector \(b=(e_s-e_t-\partial c)/m\) is integral and has coordinate sum zero. Because the graph has every directed edge, route nonnegative integral flows from the vertices with positive coordinates of \(b\) to those with negative coordinates; this gives \(z\in\mathbb N^E\) with \(\partial z=b\). Then \(c+mz\) has the desired residues and exact boundary \(e_s-e_t\). Adding \(m\) copies of *each* directed edge preserves both boundary and residues, and makes the supporting directed multigraph strongly connected. The Euler-trail criterion produces a walk from \(s\) to \(t\) traversing precisely these edges. The criterion also handles \(s=t\) (an Euler circuit) and all composite moduli.

**2. Counting reachable counting states.** After the compulsory initial input symbol \(0\), use states \((s,r)\), where \(s\) is the most recent letter and \(r\) the vector of bigram counts modulo \(m\). The transition on input \(a\) is
\[
(s,r)\xrightarrow{a}(a,r+e_{sa}).
\]
For a prefix starting with \(0\), telescoping gives \(\partial r=e_0-e_s\). Conversely, by Step 1 each such modular vector is realizable by a walk starting at \(0\), so all these states are reachable. The incidence homomorphism \(\partial:(\mathbb Z/m\mathbb Z)^E\to\{b\in(\mathbb Z/m\mathbb Z)^{\Sigma}:\sum b_a=0\}\) is onto: edges from \(0\) to other vertices generate its target. Its kernel has size \(m^{|E|-(q-1)}=m^d\). Each endpoint \(s\) consequently has exactly \(m^d\) accessible residue states, for \(qm^d\) in total. Add an initial state (rejecting the empty word) which accepts a first \(0\) and rejects any other first letter, and a permanent rejecting sink. Only \((0,0)\) is an accepting counting state. This gives a complete \(qm^d+2\)-state automaton.

**3. Myhill–Nerode minimality.** For each counting state \((s,r)\) and any prescribed first continuation letter \(a\), Step 1 applied to the target residual \(-r-e_{sa}\), with endpoints \(a\) and \(0\), yields an accepting continuation beginning with \(a\). Thus every counting state has a nonempty right language, including a word beginning with any desired letter.

Two counting states \((s,r)\) and \((s,r')\) with the same endpoint but different residues are distinguished by any suffix accepted from the first: the added edge-count vector is identical for both, so the second ends with nonzero total residues. Now suppose \(s\ne t\) and the right languages of \((s,r)\) and \((t,r')\) were identical. For each \(a\in\Sigma\), choose a suffix starting with \(a\) that is accepted from \((s,r)\). The only difference in edge counts when this suffix is run from \(t\) instead of \(s\) is \(e_{ta}-e_{sa}\). Equivalence would force
\[
r'-r=e_{sa}-e_{ta}\pmod m
\]
for every \(a\). These right-hand vectors differ as \(a\) varies, since \(q,m\ge2\) and different first letters use disjoint edge-coordinate columns. This is impossible. The initial state is distinct from each counting state because it rejects all words beginning with a symbol other than \(0\), while every counting state admits some accepting such continuation. It is distinct from the sink because \(0\) is accepted from the initial state. The sink is distinct from every counting state because the latter have accepting continuations. Hence all \(qm^d+2\) states are inequivalent.

**4. Periodic limiting acceptance density.** Restrict to the \(qm^d\) counting states. Their letter-transition graph is strongly connected: for any \((s,r)\) and \((t,r')\), the difference \(r'-r\) has boundary \(e_s-e_t\), and Step 1 constructs an input walk realizing it. Each state has exactly \(q\) outgoing transitions and exactly \(q\) incoming transitions, one for every possible predecessor endpoint (with uniquely determined preceding residue). Thus the uniform distribution is stationary under independent uniform input letters.

Every transition increases the sum \(\sum_{ab}r_{ab}\pmod m\) by one; every directed cycle therefore has length divisible by \(m\). A cycle of length \(m\) exists at \((0,0)\), obtained by repeating symbol \(0\) exactly \(m\) times. The irreducible finite Markov chain has period exactly \(m\). Its cyclic classes are the fibers of the total-residue sum. They all have size \(qm^{d-1}\): on every fixed-endpoint affine incidence fiber, adding a unit of the loop coordinate \(r_{00}\) cycles through all possible total residues without affecting boundary. By periodic finite-state Markov convergence, after \(n-1\) inputs from \((0,0)\) with \(n-1\equiv0\pmod m\), the probability of state \((0,0)\) tends to \((qm^{d-1})^{-1}\). The first input of the original word must be \(0\), an independent event of probability \(1/q\), giving the claimed limit. For other length residues, the total number \(n-1\) of adjacent pairs is not a multiple of \(m\), so acceptance is impossible.

## Verification

Two independent finite-state programs accompany this result. Run `python3 verify_bfs.py` for reachable-state breadth-first construction, right-language refinement, and direct short-word acceptance oracles. Run `g++ -O2 -std=c++17 verify_residue.cpp -o verify_residue && ./verify_residue` for an independently enumerated modular-incidence state space and separate partition refinement. The programs agree at \((q,m)=(2,2),(2,3),(2,4),(3,2)\), obtaining minimal sizes \(18,56,130,386\), respectively. Exact-length dynamic programming for \((q,m)=(2,2)\) illustrates convergence along odd lengths to \(1/16\). Machine outputs are included separately. These bounded checks are not used as a substitute for Steps 1–4, which apply to all admissible parameters and word lengths.

## Relationship to prior work

The base motivation is the study of factor frequencies and modular prefix statistics in recent work. Bell, Burnett, and Schulz (2026) study frequencies of finite factors of infinite words via Rauzy graphs. Puzynina and Schavelev (2026) study modular distributions of prefix *letter* Parikh vectors preceding factors. Karhumäki, Saarela, and Zamboni (2013) develop \(k\)-abelian equivalence based on complete length-at-most-\(k\) factor counts; in particular, their Lemma 2.3 describes endpoint data implicit in length-two counts. None of the inspected statements directly establishes the minimum DFA size for the anchored modular bigram language or its length-dependent density. The proof here adds a modular Euler-trail realization, a full residual-state separation, and a periodic Markov-chain analysis. Results about *scattered* pair counts do not imply the contiguous-edge statement, since the underlying counts and update laws differ.

## Limitations

This theorem concerns the complete directed length-two factor graph, one distinguished start/end symbol, all ordered pairs, and a uniform common modulus. It does not determine state complexity for a proper subset of pair constraints, non-complete allowed-transition graphs, longer contiguous factors, or nonuniform moduli. The density statement is a limit along a residue class, not a finite-length exact counting formula. Although extensive source comparisons were made, unindexed equivalent previous results remain a publication-priority risk. No independent mathematical audit has been performed.

## References

1. J. Bell, L. Burnett, and C. Schulz, *Frequencies of subwords in words of linear subword complexity*, arXiv:2607.28273, originally public July 30, 2026. https://arxiv.org/abs/2607.28273
2. S. Puzynina and V. Schavelev, *WELLDOC property for words generated by morphisms*, arXiv:2603.08492, originally public March 9, 2026. https://arxiv.org/abs/2603.08492
3. J. Karhumäki, A. Saarela, and L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104, originally public January 22, 2013. https://arxiv.org/abs/1301.5104
