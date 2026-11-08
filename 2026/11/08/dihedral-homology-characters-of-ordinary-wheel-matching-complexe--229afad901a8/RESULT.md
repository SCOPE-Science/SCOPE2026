# Dihedral homology characters of ordinary wheel matching complexes

## Finding
For \(n\ge3\), let \(W_{n+1}\) consist of the cycle \(C_n\) on vertices indexed by \(\mathbb Z/n\mathbb Z\), together with a hub adjacent to every rim vertex. Write \(X_n=\mathcal M(W_{n+1})\) for the **ordinary matching complex**, whose simplices are sets of pairwise vertex-disjoint graph edges. The dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\), \(s(i)=-i\) and fixes the hub. Let \(d=\lfloor(n-1)/3\rfloor\), \(c_m=2\cos(\pi m/3)\), and \(b_n=2\), \(n-1\), or \(n+1\) according as \(n\equiv0,1,2\pmod3\).

The reduced homology is torsion-free and concentrated in degree \(d\), with rank \(b_n\) (known nonequivariantly). Its complete rational dihedral character is
\[\chi_n(1)=b_n,\qquad \chi_n(r^a)=(-1)^{d+1}c_{\gcd(n,a)}\quad(1\le a<n),\]
\[\chi_n(r^as)=\begin{cases}0,&n\text{ odd or }3\mid n,\\(-1)^{n/2+1},&n\text{ even and }3\nmid n.\end{cases}\]
In particular,
\[\dim_{\mathbb Q}\widetilde H_d(X_n;\mathbb Q)^{D_n}=\begin{cases}1,&n\bmod12\in\{2,5,10,11\},\\0,&\text{otherwise}.\end{cases}\]
For \(n=3\) the degree is zero, and all homology and Lefschetz traces throughout are **reduced**. This character result, not the previously known wedge homotopy type, is the asserted contribution.

## Assumptions and scope
The wheel is the simple graph with exactly \(n\) rim edges and \(n\) spokes; this is not a discrete-Morse complex. A simplex has its graph edges put in a fixed linear order for computing induced permutation signs. All group actions, rational traces and reduced homology refer to the natural graph-induced action. The result holds for every integer \(n\ge3\). No claim is made about the equivariant homotopy type or integral decomposition as a lattice.

## Proof
**1. Homology concentration.** In the ordinary matching complex, the rim-edge-only subcomplex \(B\) is \(\operatorname{Ind}(C_n)\). The simplices involving the spoke at rim vertex \(i\) form the cone \(s_i*A_i\), where \(A_i\) is the independence complex of the path on the remaining \(n-2\) rim edges. The intersections of distinct spoke cones lie in \(B\). Standard path/cycle independence homotopy formulas and their attachment sequences give exactly the known wheel computation
\[\widetilde H_j(X_n;\mathbb Z)=\begin{cases}\mathbb Z^{b_n},&j=d,\\0,&j\ne d.\end{cases}\]
This is the previously published nonequivariant result of Vega, cited below; it is used, not claimed as new. The integral rank also shows there is no torsion.

**2. Signed simplicial Lefschetz formula.** For \(g\in D_n\), define
\[F_g=\sum_{\substack{M\text{ a matching of }W_{n+1}\\gM=M}}(-1)^{|M|}\operatorname{sgn}(g\mid M),\]
with the empty matching contributing \(1\). The sign is the parity of the induced permutation of the edges in the fixed simplex. The alternating trace on reduced simplicial chains is \(-F_g\), so concentration in degree \(d\) implies \(\chi_n(g)=(-1)^{d+1}F_g\). This identity is exact in characteristic zero and applies to disconnected \(X_3\).

**3. Path and cycle polynomials.** Let \(p_m=I(P_m;-1)\) for the independent-set polynomial of a path of \(m\) vertices. Then \(p_0=1\), \(p_1=0\), \(p_m=p_{m-1}-p_{m-2}\), so its values at residues modulo six are \((1,0,-1,-1,0,1)\). The cyclic polynomial \(I(C_m;-1)=c_m=2\cos(\pi m/3)\) has values \((2,1,-1,-2,-1,1)\) modulo six; the \(m=1,2\) values are the necessary orbit-quotient conventions, not assertions about simple one- or two-vertex cycles. For the identity, partition matchings by their unique spoke or no spoke to obtain \(F_1=c_n-np_{n-2}\), which agrees with \((-1)^{d+1}b_n\).

