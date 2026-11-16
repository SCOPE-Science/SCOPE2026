# The Apéry fourth moment of uniform spherical cross ratios

## Finding

Let \(P_1,P_2,P_3,P_4\) be independent points distributed according to normalized area on the unit sphere \(S^2\). Write \(z_i\) for stereographic coordinates, and use the cross-ratio convention
\[
Z=\frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_2)(z_3-z_4)},\qquad Y=\log|Z|.
\]
Then the first nontrivial higher logarithmic moment has the exact value
\[
\boxed{\mathbb E[Y^4]=12-6\zeta(3)=4.787658581042434\ldots.}
\]
Together with \(\mathbb E Y=0\) and \(\mathbb E Y^2=1\), this gives excess kurtosis \(9-6\zeta(3)\). The underlying four-edge dependency has the exact spectral value
\[
\boxed{\mathbb E[X_{13}X_{24}X_{12}X_{34}]
=\frac5{16}-\frac{\zeta(3)}4
=0.0119857742101014\ldots,}
\]
where \(X_{ij}=\log(|P_i-P_j|/2)+1/2\). These four centered edge variables are three-wise independent but not jointly independent. The displayed identities form one connected result: the four-edge dependency is precisely the correction to the independent-edge fourth moment.

## Assumptions and scope

All four sphere points are iid with normalized rotation-invariant area measure \(d\sigma=dA/(4\pi)\). Chordal distances are Euclidean distances in \(\mathbb R^3\), halved to lie in \([0,1]\). Coincidences have measure zero. The cross ratio is the standard stereographically invariant quantity with the above convention, and the logarithm is the real logarithm of its modulus. All random variables possess finite moments of every finite order: conditional on any fixed endpoint, the squared half-chord distance to an independent uniform point is uniform on \((0,1)\), and logarithms of such variables have all finite moments. The claim concerns four **spherical** samples, not four samples on a circle.

## Proof

**1. Chordal representation and one-edge law.** Stereographic metric factors cancel between the four terms in the cross ratio, so, setting \(q_{ij}=|P_i-P_j|/2\),
\[
Y=\log q_{13}+\log q_{24}-\log q_{12}-\log q_{34}
=X_{13}+X_{24}-X_{12}-X_{34}.
\]
For independent uniform \(P,Q\in S^2\), \(q(P,Q)^2=(1-P\cdot Q)/2\) is uniform on \((0,1)\). Consequently, the centered variable \(X=\log q+1/2\) has law \((1+\log U)/2\), where \(U\) is uniform on \((0,1)\). Integrating the elementary exponential density gives
\[
\mathbb E X=0,\qquad \mathbb E X^2=\frac14,\qquad
\mathbb E X^4=\frac9{16}.
\]

**2. Three-wise independence.** View each \(X_{ij}\) as an edge function on the four vertices \(1,2,3,4\). The selected edges \((13),(32),(24),(41)\) form a simple cycle of length four. Every proper subset is a forest. For any finite forest of independent uniform spherical vertices, its edge-chord variables are mutually independent: integrate out a leaf vertex first; conditional on its neighbor, its incident chord has a law independent of that neighbor by rotation invariance. Repeating the leaf elimination factors the joint expectation of any bounded functions of the edges. Truncation extends this property to integrable edge functions. Thus every subset of at most three selected centered edge variables is independent. In particular all mixed terms containing a singleton centered edge vanish, and all two-edge and three-edge moments factor as in the independent model.

