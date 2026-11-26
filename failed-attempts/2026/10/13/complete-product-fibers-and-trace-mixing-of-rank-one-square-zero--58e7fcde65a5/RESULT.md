# Complete product fibers and trace mixing of rank-one square-zero matrices

## Finding
Let \(q\) be any prime power, \(n\ge2\), and \(r\ge1\). Write \(V=\mathbb F_q^n\) and
\[\mathcal N_{n,q}=\{X\in\operatorname{End}(V):\operatorname{rank}X=1,\ X^2=0\}.\]
For a prescribed \(B\in\operatorname{End}(V)\), let
\[F_r(B)=\#\{(X_1,\ldots,X_r)\in\mathcal N_{n,q}^r:X_1\cdots X_r=B\}.\]
Put
\[
D=q^n-1,\qquad H=q^{n-1},\qquad J=q^{n-2},\qquad
C=\frac{D(H-1)}{q-1},\qquad
\lambda=H(H-1),\qquad \mu=-(q-1)J.
\]
The **complete prescribed-product distribution**, valid uniformly in all finite characteristics and extensions, is
\[
\boxed{F_r(B)=\begin{cases}
C^r-C\lambda^{r-1},&B=0,\\[2mm]
\dfrac{(H-1)\lambda^{r-1}+H(q-1)\mu^{r-1}}{D},
&\operatorname{rank}B=1,\ \operatorname{tr}B=0,\\[3mm]
\dfrac{(H-1)(\lambda^{r-1}-\mu^{r-1})}{D},
&\operatorname{rank}B=1,\ \operatorname{tr}B\ne0,\\[3mm]
0,&\operatorname{rank}B\ge2.
\end{cases}}
\]
Both nonzero-target formulas are integer counts despite their displayed quotients. In particular, if \(n=2\), a product of exactly two such factors can never equal a nonzero rank-one nilpotent matrix, although every rank-one matrix is a product of three such factors. For \(n\ge3\), already two factors realize every rank-one target.

There are exactly \(C\) factors in \(\mathcal N_{n,q}\). Under independent uniform sampling of factors,
\[
\Pr(X_1\cdots X_r\ne0)=\left(\frac{\lambda}{C}\right)^{r-1}
=\left(\frac{q^{n-1}(q-1)}{q^n-1}\right)^{r-1}.
\]
Let \(U\) be the uniform law on all nonzero rank-one matrices, and let \(P_r\) be the product law conditional on a nonzero product. Its exact total-variation distance is
\[
\boxed{\|P_r-U\|_{\mathrm{TV}}=
\frac{q^{n-1}(q-1)}{q^n-1}
\left(\frac{q-1}{q(q^{n-1}-1)}\right)^{r-1}.}
\]
Thus conditioning on nonvanishing leads to uniform rank-one products at an explicit geometric rate. The trace-zero versus nonzero-trace deviation alternates sign with word length because \(\mu<0\).

## Assumptions and scope
Every factor is **nonzero, rank one, and square zero**, not an arbitrary nilpotent or an arbitrary square-zero operator. Products are ordered; a factor may repeat. Trace, rank, and dimensions are over \(\mathbb F_q\). The formula includes the boundary \(r=1\), characteristic two, and all nonprime finite fields. The case \(B=0\) is separate from nonzero rank-one targets, even though its trace is zero. The distance formula uses the usual half-\(\ell^1\) total-variation normalization on the finite set of nonzero rank-one matrices.

## Proof
**1. Count factors and normalize rank-one operators.** Any nonzero rank-one operator can be written as \(u\varphi\) with \(u\in V\setminus\{0\}\) and \(\varphi\in V^*\setminus\{0\}\), uniquely up to \((u,\varphi)\mapsto(cu,c^{-1}\varphi)\) for \(c\in\mathbb F_q^\times\). It obeys \((u\varphi)^2=\varphi(u)u\varphi\) and \(\operatorname{tr}(u\varphi)=\varphi(u)\). For each nonzero \(u\), there are \(H-1=q^{n-1}-1\) nonzero forms annihilating it. Consequently \(|\mathcal N_{n,q}|=D(H-1)/(q-1)=C\). Every product of the factors has rank at most one, and the initial fibers obey \(F_1(B)=1\) for nonzero rank-one traceless \(B\), and \(F_1(B)=0\) otherwise.

**2. A two-stratum transition.** The number of length-\(r\) products yielding any fixed nonzero rank-one \(B\) depends only on whether \(\operatorname{tr}B\) vanishes. Indeed, similarity changes \(B\) within a fixed nonzero-trace similarity class; multiplying a single factor by a nonzero scalar changes the product by that scalar and preserves the factor set, thereby identifying all nonzero trace values. All nonzero rank-one traceless targets form one similarity class. Denote the respective fibers by \(f_r^0\) and \(f_r^1\).

Fix a nonzero rank-one target \(B=u\beta\) with nonzero column \(u\) and nonzero row \(\beta\). Every decomposition \(XZ=B\) with \(X\in\mathcal N_{n,q}\) and nonzero rank-one \(Z\) is uniquely of the form
\[X=u\varphi,\qquad Z=v\beta,\qquad \varphi(u)=0,\quad \varphi(v)=1.\]
Conversely these equations always produce an admissible decomposition. Separate the choices by \(\beta(v)=0\) or \(\beta(v)\ne0\), the trace class of \(Z\). If \(\beta(u)\ne0\), the nonzero \(\varphi\) in the annihilator of \(u\) is linearly independent of \(\beta\); there are \(H-1\) choices for \(\varphi\), and \(J=q^{n-2}\) vectors \(v\) with \(\varphi(v)=1\) and \(\beta(v)=0\), or \((q-1)J\) with \(\beta(v)\ne0\).

If instead \(\beta(u)=0\), there are \(q-1\) nonzero functionals \(\varphi\) proportional to \(\beta\), each giving \(H\) vectors \(v\) with \(\varphi(v)=1\), necessarily with \(\beta(v)\ne0\). The other \(H-q\) functionals in the annihilator of \(u\) are independent of \(\beta\) and each yield \(J\) vectors of trace zero and \((q-1)J\) of nonzero trace. Therefore
\[
\begin{pmatrix}f_{r+1}^0\\ f_{r+1}^1\end{pmatrix}=
K\begin{pmatrix}f_r^0\\ f_r^1\end{pmatrix},\qquad
K=\begin{pmatrix}
H(J-1)&(q-1)HJ\\
J(H-1)&(q-1)J(H-1)
\end{pmatrix},\qquad
\begin{pmatrix}f_1^0\\ f_1^1\end{pmatrix}=\begin{pmatrix}1\\0\end{pmatrix}.
\]

**3. Diagonalize without assumptions on characteristic.** Over the ordinary rational number field (since the matrix \(K\) consists of integer counts), the vectors
\[v_+=(1,1)^{\mathsf T},\qquad v_-=(H(q-1),-(H-1))^{\mathsf T}\]
are eigenvectors with eigenvalues \(\lambda=H(H-1)\) and \(\mu=-(q-1)J\), respectively. Also
\[(1,0)^{\mathsf T}=\frac{H-1}{D}v_++\frac1D v_-\]
because \(qH-1=D\). Applying \(K^{r-1}\) proves exactly the two rank-one formulas in the box. There is no hidden exceptional case: \(D>0\), \(H>1\), and \(|\mu|<\lambda\) whenever \(n\ge2\) and \(q\ge2\).

**4. Recover the zero fiber.** Fix any nonzero rank-one partial product \(u\beta\). It remains nonzero after right multiplication by \(X=v\varphi\in\mathcal N_{n,q}\) exactly when \(\beta(v)\ne0\). There are \((q-1)H\) possible nonzero columns \(v\) with this property and \(H-1\) nonzero annihilating forms \(\varphi\) for each; dividing by \(q-1\) for the scalar ambiguity leaves precisely \(\lambda=H(H-1)\) admissible matrices \(X\), independently of the partial product. Exactly \(C\lambda^{r-1}\) ordered words have nonzero product, out of \(C^r\) words in total. This gives the zero formula and the survival probability.

**5. Exact mixing distance.** There are \(C\) nonzero rank-one traceless matrices and \(DH\) nonzero rank-one matrices with nonzero trace; their sum is \(D^2/(q-1)\). Conditional on a nonzero product, the limiting uniform per-target mass is \((q-1)/D^2\), since \((H-1)/(DC)=(q-1)/D^2\). The deviations of the two trace classes from this mass are, respectively,
\[\frac{H(q-1)\mu^{r-1}}{DC\lambda^{r-1}},\qquad
-\frac{(H-1)\mu^{r-1}}{DC\lambda^{r-1}}.\]
Multiplying their absolute values by the sizes of the two classes and taking half the sum yields
\[\|P_r-U\|_{\mathrm{TV}}=\frac{H(q-1)}{D}\left|\frac{\mu}{\lambda}\right|^{r-1},\]
which is the displayed closed form. The factor \(\mu^{r-1}\) establishes alternating trace bias.

**6. Support boundary.** At length two the trace-zero and nonzero-trace fibers are respectively \(H(J-1)\) and \(J(H-1)\), directly from the transition matrix. Thus the former vanishes precisely for \(n=2\), while the latter is always positive. For \(n=2\), the matrix \(K\) has strictly positive off-diagonal entries and positive lower-right entry, so both classes have positive length-three fibers; inserting additional factors preserves positivity at larger lengths. For \(n\ge3\), both length-two fibers are positive. This completes the stated support classification.

## Verification
The standalone Python 3 program `verify.py` independently constructs all nonzero rank-one square-zero matrices as vector dyads, forms the complete product distribution by iterated matrix multiplication, and compares the count of **every zero or rank-one target** to the formula. It also checks that no target of rank greater than one occurs. The program covers \((q,n)=(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(4,3),(2,4)\) at lengths from one to three, four, or five as indicated by the program output. The order-four field uses the irreducible relation \(z^2+z+1=0\), so it tests a nonprime field. Execution of `python3 verify.py` reports `VERIFY_OK`. These are finite corroborations only; the preceding proof supplies the all-field, all-dimension, all-length argument.

## Relationship to prior work
The existence theory for products of nilpotent or square-zero matrices investigates which matrices admit some factorization and permissible factor ranks; see Sullivan (2008), Mohammadian (2012), and Botha (2016), and the full-text synthesis by Hattingh (2018, especially Chapter 4). Kokol Bukovšek, Košir, Novak, and Oblak (2007) classify products of *commuting* square-zero or nilpotent operators, a genuinely different constraint: a product of commuting nilpotent matrices is nilpotent, whereas the present unrestricted products can have nonzero trace. The formula here counts every ordered factorization into the minimal nonzero nilpotent orbit and gives an exact finite-field mixing law. Neither an existence criterion nor a commuting-factor theorem yields these frequencies without a new count. Counts for products of rank-one **idempotents** concern a distinct factor orbit with trace one and a different spectral transition; they do not imply the displayed nilpotent-orbit law by a parameter substitution.

## Limitations
This theorem treats products exclusively of nonzero rank-one square-zero factors; it does not count products of all square-zero matrices of higher ranks, additive decompositions, or factorizations with commuting factors. It counts matrix tuples, not their equivalence classes under simultaneous conjugation. Searches of available published literature did not establish priority beyond the inspected material; potentially relevant paywalled factorization articles could not be read in full. Neither this finite verification program nor the present review constitutes an independent audit.

## References
1. R. P. Sullivan, “Products of nilpotent matrices,” *Linear and Multilinear Algebra* **56** (2008), 311–317. DOI: 10.1080/03081080701269548. Published online 2008-05-09.
2. A. Mohammadian, “Sums and Products of Square-Zero Matrices,” *Communications in Algebra* **40** (2012), 4568–4574. DOI: 10.1080/00927872.2011.613423.
3. J. D. Botha, “Products of idempotent and square-zero matrices,” *Linear Algebra and Its Applications* **497** (2016), 116–133. DOI: 10.1016/j.laa.2016.02.026.
4. D. Kokol Bukovšek, T. Košir, N. Novak, and P. Oblak, “Products of commuting nilpotent operators,” *Electronic Journal of Linear Algebra* **16** (2007), 237–247. DOI: 10.13001/1081-3810.1199. Full text: https://journals.uwyo.edu/index.php/ela/article/download/455/455/455.
5. C. J. Hattingh, *Sums and Products of Square-Zero Matrices*, MSc thesis, 2018, arXiv:1804.02140, especially Chapter 4, https://arxiv.org/pdf/1804.02140.
