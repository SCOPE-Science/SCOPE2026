# Exact parity-split Ising frustration on Mycielski cycle graphs

## Finding
For each integer \(n\ge4\), let \(G_n=\mu(C_n)\) be the Mycielskian of the simple cycle of length \(n\). Put classical spins \(s_z\in\{-1,1\}\) at its \(2n+1\) vertices and antiferromagnetic coupling \(J>0\) on every edge, with zero external field. For the Hamiltonian
\[
H(s)=J\sum_{\{z,z'\}\in E(G_n)}s_zs_{z'},
\]
the ground-state energy and number of labeled ground configurations are exactly
\[
\frac{E_0(n)}J=\begin{cases}-3n,&n\text{ even},\\-3(n-1),&n\text{ odd},\end{cases}
\qquad
 g(n)=\begin{cases}4,&n\text{ even},\\2n,&n\text{ odd}.\end{cases}
\]
Every ground state has total spin \(M=\sum_{z\in V(G_n)}s_z\in\{-1,+1\}\), and precisely half of the ground states have each sign. Equivalently, the minimum number of unsatisfied (equal-spin) edges is \(n/2\) for even \(n\) and \((n+3)/2\) for odd \(n\), while the maximum-cut sizes are \(7n/2\) and \((7n-3)/2\), respectively.

For odd \(n\ge5\), the underlying graph is triangle-free and four-chromatic; its exact Ising degeneracy grows only linearly, with a single movable domain-wall defect. For even \(n\), the graph is triangle-free and three-chromatic and has only four ground states.

## Assumptions and scope
The graph has cycle vertices \(v_i\), their shadows \(u_i\), and apex \(w\), with indices modulo \(n\) and exactly the edges \(\{v_i,v_{i+1}\}\), \(\{u_i,v_{i-1}\}\), \(\{u_i,v_{i+1}\}\), and \(\{w,u_i\}\) for all \(i\). There are \(4n\) edges, each counted once. Spins are classical Ising variables; no field, disorder, boundary terms, dynamics, or quantum correction is present. The simple-cycle condition \(n\ge4\) excludes the exceptional triangle \(C_3\).

## Proof
**Step 1: eliminate the shadow spins exactly.** Fix the apex spin \(\eta=s_w\) and original cycle spins \(\sigma_i=s_{v_i}\). Each shadow spin \(\tau_i=s_{u_i}\) appears only as
\[
J\tau_i(\sigma_{i-1}+\sigma_{i+1}+\eta).
\]
The coefficient is a sum of three signs, hence never zero. Its minimizing choice is unique: \(\tau_i=-\operatorname{sgn}(\sigma_{i-1}+\sigma_{i+1}+\eta)\). Define \(x_i=(1+\eta\sigma_i)/2\in\{0,1\}\). Let \(B=\sum_i\mathbf1_{x_i\ne x_{i+1}}\) and \(T=\sum_i x_ix_{i+2}\). The cycle contributes \(n-2B\), and the minimized shadow/apex terms contribute \(-n-2T\), so
\[
\min_{(\tau_i)}H/J=-2(B+T).
\]
It remains to maximize \(F=B+T\) among cyclic binary words of length \(n\), with an independent overall factor of two for the apex sign.

**Step 2: an exact cyclic-word inequality.** Set
\[
k=\sum_i x_i,\quad C_1=\sum_i x_ix_{i+1},\quad C_2=\sum_i x_ix_{i+2},\quad D_2=k-C_2.
\]
By expanding the number of boundaries, \(B=2k-2C_1\), hence
\[
F=3k-2C_1-D_2.
\]
Both \(C_1,D_2\) are nonnegative. If \(k>n/2\), then \(C_1\ge2k-n\): the \(n-k\) zero positions can separate at most \(n-k\) runs of ones, so at least \(k-(n-k)\) pairs of adjacent ones remain.

For even \(n\), if \(k\le n/2\), the inequality gives \(F\le3k\le3n/2\). Equality forces \(k=n/2\) and \(C_1=0\), i.e., the two perfectly alternating cyclic words, each having \(D_2=0\). If \(k>n/2\), then \(F\le2n-k<3n/2\). Therefore \(\max F=3n/2\), with exactly two binary maximizers for each apex sign.

For odd \(n\ge5\), whenever \(0<k<n\), one has \(D_2\ge1\): otherwise the ones would be invariant under the step-two cyclic shift, which is transitive because \(n\) is odd, forcing either all zeros or all ones. If \(k\le(n-1)/2\), then \(F\le3k-1<3(n-1)/2\). If \((n+1)/2\le k<n\), then
\[
F\le2n-k-1\le\frac{3(n-1)}2,
\]
with equality only when \(k=(n+1)/2\), \(C_1=1\), and \(D_2=1\). These conditions are achieved by the cyclic words that alternate except for exactly one adjacent \(11\) pair. There are precisely \(n\) such words, obtained by placing that pair in any of the \(n\) cyclic positions. The words with \(k=0\) or \(k=n\) give \(F=0\) or \(F=n\), both strictly below \(3(n-1)/2\) for \(n\ge5\). Thus \(\max F=3(n-1)/2\) and there are exactly \(n\) binary maximizers for each apex sign.

**Step 3: count spins, magnetizations, and frustrated bonds.** Each maximizing cyclic word and apex sign uniquely determines all shadow spins, proving the energy and degeneracy formulas. For even \(n\), in each alternating word with apex \(+1\), the original cycle and shadow magnetizations both vanish, leaving \(M=+1\). For odd \(n\), with apex \(+1\), the original cycle has sum \(+1\); exactly \((n-3)/2\) shadows are positive, so the shadow sum is \(-3\), leaving \(M=-1\). Global spin reversal pairs every ground state with one of opposite magnetization. Finally, \(|E(G_n)|=4n\) and \(H/J=2N_{\mathrm{unsat}}-4n\), giving the frustration indices and maximum cuts stated above. This proves the result for every integer \(n\ge4\).

## Verification
The standalone file `verify_direct.cpp` directly enumerates every spin configuration of the **physical graph**, independently of the elimination argument, for each \(4\le n\le11\). It confirms minimum energy, total degeneracy, and the complete \(M=\pm1\) magnetization counts. Compile and run using `g++ -O3 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct`.

The independent file `verify_transfer.py` uses a four-state max-plus recursion on cyclic binary words to compute ground-state energies and degeneracies for every \(4\le n\le201\). Run with `python3 verify_transfer.py`. Both programs completed all specified assertions. These are finite checks, not substitutes for the all-\(n\) proof above.

## Relationship to prior work
Mycielski introduced the graph operation that preserves triangle-freeness while increasing chromatic number [1]; Rudnicki and Stewart formally analyzed its graph-theoretic properties [2]. The earlier antiferromagnetic Ising study of Mostovoy and collaborators [3] uses domain-wall and frustration language on the **two-dimensional triangular lattice**, not Mycielskian cycles. A previously available exact three-state Potts field classification for the **single** Grötzsch graph \(\mu(C_5)\) already implies the \(n=5\), two-state zero-field instance; that instance is not claimed as a separate discovery. Neither that finite special case nor the inspected general graph-construction literature implies the all-length parity classification and exact state multiplicities given here. The unrestricted nearest-neighbor Ising-to-maximum-cut equivalence is classical; the new content is its evaluated, multiplicity-resolved form on this particular infinite graph family.

## Limitations
The result is limited to uniform positive coupling and zero field on the specified finite graphs. No claim is made about finite temperature, stability against perturbations, dynamical relaxation, quantum spins, or any phase transition in an infinite physical lattice. The zero-temperature entropy per site tends to zero because \(g(n)\) is at most linear. The historical-priority comparison cannot eliminate unidentified earlier max-cut tables or unindexed equivalent formulations. A copy of Mycielski's original 1955 full text was not accessible in this examination; its verified bibliographic record and later formalization support the graph definition, not any assertion about previously solved Ising energies.

## References
[1] J. Mycielski, “Sur le coloriage des graphes,” *Colloquium Mathematicum* **3** (1955), 161–162. https://doi.org/10.4064/cm-3-2-161-162

[2] P. Rudnicki and L. Stewart, “The Mycielskian of a Graph,” *Formalized Mathematics* **19** (2011), 27–34. https://doi.org/10.2478/v10037-011-0005-6

[3] M. Mostovoy, N. Prokof'ev, D. Khomskii, and J. Knoester, “Frustrated spin model as a hard-sphere liquid,” first submitted publicly October 31, 2002, arXiv:cond-mat/0210711. https://arxiv.org/abs/cond-mat/0210711
