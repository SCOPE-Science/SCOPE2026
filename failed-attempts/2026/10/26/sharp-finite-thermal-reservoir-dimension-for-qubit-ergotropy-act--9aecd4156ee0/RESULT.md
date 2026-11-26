# Sharp finite thermal-reservoir dimension for qubit ergotropy activation

## Finding

For a passive, energy-incoherent qubit coupled by an arbitrary energy-preserving unitary to a Gibbs reservoir with exactly \(d\) equally spaced, nondegenerate levels, the maximal achievable excitation and ergotropy admit exact closed formulas. The finite reservoir activates positive ergotropy for some passive qubit input exactly when \(d\ge3\) and \(q=e^{-\beta\Delta}>q_d\), where \(q_d\) is the unique solution in \((1/2,1)\) of
\[
\sum_{k=1}^{d-1}q_d^k=1.
\]
Consequently, for each \(1/2<q<1\), the smallest permitted reservoir dimension is
\[
\boxed{d_{\min}(q)=1+\left\lfloor\frac{\log(2q-1)}{\log q}\right\rfloor.}
\]
At \(q=1\) the minimum is \(3\); at \(0<q\le1/2\), no finite dimension suffices. The sharp activation threshold satisfies
\[
q_d=\frac12+2^{-d-1}+O(d4^{-d}),\qquad
-\log q_d=\log2-2^{-d}+O(d4^{-d}).
\]
These statements concern only the specified finite, single-ladder reservoir and passive diagonal qubit inputs, not every possible reservoir spectrum or arbitrary coherent inputs.

## Assumptions and scope

Fix \(\Delta>0\), an integer \(d\ge2\), and inverse temperature \(\beta\ge0\). The system Hamiltonian is \(H_S=\Delta|e\rangle\langle e|\), and the environment has \(H_B=\Delta\sum_{k=0}^{d-1}k|k\rangle\langle k|\). Write \(q=e^{-\beta\Delta}\in(0,1]\), \(Z_d=\sum_{k=0}^{d-1}q^k\), and \(w_k=q^k/Z_d\). The bath starts in \(\gamma_B=\sum_k w_k|k\rangle\langle k|\); the system starts in the passive state \(\rho_S=p|g\rangle\langle g|+(1-p)|e\rangle\langle e|\) with \(1/2\le p\le1\). All joint unitaries \(U\) satisfying \([U,H_S\otimes I+I\otimes H_B]=0\) are admissible. There is no additional work storage system, coherence catalyst, intermediate bath resetting, or ancillary Hilbert space. Ergotropy denotes the system's maximum cyclic-unitary extractable work after tracing out the bath.

For every admissible \((d,q,p)\), the exact supremum of the final excited population is the attained value
\[
E_d(p,q)=(1-p)w_{d-1}+\sum_{k=1}^{d-1}\max\bigl\{p w_k,(1-p)w_{k-1}\bigr\}.
\]
Equivalently,
\[
E_d(p,q)=\begin{cases}
1-p,&pq\le1-p,\\
p(1-w_0)+(1-p)w_{d-1},&pq>1-p.
\end{cases}
\]
Every allowed output qubit remains diagonal. Therefore the exact maximum final ergotropy is
\[
\boxed{\mathcal W_{\max}(d,q,p)=\Delta\,[2E_d(p,q)-1]_+,}
\]
where \([z]_+=\max\{z,0\}\). In the second branch, simultaneously exchanging \(|g,k\rangle\) and \(|e,k-1\rangle\) in every nontrivial energy sector attains the maximum; in the first branch, the identity attains it. At equality both choices are optimal.

For \(d\ge3\), \(q>q_d\), define
\[
p_{\mathrm{crit}}(d,q)=\frac{1/2-w_{d-1}}{1-w_0-w_{d-1}}.
\]
Then \(\mathcal W_{\max}>0\) exactly for \(p>p_{\mathrm{crit}}\); the critical population satisfies \(1/2\le p_{\mathrm{crit}}<1\). For \(d=2\) or \(q\le q_d\), no passive input acquires positive ergotropy. For fixed \(1/2<q<1\), the explicit minimum dimension above is an exact threshold for the *existence of some passive initial qubit input*, not a claim that every passive input works.

## Proof

**Energy-sector extremality.** The total-energy eigenspaces at energies \(0\) and \(d\Delta\) are respectively \(\operatorname{span}\{|g,0\rangle\}\) and \(\operatorname{span}\{|e,d-1\rangle\}\). For each \(1\le k\le d-1\), the sector at \(k\Delta\) is exactly \(\operatorname{span}\{|g,k\rangle,|e,k-1\rangle\}\), initially diagonal with entries \(a_k=pw_k\) and \(b_k=(1-p)w_{k-1}\). The excited-state population contributed by this sector is a diagonal matrix element of \(V_k\operatorname{diag}(a_k,b_k)V_k^\dagger\) for a two-dimensional unitary \(V_k\), which ranges over \([\min(a_k,b_k),\max(a_k,b_k)]\). All sectors admit independent unitary choices. The upper end is attained by a swap if \(a_k>b_k\) and the identity otherwise; the isolated upper sector contributes \((1-p)w_{d-1}\). Summing proves the exact \(E_d\) expression. Because \(a_k/b_k=pq/(1-p)\) is independent of \(k\) (with the obvious endpoint convention when \(p=1\)), all interior sectors make the same choice, yielding the displayed piecewise formula.

