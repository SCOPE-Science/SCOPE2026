# Complete support-shape Fourier-rank diagram on the six-element nonabelian group

## Finding
Let \(G=S_3=\langle r,s\mid r^3=s^2=e,\ srs=r^{-1}\rangle\), and let \(f:G\to\mathbb C\) be nonzero. Let \(a,b\) denote the numbers of nonzero coefficients on the rotation coset \(\{e,r,r^2\}\) and reflection coset \(\{s,sr,sr^2\}\), reordered so \(a\ge b\). Define the rank-weighted Fourier support
\[
\mu(f)=\sum_{\rho\in\widehat G}(\dim\rho)\operatorname{rank}\widehat f(\rho),
\]
which equals the rank of unnormalized left convolution by \(f\) on \(\mathbb C[G]\). For **every fixed nonempty subset** of shape \((a,b)\), as all coefficients on that subset vary freely over \(\mathbb C\setminus\{0\}\), exactly the following \(\mu\)-values occur:

| Support shape \((a,b)\) | Exact attainable \(\mu(f)\) |
|:--|:--|
| \((1,0)\) | \(\{6\}\) |
| \((2,0)\) | \(\{4,6\}\) |
| \((1,1)\) | \(\{3,6\}\) |
| \((3,0)\) | \(\{2,4,6\}\) |
| \((2,1)\) | \(\{4,5,6\}\) |
| \((3,1)\) | \(\{3,4,5,6\}\) |
| \((2,2)\) | \(\{2,3,4,5,6\}\) |
| \((3,2)\) | \(\{2,3,4,5,6\}\) |
| \((3,3)\) | \(\{1,2,3,4,5,6\}\) |

The four-point transition is particularly sharp: an unbalanced three–one support cannot have rank two, but **every** balanced two–two support can. The three-tap cases are known from prior work; the novel scope is the complete diagram including all higher sparsities and coefficient choices.

## Assumptions and scope
No positivity, integrality, reality or modulus restriction is imposed on nonzero complex coefficients. The support consists **exactly** of the chosen locations, not merely a subset thereof. Count in either coset first and sort the two counts; the coset swap preserves rank. The Fourier transform can be taken with unitary-representation inverses or without them: the rank-weighted support is identical after the standard equivalent-convention transformation. All ranks are complex ranks of unnormalized convolution (normalization by a nonzero scalar does not affect rank).

