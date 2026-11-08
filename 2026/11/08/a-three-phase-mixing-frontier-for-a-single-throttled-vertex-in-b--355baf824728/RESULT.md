# A three-phase mixing frontier for a single throttled vertex in balanced bipartite graphs

## Finding
Fix an integer \(m\ge3\) and \(b\in[0,1]\). Let \(K_{m,m}\) have bipartition \(U=\{u_0,\ldots,u_{m-1}\}\) and \(V=\{v_1,\ldots,v_m\}\). Among all real symmetric entrywise-nonnegative stochastic matrices \(P\) supported on this graph and its holding loops, constrain the total probability of moving from \(u_0\) to \(V\) to be \(b\), equivalently \(P_{u_0u_0}=1-b\). Write \(\rho(P)=\|P-\mathbf1\mathbf1^{\mathsf T}/(2m)\|_2\), the second-largest eigenvalue modulus (with multiplicity) on the constant-orthogonal subspace.

Set
\[
 a_0=\frac1m,\qquad a_1(b)=\frac{2m-(m+1)b}{m(2m-1)},
\]
\[
 A_m=m(3m-1),\quad B_m(b)=(3m+1)b-8m+2,\quad C_m(b)=4-\frac{2(m+1)b}{m},
\]
\[
 a_2(b)=\frac{-B_m(b)-\sqrt{B_m(b)^2-4A_mC_m(b)}}{2A_m}.
\]
The exact minimum is attained by setting all \(m\) edges from \(u_0\) to \(V\) to \(b/m\), all other cross-part edges to \(a_*(b)\), and holding probabilities to the residual row sums, where
\[
 a_*(b)=\begin{cases}
 1/m,&0\le b\le1/(m+1),\\
 a_1(b),&1/(m+1)\le b\le2/3,\\
 a_2(b),&2/3\le b\le1.
\end{cases}
\]
Its optimal mixing modulus is
\[
 \boxed{\rho_*(b)=\begin{cases}
 \displaystyle\frac{1-(m+1)b+\sqrt{[1-(m+1)b]^2+4m(m-1)(1-b)}}{2m},&0\le b\le1/(m+1),\\[5pt]
 \displaystyle\sqrt{\frac{2(m+1)b^2-4mb+2m-1}{2m-1}},&1/(m+1)\le b\le2/3,\\[5pt]
 1-ma_2(b),&2/3\le b\le1.
\end{cases}}
\]
The two phase boundaries are \(b=1/(m+1)\), where all ordinary cross-edges first cease to be saturated, and \(b=2/3\), where an internal vertex-class eigenvalue replaces the positive quotient eigenvalue as the active spectral constraint. At \(b=2/3\), \(a_*(b)=2/(3m)\) and \(\rho_*(b)=1/3\).

## Assumptions and scope
All vertices have equal stationary probability. Transition probabilities are nonnegative, symmetric and supported on edges or holding loops only; zero transition weights are permitted. The distinguished vertex is \(u_0\), and its *aggregate* outgoing probability, not the weight of any specified individual edge, is fixed to \(b\). The optimization ranges over all feasible matrices, without imposing symmetry on their free weights. The construction gives at least one globally optimal matrix; uniqueness among arbitrary nonsymmetric-weight assignments is not asserted. The case \(m=2\) is excluded: its absent internal eigenspace changes the high-\(b\) branch.

## Proof
**Symmetry reduction.** The subgroup permuting \(U\setminus\{u_0\}\) and independently permuting \(V\) preserves the graph, the fixed aggregate \(b\), and feasibility. Averaging \(P\) over this group cannot increase the convex spectral norm \(\|P-\mathbf1\mathbf1^{\mathsf T}/(2m)\|_2\). Thus at least one optimum has two types of cross-edges: \(b/m\) from \(u_0\), and \(a\) from every other \(u_i\), with \(0\le a\le1/m\). The holding probabilities are \(1-b\), \(1-ma\), and \(1-b/m-(m-1)a\), all nonnegative on this interval.

**Spectrum.** The differences within \(U\setminus\{u_0\}\) form an eigenspace of dimension \(m-2\) with eigenvalue \(\alpha=1-ma\); the differences within \(V\) form an eigenspace of dimension \(m-1\) with eigenvalue \(\beta=1-b/m-(m-1)a\). On vectors constant on each of the three classes \(\{u_0\},U\setminus\{u_0\},V\), the stochastic quotient is
\[
 Q=\begin{pmatrix}
 1-b&0&b\\0&1-ma&ma\\b/m&(m-1)a&1-b/m-(m-1)a
 \end{pmatrix}.
\]
It is similar to a symmetric matrix, and its remaining nonstationary eigenvalues \(t_+\ge t_-\) are the roots of
\[
 q(x)=x^2-Tx+D,\quad T=2-\frac{m+1}{m}b-(2m-1)a,\quad D=1-\frac{m+1}{m}b+a(2mb-2m+1).
\]
The exact objective is \(\max\{|t_+|,|t_-|,\alpha,\beta\}\). Here \(\alpha,\beta\ge0\). At fixed \(b\), increasing \(a\) subtracts a nonnegative multiple of the Laplacian of \(K_{m-1,m}\), so \(t_+,t_-,\alpha,\beta\) are all nonincreasing in \(a\). Consequently, the positive spectral envelope is nonincreasing and \(-t_-\) is nondecreasing.

