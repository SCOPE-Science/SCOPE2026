# The complete Kirillov-rank spectrum of characteristic-two star graph Lie algebras

## Finding
For each integer \(m\ge2\) and finite field \(K=\mathbb F_q\) of characteristic two, let \(L_m\) be the class-three graph Lie algebra for the star \(K_{1,m}\), defined in detail below. For each functional \(\lambda\in L_m^*\), its **Kirillov alternating form** is \(\mathcal K_\lambda(x,y)=\lambda([x,y])\). The entire distribution of its rank is encoded by
\[
\boxed{\displaystyle
P_{m,q}(t)=\sum_{\lambda\in L_m^*}t^{\operatorname{rank}\mathcal K_\lambda}
=q^{m+1}\sum_{k=0}^{\lfloor m/2\rfloor}H_{m,k}(q)
\left(q^{2k}t^{4k}+(q^m-q^{2k})t^{4k+2}\right),}
\]
where
\[
H_{m,k}(q)={m\brack 2k}_q\,q^{k(k-1)}\prod_{j=1}^k(q^{2j-1}-1),
\]
\({m\brack r}_q=\prod_{i=0}^{r-1}(q^{m-i}-1)/(q^{r-i}-1)\) is the Gaussian coefficient and an empty product is one. Terms with zero coefficients may be omitted. Thus the complete multiplicity of *every* Kirillov rank is determined explicitly, not merely its generic maximum.

In particular the index, defined as the minimum radical dimension of these forms, is
\[
\boxed{\operatorname{ind}(L_m)=1+\binom m2.}
\]
For instance, at \(m=3,q=2\), the exact spectrum is
\[
P_{3,2}(t)=16+112t^2+448t^4+448t^6.
\]
At \(m=2,q=2\) the spectrum is \(8+24t^2+32t^4\). The formula also counts the possible dimensions of coadjoint stabilizer Lie algebras by subtracting rank from \(\dim L_m\).

## Assumptions and scope
Fix \(m\ge2\), a finite field \(K\) with \(q=2^s\) elements and \(s\ge1\). The Lie algebra \(L_m\), introduced by Gallo and Videla for the star graph, has basis
\[
c,\ x_1,\dots,x_m,\ a_1,\dots,a_m,\ z_{ij}\quad(1\le i<j\le m).
\]
The nonzero brackets on these basis elements, up to alternation, are \([c,x_i]=a_i\) and \([x_i,a_j]=[x_j,a_i]=z_{ij}\) for \(i<j\). The elements \(z_{ij}\) are central and all other unspecified brackets vanish. Hence \(n=\dim_K L_m=1+2m+\binom m2\). The Kirillov rank spectrum is a function counting \(K\)-linear functionals, not a classification of group characters, geometric coadjoint orbits, or additive commutator fibers.

## Proof
**Step 1 (reduce the full form to one augmented matrix).** For any \(\lambda\in L_m^*\), set \(\alpha_i=\lambda(a_i)\) and \(\beta_{ij}=\lambda(z_{ij})\). In the direct-sum ordering of the \(m\) leaf vectors followed by \(c,a_1,\dots,a_m\) and then the central vectors, the Kirillov matrix is
\[
\mathcal K_\lambda=\begin{pmatrix}0&T&0\\-T^{\mathsf T}&0&0\\0&0&0\end{pmatrix},
\qquad T=\begin{pmatrix}-\alpha&B\end{pmatrix},
\]
where \(B\) is the \(m\times m\) symmetric zero-diagonal matrix with \(B_{ij}=\beta_{ij}\). Consequently \(\operatorname{rank}\mathcal K_\lambda=2\operatorname{rank}T\). This identity holds even in characteristic two because a block off-diagonal matrix has twice the rank of its off-diagonal block. The values of \(\lambda\) on \(c,x_1,\dots,x_m\) do not enter the bracket, giving \(q^{m+1}\) functionals for each choice of \((\alpha,B)\).

