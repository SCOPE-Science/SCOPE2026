# Exact threshold phases and source-set census for discounted hitting domination on cycles

## Finding

Fix any integer \(n\ge3\), discount \(0<\lambda<1\), and coverage requirement \(0<\tau\le1\). For each nonempty \(S\subseteq V(C_n)\), let \(T_S\) denote first hitting time of \(S\) by simple random walk from a specified starting vertex and write \(h_v^S=\mathbb E_v[\lambda^{T_S}]\). Define the labelled source-set polynomial \(F_{n,\lambda,\tau}(z)=\sum_{S:\min_v h_v^S\ge\tau}z^{|S|}\).

Let \(\theta=\operatorname{arcosh}(1/\lambda)>0\), and for each positive integer \(\ell\) put
\[
\phi_\ell=\frac{\cosh(\theta (\ell\bmod 2)/2)}{\cosh(\theta\ell/2)}.
\]
Let \(L=\max\{\ell\ge1:\phi_\ell\ge\tau\}\) and \(L_n=\min\{n,L\}\). Then \(L\) exists, is finite and positive. **Exactly** the source sets whose successive cyclic source gaps have at most \(L\) edges are feasible. In particular
\[
F_{n,\lambda,\tau}(z)=\sum_{k=1}^{n}\frac{n}{k}[t^n](t+t^2+\cdots+t^{L_n})^k z^k,
\]
\[
\delta_{\lambda,\tau}(C_n)=\left\lceil\frac{n}{L_n}\right\rceil,
\qquad
\#\{S:\lvert S\rvert=\delta_{\lambda,\tau}(C_n),\ \min_vh_v^S\ge\tau\}=\frac{n}{\delta_{\lambda,\tau}(C_n)}[t^n](t+\cdots+t^{L_n})^{\delta_{\lambda,\tau}(C_n)}.
\]
These are labelled subsets, not dihedral orbits. Equality at a threshold is feasible.

The length threshold may equivalently be obtained without testing infinitely many lengths. Set \(A=\operatorname{arcosh}(1/\tau)/\theta\) and \(B=\operatorname{arcosh}(\cosh(\theta/2)/\tau)/\theta\). Then
\[
L=\max\left\{2\lfloor A\rfloor,\ 2\left\lfloor B-\frac12\right\rfloor+1\right\}.
\]
For \(\lambda=1/2\), the first gaps have thresholds \(\phi_1=1\), \(\phi_2=1/2\), \(\phi_3=1/3\), \(\phi_4=1/7\). Hence at \(n=10\), \(\tau=1/3\) there are 25 minimum four-source sets, whereas immediately above \(1/3\) (up to and including \(1/2\)) there are two minimum five-source sets.

## Assumptions and scope

The graph is the simple undirected labelled \(n\)-cycle; the walk moves to either neighbor with probability \(1/2\). Every vertex in \(S\) is held at support one, and \(T_S=0\) there. The discount and threshold are homogeneous, with \(0<\lambda<1\) and \(0<\tau\le1\). Source sets are nonempty. Source gaps are positive numbers of cycle edges and sum to \(n\). For one source, its unique gap is \(n\). No asymptotic approximation or generic-position assumption is imposed.

## Proof

For a fixed nonempty \(S\), first-step conditioning gives \(h_v^S=1\) on \(S\), and on each remaining vertex
\[
h_v^S=\frac\lambda2(h_{v-1}^S+h_{v+1}^S).
\]
The linear system has a unique solution: the coefficient operator is a strict contraction on bounded functions away from prescribed boundary values because \(\lambda<1\). Successive sources split the complement into independent open intervals: on a cyclic gap of length \(\ell\), index its vertices \(0,1,\ldots,\ell\), with the endpoint values both one (even if the endpoints represent the same source). The unique recurrence solution is
\[
h_i=\frac{\cosh(\theta(i-\ell/2))}{\cosh(\theta\ell/2)},\qquad \cosh\theta=1/\lambda.
\]
Indeed, the endpoints are one and the hyperbolic addition formula implies \(h_{i-1}+h_{i+1}=2\cosh\theta\,h_i=2h_i/\lambda\). The smallest support on the gap occurs at the central integer vertex or two central vertices; its value is exactly \(\phi_\ell\). This includes \(\ell=1\), where no non-source vertex lies in the gap and the endpoints have value one.

