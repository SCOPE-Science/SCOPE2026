# Sharp generic fusion width seventeen for the order-seven Heisenberg bilinear model

## Finding
For the finite Heisenberg group \(G=UT_3(\mathbb F_7)\), let \(Z\) be its center and put \(\mathcal H_s=\operatorname{Ind}_Z^G\psi_s\), with \(s\in\mathbb F_7\). For **every** ordered central-character pair \((s,t)\in\mathbb F_7^2\), the sum of seventeen allowed equivariant bilinear fusion channels from \(\mathcal H_s\times\mathcal H_t\) to \(\mathcal H_{s+t}\) is dominant. Equivalently, its seventeenth projective secant variety fills the ambient projective space:
\[
\sigma_{17}(\mathbb P X_{s,t})=\mathbb P^{2400}.
\]
The **exact generic fusion width** is \(17\), for all \(49\) pairs \((s,t)\). Specifically, a nonempty Zariski-open set of bilinear equivariant maps has exact width \(17\); no claim is made that every target admits a seventeen-channel decomposition. This is the first expected filling order for this field size.

## Assumptions and scope
All representation spaces, affine images, secant varieties, and genericity assertions are over \(\mathbb C\). Fix \(K=\mathbb F_7^2\) of size \(N=49\), a primitive complex seventh root \(\zeta\), and additive characters \(\psi_s(z)=\zeta^{sz}\). Write \(A(a),B(b)\) for the twisted-convolution commutant operators with kernels \(a,b\in\mathbb C^K\), and \(d\in\mathbb C^K\) for the basepoint row of the output operator. Under evaluation at the basepoint, each equivariant bilinear map is a \(49\times49\) matrix. The one-channel polynomial map is
\[
F_{s,t}(a,b,d)_{i,j}=\sum_{k\in K} d_k a_{i-k}b_{j-k}\zeta^{-k_x\left(s(i_y-k_y)+t(j_y-k_y)\right)},\quad i,j\in K,
\]
with all subscripts and exponents computed modulo \(7\). The seventeen-channel map \(\Phi_{17}\) sums seventeen independent copies of \(F_{s,t}\), hence maps \(\mathbb A^{2499}\) to \(\mathbb A^{2401}\). Let \(X_{s,t}\) denote the Zariski closure of the one-channel image.

## Proof
**1. Necessary lower bound.** A channel has three kernel vectors of length \(49\). On a dense parameter subset the free action
\[
(a,b,d)\mapsto(\lambda a,\mu b,(\lambda\mu)^{-1}d), \qquad(\lambda,\mu)\in(\mathbb C^*)^2
\]
preserves its output. Thus each one-channel image has dimension at most \(3\cdot49-2=145\), and the closure of the sixteen-channel sum has dimension at most \(16\cdot145=2320<2401\). Consequently a general target has width at least \(17\). This argument needs only the two scaling symmetries, not any prior classification of lower secants.

**2. Differential coordinates.** Index \(K\) by \(7x+y\) for \((x,y)\in\mathbb F_7^2\). In channel \(z\), the partial derivatives of the preceding monomial sum at \((a_z,b_z,d_z)\) in output row \((i,j)\) are the sum of the contributions from \(k\) with \(u=i-k\), \(v=j-k\):
\[
\partial_{a_z[u]}:d_z[k]b_z[v]\zeta^{-k_x(su_y+tv_y)},\quad
\partial_{b_z[v]}:d_z[k]a_z[u]\zeta^{-k_x(su_y+tv_y)},\quad
\partial_{d_z[k]}:a_z[u]b_z[v]\zeta^{-k_x(su_y+tv_y)}.
\]
For fixed \((i,j)\) and the indicated derivative coordinate there is exactly one compatible \(k\); equivalently the verifier sums the contributions over all \(k\). The full Jacobian has \(2401\) rows and \(2499\) columns.

**3. Four exact nonzero maximal minors.** Work in \(\mathbb F_8=\mathbb F_2[\alpha]/(\alpha^3+\alpha+1)\). The element \(\alpha\) has order \(7\), so there is a ring homomorphism \(\mathbb Z[\zeta_7]\to\mathbb F_8\) carrying \(\zeta_7\mapsto\alpha\). Generate the seventeen triples of \(49\)-vectors for each of four representatives \((0,0),(0,1),(1,1),(1,2)\) exactly by the embedded `verify_q7.py`, using the SHA-256 counter stream with seed `q7-fill-certificate-v1|s=<s>|t=<t>` and taking the least three bits of each byte. This specifies fixed integral parameter points, not merely random tests.

The embedded program constructs each Jacobian over \(\mathbb F_8\) and runs exact row elimination, recording the first available pivot column at each step. For all four pairs it reaches rank \(2401\), producing a specific nonzero \(2401\times2401\) minor. The determinant residues in the field encoding \(1,\alpha,\alpha^2\) are respectively \(1,6,6,1\). The SHA-256 digests of the ordered pivot columns, packed as little-endian unsigned 16-bit indices, are:

