# Sharp one-site Fourier frame bounds on cross-polytope graph colourings

## Finding

Let \(m\ge 3\), \(q\ge m\), and let \(G_m=K_{2,2,\ldots,2}\) be the complete \(m\)-partite graph with two vertices in each part (equivalently, the graph of the \(m\)-dimensional cross-polytope). Give the finite set \(\Omega_{m,q}\) of proper vertex colourings by \(\mathbb Z/q\mathbb Z\) its uniform probability measure. In \(L^2(\Omega_{m,q})\), consider the constant \(1\) and every one-site nontrivial additive character
\[
\chi_{v,a}(c)=\exp(2\pi i a c(v)/q),\qquad v\in V(G_m),\quad 1\le a<q.
\]
Their probability-normalized Gram matrix has exactly the following multiset of eigenvalues (with coincident levels combined):
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\ \hline
1&1\\
L_{\rm anti}=\dfrac{q(1-p)}{q-1}&m(q-1)\\
L_{\rm pair}=\dfrac{q(1+p)}{q-1}&(m-1)(q-1)\\
L_{\rm total}=\dfrac{q(1+p)-2m}{q-1}&q-1
\end{array}
\]
where the explicitly computable rational number \(p=p_{m,q}\) is
\[
Z_{m,q}=\sum_{s=0}^{m}\binom ms(q)_{2m-s},\qquad
p_{m,q}=\frac{qZ_{m-1,q-1}}{Z_{m,q}},\qquad
(q)_r=\begin{cases}q!/(q-r)!,&0\le r\le q,\\0,&r>q.\end{cases}
\]
At the chromatic palette \(q=m\), the Gram rank is \(1+(m-1)^2\), and the nullity is \(m^2-1\). The frame becomes linearly independent **exactly at** \(q\ge m+1\). At the first admissible extra colour, \(q=m+1\),
\[
p_{m,m+1}=\frac{m}{m+1},\qquad
L_{\rm anti}=L_{\rm total}=\frac1m,\qquad
L_{\rm pair}=\frac{2m+1}{m},
\]
so its **sharp squared singular-value condition number** is exactly \(2m+1\). For every \(q>m\), the sharp squared condition number is
\[
\kappa_{m,q}^{2}=\frac{L_{\rm pair}}{\min\{L_{\rm anti},L_{\rm total}\}}.
\]
For each fixed \(m\ge3\), as the palette increases without bound,
\[
\kappa_{m,q}^{2}=1+\frac{2m}{q}+O_m(q^{-2}).
\]
These are statements for every integer in the stated parameter ranges, not finite-range extrapolations.

## Assumptions and scope

A proper colouring is a function \(c:V(G_m)\to\mathbb Z/q\mathbb Z\) assigning distinct colours to adjacent vertices. Colours may be reused only by the two vertices in the same part. Both vertices are labelled, and the \(m\) parts are labelled; no division by graph automorphisms or colour permutations is made. The inner product is the uniform probability expectation \(\langle f,g\rangle=\mathbb E[f\overline g]\). Each listed character has squared norm one. The Gram is on the \(1+2m(q-1)\) displayed functions, not on all Fourier characters of the ambient product group. Here a frame being linearly independent is equivalent to positivity of this finite Gram; no claim is made that these characters span the entire space of functions on the colouring set.

## Proof

**1. Colouring count and the within-part coincidence probability.** A proper colouring uses one colour in each monochromatic part and two different colours in each nonmonochromatic part; colours used by different parts are disjoint. If precisely \(s\) parts are monochromatic, there are \(\binom ms\) choices of those parts, then \((q)_{2m-s}\) injections assigning distinct colours to the remaining ordered colour positions. This proves the stated formula for \(Z_{m,q}=|\Omega_{m,q}|\), with \(Z_{0,q}=1\). Fix either part. Making it monochromatic leaves one chosen colour and a proper colouring of the remaining \(m-1\) parts with a reduced \((q-1)\)-colour palette. Therefore
\[
\mathbb P\{c(u)=c(v)\}=p_{m,q}=qZ_{m-1,q-1}/Z_{m,q}
\]
for the two vertices in a common part. For vertices in different parts that probability is zero. By complete permutation symmetry of the \(q\) colour names, each one-site marginal is uniform.

