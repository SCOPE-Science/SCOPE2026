# Exact inverse fibers and output capacities of cyclic Rule 254 on the golden-mean constraint

## Finding

Fix an integer \(n\ge1\). On indexed binary rings let
\[
X_n=\{x\in\{0,1\}^n:x_ix_{i+1}=0\text{ for every }i\pmod n\},\qquad
(F_nx)_i=x_{i-1}\lor x_i\lor x_{i+1}.
\]
The repeated indices at \(n=1,2\) are intentional. This is elementary cellular automaton Rule 254 (three-neighbor Boolean OR), **restricted on its input** to the golden-mean constraint. Write \(p_n(y)=|\{x\in X_n:F_nx=y\}|\).

For every nonconstant cyclic output \(y\), let \(L_1,\ldots,L_k\) be the lengths of its maximal cyclic runs of ones. Define \(c_t=0\) for \(t<0\), \(c_0=1\), and \(c_t=c_{t-2}+c_{t-3}\) for \(t\ge1\) (all negative-index terms zero). Then
\[
\boxed{p_n(y)=\prod_{j=1}^{k}c_{L_j-3},\qquad
\sum_{t\ge0}c_tz^t=\frac1{1-z^2-z^3}.}
\]
The two constant-output cases are \(p_n(0^n)=1\), and \(p_n(1^n)=P_n\) for \(n\ge2\), where the known Perrin sequence is determined by \(P_0=3,P_1=0,P_2=2\) and \(P_n=P_{n-2}+P_{n-3}\) for \(n\ge3\). At \(n=1\), \(p_1(1)=0\).

Thus for \(n\ge2\), an output is attainable exactly when it is all zero, all one, or every cyclic run of ones has length \(3\) or at least \(5\). Equivalently, attainable cyclic outputs avoid all three cyclic subwords \(010\), \(0110\), and \(011110\); at \(n=1\), only \(0\) is attainable. Nonconstant attainable outputs have a unique preimage exactly when every one-run length belongs to \(\{3,5,6,7\}\); the all-zero output is uniquely invertible and the all-one output is not for \(n\ge2\).

