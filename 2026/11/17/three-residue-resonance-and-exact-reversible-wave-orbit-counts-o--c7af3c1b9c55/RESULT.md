# Three-residue resonance and exact reversible-wave orbit counts on friendship graphs

## Finding

Let \(k\ge2\) and let \(F_k=K_1\vee(kK_2)\) be the friendship graph of \(k\) triangles sharing one central vertex, with \(n=2k+1\) individually labelled vertices. Over a finite field \(\mathbb F_q\), \(q=3^f\), \(f\ge1\), let \(A_k\) be its loopless adjacency matrix and define the second-order graph wave
\[
T_k(u,v)=(A_ku-v,u),\qquad (u,v)\in\mathbb F_q^n\times\mathbb F_q^n.
\]
All \(q^{4k+2}\) states are periodic immediately. For any positive integer \(t\), define \(w_t=3^{\nu_3(t)}\), \(b_t=\min(2,w_t)\), \(c_t=\min(4,w_t)\), and use \([j\mid t]\) for the indicator of divisibility. Then the *exact* fixed-space dimension \(D_k(t)=\dim_{\mathbb F_q}\ker(T_k^t-I)\) is
\[
\boxed{D_k(t)=\begin{cases}
2[4\mid t]+[2\mid t]\big(c_t+(k-2)b_t\big)+kb_t,&k\equiv0\pmod3,\\
c_t+kb_t+(k-1)[2\mid t]b_t,&k\equiv1\pmod3,\\
4[10\mid t]+kb_t+(k-1)[2\mid t]b_t,&k\equiv2\pmod3.
\end{cases}}
\]
The first case automatically has \(k\ge3\), so all displayed multiplicities are nonnegative. Thus \(\#\operatorname{Fix}(T_k^t)=q^{D_k(t)}\) for every positive \(t\). The exact order of the permutation \(T_k\) is
\[
\boxed{L_k=\begin{cases}
36,&k\equiv0\pmod3,\\
18,&k\equiv1\pmod3,\\
30,&k\equiv2\pmod3.
\end{cases}}
\]
For every positive divisor \(d\) of \(L_k\), the number of labelled states having *least temporal period* \(d\), and the number of their distinct time-orbits, are respectively
\[
P_k(d)=\sum_{e\mid d}\mu(d/e)q^{D_k(e)},\qquad C_k(d)=P_k(d)/d.
\]
For all other \(d\), both counts vanish. In particular, the fraction of all paired-row states attaining maximal period \(L_k\) is
\[
\boxed{\Pr(\text{least period}=L_k)=\begin{cases}
(1-q^{-2})(1-q^{-1}),&k\equiv0\pmod3,\\
(1-q^{-1})(1-q^{-2(k-1)}),&k\equiv1\pmod3,\\
(1-q^{-4})(1-q^{-(2k-1)}),&k\equiv2\pmod3.
\end{cases}}
\]
As \(k\to\infty\) through residue classes zero, one, and two, respectively, these fractions tend to the three distinct positive constants \((1-q^{-2})(1-q^{-1})\), \(1-q^{-1}\), and \(1-q^{-4}\). The class \(k\equiv2\) has a primitive tenth-root contribution absent from the other two classes.

## Assumptions and scope

There is one hub and exactly \(k\) disjoint pairs of nonhub vertices; the hub is adjacent to every nonhub vertex and each pair is joined by one additional edge. Vertex labels, both time rows and the direction of time are retained in counts. The field has characteristic three, although its cardinality may be any power \(3^f\). The coefficient \(-1\) in the previous-row term is essential: the rule is not the one-row XOR map or a synchronous excitation automaton. We consider every positive integer \(t\) and all \(k\ge2\), without restrictions on extension degree \(f\). The one-triangle graph \(k=1\) is deliberately excluded, as are graphs with no triangle and fields of other characteristics.

## Proof

**1. Reversibility and the adjacency decomposition.** The inverse is \(T_k^{-1}(u,v)=(v,A_kv-u)\); hence, on the finite state space, every state is already periodic at time zero. Write a vector of vertex values as \((h;a_1,b_1;\ldots;a_k,b_k)\). Since two is invertible in characteristic three, change coordinates to \(s_i=a_i+b_i\) and \(d_i=a_i-b_i\). A single adjacency action gives
\[
h'=\sum_{i=1}^k s_i,\qquad s_i'=s_i+2h,\qquad d_i'=-d_i.
\]
Thus the \(k\) contrast coordinates form \(k\) eigenlines of eigenvalue \(-1\). The remaining \((k+1)\)-dimensional subspace has characteristic polynomial \((x-1)^{k-1}(x^2-x-2k)\). Indeed the subspace \(h=0,\sum_i s_i=0\) is a \((k-1)\)-dimensional eigenvalue-one subspace, and the quotient, in coordinates \( (h,S)\) with \(S=\sum_i s_i\), has matrix \(\begin{psmallmatrix}0&1\\2k&1\end{psmallmatrix}\). Directly solving \(A_kz=z\) forces \(h=0\) and \(\sum_i s_i=0\), so the eigenvalue-one eigenspace on this block has *exactly* dimension \(k-1\).

Accordingly, the adjacency Jordan structure over \(\mathbb F_3\) is as follows. For \(k\equiv0\pmod3\), it consists of \(J_1(0)\), \(J_2(1)\), \(k-2\) copies of \(J_1(1)\) and \(k\) copies of \(J_1(-1)\). For \(k\equiv1\pmod3\), it consists of one \(J_2(-1)\), \(k\) copies of \(J_1(-1)\), and \(k-1\) copies of \(J_1(1)\). For \(k\equiv2\pmod3\), it consists of \(k\) copies of \(J_1(-1)\), \(k-1\) copies of \(J_1(1)\), and one two-dimensional irreducible block with minimal polynomial \(x^2-x+2\). The latter polynomial has nonsquare discriminant \(2\) over \(\mathbb F_3\). These partitions follow from the displayed eigenspace dimensions and their total algebraic multiplicities, on the stated \(k\ge2\) domain.

**2. Transfer adjacency blocks to temporal blocks.** On an invariant adjacency block \(B\), the paired-row wave is \(\bigl(\begin{smallmatrix}B&-I\\I&0\end{smallmatrix}\bigr)\), and its characteristic polynomial is \(\det(z^2I-zB+I)\). For \(B=J_s(\lambda)\), put \(h_\lambda(z)=z^2-\lambda z+1\). The identity
\[
h_\lambda(T)=\operatorname{diag}(B-\lambda I,B-\lambda I)T
\]
(up to an irrelevant minus sign) shows that the \(h_\lambda\)-primary module has nilpotence exponent \(s\). If \(h_\lambda\) is irreducible, its kernel has dimension two, so the temporal block is cyclic with invariant polynomial \(h_\lambda^s\). If \(h_\lambda=(z-\alpha)^2\), solving \(T(u,v)=\alpha(u,v)\) gives a one-dimensional eigenspace because \(\ker(B-\lambda I)\) has dimension one. Thus here too the temporal block is a **single** Jordan block of dimension \(2s\). The same reasoning for the irreducible quadratic adjacency factor uses the displayed determinant and its irreducibility.

In characteristic three these are the exact temporal contributions:
\[
\begin{array}{c|c|c|c}
\text{adjacency factor}&\text{wave factor}&\text{wave block dimension}&\text{block order}\\\hline
J_1(0)&z^2+1&2&4\\
J_1(1)&(z+1)^2&2&6\\
J_2(1)&(z+1)^4&4&18\\
J_1(-1)&(z-1)^2&2&3\\
J_2(-1)&(z-1)^4&4&9\\
x^2-x+2&\Phi_{10}(z)=z^4-z^3+z^2-z+1&4&10
\end{array}
\]
Here \(z^2+1\) has roots of order four and \(\Phi_{10}\) is the irreducible tenth cyclotomic polynomial over \(\mathbb F_3\) (because the multiplicative order of three modulo ten is four). A unipotent Jordan chain of length two has a three-primary order factor three, while a chain of length four has a factor nine. A chain at eigenvalue \(-1\) has an additional factor two.

**3. All fixed-point dimensions.** If \(t=3^rm\) with \(3\nmid m\), the multiplicity of each relevant root of \(z^t-1\) is \(w_t=3^r\). Therefore the nullity contribution of \(J_j(1)\) is \(\min(j,w_t)\), and that of \(J_j(-1)\) is \([2\mid t]\min(j,w_t)\). The quadratic order-four block contributes \(2[4\mid t]\), and the cyclotomic tenth-root block contributes \(4[10\mid t]\). Summing these contributions for the three adjacency Jordan partitions in step one gives, term by term, the three formulas for \(D_k(t)\). Their dimensions sum to \(2n=4k+2\) at the asserted orders, proving complete periodicity and the exact maximal orders by taking the least common multiple of the actual blocks, not merely a multiple.

**4. Primitive populations and maximal-period fractions.** Since the map is bijective, \(\#\operatorname{Fix}(T_k^t)=\sum_{d\mid t}P_k(d)\). Möbius inversion yields the displayed formula, with no assumptions about which divisors have positive populations. In class \(k\equiv0\), period thirty-six requires both a nonzero order-four quadratic block and a top-layer component in the length-four negative-eigenvalue chain, with respective fractions \(1-q^{-2}\) and \(1-q^{-1}\). In class \(k\equiv1\), period eighteen requires a top-layer component of the positive-eigenvalue length-four temporal Jordan chain *and* at least one nonzero vector in the \(k-1\) negative-eigenvalue size-two temporal chains; their two independent probabilities are \(1-q^{-1}\) and \(1-q^{-2(k-1)}\). In class \(k\equiv2\), period thirty requires a nonzero cyclotomic tenth-root component and a nonzero three-primary component, with fractions \(1-q^{-4}\) and \(1-q^{-(2k-1)}\). Multiplication of these independent proportions proves all three formulas and their limits. \(\square\)

## Verification

Run `python3 check_matrices.py` and `python3 check_exhaustive.py` from the directory holding these files. The first independently assembles the field-three adjacency and two-row temporal matrices and verifies the asserted fixed dimensions at every time up to the exact order for \(k=2,\ldots,10\): **252 exact modular nullity comparisons** and direct global-order checks. The second uses direct vertex-local transitions without matrix powers to enumerate all **59,049** states for two triangles, matching each least temporal period against the Möbius-inversion formulas. For \(k=2\) the nonzero populations are \(P_1=9\), \(P_2=18\), \(P_3=72\), \(P_6=630\), \(P_{10}=2160\), \(P_{30}=56160\). The captured outputs are supplied alongside the programs. These finite tests support, but do not replace, the unrestricted proof in the previous section.

## Relationship to prior work

The reversible second-order construction is standard, not a new model: Toffoli, Capobianco and Mentrasti (2007, Section 7.1) discuss its invertible implementation; Vlasov (2013, Sections 2--3) writes the previous-state subtraction rule on general discrete cell spaces. Previously published exact wave classifications on complete bipartite graphs over characteristic three establish temporal orders eight and twelve in that **different graph family**; they do not cover triangular friendship graphs, which have a nonzero local petal-to-petal adjacency and exhibit the three orders eighteen, thirty and thirty-six. Binary reversible waves on complete multipartite graphs concern a different coefficient field. Published first-order binary parity dynamics on triangular--pentagonal windmills is also distinct: its one-time-level update has a transient hyperplane and maximum period six rather than the present everywhere-periodic two-row rule.

Li, Zhang and Wang (2026, Theorem 4 and Sections 3--5) obtain ordinary adjacency, Laplacian and signless-Laplacian characteristic polynomials on the **same Dutch-windmill graph family**, thus overlapping with the characteristic-polynomial input to step one. Their inspected full article does not derive the characteristic-three adjacency *Jordan partitions*, the second-order temporal invariant factors, primitive temporal populations, or the three-residue resonance and maximal-period fractions established here. The matrix-polynomial calculation is a shared input, not a claim of a newly discovered graph spectrum.

## Limitations

The theorem concerns the precise unforced two-row neighbor-sum rule, undirected simple triangular friendship graphs, and finite fields of characteristic three. Other primes, nonuniform weights, nonsynchronous updates, different petal lengths, and temporal automorphism quotients are not addressed. The underlying reversible construction and graph characteristic polynomial are established prior knowledge. Although the closest accessible results were examined and their implications compared, further unindexed literature may contain equivalent temporal formulas. The result has received no independent mathematical validation.

## References

1. T. Toffoli, S. Capobianco, P. Mentrasti, *When—and how—can a cellular automaton be rewritten as a lattice gas?*, public preprint 2007-09-07, arXiv:0709.1173, Section 7.1. https://arxiv.org/abs/0709.1173
2. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, public preprint 2013-11-18, arXiv:1311.4297, Sections 2--3. https://arxiv.org/abs/1311.4297
3. W. Li, Y. Zhang, Y. Wang, *On the characteristic polynomials of Dutch windmill graphs and their applications*, AIMS Mathematics 11 (2026), 16697--16711, Theorem 4, DOI:10.3934/math.2026685. https://www.aimspress.com/aimspress-data/math/2026/6/PDF/math-11-06-685.pdf
4. *Mod-three resonance trichotomy for reversible waves on complete bipartite graphs*, publicly available research result (2026), primary result and proof inspected.
5. *Twenty-four-step resonances in reversible waves on complete multipartite graphs*, publicly available research result (2026), primary result and proof inspected.
6. *Triangle–pentagon windmills: a complete parity-orbit and entrance-time census*, publicly available research result (2026), primary result and proof inspected.
