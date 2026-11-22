# A ninth-order quadratic Walsh resonance in descent profiles of \(132\)-avoiding permutations

## Finding

For \(n\geq 1\), let \(\operatorname{Av}_n(132)\) be the permutations of \(\{1,\ldots,n\}\) with no indices \(i<j<k\) satisfying \(\pi_i<\pi_k<\pi_j\). Their descent-profile counting kernel on \((\mathbb F_2)^{n-1}\) is
\[
f_n(x)=\#\{\pi\in\operatorname{Av}_n(132):\operatorname{Des}(\pi)=x\},
\quad \operatorname{Des}(\pi)=\{i:\pi_i>\pi_{i+1}\}.
\]
For each frequency set \(S\subseteq\{1,\ldots,n-1\}\), write the **unnormalized** Walsh multiplier
\[
W_n(S)=\sum_{\pi\in\operatorname{Av}_n(132)}(-1)^{|\operatorname{Des}(\pi)\cap S|}.
\]
Let \(C_n=\binom{2n}{n}/(n+1)\) be the Catalan number. **For every integer \(n\ge4\)**,
\[
\boxed{W_n(\{1,2\})=W_n(\{1,3\})
=C_n-4C_{n-1}+2C_{n-2}
=\frac{(n-2)(n-9)}{2(2n-3)(2n-1)}C_n.}
\]
In particular, these two distinct two-coordinate Fourier modes cancel **if and only if \(n=9\)**. At \(n=9\), all singleton modes survive, and **precisely four of the 28 two-coordinate modes cancel**: \(\{1,2\},\{1,3\},\{6,8\},\{7,8\}\). Direct exhaustive calculation further finds no two-coordinate cancellation for \(2\le n\le8\). Therefore the first cancellation in the *quadratic character band* (among all orders \(n\ge2\)) is at order nine; this does not assert first singularity of the full convolution operator.

## Assumptions and scope

The permutations are **labelled**, 132-avoidance is classical (not consecutive-pattern avoidance), descents refer to *positions*, and the Fourier group is the Boolean group of the \(n-1\) descent positions. The kernel retains multiplicities: different permutations with the same descent set contribute separately. The Fourier transform is not divided by the group size. The infinite identity concerns only the displayed two frequencies; the complete weight-two cancellation census is claimed only through order nine.

## Proof

Every \(132\)-avoiding permutation has a unique decomposition \(\pi=L\,n\,R\), with both sides avoiding \(132\), and every label in \(L\) exceeding every label in \(R\). If \(|L|=\ell\), \(|R|=r\), then the join at position \(\ell\) is an ascent when \(\ell>0\), the join at position \(\ell+1\) is a descent when \(r>0\), and the internal descent positions of \(L\) and \(R\) are copied and shifted, respectively. This proves the Catalan decomposition and gives all the signed recurrences below without probabilistic assumptions.

Let \(C=C(z)=\sum_{n\ge0}C_nz^n\), so \(C=1+zC^2\), and hence \(1-zC=C^{-1}\). Define four formal series, each starting at the smallest indicated length:
\[
B=\sum_{n\ge2}W_n(\{1\})z^n,\quad
E=\sum_{n\ge3}W_n(\{2\})z^n,\quad
A=\sum_{n\ge3}W_n(\{1,2\})z^n,\quad
D=\sum_{n\ge4}W_n(\{1,3\})z^n.
\]
Splitting by \(\ell=0,1,2,3\) or \(\ell\) larger, as applicable, gives exact formal-series identities
\[
\begin{aligned}
(1-zC)B&=-z(C-1)+z^2C,\\
(1-zC)E&=zB-z^2(C-1)+2z^3C,\\
(1-zC)A&=-zB-z^2(C-1),\\
(1-zC)D&=-zE+z^2B-z^4C.
\end{aligned}
\]
The second identity uses the two permutations on the two-element left side when \(\ell=2\); the final identity uses \(W_3(\{1\})=-1\) on the three-element left side when \(\ell=3\). These are the boundary terms most easily lost if one shifts descent positions incorrectly.

