# Sharp worst-case inverse branching for cyclic Rule 184

## Finding

Let \(T_n\) be elementary cellular automaton Rule 184 on the **indexed** binary cyclic ring of length \(n\geq1\), and let \(d_n(y)=|T_n^{-1}(y)|\) be the number of one-step predecessors of an output configuration \(y\). With Fibonacci numbers \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\) and Lucas numbers \(L_0=2,L_1=1,L_{j+2}=L_{j+1}+L_j\), its exact worst-case inverse branching is

\[
\max_{y\in\{0,1\}^n}d_n(y)=
\begin{cases}
L_{n/2}, & n\text{ even},\\
F_{(n+1)/2}, & n\text{ odd}.
\end{cases}
\]

For \(n\leq3\), every output has exactly one predecessor. For even \(n\geq4\), exactly the two strictly alternating cyclic outputs maximize \(d_n\). For odd \(n\geq5\), precisely the \(2n\) outputs with exactly one cyclic adjacent equal pair maximize \(d_n\); these are the nearly alternating outputs, including either a unique \(00\) pair or a unique \(11\) pair.

More generally, if a nonconstant output is decomposed into alternating positive-length runs
\[
y=0^{a_1}1^{b_1}\cdots0^{a_t}1^{b_t},\qquad a_j,b_j\geq1,
\]
with cyclic indices, define \(s_j\in\{0,1\}\) for the \(01\) junction preceding the run \(1^{b_j}\). Then the *exact* inverse multiplicity is
\[
d_n(y)=\#\bigl\{s\in\{0,1\}^t:\ (b_j=1\land s_j=1)\lor(a_{j+1}=1\land s_{j+1}=1)\text{ for every }j\bigr\}.
\]
For the two constant outputs, \(d_n(y)=1\). This formula also characterizes outputs without predecessors.

## Assumptions and scope

A configuration is a word with fixed coordinate labels \(0,\ldots,n-1\), with indices taken modulo \(n\). The synchronous local map is
\[
(T_nx)_i=(x_{i-1}\wedge\neg x_i)\vee(x_i\wedge x_{i+1}).
\]
It is equivalently the simultaneous swap of all disjoint occurrences of \(10\) into \(01\). The formula counts *distinct full predecessor words*, not trajectories, preimages of finite line blocks, rotation orbits, or independent preimage choices. All displayed assertions quantify over every integer \(n\geq1\).

## Proof

**1. Exact inverse-swap law.** The forward dynamics swaps every input \(10\) junction. Such junctions are disjoint. Given output \(y\), a putative input can therefore be recovered only by selecting some of its \(01\) junctions and reversing each selected \(01\) to \(10\). This gives a one-to-one correspondence between selections and candidate inputs. The selected junctions are pairwise disjoint. In the candidate input, all \(10\) junctions created by a reversal are precisely the selected ones, provided no original output \(10\) junction survives. An original \(10\) is destroyed if and only if at least one adjacent output \(01\) is selected; the adjacent left \(01\) exists exactly when the intervening ones run has length one, and the adjacent right \(01\) exists exactly when the following zeros run has length one. Original \(00\), \(11\), and unselected \(01\) junctions cannot produce any additional \(10\). Thus the selection is a genuine predecessor if and only if all the displayed clauses hold. Every satisfying selection gives a different input. Conservation of the number of ones proves the constant-output case.

**2. Cyclic vertex-cover upper bound.** Every displayed clause implies \(s_j\lor s_{j+1}\). Hence the valid selections are contained in the binary vertex covers of a cyclic \(t\)-vertex graph. Their number is \(L_t\) for \(t\geq1\) (for \(t=1\), the single clause forces its one variable). One can count the covers by transfer matrix \(\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\): its \(t\)-th-power trace is \(L_t\). Consequently \(d_n(y)\leq L_t\). Also \(n=\sum_j(a_j+b_j)\geq2t\), and equality holds precisely for a strictly alternating output.

**3. Even lengths and equality.** Write \(n=2k\), with \(k\geq2\). Then \(t\leq k\). At \(t=k\), every run has length one, every clause is the full disjunction \(s_j\lor s_{j+1}\), and \(d_n(y)=L_k\). Otherwise \(t\leq k-1\) and \(d_n(y)\leq L_t\leq L_{k-1}<L_k\). Hence only the two alternating outputs maximize.

