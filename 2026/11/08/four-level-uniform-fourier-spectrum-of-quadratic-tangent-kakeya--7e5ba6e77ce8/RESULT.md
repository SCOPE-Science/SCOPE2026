# Four-level uniform Fourier spectrum of quadratic-tangent Kakeya sets over odd-degree ternary fields

## Finding
Let \(m\ge3\) be odd, \(q=3^m\), and \(F=\mathbb F_q\). Put
\[
K=\{(x,tx-t^2):x,t\in F\}\cup\{(0,y):y\in F\},
\qquad \mu=|K|^{-1}\mathbf1_K.
\]
This is a Kakeya set in \(F^2\), with \(|K|=(q^2+2q-1)/2\). For the unnormalized Fourier transform
\[
\widehat{\mathbf1_K}(a,b)=\sum_{(x,y)\in K}\psi(-ax-by),
\quad \psi(z)=\exp(2\pi i\operatorname{Tr}_{F/\mathbb F_3}(z)/3),
\]
the complete nonzero-frequency squared-modulus spectrum is

| \(|\widehat{\mathbf1_K}(a,b)|^2\) | Number of nonzero frequencies |
|:--|--:|
| \( (q-1)^2/4 \) | \(q-1\) |
| \( (q+1)^2/4 \) | \(q(q-1)/3\) |
| \( (q+1)(q+1-\sqrt{3q})/4 \) | \((q-1)(q/3+3^{(m-1)/2})\) |
| \( (q+1)(q+1+\sqrt{3q})/4 \) | \((q-1)(q/3-3^{(m-1)/2})\) |

All four levels are distinct and strictly positive for every admissible \(m\). In particular, no Fourier coefficient vanishes. The **sharp uniform-probability Fourier bias** is
\[
\boxed{\max_{(a,b)\ne(0,0)}|\widehat\mu(a,b)|=
\frac{\sqrt{(q+1)(q+1+\sqrt{3q})}}{q^2+2q-1}},
\]
with exactly \((q-1)(q/3-3^{(m-1)/2})\) maximizing frequencies. This bias is \((1+O(q^{-1/2}))/q\), where the asymptotic is along odd degrees \(m\to\infty\).

## Assumptions and scope
The characteristic is precisely three, the field extension degree is odd and at least three, all points of \(K\) have equal positive mass, and Fourier frequencies are identified with \(F^2\) using the coordinate dot product. The trace character displayed above is fixed; replacing it by any nontrivial additive character merely permutes nonzero frequencies, preserving the distribution. The lines \(y=tx-t^2\) for \(t\in F\), and the line \(x=0\), exhibit all \(q+1\) projective line directions.

## Proof
Write \(\chi:F\to\{-1,0,1\}\) for the quadratic multiplicative character. The union of nonvertical lines is exactly
\[
U=\{(x,y):\chi(x^2-4y)\ge0\},\qquad
\mathbf1_U(x,y)=\tfrac12\bigl[1+\chi(x^2-4y)+\mathbf1_{\{x^2-4y=0\}}\bigr].
\]
Indeed, \(y=tx-t^2\) is equivalent to \(t^2-xt+y=0\). At \(x=0\), the missing vertical-line points constitute
\[
V=K\setminus U=\{(0,y):\chi(-4y)=-1\},\qquad |V|=(q-1)/2.
\]
For each \(x\) there are \((q+1)/2\) points in \(U\); hence \(|K|=q(q+1)/2+(q-1)/2\).

Set \(G=\sum_{u\in F}\chi(u)\psi(u)\). The elementary quadratic Gauss identities are
\[
\sum_u\chi(u)\psi(cu)=\chi(c)G\quad(c\ne0),\quad
\sum_x\psi(cx^2+dx)=\chi(c)G\psi(-d^2/(4c))\quad(c\ne0),
\]
and \(|G|^2=q\), \(\overline G=\chi(-1)G\). Since \(q=3^m\equiv3\pmod4\), \(\chi(-1)=-1\), and consequently \(G=\kappa i\sqrt q\) for an unspecified sign \(\kappa\in\{\pm1\}\). These identities follow from counting solutions of \(x^2=u\) and additive-character orthogonality; they require no sign convention for the Gauss sum.

For \(b\ne0\), substitute \(u=x^2-4y\) into the three terms in \(\mathbf1_U\). The constant term vanishes, the quadratic-character term gives \(q\psi(a^2/b)\), and the discriminant-zero term gives \(\chi(-b)G\psi(a^2/b)\). The Fourier transform of \(\mathbf1_V\) is \(-(1+\chi(b)G)/2\). Thus the exact full complex Fourier formula is
\[
\boxed{\widehat{\mathbf1_K}(a,b)=\tfrac12\Big[(q+\chi(-b)G)\psi(a^2/b)-(1+\chi(b)G)\Big]},\qquad b\ne0.
\]
For \(b=0,a\ne0\), only \(V\) contributes, giving \((q-1)/2\). At the origin the transform equals \(|K|\). For \(a=0,b\ne0\), the displayed formula becomes \((q-1-2\chi(b)G)/2\), of squared modulus \((q+1)^2/4\).

