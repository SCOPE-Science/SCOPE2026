# The terminal Cartier rank of binary Serre-type maximal curves

## Finding

Let \(n=2s+1\ge3\) be odd, put \(Q=4^s\) and \(m=(2Q+1)/3=(2^n+1)/3\), and let \(X_n\) be the smooth projective model of
\[
y^4+y=x^m
\]
over the algebraic closure of \(\mathbb F_2\). For the Cartier operator \(\mathcal C:H^0(X_n,\Omega^1)\to H^0(X_n,\Omega^1)\),
\[
\boxed{\operatorname{rank}(\mathcal C^{n-1})=\frac{n-1}{2},\qquad \mathcal C^n=0.}
\]
Thus the nilpotency index is exactly \(n\), and the number of chains of maximum length in the nilpotent Cartier rank filtration is \((n-1)/2\). More precisely, the terminal nonzero Cartier image has the explicitly described basis
\[
\operatorname{im}(\mathcal C^{n-1})
=\bigoplus_{t=0}^{s-1} k\,x^{2(4^t-1)/3}\,dx.
\]
In particular this rank grows linearly in \(n\) although the genus is \(2^{n-1}-1\).

## Assumptions and scope

The base field is \(k=\overline{\mathbb F}_2\); all ranks are dimensions over \(k\). The integer \(s\) ranges over all integers \(s\ge1\). The curve is the normalization of the displayed affine curve. As \(m\) is odd, its function field is a degree-four separable extension of \(k(x)\), with unique point at infinity, valuations \(v_\infty(x)=-4\), \(v_\infty(y)=-m\), and genus \(g=3(m-1)/2=Q-1\). In particular, \(\operatorname{div}(dx)=(2g-2)P_\infty\), and the holomorphic differentials have monomial basis
\[
\mathcal B=\{x^iy^j\,dx:\ i\ge0,\ 0\le j\le2,\ 4i+mj\le2Q-4\}.
\]
These statements also follow directly from the one-pole semigroup \(\langle4,m\rangle\), using smoothness of the affine chart (the partial derivative with respect to \(y\) is one). No other curve families, extension-field point counts, or complete Ekedahl--Oort types are classified here.

## Proof

Write \(r=2s=n-1\), so that \(Q=2^r\). The defining equation in characteristic two gives
\[
y=y^4+x^m=y^{4^s}+\sum_{t=0}^{s-1}x^{m4^t}
  =y^Q+\sum_{t=0}^{s-1}x^{m4^t}.
\tag{1}
\]
For any function \(f\) expanded in the \(Q\)-basis \(1,x,\ldots,x^{Q-1}\) over \(k(X_n)^Q\), the iterate \(\mathcal C^r(f\,dx)\) is its coefficient of \(x^{Q-1}\), with the \(Q\)-th power removed, times \(dx\). In particular, for an individual term \(x^e h^Q\,dx\), it survives exactly when \(e\equiv Q-1\pmod Q\); its image is \(x^{(e-Q+1)/Q}h\,dx\). This is the standard iterated Cartier formula, not a finite-sample argument.

For \(j=0\), the basis bound is \(0\le i\le Q/2-1<Q-1\), so \(\mathcal C^r(x^i\,dx)=0\). For \(j=1\) the bound is \(0\le i\le (Q-4)/3\). In (1), the term \(x^iy^Q\) contributes nothing because \(i<Q-1\). The term with index \(t\) contributes exactly when
\[
i+m4^t\equiv Q-1\pmod Q.
\]
For each \(0\le t<s\), the unique solution in the allowed interval is
\[
i_t=\frac{Q-4^t-3}{3}, \qquad 0\le i_t\le\frac{Q-4}{3}.
\]
Indeed the identity
\[
i_t+m4^t=Q\,\frac{2\cdot4^t+1}{3}-1
\]
proves the congruence, and the allowed interval has length less than \(Q\). Hence
\[
\mathcal C^{n-1}(x^{i_t}y\,dx)
=x^{2(4^t-1)/3}\,dx.
\tag{2}
\]
All these exponents are distinct, so the displayed images are linearly independent.

