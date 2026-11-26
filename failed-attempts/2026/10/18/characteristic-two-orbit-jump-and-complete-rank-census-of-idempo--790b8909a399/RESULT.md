# Characteristic-two orbit jump and complete rank census of idempotent derivations of free two-step Lie algebras

## Finding

Let \(K=\mathbb F_q\), where \(q\) is any prime power, and let \(n\ge2\). For an \(n\)-dimensional vector space \(V\) over \(K\), put
\[
L_n=V\oplus\bigwedge^2 V,\qquad [u,v]=u\wedge v,\qquad [L_n,\bigwedge^2V]=0.
\]
This is the free two-step nilpotent Lie algebra on \(n\) generators. Write \(\mathscr I_n(K)=\{D\in\operatorname{Der}_K(L_n):D^2=D\}\), where the equation is an identity of linear endomorphisms of the entire Lie algebra, not a restricted Lie \(p\)-power condition.

**Orbit and rank census.** The conjugation action of \(\operatorname{Aut}_K(L_n)\) on \(\mathscr I_n(K)\) has one orbit for each admissible \(r=\operatorname{rank}(\overline D: L_n/[L_n,L_n]\to L_n/[L_n,L_n])\). Precisely,
\[
R_p=\begin{cases}\{0,1\},& \operatorname{char}K\ne2,\\
\{0,1,\ldots,n\},&\operatorname{char}K=2.
\end{cases}
\]
For each \(r\in R_p\), set \(s=n-r\) and
\[
h_p(r,s)=\begin{cases}
r\binom{s}{2}+rs^2,&\operatorname{char}K\ne2,\\
r\left(\binom{r}{2}+\binom{s}{2}\right)+rs^2,&\operatorname{char}K=2.
\end{cases}
\]
That orbit consists of exactly
\[
M_{n,q}(r)={n\brack r}_q\,q^{rs+h_p(r,s)}
\]
derivations, every one of full endomorphism rank \(r(s+1)\). Here \({n\brack r}_q=\prod_{i=0}^{r-1}(q^{n-i}-1)/(q^{r-i}-1)\). Thus the **complete** rank enumerator is
\[
\boxed{\mathcal I_{n,q}(T)=\sum_{r\in R_p}M_{n,q}(r)T^{r(n-r+1)}.}
\]
In odd characteristic this reduces to
\[
\boxed{\mathcal I_{n,q}(T)=1+{n\brack1}_q q^{(n-1)(3n-2)/2}T^n.}
\]
In characteristic two, the maximum full rank is \(\lfloor(n+1)^2/4\rfloor\); the entire support is \(\{r(n-r+1):0\le r\le n\}\). Orbit indices can collide at the same full rank. For example, for \(n=3\), \(r=1\) and \(r=3\) both give rank three, but are different automorphism-conjugacy classes. The exact examples are
\[
\mathcal I_{3,2}(T)=1+1408T^3+448T^4,\quad
\mathcal I_{3,3}(T)=1+28431T^3.
\]

## Assumptions and scope

The theorem concerns all finite fields, all integers \(n\ge2\), and *derivations* (not algebra automorphisms, Lie algebra endomorphisms, arbitrary idempotent linear maps, or idempotents in an enveloping algebra). All ranks are ranks as \(K\)-linear operators. The characteristic-two case uses the alternating exterior-product Lie bracket, so it remains a valid Lie algebra despite \(-1=1\). A binomial coefficient with upper argument below two is interpreted as zero. No assumption of algebraic closure is made.

## Proof

**1. Exhaustive parametrization.** The commutator ideal \([L_n,L_n]=\bigwedge^2V\) is characteristic. Every derivation has a unique block matrix with respect to the fixed direct sum:
\[
D_{A,f}=\begin{pmatrix}A&0\\ f&\rho(A)\end{pmatrix},\qquad
A\in\operatorname{End}(V),\quad f\in\operatorname{Hom}(V,\bigwedge^2V),
\]
where \(\rho(A)(u\wedge v)=Au\wedge v+u\wedge Av\). The formula follows by applying the Leibniz rule to every bracket of two elements of \(V\). Conversely any \(A,f\) with this formula defines a derivation, since central brackets give no further constraints. In particular, no block parameter is omitted.

**2. Idempotence and characteristic boundary.** Direct block multiplication gives precisely the three simultaneous requirements
\[
A^2=A,\qquad \rho(A)^2=\rho(A),\qquad fA+\rho(A)f=f.
\]
Write \(V=U\oplus W\), where \(U=\operatorname{im}A\), \(W=\ker A\), \(r=\dim U\) and \(s=\dim W\). The restriction of \(\rho(A)\) has eigenvalue \(2\) on \(\bigwedge^2U\), \(1\) on \(U\wedge W\), and \(0\) on \(\bigwedge^2W\). Over a field of odd characteristic, \(2\) is not idempotent; since \(\bigwedge^2U=0\) exactly for \(r\le1\), the only admissible ranks of \(A\) are zero and one. In characteristic two, all three eigenvalues are in \(\{0,1\}\), allowing every \(0\le r\le n\).

**3. All central parameters and their dimension.** Let \(B=\rho(A)\), which is idempotent in each admissible case. On inputs \(u\in U\) the equation \(fA+Bf=f\) becomes \(Bf(u)=0\); on inputs \(w\in W\) it becomes \(Bf(w)=f(w)\). Thus
\[
f(U)\subseteq\ker B,\qquad f(W)\subseteq\operatorname{im}B.
\]
The image of \(B\) is \(U\wedge W\) of dimension \(rs\) in every case. Its kernel has dimension \(\binom s2\) when the characteristic is odd (only \(r\le1\)), and \(\binom r2+\binom s2\) in characteristic two. Hence the space of admissible \(f\) is a vector space of dimension \(h_p(r,s)\), and has exactly \(q^{h_p(r,s)}\) elements.

