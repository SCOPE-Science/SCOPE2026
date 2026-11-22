# Sharp zero-correlation shells and independent translated majority readouts

## Finding
Let \(d=2m+1\ge1\), let \(X\) be uniform on the binary cube \(\{0,1\}^d\), and write \(|x|\) for the number of one-bits in a vector. For any fixed mask \(u\), define \(I_u={\bf1}\{|X\oplus u|\le m\}\). These are fair zero-one majority readouts on a *common* underlying random vector, after deterministically complementing the coordinates indexed by \(u\).

**The independence classification.** For masks \(u,v\) separated by Hamming distance \(a=|u\oplus v|\), the variables \(I_u,I_v\) are independent precisely when
\[
 d\equiv3\pmod4,\qquad a\in\{(d-1)/2,(d+1)/2\}.
\]
For \(d\equiv3\pmod4\), their covariance is positive at smaller distances and negative at larger distances. For \(d\equiv1\pmod4\), it is positive through \(a=(d-1)/2\), negative from \(a=(d+1)/2\), and never zero.

**A multivariate consequence.** For every \(k\ge0\), there are four distinct fixed masks in dimension \(d=4k+3\) for which *each selection of three* translated-majority readouts is jointly independent. The theorem does not assert independence of all four simultaneously.

## Assumptions and scope
All coordinate bits of \(X\) are independent and fair; the masks are deterministic and no additional random noise is applied. Only odd dimensions are claimed, avoiding majority ties. The conclusions hold for each finite \(d\) exactly, without asymptotics. This is an exact covariance and independence result, not a distributional approximation for independently perturbed voters.

## Proof
Set \(B=\{x:|x|\le m\}\), so \(|B|=2^{d-1}\) by bitwise complementation and oddness of \(d\). Therefore \(\Pr(I_u=1)=1/2\). Translation invariance reduces the pair calculation to \(u=0\), \(v=(1,\dots,1,0,\dots,0)\) with \(a\) initial ones. Write
\[
 K_a=|B\cap(B\oplus v)|
 =\sum_{j=0}^{a}\sum_{\ell=0}^{d-a}
 \binom aj\binom{d-a}{\ell}
 {\bf1}\{j+\ell\le m,\ a-j+\ell\le m\}.
\]
Thus \(\operatorname{Cov}(I_u,I_v)=K_a/2^d-1/4\).

Compare two masks with \(a\) and \(a+1\) flipped coordinates, taking the last coordinate to be the one newly flipped. For a fixed assignment of the other \(d-1\) coordinates, let \(T\) and \(S\) be its distances from the two masks in those coordinates. Summing over the two possible final bits, the difference between the numbers of joint successes is exactly \({\bf1}\{T=m,S=m\}\). Indeed the four pairs of upper bounds are respectively \((m,m),(m-1,m-1)\) before flipping and \((m,m-1),(m-1,m)\) afterward; inclusion-exclusion of their indicators is one exactly at \(T=S=m\).

The equation \(T=S=m\) requires \(a=2s\) to be even. Of the first \(2s\) coordinates exactly \(s\) must be one, while among the remaining \(d-2s-1\) exactly \(m-s\) must be one. Hence for \(0\le s\le m\)
\[
 K_{2s}-K_{2s+1}=\binom{2s}s\binom{d-2s-1}{m-s}>0,
 \qquad K_{2s+1}-K_{2s+2}=0
\]
whenever the second expression has indices in range. In particular \(K_0>K_1=K_2>K_3=K_4>\cdots>K_d=0\) with the implied truncation at the boundary.

If \(\mathbf1\) is the all-one vector, \(B\oplus\mathbf1=B^c\). Replacing one of the two masks by its bitwise complement turns its distance \(a\) into \(d-a\), and partitions the successes with first mask fixed. Hence \(K_a+K_{d-a}=|B|=2^{d-1}\). At \(d=4k+3\), the central distances \(2k+1\) and \(2k+2\) form one equal plateau, and their complement identity forces both counts to be \(2^{d-2}\), exactly the threshold for independence. At \(d=4k+1\), the two central counts straddle a strict drop and thus lie strictly on opposite sides of \(2^{d-2}\). The complete sign and zero classifications follow from the strict staircase.

For the multivariate assertion, partition the \(4k+3\) coordinates into disjoint sets \(C,A_1,A_2,A_3\), where \(|C|=k\) and \(|A_j|=k+1\). Take four masks \(u_0=0\) and \(u_j={\bf1}_{C\cup A_j}\) for \(j=1,2,3\). Their six pairwise Hamming distances are \(2k+1\) or \(2k+2\); therefore every pair of readouts is independent. Simultaneously complementing every bit of \(X\) replaces all four readouts by their complements. For any three selected readouts, the associated fair signs have zero one- and two-variable moments by pairwise independence; their three-variable product also has expectation zero by global sign reversal. Fourier inversion on \(\{-1,1\}^3\) now gives the uniform distribution on all eight sign patterns. This proves three-wise independence.

## Verification
Run `python verify.py` in a Python 3 interpreter. The checker evaluates the exact overlap sums and their difference/complement laws at every odd dimension from \(1\) through \(61\); independently enumerates every input of dimensions through \(13\); and verifies all eight output patterns for every triple of the four constructed readouts at dimensions \(3,7,11,15\). It passed **2,115 exact assertions**. These finite checks test the algebra and boundaries; the proof above establishes all odd dimensions.

## Relationship to prior work
Mossel, O'Donnell and Oleszkiewicz study noise stability and extremal majority behavior for *independently correlated coordinate pairs*, rather than an exact predetermined set of flipped bits. Filmus, Kindler, Mossel and Wimmer prove an invariance principle for uniform Hamming-weight slices, not an exact classification of the zeros of translated-majority pair correlation. Standard Boolean-function autocorrelation is the equivalent language for this pair problem; the three-input majority autocorrelation table already has zeros at shifts of weights one and two. The present claim is confined to the exact all-odd-dimension zero set, its strict sign staircase, and the explicit three-wise-independent four-readout construction; it does not claim to introduce the autocorrelation formalism or the three-input example.

## Limitations
Only deterministic mask flips, fair independent input bits, and odd coordinate counts are treated. Pairwise independence alone would not guarantee three-wise independence without the explicit antipodal symmetry. No assertion is made concerning four-way independence of the constructed four readouts, nonuniform bits, even-dimensional tie rules, or noisy random masks. A general pre-existing exact majority-autocorrelation formula might imply the zero-set calculation indirectly; historical priority has not been independently settled. A 2013 article on balanced-Boolean autocorrelation distributions was accessible only at abstract level, not in full.

## References
- E. Mossel, R. O'Donnell and K. Oleszkiewicz, *Noise stability of functions with low influences: invariance and optimality*, arXiv:math/0503503, first posted 2005-03-23. https://arxiv.org/abs/math/0503503
- Y. Filmus, G. Kindler, E. Mossel and K. Wimmer, *Invariance principle on the slice*, arXiv:1504.01689, first posted 2015-04-07. https://arxiv.org/abs/1504.01689
- Y. Zhou, W. Zhang, J. Li, X. Dong and G. Xiao, *The autocorrelation distribution of balanced Boolean function*, Frontiers of Computer Science 7 (2013), 272–278, DOI:10.1007/s11704-013-2013-x. Abstract-only comparison.
- *Boolean Functions: The Basics*, section 5, autocorrelation table for three-input majority. https://booleanfunction.github.io/basics.html
