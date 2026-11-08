# Exact retraction-rank spectrum and two-point concentration in free class-two Lie algebras

## Finding

Fix a prime power \(q\) and an integer \(n\ge2\). Let \(V=\mathbb F_q^n\) and let \(L_n=V\oplus\bigwedge^2 V\), with Lie bracket \([v,w]=v\wedge w\) for \(v,w\in V\) and the exterior-square summand central. This is the free nilpotent Lie algebra of class two on \(n\) generators, also in characteristic two.

For \(0\le r\le n\), let \(N_{n,r}(q)\) count Lie algebra endomorphisms \(P:L_n\to L_n\) with \(P^2=P\) and induced rank \(r\) on \(L_n/[L_n,L_n]\cong V\). Then

\[
\boxed{N_{n,r}(q)={n\brack r}_q\,q^{r(n-r)+r(\binom n2-\binom r2)+(n-r)\binom r2}.}
\]

Here \({n\brack r}_q=\prod_{j=1}^r(q^{n-r+j}-1)/(q^j-1)\) is a Gaussian binomial coefficient. Every such idempotent has image dimension \(r+\binom r2\), and every two idempotents with the same \(r\) are conjugate by \(\operatorname{Aut}(L_n)\). No other image ranks occur.

For fixed \(q\), choose an idempotent uniformly from all \(\sum_{r=0}^nN_{n,r}(q)\) possibilities and let \(R_n\) be its induced rank on \(V\). Set

\[
\tau_n=\frac{n-2+\sqrt{7n^2+8n+4}}6,\qquad
\alpha=\frac{1+\sqrt7}{6}.
\]

Then the **two-point concentration theorem** states

\[
\Pr\bigl(R_n\in\{\lfloor\tau_n\rfloor,\lceil\tau_n\rceil\}\bigr)
=1-O_q\bigl(nq^{-\sqrt7 n/2}\bigr).
\]

In particular, \(R_n/n\to\alpha\) in probability, while the ratio of image dimension to ambient dimension converges in probability to

\[
\alpha^2=\frac{4+\sqrt7}{18}.
\]

Finally, with \(N_n(q)=\sum_rN_{n,r}(q)\),

\[
\lim_{n\to\infty}\frac{\log_qN_n(q)}{n^3}
=\frac{10+7\sqrt7}{108}.
\]

The concentration is substantially sharper than a central-limit window: the random rank lies on at most two adjacent integers with exponentially small error.

## Assumptions and scope

All maps are \(\mathbb F_q\)-linear **Lie algebra homomorphisms**; they are not arbitrary idempotent linear maps. The integer \(n\ge2\) varies, and \(q\) remains fixed in the asymptotic statements. The endomorphism rank \(r\) always refers to the induced transformation on the abelianization \(V\), whereas the full image has dimension \(r+\binom r2\). In characteristic two, the bracket is alternating because the exterior product satisfies \(v\wedge v=0\); none of the arguments divides by two.

## Proof

**1. Normal form.** Because \([L_n,L_n]=\bigwedge^2V\), every Lie homomorphism preserves the exterior-square summand. Its restriction to \(V\), followed by projection onto \(V\), is some \(A\in\operatorname{End}(V)\); its remaining component is a map \(B:V\to\bigwedge^2V\). Bracket preservation forces its action on \(\bigwedge^2V\) to equal \(\bigwedge^2A\). Conversely, every pair \((A,B)\) defines a homomorphism

\[
P_{A,B}(v,z)=(Av,\ Bv+(\bigwedge^2 A)z).
\]

Direct composition gives the necessary and sufficient idempotency equations

\[
A^2=A,\qquad BA+(\bigwedge^2A)B=B.
\]

**2. Allowed central components.** An idempotent \(A\) splits \(V=U\oplus W\), where \(U=\operatorname{im}A\), \(W=\ker A\) and \(\dim U=r\). The operator \(\bigwedge^2A\) projects \(\bigwedge^2V\) onto \(\bigwedge^2U\), with kernel \((U\wedge W)\oplus\bigwedge^2W\). Applying the second idempotency equation separately to \(U\) and \(W\) yields exactly

\[
B(U)\subseteq\ker(\bigwedge^2A),\qquad
B(W)\subseteq\operatorname{im}(\bigwedge^2A).
\]

These two conditions are independent and provide an affine vector space of choices of dimension

\[
h(n,r)=r\left(\binom n2-\binom r2\right)+(n-r)\binom r2.
\]

The restriction of \(P_{A,B}\) to the central summand has rank \(\binom r2\), while its induced abelianization has rank \(r\); hence the full image dimension is \(r+\binom r2\).

**3. One automorphism orbit for every rank.** Every invertible \(G:V\to V\) induces an automorphism \((v,z)\mapsto(Gv,(\bigwedge^2G)z)\). Consequently we may conjugate \(A\) to the standard projection onto the first \(r\) coordinates. For a fixed \(A\), any \(C:V\to\bigwedge^2V\) determines a central-shear automorphism \(S_C(v,z)=(v,z+Cv)\). Conjugating the standard lift \(P_{A,0}\) gives the central component \(CA-(\bigwedge^2A)C\). Given any permissible \(B\), choose \(C|_U=B|_U\) and \(C|_W=-B|_W\). The conditions in Step 2 ensure

\[
CA-(\bigwedge^2A)C=B.
\]

Therefore every idempotent with abelianized rank \(r\) is automorphism-conjugate to \((v,z)\mapsto(Av,(\bigwedge^2A)z)\), where \(A\) is the standard rank-\(r\) projection. Different ranks cannot be conjugate.

