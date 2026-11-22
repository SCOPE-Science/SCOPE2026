# The unique exceptional trace-form class in the eleventh cyclotomic field

## Finding
Let \(K=\mathbb Q(\zeta)\), where \(\zeta\) is a primitive eleventh root of unity, \(K^+=\mathbb Q(\zeta+\zeta^{-1})\), \(\mathcal O=\mathbb Z[\zeta]\), and \(\pi=1-\zeta\). For any totally positive \(a\in K^+\), define
\[
q_a(x)=\operatorname{Tr}_{K/\mathbb Q}(ax\overline{x}),\qquad
\mu(a)=\min_{x\in\mathcal O\setminus\{0\}}q_a(x).
\]
Then **there is a nonunit element \(x\in\mathcal O\) with \(q_a(x)=\mu(a)\) if and only if**
\[
\boxed{a=\frac{c}{(\pi\overline\pi)(\varepsilon\overline\varepsilon)}
\quad\text{for some }c\in\mathbb Q_{>0},\quad
\varepsilon\in\mathcal O^\times.}
\]
For such a weight, \(\mu(a)=10c\), both \(\varepsilon\) and \(\pi\varepsilon\) are minimal, and every nonunit minimal element has absolute field norm \(11\). Thus there is exactly **one rational-homothety and unit-norm equivalence class** of positive trace-form weights admitting a nonunit minimum. At every other totally positive weight, every shortest nonzero element is a unit.

## Assumptions and scope
The field, weight, and minimum are precisely as defined above. A unit is an element of \(\mathcal O^\times\). We classify **all** totally positive algebraic weights \(a\in K^+\), not merely rational weights or a finite coefficient sample. Weight equivalence means multiplication by a positive rational number and by \((\varepsilon\overline\varepsilon)^{-1}\) for a unit. The result addresses shortest elements of unary trace forms, not arbitrary positive definite quadratic forms in ten variables.

The proof uses two published facts concerning \(K\) from Chang [1]: (i) every nonunit minimum is \(\pi\varepsilon\) for some unit, and then all five elements \(\varepsilon v_k\), with \(v_k=\pi/(1-\zeta^k)\), are also minimal; (ii) for the reference weight \(a_0=(\pi\overline\pi)^{-1}\), the minimum equals \(10\) and is attained by \(1\) and \(\pi\). These statements are independently identified below by theorem and section. The new step is to prove that the five equality conditions **force the entire weight**, not just its minimum value.

## Proof
**1. Equality constraints.** Write \(A_j=(1-\zeta^j)(1-\zeta^{-j})\) and \(h_j=A_j^{-1}\), for \(1\le j\le5\). Let \(\sigma_j:K^+\hookrightarrow\mathbb R\) send \(\zeta+\zeta^{-1}\) to \(\zeta^j+\zeta^{-j}\), and set \(b_j=\sigma_j(a\varepsilon\overline\varepsilon)\sigma_j(A_1)>0\). Since
\[
\sigma_j(v_k\overline{v_k})=\frac{\sigma_j(A_1)}{\sigma_j(A_k)}=\frac{\sigma_j(A_1)}{A_{jk}},
\]
where subscripts on \(A\) are read modulo \(11\) and identify \(t\) with \(-t\), we have
\[
\frac12q_a(\varepsilon v_k)=\sum_{j=1}^{5}\frac{b_j}{A_{jk}},
\qquad
\frac12q_a(\pi\varepsilon)=\sum_{j=1}^{5}b_j.
\]
If \(\pi\varepsilon\) is a minimum, Chang's Proposition 5.2 [1] implies \(q_a(\varepsilon v_k)=q_a(\pi\varepsilon)\) for all \(k=1,\ldots,5\). Thus, with the real \(5\times5\) matrix \(M_{kj}=A_{jk}^{-1}\),
\[
Mb=\Big(\sum_jb_j\Big)\mathbf1.
\]

**2. Exact nonsingularity.** The sum identity in [1, Lemma 5.1] gives \(\sum_{j=1}^5A_{jk}^{-1}=5\) for each \(k\), so \(M\mathbf1=5\mathbf1\). We now show \(M\) invertible. Since \(M_{kj}=\sigma_j(h_k)\), its row Gram matrix has rational entries
\[
G_{k\ell}=\sum_{j=1}^5\sigma_j(h_kh_\ell)
=\operatorname{Tr}_{K^+/\mathbb Q}(h_kh_\ell)
=\begin{pmatrix}
11&4&3&3&4\\
4&11&3&4&3\\
3&3&11&4&4\\
3&4&4&11&3\\
4&3&4&3&11
\end{pmatrix}.
\]
A direct exact determinant evaluation gives \(\det G=75625=275^2>0\). For reproducibility, each entry can be computed in \(\mathbb Q[Z]/\Phi_{11}(Z)\): take
\[
h_k=(2-Z^k-Z^{11-k})^{-1},\quad
\operatorname{Tr}_{K/\mathbb Q}(\sum_{r=0}^9c_r\zeta^r)=10c_0-\sum_{r=1}^9c_r,
\]
and divide the resulting trace of \(h_kh_\ell\) by two. The supplied standalone `check.py` performs all inversions, traces, and the determinant using **exact rational arithmetic without external dependencies**. As \(G=MM^{\mathsf T}\), the nonzero determinant proves \(M\) invertible. There is also a structural explanation: the five \(h_k\) are the Galois orbit of \(h_1\) in the cyclic quintic extension \(K^+/\mathbb Q\). Their trace is \(5\ne0\) and \(h_1\notin\mathbb Q\). The regular rational representation of a cyclic group of prime order five splits as the trivial representation and one irreducible four-dimensional representation; consequently the orbit spans both components and forms a rational normal basis. Its conjugate evaluation matrix is therefore nonsingular.