**3. Logarithmic spherical-harmonic operator.** Define the real symmetric kernel on \(S^2\times S^2\)
\[
K(P,Q)=\log\frac{|P-Q|}{2}+\frac12
=\frac12\log\frac{1-P\cdot Q}{2}+\frac12,
\]
and its integral operator \((Tf)(P)=\int K(P,Q)f(Q)\,d\sigma(Q)\). This is Hilbert--Schmidt because the logarithmic diagonal singularity is square-integrable. The constant function has eigenvalue zero. By Funk--Hecke, the degree-\(\ell\) spherical harmonics (multiplicity \(2\ell+1\)) have eigenvalue
\[
\lambda_\ell=\frac12\int_{-1}^{1}K(t)P_\ell(t)\,dt
=\frac14\int_{-1}^{1}\log\frac{1-t}{2}P_\ell(t)\,dt
=-\frac1{2\ell(\ell+1)},\quad\ell\ge1.
\]
For completeness, multiply the Legendre equation \(((1-t^2)P_\ell'(t))'=-\ell(\ell+1)P_\ell(t)\) by \(\log((1-t)/2)\), integrate by parts and use \(\int_{-1}^{1}P_\ell(t)\,dt=0\) and \(P_\ell(1)=1\). The boundary terms vanish, and the remaining derivative integral is \(\int_{-1}^{1}(1+t)P_\ell'(t)\,dt=2\). Hence the displayed Legendre-log integral equals \(-2/[\ell(\ell+1)]\).

**4. Four-cycle trace and exact summation.** The mixed four-edge moment is the integral of the product of \(K\) around its four-cycle. Since \(T\) is Hilbert--Schmidt, \(T^4\) is trace-class, and repeated Hilbert--Schmidt kernel composition (or finite-rank approximation in Hilbert--Schmidt norm) justifies the identity
\[
M_4:=\mathbb E[X_{13}X_{24}X_{12}X_{34}]
=\operatorname{Tr}(T^4)
=\sum_{\ell=1}^{\infty}(2\ell+1)\lambda_\ell^4
=\sum_{\ell=1}^{\infty}\frac{2\ell+1}{16\ell^4(\ell+1)^4}.
\]
The rational summand splits exactly as
\[
\frac{2\ell+1}{16\ell^4(\ell+1)^4}
=\frac1{8\ell^2}-\frac1{8\ell^3}+\frac1{16\ell^4}
-\frac1{8(\ell+1)^2}-\frac1{8(\ell+1)^3}-\frac1{16(\ell+1)^4}.
\]
The quadratic and quartic terms telescope, while the cubic terms add to an ordinary \(\zeta(3)\) sum, giving
\[
M_4=\frac5{16}-\frac{\zeta(3)}4>0.
\]
The strict positivity also follows directly from the nonzero degree-one spherical harmonics in the spectral sum.

**5. Fourth-moment expansion.** Expand \(Y^4\) using the four signed, centered edge variables. Three-wise independence kills every term involving an odd singleton. The terms supported on a single edge contribute \(4(9/16)\); those supported on two distinct edges with exponents two and two contribute \(6\binom42(1/4)^2=36/16\). The only additional term, with one power of each edge, has coefficient \(4!=24\) and positive total sign (two minus signs). Hence
\[
\mathbb E Y^4=4\frac9{16}+36\frac1{16}+24M_4
=\frac92+24\left(\frac5{16}-\frac{\zeta(3)}4\right)
=12-6\zeta(3).
\]
Pairwise independence also yields \(\mathbb E Y^2=4(1/4)=1\), while inversion of the cross ratio changes the sign of \(Y\) in distribution, so the odd moments vanish. This proves the theorem.

## Verification

The accompanying standalone script `CHECK.py` checks the rational partial fraction identity and infinite zeta sum symbolically, verifies eight Legendre-log integrals to high numerical precision, checks six finite spectral truncations against analytical tail inequalities, and tests the one- and four-edge moment formulas using a seeded independent spherical sample. These finite checks are not substitutes for the analytical proof of the integral identities or trace formula.

## Relationship to prior work

Marshall and Martin (2026) determine the **complete planar density** of the spherical cross ratio and explicitly calculate \(\mathbb E\log|Z|=0\) and \(\operatorname{Var}(\log|Z|)=1\). Their Proposition 5.1 also notes that the four chordal logarithms are not jointly independent. A complete distribution formally determines all integrable moments by quadrature; that stronger distributional description is not disputed. The present contribution is the *exact closed evaluation* of the previously unevaluated fourth logarithmic moment and the spectral identification and value of its connected four-edge correction. Their paper has no statement of the Apéry-constant value, the four-edge trace, or the fourth moment. Martin's 2018 earlier cross-ratio calculation samples four points **on a circle**, a distinct probability model with a real-valued cross ratio. The Funk--Hecke formula, Legendre equation, spherical harmonics, and trace-of-kernel identities used here are classical tools and are not claimed as new.

## Limitations

This is an exact fourth-moment statement and its four-edge explanation, not a new closed law for the entire cross ratio: the full density is known. No assertion is made about all higher logarithmic moments, arbitrary nonuniform sphere distributions, or other cross-ratio conventions without an explicit relabeling. Equivalence to older spherical Green-kernel cycle identities under different terminology has not been independently ruled out; publication priority requires external confirmation.

## References

1. Tim Marshall and Gaven Martin, *Random complex cross ratios*, arXiv:2611.07670v1, initially publicly submitted 2026-11-05. Primary text: https://arxiv.org/html/2611.07670v1 (especially Sections 1, 2, and 5.1, Proposition 5.1).
2. Gaven J. Martin, *Random Ideal Hyperbolic Quadrilaterals, the Cross Ratio Distribution and Punctured Tori*, arXiv:1807.06202v1, initially publicly submitted 2018-07-17. Primary text: https://arxiv.org/abs/1807.06202 (circle rather than sphere sampling model).
3. Standard analytic identities: Funk--Hecke formula, Legendre differential equation, and the spectral trace identity for powers of a Hilbert--Schmidt integral operator.