**4. Enumeration.** The number of rank-\(r\) idempotent linear maps on \(V\) is \({n\brack r}_q q^{r(n-r)}\): select the image subspace and one of its \(q^{r(n-r)}\) complementary kernels. Each admits exactly \(q^{h(n,r)}\) choices for \(B\), by Step 2. Multiplication proves the claimed exact formula. In particular, \(r=0\) and \(r=n\) give respectively the zero map and the identity map.

**5. Concentration.** The Gaussian factor can be written

\[
{n\brack r}_q=q^{r(n-r)}G_{n,r}(q),\qquad
1\le G_{n,r}(q)\le D_q^{-1},\quad
D_q=\prod_{j\ge1}(1-q^{-j})>0.
\]

Thus \(N_{n,r}(q)=q^{E_n(r)}G_{n,r}(q)\), where the real polynomial

\[
E_n(x)=\tfrac12n^2x+\tfrac12nx^2+nx-x^3-x^2
\]

has derivative \(E'_n(x)=n^2/2+nx+n-3x^2-2x\), positive from \(0\) up to the unique positive critical point \(\tau_n\) and negative thereafter. Put \(\Delta_n=\sqrt{7n^2+8n+4}\). Exactly,

\[
E_n(\tau_n+s)=E_n(\tau_n)-\tfrac12\Delta_n s^2-s^3.
\]

Let \(k=\lfloor\tau_n\rfloor\), \(\ell=\lceil\tau_n\rceil\). Writing \(d=\tau_n-k\in[0,1)\), the Taylor identity gives

\[
E_n(k)-E_n(k-1)\ge\Delta_n/2-7,
\qquad
E_n(\ell)-E_n(\ell+1)\ge\Delta_n/2+1,
\]

whenever the adjacent ranks are in \([0,n]\). Since \(E_n\) rises to \(\tau_n\) and then falls, every integer outside \(\{k,\ell\}\) has exponent at least \(\Delta_n/2-7\) lower than \(\max(E_n(k),E_n(\ell))\). Consequently

\[
\Pr(R_n\notin\{k,\ell\})
\le(n+1)D_q^{-1}q^{7-\Delta_n/2}
\le(n+1)D_q^{-1}q^{7-\sqrt7n/2}.
\]

This proves the two-point assertion. Since \(\tau_n/n\to\alpha\) and the image dimension is \(R_n(R_n+1)/2\), both probabilistic limits follow.

**6. Total logarithmic growth.** Uniformly over \(0\le r\le n\),

\[
E_n(r)=n^3f(r/n)+O(n^2),\qquad f(x)=x/2+x^2/2-x^3.
\]

The maximum of \(f\) on \([0,1]\) occurs at \(\alpha=(1+\sqrt7)/6\) with \(f(\alpha)=(10+7\sqrt7)/108\). Since \(1\le G_{n,r}(q)\le D_q^{-1}\) and there are \(n+1\) summands, squeezing the sum between its largest exponential term and \((n+1)D_q^{-1}\) times that term proves the logarithmic limit.

## Verification

Execute `python3 verify.py` using Python 3 and only its standard library. The independent enumerator constructs all candidate homomorphisms by their images on the generating basis, forms their full linear matrices including the exterior-square action, composes those matrices, and checks idempotency and image rank without using the counting formula. It exhausts \((n,q)=(2,2),(2,3),(3,2)\), returning respectively the full image-rank histograms \((1,12,1)\), \((1,36,1)\), and \((1,224,896,1)\) at the allowed image ranks. A separate exhaustive central-shear calculation checks the conjugation normal form for all admissible maps in \((n,q)=(3,2)\). A second arithmetic module checks the exact Gaussian formula and two-point concentration numerically for several larger \(n\) and \(q=2,3\). The run terminates with `VERIFY_OK`.

Finite enumeration is a check of boundary cases, not a proof of the all-dimension or asymptotic statements. Those follow from Steps 1–6.

## Relationship to prior work

The exterior-square description of the free class-two Lie algebra, its universal mapping property, and the general shape of its automorphisms are established prior mathematics. Cagliero–Gutiérrez Frez–Szechtman (2017) use the same Lie algebra for uniserial representation theory. Benito–Roldán-López (2019) explicitly describe homomorphism extensions and automorphism structure of free nilpotent Lie algebras. Ruan–Sheng–Zhang (2017) realize a free two-step nilpotent Lie algebra using Hall-Lie constructions for oriented paths. None of these structural facts is claimed as new.

The new claim assessed here is their specialization to an exact all-rank **idempotent Lie-homomorphism** census, the single-conjugacy-orbit classification, and the sharp exponentially accurate two-neighbor concentration with its irrational limiting rank fraction. The \(n=2\) Heisenberg specialization and elementary Gaussian counts of linear projections are not separately claimed as novel.

## Limitations

The theorem applies only to the free two-step nilpotent Lie algebra, not arbitrary two-step quotients or higher nilpotency classes. The asymptotic fixes \(q\) and takes \(n\to\infty\); it does not assert estimates uniform in growing field size. The stated two-point law does not specify the relative probability assigned to each of the two adjacent ranks. The mathematical derivation is self-contained, but the literature comparison is not a certification of global publication priority.

## References

1. L. Cagliero, L. Gutiérrez Frez, F. Szechtman, *Free 2-step nilpotent Lie algebras and indecomposable representations*, arXiv:1703.06214v1, first public 2017-03-17; https://arxiv.org/html/1703.06214v1.
2. P. Benito, J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897v1, first public 2019-11-05; https://arxiv.org/html/1911.01897v2.
3. S. Ruan, J. Sheng, H. Zhang, *Lie algebras arising from 1-cyclic perfect complexes*, arXiv:1705.07307v1, first public 2017-05-20; https://arxiv.org/abs/1705.07307.
