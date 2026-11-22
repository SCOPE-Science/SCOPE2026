# Three common quaternionic lines force a projective continuum: a sharp \(4r+9\)-dimensional locus

## Finding

For every integer \(r\ge2\), put \(\mathcal L_{r,\ge3}\subset M_2(\mathbb H)^r\) for the set of tuples preserving at least three distinct common right quaternionic lines. Then
\[
\mathcal L_{r,\ge3}=
\bigl\{(P\operatorname{diag}(a_i,a_i)P^{-1})_{i=1}^r:
P\in\operatorname{GL}_2(\mathbb H),\ a_i\in\mathbb H\bigr\},
\qquad \dim_\mathbb R\mathcal L_{r,\ge3}=4r+9.
\]
Every tuple in this locus actually fixes infinitely many common right quaternionic lines. There is no finite common-line count greater than two. The full invariant-line space is a conjugate of exactly one of \(\mathbb RP^1\), \(\mathbb CP^1\), or \(\mathbb HP^1\), with real dimensions \(1,2,4\).

## Assumptions and scope

Here \(\mathbb H\) is the real Hamilton quaternion division algebra, \(M_2(\mathbb H)\) acts on columns in the right module \(\mathbb H^2\), and a *right line* means a one-dimensional right \(\mathbb H\)-submodule. An invariant line \(W\) obeys \(A_iW\subseteq W\) for every \(1\le i\le r\). Distinct lines mean distinct submodules, not merely distinct nonzero spanning vectors. Real dimension always means semialgebraic dimension. The claim concerns tuples for \(r\ge2\), not higher matrix orders or arbitrary division rings.

## Proof

**1. Three lines imply a repeated diagonal representation.** Distinct right lines \(W_1,W_2\subset\mathbb H^2\) meet in zero and give a direct sum, so a matrix \(P\in\operatorname{GL}_2(\mathbb H)\) with columns spanning them simultaneously conjugates every \(A_i\) into a diagonal matrix \(\operatorname{diag}(a_i,b_i)\). Every third line distinct from both coordinate axes has a unique generator \((1,t)^\mathsf T\) with \(t\in\mathbb H^\times\). Its invariance gives \(b_it=ta_i\) for all \(i\). Consequently the common invertible change \(\operatorname{diag}(1,t)\) turns every \(\operatorname{diag}(a_i,b_i)\) into \(\operatorname{diag}(a_i,a_i)\). Conversely each repeated-diagonal tuple preserves both axes and all graphs \((1,s)^\mathsf T\mathbb H\) with \(s\in\mathbb R\), establishing the equivalence and the infinite-line assertion.

**2. Classify every common line.** For \(\operatorname{diag}(a_i,a_i)\), the line \((1,t)^\mathsf T\mathbb H\) is invariant if and only if \(a_it=ta_i\) for all \(i\), while the second axis is always invariant. Therefore its complete fixed-line set is \(\mathbb P^1(C)\) for \(C=C_\mathbb H(a_1,\ldots,a_r)\). The centralizer of one nonreal quaternion consists of the real span of \(1\) and its imaginary direction, isomorphic to \(\mathbb C\); two nonparallel nonzero imaginary directions have only real common centralizers. If all \(a_i\) are real, then \(C=\mathbb H\). Thus \(C\) is exactly \(\mathbb R\), a conjugate copy of \(\mathbb C\), or \(\mathbb H\). This yields precisely the three listed projective-line types and dimensions. It also gives examples: \(a_1=\mathbf i,a_2=\mathbf j\) gives \(\mathbb RP^1\), \(a_1=\mathbf i,a_2=1\) gives \(\mathbb CP^1\), and all real \(a_i\) give \(\mathbb HP^1\), with arbitrary additional coordinates when \(r>2\). In contrast, \(\operatorname{diag}(0,1)\) has exactly its two coordinate-axis invariant lines, because a third graph would require \(t=0\).

