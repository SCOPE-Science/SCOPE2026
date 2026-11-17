# Joint rank spectra of commuting square-zero derivations on truncated polynomial algebras

## Finding

Let \(k\) be a field of characteristic \(2\), \(m\ge1\), and \(N\in\{2m,2m+1\}\). Set \(A_N=k[t]/(t^N)\) and \(W_N=\operatorname{Der}_k(A_N)\). For every integer \(r\ge1\), define the restricted commuting-tuple locus
\[
\mathcal C_r(N)=\{(D_1,\ldots,D_r)\in W_N^r:D_i^2=0,\ [D_i,D_j]=0\text{ for all }i,j\}.
\]
Put \(B=k[s]/(s^m)\), \(c=\lceil m/2\rceil\), and \(\ell=\lfloor m/2\rfloor\). There is a canonical coefficient identification \(W_N\cong B\oplus B\), written \((a,b)\), specified below. For every \(j=c,\ldots,m\), define the \(m\)-dimensional linear space
\[
L_j=\{(a,b):a\in s^{m-j}B,\ b\in s^jB\}.
\]
The reduced variety of \(\mathcal C_r(N)\) over every field of characteristic two is precisely
\[
\boxed{\mathcal C_r(N)_{\mathrm{red}}=\bigcup_{j=c}^{m} L_j^r.}
\]
These are exactly its \(\ell+1\) geometrically irreducible components, each of dimension \(mr\); for \(c\le i<j\le m\), their intersection has dimension \(r(m-j+i)\). In particular **every commuting tuple of square-zero derivations lies in one common abelian linear subspace** \(L_j\). This assertion concerns the reduced variety and makes no claim of reducedness for the defining equation scheme.

For \(q=2^e\) with \(e\ge1\), write \(\rho(D)=\operatorname{rank}_k(D:A_N\to A_N)\). For \(j=c,\ldots,m\) and \(0\le h\le m\), put
\[
 F_{j,q}(h)=q^{\min(j,h)+\min(m-j,h)},\qquad
 G_{j,q}(h)=q^{\min(j-1,h)+\min(m-j,h)}\quad(j>c).
\]
Set \(F_{j,q}(-1)=G_{j,q}(-1)=0\), and define rank polynomials
\[
P_{j,q}(z)=\sum_{h=0}^{m}(F_{j,q}(h)-F_{j,q}(h-1))z^h,
\]
\[
Q_{j,q}(z)=\sum_{h=0}^{m}(G_{j,q}(h)-G_{j,q}(h-1))z^h\quad(j>c).
\]
Then the **complete joint rank generating polynomial** is
\[
\boxed{\sum_{(D_1,\ldots,D_r)\in\mathcal C_r(N)(\mathbb F_q)}
 \prod_{i=1}^r z_i^{\rho(D_i)}
 =\sum_{j=c}^{m}\prod_{i=1}^r P_{j,q}(z_i)
 -\sum_{j=c+1}^{m}\prod_{i=1}^r Q_{j,q}(z_i).}
\]
Consequently the total count and its all-arity generating function (including the one empty tuple at \(r=0\)) are
\[
\boxed{\#\mathcal C_r(N)(\mathbb F_q)
 =(\ell+1)q^{mr}-\ell q^{(m-1)r}},\qquad
\boxed{\sum_{r\ge0}\#\mathcal C_r(N)(\mathbb F_q)u^r
 =\frac{\ell+1}{1-q^m u}-\frac{\ell}{1-q^{m-1}u}}.
\]
The geometric component arrangement, entire joint-rank polynomial, and counts are **identical** for the adjacent truncation lengths \(2m\) and \(2m+1\).

## Assumptions and scope

Throughout, \(k\) is an arbitrary field of characteristic two, \(N\ge2\), and \(m=\lfloor N/2\rfloor\). All ranks are ordinary \(k\)-vector-space ranks on \(A_N\), not Lie-adjoint ranks. For \(N=2m\), any derivation is uniquely \(D(t)=a(t^2)+t b(t^2)\), where \(a,b\in B\). For \(N=2m+1\), the relation \(D(t^N)=0\) forces the constant term of \(D(t)\) to vanish, and any derivation is uniquely \(D(t)=t^2a(t^2)+t b(t^2)\), again with \(a,b\in B\). These are coefficient identifications, not natural algebra isomorphisms between the truncated rings. No derivations are required to commute with any additional distinguished endomorphism.

