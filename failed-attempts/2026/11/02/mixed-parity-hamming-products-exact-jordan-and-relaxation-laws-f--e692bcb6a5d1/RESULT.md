# Mixed-parity Hamming products: exact Jordan and relaxation laws for neighbor parity

## Finding

Let \(d\ge2\), and let \(m_1,\ldots,m_d\ge2\) include **at least one even and at least one odd** integer. On the Cartesian product \(G=K_{m_1}\square\cdots\square K_{m_d}\), assign a state in a finite field \(\mathbb F_q\) of characteristic two to each vertex. Update all states synchronously by the sum of the states at adjacent vertices, without self-feedback. The following formulas give every Jordan block of the update and all periodic-orbit and first-entry counts.

Write \(I_{\mathrm o}=\{i:m_i\text{ is odd}\}\), \(I_{\mathrm e}=\{i:m_i\text{ is even}\}\), and define the **integer** quantities
\[
U=\prod_{i\in I_{\mathrm o}}m_i,\qquad
\Delta=\prod_{i\in I_{\mathrm o}}(m_i-2),\qquad
V=\prod_{i\in I_{\mathrm e}}m_i,\qquad
H=\prod_{i\in I_{\mathrm e}}(m_i-2),
\]
\[
c_0=(U+\Delta)/2,\quad c_1=(U-\Delta)/2,\quad r=(V-H)/2,\quad \epsilon=d\bmod 2.
\]
Put
\[
Z=Vc_{\epsilon},\quad W=Vc_{1-\epsilon},\quad
b_0=rc_{\epsilon},\quad b_1=rc_{1-\epsilon},\quad
s_0=Hc_{\epsilon},\quad s_1=Hc_{1-\epsilon}.
\]
Here subscripts are ordinary binary indices, and \(J_j(\lambda)\) denotes a size-\(j\) Jordan block with eigenvalue \(\lambda\). The adjacency update matrix \(A\), of size \(UV\), satisfies
\[
\boxed{A\sim J_2(0)^{\oplus b_0}\oplus J_1(0)^{\oplus s_0}
\oplus J_2(1)^{\oplus b_1}\oplus J_1(1)^{\oplus s_1}.}
\]
All four multiplicities are nonnegative integers; because both parities occur, \(b_0,b_1>0\). In particular, **every such mixed-parity graph simultaneously supports nontrivial two-cycles and genuine two-step transients**. There are no other primitive periods and all configurations are periodic after at most two updates; both features are sharp.

For each integer \(t\ge0\), let \(T(x)\) be the first time that the orbit of \(x\) reaches a periodic configuration. With field cardinality \(q=2^f\) for \(f\ge1\), the exact first-entry populations are
\[
\boxed{\begin{aligned}
\#\{T=0\}&=q^W,\\
\#\{T=1\}&=q^W(q^{s_0+b_0}-1),\\
\#\{T=2\}&=q^W(q^Z-q^{s_0+b_0}),\\
\#\{T>2\}&=0.
\end{aligned}}
\]
There are precisely \(q^{s_1+b_1}\) fixed configurations and
\[
\boxed{\frac{q^W-q^{s_1+b_1}}{2}}
\]
distinct primitive two-cycle orbits. Every periodic configuration is either fixed or belongs to one of these two-cycles.

## Assumptions and scope

The graph is simple, undirected, and has vertices \((v_1,\ldots,v_d)\) with \(0\le v_i<m_i\). Two vertices are adjacent precisely when they disagree in exactly one coordinate. All updates are simultaneous; the state of a vertex is replaced by the sum in \(\mathbb F_q\) of its neighbors' **previous** states. The field size \(q\) and graph alphabet sizes \(m_i\) are unrelated; the only field hypothesis is characteristic two. In particular, \(q\) can be any power of two, not just two.

The theorem's novel scope is the genuinely heterogeneous-parity regime, which excludes the uniform-alphabet Hamming graphs classified in earlier modular-rank work. Homogeneous-parity cases are used only inside the proof as algebraic building blocks, not asserted as new results.

