# Inverse-list spectra and a geometric decoding law for run-capped binary deletion channels

## Finding
Fix an integer \(h\ge1\). Let \(\mathcal L_h(n)\) be the set of binary words of length \(n\) in which every maximal constant run has length at most \(h\). For every received word \(y\in\{0,1\}^m\), \(m\ge1\), define
\[
P_h(y)=\bigl|\{x\in\mathcal L_h(m+1):\text{deleting one symbol of }x\text{ can produce }y\}\bigr|.
\]
Distinct parent *words*, not deletion positions or embeddings, are counted.

**Exact inverse-list classification.** If every constant run of \(y\) has length at most \(h\), and \(b_h(y)\) is the number of its maximal runs having length exactly \(h\), then
\[
P_h(y)=m+2-b_h(y).
\]
If precisely one run has length \(s>h\), all others have lengths at most \(h\), and \(s\le2h\), then
\[
P_h(y)=2h-s+1.
\]
In all other cases \(P_h(y)=0\). Consequently a received word is uniquely decodable if and only if it has precisely one constant run of length \(2h\) and all other runs are of length at most \(h\).

**Complete finite-length distribution.** Let \(N_{h,m,j}\) count received words of length \(m\) with exactly \(j\ge1\) distinct valid parents. Define \(A_h(z)=z+z^2+\cdots+z^h\) and
\[
B_h(z,t)=\sum_{a=1}^{h-1}z^a t^a+z^h t^{h-1}.
\]
Then, as an identity of formal power series in \(z\) with coefficients polynomial in \(t\),
\[
\boxed{\sum_{m\ge1}\sum_{j\ge1}N_{h,m,j}z^mt^j
=\frac{2t^2 B_h(z,t)}{1-B_h(z,t)}
+\frac{2\sum_{s=h+1}^{2h}z^s t^{2h-s+1}}{(1-A_h(z))^2}.}
\]
In particular, with \(U_{h,m}=N_{h,m,1}\),
\[
\boxed{\sum_{m\ge1}U_{h,m}z^m=\frac{2z^{2h}}{(1-A_h(z))^2}.}
\]
The generating function of all feasible receiver words is obtained by putting \(t=1\) in the boxed distribution. The number with zero parents is \(2^m-\sum_{j\ge1}N_{h,m,j}\). For \(h\ge2\), the maximum list size for length \(m\) is \(m+2\); for \(h=1\), it is \(2\).

**Limiting decoding-list law.** For \(h\ge2\), let \(\rho_h\in(0,1)\) be the unique solution of \(A_h(\rho_h)=1\). Choose uniformly among the *distinct feasible* received words of length \(m\). For every \(1\le j\le h\),
\[
\boxed{\lim_{m\to\infty}\Pr(P_h(y)=j\mid P_h(y)>0)
=\frac{\rho_h^{h-j}}{\sum_{r=0}^{h-1}\rho_h^r}.}
\]
The limiting mass on lists of size greater than \(h\) is zero. In particular, unique-decoding observations have strictly positive limiting density; when \(h=2\), this density is \((3-\sqrt5)/2\). At \(h=1\), their feasible-output density tends to one.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), the original is a finite, ordered, *linear* word with two free endpoints, and exactly one symbol is deleted at an unknown position. Run limits apply to the original source only; received words may violate them. The bounds include \(h=1\) and all positive receiver lengths. Rotation classes, cyclic words, weighted deletion histories, and multiple deletions are not considered.

## Proof
For a fixed received binary word of length \(m\), the number of *distinct unrestricted* one-symbol supersequences is \(m+2\). There are \(2(m+1)\) position/bit insertion choices. Inserting the same bit into any one maximal run of length \(a\) produces just one distinct run-extension word instead of \(a+1\) choices. Summing the \(a\) redundant positions across all runs subtracts \(m\), giving \(2(m+1)-m=m+2\).

If the receiver already obeys the cap, a distinct supersequence fails the cap precisely when it extends a maximal receiver run of length \(h\). There is exactly one extension word for each such run, and different runs lead to different extension words; no insertion can lengthen more than one maximal run. Subtracting \(b_h(y)\) gives the first case. It is never a singleton: \(m+2-b_h(y)\ge2\), because \(b_h(y)\le m\).

