# Integral critical group of the bitangent–Aronhold incidence graph

## Finding
Let \(C\) be any smooth, geometrically connected, non-hyperelliptic plane quartic over an algebraically closed field \(k\) of characteristic distinct from \(2\). Its \(28\) bitangents and \(288\) Aronhold heptads define a simple bipartite incidence graph \(\Gamma\), with a bitangent adjacent to a heptad precisely if it belongs to the heptad. Write \(L\) for its integral graph Laplacian and \(K(\Gamma)=\operatorname{coker}(L_{\mathrm{red}})\) for the critical group of any reduced Laplacian. Then
\[
K(\Gamma)\cong \mathbb Z/16\mathbb Z\oplus(\mathbb Z/64\mathbb Z)^{26}
\oplus(\mathbb Z/7\mathbb Z)^{235}\oplus(\mathbb Z/49\mathbb Z)^{26}.
\]
It has order \(2^{160}7^{287}\), exponent \(3136\), and the graph has that same number of spanning trees.

## Assumptions and scope
The characteristic assumption ensures the classical reduced configuration of \(28\) bitangents and the standard theta-characteristic description of the \(288\) Aronhold heptads. The resulting abstract graph is independent of the quartic because these classical incidence structures are equivalent under the genus-three level-two symplectic action. All graph groups are over \(\mathbb Z\). The result does not identify the chip-firing group with a divisor-class group on \(C\).

For computation, fix a regular Cayley octad labelled by \(\{0,\ldots,7\}\). Its \(28\) bitangents are indexed by unordered pairs \(ij\). Represent the theta-characteristic torsor by the even-subset quotient \(V=\mathbb F_2^8{}_{\mathrm{even}}/\langle\mathbf1\rangle\) with the distinguished even quadratic refinement \(q(S)=|S|/2\pmod 2\). Every pair \(ij\) is an odd theta characteristic, and a triple of distinct bitangents \(ij,ab,cd\) is azygetic precisely when the symmetric difference of its three two-element subsets has cardinality \(0\) or \(4\).

## Proof
**1. Enumerating exactly the heptads.** Interpret a seven-bitangent selection as a seven-edge simple graph on the eight octad labels. The triple azygetic condition forbids both a three-edge path and a three-edge matching. A connected graph without a three-edge path must be a star or a triangle. The matching condition and the bound of eight vertices force precisely two seven-edge shapes: the seven-edge star (eight instances) and a four-edge star disjoint from a triangle (\(8\binom73=280\) instances). Conversely, every triple from either graph shape has symmetric difference of cardinality \(0\) or \(4\), proving that all \(288\) are Aronhold heptads. These two graph shapes and their \(8+280\) count are classical, not asserted as a new classification [1,2].

**2. The incidence Gram matrix.** Let \(B\in\{0,1\}^{28\times288}\) have a unit at \((b,h)\) when bitangent \(b\) belongs to heptad \(h\). Every column has sum \(7\), and every row has sum \(72\). Every distinct pair of bitangents lies together in \(16\) heptads, by direct counting in the two graph shapes (also certified by the finite verifier). Hence
\[
BB^{\mathsf T}=56I_{28}+16J_{28}.
\]
The graph has \(316\) vertices and \(28\cdot72=288\cdot7=2016\) edges, and its Laplacian is
\[
L=\begin{pmatrix}72I_{28}&-B\\-B^{\mathsf T}&7I_{288}\end{pmatrix}.
\]
It is connected because distinct bitangents occur together in heptads. The Gram identity gives nonzero Laplacian eigenvalues \(79\) once, \(7\) with multiplicity \(260\), and the two roots of \(z^2-79z+448\), each with multiplicity \(27\). By the matrix-tree theorem,
\[
\tau(\Gamma)=\frac{79\cdot7^{260}\cdot448^{27}}{316}=2^{160}7^{287}.
\]
Thus no prime other than \(2\) or \(7\) can occur in the integral critical group.

