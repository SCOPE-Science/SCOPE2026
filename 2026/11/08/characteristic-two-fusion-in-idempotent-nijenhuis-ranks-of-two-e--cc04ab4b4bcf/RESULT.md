# Characteristic-two fusion in idempotent Nijenhuis ranks of two-eigenvalue Lie algebras

## Finding

For every integer \(n\ge1\) and prime power \(q\), put \(K=\mathbb F_q\). On
\[
\mathfrak g_n(K)=Ke\oplus U\oplus W,\qquad \dim_K U=\dim_K W=n,
\]
set \([e,u]=u\) for \(u\in U\), \([e,w]=-w\) for \(w\in W\), and \([U\oplus W,U\oplus W]=0\). Count **distinct linear maps** \(P:\mathfrak g_n(K)\to\mathfrak g_n(K)\) with \(P^2=P\) and zero Lie Nijenhuis torsion,
\[
[P x,P y]+P^2[x,y]-P([P x,y]+[x,P y])=0\quad\text{for all }x,y.
\]
Write \(N_{n,r}(q)\) for the number having rank \(r\), where \(0\le r\le2n+1\). Write \({a\brack b}_q\) for a Gaussian binomial coefficient, taken as zero unless \(0\le b\le a\).

**Even characteristic.** Every linear idempotent is Nijenhuis, so
\[
\boxed{N_{n,r}(q)={2n+1\brack r}_q q^{r(2n+1-r)}.}
\]

**Odd characteristic.** Define
\[
S_{n,k}(q)=\sum_{i+j=k}{n\brack i}_q{n\brack j}_q
\]
for every integer \(k\), with out-of-range coefficients understood to be zero. For \(0\le t\le2n-1\), define
\[
\begin{aligned}
T_{n,t}(q)=\sum_{i+j=t}\bigg(&\mathbf1_{i<n}{n\brack i}_q{n-i\brack1}_q q^{i(n-i-1)}{n\brack j}_q q^{j(n-j)}\\
+&\mathbf1_{j<n}{n\brack i}_q q^{i(n-i)}{n\brack j}_q{n-j\brack1}_q q^{j(n-j-1)}\bigg),
\end{aligned}
\]
where the sum ranges over \(0\le i,j\le n\), each indicated term is **omitted** if its condition fails, and \(T_{n,t}=0\) outside the stated range. Then the exact answer is
\[
\boxed{
N_{n,r}(q)=q^{r(2n-r+1)}\bigl(S_{n,2n-r}(q)+S_{n,r-1}(q)\bigr)
 +(q-1)q^{2n}T_{n,r-1}(q).
}
\]
Both formulas have \(N_{n,0}=N_{n,2n+1}=1\), all interior ranks occur, and \(N_{n,r}=N_{n,2n+1-r}\).

**Quantitative characteristic change.** Let \(H_n(q)=\sum_r N_{n,r}(q)\), and let \(I_n(q)\) denote the number of *all* linear idempotents on the same \((2n+1)\)-dimensional vector space. For every fixed odd prime power \(q\),
\[
\log_q H_n(q)=\tfrac32n^2+O_q(n),\qquad
\log_q I_n(q)=2n^2+O_q(n),\qquad
\boxed{H_n(q)/I_n(q)=q^{-n^2/2+O_q(n)}}.
\]
For every even \(q\), by contrast, \(H_n(q)/I_n(q)=1\) **exactly**, at every dimension. In odd characteristic, the number of Nijenhuis projections whose image and kernel both project nontrivially onto \(Ke\) is at most \(q^{n^2+O_q(n)}\), exponentially smaller on the quadratic scale than \(H_n(q)\). This is an eigenspace-fusion effect, not an arbitrary selection of subalgebra dimensions.

## Assumptions and scope

All Lie algebras are finite-dimensional over the indicated finite field. The bracket is defined by bilinearity and skew-symmetry, including the ordinary alternating convention in characteristic two. The Nijenhuis identity is the algebraic torsion identity displayed above; it does **not** mean the operator is a derivation, a homomorphism, an averaging map, or a Rota–Baxter map. A linear idempotent is counted once, not modulo automorphisms. Characteristic two makes \(-1=1\); no assumption that \(q\) is prime rather than a prime power is used in the proof.

## Proof

**1. Projection criterion, valid in every characteristic.** Write \(L=\operatorname{im}P\oplus\ker P\). The torsion of an idempotent projection is bilinear, and evaluating it on \(x,y\) in \(\operatorname{im}P\) gives \((I-P)[x,y]\). For \(x,y\in\ker P\), it gives \(P[x,y]\). For one vector in each summand it is zero. Thus
\[
P\text{ is Nijenhuis}\iff\operatorname{im}P\text{ and }\ker P\text{ are Lie subalgebras}.
\]
Every ordered pair of complementary Lie subalgebras corresponds to exactly one such projection, and rank equals the dimension of the first subalgebra.