**Diagonal reduced output.** The product input commutes with total energy, as does its conjugate by every allowed \(U\). Its partial trace commutes with \(H_S\), since partial trace is covariant under simultaneous system and bath time translations. The nondegenerate qubit energy levels therefore have no output coherence. A diagonal qubit whose excited population is \(r\) has ergotropy \(\Delta[2r-1]_+\); this expression is nondecreasing in \(r\). Thus maximizing the population also maximizes the ergotropy, including its zero region.

**Dimension and input thresholds.** The maximal excited population is a convex, piecewise-affine function of \(p\), the pointwise maximum of the constant-input branches; in particular its maximum over \(p\in[1/2,1]\) occurs at an endpoint. At \(p=1/2\), both the identity and swap branches yield no excited population above \(1/2\). The only possible activating endpoint is \(p=1\), where \(E_d(1,q)=1-w_0\). Hence activation for some passive input is equivalent to \(w_0<1/2\), or \(\sum_{k=1}^{d-1}q^k>1\). For \(d=2\) this is impossible at \(q\le1\); for \(d\ge3\), the sum is strictly increasing in \(q\), below one at \(q=1/2\) and above one at \(q=1\). This yields the unique \(q_d\) and the exact phase boundary. Solving \(E_d(p,q)>1/2\) in the swap branch produces \(p>p_{\mathrm{crit}}\). That inequality automatically places \(p\) within the swap branch: if it did not, the attainable population would be \(1-p\le1/2\).

For \(0<q<1\), the geometric-sum threshold is \(q(1-q^{d-1})/(1-q)>1\), exactly \(q^d<2q-1\). This inequality is impossible for \(q\le1/2\) and equivalent, when \(q>1/2\), to \(d>\log(2q-1)/\log q\), because \(\log q<0\). This gives the integer minimum. At \(q=1\), the sum equals \(d-1\), so activation begins at \(d=3\).

Finally \(q_d\) solves \(q_d^d=2q_d-1\). Writing \(q_d=1/2+\delta_d\), the equation \(2\delta_d=2^{-d}(1+2\delta_d)^d\) first gives \(\delta_d=O(2^{-d})\) for sufficiently large \(d\), by monotonicity and bounding the root between \(1/2\) and \(1/2+C2^{-d}\). Expanding the right side then gives \(\delta_d=2^{-d-1}+O(d4^{-d})\), and Taylor expansion of \(-\log(1/2+\delta_d)\) gives the stated inverse-temperature asymptotic. The roots strictly decrease with \(d\) since adding the next positive monomial increases the defining sum.

**Exact finite-cutoff discrepancy.** When \(0<q<1\) and \(pq>1-p\), the ideal infinite-ladder single-mode \(\beta\)-swap excites the qubit with probability \(pq\). Direct substitution of \(Z_d=(1-q^d)/(1-q)\) yields
\[
\boxed{pq-E_d(p,q)=\frac{(1-q)[p(1+q)-1]q^{d-1}}{1-q^d}.}
\]
The numerator is strictly positive in the stated swap regime, proving a quantitative, exponentially small but nonzero finite-reservoir truncation penalty. This last identity does not assert that the infinite-bath \(\beta\)-swap is new.

## Verification

The standalone `check_ladder.py` enumerates energy-preserving two-dimensional sector rotations for finite dimensions, constructs normalized joint states and verifies commutation with the total Hamiltonian and the absence of reduced coherence. It checks the predicted exact extrema against explicit matrices, samples intermediate controls, verifies threshold roots and minimal dimensions, and tests asymptotics. Running `python check_ladder.py` with NumPy produced `PASS 1484 standalone assertions`. These finite checks support, but do not replace, the universal sector proof. The code is included in the finding package with its dependency specification.

## Relationship to prior work

Singh, Saha and Sen (2026) establish that passive-qubit ergotropy injection is impossible for a thermal qubit environment and exhibit a three-level thermal environment that can inject it. Their equispaced three-level case has the same first nontrivial threshold \(q_3=(\sqrt5-1)/2\). The present theorem takes those results as boundary cases and determines the optimal output, exact existence threshold and minimal required bath dimension for every finite equispaced ladder and every passive diagonal qubit input. This is a finite-resource classification, not a claim that the three-level example itself is new.

Hu (2018) gives the more general *infinite*-single-mode bosonic-bath reachable qubit states and the \(\beta\)-swap bound; it already implies a global population upper bound \(pq\) in the swap regime. That bound does not supply the fixed finite-reservoir optimum \(E_d\), the minimum \(d\) as a function of temperature, or the finite-cutoff error. Results about arbitrary thermodynamic reservoirs or coherent/catalytic resources do not automatically transfer to the constrained single finite ladder used here. An unidentified stronger finite-bath theorem remains an originality risk.

## Limitations

This theorem assumes a single finite, nondegenerate, equally spaced Gibbs reservoir, gap matching, diagonal passive qubit inputs, and one energy-preserving joint unitary. It does not optimize over arbitrary bath Hamiltonians, additional ancillas, repeated resets, catalysts, state coherences, general interacting thermal machines or non-energy-conserving controls. The statement is an exact self-reviewed finite-dimensional result, not an independently audited priority or experimental realization. Numerical tests cannot verify all parameter values.

## References

1. Deependra Singh, Debarupa Saha and Ujjwal Sen, *Towards minimal conditions for ergotropy injection in open quantum systems*, arXiv:2609.04457v1 (first public 2026-09-03), https://arxiv.org/abs/2609.04457.
2. Xueyuan Hu, *Thermal Operations Involving a Single-mode Bosonic Bath*, arXiv:1807.02942v1 (first public 2018-07-09), https://arxiv.org/html/1807.02942v1.
