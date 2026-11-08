# Penultimate secants of order-seven Heisenberg bilinear channel varieties are nondefective

## Finding
For \(G=UT_3(\mathbb F_7)\), let \(\mathcal H_s=\operatorname{Ind}_{Z}^{G}\psi_s\) denote the induced representation associated with a central character \(s\in\mathbb F_7\). For every ordered pair \((s,t)\in\mathbb F_7^2\), let \(X_{s,t}\subset\mathbb A^{2401}_{\mathbb C}\) be the one-channel affine image closure of the equivariant bilinear map parameterization defined below. Then for every integer \(1\le r\le16\),
\[
\dim \overline{X_{s,t}+\cdots+X_{s,t}}=145r,
\qquad \dim\sigma_r(\mathbb P X_{s,t})=145r-1.
\]
The sum on the left has \(r\) summands. In particular, the sixteenth projective secant is nondefective, of dimension \(2319\) and codimension \(81\) inside \(\mathbb P^{2400}\). This proves the expected dimensions at **every non-filling order through the penultimate expected order** for all \(49\) central-character pairs. Nothing here establishes filling at order \(17\).

## Assumptions and scope
All varieties and dimensions are over \(\mathbb C\). Write \(K=\mathbb F_7^2\), \(N=|K|=49\), and let \(\zeta\) be a primitive seventh root of unity. For \(k=(k_x,k_y)\) and \(u=(u_x,u_y)\) in \(K\), set
\[
\beta_s(k,u)=\zeta^{-s k_xu_y}.
\]
For \(a,b,d\in\mathbb C^K\), the matrix of one channel, in the basepoint-coefficient model, is
\[
F_{s,t}(a,b,d)_{i,j}=\sum_{k\in K} d_k\,a_{i-k}\,b_{j-k}\,\beta_s(k,i-k)\beta_t(k,j-k),\qquad i,j\in K.
\]
This is exactly the \(A(a)^T\operatorname{diag}(d)B(b)\) model using the twisted shifts of Nguyen and Nguyen. Define \(\Phi_r\) by summing \(r\) copies of \(F_{s,t}\); its image closure is the affine cone over the projective secant. The finite-field computation below is a characteristic-zero *nonvanishing* certificate; no geometric statement is asserted over characteristic \(29\).

## Proof
**Upper bound.** One channel depends on \(3N=147\) parameters. Wherever all three vectors are nonzero, the two-dimensional scaling torus acts without changing its matrix:
\[
(a,b,d)\longmapsto(\lambda a,\mu b,(\lambda\mu)^{-1}d).
\]
The one-channel affine image dimension is therefore at most \(3N-2=145\), so every \(r\)-channel sum has dimension at most \(145r\). The one-channel equality is established independently in Nguyen--Nguyen, Theorem 5.7.

**Exact finite-field witness.** Reduce the coefficient ring \(\mathbb Z[\zeta]\) via \(\mathbb Z[\zeta]\to\mathbb F_{29}\), \(\zeta\mapsto7\). The element \(7\in\mathbb F_{29}\) has exact order \(7\). The associated cyclotomic relation is therefore respected. The included `parameters_q7.txt` contains exactly \(16\) triples of \(49\)-component vectors with entries in \(\{1,\ldots,28\}\). For every input type pair \((s,t)\), form the \(2401\times2352\) Jacobian of \(\Phi_{16}\) at these same parameters. Delete in each channel the derivative columns for \(a_{(0,0)}\) and \(b_{(0,0)}\), leaving a \(2401\times2320\) matrix. These columns are omitted solely to select \(2320\) columns; there is no claim that those columns vanish. The exact finite-field ranks of the resulting matrices, computed by `verify_q7.cpp`, are
\[
\begin{array}{c|rrrr}
(s,t)&(0,0)&(0,1)&(1,1)&(1,2)\\\hline
\operatorname{rank}_{\mathbb F_{29}}&2320&2320&2320&2320.
\end{array}
\]
For reconstruction, the derivative in a parameter \(a_h\) is
\[
\frac{\partial F_{s,t}(a,b,d)_{i,j}}{\partial a_h}=d_{i-h}\,b_{j-i+h}\,\beta_s(i-h,h)\beta_t(i-h,j-i+h).
\]
The formulas for derivatives with respect to \(b_h\) and \(d_h\) follow by differentiating the same displayed finite sum. The independent `check_derivatives.py` tests \(240\) exact finite-difference identities in \(\mathbb F_{29}\), including all three parameter families and all four pairs of central types.

