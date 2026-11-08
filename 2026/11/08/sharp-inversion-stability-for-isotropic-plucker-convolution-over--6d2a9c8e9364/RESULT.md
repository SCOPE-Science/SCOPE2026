# Sharp inversion stability for isotropic-Plucker convolution over finite symplectic spaces

## Finding

Let \(q\) be any prime power, let \(n=2m\ge6\), and let \((V,\Omega)\) be an \(n\)-dimensional symplectic vector space over \(\mathbb F_q\). The natural cone of nonzero totally isotropic decomposable bivectors is
\[
C_\Omega=\{u\wedge v\in\bigwedge^2V:\ u,v\in V,\ u\wedge v\ne0,\ \Omega(u,v)=0\}.
\]
On the additive group \(W=\bigwedge^2V\), consider the **unweighted, unnormalized** convolution
\[
(Tf)(z)=\sum_{w\in C_\Omega}f(z+w),\qquad f:W\to\mathbb C.
\]
It is invertible for **every** prime-power field, including characteristic two. Its sharp singular-value endpoints and exact spectral condition number are
\[
\boxed{\ \sigma_{\min}(T)=\frac{q^{n-2}-1}{q^2-1},\qquad
\sigma_{\max}(T)=\frac{(q^n-1)(q^{n-2}-1)}{q^2-1},\qquad
\kappa_2(T)=q^n-1.\ }
\]
For every alternating-bilinear Fourier frequency \(B\), all eigenvalues lie in the arithmetic lattice
\[
\lambda_B=j(B)q^{n-2}-\frac{q^{n-2}-1}{q^2-1},
\qquad j(B)\in\mathbb Z,\quad j(B)\ge-1.
\]
The least-stable frequencies are **precisely** those with \(j(B)=0\). Equivalently, among the \(q\) forms in the pencil \(B+t\Omega\), exactly one has corank two and every other one is nondegenerate. Such frequencies exist in every covered parameter range. The theorem supplies an eigenvalue for each character, not a closed count of the multiplicity of every distinct eigenvalue.

## Assumptions and scope

All dimensions are over \(\mathbb F_q\). The form \(\Omega\) is alternating and nondegenerate; \(n=2m\ge6\) and \(q\ge2\). The ground additive character \(\psi:\mathbb F_q\to\mathbb C^\times\) is any fixed nontrivial additive character. For each alternating bilinear form \(B\) on \(V\), denote by the same letter its unique induced linear functional on \(\bigwedge^2V\), and define \(\chi_B(w)=\psi(B(w))\). These exhaust the characters of \(W\). Singular values use the counting \(\ell^2(W)\)-norm; scaling \(T\) by the support cardinality leaves its condition number unchanged.

For each \(t\in\mathbb F_q\), let
\[
2s_t=\dim\operatorname{rad}(B+t\Omega).
\]
This is an even integer because the rank of an alternating form is even, also in characteristic two. Write \([s]_{q^2}=(q^{2s}-1)/(q^2-1)\), with \([0]_{q^2}=0\), and
\[
J(B)=\sum_{t\in\mathbb F_q}[s_t]_{q^2},\qquad
\delta=\frac{q^{n-2}-1}{q^2-1}>0.
\]

## Proof

**1. Fourier multiplier.** The character \(\chi_B\) is an eigenvector of \(T\), with eigenvalue \(\lambda_B=\sum_{w\in C_\Omega}\psi(B(w))\). Every nonzero decomposable bivector \(w=u\wedge v\) has exactly \(|\mathrm{SL}_2(\mathbb F_q)|=q(q^2-1)\) ordered independent presentations \((u,v)\) with that exact wedge. Consequently
\[
q(q^2-1)\lambda_B
=\sum_{\substack{u,v\in V\text{ independent}\\\Omega(u,v)=0}}
\psi(B(u,v)).
\]
For any alternating form \(D\) of rank \(r\), summation first in \(v\) yields the exact identity
\[
\sum_{u,v\in V}\psi(D(u,v))=q^{2n-r}.
\]
The \(q^n+q(q^n-1)=q^{n+1}+q^n-q\) dependent ordered pairs contribute one to every such additive-character sum, and all satisfy \(\Omega(u,v)=0\). Inserting character orthogonality
\[\mathbf1_{\Omega(u,v)=0}=q^{-1}\sum_{t\in\mathbb F_q}\psi(t\Omega(u,v))\]
gives
\[
\lambda_B=
\frac{q^{n-2}\left(\sum_{t\in\mathbb F_q}q^{2s_t}-q(q+1)\right)+1}{q^2-1}.
\]
This derivation is valid over every prime-power field, not only prime fields.

**2. Integral lattice and exact lower endpoint.** Since \(\sum_t q^{2s_t}=q+(q^2-1)J(B)\), the previous formula simplifies to
\[
\lambda_B=q^{n-2}(J(B)-1)-\delta.
\]
The integer \(J(B)\) is nonnegative. If it is zero, then \(|\lambda_B|=q^{n-2}+\delta>\delta\). If it is one, then \(\lambda_B=-\delta\). If it is at least two, then
\[
|\lambda_B|\ge q^{n-2}-\delta>\delta,
\]
because \(2\delta<q^{n-2}\) for every \(q\ge2\) and \(n\ge6\). Hence **every** singular value is at least \(\delta\), and equality holds **if and only if** \(J(B)=1\). Since each positive term \([s]_{q^2}\) is at least one and equals one only for \(s=1\), this last condition is exactly the unique-corank-two pencil criterion.

