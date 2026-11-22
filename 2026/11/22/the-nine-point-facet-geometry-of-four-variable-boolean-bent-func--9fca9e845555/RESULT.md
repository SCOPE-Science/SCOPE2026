# The nine-point facet geometry of four-variable Boolean bent functions

## Finding

Let \(V=\mathbb F_2^4\), and let \(\mathcal B\) be **all** Boolean bent functions \(f:V\to\mathbb F_2\). Regard each function as the point-membership concept \(\{x\in V:f(x)=1\}\). Let \(\mathcal Q_{10}\) be the family of supports of cardinality ten among these concepts. A finite query support \(S\subseteq V\) is VC-shattered by \(\mathcal B\) **if and only if** \(S\subsetneq Q\) for some \(Q\in\mathcal Q_{10}\). Equivalently, the entire shattering complex is the complex of proper subsets of the 448 ten-point nonsingular affine quadratic blocks.

The exact shattered-support polynomial, with the coefficient of \(z^k\) counting shattered \(k\)-element supports, is
\[
\Phi_{\mathcal B}(z)=1+16z+120z^2+560z^3+1820z^4+4368z^5+8008z^6+11200z^7+10080z^8+4480z^9.
\]
There are exactly 896 bent concepts. All inclusion-maximal shattered sets have size nine, there are 4480 of them, and they form a **single** orbit under \(\operatorname{AGL}(4,2)\). In particular this is a pure eight-dimensional simplicial complex, and
\[\operatorname{VCdim}(\mathcal B)=\operatorname{Ldim}(\mathcal B)=9.\]

There are precise low-codimension obstructions: every support of at most six points is shattered; the 240 nonshattered seven-point sets are exactly the sets obtained by deleting one point from an affine hyperplane; and an eight-point set is shattered exactly when it has **no** complementing translation, i.e. there is no \(t\in V\setminus\{0\}\) such that \(S+t=V\setminus S\). Thus 2790 eight-point sets fail, in affine orbits of sizes 30, 840, and 1920.

## Assumptions and scope

The Walsh transform is \(W_f(u)=\sum_{x\in V}(-1)^{f(x)+u\cdot x}\). Bent means \(|W_f(u)|=4\) for all sixteen \(u\in V\). A support \(S\) is shattered when the restricted vectors \((f(x))_{x\in S}\), as \(f\) runs over all of \(\mathcal B\), realize all \(2^{|S|}\) binary assignments. An affine quadratic block is a zero or one set of a polynomial of degree at most two whose polar alternating bilinear form is nonsingular. A ten-point block is the larger of the two possible bent-function support sizes, six and ten. The claim is exact for four variables only. In particular, it does not claim the same characterization for six or more variables, for bent subsets, or for every quadratic function.

For reproducibility, number the sixteen points by \(x\in\{0,\ldots,15\}\) using their four binary coordinates, and encode any subset by the integer mask with bit \(x\) set if \(x\) belongs. The ordered quadratic monomials are indexed by \((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)\).

## Proof

**1. Complete concept enumeration.** Every bent function in four binary variables has algebraic degree at most two (the classical even-variable bent degree bound). Write it uniquely as
\[
f(x)=\sum_{0\le i<j<4}b_{ij}x_ix_j+\sum_{i=0}^3a_ix_i+c,
\qquad a_i,b_{ij},c\in\mathbb F_2.
\]
Its polar form is the alternating matrix with off-diagonal entries \(b_{ij}\). The Walsh-square identity shows that the function is bent precisely when this matrix is nonsingular: for a nonzero shift \(h\), the derivative \(f(x+h)+f(x)\) is a nonconstant affine function exactly when the polar radical is zero. The alternating forms of rank four number 28; multiplying by the 32 affine choices gives \(28\cdot32=896\) distinct functions. The Walsh condition independently enumerates exactly the same 896 truth tables. Their weights are exactly six or ten, with 448 of each weight. The independent Walsh verifier checks all \(2^{16}\) possible truth tables, not a sampled subcollection.

**2. Upper and necessity bounds.** A shattered support of size ten would require at least \(2^{10}=1024\) different concepts, more than 896. Larger sizes are excluded by downward closure. For any shattered \(S\) of size at least seven, the all-ones trace gives a bent support containing \(S\). Since a bent support has only six or ten points, it must be some \(Q\in\mathcal Q_{10}\). The size bound implies \(S\subsetneq Q\).

**3. Sufficiency from a single nine-point trace certificate and affine transitivity.** The representative mask \(S_0=\texttt{0x0777}\) has points \(\{0,1,2,4,5,6,8,9,10\}\) and is obtained from the ten-point block \(\texttt{0x8777}\) by deleting point fifteen. `nine_trace_witnesses.json` lists, for each of its 512 traces in lexicographic binary integer order, a complete 16-bit bent-function truth table attaining that trace; `verify_quadratic.py` checks every entry both for bentness and for the exact prescribed trace. Consequently \(S_0\) is shattered.

Affine changes of input coordinates preserve bentness, so \(\operatorname{AGL}(4,2)\) preserves shattering and \(\mathcal Q_{10}\). The four coordinate translations, three adjacent coordinate swaps, and three adjacent elementary shears generate this affine group. Breadth-first enumeration under those ten explicit generators gives an orbit of size 4480 for \(S_0\). Independently, the 448 distinct ten-point blocks have precisely 4480 *distinct* nine-point deletions. Distinctness follows also from the minimum four-point Hamming separation of different weight-ten bent functions: two distinct ten-point blocks meet in at most eight points. The script checks both orbit equality and maximum pairwise intersection eight. Hence **every** nine-point proper subset of a ten-point block belongs to the orbit of \(S_0\), and is shattered. Every smaller proper subset of any ten-point block extends to such a nine-point shattered subset and is therefore shattered.