**2. Subalgebras of an almost-abelian Lie algebra.** Put \(V=U\oplus W\) and let \(A=\operatorname{ad}_e|_V\), diagonal with eigenvalues \(1,-1\). A subspace \(B\subseteq\mathfrak g_n\) is a Lie subalgebra if and only if either (i) \(B\subseteq V\), or (ii) \(B=K(e+v)\oplus Z\), where \(Z=B\cap V\) is \(A\)-invariant and \(v\) is a coset in \(V/Z\). Indeed \([e+v,z]=Az\), and all brackets inside \(V\) vanish. For odd characteristic, the two eigenvalues are distinct, so \(Z=(Z\cap U)\oplus(Z\cap W)\). Consequently the number of invariant \(k\)-subspaces of \(V\) is exactly \(S_{n,k}(q)\).

**3. Exactly one complementary summand projects to \(Ke\).** Suppose the image lies in \(V\), has dimension \(r\), and the kernel has an \(A\)-invariant intersection \(Z\) with \(V\) of dimension \(2n-r\). There are \(S_{n,2n-r}\) choices for \(Z\), \(q^{r(2n-r)}\) ordinary complements to \(Z\) inside \(V\), and \(q^r\) lifts \(K(e+v)\) modulo \(Z\). The contribution is \(q^{r(2n-r+1)}S_{n,2n-r}\). Interchanging image and kernel gives \(q^{r(2n-r+1)}S_{n,r-1}\): the image's invariant part has dimension \(r-1\), its vector-space complement has dimension \(2n-r+1\), and its lift has \(q^{2n-r+1}\) choices. These two cases are disjoint.

**4. Both summands project to \(Ke\).** Write their respective invariant parts as \(Z_1,Z_0\subseteq V\), with dimensions \(r-1\) and \(2n-r\). The subspaces must be disjoint, and \(H=Z_1\oplus Z_0\) is a hyperplane in \(V\). For odd characteristic, each \(Z_i\) splits into its \(+1\) and \(-1\) eigenspaces. The codimension-one deficit of \(H\) occurs in exactly one eigenspace. If the image contains \(i\) dimensions of the \(+1\) eigenspace and \(j\) dimensions of the \(-1\) eigenspace, then \(i+j=r-1\). For a fully filled eigenspace of dimension \(n\), the number of ordered complementary subspaces of dimensions \(i,n-i\) is \({n\brack i}_q q^{i(n-i)}\). For an eigenspace with one missing dimension, the count of ordered disjoint subspaces of dimensions \(i,n-i-1\) is \({n\brack i}_q{n-i\brack1}_q q^{i(n-i-1)}\). Considering the two possible deficient eigenspaces proves that the number of ordered \((Z_1,Z_0)\) is exactly \(T_{n,r-1}\).

For each such pair, lifts \(e+a\) modulo \(Z_1\) and \(e+b\) modulo \(Z_0\) have altogether \(q^{2n+1}\) choices. The resulting two Lie subalgebras have trivial intersection precisely when \(a-b\notin H\). Exactly \(q^{2n}\) pairs have \(a-b\in H\). Hence each ordered pair of invariant parts yields \((q-1)q^{2n}\) projections. This proves the third term and completes the odd-characteristic count.

**5. Characteristic two.** Here \(A=I_V\), so \([ae+v,be+w]=a(be+w)-b(ae+v)=a y-b x\). The bracket of any two elements lies in their linear span. Every vector subspace is therefore a Lie subalgebra. By Step 1 every linear idempotent is Nijenhuis. Choosing its \(r\)-dimensional image gives \({2n+1\brack r}_q\) possibilities, and choosing a complement gives \(q^{r(2n+1-r)}\) possibilities. Exchanging image and kernel proves palindromicity in both characteristics.

