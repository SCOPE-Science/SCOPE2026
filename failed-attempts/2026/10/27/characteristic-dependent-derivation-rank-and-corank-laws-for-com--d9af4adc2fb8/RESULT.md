# Characteristic-dependent derivation rank and corank laws for complete multipartite evolution algebras

## Finding

Let \(G=K_{n_1,\ldots,n_s}\) be the complete multipartite simple graph with \(s\ge2\) and positive part sizes \(n_i\). Let \(E_G\) be its graph evolution algebra over \(\mathbb F_q\): the vertex vectors \(e_v\) form a basis, \(e_ve_w=0\) for \(v\ne w\), and \(e_v^2\) is the sum of the basis vectors adjacent to \(v\). Put \(m_i=n_i-1\) and let \(R_{G,q}(t)=\sum_{D\in\operatorname{Der}(E_G)}t^{\operatorname{rank}_{\mathbb F_q}D}\).

Define \(\Phi_d(q)=\prod_{j=1}^{d}(1-q^{-j})\), \(\Phi_0(q)=1\), and the Gaussian coefficient \({m\brack r}_q\) to count \(r\)-subspaces of \(\mathbb F_q^m\). Set
\[
S_q(m,t)=\sum_{r=0}^m {m\brack r}_q q^{r(r+1)/2}\prod_{j=1}^{\lceil r/2\rceil}(1-q^{-(2j-1)})\,t^r,
\]
\[
A_q(m,t)=\sum_{j=0}^{\lfloor m/2\rfloor}{m\brack 2j}_q q^{j(j-1)}\prod_{h=1}^{j}(q^{2h-1}-1)\,t^{2j}.
\]
All coefficients of these expressions are nonnegative integers. The following exact rank enumerations hold:

**Even characteristic.** For every \(q=2^e\), without restrictions on the part sizes,
\[
\boxed{R_{G,q}(t)=\prod_{i=1}^s S_q(m_i,t).}
\]
**Odd characteristic away from the resonance divisors.** If \(q=p^e\), \(p\ge5\), and \(p\nmid n_i\) for every \(i\), then
\[
\boxed{R_{G,q}(t)=\prod_{i=1}^s A_q(m_i,t).}
\]
In the odd-characteristic case every derivation has even rank. In even characteristic, odd ranks do occur whenever some part has at least two vertices.

These rank laws have explicit limiting corank laws. Fix \(q\), and let \(m_i\to\infty\) for each of a fixed number \(s\) of parts, respecting the stated divisibility restrictions and, in odd characteristic, fixing the parity of each \(m_i\). Let \(D\) be a uniformly chosen derivation. The blockwise defects \(Z_i=m_i-\operatorname{rank}(D\vert_{\operatorname{span}\{e_v:v\in V_i\}})\) are independent for every finite size. Write \(P_q=\prod_{j\ge1}(1-q^{-(2j-1)})\). In even characteristic each \(Z_i\) converges in total variation to
\[
\Pr(Z_i=d)=\frac{P_q q^{-d(d+1)/2}}{\Phi_d(q)},\qquad d=0,1,2,\ldots.
\]
In odd characteristic, if \(m_i\equiv\epsilon_i\pmod 2\), each \(Z_i\) converges in total variation to
\[
\Pr(Z_i=d)=\begin{cases}
\displaystyle\frac{P_q q^{-d(d-1)/2}}{\Phi_d(q)},&d\equiv\epsilon_i\pmod2,\\
0,&\text{otherwise}.
\end{cases}
\]
The overall rank deficit \(\sum_i m_i-\operatorname{rank}D\) converges in total variation to the convolution of these independent laws. Thus the small-characteristic change is not merely an increase in derivation-space dimension: it changes the possible parities and the universal limiting deficiency law.

## Assumptions and scope

Every graph part is nonempty and \(s\ge2\). The even-characteristic statement applies to all prime powers \(q=2^e\); the odd-characteristic statement deliberately excludes \(p=3\) and those \(p\ge5\) dividing a part size. No assertion about these excluded odd-characteristic cases is made. Rank always means the rank of a derivation as a linear endomorphism of the full evolution algebra, rather than rank of its adjoint action or dimension of its derivation space. Empty products have value one, so singleton parts cause no difficulty. The limiting statement uses fixed \(s\), fixed \(q\), and independently growing parts.