**4. Rotations.** For nonidentity \(r^a\), put \(h=\gcd(n,a)\) and \(t=n/h>1\). Every spoke orbit contains two spokes meeting at the hub and hence cannot occur in an invariant matching. The rim-edge orbits consist of \(t\) disjoint edges when admissible; orbits indexed by \(\mathbb Z/h\mathbb Z\) conflict exactly as consecutive vertices of its cycle quotient. For \(h=1\), only the empty matching occurs. An orbit of \(t\) rim edges contributes signed weight \((-1)^t(-1)^{t-1}=-1\) (the final sign is the permutation parity of a length-\(t\) cycle). Thus \(F_{r^a}=c_h\), including \(h=1,2\) with the conventions above.

**5. Reflections.** Classify rim edges and spokes by orbits under \(r^as\). A two-edge orbit that can appear together contributes weight \((-1)^2(-1)= -1\), and a fixed edge contributes \(-1\). For odd \(n\), a reflection fixes one spoke and one rim edge. The rim-only admissible orbits form a path quotient with independence value \(p_{(n-1)/2}\); the choices including the fixed spoke contribute its negative, so \(F_{r^as}=0\). For even \(n\), a vertex-axis reflection fixes two spokes and no rim edges: its rim-only quotient has polynomial \(p_{n/2-2}\), and the two fixed-spoke choices contribute \(-2p_{n/2-2}\). Thus \(F=-p_{n/2-2}\). An edge-axis reflection fixes two rim edges and no spokes, with path-quotient value \(p_{n/2+1}=-p_{n/2-2}\), by the recurrence. Therefore every even-rim reflection has the same \(F=-p_{n/2-2}\). Substituting the six-periodic values yields the stated reflection trace.

**6. Invariant classes.** The character-average formula gives
\[\dim\widetilde H_d(X_n;\mathbb Q)^{D_n}=\frac{1}{2n}\left(b_n+(-1)^{d+1}\!\sum_{a=1}^{n-1}c_{\gcd(n,a)}+n\chi_n(s)\right).\]
The divisor identity \(\sum_{a=0}^{n-1}c_{\gcd(n,a)}=\sum_{h\mid n}\varphi(n/h)c_h\) equals \(n\) when \(\gcd(n,6)=1\), and zero otherwise. To check this, separate the powers of \(2\) and \(3\) in the divisor sum: whenever a prime-power factor of either type is present, the contribution from exponent zero cancels the sum over all positive exponents because \(c_{2^j u}=-c_u\) for odd \(u\) prime to three and \(c_{3^j u}=-2c_u\) for \(3\nmid u\); otherwise every divisor is prime to six and contributes \(c_h=1\). Substituting \(b_n\), \(d\), and the reflection formula into this exact average and checking residues modulo twelve produces the announced set \(\{2,5,10,11\}\). No finite numerical extrapolation enters this proof.

## Verification
The standalone standard-library Python script `verify_wheel_matching.py` reconstructs every matching and its signed fixed-simplex Lefschetz contribution for each of the \(204\) elements of \(D_n\) across \(3\le n\le14\). It independently re-evaluates the same invariant sum by admissible edge-orbit conflict polynomials and checks agreement with the closed formula. Its final phase verifies periodic character and integrality of the dihedral invariant average for \(3\le n\le204\). The finite tests support the general algebraic argument but are not its replacement. The exact command is `python verify_wheel_matching.py`.

## Relationship to prior work
Adamaszek's early graph-independence work analyzes cyclic independence complexes and the deletion/cofiber methods underlying the rim term. Vega's published wheel result already establishes the *nonequivariant* matching-complex wedge rank and concentration used in step 1. Neither inspected text provides this dihedral character, reflection formula, or 12-periodic dihedral invariant dimension. A separately indexed character theorem covers matching complexes of **cycles**, not of wheels; indexed wheel results concerning **discrete-Morse complexes** are about a different simplicial complex. No exhaustive publication-priority conclusion is claimed.

## Limitations
No integral indecomposable representation-lattice classification, explicit equivariant wedge model, or action at other graph complexes is deduced. The statement relies on previously published homology concentration and does not reprove Vega's full discrete-Morse collapse. An undiscovered equivalent representation calculation remains possible. Independent mathematical audit has not been performed.

## References
1. M. Adamaszek, *Splittings of independence complexes and powers of cycles*, arXiv:1106.6250 (first public 2011), https://arxiv.org/abs/1106.6250.
2. J. Vega, *2-Matching Complexes*, arXiv:1909.10406 (first public 2019), particularly the ordinary wheel matching-complex theorem, https://arxiv.org/abs/1909.10406.
3. *Dihedral homology characters and quotient congruences for cycle matching complexes*, published-finding corpus indexed record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-homology-characters-and-quotient-congruences-for-cycle--6d9fbe47cba0.
4. *Dihedral top homology of wheel discrete-Morse complexes*, published-finding corpus indexed record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-top-homology-of-wheel-discrete-morse-complexes--07726f70cc8e.
