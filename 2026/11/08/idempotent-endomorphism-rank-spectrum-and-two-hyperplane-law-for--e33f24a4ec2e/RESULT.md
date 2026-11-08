# Idempotent endomorphism rank spectrum and two-hyperplane law for a solvable Leibniz algebra

## Finding

Let \(q\) be any prime power and \(m\geq 0\). On the vector space
\(L_m=\mathbb F_q e_1\oplus\mathbb F_q e_2\oplus W\), where
\(\dim W=m\), define a left Leibniz bracket by
\([e_2,e_1]=e_1\), all other basis brackets being zero. This is the
non-Lie, nonnilpotent Leibniz algebra consisting of the two-dimensional
nonabelian factor and an \(m\)-dimensional abelian factor.

For integers \(d\geq0\) and \(k\), put
\[
I_d(k;q)=
\begin{cases}
\displaystyle {d\brack k}_q\,q^{k(d-k)},&0\leq k\leq d,\\
0,&\text{otherwise},
\end{cases}
\qquad
{d\brack k}_q=\prod_{i=0}^{k-1}\frac{q^{d-i}-1}{q^{k-i}-1}.
\]
Thus \(I_d(k;q)\) is the number of rank-\(k\) linear idempotents on
\(\mathbb F_q^d\). Let \(R_{m,k}(q)\) count the **idempotent Leibniz
endomorphisms** \(P:L_m\to L_m\) of linear image rank \(k\). Then for
every integer \(0\leq k\leq m+2\),
\[
\boxed{
R_{m,k}(q)=I_{m+1}(k;q)
 +(q^{2k}-q^k)I_m(k;q)
 +\mathbf1_{\{k\geq2\}}q^{m-k+2}I_m(k-2;q).
}
\]
This formula, with the stated zero convention, includes the zero map and
the identity, which are the unique idempotents of ranks \(0\) and
\(m+2\), respectively. The three terms result from two maximal abelian
hyperplanes and nonabelian retracts, with their intersection subtracted.

More precisely, put \(H_1=\mathbb F_q e_1\oplus W\) and
\(H_2=\mathbb F_q e_2\oplus W\). The numbers of rank-\(k\)
idempotent endomorphisms having image in \(H_1\), in \(H_2\), and in
\(W=H_1\cap H_2\), respectively, are
\[
q^{2k}I_m(k;q),\qquad I_{m+1}(k;q),\qquad q^k I_m(k;q).
\]
All other idempotent endomorphisms have nonabelian image isomorphic to
the corresponding lower-dimensional algebra \(L_{k-2}\); their number is
\(q^{m-k+2}I_m(k-2;q)\), for \(2\leq k\leq m+2\).

Write \(J_d(q)=\sum_{k=0}^d I_d(k;q)\) and
\(N_m(q)=\sum_k R_{m,k}(q)\). For **fixed** \(q\), as \(m\to\infty\),
\[
\boxed{N_m(q)=2J_{m+1}(q)\bigl(1+O_q(q^{-m/2})\bigr).}
\]
A uniform random idempotent endomorphism has image contained in exactly
one of \(H_1,H_2\) with limiting probability \(1/2\) for each
hyperplane. Its probability of nonabelian image, or image contained in
both hyperplanes, is \(O_q(q^{-m/2})\).

The count has a sharp theta-type asymptotic. Set
\[
c_q=\prod_{j=1}^{\infty}(1-q^{-j}),\qquad
\Theta_{\delta}(q)=\sum_{z\in\mathbb Z+\delta}q^{-2z^2},
\quad \delta\in\{0,1/2\}.
\]
With \(d=m+1\) and \(\delta=0\) for even \(d\),
\(\delta=1/2\) for odd \(d\),
\[
\boxed{
N_m(q)\sim \frac{2\Theta_\delta(q)}{c_q}\,q^{d^2/2}.
}
\]
If \(K_m\) denotes the rank of a uniformly random idempotent
endomorphism, then along either parity of \(d=m+1\), the centered rank
\(K_m-d/2\) converges in distribution on \(\mathbb Z+\delta\) to
\[
\Pr(K_m-d/2=z)\longrightarrow
\frac{q^{-2z^2}}{\Theta_\delta(q)}
\quad\text{for each fixed }z\in\mathbb Z+\delta.
\]

## Assumptions and scope

The finite formula holds for every prime power \(q\), including even
characteristic, and for \(m=0\). The algebra is **explicitly defined**
by the displayed bracket; no classification of all Leibniz algebras in
characteristic two is asserted. The limit theorems hold for fixed
\(q\) as \(m\) increases, not when \(q\) varies with \(m\).