## Proof

**1. The derivation equations and block separation.** Write \(u_i=\sum_{v\in V_i}e_v\), and \(w_i=\sum_{j\ne i}u_j\). Every \(e_v\) in part \(i\) has square \(w_i\). If \(D(e_b)=\sum_a d_{ab}e_a\), the Leibniz identities on basis products are
\[
 d_{ba}w_b+d_{ab}w_a=0\quad(a\ne b),\qquad D(w_a)=2d_{aa}w_a.
\]
For two vertices in different parts, \(w_a,w_b\) are linearly independent: for \(s=2\) they have disjoint nonempty supports; for \(s\ge3\), projecting onto their two corresponding parts (and a third part if needed) rules out dependence over every field. Hence cross-part entries vanish and \(D\) is block diagonal. Within any one part, the first equation says that its off-diagonal block entries satisfy \(d_{ab}=-d_{ba}\).

**2. Characteristic two.** The second Leibniz equation reads \(D(w_i)=0\). Since \(D\) is block diagonal and every part appears in some \(w_i\), it is equivalent to \(D(u_j)=0\) for every \(j\). The unrestricted diagonal together with skew-symmetric off-diagonal entries in characteristic two says precisely that each block \(B_j\) is symmetric and \(B_j\mathbf1=0\). Conversely, any such blocks satisfy every Leibniz equation. A simultaneous change of coordinates for bilinear forms with first basis vector \(\mathbf1\) identifies this vector space of blocks, preserving rank and counting, with all symmetric \(m_j\times m_j\) matrices and one zero row and column.

**3. Odd characteristic under the stated hypotheses.** Inside part \(i\), the second equation makes all diagonal entries equal, say \(\alpha_i\), because \(w_i\ne0\) and \(2\ne0\). Thus \(B_i=\alpha_i I+H_i\) with \(H_i^T=-H_i\). If \(s=2\), the equations \(D(u_2)=2\alpha_1u_2\), \(D(u_1)=2\alpha_2u_1\) imply \(H_1\mathbf1=(2\alpha_2-\alpha_1)\mathbf1\) and \(H_2\mathbf1=(2\alpha_1-\alpha_2)\mathbf1\). Since \(\mathbf1^TH_i\mathbf1=0\) and \(p\nmid n_i\), it follows that \(\alpha_1=2\alpha_2\), \(\alpha_2=2\alpha_1\), and so \(3\alpha_1=3\alpha_2=0\). As \(p\ge5\), both vanish. If \(s\ge3\), the equations for distinct neighboring parts force all \(\alpha_i\) to a common \(\alpha\). Then \(H_j\mathbf1=\alpha\mathbf1\) for each \(j\), and \(p\nmid n_j\) forces \(\alpha=0\). Thus in all permitted odd cases the blocks are exactly skew-symmetric matrices \(H_j\) with \(H_j\mathbf1=0\). Congruence with a basis starting with \(\mathbf1\) identifies their ranks and multiplicities with arbitrary alternating \(m_j\times m_j\) matrices. Conversely, all those matrices give derivations.

**4. Finite-field form enumeration.** A bilinear form of rank \(r\) has a uniquely determined radical of dimension \(m-r\); choosing it yields \({m\brack r}_q\) possibilities, and the induced quotient form is nondegenerate. For alternating matrices only \(r=2j\) occurs; symplectic-basis counting gives \(q^{j(j-1)}\prod_{h=1}^{j}(q^{2h-1}-1)\) nondegenerate alternating matrices of size \(2j\). For symmetric matrices put \(N_r\) equal to the count of invertible symmetric matrices of size \(r\). The elementary bordered-matrix argument gives
\[
N_0=1,\quad N_1=q-1,\quad N_{r+1}=q^r(q-1)\left(N_r+{r\brack1}_qN_{r-1}\right).
\]
Indeed, an invertible upper-left block allows \(q^r(q-1)\) choices of last column and corner; a corank-one upper-left block gives the same factor after requiring the last column not annihilate its radical; a larger radical cannot be repaired by one border. Induction yields \(N_r=q^{r(r+1)/2}\prod_{j=1}^{\lceil r/2\rceil}(1-q^{-(2j-1)})\). The independent block identifications in steps 2 and 3 now prove both product formulas.

