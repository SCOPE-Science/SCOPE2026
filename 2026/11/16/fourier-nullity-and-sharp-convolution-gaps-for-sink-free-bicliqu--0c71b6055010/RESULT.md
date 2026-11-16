# Fourier nullity and sharp convolution gaps for sink-free biclique orientations

## Finding
For every integer \(n\geq3\), the indicator of sink-free orientations of the complete bipartite graph \(K_{2,n}\), encoded as a function on \(G_n=(\mathbb F_2)^{2n}\), has exactly \((3^n-1)/2\) vanishing unnormalized Walsh--Fourier coefficients. In particular, convolution by this indicator has rank
\[
\operatorname{rank}C_n=4^n-\frac{3^n-1}{2}.
\]
Its smallest nonzero Fourier-multiplier magnitude is precisely \(2\), hence \(\|C_n^\dagger\|_{2\to2}=1/2\), and its positive-spectrum condition number is \((3^n-2^{n+1}+1)/2\). Although each such convolution is singular, its relative nullity tends to zero exponentially, asymptotic to \(\tfrac12(3/4)^n\). The boundary cases are: for \(n=1\), no sink-free orientations and rank zero; for \(n=2\), exactly eight vanishing multipliers, rank eight, and smallest nonzero magnitude two.

## Assumptions and scope
Let the two vertices in the small part of \(K_{2,n}\) be hubs \(L,R\), with remaining vertices \(w_1,\ldots,w_n\). An orientation is encoded by \(x,y\in\mathbb F_2^n\): \(x_i=1\) if the edge \(Lw_i\) points from \(w_i\) toward \(L\), and \(y_i=1\) if \(Rw_i\) points from \(w_i\) toward \(R\). Thus every \(w_i\) has positive outdegree exactly when its column \((x_i,y_i)\) is one of \((1,0),(0,1),(1,1)\). Hub \(L\) has positive outdegree exactly when a column \((0,1)\) occurs; hub \(R\) exactly when a column \((1,0)\) occurs. Consequently the sink-free support \(S_n\) consists of length-\(n\) words over these three columns containing both \((1,0)\) and \((0,1)\).

For \((u,v)\in G_n\), let \(\chi_{u,v}(x,y)=(-1)^{u\cdot x+v\cdot y}\). Set \(W_n(u,v)=\sum_{(x,y)\in S_n}\chi_{u,v}(x,y)\), using unnormalized Walsh transforms. Define the convolution \(C_nf(z)=\sum_{s\in S_n}f(z+s)\) on \(\ell^2(G_n)\) with counting measure. Its character eigenvalues are \(W_n(u,v)\).

## Proof
**Exact formula.** Let \(a\) be the number of indices where \((u_i,v_i)=(0,0)\); let \(|u|\) and \(|v|\) be Hamming weights. For a column in the three-letter alphabet, the character sum equals \(3\) when \((u_i,v_i)=(0,0)\) and \(-1\) otherwise. Its product across all columns is \((-1)^{n-a}3^a\). Remove words with no \((1,0)\): the remaining alphabet is \((0,1),(1,1)\), whose character sum is \(2^n\mathbf 1_{u=0}(-1)^{|v|}\). Removing words with no \((0,1)\) similarly contributes \(2^n\mathbf 1_{v=0}(-1)^{|u|}\). Their intersection consists of the all-\((1,1)\) word and contributes \((-1)^{|u|+|v|}\). Inclusion--exclusion therefore gives, at every frequency,
\[
W_n(u,v)=(-1)^{n-a}3^a+(-1)^{|u|+|v|}-2^n\big(\mathbf 1_{u=0}(-1)^{|v|}+\mathbf 1_{v=0}(-1)^{|u|}\big). \tag{1}
\]
At the trivial frequency, \(|S_n|=3^n-2^{n+1}+1\).