If the receiver contains a run of length \(s>h\), any admissible parent must insert the *opposite* bit strictly inside that run. The two pieces of the split run must both have positive lengths at most \(h\). These conditions have exactly \(2h-s+1\) solutions when \(h<s\le2h\), and none for \(s>2h\). An insertion cannot repair two distinct overlong runs. The parent word is distinct for every allowed split and no other run is altered. This proves the complete three-case classification, including the singleton criterion \(s=2h\).

To enumerate the first case, write every admissible nonempty receiver as an alternating sequence of positive-length runs, each of size \(1,\ldots,h\), and choose the initial bit in two ways. A run of length \(a<h\) contributes \(z^a t^a\), while a run of length \(h\) contributes \(z^h t^{h-1}\). The additional factor \(t^2\) accounts for the \(m+2\) term. Summing over one or more runs gives \(2t^2B_h/(1-B_h)\).

For the second case, choose the single long run \(s\in\{h+1,\ldots,2h\}\), its initial binary value in two ways, and two independently chosen possibly-empty ordered sequences of ordinary runs on its left and right. Each ordinary run has a length in \(1,\ldots,h\). This yields \(2z^s(1-A_h(z))^{-2}\) words, each with list size \(2h-s+1\). Summation gives the second rational summand. Extracting \(t^1\) requires \(s=2h\), proving the unique-decoding generating function. Alternating words have no length-\(h\) runs for \(h\ge2\) and attain the bound \(m+2\).

For the limit law, \(1-A_h(z)\) has a simple positive zero at \(\rho_h\). As \(h\ge2\) includes a run of length one and of length two, the coefficient sequence is aperiodic, so no other singularity lies on \(|z|=\rho_h\). The contribution of receivers with all runs at most \(h\) has only a simple pole, while each possible single overlong run gives a positive double-pole contribution. The leading coefficients of these double-pole terms are proportional to \(\rho_h^s m\rho_h^{-m}\). Normalizing over \(s=h+1,\ldots,2h\) and replacing \(s\) with \(2h-j+1\) yields the displayed truncated geometric law. For \(h=1\), the full feasible-output series equals \(2z/(1-z)+2z^2/(1-z)^2\), and the singleton series equals \(2z^2/(1-z)^2\), giving limiting fraction one.

## Verification
Run the self-contained Python 3 checker `verify.py` in the same directory. It independently enumerates every possible source insertion and compares the parent set to the run formula, then independently constructs the formal-series coefficient histogram from run compositions. This checks all \(20{,}470\) received words over caps \(1\le h\le5\) and lengths \(1\le m\le11\), including \(123{,}144\) parent incidences. The printed `VERIFY_OK` is a finite sanity check, not a substitute for the preceding all-length proof.

## Relationship to prior work
Atashpendar et al. study unrestricted binary supersequence and deletion-embedding distributions; their source set is not homopolymer capped. Kovačević and Vukobratović develop RLL source growth and bounds for deletion-correcting codes, not the complete inverse-fiber distribution over all possible received words. Takemoto and Nozaki construct efficient run-capped insertion/deletion-correcting codes, not the unconstrained-receiver list spectrum. The present statement is about every received word, including inadmissible words that become feasible only after a deletion; these words dominate the limiting feasible-output distribution. Classical one-insertion supersequence counting provides one ingredient but does not itself give the cap-dependent inverse-list classification and its geometric asymptotic law.

## Limitations
Novelty is assessed against the identified literature and accessible mathematical records, not guaranteed against unindexed publications or implicit presentations using a more general constrained-channel formalism. The limiting law samples uniformly from distinct feasible outputs, not according to the probability of outputs from uniformly sampled sources or deletion positions. The proof does not address error-correcting code optima, weighted preimage likelihoods, or more than one deletion. The work has not undergone an independent mathematical audit.

## References
- A. Atashpendar et al., *From Clustering Supersequences to Entropy Minimizing Subsequences for Single and Double Deletions*, arXiv:1802.00703 (first public version 2018-02-02), https://arxiv.org/abs/1802.00703.
- M. Kovačević and D. Vukobratović, *Asymptotic Behavior and Typicality Properties of Runlength-Limited Sequences*, arXiv:2105.04617 (first public version 2021-05-10), https://arxiv.org/abs/2105.04617.
- R. Takemoto and T. Nozaki, *Construction and Encoding Algorithm for Maximum Run-Length Limited Single Insertion/Deletion Correcting Code*, arXiv:2012.13536 (first public version 2020-12-25), https://arxiv.org/abs/2012.13536.