Here *idempotent* means \(P\circ P=P\) for an **algebra
endomorphism**, not an element \(x\in L_m\) satisfying \([x,x]=x\).
Such an endomorphism is a retraction onto the Leibniz subalgebra that
forms its image.

## Proof

**1. Endomorphism dichotomy.** Write \(\alpha(x)\) and \(\beta(x)\)
for the \(e_1\)- and \(e_2\)-coordinates of \(x\). Then
\([x,y]=\beta(x)\alpha(y)e_1\), which directly verifies the left
Leibniz identity. For any algebra endomorphism \(P\),
\[
P(e_1)=P([e_2,e_1])=[P(e_2),P(e_1)]\in\mathbb F_qe_1.
\]
Write \(P(e_1)=a e_1\). If \(a\ne0\), applying bracket preservation
to all basis pairs forces
\[
P(e_1)=a e_1,\qquad P(e_2)=e_2+v,\qquad P(w)=B(w)
\quad(w\in W),
\]
where \(v\in W\), \(B\in\operatorname{End}_{\mathbb F_q}(W)\).
The condition \(P^2=P\) is exactly
\(a=1\), \(B^2=B\), \(Bv=0\). In this case the image is
nonabelian. When \(\operatorname{rank}B=r\), there are
\(I_m(r;q)\) choices of \(B\) and \(q^{m-r}\) choices of \(v\)
in its kernel. Its image has rank \(r+2\).

If \(a=0\), then \(P(e_1)=0\) and all images commute:
\([P(x),P(y)]=0\) for every \(x,y\). Thus
\((\beta\circ P)(x)(\alpha\circ P)(y)=0\) for all \(x,y\).
Over a field a tensor product of two linear functionals vanishes only
when at least one factor vanishes. Therefore \(\operatorname{im}P\)
lies in \(H_1=\ker\beta\) or \(H_2=\ker\alpha\). Conversely, an
idempotent linear map killing \(e_1\) and taking values in either
hyperplane is an algebra endomorphism: both sides of the bracket
preservation identity vanish.

**2. Count the abelian images.** When \(\operatorname{im}P\subseteq
H_2\), the restriction \(P|_{H_2}\) is an arbitrary linear
idempotent of rank \(k\) on the \((m+1)\)-space \(H_2\), and
\(P(e_1)=0\). The count is \(I_{m+1}(k;q)\).

When \(\operatorname{im}P\subseteq H_1\), the equation
\(P(e_1)=0\) implies \(\operatorname{im}P\cap\mathbb F_qe_1=0\):
otherwise idempotence would require \(P(e_1)=e_1\). Each possible
image is the graph of a linear functional on some \(k\)-space
\(U\subseteq W\). There are \({m\brack k}_q q^k\) such images.
For a fixed image, choosing the projection of \(W\) onto \(U\)
requires \(q^{k(m-k)}\) choices, and \(P(e_2)\) can be any of
\(q^k\) elements of the image. Hence this case contributes
\(q^{2k}I_m(k;q)\).

The intersection of the two cases consists of maps with image
contained in \(W\). They are determined by a rank-\(k\) projection
on \(W\) and an arbitrary image value of \(e_2\), giving
\(q^kI_m(k;q)\). Inclusion-exclusion, followed by addition of the
nonabelian case from Step 1, proves the boxed rank formula. For a
\(d\)-space the elementary count of projections is
\({d\brack k}_q q^{k(d-k)}\): choose the \(k\)-dimensional image,
then one of the \(q^{k(d-k)}\) complementary kernels.

**3. Uniform asymptotic estimates.** Set
\(c_{q,d}=\prod_{j=1}^d(1-q^{-j})\), with \(c_{q,0}=1\). Then
\[
I_d(k;q)=q^{2k(d-k)}
\frac{c_{q,d}}{c_{q,k}c_{q,d-k}},
\qquad
1\leq\frac{c_{q,d}}{c_{q,k}c_{q,d-k}}\leq c_q^{-1}.
\]
The factor tends to \(c_q^{-1}\) whenever both \(k\) and
\(d-k\) tend to infinity. The bound is uniform and the quadratic
identity
\(2k(d-k)=d^2/2-2(k-d/2)^2\) gives summable tails.
Consequently
\[
J_d(q)\sim c_q^{-1}q^{d^2/2}
\sum_{z\in\mathbb Z+\delta}q^{-2z^2},
\]
with the parity convention in the finding.