## Proof
**1. Exact Fourier block formula.** Order group elements \(e,r,r^2,s,sr,sr^2\) and write the coefficients as \(u=(u_0,u_1,u_2)\) and \(v=(v_0,v_1,v_2)\). Set
\[
A(z)=u_0+u_1z+u_2z^2,\qquad B(z)=v_0+v_1z+v_2z^2,
\]
\(\omega=\exp(2\pi i/3)\), \(U=A(1)\), \(V=B(1)\). The two one-dimensional irreducible Fourier blocks are \(U+V\) and \(U-V\). With \(\rho(r)=\operatorname{diag}(\omega,\omega^2)\), \(\rho(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), the two-dimensional block is
\[
M=\begin{pmatrix}A(\omega)&B(\omega^2)\\ B(\omega)&A(\omega^2)\end{pmatrix}.
\]
Consequently
\[
\mu(f)=\mathbf1_{U+V\ne0}+\mathbf1_{U-V\ne0}+2\operatorname{rank}M.\tag{1}
\]
This follows directly from the irreducible decomposition of the regular representation, where the two-dimensional block occurs twice.

Define the homogeneous quadratic form
\[
Q(x_0,x_1,x_2)=x_0^2+x_1^2+x_2^2-x_0x_1-x_0x_2-x_1x_2.
\]
The identities \(1+\omega+\omega^2=0\) and \(\omega\omega^2=1\) give
\[
\det M=Q(u)-Q(v).\tag{2}
\]
Moreover \(M=0\) exactly when both triples are constant: \(u_0=u_1=u_2\) and \(v_0=v_1=v_2\). Indeed both nontrivial Fourier coefficients of a length-three vector vanish if and only if it is constant. Thus \(\operatorname{rank}M=0,1,2\) according to the exact alternatives \(M=0\), \(M\ne0\) with \(Q(u)=Q(v)\), and \(Q(u)\ne Q(v)\).

**2. Support geometry depends only on the two counts.** Left and right translation \(f(g)\mapsto f(r^p g r^q)\) shifts rotation positions by \(p+q\) and reflection positions by \(q-p\), modulo three. The map \((p,q)\mapsto(p+q,q-p)\) is invertible over \(\mathbb Z/3\mathbb Z\), so the two cosets can be shifted independently. Any subset of a three-cycle of a given size is a cyclic shift of its first \(a\) positions. Left multiplication by \(s\) interchanges the two cosets. Left/right translations change convolution by pre-/postcomposition with invertible regular translations, so preserve \(\mu\). It is therefore enough to realize ranks using canonical supports \(u_0,\ldots,u_{a-1}\) and \(v_0,\ldots,v_{b-1}\), leaving the remaining entries exactly zero.

**3. Exclude every unlisted rank.** Write \(k\) for the number of nonzero one-dimensional blocks in (1), so \(k\in\{0,1,2\}\), and let \(m=\operatorname{rank}M\in\{0,1,2\}\). Then \(\mu=k+2m\). The following deductions are exhaustive.

* At support shape \((1,0)\), the two one-dimensional blocks are nonzero and \(M\) is invertible, giving \(\mu=6\).
* At shape \((2,0)\), the one-dimensional blocks coincide: they are either both nonzero or both zero. The standard block is diagonal and cannot be zero, since a nonzero two-supported triple cannot be constant. Thus only \(\mu=4,6\). At \((3,0)\) the same parity argument applies, now permitting \(M=0\) when the rotation triple is constant; only \(\mu=2,4,6\) can occur.
* At shape \((1,1)\), translate the two nonzero coefficients to \(u_0=\alpha,v_0=\beta\), both nonzero. Equation (2) is \(\alpha^2-\beta^2\); if \(\alpha=\pm\beta\), precisely one one-dimensional block vanishes and \(m=1\), giving \(\mu=3\). Otherwise both blocks are nonzero and \(m=2\), giving \(\mu=6\).
* At \((2,1)\), normalize to \(u=(\alpha,\beta,0)\), \(v=(\gamma,0,0)\), all three nonzero. The matrix \(M\) cannot vanish. The two one-dimensional blocks cannot both vanish because that would force \(\gamma=0\). If either block vanishes then \(\gamma=\pm(\alpha+\beta)\), while (2) becomes \(\det M=\alpha^2-\alpha\beta+\beta^2-(\alpha+\beta)^2=-3\alpha\beta\ne0\). Thus \(k=1\) forces \(m=2\), and the only ranks are \(4,5,6\).
* At \((3,1)\), since the lone reflection coefficient is nonzero, the two one-dimensional blocks cannot simultaneously vanish; also \(M\ne0\) since a singleton reflection triple is not constant. Thus \(k\ge1\), \(m\ge1\), and the possible ranks are contained in \(\{3,4,5,6\}\).
* At either \((2,2)\) or \((3,2)\), \(M=0\) is impossible because at least one triple has two nonzero entries and a zero. Hence \(m\ge1\), so \(\mu\ge2\); all ranks are at most six.
* At \((3,3)\), the only general bounds are \(1\le\mu\le6\), since the Fourier transform is invertible as a linear transformation and \(f\ne0\).

**4. Explicit exact witnesses establish all inclusions.** The standalone file `VERIFY.py` contains a 31-case table covering **every one of the allowed rank/shape pairs** and checking nonzero support, both the formula (1)–(2), and independently the exact rank of the full \(6\times6\) regular-convolution matrix. All 31 checks pass. Most witnesses have small nonzero integer coefficients; the single Gaussian-integer witness for \((3,2)\) at rank three is
\[
(u_0,u_1,u_2;v_0,v_1,v_2)=(1,1,2;\,2+i,2-i,0).
\]
Here \(U=V=4\), \(Q(u)=Q(v)=1\) and \(M\ne0\), so (1) gives \(\mu=1+2=3\). In the same shape, rank two is witnessed by \((3,5,-8;7,-7,0)\): both one-dimensional blocks vanish, \(Q(u)=Q(v)=147\), and \(M\ne0\). The remaining listed ranks follow by the exact calculations in `VERIFY.py`. Independent coset-shift invariance from step 2 transfers each canonical witness to **every fixed support** of its shape. The exclusions in step 3 plus existence for every admissible pair finish the classification.

## Verification
Run `python3 VERIFY.py` with Python 3 and SymPy installed. The checker computes the rank of the complete regular convolution matrix over exact algebraic arithmetic, independently calculates the irrep decomposition rank from (1)–(2), and compares each of 31 explicit witnesses with its claimed rank. It also cross-checks all support locations of sizes one through four with all nonzero weights in \(\{1,-1,2\}\), computing both ranks from scratch. Output is recorded in `CHECK_OUTPUT.txt`. These extra finite tests corroborate the proof; the universal quantifiers over arbitrary complex coefficients are established by steps 1–3, **not** inferred from finite enumeration.

## Relationship to prior work
Alagic–Russell's nonabelian uncertainty inequality provides the rank-weighted Fourier-support framework, but only a lower bound, not a complete attainable-rank diagram. Meshulam's earlier work gives general support inequalities, not the nine support-shape strata. A published complete three-tap dihedral classification **already establishes** both three-tap rows; we do not claim them as new. A separate balanced four-tap study analyzes **unit-weight** two–two supports and their singular values, rather than arbitrary complex weights, the unbalanced four-point shape, or five-/six-point spectra. The current finding combines these slices with genuinely new coefficient-sensitive four-, five-, and six-tap attainability and gap assertions into one complete first-nonabelian-group diagram.

## Limitations
Only the six-element group \(S_3\) is classified. The theorem concerns rank, not numerical singular-value conditioning, and the phase of coefficients matters. It neither extends to every dihedral group nor implies a sharp global nonabelian uncertainty inequality. The three-tap rows are already covered by earlier work. A differently presented prior exhaustive group-algebra table could be equivalent; the searches and relevant primary texts inspected do not rule out unindexed priority. The complete classification is limited to this one nonabelian group and does not quantify singular-value stability.

## References
1. R. Meshulam, *An Uncertainty Inequality for Groups of Order pq*, European Journal of Combinatorics **13** (1992), 401–407. DOI: https://doi.org/10.1016/S0195-6698(05)80019-8 . Public copy: https://meshulam.net.technion.ac.il/files/2021/05/uncer_pq.pdf . The source gives September 1992 but no verified calendar day.
2. R. Meshulam, *An Uncertainty Inequality for Finite Abelian Groups*, first posted 2003-12-22, https://arxiv.org/abs/math/0312407 . The abelian scope is distinct from the nonabelian rank problem.
3. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, first posted 2006-08-28, https://arxiv.org/abs/math/0608702 .
4. *Complete three-tap Fourier-rank spectrum on odd-prime dihedral groups*, publicly available 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-complete-three-tap-fourier-rank-spectrum-on-odd-prime-dihedral-g--eb09d9b17153 .
5. *Balanced four-tap generalized-dihedral convolution: three nullity strata and a sharp quadratic spectral gap*, publicly available 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-balanced-four-tap-generalized-dihedral-convolution-three-nullity--d4787ab578c7 .
