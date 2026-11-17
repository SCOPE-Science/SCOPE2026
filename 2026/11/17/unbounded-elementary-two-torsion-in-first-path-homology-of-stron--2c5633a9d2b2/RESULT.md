# Unbounded elementary two-torsion in first path homology of strongly connected circulants

## Finding

There is an explicit family of finite, strongly connected, vertex-transitive, loopless directed circulant graphs with arbitrarily large elementary two-torsion rank in **integral regular GLMY path homology in degree one**. More precisely, fix an integer \(r\ge1\), and put
\[
T=\{0,1,9,10,13,15,17,20\},\qquad
S_r=\{1\}\cup\bigcup_{i=0}^{r-1}\{2\cdot100^{r+i}+2\cdot100^i t:t\in T\}.
\]
For **every integer** \(n>2\max S_r\), let \(D_{r,n}=\operatorname{Cay}(\mathbb Z/n\mathbb Z,S_r)\), with directed arcs \(x\to x+s\pmod n\) for \(s\in S_r\). Then
\[
\boxed{H_1^{\mathrm{path}}(D_{r,n};\mathbb Z)
\cong \mathbb Z^{2r+1}\oplus(\mathbb Z/2\mathbb Z)^r.}
\]
The degree of the digraph is \(8r+1\), and the directed step \(1\) makes it strongly connected. In particular, its rational first Betti number is \(2r+1\) whereas the mod-two first Betti number is \(3r+1\); the difference grows without bound.

## Assumptions and scope

All graph vertices are the residue classes modulo \(n\), all steps are strictly positive and strictly below \(n/2\), and path homology means the regular integer GLMY chain complex: \(\Omega_0\) is the free group of vertices; \(\Omega_1\) the free group of directed arcs; and \(\Omega_2\) consists of integer linear combinations of allowed two-paths whose path boundary lies in the allowed one-path group. Its boundary is \(\partial(x,y,z)=(y,z)-(x,z)+(x,y)\), with the forbidden middle-deletion term required to cancel. No statement about higher path homology or the underlying undirected clique complex is made.

## Proof

**1. An integral degree-one presentation.** Let \(S\subset\mathbb Z_{>0}\) be finite, contain \(1\), and satisfy \(n>2\max S\). Write \(e_s(x)\) for the directed edge \(x\to x+s\pmod n\). An allowed two-path \((x,x+s,x+s+t)\) has an allowed middle-deletion term precisely when \(s+t\in S\). If it does not, its forbidden term is the formal edge \((x,x+s+t)\). Distinct starts and distinct integer sums give distinct forbidden terms, since \(0<s+t<n\). Thus \(\Omega_2\) is generated integrally by the individual triangles with \(s+t\in S\), and by differences between two-paths with the same start and the same sum \(s+t=u+v\notin S\). This follows from the kernel of a map from a free abelian group to a free group, partitioned by forbidden endpoint.

For every \(s\in S\), the two-path difference \((1,s)-(s,1)\) is allowed as an invariant two-chain (or is the difference of two individually allowed triangles). Its boundary gives
\[
e_s(x+1)-e_s(x)=e_1(x+s)-e_1(x).
\]
Define \(P_s(x)=\sum_{j=0}^{s-1}e_1(x+j)\) and \(f_s(x)=e_s(x)-P_s(x)\). The displayed equality says \(f_s(x+1)=f_s(x)\). Eliminating these relations identifies all \(f_s(x)\) with one generator \(E_s\), for each \(s\ne1\), and leaves the \(n\) edges \(e_1(x)\) free. Furthermore \(E_1=0\). The remaining two-chain boundaries reduce exactly to
\[
E_s+E_t-E_{s+t}\quad(s+t\in S),
\qquad E_s+E_t-E_u-E_v\quad(s+t=u+v\notin S).
\]
Indeed \(P_s(x)+P_t(x+s)=P_{s+t}(x)\), so all \(P\)-terms cancel. The boundary of \(E_s\) is zero, whereas \(\partial e_1(x)=[x+1]-[x]\). The kernel of the latter incidence boundary is generated over the integers by \(\sum_x e_1(x)\). Consequently
\[
H_1^{\mathrm{path}}(D_{n,S};\mathbb Z)
\cong\mathbb Z\oplus
\frac{\mathbb Z\langle E_s:s\in S\setminus\{1\}\rangle}{\text{short additive relations}}.
\tag{1}
\]
All eliminations are integral, with unit coefficients; no field argument, hidden saturation assumption or large-modulus calculation is used.