Substituting \(1-zC=C^{-1}\) and \(zC^2=C-1\) gives
\[
B=(2z-1)C+1-z,\qquad
E=(2z-1+2z^2)C+1-z-2z^2,
\]
\[
A=(1-4z+2z^2)C-1+3z,\qquad D=A+z^3.
\]
For each \(n\ge4\), the coefficients of \(z^n\) in \(A\) and \(D\) coincide and equal \(C_n-4C_{n-1}+2C_{n-2}\). Using \(C_{n-1}/C_n=(n+1)/(2(2n-1))\) and \(C_{n-2}/C_{n-1}=n/(2(2n-3))\), this is exactly the stated rational multiple of \(C_n\). For \(n\ge4\) all denominator factors and \(C_n\) are strictly positive, and the sole zero occurs at \(n=9\).

For the finite assertion, `checker.py` independently enumerates all \(n!\) permutations through \(n=9\), rejects those containing a 132 pattern by direct three-index comparison, accumulates the descent-profile counts, and applies a full integer Walsh–Hadamard transform. It checks the transform **character by character** against an independent signed recursion from the maximum-element decomposition. The exhaustive frequency list for \(n=9\) has exactly the four displayed zeros at weight two and no zeros at weight one. All smaller orders have no weight-two zeros. Since every permutation and every relevant Boolean frequency was enumerated, these finite checks are exhaustive certificates, not a statistical sample.

## Verification

Run `python3 checker.py` from the directory containing this result and the checker. It uses Python's standard library, exhaustively verifies both independently implemented transforms through order nine, and verifies the displayed two-character formula against the recursive transform for orders four through 34. It prints `PASS: independent brute, two-coordinate table and infinite-formula finite replay` on success. The formal-series derivation above proves the full infinite statement independently of the finite computations.

## Relationship to prior work

Reifegerste's descent/excedance bijection (2002, Proposition 2.4) equates the **entire descent-set distribution** on \(132\)-avoiding permutations to a corresponding excedance-set distribution on \(321\)-avoiders. It is a stronger structural equivalence at the level of distributions, but does not itself evaluate the two fixed-position signed moments above or identify their isolated ninth-order zero. Mansour (2004) studies sign-balance and positional ascents/descents in \(132\)-avoiders; his permutation **inversion sign** and first/last-descent results are distinct from the Walsh parity of the specific pairs of descent indicators evaluated here. Barnabei–Bonetti–Silimbani (2010) discuss the Dyck-valley interpretation of \(132\)-descent enumeration and focus on the aggregate descent statistic for \(123\)-avoiders.

Two related subsequently published computational studies examine Fourier convolution from the **inversion-incidence** embeddings of pattern-avoiding permutations and **quadratic sampling** of laws on stack-sortable permutations. Neither statement yields the exact fixed-position descent-profile multipliers without additional signed enumeration. The new content claimed is narrowly the two-frequency all-length identity and the exhaustive first degree-two cancellation census, not the Catalan count, the bijection, or an arbitrary-character spectrum theorem.

## Limitations

The exact full weight-two census was checked only through \(n=9\). No classification of weight-two zero frequencies for \(n>9\), no full Fourier rank, and no arbitrary-frequency invertibility statement is implied. Priority remains provisional against any unindexed equivalent signed descent-moment computation, especially formulations transported through Reifegerste's bijection. The finite verifier is complete for the indicated small orders but is not a proof of the infinite identity; the explicit generating-function argument is that proof. Independent review has not been performed.

## References

1. A. Reifegerste, *On the diagram of 132-avoiding permutations* (first public arXiv version 2002-08-01), https://arxiv.org/abs/math/0208006 , especially Proposition 2.4.
2. T. Mansour, *Equidistribution and sign-balance on 132-Avoiding Permutations*, Séminaire Lotharingien de Combinatoire 51 (2004), https://www.mat.univie.ac.at/~slc/wpapers/s51mansour.pdf .
3. M. Barnabei, F. Bonetti, M. Silimbani, *The descent statistic on 123-avoiding permutations*, Séminaire Lotharingien de Combinatoire 63 (2010), https://www.mat.univie.ac.at/~slc/wpapers/s63barnbosi.pdf .
4. *First Walsh-rank separation and endpoint-stability contrast for 123- and 132-avoiding permutations* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-first-walsh-rank-separation-and-endpoint-stability-contrast-for--f516d96e4111 .
5. *Quadratic Walsh tomography of stack-sortable permutations: first failure at six positions* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-quadratic-walsh-tomography-of-stack-sortable-permutations-first--f9b612ba445d .