The schemes are defined by the original polynomial equations \(D_i^2=0\) and \([D_i,D_j]=0\); geometric statements refer only to their reductions, whereas all point counts are for finite fields. At \(r=0\) only the total count is asserted, not a component decomposition.

## Proof

**1. Derivation and restricted-square identities.** In characteristic two, \(D(t^{2j})=0\) and \(D(t^{2j+1})=t^{2j}D(t)\). In either coefficient identification above, the square of \(D=(a,b)\) is zero if and only if
\[
 ab=0,\qquad b^2=0\quad\text{in }B.
\]
For two derivations \(D=(a,b)\) and \(E=(a',b')\), direct substitution in \([D,E](t)=D(E(t))+E(D(t))\) gives
\[
[D,E]=0\quad\Longleftrightarrow\quad ab'+a'b=0\quad\text{in }B.
\]
For odd \(N\), the even contribution to the bracket is multiplied by \(t^2\), which is an injective coefficient shift \(B\to t^2k[t^2]/(t^{2m+1})\); therefore the same equations hold exactly. Both identities arise from the original derivation action on the generator and are necessary and sufficient since derivations are determined by their action on \(t\).

**2. Valuation rigidity.** In \(B\), put \(\nu(0)=m\) and \(\nu(s^ju)=j\) when \(u\) is a unit. The square-zero condition \(b_i^2=0\) forces \(b_i\in s^cB\), as the leading nonzero coefficient cannot square to zero in a field. Set \(\alpha=\min_i\nu(a_i)\). If all \(a_i=0\), the entire tuple lies in \(L_c^r\). Otherwise choose \(k\) with \(\nu(a_k)=\alpha<m\). From \(a_kb_k=0\) follows \(b_k\in s^{m-\alpha}B\). Since every \(a_i\in s^\alpha B\), we have \(a_i b_k=0\). The commutation equation then implies \(a_k b_i=0\), so every \(b_i\in s^{m-\alpha}B\). Taking \(j=\max(c,m-\alpha)\), we obtain \(a_i\in s^{m-j}B\) and \(b_i\in s^jB\) for every \(i\). Hence the tuple belongs to \(L_j^r\). Conversely, for any fixed \(j\ge c\), all products \(a_i b_h\) and \(b_i b_h\) vanish, so every tuple in \(L_j^r\) satisfies the defining conditions.

**3. Components and intersections.** Each \(L_j\) is a linear \(m\)-space: its \(a\)-coordinate has dimension \(j\), and its \(b\)-coordinate has dimension \(m-j\). If \(i<j\), the intersection has \(a\in s^{m-i}B\) and \(b\in s^jB\), hence dimension \(m-j+i\); taking the \(r\)-fold Cartesian power multiplies this dimension by \(r\). For \(j<m\), the point \((s^{m-j},s^j)\) belongs to \(L_j\) and to no other \(L_h\); for \(j=m\), use \((1,0)\). Thus none of these geometrically irreducible linear spaces is contained in another. Their union is exactly the underlying set over every extension field, proving the claim about the reduced variety and its components.

**4. Rank and finite-field enumerators.** The derivation sends its odd-polynomial input \(t\,v(t^2)\) to \(D(t)v(t^2)\) and kills the even-polynomial input. In both parity cases, the resulting multiplication map is linearly equivalent to
\[
 B\longrightarrow B\oplus B,\qquad v\longmapsto(av,bv).
\]
Its kernel is the annihilator of the ideal \((a,b)=(s^{\min(\nu(a),\nu(b))})\); therefore
\[
\rho(D)=m-\min(\nu(a),\nu(b)).
\]
For \(L_j\), having rank at most \(h\) is equivalent to \(a,b\in s^{m-h}B\), so its cardinality is \(F_{j,q}(h)\). The neighboring intersection \(L_{j-1}\cap L_j\) similarly gives \(G_{j,q}(h)\). Taking consecutive differences yields exactly the rank-polynomial coefficients above.

Finally, as \(j\) increases, the intersection of \(L_j^r\) with the union of its predecessors equals \((L_{j-1}\cap L_j)^r\), because all earlier intersections are nested inside this one. Thus adding the components in order gives the displayed product-minus-product multivariate polynomial. Its specialization at all \(z_i=1\) counts one \(q^{mr}\)-sized component plus \(\ell\) components, each contributing \(q^{mr}-q^{(m-1)r}\). Summing the resulting two exponentials over \(r\ge0\) yields the rational generating function. All arguments are valid in every characteristic-two field and do not depend on the cardinality of \(k\).