**3. All-field attainment, including characteristic two.** Identify \(V=\mathbb F_q^m\oplus\mathbb F_q^m\) with
\[
\Omega((x,y),(x',y'))=x^{\mathsf T}y'-y^{\mathsf T}x'.
\]
Let \(N\) be one nilpotent Jordan block of size \(m\), and define
\[
B((x,y),(x',y'))=x^{\mathsf T}N^{\mathsf T}y'-y^{\mathsf T}N x'.
\]
This is alternating in all characteristics. Its pencil has block matrix
\[
B+t\Omega=\begin{pmatrix}
0&N^{\mathsf T}+tI_m\\ -(N+tI_m)&0
\end{pmatrix}.
\]
At \(t=0\), the corank is two because \(N\) has a one-dimensional kernel. At every \(t\ne0\), the nilpotence of \(N\) makes \(N+tI_m\) invertible, so the pencil is nondegenerate. Thus \(J(B)=1\) and \(\sigma_{\min}(T)=\delta\). The construction is valid for all \(m\ge3\) and every prime-power \(q\).

**4. Exact upper endpoint and invertibility.** The support size follows by counting ordered independent pairs with \(\Omega(u,v)=0\): there are \(q^n-1\) nonzero choices for \(u\), and \(q^{n-1}-q\) choices for \(v\) in \(u^{\perp_\Omega}\setminus\langle u\rangle\). Dividing by \(q(q^2-1)\),
\[
|C_\Omega|=\frac{(q^n-1)(q^{n-2}-1)}{q^2-1}=(q^n-1)\delta.
\]
The trivial character attains this eigenvalue; the triangle inequality \(|\lambda_B|\le|C_\Omega|\) proves it is \(\sigma_{\max}(T)\). Step 2 shows that no eigenvalue is zero. Fourier diagonalization therefore gives an everywhere-defined inverse on complex \(\ell^2(W)\) and exactly \(\kappa_2(T)=|C_\Omega|/\delta=q^n-1\).

## Verification

The scripts `CHECK_PRIME.py` and `CHECK_GF4.py` contain finite checks using independent exterior-product construction and direct Fourier sums, compared with the pencil-rank multiplier. Executing `python CHECK_PRIME.py` (NumPy required) checked complete Fourier spectra for \((q,n)=(2,4),(3,4),(2,6)\), including all \(32768\) frequencies of the dimension-six binary case; it also tested \(27\) explicit frequencies for \((q,n)=(3,6)\), including a nilpotent-Jordan minimizer. The dimension-four computations verify the normalization but are outside the new theorem's dimension scope. Executing `python CHECK_GF4.py` (standard library only) checked \(50\) Fourier frequencies of a four-dimensional symplectic space over \(\mathbb F_4\), including the correct trace character. Both scripts completed successfully. These finite checks corroborate the proof but are not a proof for arbitrary \(q,n\).

## Relationship to prior work

The isotropic Plücker geometry and its associated projective codes were studied by Cardinali and Giuzzi [1,2]. Their 2015 analysis relates hyperplane sections to eigenvectors of a pencil of alternating forms and determines the minimum distance of line symplectic Grassmann codes. It also gives the full weight enumerator in the four-dimensional Lagrangian case. The projective codeword weight \(\mathrm{wt}(B)\) is linked to the present convolution multiplier by
\[
\lambda_B=(q-1)L-q\,\mathrm{wt}(B),
\]
where \(L\) is the number of isotropic projective lines. Thus these are mathematically related descriptions, and **no separate novelty is claimed for the geometry, for the general character-orthogonality method, or for the dimension-four weight spectrum**. Determining a minimum codeword weight, however, does not identify the weight closest to \((q-1)L/q\), which controls the smallest absolute Fourier multiplier. The assertion here is the all-dimension, all-field **nearest-zero Fourier bound**, its exact condition number, and the necessary-and-sufficient least-stable-pencil characterization with an explicit attaining family. Literature comparisons did not locate those conclusions as stated; an implicit-corollary or historical-priority risk remains.

## Limitations

The claim begins at symplectic dimension six; it does not assert a new classification in dimension four. Its kernel is empty only for the specified **unweighted full isotropic cone**. Weighted subsets, noisy sampling design, other Grassmann ranks, and complete closed multiplicity formulas for every spectral level are not treated. The proof is mathematical and self-contained, but the literature-priority check is bounded and no independent mathematical audit has been performed.

## References

[1] I. Cardinali and L. Giuzzi, *Enumerative Coding for Line Polar Grassmannians with Applications to Codes*, first posted 2014-12-17, arXiv:1412.5466, https://arxiv.org/abs/1412.5466 (especially symplectic line enumeration and Plücker setup).

[2] I. Cardinali and L. Giuzzi, *Minimum Distance of Symplectic Grassmann Codes*, first posted 2015-03-17, arXiv:1503.05456, https://arxiv.org/abs/1503.05456 (especially Section 3, hyperplane intersections, Lemmas 3.1–3.3, Proposition 3.5).
