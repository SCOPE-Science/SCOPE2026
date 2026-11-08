# Complete finite-field product fibers for pairs of commuting square-zero matrices

## Finding

For every integer \(n\ge1\), every finite field \(\mathbb F_q\), and every matrix \(D\in M_n(\mathbb F_q)\), define the **ordered product fiber**
\[
\Phi_{n,q}(D)=\#\{(B,C)\in M_n(\mathbb F_q)^2:B^2=C^2=0,\ BC=CB=D\}.
\]
The exact fiber size is determined by the rank and square-zero condition on \(D\), with **one formula in every dimension and characteristic**. Let \({h\brack j}_q\) be the Gaussian binomial coefficient (zero outside \(0\le j\le h\)), and define
\[
\begin{aligned}
I_q(h,t)&=\prod_{i=0}^{t-1}(q^h-q^i),\\
M_q(u,d)&=\sum_{j=0}^{u}\sum_{\ell=0}^{d}(-1)^{u-j+\ell}
q^{\binom{u-j}{2}+\binom{\ell}{2}}{u\brack j}_q{d\brack\ell}_q q^{2j(d-\ell)},\\
Z_b(q)&=\sum_{0\le u\le k\le b}{b\brack k}_q{k\brack u}_q M_q(u,b-k).
\end{aligned}
\]
The convention for empty products is one, and \(Z_0(q)=1\). The complete answer is
\[
\boxed{\Phi_{n,q}(D)=\begin{cases}
Z_n(q),&D=0,\\
q^{3t^2+2t(n-4t)}I_q(n-2t,t)I_q(n-3t,t)Z_{n-4t}(q),&D^2=0,\ \operatorname{rank}D=t\ge1,\ 4t\le n,\\
0,&\text{otherwise.}
\end{cases}}
\]
In particular, every square-zero matrix of positive rank \(t\le\lfloor n/4\rfloor\) occurs as the product of commuting square-zero factors, and every product with positive rank outside this range is impossible. All nonzero matrices of the same admissible rank have the same fiber cardinality.

The first nonzero fiber, \(n=4,t=1\), has size \(q^3(q-1)(q^2-1)\), a previously established special case. The general formula additionally yields, for instance, \(\Phi_{5,2}(D)=672\) for each rank-one square-zero \(D\), and \(\Phi_{6,2}(D)=134400\) for each such \(D\). These examples are consequences, not substitutes for the general result.

## Assumptions and scope

The product map is restricted to **ordered** commuting square-zero pairs of matrices over the same finite field. Rank and square-zero are taken over \(\mathbb F_q\). A positive-rank square-zero target \(D\) has Jordan type \((2^t,1^{n-2t})\), so its conjugacy class is determined by \(t\); conjugation preserves the fiber. No field-characteristic restriction is imposed. The zero target is treated separately.

## Proof

**Zero-target fibers by two Möbius inversions.** The condition \(B^2=C^2=BC=CB=0\) means that the joint image \(U=\operatorname{im}B+\operatorname{im}C\) lies in the common kernel \(K=\ker B\cap\ker C\). For \(\dim U=u\), \(\dim K=k\), choosing the flag \(U\subseteq K\subseteq\mathbb F_q^b\) takes \({b\brack k}_q{k\brack u}_q\) choices. Both endomorphisms descend to maps \(\mathbb F_q^b/K\to U\). The defining exact image and kernel conditions say that their images jointly span \(U\) and their kernels intersect trivially. For \(d=b-k\), the number of such ordered map pairs is precisely \(M_q(u,d)\): subspace-lattice Möbius inversion enforces the spanning-image condition and an independent inversion enforces trivial common kernel. Specifically, choosing a possible smaller image of dimension \(j\) and a common kernel of dimension \(\ell\) leaves \(q^{2j(d-\ell)}\) maps, with Möbius weights \((-1)^{u-j}q^{\binom{u-j}{2}}\) and \((-1)^\ell q^{\binom\ell2}\). Summation gives \(Z_b(q)\), including \(b=0\), and hence the claimed \(D=0\) fiber.

**Nonzero-target block geometry.** Suppose \(D=BC=CB\ne0\), \(\operatorname{rank}D=t\). Then \(D^2=0\), while \(BD=DB=CD=DC=0\). Take a basis \(V=E\oplus H\oplus F\) in which \(D:F\to E\) is the identity, \(\dim E=\dim F=t\) and \(\dim H=a=n-2t\). The annihilation of \(D\) means the factors have unique block forms
\[
B=\begin{pmatrix}0&P&Q\\0&R&S\\0&0&0\end{pmatrix},\qquad
C=\begin{pmatrix}0&U&V_0\\0&T&H_0\\0&0&0\end{pmatrix}.
\]
Here \(P,U:H\to E\), \(S,H_0:F\to H\), \(R,T:H\to H\), and \(Q,V_0:F\to E\).