## Verification

The standalone script `check_commuting_derivations.py` reconstructs \(D(t^j)\) on the actual basis \(1,t,\ldots,t^{N-1}\), multiplies the resulting finite-field matrices, checks \(D^2=0\), and compares the original commutator equations against common-component membership. It then enumerates commuting ordered tuples of lengths up to four using only the directly verified matrix-commutation relation. Independent row reduction calculates individual ranks and compares entire tuple-rank histograms with the stated multivariate formula.

Its finite-field implementation covers \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\) with explicit irreducible binary polynomials. For example, at \(q=2\) the numbers of commuting \(r\)-tuples for \(r=1,2,3\) are respectively \((6,28,120)\) at \(N=4,5\), \((12,112,960)\) at \(N=6,7\), and \((32,640,11264)\) at \(N=8,9\). At \(q=4\), the corresponding counts at \(N=4,5\) are \((28,496,8128)\). All checked configurations, including full rank-vector histograms for selected dimensions, passed. Run with `python3 check_commuting_derivations.py`; the captured output is in `CHECKS.txt`.

The finite computations are checks of specific instances; the proof of the unrestricted theorem is the valuation and intersection argument above.

## Relationship to prior work

Evans and Fuchs (2001, arXiv:math/0111271) study the restricted \(p\)-operator on the ordinary \(p\)-dimensional Witt algebra. Yao and Chang (2013, arXiv:1301.5667) study nilpotent commuting pairs for the Witt algebra under \(p>3\), while Yao's 2015 paper studies higher tuples in that setting. Ngo (2014, arXiv:1401.6820) addresses commuting restricted nilpotent tuples in classical Lie algebras. Those domains and conclusions do not give the present characteristic-two, arbitrary-truncation, finite-field **joint rank distribution**. Carlson, Friedlander and Pevtsova (2011, arXiv:1106.4474) motivate rank data for representations of truncated polynomial algebras, but do not count this family of derivation tuples.

A previously established result for these characteristic-two truncated polynomial rings gives the single-operator square-zero component arrangement and its univariate point count. Those individual components and the one-operator count are background, not asserted as separately new here. The assessed contribution is the common-component rigidity for commuting tuples together with the complete multivariate joint rank enumeration for every tuple length and both parity classes; the unrefined all-arity count is a specialization. No claim is made that finite-field searches alone prove historical uniqueness.

## Limitations

Only characteristic two, the rings \(k[t]/(t^N)\), and ordered tuples of ordinary derivations satisfying both square-zero and pairwise-commutation conditions are included. The theorem does not classify automorphism-conjugacy orbits, arbitrary nilpotent derivations, higher restricted nilpotence, indecomposable module types, or nonreduced scheme structures. The full text of Yao's 2015 arbitrary-tuple Witt paper was not accessible in the checked sources; its published scope assumes \(p>3\) and it remains a priority-comparison risk. Independent external validation is not claimed.

## References

- Tyler J. Evans and Dmitry Fuchs, *On the Restricted Lie Algebra Structure for the Witt Lie Algebra in Finite Characteristic*, arXiv:math/0111271v1, first public 2001-11-27. https://arxiv.org/abs/math/0111271
- Yu-Feng Yao and Hao Chang, *Nilpotent commuting varieties of the Witt algebra*, arXiv:1301.5667v1, first public 2013-01-23. https://arxiv.org/abs/1301.5667
- Yu-Feng Yao, *On nilpotent commuting varieties of r-tuples in the Witt algebra*, J. Pure Appl. Algebra 219 (2015), 4042–4054. https://doi.org/10.1016/j.jpaa.2015.02.005
- Nham V. Ngo, *On nilpotent commuting varieties and cohomology of Frobenius kernels*, arXiv:1401.6820v1, first public 2014-01-27. https://arxiv.org/abs/1401.6820
- Jon F. Carlson, Eric M. Friedlander and Julia Pevtsova, *Representations of elementary abelian p-groups and bundles on Grassmannians*, arXiv:1106.4474v1, first public 2011-06-22. https://arxiv.org/abs/1106.4474