**All zeros when \(n\geq3\).** At a frequency with \(u,v\ne0\), write \(b,c,d\) for the counts of pairs \((1,0),(0,1),(1,1)\) among frequency coordinates. Formula (1) simplifies to
\[
W_n(u,v)=(-1)^{b+c}\big(1+(-1)^d3^a\big).
\]
This is zero if and only if \(a=0\) and \(d\) is odd. The latter condition forces both \(u\) and \(v\) nonzero, so no additional qualification is required. At an axial nontrivial frequency, for example \(u=0,v\ne0\), the exact multiplier is \((-1)^{|v|}(3^a+1-2^n)\). It cannot vanish for \(n\geq3\), because \(2^n-1\equiv7\pmod8\), whereas \(3^a\equiv1\) or \(3\pmod8\). At \((0,0)\), \(3^n-2^{n+1}+1>0\) for \(n\geq2\). Therefore the zero set is exactly the set of frequency words over \((1,0),(0,1),(1,1)\) with an odd number of \((1,1)\) positions. Its size, by a two-term binomial parity count, is \((3^n-1)/2\).

**Sharp positive gap.** The support has even size for \(n\geq2\), hence every integer Walsh multiplier is even. Choose a frequency with one coordinate \((1,0)\) and all other coordinates \((0,1)\). For every \(n\geq2\) this is nonaxial and has \(a=d=0\), so formula (1) gives a multiplier of magnitude \(2\). Since Walsh diagonalization is unitary after normalizing the character basis, the smallest nonzero singular value is \(2\) and the pseudoinverse norm is \(1/2\). The maximal absolute multiplier equals \(|S_n|\) by the triangle inequality and is attained at the trivial character, yielding the condition number on the orthogonal complement of the kernel. The relative nullity is \((3^n-1)/(2\cdot4^n)\) and has the stated asymptotic.

**Boundary cases.** At \(n=1\), no word contains both required letters. At \(n=2\), the two words \((1,0)(0,1)\) and \((0,1)(1,0)\) constitute the whole support; their two-point Fourier transform has eight zero coefficients among sixteen. This agrees with the exact coefficient formula and yields rank eight and gap two.

## Verification
The included standalone pure-Python checker enumerates orientations from their edge bits, independently enforces vertex outdegree conditions, computes integer Walsh--Hadamard transforms, and compares every coefficient against (1) for lengths \(1\) through \(8\). At lengths \(1\) through \(4\) it separately recomputes each coefficient as a direct signed sum over the enumerated support. It also checks Parseval's identity, graph-orientation counts, nullity and the minimal positive gap. The checker reports `SINK_FREE_BICLIQUE_FOURIER_EXACT_PASS`; finite tests corroborate but do not replace the all-length proof above.

## Relationship to prior work
Cohn, Pemantle, and Propp's work introduces and studies sink-popping and efficient uniform generation of sink-free orientations. Its results concern sampling and the number of pops rather than Walsh character sums. Subsequent work by Anand, Freifeld, Guo, Wang, and Wang develops a local sampler and approximate-counting results with minimum-degree hypotheses; this does not supply the claimed explicit convolution spectrum for the present degree-two right vertices. Fourier analyses of spanning-tree incidence vectors of \(K_{2,n}\) address a different combinatorial support, and Fourier results for acyclic orientations cannot cover this support, since every finite directed acyclic graph has a sink. The exact zero-set and sharp spectral-gap theorem are assessed as distinct under the comparisons performed; priority against every possible previous character-weighted orientation identity is not certified.

## Limitations
The all-length classification is specific to sink-free orientations of \(K_{2,n}\) and to unnormalized binary Walsh convolution. It neither gives the full signed multiplicity of every nonzero multiplier nor establishes corresponding formulae for general \(K_{m,n}\). An unexamined equivalent weighted-orientation formula may exist. Independent mathematical review has not been performed.

## References
1. H. Cohn, R. Pemantle, and J. Propp, *Generating a random sink-free orientation in quadratic time*, arXiv:math/0103189, first posted 2001-03-27; Electronic Journal of Combinatorics 9 (2002), R10, doi:10.37236/1627. https://arxiv.org/abs/math/0103189
2. K. Anand, G. Freifeld, H. Guo, C. Wang, and J. Wang, *Sink-free orientations: a local sampler with applications*, arXiv:2502.05877 (2025). https://arxiv.org/abs/2502.05877