| Representative | Determinant in \(\mathbb F_8\) | Pivot-column SHA-256 |
|---|---:|---|
| \((0,0)\) | 1 | `bb0c78b1653184ed834995a78cec30ee99b5177a2fc591e3c592daab01142a57` |
| \((0,1)\) | 6 | `48e9e7b30f10c6d229d89a2a2c2c124fcce73c873516a9af1c4b8c8e233bdafc` |
| \((1,1)\) | 6 | `ec0035959d1ac0f7e1bb9b4325d47791ed42a78718f540eca84a51f1471133ba` |
| \((1,2)\) | 1 | `828da0983eef85ce78b4b558bdaaed75f0292ed73435d1754a366a427d0e604c` |

Since reduction of a zero algebraic-integer determinant is zero, these four nonzero residues exhibit nonzero complex Jacobian minors for the four complex parameter points obtained by lifting the kernel entries. Hence \(\Phi_{17}\) has surjective differential at those points, proving dominance over \(\mathbb C\) for the four representatives.

**4. All central types.** The three central weights \((s,t,-s-t)\) can be permuted by dualizing one factor in the invariant trilinear form \(\sum_x (Af)(x)(Bg)(x)(C^{\mathsf T}h)(x)\); simultaneously scaling them by any nonzero element of \(\mathbb F_7\) is implemented by a Heisenberg-group automorphism. Both operations induce linear equivalences of one-channel images and all their secants. The \(49\) ordered pairs split into four orbits of sizes \(1,18,18,12\), represented by the four cases above. The verifier independently enumerates all four orbits. Thus all \(49\) seventeenth secants fill their ambient space.

**5. Exact, not just border, width.** The dominant polynomial image is constructible and contains a nonempty Zariski-open subset of its irreducible affine target. The sixteen-channel image closure is proper by Step 1, so an open subset has width exactly \(17\). This proves exact generic representability, not a claim about all matrices or all complex targets.

## Verification
The complete standard-library Python program `verify_q7.py` is embedded alongside this report and is the source of the mathematical certificate. Run `python3 verify_q7.py`. It constructs all four \(2401\times2499\) Jacobians; verifies that \(\alpha\) has order seven, that its finite-field arithmetic is consistent, and that the four orbit representatives cover all central types; checks direct one-channel polynomial finite differences against exact Jacobian entries in all three parameter families; then performs deterministic exact Gaussian elimination using three bit-planes per row. The program checks all four nonzero determinants and the fixed parameter/pivot hashes, and aborts on disagreement. No floating-point rank calculation is involved.

A second implementation using 64-bit packed arrays and compiled exact arithmetic was compared against the standard-library construction on every entry of each of the four matrices. The published certificate does not require that optional implementation. Finite-field nonvanishing proves the characteristic-zero statement through the cyclotomic reduction, rather than treating a finite experiment as an infinite proof.

## Relationship to prior work
Nguyen Bich Van and Nguyen Trung Kien, *Secant dimensions and bilinear decomposition widths for finite Heisenberg groups*, arXiv:2611.01104v1, first public October 31, 2026, define the channel model, prove the uniform one-channel bound and second secants, and verify filling through field order five. Their Conjecture 11.1 predicts the first filling rank for all \(q\), and leaves \(q=7\) untreated. Their Propositions 7.1--7.2 establish the central-type symmetries used here.

A subsequently published, directly relevant mathematical report proves the nondefectivity of **all** the order-seven secants through \(r=16\) and explicitly says that its methods do not settle filling at \(r=17\). Its entire mathematical result was inspected; no filling-rank claim appears there. The present result supplies precisely that missing filling result, without reasserting the earlier sub-filling classifications as new.

The untwisted pair is equivalent, after finite Fourier transform, to a group-based phylogenetic tripod over \(\mathbb F_7^2\). Baños et al., *Dimensions of Group-based Phylogenetic Mixtures*, prove their broad join nondefectivity theorem when the number of leaves is at least \(2r+5\), which does not apply to a three-leaf tripod with seventeen mixture components. Their conjectural general claw case is not a proof of this filling assertion.

## Limitations
The theorem concerns the single prime field order \(q=7\), all central-character pairs, and complex-algebraic generic behavior. The exact ranks are witnessed after reduction to characteristic two, but they make no assertion about the characteristic-two geometry. The result does not determine exceptional individual targets, worst-case fusion width, or exact secant equations. The published penultimate-secant report supplies separate lower-order dimensions; they are not needed for this proof. Potential earlier unindexed algebraic-statistical literature remains a priority risk; no independent mathematical audit has been performed.

## References
1. Nguyen Bich Van and Nguyen Trung Kien, *Secant dimensions and bilinear decomposition widths for finite Heisenberg groups*, arXiv:2611.01104v1 (submitted October 31, 2026), Sections 3--11, especially 5, 7, 8 and Conjecture 11.1. https://arxiv.org/html/2611.01104v1
2. *Penultimate secants of order-seven Heisenberg bilinear channel varieties are nondefective*, published mathematical record (November 2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-penultimate-secants-of-the-order-seven-heisenberg-bilinear-chann--db0f5ed6395c
3. H. Baños et al., *Dimensions of Group-based Phylogenetic Mixtures*, arXiv:1711.08686 (2017), Theorem 1.1 and Section 5. https://arxiv.org/abs/1711.08686