**2. Fourier colour blocks.** Write \(\omega=\exp(2\pi i/q)\). For any two sites \(u,v\), their joint law is invariant under all permutations of colour names. If \(t=\mathbb P\{c(u)=c(v)\}\), every equal ordered colour pair has probability \(t/q\), and every unequal ordered colour pair has probability \((1-t)/(q(q-1))\). Directly summing roots of unity gives, for \(1\le a,b<q\),
\[
\mathbb E[\omega^{a c(u)-b c(v)}]
=\mathbf 1_{\{a=b\}}\frac{qt-1}{q-1}
\]
when \(u\ne v\); at \(u=v\) the same expression is \(\mathbf1_{\{a=b\}}\). Each nontrivial character has zero mean and is therefore orthogonal to the constant. Consequently the Gram consists of the constant block \([1]\) and \(q-1\) identical real symmetric spatial blocks \(H\) indexed by the \(2m\) vertices. The diagonal of \(H\) is one; opposite vertices within the same part have entry \(r=(qp-1)/(q-1)\); vertices in different parts have entry \(b=-1/(q-1)\).

**3. All eigenspaces and multiplicities.** The spatial coordinate space splits orthogonally into (i) the \(m\)-dimensional space of within-part antisymmetric vectors, (ii) the \((m-1)\)-dimensional space of vectors constant on each pair whose pair means sum to zero, and (iii) the span of the all-ones vector. The matrix \(H\) acts there, respectively, by \(1-r\), \(1+r-2b\), and \(1+r+2(m-1)b\). Substituting \(r,b\) yields precisely the three displayed levels and all multiplicities. The spectrum is complete because the spatial dimensions add to \(2m\), and the nonconstant blocks are orthogonal for different colour frequencies.

**4. Sharp rank boundary.** When \(q=m\), every proper colouring must use exactly one colour per part, so \(p=1\). Thus \(L_{\rm anti}=L_{\rm total}=0\) and \(L_{\rm pair}=2m/(m-1)>0\); the claimed rank and nullity follow. If \(q>m\), there exists a colouring with one part using two distinct colours, so \(p<1\) and \(L_{\rm anti}>0\). The pair level is strictly positive. For the remaining level, let \(S\) be the number of parts using two distinct colours. Every proper colouring uses exactly \(m+S\) colours, hence \(S\le q-m\), and by exchangeability \(p=1-\mathbb ES/m\). If \(m<q<2m\), this implies \(p\ge(2m-q)/m>(2m-q)/q\), so \(q(1+p)>2m\); if \(q\ge2m\), the latter strict inequality follows from \(p>0\). Therefore \(L_{\rm total}>0\) for every \(q>m\), proving the exact independence threshold.

**5. Sharp frame bounds.** As \(p>0\), \(L_{\rm pair}-L_{\rm anti}=2qp/(q-1)>0\). Also \(L_{\rm pair}-L_{\rm total}=2m/(q-1)>0\) and \(L_{\rm pair}-1=(1+qp)/(q-1)>0\). Thus \(L_{\rm pair}\) is the largest Gram eigenvalue. For \(q>m\), condition on a colouring of the other \(m-1\) parts. If it uses \(K\ge m-1>0\) distinct colours, the remaining two vertices may independently choose any of the \(q-K\) unused colours, giving conditional coincidence probability \(1/(q-K)>1/q\). Averaging shows \(qp>1\), whence \(L_{\rm anti}<1\). The smallest eigenvalue is therefore \(\min\{L_{\rm anti},L_{\rm total}\}\), and the stated sharp condition ratio follows. This comparison also handles any collisions of eigenvalues without asserting distinctness where none was proved.

