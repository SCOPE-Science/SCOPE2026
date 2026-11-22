# Four Fourier-intensity observations determine three intervals with equal gaps

## Finding
Let \(a,b,c,g>0\), put \(L=a+b+c+2g\), and consider
\[
\Omega_{a,b,c,g}=[0,a]\cup[a+g,a+g+b]\cup[a+2g+b,L].
\]
Set \(\mathcal I_{\Omega}(t)=\left|\int_{\Omega}e^{-itx}\,dx\right|^2\). **Within the class of three positive-length intervals separated by two gaps of the same positive length, and with known total span \(L\), the four real measurements**
\[
\mathcal I(0),\qquad \mathcal I(2\pi/L),\qquad
\mathcal I''(0),\qquad \mathcal I^{(4)}(0)
\]
**determine \(\Omega\) up to translation and reflection.** This holds for all positive real lengths; neither an integer-grid assumption nor genericity is needed.

## Assumptions and scope
The Fourier transform uses \(\widehat{\mathbf1_{\Omega}}(t)=\int_{\Omega}e^{-itx}\,dx\), with no normalization. The support is understood up to changes at its endpoints. Its smallest containing interval has known length \(L\); translation normalizes the left endpoint to \(0\). The occupied lengths \(a,b,c\) and both hole lengths \(g\) are strictly positive. Reflection exchanges \(a\) and \(c\). This is an injectivity theorem **within the equal-hole family**, not among unrestricted finite unions of intervals.

## Proof
Write \(S=a+b+c\), \(v=a+c\), \(D=b+g\), \(h=(a-c)/2\), and \(\operatorname{sinc}(u)=\sin(u)/u\) with value \(1\) at zero. The complement of \(\Omega\) in \([0,L]\) is two intervals of common length \(g\), whose center separation is \(D\) and whose average center differs from \(L/2\) by \(h\). Subtract their transforms from the transform of \([0,L]\). Squaring the modulus gives the exact identity
\[
\mathcal I(t)=L^2\operatorname{sinc}^2(Lt/2)
 +4g^2\operatorname{sinc}^2(gt/2)\cos^2(Dt/2)
 -4Lg\operatorname{sinc}(Lt/2)\operatorname{sinc}(gt/2)
 \cos(Dt/2)\cos(ht).\tag{1}
\]
Suppose two admissible triples with the same known span have identical four measurements; prime the parameters of the second. Since \(\mathcal I(0)=S^2\), they have the same \(S\), so \(g=g'=(L-S)/2\). Because \(\operatorname{sinc}(\pi g/L)\ne0\), evaluation of (1) at \(t=2\pi/L\) implies
\[
\cos^2(\pi D/L)=\cos^2(\pi D'/L).
\]
Here \(0<D,D'<L\), so precisely \(D'=D\) or \(D'=L-D\).

In the first case, the common \(D\) gives \(b'=b\) and \(a'+c'=a+c=v\). Subtracting the two versions of (1), their difference is a nonzero analytic factor near zero times \(\cos(ht)-\cos(h't)\). Equality of the second derivatives therefore gives \(h'^2=h^2\). Thus \(\{a',c'\}=\{a,c\}\), as required.

In the second case, \(D'=L-D\) forces \(b'=v=a+c\), so \(v'=a'+c'=b\). Since \(D'=v+g\), subtraction of (1), using \(\cos^2(A)-\cos^2(B)=-\sin(A+B)\sin(A-B)\), yields
\[
\mathcal I_{\Omega}(t)-\mathcal I_{\Omega'}(t)
 =-4gL\operatorname{sinc}(gt/2)\operatorname{sinc}(Lt/2)P(t),\tag{2}
\]
where
\[
P(t)=\cos((b+g)t/2)\cos(ht)
 -\cos((v+g)t/2)\cos(h't)
 +\sin(gt/2)\sin((b-v)t/2).
\]
The analytic prefactor in (2) is nonzero at \(t=0\). The function \(P\) is even and \(P(0)=0\); hence equality of the second and fourth derivatives of the measured intensities implies \([t^2]P=[t^4]P=0\). Direct Taylor expansion gives
\[
[t^2]P=-\frac{b^2-v^2+4h^2-4h'^2}{8},
\]
which forces \(h'^2=h^2+(b^2-v^2)/4\). Substitute this relation in the fourth coefficient; exact factorization gives
\[
[t^4]P=-\frac{(b-v)(v-2h)(v+2h)(b+v+3g)}{96}
=-\frac{(b-v)\,4ac\,(S+3g)}{96}.\tag{3}
\]
Strict positivity of \(a,c,g,S\) implies \(b=v\). Consequently \(D'=L-D=D\), reducing to the first case. Thus the only ambiguity is reflection; translation was fixed by normalizing the span. \(\square\)

## Verification
The accompanying standalone `checker.py` verifies the two exact symbolic coefficient identities in (3) using SymPy and separately compares direct interval-by-interval Fourier integration with (1) in \(1{,}500\) deterministic real-parameter examples. Reproduce by running `python checker.py` with Python 3 and SymPy installed. These finite checks support but do not replace the all-parameter analytical proof above.

## Relationship to prior work
Xia and Xu, *Fourier Phase Retrieval for Finite Unions of Intervals* (arXiv:2606.19855, first posted 2026-06-18), study the general interval-union phase retrieval problem, establishing nonuniqueness for arbitrary three-or-more-interval unions. The present theorem isolates the equal-hole three-interval subfamily and gives a four-observation injectivity statement, rather than requiring the whole Fourier-intensity function. Rosenblatt and Seymour's homometric-set framework and Bianchi's covariogram survey explain the broader Fourier-magnitude ambiguity mechanism. Exact coverage by inaccessible full texts has not been ruled out.

## Limitations
The span must be known, and all five positive lengths must be strictly positive. The four data are noiseless and contain two exact derivatives; neither numerical conditioning nor stable recovery under noise is established. The result does not claim injectivity across different numbers of components or across unequal-hole candidates. The full text of the closest 2026 preprint was not accessible for a complete theorem-by-theorem comparison; an older equivalent special case remains possible. There has been no independent mathematical validation.

## References
1. Y. Xia and Z. Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855 (first public 2026-06-18), https://arxiv.org/abs/2606.19855.
2. J. Rosenblatt and P. D. Seymour, *The Structure of Homometric Sets*, SIAM Journal on Algebraic and Discrete Methods (1982), https://doi.org/10.1137/0603035.
3. G. Bianchi, *The Covariogram Problem: A Survey*, https://people.dimai.unifi.it/bianchi/lavori/covariogram_survey14.pdf.