For the two abelian-hyperplane totals write
\(A_m=\sum_k q^{2k}I_m(k;q)\) and
\(B_m=J_{m+1}(q)\). The exact Gaussian-binomial relation is
\[
q^{2k}I_m(k;q)
=I_{m+1}(k;q)\frac{q^{m+1}-q^k}{q^{m+1}-1}
\quad(0\leq k\leq m+1),
\]
using \(I_m(m+1;q)=0\). Thus
\(B_m-A_m=O_q(q^{-m/2}B_m)\). The overlap and nonabelian totals are
\[
X_m=\sum_{k=0}^{m}q^kI_m(k;q),\qquad
C_m=\sum_{r=0}^{m}q^{m-r}I_m(r;q).
\]
In each sum the exponent, after inserting the Gaussian bound, is a
concave quadratic of maximum
\(m^2/2+m/2+1/8\); its shifted discrete-Gaussian sum is bounded
uniformly in \(m\). Meanwhile
\(B_m\geq q^{\lfloor (m+1)^2/2\rfloor}\). Hence
\(X_m+C_m=O_q(q^{-m/2}B_m)\). We obtain
\[
N_m=A_m+B_m-X_m+C_m=2B_m(1+O_q(q^{-m/2})).
\]
It follows that the fractions from \(H_1\setminus H_2\) and
\(H_2\setminus H_1\) tend to \(1/2\) each, while the overlap
and nonabelian fractions vanish at the claimed rate. Moreover,
for each fixed centered rank \(z\), the rank-\(k\) formula with
\(k=(m+1)/2+z\) equals \(2I_{m+1}(k;q)(1+o(1))\).
Together with the theta asymptotic for \(J_{m+1}\), this proves
the discrete-Gaussian rank law.

## Verification

Run `python3 verify.py` in the directory containing the accompanying
standalone script. The script constructs every linear map on the
small indicated vector spaces, checks multiplication of its full
matrix to establish \(P^2=P\), checks the original Leibniz bracket
on every ordered basis pair, and computes its rank by elimination.
It compares the rank counts and the four image categories separately.

Exhaustive checks were completed for
\((q,m)=(2,0),(3,0),(5,0),(2,1),(3,1),(2,2)\).
For example, the rank spectra for \(q=2\) and \(m=0,1,2\) were
\((1,1,1)\), \((1,8,3,1)\), and \((1,40,44,13,1)\).
Independent integer formula consistency checks cover
\(m=0,\ldots,19\) for \(q\in\{2,3,5\}\); larger sizes provide
numerical asymptotic sanity checks. The script ends with `VERIFY_OK`.
These finite tests do not prove the infinite assertions; the proof above does.

## Relationship to prior work

Di Bartolo, La Rosa and Mancini identify the algebra \(L_m\) (under a
dimension-shifted notation) among non-nilpotent non-Lie Leibniz
algebras with one-dimensional derived algebra, and determine its
derivations, automorphisms and biderivations. The bracket and the
classification over fields of characteristic different from two
are established results, not new claims here. Their cited paper does
not present the rank enumeration of idempotent algebra endomorphisms
used above.

Ruan, Hao and Chen investigate direct-sum decompositions using
idempotents in the **centroid**, which is a narrower algebraic
condition than being an idempotent element of the endomorphism
**monoid**. Neither their splitting criterion nor the usual Gaussian
count of linear projections determines the present formula without
the Leibniz-specific endomorphism dichotomy and overlap count.

The formula \({d\brack k}_q\,q^{k(d-k)}\) for ordinary linear
idempotents and its theta asymptotic are standard comparison facts;
novelty is not claimed for these independently. The contribution
assessed here is their exact, structurally weighted combination for
this Leibniz family and the resulting two-hyperplane limit law.

## Limitations

The result treats the explicitly presented split family; it does not
classify retractions of other solvable or nilpotent Leibniz algebras.
For characteristic two it asserts properties of this presented
algebra only, not an exhaustive classification of all algebras with
the same derived dimension. The asymptotics require fixed \(q\), and
the local rank limit is parity-dependent. An unlocated general theorem
on endomorphism retractions of bilinear rank-one algebras could imply
this special-case count; publication priority is therefore provisional.
Independent mathematical validation has not been performed.

## References

1. A. Di Bartolo, G. La Rosa, M. Mancini, *Non-Nilpotent Leibniz Algebras with One-Dimensional Derived Subalgebra*, arXiv:2307.09102 (first posted 2023-07-18); Mediterranean Journal of Mathematics 21 (2024), article 138. https://arxiv.org/abs/2307.09102 ; https://doi.org/10.1007/s00009-024-02679-0
2. J. Ruan, Z. Hao, L. Chen, *On Decompositions of Leibniz Algebras* (public preprint uploaded September 2024), DOI:10.13140/RG.2.2.24174.83520. https://doi.org/10.13140/RG.2.2.24174.83520