**6. The first extra colour.** At \(q=m+1\), only all-monochromatic colourings and colourings with exactly one bichromatic part are possible. Counting gives \(Z_{m,m+1}=(m+1)(m+1)!\) and \(Z_{m-1,m}=m\,m!\). Hence \(p=m/(m+1)\). Inserting this into the three exact levels gives \(L_{\rm anti}=L_{\rm total}=1/m\) and \(L_{\rm pair}=(2m+1)/m\), which proves the exact sharp ratio \(2m+1\).

**7. Large-palette limit.** For fixed \(m\), the number of colours used by the other \(m-1\) parts is between \(m-1\) and \(2(m-1)\). Conditioning as above and taking \(q\ge2m\),
\[
\frac1{q-m+1}\le p\le\frac1{q-2m+2}.
\]
Consequently \(p=1/q+O_m(q^{-2})\), so \(L_{\rm anti}=1+O_m(q^{-2})\), \(L_{\rm pair}=1+2/q+O_m(q^{-2})\), and \(L_{\rm total}=1-2(m-1)/q+O_m(q^{-2})\). For sufficiently large \(q\), the last of these is the smallest; their ratio proves the stated expansion.

## Verification

The accompanying standalone script `verify_colouring_frame.py` uses only the Python standard library. Running `python3 verify_colouring_frame.py` verifies the exact falling-factorial colouring count and recursive count identity, performs exact rational Gram-block eigenvector checks for 242 parameter pairs with \(3\le m\le17\), exhaustively enumerates all proper colourings in eight smaller examples (up to 7560 colourings in one example), independently checks their character correlations and 3756 full-complex-Fourier Gram entries, and tests finite-palette consistency with the proved asymptotic. Its printed PASS report is corroboration; the all-parameter proof is in the seven steps above.

## Relationship to prior work

Shrock and Xu, *Weighted-Set Graph Colorings* (first public preprint 2009-11-22, arXiv:0911.4218v1), develop weighted chromatic partition functions and calculate illustrative graph families. They supply relevant uniform proper-colouring context but do not state the three-eigenvalue Fourier-character Gram law or the first-extra-colour condition ratio. Cahill, Fickus, Mixon, Poteet, and Strawn, *Constructing finite frames of a given spectrum and set of lengths* (arXiv:1106.0921v1), explain why sharp frame-operator extremal eigenvalues are the quantitative stability invariants; they give general construction machinery, not this proper-colouring restriction spectrum. Crew and Spirkl, *A complete multipartite basis for the chromatic symmetric function* (arXiv:2009.14141), study colouring enumerators for the same broad graph class; their chromatic symmetric-function basis results are not an explicit pair-resolved Fourier Gram diagonalization. A previously known two-part proper-colouring calculation concerns \(K_{2,2}\), the \(m=2\) member excluded here, and does not directly give the \(m\ge3\) theorem. This is a bounded originality comparison, not a claim of exhaustive historical priority.

## Limitations

The claim is about one-site additive characters and uniform proper-colouring sampling, not higher Fourier bands, weighted Potts measures, or arbitrary complete multipartite part sizes. The sharp condition formula for general \(q>m\) uses a minimum of two explicit rational expressions; no global branch-ordering claim is made. No independent mathematical validation has been performed. Searches and inspected literature cannot exclude an equivalent older derivation of this exact finite family; the remaining historical risk is documented separately.

## References

1. R. Shrock and Y. Xu, *Weighted-Set Graph Colorings*, arXiv:0911.4218v1, publicly posted 2009-11-22, https://arxiv.org/abs/0911.4218.
2. J. Cahill, M. Fickus, D. G. Mixon, M. J. Poteet, and N. K. Strawn, *Constructing finite frames of a given spectrum and set of lengths*, arXiv:1106.0921v1, publicly posted 2011-06-05, https://arxiv.org/abs/1106.0921.
3. L. Crew and S. Spirkl, *A complete multipartite basis for the chromatic symmetric function*, arXiv:2009.14141, first public 2020-09-29, https://arxiv.org/abs/2009.14141.