For \(j=2\), use the square of (1):
\[
y^2=y^{2Q}+\sum_{t=0}^{s-1}x^{2m4^t}.
\]
The basis bound is \(0\le i\le\lfloor(Q-7)/6\rfloor\) (an empty interval if \(Q=4\)). The first term again cannot contribute. For each index \(t\), a possible residue solving \(i+2m4^t\equiv Q-1\pmod Q\) is \(i\equiv2i_t+1\pmod Q\). But
\[
Q/2-1\le2i_t+1\le(2Q-5)/3<Q,
\]
whereas \(i\le\lfloor(Q-7)/6\rfloor<Q/2-1\). Thus no such \(i\) exists, proving that every \(j=2\) basis differential is killed by \(\mathcal C^{n-1}\).

The nonzero images have therefore been found exhaustively, and (2) proves \(\operatorname{rank}(\mathcal C^{n-1})=s\). Finally, all output exponents in (2) are even. For any nonnegative integer \(a\), \(\mathcal C(x^{2a}\,dx)=0\), so the next Cartier iterate kills the entire image. Thus \(\mathcal C^n=0\), while \(\mathcal C^{n-1}\ne0\), completing the proof. The count of length-\(n\) chains follows from the standard rank filtration of a nilpotent semilinear map over the perfect field \(k\).

## Verification

The independent exact-arithmetic checker `cartier_terminal_check.py` constructs the monomial differential basis and evaluates \(\mathcal C^{n-1}\) in two mathematically distinct ways: by the direct \(Q\)-power expansion (1), and by iterating the one-step Cartier map. It compares both to the symbolic closed form (2) for \(n=3,5,7,9,11,13,15\), checks rank, and verifies that the final image is annihilated by one more Cartier application. These are finite tests only; the proof above covers every odd \(n\ge3\). Run `python3 cartier_terminal_check.py` with Python 3.8 or later; no packages or external input are required.

## Relationship to prior work

Abdón--Bezerra--Quoos introduced these maximal curves, supplying their genus and maximality. Garcia--Tafazolian proved the general vanishing \(\mathcal C^n=0\) for curves maximal over \(\mathbb F_{2^{2n}}\). Thus the vanishing half of the theorem is compatible with a known general upper bound; its sharpness for this entire family, and the exact rank and basis of \(\mathcal C^{n-1}\), are the additional conclusions.

Shafighi (2026), arXiv:2610.15266, computes the \(a\)-number and derives an explicit **one-step** Cartier action on a monomial basis. That action makes all iterates computable in principle, but the inspected paper does not state the uniform penultimate-rank formula or identify the terminal image. The present proof evaluates the penultimate iterate for all \(n\) simultaneously, rather than treating a finite list. Groen's general results give bounds for powers on Artin--Schreier covers, not this terminal equality for the degree-four elementary-abelian covers. The corresponding results for van der Geer--van der Vlugt curves (2026) concern a different family.

## Limitations

The result covers only the \(q=2\) specialization of the Serre-type maximal curves and only the last nonzero Cartier iterate; it does not supply all intermediate ranks or the complete Ekedahl--Oort type. Its novelty is conditional on the accessible comparison, especially because the published one-step formula formally allows algorithmic recovery of the answer. The 2009 original construction was located by bibliographic description but its full text was not available for inspection. No independent mathematical audit has been performed.

## References

1. M. Shafighi, *The a-number of the Serre-type maximal curves of Abdón--Bezerra--Quoos*, arXiv:2610.15266 (first public version October 11, 2026), especially Sections 3, 4, 6.
2. M. Abdón, J. Bezerra, L. Quoos, *Further examples of maximal curves*, J. Pure Appl. Algebra 213 (2009), 1192--1196, doi:10.1016/j.jpaa.2008.11.037.
3. A. Garcia, S. Tafazolian, *Certain maximal curves and Cartier operators*, Acta Arith. 135 (2008), 199--218, Theorem 3.3, doi:10.4064/aa135-3-1.
4. S. Groen, *Powers of the Cartier operator on Artin--Schreier covers*, Int. J. Number Theory 20 (2024), 1901--1941, arXiv:2208.06504.
5. G. B. Almeida Filho, S. Tafazolian, S. C. Vieira, *a-Numbers, higher Cartier ranks and maximality of van der Geer--van der Vlugt curves*, arXiv:2610.17476 (2026).
