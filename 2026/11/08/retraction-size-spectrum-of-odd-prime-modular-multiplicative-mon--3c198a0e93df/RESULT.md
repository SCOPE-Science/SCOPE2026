# Retraction-size spectrum of odd-prime modular multiplicative monoids

## Finding

For every odd prime \(p\) and integer \(e\ge 2\), let \(M_{p,e}\) denote the multiplicative monoid of residues \(\mathbb Z/p^e\mathbb Z\). An endomorphism here preserves multiplication and identity, but is **not** assumed additive. A *retraction endomorphism* is one with \(f\circ f=f\). Its image is a retract submonoid.

Put \(N=(p-1)p^{e-1}\), \(\varphi_j=(p-1)p^{j-1}\), and
\[
T_{p,e}=\{t\in\{0,\ldots,N-1\}:t^2\equiv t\pmod N\},\qquad
h_j(t)=\frac{\varphi_j}{\gcd(t,\varphi_j)}.
\]
The complete *image-size enumerator*, whose coefficient of \(z^s\) is the number of retraction endomorphisms with exactly \(s\) elements in their image, is
\[
\boxed{E_{p,e}(z)=z+\sum_{t\in T_{p,e}}\left[z^{1+h_e(t)}+\gcd(t,\varphi_{e-1})\,z^{1+\sum_{j=1}^e h_j(t)}\right].}
\]
In particular, if \(\omega(n)\) is the number of distinct prime divisors of \(n\) and \(\ell^b\parallel(p-1)\) runs through its exact prime-power factors, the number of retraction endomorphisms is
\[
\boxed{E_{p,e}(1)=1+2^{\omega(p-1)+1}+(1+p^{e-2})\prod_{\ell^b\parallel(p-1)}(1+\ell^b).}
\]
There is an exact structural dichotomy: apart from the constant-one map, every retraction either sends **all nonunits to zero**, or maps \(p\) to an element of valuation exactly one and **preserves every nonzero valuation stratum**. There are no retractions with \(f(p)\) of valuation strictly between one and infinity.

For example,
\[
E_{3,3}(z)=z+z^2+z^3+6z^4+3z^7+z^{10}+2z^{14}+z^{19}+z^{27}.
\]
Thus the multiplicative monoid of \(\mathbb Z/27\mathbb Z\) has exactly \(17\) retraction endomorphisms, and the polynomial records all nine possible image sizes and multiplicities.

## Assumptions and scope

All quantifiers range over odd primes \(p\) and integers \(e\ge2\). The polynomial and cardinality count unital multiplicative monoid endomorphisms, including the constant-one map. An endomorphism need not fix the absorbing zero; the constant-one map is the only endomorphism that does not. The submonoid \(f(M_{p,e})\) is the image of an idempotent map; its size is counted with multiplicity over all such maps, not up to image isomorphism. The ring's additive group is **not** part of the structure being preserved.

## Proof

**1. Normal form of all endomorphisms.** Write \(R=\mathbb Z/p^e\mathbb Z\) and \(U=R^\times\). The group \(U\) is cyclic of order \(N\), so every restriction \(f|_U\) is uniquely a power map \(u\mapsto u^t\), with \(t\) modulo \(N\). Because \(0\) is absorbing, \(f(0)\) is an idempotent of \(R\), hence \(0\) or \(1\). If \(f(0)=1\), then \(f(x)=f(x)f(0)=f(0)=1\) for every \(x\): this is the constant-one map. Otherwise \(f(0)=0\), and \(f(p)\) cannot be a unit, since \(f(p)^e=f(0)=0\). Put \(a=f(p)\in pR\).

Every nonzero \(x\in R\) can be written as \(p^ku\), where \(0\le k<e\) and \(u\in U\). Thus the map must have form
\[
F_{t,a}(0)=0,\quad F_{t,a}(u)=u^t,\quad F_{t,a}(p^ku)=a^ku^t.
\]
This formula is well defined: if \(p^ku=p^kv\) in \(R\), then \(u\equiv v\pmod {p^{e-k}}\), whence \(u^t\equiv v^t\pmod {p^{e-k}}\); multiplication by \(a^k\), which is divisible by \(p^k\), makes both values equal modulo \(p^e\). Multiplicativity follows from the formula, including products which vanish. Every choice of \(t\pmod N\) and \(a\in pR\) therefore yields an endomorphism; the choices are unique from the restriction to \(U\) and the value at \(p\).