**Step 2 (alternating ranks).** In characteristic two, a symmetric zero-diagonal matrix is alternating. It has even rank, say \(2k\) with \(0\le k\le\lfloor m/2\rfloor\). The number of such matrices is exactly \(H_{m,k}(q)\): choose the \((m-2k)\)-dimensional radical (\({m\brack 2k}_q\) possibilities), then choose a nondegenerate alternating form on its \(2k\)-dimensional quotient. The latter number equals
\[
\frac{|\operatorname{GL}_{2k}(\mathbb F_q)|}{|\operatorname{Sp}_{2k}(\mathbb F_q)|}
=q^{k(k-1)}\prod_{j=1}^k(q^{2j-1}-1).
\]
This quotient count is valid in characteristic two because every nondegenerate alternating form has a symplectic basis and the symplectic group acts freely and transitively on ordered symplectic bases.

**Step 3 (the extra covector).** For fixed \(B\) of rank \(2k\), exactly \(q^{2k}\) choices of \(\alpha\in K^m\) lie in its column space; then \(\operatorname{rank}T=2k\). The remaining \(q^m-q^{2k}\) choices give \(\operatorname{rank}T=2k+1\). Therefore the two Kirillov ranks are \(4k\) and \(4k+2\), respectively. Multiplying these two counts by \(H_{m,k}(q)\) and the free factor \(q^{m+1}\), then summing \(k\), proves the stated polynomial.

**Step 4 (sharp maximum and consistency).** For even \(m\), there exists a nondegenerate alternating \(B\), hence \(\operatorname{rank}T=m\). For odd \(m\), take \(B\) of rank \(m-1\) and choose \(\alpha\) outside its column space, again giving \(\operatorname{rank}T=m\). Thus \(\max\operatorname{rank}\mathcal K=2m\), and subtracting from \(1+2m+\binom m2\) proves the index formula. Also \(P_{m,q}(1)=q^{m+1+m+\binom m2}=q^{\dim L_m}\), because the sum of the alternating-matrix rank classes is the entire \(q^{\binom m2}\)-element space and each admits \(q^m\) vectors \(\alpha\).

## Verification
The included standalone checker, `verify.py`, independently forms the defining bracket matrix for the star Lie algebra and counts ranks over \(\mathbb F_2\) and \(\mathbb F_4\). It exhausts the parameters \((\alpha,\beta)\) in six configurations \((m,q)=(2,2),(2,4),(3,2),(3,4),(4,2),(5,2)\). It checks all augmented-matrix ranks and compares their distributions with the closed formula. It separately verifies the entire original Kirillov block matrix for every parameter assignment at \(m\le3\) and for additional cases at \(m=4,5\). Every check passes; exact output is in `verification_output.txt`. These are finite corroborations, not the infinite-rank proof, which is the argument above.

## Relationship to prior work
Gallo and Videla, *Nilpotent Lie algebras of nilpotence class at most three via graphs*, arXiv:2610.33963v1 (October 25, 2026), Section 3, define the star algebra and compute its dimension, lower-central-series dimensions and center, not a distribution of Kirillov-form ranks. The present result uses their brackets without claiming their construction or structural dimensions are new.

Burde and Dekimpe, *The index of nilpotent Lie algebras*, arXiv:2505.08331v1, discuss indices of free nilpotent algebras, **two-step** graph Lie algebras and filiform algebras, primarily in characteristic zero; their index theorem does not give the full even-characteristic rank-multiplicity polynomial of the different class-three star construction. Earlier finite-graph two-step character-degree enumerations deal with alternating weighted graph adjacency matrices but not the augmented coadjoint matrix of this three-step family. A separately known element-commuting probability for characteristic-two stars counts commuting *elements*, not the dimensions of all coadjoint stabilizers and does not by itself fix the rank spectrum. The classical finite-field enumeration of alternating forms is used as established input rather than claimed as new.

## Limitations
This result is restricted to characteristic two and the star-graph class-three family. It gives exact counts of linear functionals by Kirillov rank, not individual orbits or group irreducible representations. No Baker–Campbell–Hausdorff character correspondence is asserted in characteristic two. The index is a consequence of the more detailed spectrum and is not claimed as an independent novelty. A general result on matrix pencils or an earlier implicit coadjoint enumeration could contain an equivalent formula; historical priority requires further expert inspection.

## References
1. A. L. Gallo and D. E. Videla, *Nilpotent Lie algebras of nilpotence class at most three via graphs*, arXiv:2610.33963v1, October 25, 2026. https://arxiv.org/html/2610.33963v1
2. D. Burde and K. Dekimpe, *The index of nilpotent Lie algebras*, arXiv:2505.08331v1, May 13, 2025. https://arxiv.org/html/2505.08331v1