Therefore the equality system has a unique solution. Since \(M\mathbf1=5\mathbf1\), its solution is \(b_j=c\) for all \(j\), with \(c=(\sum_jb_j)/5>0\). Equivalently,
\[
\sigma_j(a\varepsilon\overline\varepsilon\pi\overline\pi)=c
\quad (1\le j\le5).
\]
An element of \(K^+\) whose five conjugates all equal the same real number must belong to \(\mathbb Q\), so \(c\in\mathbb Q_{>0}\). This yields the claimed necessary form of \(a\).

**3. Sufficiency.** Conversely, let \(a=c/(\pi\overline\pi\varepsilon\overline\varepsilon)\), with \(c\in\mathbb Q_{>0}\) and \(\varepsilon\) a unit. For every \(x\in\mathcal O\),
\[
q_a(x)=c\,\operatorname{Tr}_{K/\mathbb Q}\!\left((x/(\pi\varepsilon))\overline{(x/(\pi\varepsilon))}\right)
=cq_{a_0}(x/\varepsilon).
\]
Multiplication by \(\varepsilon^{-1}\) permutes the nonzero elements of \(\mathcal O\). Chang's Lemma 5.5 and Proposition 3.4 [1] give \(\mu(a_0)=10\), attained by both \(1\) and \(\pi\). Consequently \(\mu(a)=10c\), attained by both \(\varepsilon\) and \(\pi\varepsilon\). Since \(\pi\) has norm \(11\), the second is a nonunit. Finally, Chang's Corollary 4.9 [1] establishes that any nonunit minimum must be of this norm. This completes the equivalence.

## Verification
Run `python3 check.py`. Its five exact identities establish the inverse expressions for \(h_k\) in the cyclotomic quotient ring. It then checks the five traces, all \(25\) Gram entries, and \(\det G=75625\). The code uses Python's standard `fractions.Fraction` and no floating-point calculations. The proof of the global minimum at the reference weight, including the infinite lattice bound, is supplied by the cited source [1], not inferred from the finite matrix computation.

## Relationship to prior work
Chang [1, Sections 4.4 and 5.1–5.3] establishes weak unit reducibility, identifies the allowable **types of minimal element**, proves the five-unit averaging equality, and gives a specific reference weight with a nonunit minimum. The present result classifies **all weights** supporting such a nonunit minimum and proves uniqueness of their equivalence class. Porter, Ling, Sarti, and Leibak [2] develop the unit-reducibility framework and use the same reference-weight construction for other conductors; their stated theorems do not give the complete weight locus for conductor \(11\). Sigrist [3] enumerates five \(C_{11}\)-perfect cyclotomic forms, a broad related classification; the article does not explicitly identify the full nonunit-minimum locus in the positive weight cone. Its historical computational tables are an originality risk rather than independent evidence of novelty.

## Limitations
The uniqueness concerns the **exceptional weight orbit**, not all shortest-vector configurations or all perfect forms. It relies on the validity of Chang's global norm restriction and reference minimum; the supplied exact arithmetic independently checks only the new nonsingularity lemma. The result does not assert a novel classification of the five perfect forms or any analogous statement for conductors other than eleven. An equivalent statement could be implicit in historical full cyclotomic-form tables or unpublished analyses.

## References
[1] Y. Chang, *Weak Unit Reducibility of the Eleventh Cyclotomic Field*, arXiv:2611.15432v1, first publicly submitted 2026-11-11, Sections 4.4 and 5.1–5.3. https://arxiv.org/html/2611.15432v1

[2] C. Porter, C. Ling, P. Sarti, and A. Leibak, *Unit Reducible Fields and Perfect Unary Forms II. Cyclotomic Fields*, Journal de Théorie des Nombres de Bordeaux 37 (2025), 443–456, DOI:10.5802/jtnb.1327. https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1327.pdf

[3] F. Sigrist, *Cyclotomic quadratic forms*, Journal de Théorie des Nombres de Bordeaux 12 (2000), 519–530, DOI:10.5802/jtnb.295. https://www.numdam.org/article/JTNB_2000__12_2_519_0.pdf