**2. Idempotence criterion.** By the generators \(U\) and \(p\), a multiplicative \(F_{t,a}\) satisfies \(F_{t,a}^2=F_{t,a}\) exactly when
\[
t^2\equiv t\pmod N\qquad\text{and}\qquad F_{t,a}(a)=a.
\]
If \(a=0\), the second equation holds. If \(a\ne0\) has valuation \(v\ge2\), then \(F_{t,a}(a)\) has valuation \(v^2>v\), with zero interpreted as valuation at least \(e\). Thus it cannot equal \(a\). If \(a=pc\), where \(c\) is a unit determined modulo \(p^{e-1}\), then \(F_{t,a}(a)=a c^t\). Therefore \(F_{t,a}(a)=a\) exactly when \(c^t\equiv1\pmod {p^{e-1}}\). The cyclic group \((\mathbb Z/p^{e-1}\mathbb Z)^\times\), of order \(\varphi_{e-1}\), has precisely \(\gcd(t,\varphi_{e-1})\) elements satisfying this condition. Consequently, for each \(t\in T_{p,e}\), exactly one retraction has \(a=0\) and exactly \(\gcd(t,\varphi_{e-1})\) retractions have \(a\) of valuation one. The constant-one map contributes one additional retraction.

**3. Image sizes.** If \(a=0\), the image consists of the identity's zero class together with the subgroup \(U^t\), whose size is \(h_e(t)=N/\gcd(t,N)\), giving \(1+h_e(t)\). If \(a=pc\), images of inputs of valuation \(k\) (for each \(0\le k<e\)) lie in valuation \(k\), and in that stratum have cardinality
\[
\left|\{p^kc^k u^t:u\in U\}\right|=\frac{\varphi_{e-k}}{\gcd(t,\varphi_{e-k})}=h_{e-k}(t).
\]
Indeed, reduction \(U\to (\mathbb Z/p^{e-k}\mathbb Z)^\times\) is surjective, and its target is cyclic; multiplication by \(c^k\) does not change the subgroup-image cardinality. The strata are disjoint, and zero contributes one element. Hence the image size is \(1+\sum_{j=1}^e h_j(t)\). Weighting these sizes by the counts in Step 2 proves the displayed polynomial.

**4. Closed cardinality.** By the Chinese remainder theorem, \(t^2\equiv t\pmod N\) means that \(t\) is either \(0\) or \(1\) on every exact prime-power factor of \(N\). Since \(e\ge2\), there are \(\omega(p-1)+1\) such factors, giving \(2^{\omega(p-1)+1}\) choices. The sum of the weights in Step 2 factorizes:
\[
\sum_{t\in T_{p,e}}\gcd(t,\varphi_{e-1})
=(1+p^{e-2})\prod_{\ell^b\parallel(p-1)}(1+\ell^b).
\]
For a prime-power factor \(\ell^b\) of \(p-1\), the two CRT choices contribute \(\ell^b\) and \(1\); for the \(p\)-part, they contribute \(p^{e-2}\) and \(1\), including the case \(e=2\). Together with the constant-one and \(a=0\) retractions, this gives the total formula.

## Verification

The standalone Python file `verify.py` directly constructs maps on residue classes for the six instances \((p,e)=(3,2),(3,3),(3,4),(5,2),(5,3),(7,2)\). It checks uniqueness of constructed maps, composition-idempotence at every element, image-size multisets against the independently evaluated polynomial, and the closed total count. In the small cases of modulus at most \(25\), it also verifies multiplicativity for every ordered pair of residues. The recorded output is supplied as `verification_output.txt`; running `python verify.py` reproduces it. These finite checks corroborate the proof but are not used to infer the result for arbitrary primes and exponents.

## Relationship to prior work

Atalaye, Baker, and Marques (arXiv:2610.02393v1, Proposition 3.1 and Corollary 3.2) classify multiplicative monoid morphisms of prime-power residue rings, giving the existence and parameterization of endomorphisms. Their later structural theorem concerns a monoid operation induced by pointwise multiplication of maps, **not their composition**. The normal form of Step 1 is consistent with their work and is not claimed to be new. The contribution assessed here is the *composition-idempotent subfamily*, its exact retraction-image spectrum, and its closed arithmetic count. The authors' earlier arXiv:2408.06278 concerns automorphisms, a smaller and different subfamily of the endomorphisms.

## Limitations

The proof concerns odd-prime powers only; it does not cover \(p=2\), whose unit groups in larger exponents are noncyclic. It counts retractions with multiplicity as maps, not isomorphism classes of retract submonoids. The image-size polynomial is an explicit finite sum of \(2^{\omega(p-1)+1}\) terms but is not simplified into a distinct-size classification. The morphism normal form is prior mathematical knowledge, and historical priority for the retraction enumerator, especially against terminology from semigroup retract theory and unpublished thesis material, remains to be independently checked.

## References

- J. Atalaye, L. Baker, and S. Marques, *Prime-Power Multiplicative Modular Monoid Morphisms*, arXiv:2610.02393v1 (first public 2026-10-01), especially Proposition 3.1, Corollary 3.2, and Theorem 3.4. https://arxiv.org/html/2610.02393v1
- J. Atalaye, L. Baker, and S. Marques, *A note on the multiplicative structure of* \(\mathbb Z/p^e\mathbb Z\), arXiv:2408.06278 (first public 2024-08-12). https://arxiv.org/abs/2408.06278