**4. The six-point covering cutoff.** For the reverse implication on the remaining sizes, the complete ten-block list covers every \(S\subseteq V\) of size at most six. This is verified by enumerating all 448 blocks and their proper submasks, then checking each of the \(\sum_{k=0}^{6}\binom{16}{k}=14893\) supports. This is a complete finite check, not a probability estimate. Consequently all such supports satisfy the ten-block criterion and are shattered by Step 3. Together with Step 2 this proves the claimed if-and-only-if for all 65536 supports.

**5. Exact face counts and geometry.** Counting the distinct proper submasks of the 448 blocks by size gives
\[
(1,16,120,560,1820,4368,8008,11200,10080,4480).
\]
There is no ten-face; all maximal faces are the 4480 nine-point deletions. For seven-point supports, the 240 missing sets agree exactly with the 30 affine hyperplanes each with one of its eight points removed. For eight-point supports, the checker tests all \(\binom{16}{8}=12870\) possibilities and proves that failure is equivalent to the existence of \(t\ne0\) with \(S+t=V\setminus S\); affine orbit enumeration refines the failure count into 30, 840, and 1920. The complementary-translation criterion is the same geometric partition that appears in an existing classification of Walsh spectral partners, but the equivalence with bent-concept shattering is the additional conclusion here.

**6. Online dimension.** A shattered fixed nine-point support yields an adaptive binary query tree of depth nine, so \(\operatorname{Ldim}\ge9\). A complete adaptive binary tree of depth ten needs at least 1024 different concepts at its leaves, impossible with 896 functions. Hence the online dimension is exactly nine.

## Verification

Two independently structured standalone programs are supplied. `verify_quadratic.py` builds bent functions using six quadratic coefficients, \(\mathbb F_2\)-rank elimination, and affine terms; it reconstructs the ten-point blocks, covers every support up through size six, checks all 512 explicit trace witnesses for \(S_0\), enumerates the affine orbit, checks block intersections, and validates both the seven- and eight-point geometric failure criteria. Its success marker is `QUADRATIC_BENT_FACE_CERTIFICATE_PASS`.

`verify_walsh.cpp` instead loops over all 65,536 Boolean truth tables, applies an integer fast Walsh–Hadamard transform and selects the 896 bent tables by the sixteen exact \(\pm4\) Walsh conditions. It tests all 65,536 supports against all concept traces and independently compares the result with the ten-block proper-subset criterion and every face count. It requires a C++17 compiler and produces `INDEPENDENT_WALSH_TRACE_ENUMERATION_PASS`. The witness file is independent of the execution of either program and can be checked entry by entry. Run:

```sh
python3 verify_quadratic.py
c++ -O2 -std=c++17 verify_walsh.cpp -o verify_walsh
./verify_walsh
```

All arithmetic and comparisons are exact. No random sampling, floating point, or assumptions about external software packages enter the calculation.

## Relationship to prior work

Polujan and Pott (2020, arXiv:2003.12308) study designs and equivalences arising from Boolean and vectorial bent functions; their bent-function design definitions and affine equivalence are used as background, not claimed new. Meidl, Polujan and Pott (2020, arXiv:2012.06866) give design and automorphism results for quadratic bent functions, including the two-transitive associated designs; they do not provide this point-query shattering criterion, nine-dimensional VC/Littlestone calculation, or all-face polynomial. Hu, Weinberger and Shayevitz (2017, arXiv:1703.01586) study asymptotic VC dimension versus minimum distance for general binary codes, including a constant-weight upper bound, not exact restrictions of this nonlinear bent-function concept class.

The publicly available result *Replayable Walsh census of all 2^16 Boolean functions in n=4 and the 256 rotation-symmetric functions in n=5* records the classical 896 bent functions; that census is not a shattering-face classification. More closely, *Exact Walsh-spectrum multiplicities for eight-point subsets of the Boolean four-cube* proves an exact partition of eight-point sets by complementary translations and Walsh spectral bases, with counts 10080, 1920, 840, and 30. The same four orbit sizes occur here, but its orthogonality-basis existence theorem neither states nor supplies the nontrivial 512-trace realization needed for bent shattering, nor the pure nine-face complex. The eight-point orbit counts are credited and **not** asserted as new in isolation.

## Limitations

The primary theorem is finite and dimension-specific. The six-point block-covering fact and the affine orbit size are verified by a complete, transparent finite checker rather than by an unrestricted all-dimension closed-form argument; the second program independently tests the claimed output against all traces. The work does not establish analogous results in higher even dimension. Similar results in historical or unindexed literature may exist; the source comparison is not an independent priority certification. No independent mathematical audit is asserted.

## References

1. A. A. Polujan and A. Pott, *On design-theoretic aspects of Boolean and vectorial bent functions*, arXiv:2003.12308, initial public version 27 March 2020. https://arxiv.org/abs/2003.12308
2. W. Meidl, A. A. Polujan and A. Pott, *Linear codes and incidence structures of bent functions and their generalizations*, arXiv:2012.06866, initial public version 12 December 2020. https://arxiv.org/abs/2012.06866
3. S. Hu, N. Weinberger and O. Shayevitz, *On the VC-Dimension of Binary Codes*, arXiv:1703.01586, initial public version 5 March 2017. https://arxiv.org/abs/1703.01586
4. *Exact Walsh-spectrum multiplicities for eight-point subsets of the Boolean four-cube*, public research record, October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-walsh-spectrum-multiplicities-for-eight-point-subsets-of-t--b981e436a3b1
5. *Replayable Walsh census of all 2^16 Boolean functions in n=4 and the 256 rotation-symmetric functions in n=5*, public research record, September 2026. https://github.com/published-finding corpus/2026/tree/main/2026/9/8/SCOPE051