**3. Exact local Smith reduction.** Delete one vertex of \(L\) to obtain a nonsingular \(315\times315\) integer matrix \(A\). Perform elementary integral row and column operations over \(\mathbb Z_{(p)}\) for \(p=2,7\). At precision \(p^{10}\), a unit pivot is eliminated by an invertible modular Schur step; when the residual block has no unit, divide that entire block by \(p\), recording one additional valuation. This yields exact local elementary-divisor valuations when all pivots are found before exhausting precision. For \(p=2\), the counts are \(e=0:288\), \(e=4:1\), \(e=6:26\); for \(p=7\), they are \(e=0:54\), \(e=1:235\), \(e=2:26\). Their valuation totals are respectively \(160\) and \(287\), agreeing with the independent determinant above. The elementary divisors therefore give the displayed group. The same local factors arise from deleting a bitangent or a heptad vertex, independently of the ordering; four choices are explicitly replayed.

For additional structural perspective on the \(2\)-part, eliminating the \(7I_{288}\) block is legal over \(\mathbb Z_{(2)}\). Deleting a bitangent vertex leaves the Schur matrix \(64I_{27}-(16/7)J_{27}\). It is \((16/7)(28I_{27}-J_{27})\); the latter has integer Smith form \(\operatorname{diag}(1,28,\ldots,28)\) with \(26\) copies of \(28\). This independently gives one \(2^4\) and \(26\) copies of \(2^6\).

## Verification
The accompanying Python files are `verify_aronhold_octad.py` (constructs the seven-edge subsets and independently verifies the classical heptad representation) and `verify_critical_group.py` (constructs \(B,L\), checks the Gram identity, and reproduces local Smith valuations for sinks \(0,1,28,315\)). Execute `python3 verify_critical_group.py` with NumPy installed, in the same folder as the two files. The local reductions use only integer modular operations; no floating-point spectral approximation enters the Smith computation. The counts sum to \(315\) factors at each prime and match the exact spanning-tree valuation. A different finite-field/surface realization does not need to be enumerated to obtain the configuration invariant.

## Relationship to prior work
Dolgachev's treatment [1] and Dalla Piazza–Fiorentino–Salvati Manni [2] provide the bitangent/Cayley-octad/Aronhold geometry and specifically already identify the \(8+280\) graph-shape distribution. Bergvall [3] treats moduli spaces marked by these structures, their symmetries, and finite-field point counts; it does not supply the reduced graph-Laplacian Smith form. A related calculation [4] concerns the integer cokernel of the rectangular \(28\times288\) heptad–bitangent incidence map, of order \(7\). That is a different quotient from the critical group of the \(316\)-vertex graph. The present integral critical-group decomposition is not claimed to improve the classical geometric enumeration.

## Limitations
The result concerns one canonical finite incidence graph and its integral Jacobian; it does not address the quartic's geometric Jacobian, its Néron–Severi lattice or arithmetic Galois descent. The prime-adic reductions are finite, reproducible computations, combined with the independent exact determinant and a direct \(2\)-local argument. The absence of a previous identical Smith computation in the examined literature does not prove exhaustive historical priority. Independent mathematical validation remains outstanding.

## References
1. I. Dolgachev, *Classical Algebraic Geometry: A Modern View*, Chapter 6, Section 6.1.2, Cambridge University Press, 2012. See also https://mathweb.ucsd.edu/~eizadi/207A-14/Dolgachev-topics.pdf.
2. F. Dalla Piazza, A. Fiorentino, R. Salvati Manni, *Plane quartics: the matrix of bitangents*, 2014, https://arxiv.org/abs/1409.5032.
3. O. Bergvall, *Arithmetic and topology of classical structures associated with plane quartics*, European Journal of Mathematics 9 (2023), article 117, https://doi.org/10.1007/s40879-023-00711-3.
4. *Aronhold heptads span the full degree-seven congruence lattice of bitangents*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-aronhold-heptads-span-the-full-degree-seven-congruence-lattice-o--7ea27d5e8181.