Let \(I_n=|F_n(X_n)|\) and \(U_n=|\{y:p_n(y)=1\}|\) for \(n\ge1\). Set
\[
D_I(z)=1-2z+z^2-z^4+z^5-z^6,\qquad
D_U(z)=1-z-z^4-z^6-z^7-z^8.
\]
Their **all-length, indexed cyclic-word** enumerators are
\[
\boxed{\sum_{n\ge1}I_nz^n=-z-z\frac{D_I'(z)}{D_I(z)},\qquad
\sum_{n\ge1}U_nz^n=-z\frac{D_U'(z)}{D_U(z)}.}
\]
Write \(\rho_I\) and \(\rho_U\) for the unique smallest-modulus zeros of \(D_I\) and \(D_U\), respectively, both positive and simple. Then
\[
I_n\sim\rho_I^{-n},\quad U_n\sim\rho_U^{-n},\quad
\frac{U_n}{I_n}\sim\left(\frac{\rho_I}{\rho_U}\right)^n
\approx(0.9789942886\ldots)^n.
\]
In particular the uniquely decodable output fraction vanishes exponentially.

## Assumptions and scope

All words have labelled/indexed sites, not necklaces modulo rotation, and all subscripts are computed modulo \(n\). The fiber counts are for one synchronous local update and inputs avoiding cyclic adjacent ones; outputs are unrestricted until reachability is tested. The standard cycle graph convention for \(n=1\) is replaced by the explicit modulo-index rule above. Perrin counts at the all-one output are acknowledged as known maximal-independent-set counts, not a newly claimed result. No noisy measurements, iterated dynamics, or claims about inverse algorithms on arbitrary nonlinear maps are included.

## Proof

**Boundary and run factorization.** An input one at site \(i\) covers exactly the three sites \(i-1,i,i+1\) of the output. If a nonconstant output has a maximal one-run occupying sites \(a,a+1,\ldots,b\) of length \(L\), the zeros at \(a-1\) and \(b+1\) force the first input one covering the run to be at \(a+1\) and the last to be at \(b-1\). Every intervening input one lies in that run. The source restriction forbids consecutive input ones, so successive input-one positions differ by at least two. Absence of holes in the output run forces each such difference to be at most three. Conversely, any chain of positions starting at \(a+1\), ending at \(b-1\), and using only differences two and three is a valid set of nonadjacent input ones whose radius-one OR image is exactly that output run. Its successive differences sum to \(L-3\), proving that the number of choices is the number of ordered compositions of \(L-3\) into parts two or three, namely \(c_{L-3}\). Input choices for distinct output one-runs are independent: their bounding zeros force the nearest chosen centers to be at least four positions apart across each zero-run. Multiplication proves the stated formula, including the impossible lengths \(1,2,4\) and all finite-run cases.

**Constant outputs and finite-type criterion.** Only the all-zero input maps to zero. An all-one output is obtained exactly when the chosen input-one sites are an independent dominating set of the ring, equivalently a maximal independent set. Their classical Perrin enumeration holds for \(n\ge2\), while the self-neighbor constraint at \(n=1\) forces the input to zero. A finite one-run of length \(L\) has a predecessor exactly when \(L-3\) is a sum of twos and threes; this occurs for \(L=3\) and every \(L\ge5\). Every cyclic nonconstant word has finite runs, so the three listed forbidden blocks are precisely the obstruction patterns. An admissible finite run has one covering chain exactly when \(L-3\in\{0,2,3,4\}\), yielding one-run lengths \(\{3,5,6,7\}\). For \(n\ge2\), the Perrin count is at least two, excluding the all-one output from the unique-fiber class. The same three forbidden finite blocks characterize the full bi-infinite image: cover each finite one-run by the same chains and choose two/three-spaced centers along any unbounded one-run, which is possible independently of all zero-separated finite runs.

**Cyclic enumerators.** Let \(A(z)=z^3+z^5/(1-z)\) enumerate allowed finite one-run lengths, and \(B(z)=z/(1-z)\) enumerate positive zero-run lengths. A nonconstant indexed cyclic output is a cyclic sequence of positive run-pairs, with one member from \(A\) and one from \(B\). A term with \(k\) pairs, length \(n\), is counted \(n/k\) times among ordered run-pair lists with a chosen starting site: there are \(n\) choices of label-origin but \(k\) choices of distinguished run. Therefore the length generating function for such outputs is
\[
-z\frac{d}{dz}\log(1-A(z)B(z)).
\]
Since \(1-AB=D_I(z)/(1-z)^2\), adding the constant outputs (one at \(n=1\), two for each \(n\ge2\)) gives \(-z-zD_I'/D_I\). Replacing \(A\) by \(A_U(z)=z^3+z^5+z^6+z^7\), and adding only the all-zero uniquely invertible output at each length, yields \(1-A_UB=D_U/(1-z)\) and \(-zD_U'/D_U\). This counts **different labelled output words**, rather than predecessor words or rotation classes.

**Asymptotic argument.** Both renewal products \(AB\) and \(A_UB\) have nonnegative coefficients, and both contain positive coefficients at consecutive lengths four and five. They are strictly increasing on the positive real interval up to one and have unique positive roots \(\rho_I,\rho_U\) of \(AB=1\) and \(A_UB=1\). The triangle inequality and the coprime supported lengths four and five imply no other root has equal or smaller modulus; differentiating each renewal denominator shows its positive zero is simple. Since \(A_U(z)<A(z)\) for positive \(z\) strictly below one, \(\rho_I<\rho_U\). The logarithmic derivative of a denominator with a simple dominant zero has coefficient \(\rho^{-n}\) with leading constant exactly one. All other poles are of greater modulus, giving the claimed asymptotic quotient.

## Verification

Run `python3 verify.py` using only the Python standard library. The script directly enumerates all admissible binary inputs and all binary output strings on every indexed ring of lengths \(1\) through \(18\), checks the run-product fibers, forbidden-block image criterion, and independently generated coefficients of both rational generating functions. It checks the small-size exceptional ring convention. All reported finite tests passed, but the all-length assertions are supported by the preceding proof, not by extrapolation from finite checks.

The first twelve image counts are \((1,2,2,6,7,14,23,38,56,87,134,210)\). The first twelve unique-fiber counts are \((1,1,1,5,6,13,22,37,46,66,100,161)\).

## Relationship to prior work

Salo's 2022 work studies invertibility, regularity, periodic points, and finite-type images for cellular automata, including a golden-mean argument for a different rule (Rule 28). It does not state the Rule-254 hard-core restricted fiber classification or these image-count series. The Perrin enumeration of maximal independent sets of cycles is classical and explicitly appears in Bisdorff and Marichal (2008); it covers only the all-one output case here. General unrestricted-source Rule-254 and other elementary-rule image results do not imply the restricted-source individual fiber formula without an additional argument. The substantive claim here is the product factorization, exact constrained image and unique-fiber spectra, and resulting entropy separation.

## Limitations

Historical mathematical equivalence under a different description of independent-set dilation or interval covering remains possible despite searches. The result gives combinatorial, not biological or noisy-channel, reconstruction guarantees. The all-one Perrin identity is prior knowledge. Finite code checks are corroboration only, not an infinite proof.

## References

- V. Salo, “On von Neumann regularity of cellular automata,” arXiv:2209.13373 (first public 27 September 2022), https://arxiv.org/abs/2209.13373.
- R. Bisdorff and J.-L. Marichal, “Counting Non-Isomorphic Maximal Independent Sets of the n-Cycle Graph,” *Journal of Integer Sequences* **11** (2008), Article 08.5.7, https://cs.uwaterloo.ca/journals/JIS/VOL11/Marichal/marichal.pdf.
- Wolfram Atlas, “Elementary Cellular Automaton Rule 254,” https://atlas.wolfram.com/01/01/254/ (local-rule identification, not a source for the new enumeration).
