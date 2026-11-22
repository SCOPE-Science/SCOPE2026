# Complete rooted furtherness barcodes and reconstruction of finite weak orders

## Finding
Let \(P=A_1\oplus\cdots\oplus A_r\) be the ordinal sum of finite antichains, where \(r\ge2\) and \(m_j=|A_j|\ge2\) for all \(j\). Fix \(x\in A_i\), define the principal downset \(U_y=\{z\in P:z\le y\}\), and equip the order complex with the rooted *furtherness* filtration
\[
F_x(t)=\Delta\bigl(\{y\in P:|U_y\setminus U_x|\le t\}\bigr),\qquad t\in\mathbb R_{\ge0}.
\]
Write \(M_j=\prod_{a=1}^j(m_a-1)\), and define \(b_{i,i}=1\) and \(b_{i,j}=\sum_{a=i}^{j-1}m_a\) when \(j>i\). **The complete ordinary persistence barcode, over every field,** has one essential degree-zero bar \([0,\infty)\) and exactly the following additional bars:
\[
\begin{aligned}
\text{degree }j-1:\quad &M_j\text{ copies of }[b_{i,j},b_{i,j+1}),&&i\le j<r,\\
\text{degree }r-1:\quad &M_r\text{ copies of }[b_{i,r},\infty).&&
\end{aligned}
\]
There are no other bars. Every stage has torsion-free integral homology, and all interval multiplicities and endpoints are integral and independent of the coefficient field. When \(i=1\), the degree-zero transient bars number \(m_1-1\); when \(i>1\), there are no transient degree-zero bars.

**Reconstruction and separation.** The complete barcode of any fixed bottom-level root determines the *ordered* vector \((m_1,\ldots,m_r)\) and therefore the finite weak order up to isomorphism. For a fixed poset, two roots have identical all-degree barcodes exactly when they belong to the same layer.

**Sharp higher-degree root stability.** For \(x\in A_1\) and \(z\in A_r\) put \(D=\sum_{a=1}^{r-1}m_a\). The exact bottleneck distance between their degree-\(r-1\) persistence diagrams is \(D-1\), while \(\max\{\Psi(x,z),\Psi(z,x)\}=D\). By letting \(D\to\infty\) with \(r\ge2\) fixed, the sharp asymptotic coefficient is \(1\) in every prescribed positive homological degree.

## Assumptions and scope
The topology is the *lower* Alexandrov topology; each \(U_y\) includes the element \(y\). The filtration uses the literal cardinality of the set difference of principal downsets, not a graph-distance metric. All thresholds are inclusive at the birth and exclusive at finite death: \([a,b)\). The filtered space is the full order complex on eligible points, not a sublevel filtration on the original chain lengths. Ordinary degree-zero persistence retains the one connected-component class. The result is valid for every finite ordered layer vector of length at least two with all entries at least two, and for every choice of root. Homology is ordinary simplicial/singular homology after realization. No assumption about a generic ordering or distinct filtration thresholds is needed.

## Proof
**Exact point weights.** For a root \(x\in A_i\), its downset is \(U_x=A_1\cup\cdots\cup A_{i-1}\cup\{x\}\). For a point \(y\in A_j\), direct set difference gives
\[
\Psi_x(y)=
\begin{cases}
0,&j<i,\\
0,&y=x,\\
1,&j=i,\ y\ne x,\\
\displaystyle\sum_{a=i}^{j-1}m_a,&j>i.
\end{cases}
\]
Since every \(m_j\ge2\), the positive threshold values \(1,b_{i,i+1},\ldots,b_{i,r}\) are strictly increasing. At \(0\le t<1\), the eligible poset is all lower layers and the single point \(x\); its order complex is a cone with apex \(x\). It is contractible and connected. At \(1\le t<b_{i,i+1}\) (when \(i<r\)) the eligible poset has exactly the complete first \(i\) levels, so the complex is \(J_i=A_1*\cdots*A_i\). Each next critical threshold introduces an entire layer, giving successively \(J_{i+1},\dots,J_r\). If \(i=r\), \(J_r\) appears directly at time one.

**Integral homology of joins.** Each \(A_a\) is a discrete space of \(m_a\) points. Put \(V_a=\ker(\varepsilon_a:\mathbb Z[A_a]\to\mathbb Z)\), a free abelian group of rank \(m_a-1\). The augmented chain complex of \(J_j=A_1*\cdots*A_j\) is the shifted tensor product of the augmented complexes of the \(A_a\). Hence
\[
\widetilde H_k(J_j;\mathbb Z)\cong
\begin{cases}
V_1\otimes\cdots\otimes V_j\cong\mathbb Z^{M_j},&k=j-1,\\
0,&k\ne j-1.
\end{cases}
\]
The Künneth calculation has no torsion or extension ambiguity because all factors have free homology concentrated in a single degree. In particular every stage has torsion-free integral homology. The join \(J_j\subseteq J_{j+1}\) lies inside the cone \(J_j*\{a\}\) for any \(a\in A_{j+1}\), so every inclusion-induced reduced homology map \(\widetilde H_k(J_j)\to\widetilde H_k(J_{j+1})\) is zero. Also, the initial cone has zero reduced homology. Thus precisely the stated rank-\(M_j\) interval is born at \(b_{i,j}\) and dies at \(b_{i,j+1}\), with the final top degree surviving forever. The ordinary connected-component generator persists from time zero. This proves the complete field barcode and the stated integral homology assertion.