**3. Exact real dimension.** Let \(G=\operatorname{GL}_2(\mathbb H)\), a real semialgebraic group of dimension \(16\), and let \(D(\mathbb H)=\{\operatorname{diag}(a,a):a\in\mathbb H\}\). Consider the semialgebraic map
\[
F:G\times\mathbb H^r\longrightarrow M_2(\mathbb H)^r,\qquad
F(P,(a_i))=(P\operatorname{diag}(a_i,a_i)P^{-1})_i.
\]
Its image is \(\mathcal L_{r,\ge3}\). The normalizer \(N_G(D(\mathbb H))\) has real dimension \(7\): any induced \(\mathbb R\)-algebra automorphism of \(\mathbb H\) is inner, so the normalizer is \(\{(uI_2)R:u\in\mathbb H^\times,\ R\in\operatorname{GL}_2(\mathbb R)\}\). The centralizer \(C_G(D(\mathbb H))=\operatorname{GL}_2(\mathbb R)\) has real dimension \(4\), the inner automorphism group \(\operatorname{Aut}_\mathbb R(\mathbb H)\cong\operatorname{SO}_3(\mathbb R)\) has dimension \(3\), so \(\dim N_G=7\). For every input, the \(N_G\)-action produces a seven-dimensional family of inputs with the same image, hence by semialgebraic fiber dimension \(\dim\operatorname{im}F\le16+4r-7\).

On the nonempty open subset where \(a_1,a_2\) do not commute, the two quaternions generate \(\mathbb H\) as a unital \(\mathbb R\)-algebra. Indeed, their nonparallel imaginary parts together with their cross product span the imaginary three-space. If \(F(P,\mathbf a)=F(Q,\mathbf b)\) for such an input, the two tuples generate exactly the same conjugate of \(D(\mathbb H)\), implying \(P^{-1}Q\in N_G(D(\mathbb H))\). Every fiber of the restriction to this open subset has dimension exactly \(7\). The image of the open subset consequently has dimension \(16+4r-7\); combining bounds proves \(\dim_\mathbb R\mathcal L_{r,\ge3}=4r+9\).

Theorem 4.11 of the cited quaternionic matrix-tuple paper gives \(\dim\mathcal L_{r,\ge2}=8r+8\) on substitution \(n=2,k=1\). Subtraction yields the codimension \(4r-1\) within that larger locus, including \(17\) versus \(24\) dimensions for \(r=2\).

## Verification

The supplied `CHECK.py` independently expands quaternion multiplication in exact integer coordinates and checks the scalar centralizer dimensions \(4,2,1\), the corresponding repeated-diagonal matrix centralizer dimensions \(16,8,4\), and the two-line contrast. It exits with `QUATERNION_THREE_LINE_CHECKS_OK`. These finite linear-algebra calculations are supporting consistency tests; they are not a substitute for the normalizer and semialgebraic dimension proof above.

## Relationship to prior work

Yao, Hou and Zhang (public preprint dated November 14, 2026), Theorem 4.11, determine the exact dimension of the locus of matrix tuples with *at least two* common invariant right quaternionic subspaces. Their discussion immediately after the theorem expressly leaves open whether that condition implies infinitely many common subspaces. The new threshold at *three* lines for \(n=2\), the exact \(4r+9\) dimension, and the complete projective-line alternatives are not consequences of the published two-line dimension formula alone. Their Remark 4.12 gives a complex comparison, rather than this quaternionic three-line classification. The proof uses the classical classification of quaternion automorphisms only in its normalizer step.

## Limitations

No statement about \(n\ge3\), higher-dimensional invariant subspaces, or general division rings is established. Prior-art searches cannot certify historical uniqueness: an earlier special-case discussion may exist under different terminology. The result has a complete self-contained proof but has not received independent mathematical validation. The checker verifies selected exact algebraic identities only.

## References

- C. Yao, B. Hou and Y. Zhang, *Quaternion Matrix Tuples with Common Invariant Subspaces: Dimension and Nonuniqueness*, arXiv:2611.19492v1, November 14, 2026. Theorem 4.11 and the paragraphs following it, and Remark 4.12. https://arxiv.org/html/2611.19492v1
- F. Zhang, *Quaternions and matrices of quaternions*, Linear Algebra and its Applications **251** (1997), 21–57, cited as quaternion-matrix background in the preceding source.
- Mathematical Reviews and zbMATH, *MSC2020*, class 15B33 (matrices over special rings, including quaternions), https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=15B.