**6. Quadratic exponent gap.** For fixed \(q\) let \(D_q=\prod_{j\ge1}(1-q^{-j})>0\). The standard Gaussian bounds are
\[
q^{k(d-k)}\le{d\brack k}_q\le D_q^{-1}q^{k(d-k)}.
\]
It follows that \(S_{n,k}\le(n+1)D_q^{-2}q^{nk-k^2/2}\). In the first odd-characteristic term put \(k=2n-r\); the exponent of its bound is
\[
3nk-\tfrac32k^2+2n-k\le\tfrac32 n^2+2n.
\]
The second term has the same bound with \(k=r-1\). For the third term, one eigenspace has complementary invariant parts and contributes at most \(D_q^{-1}q^{n^2/2}\) for each dimension choice, while the deficient eigenspace contributes at most \(D_q^{-2}q^{(n^2-1)/2}\). There are at most \(2(n+1)\) splits, and the lift factor is \((q-1)q^{2n}\). Summing ranks therefore bounds all odd-characteristic maps by \(q^{3n^2/2+O_q(n)}\). Taking \(r=n\) and retaining the middle summand \({n\brack\lfloor n/2\rfloor}_q{n\brack\lceil n/2\rceil}_q\) in \(S_{n,n}\) supplies the matching lower bound \(q^{3n^2/2+n-O(1)}\). The same argument bounds the double-lift case by \(q^{n^2+O_q(n)}\). For all linear idempotents, the rank formula in Step 5 and the same Gaussian bounds give \(\log_q I_n(q)=2n^2+O_q(n)\). Their difference proves the asserted probability exponent. All constants are for fixed \(q\); no uniformity over fields growing with \(n\) is claimed.

## Verification

Running `python3 verify.py` checks the Gaussian formulas against the torsion identity and tests the subalgebra-pair classification by a second enumeration route. Direct matrix enumeration over prime fields gives the rank tuples (in order from rank zero):
\[
\begin{array}{c|c|c}
(n,q)&\text{rank counts}&\text{method}\\\hline
(1,2)&(1,28,28,1)&\text{torsion matrices}\\
(1,3)&(1,63,63,1)&\text{torsion matrices}\\
(1,5)&(1,275,275,1)&\text{torsion matrices}\\
(2,2)&(1,496,9920,9920,496,1)&\text{subalgebra pairs}\\
(2,3)&(1,2025,35802,35802,2025,1)&\text{subalgebra pairs}
\end{array}
\]
These exhaustive finite checks do not prove formulas for untested \(n\) or extension fields. The proof above handles all prime powers and dimensions independently of computation. The verifier uses no external packages.

## Relationship to prior work

The general notion of Nijenhuis torsion and deformation-theoretic uses are established. Zou, Gao, Kang and Lü (arXiv:2308.12121, first posted 2023-08-23) classify Nijenhuis operators on two-dimensional complex pre-Lie and three-dimensional complex associative algebras, with applications to associated Lie algebras; they do not supply the present finite-field rank polynomial for the infinite two-eigenvalue family. Li, Ma and Wang (arXiv:2310.14267, first posted 2023-10-22) address Nijenhuis operators arising from triangular Leibniz bialgebras, not this enumeration. The 2026 open-access work *Torsion-Free H-Structures on Almost Abelian Solvmanifolds* gives an important broad real-field characterization of product structures on almost-abelian Lie algebras, overlapping the **structural** context of odd-characteristic idempotent Nijenhuis operators via \(2P-I\). Its existence and normal-form statements do not directly provide the finite-field multiplicity polynomial or the characteristic-two jump. The elementary projection-to-subalgebra criterion and Gaussian binomial counts are standard inputs, not asserted as new. The asserted contribution is their explicit two-eigenvalue orbit-free rank enumeration and quantified characteristic fusion.

## Limitations

The result concerns only the stated semidirect family, not arbitrary almost-abelian Lie algebras or general nonidempotent Nijenhuis operators. The asymptotic exponent comparison assumes \(q\) fixed. The even-characteristic count is a straightforward structural degeneration and is not by itself claimed to be a new general theorem. The finite-field enumeration is an exact count of labeled linear maps, not an isomorphism classification. A broader unpublished or unlocated product-structure enumeration could affect publication priority. No independent mathematical audit has been performed.

## References

1. X. Zou, X. Gao, C. Kang and J. Lü, *Nijenhuis Operators on 2D Pre-Lie Algebras and 3D Associative Algebras*, arXiv:2308.12121, first submitted 2023-08-23. https://arxiv.org/abs/2308.12121
2. H. Li, T. Ma and S. Wang, *When Leibniz Algebras Are Nijenhuis?*, arXiv:2310.14267, first submitted 2023-10-22. https://arxiv.org/abs/2310.14267
3. *Torsion-Free H-Structures on Almost Abelian Solvmanifolds*, *Journal of Geometric Analysis* 36 (2026), article 161, published 2026-03-31. https://doi.org/10.1007/s12220-026-02413-0
4. J. Liu, Y. Sheng, Y. Zhou and C. Bai, *Nijenhuis Operators on n-Lie Algebras*, arXiv:1601.02356, submitted 2016-01-11. https://arxiv.org/abs/1601.02356