**4. Conjugacy, not merely a cardinality count.** For every linear map \(h:V\to\bigwedge^2V\), the central shear \(S_h=\begin{pmatrix}I&0\\h&I\end{pmatrix}\) is a Lie algebra automorphism. A direct multiplication yields
\[
S_hD_{A,f}S_h^{-1}
= D_{A,\,f+hA-Bh}.
\]
Taking \(h|_U=-f|_U\) and \(h|_W=f|_W\) sends any admissible \(f\) to zero, because \(Bf(U)=0\) and \(Bf(W)=f(W)\). Conversely, any two rank-\(r\) projections \(A\) on \(V\) are conjugate by \(\operatorname{GL}(V)\), and the natural action of \(\operatorname{GL}(V)\) on \(L_n\) intertwines their induced exterior-square actions. Therefore all idempotent derivations with the same \(r\) are conjugate. Automorphism conjugacy preserves the induced map on \(L_n/[L_n,L_n]\), so distinct values of \(r\) cannot be conjugate.

**5. Counting and full ranks.** An ordered pair \((U,W)\) with \(V=U\oplus W\), \(\dim U=r\), determines exactly one rank-\(r\) idempotent \(A\). There are \({n\brack r}_q\) choices of \(U\), and then \(q^{rs}\) complements \(W\). For each \(A\) there are \(q^{h_p(r,s)}\) valid \(f\), giving the formula for \(M_{n,q}(r)\). Step 4 shows that \(D_{A,f}\) is conjugate to \(\operatorname{diag}(A,B)\), and therefore its full rank equals \(r+rs=r(s+1)\). This proves all coefficients and every support assertion: each rank listed occurs since its count is positive, and all idempotents have been enumerated. The maximum characteristic-two rank follows by maximizing the concave integer quadratic \(r(n+1-r)\) over \(0\le r\le n\). For odd characteristic, the single nonzero index \(r=1\) has exponent \(s+h_p(1,s)=s+\binom{s}{2}+s^2=(n-1)(3n-2)/2\), proving the displayed closed form.

## Verification

The standalone programs `verify_idempotent.cpp` and `verify_gf4.py` construct the full derivation matrices independently of the proof's orbit counting. The C++ program exhausts all possible \(A,f\) for \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3)\), comparing the rank histogram after direct matrix multiplication with the closed formula. It reports `VERIFY_OK_IDEMPOTENT_FREE_CLASS2`. The separately implemented Python program enumerates all \(4^6\) candidate coefficient arrays for \(n=2\) over the genuine field \(\mathbb F_4\) and reports `VERIFY_OK_IDEMPOTENT_FREE_CLASS2_GF4`. The computations are finite tests, not proof of the assertion for arbitrary \(n,q\); the proof above is uniform.

## Relationship to prior work

Burde and Moens (arXiv:1108.3548v1, 2011) study finite-order **nonsingular** derivations of complex Lie algebras, including the two-step setting. Their periodicity results do not classify singular idempotent derivations, and do not imply the finite-field orbit sizes or the characteristic-two jump. Benito and de-la-Concepción (2014, Proposition 2.3) describe the general extension of generator maps to derivations of free nilpotent Lie algebras in characteristic zero; our Step 1 specializes this general structural mechanism but Steps 2–5 impose and solve a new quadratic projection condition over every characteristic. Benito and Roldán-López (arXiv:1911.01897v2, 2019) likewise describe derivations and automorphisms in characteristic zero, not these idempotent-orbit and rank counts. Krutov and Lebedev (arXiv:1711.00638v1, 2017) relate characteristic-two idempotent derivations to gradings modulo two in the setting of simple Lie algebras; in the present free nilpotent family, these gradings are classified and enumerated explicitly. None of the examined statements gives the four-parameter \((n,q,r,\operatorname{char}K)\) orbit-size formula above. An undiscovered equivalent treatment under grading or modular-nilpotent terminology cannot be ruled out.

## Limitations

This is not a general classification for all two-step nilpotent Lie algebras or higher nilpotency classes. In characteristic two, a rank-\(r\) generator projection may induce the same full operator rank as a different index \(r\), so the rank enumerator alone does not recover the conjugacy orbit. The uniqueness assertion concerns actual \(K\)-rational automorphism conjugacy, not an independent publication-priority determination. There is no independent mathematical audit; the argument and supporting finite checks are presented for direct scrutiny.

## References

1. D. Burde and W. Moens, *Periodic derivations and prederivations of Lie algebras*, arXiv:1108.3548v1 (first posted 2011-08-17), https://arxiv.org/abs/1108.3548.
2. P. Benito and D. de-la-Concepción, *An overview of free nilpotent Lie algebras*, Comment. Math. Univ. Carol. 55 (2014), 325–339, Proposition 2.3; open text https://investigacion.unirioja.es/documentos/5bbc696ab750603269e81ac8/f/617a4e5f2bb80f973acc38e7.pdf.
3. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotiens*, arXiv:1911.01897v2 (2019), https://arxiv.org/abs/1911.01897.
4. A. Krutov and A. Lebedev, *On Gradings Modulo 2 of Simple Lie Algebras in Characteristic 2*, arXiv:1711.00638 (2017), https://arxiv.org/abs/1711.00638.