**First regime.** At \(a=1/m\), the roots satisfy
\[
 q(x)=x^2+\frac{(m+1)b-1}{m}x-\frac{(m-1)(1-b)}m.
\]
For \(b\le1/(m+1)\), \(t_++t_-\ge0\), so \(t_+\ge|t_-|\). Also \(\alpha=0\), \(\beta=(1-b)/m\le t_+\); the last inequality follows since \(t_+\) decreases with \(b\), and at the endpoint it equals \(\sqrt{(m-1)/(m+1)}\ge1/m\). Since no feasible \(a\) exceeds \(1/m\) and \(t_+\) decreases in \(a\), this endpoint is globally optimal. Solving the quadratic gives the first branch.

**Middle regime.** The choice \(a=a_1(b)\) sets \(T=0\), so \(t_+=-t_-=R\), where
\[
 R^2=\frac{2(m+1)b^2-4mb+2m-1}{2m-1}.
\]
The following exact factorizations verify that the internal eigenspaces do not dominate when \(1/(m+1)\le b\le2/3\):
\[
 R^2-\alpha^2=\frac{(3b-2)(m-1)((m+1)b-2m)}{(2m-1)^2}\ge0,
\]
\[
 R^2-\beta^2=\frac{(3b-2)(b(m^2+2m-2)-2m(m-1))}{(2m-1)^2}\ge0.
\]
For \(a\le a_1\), monotonicity gives \(t_+(a)\ge R\); for \(a\ge a_1\), it gives \(-t_-(a)\ge R\). Hence \(a_1\) is globally optimal.

**Third regime.** Suppose \(2/3<b\le1\). At \(a=a_1\), the above factorization implies \(\alpha>R=-t_-\) and \(\alpha>\beta\). At \(a=b/m\), the quotient eigenvalues are \(1-b\) and \(1-2b\), while \(\alpha=\beta=1-b\); thus \(-t_-=2b-1>1-b\). The decreasing function \(\alpha\) and nondecreasing function \(-t_-\) therefore cross at exactly one \(a\in(a_1,b/m)\). On this interval \(\alpha\ge\beta\), and
\[
 q(\alpha)=a(m-1)(b-ma)\ge0.
\]
Since \(\alpha>t_-\), this yields \(\alpha\ge t_+\). Therefore the objective crosses exactly between \(\alpha\) and \(-t_-\), and the crossing is globally optimal. The equation \(q(-\alpha)=0\) reduces to
\[
 m(3m-1)a^2+[(3m+1)b-8m+2]a+4-2(m+1)b/m=0.
\]
The root in \((a_1,b/m)\) is precisely \(a_2(b)\), proving the third branch. Continuity at both displayed boundaries follows by substitution.

## Verification
The included `verify.py` is a standalone Python-3 standard-library checker. It verifies rational polynomial/factorization identities for \(1313\) exact parameter cases, constructs full rational stochastic matrices and tests the claimed invariant eigenspaces, and compares the formula against \(334411\) alternative feasible invariant parameters across \(1111\) parameter instances. The run returned `VERIFY_OK`. Its finite tests do not establish the continuum or all-size statements; those follow from the proof above.

## Relationship to prior work
Boyd, Diaconis and Xiao (2003) formulated fastest symmetric Markov mixing as a convex spectral optimization. Boyd, Diaconis, Parrilo and Xiao (2007, arXiv:0709.0955v1, §§3.1.2 and 5.3.1) solved the *unrestricted*, fully edge-invariant complete-bipartite problem; for \(K_{m,m}\) it has uniform cross-edge weight \(2/(3m)\) and SLEM \(1/3\). This is the single point \(b=2/3\) here, not the constrained frontier. Their orbit/symmetry machinery supplies a legitimate method of reduction but no formula for a singled-out vertex with fixed aggregate transition budget. Jafarizadeh (2020) studies unrestricted fastest mixing for clique lifts, subgraphs and varying stationary distributions; its studied graph families and constraints do not state the present fixed-row-probability frontier. No equivalence or stronger formula was found in the inspected sources, although complete bibliographic priority cannot be guaranteed.

## Limitations
The result concerns symmetric stochastic matrices with uniform stationary distribution and exactly one fixed aggregate row-crossing probability; it does not describe nonreversible chains, arbitrary stationary distributions, multiple simultaneous throttled vertices, or classify all optimal matrices. A related later graph-lifted mixing paper and other unindexed sources could contain an overlooked equivalent parameterization; this remains a priority risk.

## References
- S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, Stanford Statistics Technical Report 2003-04, February 2003. https://statistics.stanford.edu/technical-reports/fastest-mixing-markov-chain-graph
- S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest mixing Markov chain on graphs with symmetries*, arXiv:0709.0955v1, first posted September 6, 2007. https://arxiv.org/abs/0709.0955
- S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs & Subgraphs*, IEEE Trans. Signal Inform. Process. Netw. 6 (2020), 88–104, DOI:10.1109/TSIPN.2020.2964211. https://doi.org/10.1109/TSIPN.2020.2964211