**2. Separation of the blocks.** Let \(B_i=100^{r+i}\) and \(L_i=100^i\). The block steps are \(2B_i+2L_i t\) for \(t\in T\); all are even, distinct and much larger than \(2\). Thus no two steps in \(S_r\) sum to another step: two even steps cannot equal a single block step because of the separated powers, while a pair involving \(1\) has odd sum or sums to \(2\). For two even block steps, their sum is
\[
2(B_i+B_j)+2(L_i t+L_j u).
\]
The correction lies in \([0,80\cdot100^{r-1}]\), while the integer sums \(B_i+B_j\) uniquely identify the unordered block pair \(\{i,j\}\), and distinct such sums differ by at least \(100^r\). Hence equal two-step sums must have the same unordered block pair. In the mixed case \(i<j\), equality further implies \(L_i(t-t')=L_j(u'-u)\); because \(L_j/L_i\ge100\) and each difference of elements of \(T\) has absolute value at most \(20\), both differences are zero. Pairs involving \(1\) also create no nontrivial collisions, by parity. Therefore **every** nontrivial short relation lies wholly within one block, and there are no relations between blocks or with \(E_1\).

**3. The exact eight-step relation lattice.** Within one block let \(X_t\) denote the generator indexed by \(t\in T\). Direct enumeration of its unordered pair sums yields exactly six independent defining relations:
\[
\begin{aligned}
X_0+X_{10}&=X_1+X_9,\\
X_0+X_{20}&=2X_{10},\\
X_1+X_{17}&=2X_9,\\
X_9+X_{17}&=2X_{13},\\
X_{10}+X_{20}&=X_{13}+X_{17},\\
X_{10}+X_{20}&=2X_{15}.
\end{aligned}
\]
Set \(a=X_0\) and \(b=X_1-X_0\). The first five equations imply, without division, \(X_t=a+tb\) for \(t\in T\setminus\{15\}\). The last equation is exactly \(2(X_{15}-a-15b)=0\). There are no additional relations: substituting \(X_{15}=a+15b+z\), \(2z=0\), satisfies all six equations, and the substitutions are mutually inverse. Each block quotient is therefore \(\mathbb Z^2\oplus\mathbb Z/2\mathbb Z\), integrally.

**4. Assembly.** By step 2 the global presentation in (1) is the direct sum of the independent eight-step block presentations and the winding-cycle generator. Hence its group is precisely \(\mathbb Z^{2r+1}\oplus(\mathbb Z/2\mathbb Z)^r\), for every stated \(r,n\). This also establishes the asserted field-dimension consequence by universal coefficients, since \(H_0\cong\mathbb Z\).

## Verification

The included standalone program `verify.py` enumerates all short relations of the eight-point block, checks that the gcds of its fifth- and sixth-order minors are \(1\) and \(2\), and independently checks the complete short-relation lists for \(1\le r\le5\). In these cases it finds exactly \(6r\) relations, all internal to a block. These finite checks test the proof's arithmetic, but the unbounded conclusion follows from the algebraic argument above, not from extrapolation. Run with `python3 verify.py`; no external packages are required.

## Relationship to prior work

The 2026 paper of Tang and Yau develops circulant path homology over arbitrary **fields** and gives an explicit short-additive-relation presentation for first homology over fields (Proposition 4.11). The integral presentation (1) follows here directly at chain level; the result adds a concrete all-parameter construction with arbitrarily many independent order-two integral classes, together with their exact orders. Its conclusion is not a direct statement of any field-rank formula. Di, Ivanov, Mukoseev and Zhang developed the general Cayley-digraph covering framework, without this family or its exact integral classification. Earlier GLMY work supplies the definition of path homology.

## Limitations

The construction uses rapidly growing numerical steps; no degree-optimality, minimal vertex counts, higher-degree path homology, or classes of odd-prime torsion are asserted. The novelty comparison is bounded by identifiable public sources; an unindexed or inaccessible equivalent family could exist. Mathematical verification here is internal and independent external validation has not been performed.

## References

1. X. Tang and S.-T. Yau, *Path homology of circulant digraphs*, arXiv:2602.04140, first public version 2026-02-04, particularly Sections 3–5 and Proposition 4.11. https://arxiv.org/abs/2602.04140
2. S. Di, S. O. Ivanov, L. Mukoseev and M. Zhang, *On the path homology of Cayley digraphs and covering digraphs*, arXiv:2305.15683. https://arxiv.org/abs/2305.15683
3. A. Grigor'yan, Y. Lin, Y. Muranov and S.-T. Yau, *Homologies of path complexes and digraphs*, arXiv:1207.2834. https://arxiv.org/abs/1207.2834