**5. Corank limits.** Let \(m\) be the dimension of a single unrestricted form, and \(d=m-r\) its corank. The Gaussian coefficient identity
\[
{m\brack d}_q=q^{d(m-d)}\frac{\prod_{k=m-d+1}^{m}(1-q^{-k})}{\Phi_d(q)}
\]
shows that the symmetric corank probability equals
\[
\frac{q^{-d(d+1)/2}}{\Phi_d(q)}\prod_{k=m-d+1}^{m}(1-q^{-k})\prod_{j=1}^{\lceil(m-d)/2\rceil}(1-q^{-(2j-1)}).
\]
For alternating matrices the corresponding expression has \(q^{-d(d-1)/2}\), the alternating product ending at \((m-d)/2\), and vanishes unless \(d\equiv m\pmod2\). At fixed \(d\), each finite prefactor converges to the displayed limit. Uniformly in \(m\), the masses are dominated respectively by \(\Phi_\infty(q)^{-1}q^{-d(d+1)/2}\) and \(\Phi_\infty(q)^{-1}q^{-d(d-1)/2}\), summable over \(d\ge0\). Dominated convergence therefore proves total-variation convergence and normalization, without relying on numerical truncation. Independence is exact for finite sizes because the block parameterizations are direct products. Finite products of convergent discrete probability measures converge in total variation, giving the joint and total-defect statements.

## Verification

The included `verify.py` constructs the multiplication table of the complete multipartite evolution algebra, independently derives all linear constraints by applying the Leibniz equation to every ordered natural-basis pair, computes their kernel over prime fields, enumerates every derivation in each tested small configuration, and counts its matrix rank. It separately implements the two proposed form-rank formulas and compares coefficients. Test cases cover bipartite and tripartite graphs, both characteristic two and permissible odd characteristics, and include zero-dimensional derivation spaces. Running `python verify.py` ends with `VERIFY_OK` upon success. The finite checks are corroboration; the all-size and prime-power assertions follow from the proof above.

## Relationship to prior work

Reis and Cadavid (2020, arXiv:2006.11934), especially their full derivation criterion and twin-block theorem, already characterize the linear space of graph-evolution-algebra derivations over arbitrary characteristic. Cadavid, Rodiño Montoya and Rodriguez (2018, arXiv:1807.02493) previously treated characteristic zero, including twin-block structure. Those structural theorems are foundational and are not claimed here. Standard classical rank counts for symmetric and alternating finite-field forms are also prior work. The result presented here is the explicitly rank-refined census on complete multipartite graph algebras and its characteristic-sensitive total-variation corank limits, which were not identified in the inspected source statements. This is not a general classification of derivations for arbitrary graphs.

## Limitations

Odd characteristic three, and odd characteristic dividing a part size, can admit coupled scalar-diagonal parameters; the clean alternating-block factorization is not asserted there. The theorem does not claim novelty for the underlying derivation decomposition or individual symmetric/alternating form counts. Complete publication priority was not established; an equivalent rank specialization under other terminology remains possible. In particular, the full general derivation parametrization in the principal prior paper makes this a specialized rank-statistics theorem rather than a new classification of all derivations. No independent mathematical audit has been performed.

## References

1. T. Reis and P. Cadavid, *Derivations of Evolution Algebras associated to graphs over a field of any characteristic*, arXiv:2006.11934, first posted 2020-06-21. https://arxiv.org/abs/2006.11934
2. P. Cadavid, M. L. Rodiño Montoya and P. M. Rodriguez, *Characterization theorems for the spaces of derivations of evolution algebras associated to graphs*, arXiv:1807.02493, first posted 2018-07-06. https://arxiv.org/abs/1807.02493
3. A. Pott, K.-U. Schmidt and Y. Zhou, *Pairs of Quadratic Forms over Finite Fields*, Electronic Journal of Combinatorics 23(2), P2.8 (2016), published 2016-04-15. https://doi.org/10.37236/4072
4. R. Gow, *Rank-related dimension bounds for subspaces of bilinear forms over finite fields*, arXiv:1703.07266, first posted 2017-03-21. https://arxiv.org/abs/1703.07266
