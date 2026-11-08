# Cyclotomic collision of fixed points on smooth cyclic Klein cubics

## Finding

For each prime \(p\ge 5\), put \(R=\mathbb Z_{(p)}\), and consider the cubic hypersurface \(\mathcal X_p\subset\mathbb P_R^{p-1}\) defined by
\[
 F_p=\sum_{i\in\mathbb Z/p\mathbb Z}X_i^2X_{i+1}=0.
\]
The coordinate cycle \(\tau([X_0:\cdots:X_{p-1}])=[X_1:\cdots:X_{p-1}:X_0]\) preserves \(\mathcal X_p\). It has scheme-theoretic fixed locus
\[
 (\mathcal X_p)^\tau\cong\operatorname{Spec}\bigl(R[\lambda]/\Phi_p(\lambda)\bigr),\qquad
 \Phi_p(\lambda)=1+\lambda+\cdots+\lambda^{p-1}.
\]
This is finite flat of degree \(p-1\). Its characteristic-zero generic fiber consists of \(p-1\) geometrically distinct points; its fiber over \(\mathbb F_p\) is one curvilinear point of length \(p-1\), with local ring \(\mathbb F_p[t]/(t^{p-1})\). The completed local ring at the collision is the degree-\(p-1\) totally ramified cyclotomic extension ring \(\mathbb Z_p[t]/(\Phi_p(1+t))\). Both the generic and special cubic hypersurfaces are smooth. At the special fixed point \(P=[1:\cdots:1]\), the induced action on \(T_P(\mathcal X_p\otimes\mathbb F_p)\) has one unipotent Jordan block of size \(p-2\).

In particular, for \(p=5\), the characteristic-five Klein cubic threefold has a unique geometric fixed point of this five-cycle, but its fixed-point subscheme has length four and its tangent representation is one Jordan block of size three.

## Assumptions and scope

The base ring is the localization \(\mathbb Z_{(p)}\) at a prime \(p\ge5\); indices in the equation are interpreted modulo \(p\). The fixed subscheme means the equalizer of \(\tau\) and the identity on the indicated projective hypersurface. No assertion is made about fixed subschemes of other automorphisms, the full automorphism group scheme, or quotient singularities. The adjective “cyclotomic” refers to the explicit polynomial \(\Phi_p\), not a claim that the cubic carries a primitive-root coefficient.

## Proof

**1. Smoothness in both fibers.** A partial derivative of \(F_p\) is
\[
 \frac{\partial F_p}{\partial X_i}=2X_iX_{i+1}+X_{i-1}^2.
\]
Over an algebraically closed field of characteristic zero or \(p\), a common projective zero of all these derivatives cannot have a zero coordinate: if \(X_i=0\), the derivative at index \(i\) gives \(X_{i-1}=0\), and this propagates cyclically to all coordinates. With all coordinates nonzero, multiplying the \(p\) gradient equations \(X_{i-1}^2=-2X_iX_{i+1}\) and canceling their common nonzero product yields \((-2)^p=1\). This is impossible in characteristic zero. In characteristic \(p\), Frobenius reduces it to \(-2=1\), impossible for \(p\ge5\). Both fibers are therefore nonsingular. Since the equation is primitive and defines a relative effective Cartier divisor in projective space, \(\mathcal X_p\to\operatorname{Spec}R\) is flat; fiberwise smoothness gives smoothness over \(R\).

**2. Ambient projective fixed scheme.** In the equalizer of the coordinate-cycle action on \(\mathbb P_R^{p-1}\), every geometric fixed point has \(X_0\ne0\): a projectively fixed vector is an eigenvector of the invertible cycle, and one zero coordinate would force every coordinate zero. Thus the entire closed fixed subscheme is contained in the chart \(X_0=1\). There, the fixed equations state that for an invertible scalar \(\lambda\) the coordinates are \(X_i=\lambda^i\) and \(\lambda^p=1\). Conversely those equations imply projective fixedness. Scheme-theoretically the projective-space fixed locus is
\[
 \operatorname{Spec}R[\lambda]/(\lambda^p-1).
\]
These identities are obtained from the proportionality equations defining the equalizer, so they hold also on nonreduced fibers.

**3. Restriction of the cubic.** On this fixed scheme, \(F_p\) becomes
\[
 \sum_{i=0}^{p-1}\lambda^{2i+(i+1)}
 =\sum_{i=0}^{p-1}\lambda^{3i+1}.
\]
Because \(3\) is invertible modulo \(p\), the exponents \(3i+1\) traverse all residues modulo \(p\). Hence modulo \(\lambda^p-1\) this polynomial equals \(\Phi_p(\lambda)\). As \(\lambda^p-1=(\lambda-1)\Phi_p(\lambda)\), the ideal cutting out fixed points on \(\mathcal X_p\) is exactly \((\Phi_p(\lambda))\). This proves the stated integral fixed-scheme isomorphism.