For \(a,b\ne0\) let \(z=a^2/b\), so \(\chi(b)=\chi(z)\). Direct multiplication, using \(G=\kappa i\sqrt q\), yields
\[
4|\widehat{\mathbf1_K}(a,b)|^2=(q+1)\Bigl(q+1-2\kappa\chi(z)\sqrt q\,\sin(2\pi\operatorname{Tr}(z)/3)\Bigr).
\]
If \(\operatorname{Tr}(z)=0\), this is the second level. Otherwise \(\sin(2\pi\operatorname{Tr}(z)/3)=\pm\sqrt3/2\), producing the third or fourth level.

To count these frequencies, set \(S_j=\sum_{\operatorname{Tr}(z)=j}\chi(z)\) for \(j\in\mathbb F_3\). Trace-fiber orthogonality, \(\chi(2)=-1\), and \(G=\kappa i\sqrt q\) imply
\[
S_0=0,\qquad S_1=\kappa\,3^{(m-1)/2},\qquad S_2=-\kappa\,3^{(m-1)/2}.
\]
Indeed \(S_j=G(\exp(-2\pi i j/3)-\exp(-4\pi i j/3))/3\). Each trace fiber has cardinality \(q/3\), and \(0\) lies in the zero fiber. Consequently there are \(q/3+3^{(m-1)/2}\) nonzero \(z\) giving the lower noncentral level, and \(q/3-3^{(m-1)/2}\) giving the upper level. Each such \(z\) arises from precisely \(q-1\) pairs \((a,b)\) with both coordinates nonzero, by choosing \(a\in F^\times\) and setting \(b=a^2/z\). The trace-zero nonzero values and \(a=0,b\ne0\) together give \((q-1)(q/3-1)+(q-1)=q(q-1)/3\) instances of the second level. The remaining \(q-1\) frequencies have \(b=0,a\ne0\). The multiplicities sum to \(q^2-1\), as required.

For \(m\ge3\), \(q/3-3^{(m-1)/2}>0\) and \(q+1>\sqrt{3q}\). Hence all four eigenlevels occur and are positive; the largest is the plus level. Dividing its square root by \(|K|\) proves the exact uniform bias and its maximizing multiplicity. This completes the proof.

## Verification
`CHECK.py` is a standalone Python 3 program using no additional packages. Run `python3 CHECK.py`. It constructs prime fields of orders 3, 5, and 7 and the degree-three extension field of order 27 using a fixed irreducible cubic, builds the union of Kakeya lines directly, compares the full Fourier transform at all frequencies against the closed complex formula, and checks the four predicted levels and multiplicities at order 27. Its successful output ends in `CHECK_OK`. The smaller fields test normalization but are not part of the general odd-degree ternary four-level assertion. The proof covers every odd \(m\ge3\) independently of the finite tests.

## Relationship to prior work
Fraser, *Fourier analytic properties of Kakeya sets in finite fields* (first public 14 May 2025; 2026 journal version), proves that every finite-field Kakeya set supports **some** probability measure with Fourier decay at most \(1/q\). Crucially, its discussion distinguishes the existence of a suitable measure from **uniform** point mass, and its main theorem does not provide the complete transform of this particular half-density construction. The exact uniform spectrum here is not a corollary of that existence theorem. Kopparty, Lev, Saraf, and Sudan, *Kakeya-type sets in finite vector spaces*, construct essentially this quadratic Kakeya point set via a quadratic polynomial, but their stated cardinality and Kakeya results do not calculate its uniform Fourier coefficients. The present work uses standard Gauss-sum identities and does not claim those identities or the quadratic Kakeya construction as new.

## Limitations
The new assertion is an explicit uniform-measure spectrum for odd-degree extensions of the field with three elements, not a spectral classification of all Kakeya sets and not the optimal measure among arbitrary nonuniform weights. The Fourier norm is unnormalized before dividing by \(|K|\); this convention matters for the four squared levels. The leading-order \(1/q\) comparison is asymptotic, not the exact inequality \(\max|\widehat\mu|\le1/q\). Earlier equivalent calculations in incidence theory, coding theory, or character-sum literature may exist despite the comparisons described. No external independent audit has been performed.

## References
1. Jonathan M. Fraser, *Fourier analytic properties of Kakeya sets in finite fields*, arXiv:2505.09464 (first submitted 14 May 2025), *Bulletin of the London Mathematical Society* 58 (2026), e70367, DOI:10.1112/blms.70367; https://arxiv.org/abs/2505.09464.
2. Swastik Kopparty, Vsevolod F. Lev, Shubhangi Saraf, and Madhu Sudan, *Kakeya-type sets in finite vector spaces*, arXiv:1003.3736; https://people.csail.mit.edu/madhu/papers/2010/seva.pdf. See Section 3, Lemma 17 and the quadratic choice of the function.
3. Classical finite-field quadratic Gauss-sum identities, as derived explicitly in the proof above.