## Proof

**Step 1: all-ones decomposition.** Let \(J_m\) denote the \(m\)-by-\(m\) all-ones matrix, and use the tensor product identification of the vertex-state space. Since \(A(K_m)=J_m+I_m\) in characteristic two, the Cartesian adjacency is
\[
A=\epsilon I+\sum_{i=1}^d \widetilde J_{m_i},
\]
where a tilde means acting on tensor factor \(i\) and as the identity on all other factors. This identity holds over every characteristic-two field.

**Step 2: odd factors.** For odd \(m\), \(J_m^2=J_m\), so its image (dimension one) and kernel (dimension \(m-1\)) split the coordinate space. On the tensor product of odd-coordinate spaces, the operator \(P=\sum_{i\in I_{\mathrm o}}\widetilde J_{m_i}\) acts by the parity of the number of factors selected from the one-dimensional images. Thus its eigenvalue-zero and eigenvalue-one multiplicities are the even and odd coefficients of
\[
\prod_{i\in I_{\mathrm o}}((m_i-1)+z).
\]
Their sum is \(U\), and their difference is \(\Delta\), giving \(c_0\) and \(c_1\). The operator \(P\) is diagonalizable, with \(P^2=P\).

**Step 3: even factors.** For even \(m\), \(J_m\) has rank one and square zero, hence is similar to \(J_2(0)\oplus J_1(0)^{\oplus(m-2)}\). On the tensor product of even-coordinate spaces, let \(D=\sum_{i\in I_{\mathrm e}}\widetilde J_{m_i}\). Commutativity and characteristic two give \(D^2=0\). Distribute the tensor products over the displayed direct sums. The summand selecting only one-dimensional zero blocks contributes \(H\) dimensions of homology \(\ker D/\operatorname{im}D\). Every summand selecting at least one two-dimensional Jordan block is acyclic: on that factor take \(h\) with \(h(v)=u\), \(h(u)=0\), where \(Du=v\), \(Dv=0\). Then \(Dh+hD=I\) on that factor, and the same tensor homotopy satisfies this identity on the entire selected summand because its cross terms occur twice and cancel in characteristic two. Therefore \(\dim(\ker D/\operatorname{im}D)=H\), and rank-nullity with \(D^2=0\) yields \(\operatorname{rank}D=(V-H)/2=r\). So \(D\sim J_2(0)^{\oplus r}\oplus J_1(0)^{\oplus H}\).

**Step 4: tensor the two decompositions.** The operators \(P\) and \(D\) act on disjoint tensor factors, and \(A=\epsilon I+P\otimes I+I\otimes D\). In the \(P\)-eigenspace of eigenvalue \(j\in\{0,1\}\), dimension \(c_j\), the restriction is \((\epsilon+j)I+D\). Thus there are \(rc_j\) size-two and \(Hc_j\) size-one blocks at eigenvalue \(\epsilon+j\), which is exactly the asserted Jordan decomposition. Because at least one odd dimension is at least three, \(c_0,c_1>0\); because at least one even dimension is at least two, \(r>0\). Hence \(b_0,b_1>0\).

**Step 5: dynamical populations.** Decompose the state space into the generalized zero-eigenspace of dimension \(Z=s_0+2b_0\) and generalized one-eigenspace of dimension \(W=s_1+2b_1\). On the first, \(A^2=0\); on the second, \(A^2=I\). Thus a configuration is periodic exactly when its generalized zero-eigenspace component is zero; it then has period one or two. The kernel of \(A\) restricted to the generalized zero-eigenspace has dimension \(s_0+b_0\), giving the three first-entry counts by subtracting nested kernels. The fixed configurations form the kernel of \(A-I\) on the one-eigenspace, dimension \(s_1+b_1\). Subtracting those fixed configurations from all \(q^W\) recurrent states and dividing by two gives the primitive two-cycle count. The inequalities \(b_0,b_1>0\) force the existence of both true two-step transients and two-cycles.