Comparing the blocks of the **four original equations** \(B^2=C^2=0\) and \(BC=CB=D\) gives
\[
PH_0=US=I_t,\quad PS=UH_0=0,\quad
PR=PT=UR=UT=0,\quad
R H_0=R S=T H_0=T S=0,
\]
together with \(R^2=T^2=RT=TR=0\). Conversely, all these conditions are sufficient, and \(Q,V_0\) are unrestricted.

The four left identities force \(S,H_0\) to be injections with disjoint images, so \(a\ge2t\), equivalently \(n\ge4t\). Choose \(H_0:F\hookrightarrow H\) in \(I_q(a,t)\) ways. For \(S\), its projection into \(H/\operatorname{im}H_0\) must be injective; it has \(I_q(a-t,t)q^{t^2}\) choices. With these injections fixed, the values of \(P,U\) on the two image subspaces are forced, while their values on a complementary \(b=a-2t=n-4t\) dimensional subspace are arbitrary: \(q^{2tb}\) choices. The two free blocks \(Q,V_0\) contribute \(q^{2t^2}\).

Set \(W=\ker P\cap\ker U\). Because \(PH_0=US=I_t\) and \(PS=UH_0=0\), one has \(H=\operatorname{im}H_0\oplus\operatorname{im}S\oplus W\) with \(\dim W=b\). The remaining equations say that \(R,T\) kill both image subspaces and have images in \(W\). Consequently they are precisely extensions by zero of a pair of endomorphisms of \(W\) satisfying \(R^2=T^2=RT=TR=0\), giving exactly \(Z_b(q)\) possibilities. Multiplication of the independent factors yields
\[
I_q(a,t)\,I_q(a-t,t)\,q^{t^2}\,q^{2tb}\,q^{2t^2}\,Z_b(q)
=q^{3t^2+2tb}I_q(a,t)I_q(a-t,t)Z_b(q).
\]
If \(4t>n\) no such pair can exist; for \(4t\le n\), the construction with \(R=T=0\) proves existence. Every step is a bijective parametrization; in particular scalar rescaling has not been quotiented out.

## Verification

The dependency-free script `check_product_fibers.py` evaluates the finite Gaussian/Möbius formula and exhaustively tests original zero-product equations for \(b=0,1,2,3\) over prime fields (including \(\mathbb F_3\) in dimension two). It also exhausts **all** candidate factor pairs for a fixed rank-one target in \(M_4(\mathbb F_2)\), testing \(B^2=C^2=0\) and \(BC=CB=D\) directly, and confirms the predicted fiber size \(24\). A separate `check_five_binary.py` verifies all 672 explicitly parametrized factor pairs for a rank-one target in dimension five against the four original equations, with results in `direct_five_binary_output.txt`. The main output is in `verification_output.txt`, with success marker `COMMUTING_SQUARE_ZERO_PRODUCT_FIBERS_OK`. All-dimensional formulas are proved by the preceding block argument and the two finite-subspace Möbius inversions; these finite checks do not prove them.

## Relationship to prior work

Kokol Bukovšek, Košir, Novak and Oblak characterize **which** matrices occur as products of commuting square-zero matrices, including the same rank bound and allowable Jordan types; this support characterization is prior and is not claimed new. An earlier finite-field census already determines the product fibers in \(4\times4\) matrices, including the \(n=4,t=1\) formula above, and an earlier double-flag enumeration gives the general zero-product pair count \(Z_b(q)\). Neither statement itself determines every nonzero fiber in arbitrary dimension. The new contribution is the uniform multiplicative reduction of **all** nonzero product fibers to the known zero-product counts and the resulting explicit all-dimensional law. Levy studies the geometry of pairs of commuting square-zero matrices in characteristic two, while Britnell and Wildon study commuting similarity-class incidence. These results do not give the all-dimensional product-fiber multiplicities.

## Limitations

This theorem counts labeled ordered matrix pairs, not simultaneous-conjugacy orbits, and concerns square-zero factors with the *commuting* requirement. The zero-fiber count \(Z_b(q)\) is included explicitly by finite Gaussian sums; its previously known double-flag interpretation is credited. The original \(4\times4\) fiber result and qualitative product characterization remain prior work. An unidentified broader factorization-fiber theorem may subsume the exact formula; independent historical-priority validation has not been carried out.

## References

1. P. Levy, *Varieties of Modules for Z/2Z × Z/2Z* (2006-09-06 first public version), arXiv:math/0609180. https://arxiv.org/abs/math/0609180
2. D. Kokol Bukovšek, T. Košir, N. Novak and P. Oblak, *Products of commuting nilpotent operators*, Electron. J. Linear Algebra 16 (2007), 237–247, Theorems 2.2–2.3. https://journals.uwyo.edu/index.php/ela/article/download/455/455/455
3. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields* (2010-01-06 first public version), arXiv:1001.0811. https://arxiv.org/abs/1001.0811