For consecutive gap lengths, \(\phi_{2r}=1/\cosh(r\theta)\) and \(\phi_{2r+1}=\cosh(\theta/2)/\cosh((r+1/2)\theta)\). For \(r\ge1\), strict monotonicity follows from \(\cosh((r+1/2)\theta)>\cosh(r\theta)\cosh(\theta/2)\), and \(\cosh((r+1)\theta)>\cosh((r+1/2)\theta)/\cosh(\theta/2)\); also \(\phi_1>\phi_2\). Thus the sequence starts at one, strictly decreases to zero, and a gap meets the floor precisely when its length does not exceed \(L\). Solving the two parity inequalities gives the displayed floor formula for \(L\).

A feasible \(k\)-source set consequently corresponds to a cyclic composition of \(n\) into \(k\) positive parts at most \(L_n\). Choosing a distinguished source vertex and reading the successive gaps produces \(n[t^n](t+\cdots+t^{L_n})^k\) ordered marked descriptions. Each unmarked set has exactly \(k\) possible distinguished sources, giving the coefficient \(n/k\) times the composition count. The minimum feasible \(k\) obeys \(kL_n\ge n\), so \(k\ge\lceil n/L_n\rceil\). Conversely this bound is attained by choosing a composition of \(n\) into that many positive parts at most \(L_n\) (distribute the remaining edges among the parts), and placing sources at its breakpoints. This proves the full polynomial, optimum and exact multiplicity. The numerical example follows by counting the compositions of ten into four parts bounded by three (ten such compositions) and into five parts bounded by two (one such composition).

## Verification

Run `python3 verify.py` using only the Python standard library. The verifier, independently of the hyperbolic gap solution, solves the original discounted random-walk Dirichlet equations on each cycle by exact rational Gaussian elimination. It exhaustively checks every nonempty labelled source set for all orders \(3\le n\le9\), across three discounts and multiple rational thresholds including exact phase boundaries. It compares the direct graph feasibility test with the gap rule and every coefficient with the bounded-composition formula. It additionally checks the ten-vertex threshold example. The actual replay yielded `INDEPENDENT_EXACT_GAUSSIAN_AND_GAP_COUNTS_OK 205 parameter_cases n=3..9` followed by `VERIFY_OK`.

## Relationship to prior work

Allagan, Pereyra, and Massey (arXiv:2609.31535, first submitted September 25, 2026) introduce and study discounted hitting domination, including general complexity, an exact mixed-integer formulation and a spider-tree algorithm. The cycle is not a spider (except no nontrivial cycle), and the present result identifies the complete cyclic, labelled, all-parameter source-set distribution and explicit transition endpoints. The classical discounted hitting equations are standard and are not claimed as novel by themselves. A different existing special-family result concerns wheel graphs, in which the universal hub changes the random-walk recurrence; that result does not imply this unweighted cycle formula by deleting a vertex or adjusting a parameter. No claim of priority is made for unexamined sources.

## Limitations

The result is specific to homogeneous simple random walks on labelled unweighted cycles. It does not cover asymmetric, weighted or vertex-dependent discount models, general graphs, trees, or cycle-with-hub transitions. The result gives a complete mathematical proof, but exhaustive computational checks are finite and independent human verification has not been performed. The original preprint PDF was not accessible during the literature comparison; a detailed public synopsis and original abstract were inspected, so historical priority remains provisional.

## References

- J. D. Allagan, K. Pereyra, W. A. Massey, *Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms*, arXiv:2609.31535 (first posted 2026-09-25), https://arxiv.org/abs/2609.31535.
- Author-paper synopsis and method synopsis, https://www.alphaxiv.org/abs/2609.31535 (accessed 2026-11-03 UTC).