**Lifting to characteristic zero.** Each of the four rank computations exhibits some nonzero \(2320\times2320\) minor after reduction modulo \(29\). That determinant, viewed in \(\mathbb Z[\zeta]\), is nonzero; hence the complex Jacobian has rank at least \(2320\) at the lifted parameter point. The upper bound just proved gives equality. The differential rank is at most the dimension of the image closure in characteristic zero, so \(\dim\overline{\operatorname{im}\Phi_{16}}=2320\) for each of the four pairs.

**All central types.** The channel varieties admit simultaneous nonzero scaling of \((s,t)\) and permutations of the triple \((s,t,-s-t)\) (Nguyen--Nguyen, Propositions 7.1--7.2). Their \(49\) ordered type pairs split into exactly four orbits with representatives and orbit sizes \((0,0):1\), \((0,1):18\), \((1,1):18\), and \((1,2):12\). These linear equivalences preserve all secant dimensions. Thus the rank conclusion holds for every pair.

**Every smaller secant order.** At each of the four witnesses the sum of \(16\) one-channel tangent images has dimension \(16\cdot145\), the sum of their individual upper bounds. Equality forces all \(16\) tangent images to be independent, each of dimension \(145\). Any subset of \(r\le16\) channels therefore has differential rank \(145r\); the general upper bound makes the secant dimension exactly \(145r\). The projective dimension is one less. At \(r=16\), the ambient projective dimension is \(2400\) and \(2400-2319=81\).

## Verification
The included `verify_q7.cpp` is a self-contained C++17 exact-arithmetic verifier. It constructs all four \(2401\times2320\) Jacobian submatrices directly from `parameters_q7.txt`, reduces entries modulo \(29\), and performs elementary row elimination without floating point. In a directory containing these artifacts, run:

```sh
g++ -O3 -std=c++17 verify_q7.cpp -o verify_q7
./verify_q7 parameters_q7.txt
python3 check_derivatives.py parameters_q7.txt
```

The observed outputs were `rank=2320 expected=2320` for each of the four cases, followed by `ALL_FOUR_JACOBIAN_RANK_CERTIFICATES_OK` and `INDEPENDENT_DERIVATIVE_FORMULAS_OK 240`. The code checks the required order of the root of unity and refuses a failed rank or malformed parameter file. Exact rank is a finite certificate for a nonzero complex minor, not a probabilistic proof and not a claim that experimentation proves generic rank without the lifting argument.

## Relationship to prior work
Nguyen Bich Van and Nguyen Trung Kien, arXiv:2611.01104v1, first submitted October 31, 2026, define these varieties, prove one-channel dimension and uniform second-secant nondefectivity, and certify all secant orders only for \(q=2,3,4,5\). Their extension-field Corollary 9.5 does not include characteristic seven; their Conjecture 11.1 leaves the first expected filling order unresolved for \(q=7\). The present new statement supplies all sub-filling orders \(1\le r\le16\) for \(q=7\), including nontrivial central characters; it uses the paper's definitions and its proven orbit symmetries.

In the untwisted pair \((0,0)\), the source's Proposition 10.1 identifies the same one-channel variety with the toric group-based tripod model for \(\mathbb F_7^2\). Baños and collaborators' claw-tree result assumes at least \(2r+1\) leaves, whereas the tripod has three leaves, so it does not imply the present sixteenth-secant conclusion. Blomenhofer and Casarotti's invariant-secant theorem gives a conditional range \(r\le \dim L/\dim X-\dim X\), which is empty for \(\dim L=2401\) and \(\dim X=145\); its hypotheses also concern irreducible group modules, not established for the present channel model.

## Limitations
The result is specific to the prime field \(\mathbb F_7\) and complex secant varieties of these channel maps. The characteristic-\(29\) computation proves a complex rank lower bound but makes no claim about singularities or equations of the secant closures. In particular, it does not prove that the seventeenth secant fills the ambient space, that the generic fusion width is \(17\), or that all finite-field prime powers share this behavior. Historical priority is subject to further inspection of specialized group-based secant literature; no independent mathematical audit has been performed.

## References
Nguyen Bich Van and Nguyen Trung Kien, *Secant dimensions and bilinear decomposition widths for finite Heisenberg groups*, arXiv:2611.01104v1 (submitted 2026-10-31), sections 3--11 and Appendix A. https://arxiv.org/html/2611.01104v1

H. Baños, N. Bushek, R. Davidson, E. Gross, P. Harris, R. Krone, C. Long, A. Stewart and R. Walker, *Dimensions of Group-based Phylogenetic Mixtures*, arXiv:1711.08686v1 (2017), section 5. https://arxiv.org/pdf/1711.08686

A. Taveira Blomenhofer and A. Casarotti, *Nondefectivity of invariant secant varieties*, arXiv:2312.12335 (2023), Theorem 1.1. https://arxiv.org/abs/2312.12335