**4. Odd lengths and equality.** Write \(n=2k+1\), with \(k\geq2\). At \(t=k\), the positive run lengths sum to \(2k+1\), so exactly one of the \(2k\) runs has length two and all others length one. Exactly one cyclic clause becomes a unit clause, forcing one junction variable; all remaining clauses are ordinary adjacent-cover clauses. Deleting the forced vertex and its satisfied incident constraints leaves a path of \(k-1\) free vertices, with \(k-2\) path edges, which has \(F_{k+1}\) covers. Conversely every near-alternating target has this structure. There are \(2n\) distinct indexed near-alternating outputs: choose the location of the unique equal neighboring pair (\(n\) choices) and its common bit (two choices).

If \(t\leq k-1\), then \(d_n(y)\leq L_t\leq L_{k-1}<F_{k+1}\) for \(k=2\) and all \(k\geq4\), using \(L_{k-1}=F_k+F_{k-2}\) and \(F_{k+1}=F_k+F_{k-1}\). At \(k=3\) (\(n=7\)), the only numerical tie in the coarse bound is \(t=2\), where \(L_2=F_4=3\). But \(n=7>2t=4\) forces some run length greater than one; therefore at least one cyclic cover clause becomes a unit clause or is impossible, and strictly fewer than the three vertex covers survive. Hence all non-near-alternating outputs are strictly suboptimal.

**5. Small rings.** For \(n=1,2,3\), the map is bijective: constant configurations are fixed, and each nonconstant configuration has either a single particle or a single vacancy, which travels deterministically by one step. All \(2^n\) targets have one predecessor, agreeing with \(F_{(n+1)/2}\) or \(L_{n/2}\) as applicable. This concludes the proof.

## Verification

Three standalone Python 3 scripts are included. Run them from the package directory as `python3 verify_direct.py`, `python3 verify_inverse.py`, and `python3 verify_run_formula.py`. `verify_direct.py` enumerates all binary full states and all inverse fibers through \(n=18\) using the local Rule 184 truth table, checking both maximum values and the exact maximizer sets. `verify_inverse.py` separately models simultaneous disjoint swaps, enumerates inverse swaps and evaluates the clause law for **every** indexed output through \(n=14\). `verify_run_formula.py` implements the cyclic run transfer matrices, tests closed forms through \(n=200\), and tests rotation invariance and upper bounds on sampled cases. Outputs are `DIRECT_VERIFY_OK`, `INVERSE_VERIFY_OK`, and `RUN_FORMULA_VERIFY_OK 200`. The all-length assertions follow from the proof, not from finite enumeration.

## Relationship to prior work

Jen (1989) gives generic finite-block preimage recurrences and discusses maximization of one-step probabilities for several elementary rules, including examples for Rules 12, 76, and 126, but the inspected material does not optimize full-ring Rule 184 predecessors. Fukś (1997) and Fukś (1999) derive block-preimage formulas and traffic-flow results for Rule 184 or closely related deterministic traffic cellular automata, but the checked propositions do not optimize one-step **full-ring** inverse multiplicity over outputs. Evans, Rajewsky and Speer (1998) analyze an open-boundary, probabilistic parallel-update traffic process, not the stated cyclic one-step inverse maximum. Powley (2009), especially Chapter 4 and Section 9.3, gives the general de Bruijn transfer-matrix method for counting predecessors of arbitrary periodic configurations. That method can compute \(d_n(y)\) for a specified \(y\), and is prior broad computational coverage; it does **not**, in the material inspected, identify the sharp Fibonacci–Lucas maximum for every ring size or classify all maximizing targets. The pointwise inversion step is not claimed as a new general technique. The specific contribution is the all-output extremal theorem and equality classification.

## Limitations

This result concerns one **synchronous** Rule 184 step on fixed-coordinate binary rings. It does not address noisy observations, multistep ancestors, open boundaries, asynchronous traffic updates, other elementary rules, or complete inverse-fiber distributions. Similarities to classical Fibonacci/Lucas vertex-cover counts are explicitly part of the proof; historical priority for the optimized extremal statement has not received an external independent audit. Generic matrix-based predecessor computations and unpublished small-ring tables remain possible prior coverage.

## References

- E. Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems 3 (1989), 421–456, especially Sections 3 and 5.4, https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf.
- H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules* (1997), arXiv:comp-gas/9703001, https://arxiv.org/abs/comp-gas/9703001.
- H. Fukś, *Exact results for deterministic cellular automata traffic models* (1999), arXiv:comp-gas/9902001, https://arxiv.org/abs/comp-gas/9902001.
- M. R. Evans, N. Rajewsky, and E. R. Speer, *Exact solution of a cellular automaton for traffic* (1998), arXiv:cond-mat/9810306, https://arxiv.org/abs/cond-mat/9810306.
- E. J. Powley, *Global properties of cellular automata*, University of York PhD thesis (October 2009), especially Chapter 4 and Section 9.3, https://www.cs.york.ac.uk/nature/group/theses/EdPowley.pdf.