**Recover the ordered layers.** Take \(i=1\). The highest degree containing a nontrivial bar is \(r-1\), so \(r\) is recovered. The \(m_1-1\) transient degree-zero bars all have death \(m_1\) and birth \(1\), thus recover \(m_1\). For each \(2\le j<r\), the degree-\(j-1\) finite bars have length exactly \(m_j=b_{1,j+1}-b_{1,j}\), thus recover \(m_j\). Finally, the ratio of the multiplicity of top-degree essential bars to that of degree-\(r-2\) finite bars equals \(M_r/M_{r-1}=m_r-1\), giving \(m_r\). The formula holds for \(r=2\) as well: degree-zero finite bars determine \(m_1\), and their number together with the top essential multiplicity determines \(m_2\). For two root levels \(i<k\), their top essential births are \(b_{i,r}>b_{k,r}\) (the latter equals one if \(k=r\)); hence their all-degree barcodes differ. All roots in the same layer have the same computed barcode.

**Sharpness in every positive degree.** For \(x\in A_1\) and \(z\in A_r\), the top-degree diagrams have the same \(M_r\) infinite bars, born respectively at \(D\) and at \(1\). Their bottleneck distance is \(D-1\), because infinite bars cannot be matched to the diagonal. Directly \(U_x=\{x\}\), \(U_z=A_1\cup\cdots\cup A_{r-1}\cup\{z\}\), whence \(\Psi(x,z)=D\) and \(\Psi(z,x)=0\). The elementary sublevel-filtration interleaving inequality gives the universal bound by the sup-norm of the two pointwise weight functions; since this sup-norm is at most \(D\) for these roots, the ratio approaches one. Fixing \(r=q+1\), and increasing any lower layer size, proves non-improvability in every fixed degree \(q\ge1\). This does not claim finite equality with the bound \(D\).

## Verification
The companion executable `verify.py` implements two routes independently of the symbolic join proof. It directly constructs the finite order, all principal downsets and their exact set-difference weights, enumerates all order-complex chains, builds their oriented boundary columns, and performs exact persistence matrix reduction modulo \(2\), \(3\), and \(101\). Separately it evaluates the closed barcode formula and compares all degrees, endpoints and multiplicities, including reconstruction tests. The executable checks eleven size vectors, 204 rooted computations over the three primes, up to five levels. Its expected terminal line begins `PASS: 11 layer-size patterns; 204 root-by-prime calculations`.

The proof above is all-parameter and integral at the level of stage homology; finite field computations are consistency checks, not a proof of infinite parameter coverage or of integral chain-level interval splitting.

## Relationship to prior work
Badra and Singh's October 2026 paper introduced centered furtherness persistence on finite topological spaces and examined degree-zero diagrams and stability; the present work keeps their filtration definition and determines every positive homological degree for arbitrary finite weak orders. The standard integral homology of complete layered poset joins has been computed previously, as has the action of weak-order self-maps on their top homology; neither gives the *root-dependent persistence maps*, exact birth/death values, barcode reconstruction, or sharp higher-degree bottleneck examples.

Prior furtherness-barcode calculations on Boolean subset posets and Boolean-sphere posets have exponentially spaced weights and different incidence relations; their exact statements do not imply the linear-threshold weak-order barcode. Related rank-selected Boolean and Steiner-design incidence complexes likewise do not contain the general ordinal-sum layer-vector theorem. The main novelty here is the complete rooted persistence classification together with the information-recovery and sharp stability consequences, not the join homology formula itself. Exact bibliographic uniqueness is not certified.

## Limitations
The layer sizes must all be at least two, and the chosen topology must be the lower Alexandrov topology. Singleton layers create cone points and require a separate formula. The coefficient-field barcode is established in every characteristic; stagewise torsion-free integral homology is established, but no stronger assertion about canonical integral persistence interval splitting is needed here. The stability sharpness is asymptotic and concerns degree-specific bottleneck distance between root filtrations of the *same* poset, not a metric between arbitrary different finite spaces. The work is a symbolic calculation for this family, not a universal classification of finite-poset furtherness.

## References
1. S. Badra and S. Singh, *Persistence diagrams of finite topological spaces*, arXiv:2610.16386v1, first public 12 October 2026, https://arxiv.org/abs/2610.16386.
2. S. Badra and S. Singh, *Furtherness in finite topological spaces*, arXiv:2603.18580v1, first public 19 March 2026, https://arxiv.org/abs/2603.18580.
3. *Top homology detects level structure in finite weak orders*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-top-homology-detects-level-structure-in-finite-weak-orders--3b673e0af61a.
4. *Complete integral furtherness barcodes of Boolean subset posets*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-complete-integral-furtherness-barcodes-of-boolean-subset-posets--d2db8c5d42da.
5. *Extremal-root furtherness barcodes on Boolean sphere posets*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-extremal-root-furtherness-barcodes-on-boolean-sphere-posets--06baeffcb578.