## Verification

The standalone file `check_hamming.py` constructs adjacency matrices directly from vertex Hamming distance and performs independent exact Gaussian elimination over \(\mathbb F_2\). It checks the predicted ranks of \(A\), \(A^2\), \(A+I\), and \((A+I)^2\), and verifies \(A^4=A^2\) for 341 coordinate tuples of lengths one through four. It further enumerates 335,564 explicitly labelled configurations in 17 finite-state cases using both two-state and four-state fields (addition in these fields is bitwise XOR). The rank checks include mixed and homogeneous tuples; the main claim concerns only mixed tuples. Exact recorded output and executable source are bundled with this result.

As a small independent instance, for \(K_2\square K_3\) over \(\mathbb F_2\), the theorem predicts exactly four initially recurrent states (two fixed and one primitive two-cycle), 12 configurations first becoming periodic after one update, and 48 after two updates; these sum to all 64 states.

## Relationship to prior work

Tadaki's 1993 study of finite rule-90 and rule-150 cellular automata motivates distinguishing relaxation from periodic motion through finite-field update matrices. Peeters' published 2002 treatment of Hamming and Doob graphs supplies especially close prior work: Theorem 3.1 concerns modular minimal polynomials and Theorem 3.4 gives the characteristic-two rank formula for **uniform even alphabet** Hamming graphs. These homogeneous results and their tensor-product method are acknowledged as predecessors. They do not state the mixed-odd/even Cartesian-product Jordan decomposition, the simultaneous transient/oscillation criterion, or the exact state and orbit populations for heterogeneous dimensions.

The standard real eigenvalue formulas for generalized Hamming products (for instance Li, Zhang and Wang, 2023) are over a setting where the one-coordinate all-ones matrices may be diagonalizable; they do not provide characteristic-two nilpotent-block multiplicities. The separate published classifications of parity automata on complete multipartite graphs and distance-two Boolean cube graphs address different adjacency relations, not the Cartesian product of complete graphs with coordinate sizes of both parities.

## Limitations

The result concerns characteristic two, synchronous neighbor sums with no self-feedback, and Cartesian products with both odd and even coordinate sizes. It does not cover nonlinear threshold rules, asynchronous updating, or fields of odd characteristic. Since the principal modular algebra in Peeters' 2002 paper is closely related, the main advance is a natural **mixed-parity dynamical classification**, not a new universal method of Jordan theory. Possible unindexed earlier treatments of heterogeneous products remain a historical-originality risk. Numerical verification is supplementary; the theorem for arbitrarily large products rests on the tensor decomposition above. The historical source date identifies the 1993 first public posting of the motivating source, not the publication date of this finding. Independent mathematical auditing has not been performed.

## References

1. S.-i. Tadaki, *Orbits in one-dimensional finite linear cellular automata*, arXiv:cond-mat/9305012, initially submitted 1993-05-14, https://arxiv.org/abs/cond-mat/9305012.
2. R. Peeters, *On the p-ranks of the adjacency matrices of distance-regular graphs*, Journal of Algebraic Combinatorics **15** (2002), 127–149, DOI:10.1023/A:1013842904024. Relevant: Section 3, Theorems 3.1 and 3.4.
3. S. Klavžar, *Characterizing subgraphs of Hamming graphs*, Journal of Graph Theory **49** (2005), 302–312, DOI:10.1002/jgt.20084.
4. E. Rowland and R. Yassawi, *A characterization of p-automatic sequences as columns of linear cellular automata*, arXiv:1209.6008 (initially submitted 2012-09-26), https://arxiv.org/abs/1209.6008.
5. Y. Li, J. Zhang and M. Wang, *The Square of Some Generalized Hamming Graphs*, Mathematics **11** (2023), article 2487, DOI:10.3390/math11112487.
