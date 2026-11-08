# Exact commutator fibers of split octonion algebras over odd finite fields

## Finding

Let \(q\) be any odd prime power, let \(\mathbb F_q\) be its field, and let \(\mathcal O_q\) be its split octonion algebra in the Zorn realization defined below. For each \(z\in\mathcal O_q\), write \(N_q(z)=\#\{(x,y)\in\mathcal O_q^2:xy-yx=z\}\). If \(\operatorname{tr}(z)\ne0\), then \(N_q(z)=0\). Otherwise write \(z=(d,s,t)\) in the seven trace-zero coordinates below and set \(Q(z)=d^2+4s\cdot t\). Let \(\chi\) be the quadratic character of \(\mathbb F_q\), extended by \(\chi(0)=0\). Then

\[
N_q(z)=\begin{cases}
q^{11}+q^{10}-q^5,&z=0,\\
q^9-q^5,&z\ne0,\ Q(z)=0,\\
q^9-q^5+(q^8-q^6)\chi(Q(z)),&Q(z)\ne0.
\end{cases}
\]

In particular, every trace-zero octonion is a commutator. The four labeled-fiber strata have sizes \(1\), \(q^6-1\), \(\tfrac{q-1}{2}(q^6+q^3)\), and \(\tfrac{q-1}{2}(q^6-q^3)\) for zero, nonzero isotropic, nonzero square-norm, and nonsquare-norm outputs, respectively. The nonzero fibers therefore detect the quadratic character of \(Q(z)\).

## Assumptions and scope

The field has odd characteristic; all cardinalities count **ordered** pairs of labeled elements, without quotienting by octonion automorphisms. The split Cayley algebra consists of Zorn vector matrices \([a,u;v,b]\) with \(a,b\in\mathbb F_q\) and \(u,v\in\mathbb F_q^3\), where

\[
[a,u;v,b][c,s;t,e]
=[ac+u\cdot t,\ as+eu-v\times t;\ cv+bt+u\times s,\ be+v\cdot s].
\]

Here \(\cdot\) and \(\times\) denote the standard dot and cross products on three-coordinate vectors. The trace is \(a+b\). Because \(2\) is invertible, each element splits uniquely as a scalar octonion plus a trace-zero element; identify the latter with \((d,s,t)\) via \([d/2,s;t,-d/2]\). The quadratic form \(Q(d,s,t)=d^2+4s\cdot t\) is nondegenerate of dimension seven, and its associated nondegenerate symmetric pairing is

\[\langle (d,s,t),(e,u,v)\rangle=de/2+s\cdot v+t\cdot u.\]

## Proof

**1. Explicit commutator and adjoint nullities.** Direct multiplication shows that for trace-zero \(x=(\delta,u,v)\) and \(y=(e,s,t)\), their octonion commutator has coordinates

\[
[x,y]=\bigl(2(u\cdot t-v\cdot s),\ \delta s-eu-2v\times t,\ -\delta t+ev+2u\times s\bigr).
\]

Scalar summands commute with everything and do not contribute. Consequently the full-octonion fiber is \(q^2\) times the trace-zero fiber. For any nonzero \(x\), the linear map \(y\mapsto[x,y]\) on the seven-dimensional trace-zero space has nullity \(3\) if \(Q(x)=0\), and nullity \(1\) if \(Q(x)\ne0\). At \(x=0\), its nullity is \(7\). We prove this directly.

If \(\delta\ne0\), the middle equation determines \(s=(eu+2v\times t)/\delta\). Substituting into the remaining vector equation and using the vector triple-product identity yields

\[
Q(x)\bigl(t-(e/\delta)v\bigr)=0.
\]

The scalar equation reduces to \(\delta (u\cdot t)=e(u\cdot v)\). For \(Q(x)\ne0\), one scalar \(e\) determines both vectors, giving nullity one. For \(Q(x)=0\), the relation \(u\cdot v=-\delta^2/4\ne0\) makes the scalar constraint independent, leaving three free coordinates. If \(\delta=0\) and \(u\cdot v\ne0\), dotting the middle equation with \(v\) forces \(e=0\); then \(t=av\), \(s=bu\), and the scalar equation gives \(a=b\), leaving one dimension. If \(\delta=0\), \(u\cdot v=0\), and \(u,v\ne0\), for each \(e\) the cross-product equations give affine lines for \(s,t\), and the scalar constraint holds automatically, leaving three free dimensions. If exactly one of \(u,v\) vanishes, the same dimension follows from one cross-product equation, one orthogonality constraint, and \(e=0\). This covers all cases.

**2. Fourier transform of the commutator distribution.** Let \(F(z)\) count ordered pairs in the trace-zero seven-space with commutator \(z\). Fix a nontrivial additive character \(\psi\) and define \(\widehat F(\lambda)=\sum_z F(z)\psi(\langle\lambda,z\rangle)\). Direct use of the dot/cross-product identities in the displayed bracket yields the invariance relation

\[
\langle \lambda,[x,y]\rangle=\langle [\lambda,x],y\rangle.
\]

Summing first over \(y\) gives \(q^7\) when \([\lambda,x]=0\), and zero otherwise. By the nullities just proved,

\[
\widehat F(\lambda)=\begin{cases}q^{14},&\lambda=0,\\q^{10},&\lambda\ne0,\ Q(\lambda)=0,\\q^8,&Q(\lambda)\ne0.\end{cases}
\]

**3. Fourier transform of the quadratic cone.** The nondegenerate quadratic form has exactly \(q^6\) zeros. Indeed, for any \(\delta\) and \(s\ne0\), the equation \(\delta^2+4s\cdot t=0\) allows \(q^2\) choices of \(t\), and the \(s=0\) contribution requires \(\delta=0\). Put \(K(z)=\sum_{\lambda:Q(\lambda)=0}\psi(-\langle\lambda,z\rangle)\). Orthogonality of \(\psi\) and completing the square show

\[
K(z)=\begin{cases}q^6,&z=0,\\0,&z\ne0,\ Q(z)=0,\\q^3\chi(Q(z)),&Q(z)\ne0.\end{cases}
\]

For completeness, if \(G=\sum_{w\in\mathbb F_q}\psi(w^2)\), the nonzero-\(a\) term in the orthogonality calculation for \(K(z)\) equals \(q^3\chi(a)G\psi(-Q(z)/(16a))\). The classical one-dimensional identity \(G^2=\chi(-1)q\) gives the displayed values; no restriction on \(q\bmod4\) is needed.

**4. Inversion and counts.** Fourier inversion, using the three Fourier coefficients above, gives

\[
F(z)=q^{-7}\bigl(q^{14}+q^{10}(K(z)-1)+q^8(q^7\mathbf1_{z=0}-K(z))\bigr).
\]

For \(z=0\), this is \(q^9+q^8-q^3\); for nonzero \(z\), it is \(q^7-q^3+(q^6-q^4)\chi(Q(z))\). Multiplication by \(q^2\) gives the claimed octonion fiber formula. A nondegenerate seven-dimensional quadratic space with \(q^6\) zeros has \(\tfrac{q-1}{2}(q^6+q^3)\) nonzero vectors of square norm and \(\tfrac{q-1}{2}(q^6-q^3)\) of nonsquare norm (obtained by the same Gaussian sum, or by direct hyperbolic splitting). The four strata sum to \(q^7\) trace-zero outputs and their multiplicity-weighted fiber sum is \(q^{16}\), accounting for all ordered input pairs. The nonzero expressions are strictly positive for odd \(q\), proving surjectivity onto the trace-zero space.

## Verification

The file `verify_commutator_fibers.py` implements trace-zero Zorn commutators and an independently programmed finite-field row-reduction solver; `verification_output.txt` contains its reproducible console output. Over \(\mathbb F_3\), the program examines all \(3^7=2187\) choices of the first trace-zero argument and all four representative output types using direct linear systems, producing exhaustive fiber counts. It additionally checks \(640\) reproducible first-argument samples over each of \(\mathbb F_5\) and \(\mathbb F_9\), with extension-field arithmetic implemented explicitly. It tests the adjoint-kernel nullity classification, the invariant bilinear pairing, and the weighted fiber mass identity. These finite tests corroborate, but do not prove, the all-field formula.

## Relationship to prior work

Castillo-Ramírez and Elduque (2015) give the split Cayley framework and the trace-zero commutator algebra in arbitrary characteristic, with primary MSC 17A75. Knarr and Stroppel (2023), Section 3.1, classify centralizers, including the zero-commutator fiber's underlying nullity data: the zero-fiber count is therefore a **known-structure consequence**, not the novelty asserted here. Lopatin and Zubkov (2022), Theorem 4.1 and Corollary 5.1, classify automorphism orbits of pairs over algebraically closed fields; their results do not state finite-field sizes of fixed-commutator fibers. De Mello and Saini (2026), Lemma 3.8 and Theorem 1.1, show that trace-zero elements are commutators and determine images of generalized commutators, not off-zero finite-field fiber populations.

The assessed new contribution is the **complete off-zero fiber law**, including the quadratic-character bias of \(q^8-q^6\) and exact output-stratum populations; the surjectivity and zero-fiber phenomena are explicitly credited. A broader finite-field orbit-enumeration or bilinear-map character-sum theorem might imply the result; this priority possibility remains unresolved and should be evaluated independently.

## Limitations

The formula assumes odd characteristic and the **split** Cayley algebra. It counts labeled ordered pairs, not automorphism orbits, and makes no claims for division octonions over other fields or characteristic two. The proof gives exact populations but not a parametrization of each solution fiber. Historical priority is provisional; independent mathematical auditing has not been performed.

## References

1. A. Castillo-Ramírez and A. Elduque, *Some special features of Cayley algebras, and \(G_2\), in low characteristics*, arXiv:1503.05529 (first posted 2015-03-18).
2. N. Knarr and M. J. Stroppel, *Subalgebras of Octonion Algebras*, arXiv:2303.00335 (2023), especially Section 3.1.
3. A. Lopatin and A. N. Zubkov, *Classification of \(G_2\)-orbits for pairs of octonions*, arXiv:2208.08122 (2022), Theorem 4.1 and Corollary 5.1.
4. T. Castilho De Mello and P. Saini, *Generalized Commutator on Octonion Algebra*, arXiv:2610.04466 (first posted 2026-10-03), Lemma 3.8 and Theorem 1.1.