**4. Fiber collision and ramification.** The monic polynomial \(\Phi_p\) has degree \(p-1\), so its quotient is a free \(R\)-module of rank \(p-1\). Over characteristic zero its roots are the primitive \(p\)-th roots of unity, all simple. In characteristic \(p\), the identity \(\lambda^p-1=(\lambda-1)^p\) gives \(\Phi_p(\lambda)=(\lambda-1)^{p-1}\). Putting \(t=\lambda-1\),
\[
 \Phi_p(1+t)=\frac{(1+t)^p-1}{t}
 =t^{p-1}+\binom p{p-1}t^{p-2}+\cdots+\binom p2 t+p.
\]
Every nonleading coefficient is divisible by \(p\), but the constant is not divisible by \(p^2\). Thus it is Eisenstein over \(\mathbb Z_p\), and the asserted local ring and total ramification follow.

**5. Tangent representation.** In characteristic \(p\), the permutation representation of a \(p\)-cycle on \(k^p\) is the single size-\(p\) nilpotent Jordan block for \(N=\tau-I\); this follows, for example, from the cyclic basis and the identity \((\tau-I)^p=0\) together with \(\dim\ker(\tau-I)=1\). At \(P\), every partial derivative of the cubic is \(3\ne0\), so its affine-cone tangent hyperplane is \(\ker(\sum_i v_i)\). The projective tangent space is
\[
 T_P\mathcal X_{p,k}=\ker\Bigl(\sum_i v_i\Bigr)/\langle(1,\ldots,1)\rangle
 =\operatorname{im}(N)/\ker(N).
\]
For one size-\(p\) Jordan block, this quotient has one block of size \(p-2\). Its fixed tangent direction has dimension one; this is consistent with, but does not replace, the fixed-scheme calculation.

## Verification

The companion standalone standard-library program `verify_klein_cyclic.py` checks the exponent permutation, Eisenstein coefficients, residual nilpotent polynomial, gradient obstruction, and cycle Jordan ranks for primes \(5,7,11,13,17,19\). Its recorded output is `verify_klein_cyclic.out` and ends in `VERIFY_OK`. These are finite algebraic regression tests only. The proof above, rather than finite extrapolation, establishes the theorem for every prime \(p\ge5\).

To reproduce, use a Python 3 interpreter and run `python3 verify_klein_cyclic.py` in a directory containing the companion file. No third-party packages are needed.

## Relationship to prior work

González-Aguilera and Liendo, *Automorphisms of prime order of smooth cubic n-folds* (arXiv:1002.4136, first posted 22 February 2010), define and investigate the Klein cyclic cubic and prime-order automorphisms in the characteristic-zero classification setting. This supplies the natural family and symmetry, not the claimed wild-characteristic fixed subscheme. Roulleau, *The Fano surface of the Klein cubic threefold* (arXiv:1001.4853, first posted 27 January 2010), analyzes the classical complex Klein cubic, automorphisms, and its Fano surface. Van Geemen and Yamauchi, *On intermediate Jacobians of cubic threefolds admitting an automorphism of order five* (arXiv:1506.05346, first posted 17 June 2015), explicitly work over characteristic zero with a primitive fifth root of unity. Their intermediate-Jacobian results do not assert the mixed-characteristic cyclotomic fixed-locus isomorphism.

The present statement makes no claim that cyclic eigenvectors, cyclotomic ramification, or unipotent Jordan theory are new individually; its subject is their exact simultaneous realization as the fixed scheme of a smooth Klein cubic family. Possible unpublished or uninspected modular-automorphism calculations remain a historical-priority risk.

## Limitations

The fixed-locus description concerns only the displayed coordinate-cycle automorphism of the displayed integral hypersurface. It does not determine a quotient, a stable model, other automorphism fixed schemes, or any global automorphism-group classification. The characteristic \(p=3\) is excluded: multiplication by three is not invertible on the index group, and the smoothness argument also changes. The result does not cover primes smaller than five. Independent validation has not been undertaken.

## References

1. X. Roulleau, *The Fano surface of the Klein cubic threefold*, arXiv:1001.4853 (first posted 2010-01-27), https://arxiv.org/html/1001.4853v1 .
2. V. González-Aguilera and A. Liendo, *Automorphisms of prime order of smooth cubic n-folds*, arXiv:1002.4136 (first posted 2010-02-22), https://arxiv.org/html/1002.4136v2 .
3. B. van Geemen and T. Yamauchi, *On intermediate Jacobians of cubic threefolds admitting an automorphism of order five*, arXiv:1506.05346 (first posted 2015-06-17), https://arxiv.org/html/1506.05346v3 .
