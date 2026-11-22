# A third-root Fano window is full spark on the seven-cycle

## Finding

Let \(\omega=\exp(2\pi i/3)\) and \(\xi=\exp(2\pi i/7)\). On \(\mathbb Z/7\mathbb Z\), consider
\[
g=(1,\omega,\omega,1,\omega,1,1),\qquad
 g(x)=\omega^{\mathbf 1_{\{1,2,4\}}(x)}.
\]
The set \(\{1,2,4\}\) is a cyclic \((7,3,1)\) difference set. Its two-phase, third-root-valued window generates the **full-spark** system
\[
\{M^bT^ag:(a,b)\in(\mathbb Z/7\mathbb Z)^2\},
\]
so every choice of seven of its 49 vectors is a basis of \(\mathbb C^7\).

The least root-of-unity alphabet order permitting such a window is **exactly three**: no \(\mu_1\)- or \(\mu_2\)-valued window has this property. This is a statement about the least integer \(q\) for which a window with entries in \(\mu_q\) exists; it is **not** a claim that three distinct phase symbols are needed. The exhibited window uses only \(1\) and \(\omega\).

## Assumptions and scope

For \(x,a,b\in\mathbb Z/7\mathbb Z\), define \((T^ag)(x)=g(x-a)\), \((M^bg)(x)=\xi^{bx}g(x)\), and
\[
G_g(x,(a,b))=\xi^{bx}g(x-a).
\]
Column index \(c=7a+b\) ranges from 0 to 48. Full spark means every set of seven distinct columns is linearly independent over \(\mathbb C\). All claims concern this precise synthesis matrix and root-of-unity alphabets \(\mu_q=\{z\in\mathbb C:z^q=1\}\). No optimal conditioning, phase retrieval, or infinite-dimensional assertion follows.

## Proof

**1. Symmetry reduction.** The shift-modulation commutation law implies that applying an inverse Weyl shift to all selected columns transforms a seven-column minor, up to nonzero column multipliers and an invertible left factor, into a minor including \((a,b)=(0,0)\). Thus every seven-column selection is represented among exactly \(\binom{48}{6}=12,271,512\) subsets containing column 0.

**2. Reduced minor.** Each coordinate \(g(x)\) is nonzero. Divide row \(x\) by \(g(x)\); column 0 becomes constant 1. Subtract row 0 from each of the other rows. A normalized seven-by-seven minor is nonzero if and only if the corresponding six-by-six matrix is invertible, with rows \(x=1,\ldots,6\) and nonzero selected column labels \(c=7a+b\):
\[
D_{x,c}=\xi^{bx}\frac{g(x-a)}{g(x)}-\frac{g(-a)}{g(0)}.
\]
Every transformation preserves the zero/nonzero determinant distinction.

**3. Exact finite-field certificate for full spark.** The accompanying standalone program `ternary_full_spark.c` evaluates these entries in the prime field \(\mathbb F_{2000000143}\), mapping \(\xi\) to 1917252147 and \(\omega\) to 1620913102. Both images have respectively exact multiplicative orders seven and three; the prime modulus is verified independently. A deterministic enumeration visits all 12,271,512 increasing six-subsets of the 48 nonzero column labels and checks invertibility by elementary, nondividing, rank-preserving row operations. Every reduced minor is nonsingular. The map \(\mathbb Z[\xi,\omega]\to\mathbb F_{2000000143}\) sends zero to zero, so nonzero reduction of a determinant **proves its characteristic-zero determinant is nonzero**. Consequently \(G_g\) is full spark. A genuinely different Leibniz dynamic-programming determinant calculation in \(\mathbb F_{1300000003}\) verifies the same 12,271,512 minors; its primitive root images are 968223065 and 90783893, respectively.

**4. Exclusion of binary alphabets.** Global sign does not affect spark, so normalize the first sign to \(+1\) and enumerate the 64 possibilities for the remaining six signs. `binary_witnesses.csv` lists, for each mask, seven distinct columns including column 0. `binary_certificates.c` finds and checks each witness at all six primitive seventh-root images in \(\mathbb F_{2000000143}\); `direct_integer_checks.py` **independently expands every one of the 64 determinant witnesses in** \(\mathbb Z[\xi]\), confirming that its six cyclotomic coefficients vanish in the quotient by \(1+X+\cdots+X^6\). For the finite-field certificate, the underlying determinant polynomial has seven coefficients of absolute value at most \(7!=5040\). Vanishing at all six primitive seventh-root residues forces those coefficients to be congruent to one another modulo the prime. Because their absolute differences do not exceed \(10080\), smaller than the modulus, they are actually equal in \(\mathbb Z\). Hence each determinant vanishes exactly over \(\mathbb C\). A constant window is included among these masks, proving the \(q=1\) exclusion also.

Together, the exhaustive positive and negative certificates prove the stated alphabet threshold.

## Verification

Build and run `REPRODUCE.sh` with a C11 compiler and Python 3. It compiles and runs two full positive checkers, regenerates the 64 negative certificates and compares their exact CSV bytes, and runs the independent cyclotomic integer-ring checker. The expected success outputs are: `SUCCESS all 12271512 reduced minors nonzero`, `PASS 12271512 minors`, `PASS 64 binary exact cyclotomic determinant certificates`, and `PASS 300 independent exact integer-ring ternary spot checks`. All enumerations are finite and exhaust their declared domains; the integer-ring spot checks are supplementary rather than the basis of full-spark proof. The prime moduli, order checks, row formula, and enumeration loops are fully contained in the source files.

## Relationship to prior work

Lawrence–Pfander–Walnut proved generic full-spark behavior for prime cyclic Gabor systems. Malikiosis subsequently proved existence in every cyclic dimension and constructed an explicit root-of-unity family using \((N-1)^4\)-th roots (for length seven, root order 1296). These theorems do not identify this third-root window or the least allowable cyclic phase alphabet. Malikiosis's later spark-deficiency theorem concerns noncyclic groups and particular symmetry-restricted cyclic vectors, not a classification of all seven-point third-root windows. General Gabor tomography and ambiguity-function rank results concern different observables from all maximal minors of the synthesis frame. The known binary obstruction is reproduced independently here; the new positive construction is not a corollary of that negative fact.

## Limitations

The result identifies an explicit full-spark window and the **least integer root alphabet order** only in dimension seven. It does not classify all third-root windows or quantify worst-case condition numbers. A third root alphabet contains two nontrivial phase values, but the construction itself requires only two *distinct* values; thus no minimal distinct-symbol statement is asserted. Originality is assessed against the cited primary texts and accessible indexed literature; an unindexed exact earlier example or an inaccessible relevant full text could preempt priority. No independent mathematical audit has been performed.

## References

1. J. Lawrence, G. E. Pfander, D. Walnut, *Linear Independence of Gabor Systems in Finite Dimensional Vector Spaces*, Journal of Fourier Analysis and Applications 11 (2005), 715–726.
2. R.-D. Malikiosis, *A Note on Gabor Frames in Finite Dimensions*, arXiv:1304.7709v1, publicly posted 29 April 2013, https://arxiv.org/pdf/1304.7709 (especially Theorem 1.2 and §5, Corollary 5.3).
3. R.-D. Malikiosis, *Spark Deficient Gabor Frames*, arXiv:1602.09012v1, publicly posted 29 February 2016, https://arxiv.org/pdf/1602.09012 (especially §§1–4).
4. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614 (2026), https://arxiv.org/abs/2609.09614; the publicly accessible abstract was compared, not its full text.
