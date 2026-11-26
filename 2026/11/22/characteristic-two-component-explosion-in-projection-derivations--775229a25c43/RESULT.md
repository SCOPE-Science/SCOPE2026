# Idempotent derivations of rectangular-band algebras: rank distributions and geometric components

## Finding
Let \(m,n\ge2\), let \(k\) be a field, and let \(A=k[S_{m,n}]\), where \((i,j)(h,l)=(i,l)\). We consider ordinary \(k\)-linear derivations with \(D^2=D\) under composition. Put \(b=n-1\) and \(c=m-1\). After choosing a band element \(e\), one has an adapted split \(A=ke\oplus B\oplus C\oplus(C\otimes B)\) with \(\dim B=b\), \(\dim C=c\), and only the following nonzero products of homogeneous types: \(e^2=e\), \(ev=v\), \(ue=u\), and \(uv=u\otimes v\) for \(v\in B,u\in C\). This split is not asserted to be canonical. The associated ranks below are intrinsic: \(s\) is the rank induced on \(\{x:xA=0\}/W\), \(t\) the rank on \(\{x:Ax=0\}/W\), where \(W\) is the intersection of these two annihilators.

In the adapted split every derivation is uniquely given by \(S\in\operatorname{End}(B),T\in\operatorname{End}(C),v_0\in B,u_0\in C\) as follows:
\[
\begin{aligned}
D(e)&=v_0+u_0,&D(v)&=S(v)+u_0\otimes v,\\
D(u)&=T(u)+u\otimes v_0,&D(u\otimes v)&=T(u)\otimes v+u\otimes S(v).
\end{aligned}
\]
It is idempotent exactly when \(S^2=S,T^2=T,S(v_0)=v_0,T(u_0)=u_0\) and either \(\operatorname{char}k=2\) or at least one of \(S,T\) is zero. In this notation \(s=\operatorname{rank} S\), \(t=\operatorname{rank} T\).

For \(k=\mathbb F_q\), let \(\mathcal P_{m,n,q}(z)\) count the derivations in question with weight \(z^{\operatorname{rank}D}\), including the zero map. In characteristic two and in odd characteristic respectively it is
\[
\mathcal P_{m,n,q}(z)=\sum_{s=0}^b\sum_{t=0}^c {b\brack s}_q{c\brack t}_q q^{s(b-s)+t(c-t)+s+t}z^{sm+tn-2st},
\]
\[
\mathcal P_{m,n,q}(z)=\sum_{s=0}^b{b\brack s}_q q^{s(n-s)}z^{sm}+\sum_{t=1}^c{c\brack t}_q q^{t(m-t)}z^{tn}.
\]
Here \({a\brack i}_q\) counts \(i\)-dimensional subspaces of \(\mathbb F_q^a\). The binary \(2\)-by-\(3\) and \(2\)-by-\(2\) polynomials are \(1+12z^2+34z^3+4z^4\) and \(1+8z^2\), respectively; the odd-field \(2\)-by-\(2\) polynomial is \(1+2qz^2\).

Over an algebraic closure the reduced solution locus has exactly \(mn\) smooth irreducible components in characteristic two, and \(m+n-1\) in other characteristics. The components are indexed by the allowed \((s,t)\); the dimension is \(2s(b-s)+2t(c-t)+s+t\). Each is a vector bundle of rank \(s+t\) over the corresponding product of fixed-rank idempotent-matrix varieties.

## Assumptions and scope
The algebra is the full \(mn\)-dimensional semigroup algebra, not generally unital. The Leibniz rule is \(D(xy)=D(x)y+xD(y)\); idempotence is an operator identity, not an equation on algebra elements. Rank in the polynomial is taken on the whole algebra. Finite-field formulas hold for every indicated prime power; the classification applies to arbitrary fields. Geometric assertions concern the reduced locus only.

## Proof
Write \(R=k^m,F=k^n\) with coordinate summation maps \(\epsilon_R,\epsilon_F\). In the band basis the algebra is \(R\otimes F\) with product \((r\otimes f)(r'\otimes f')=\epsilon_F(f)\epsilon_R(r')r\otimes f'\). Choose the basis vectors \(r_0,f_0\) for the row and column of \(e=r_0\otimes f_0\). Put \(R_0=\ker\epsilon_R\), \(F_0=\ker\epsilon_F\). The tensor expansions of \(R=kr_0\oplus R_0\) and \(F=kf_0\oplus F_0\) give \(B=kr_0\otimes F_0\), \(C=R_0\otimes kf_0\) and \(W=R_0\otimes F_0\cong C\otimes B\), with exactly the asserted product table. From that table \(B\oplus W=\{x:xA=0\}\), \(C\oplus W=\{x:Ax=0\}\). Derivations preserve these annihilators by the Leibniz rule and hence also their intersection. Thus \(S,T\) will represent canonical quotient actions even though the splittings depend on \(e\).

Differentiating \(e^2=e\) forces \(D(e)\in B\oplus C\). The two equations \(ev=v,ve=0\) then force the displayed \(D(v)\); the equations \(ue=u,eu=0\) force \(D(u)\); differentiating \(uv=u\otimes v\) forces \(D\) on \(W\). For sufficiency define \(P:R\to R_0\) by \(P(r_0)\otimes f_0=u_0\) and \(P|_{R_0}=T\) under the indicated identification. Define \(Q:F\to F_0\) by \(r_0\otimes Q(f_0)=v_0\) and \(Q|_{F_0}=S\). Then the proposed map is \(P\otimes I_F+I_R\otimes Q\). This satisfies Leibniz on pure tensors by the product formula: the two possible cross terms vanish by \(\epsilon_R P=0\) and \(\epsilon_F Q=0\). Uniqueness follows by comparing components.

Idempotence forces the displayed projection and fixed-vector conditions by its \(B,C\) components on \(e,B,C\); these conditions are equivalent to \(P^2=P,Q^2=Q\). With these in place the remaining equation is \(D^2-D=2P\otimes Q=0\). A tensor product of nonzero maps over a field is nonzero, and under the fixed-vector conditions \(P=0\) exactly when \(T=0\), and \(Q=0\) exactly when \(S=0\). This proves the classification in every characteristic.

The ranks of the projections \(P,Q\) on \(R,F\) are \(t,s\); their images already come from \(R_0,F_0\) because \(u_0\in\operatorname{im}T,v_0\in\operatorname{im}S\). Split each vector space into projection image and kernel. The operator \(D\) acts there by the sums of the two eigenvalues, each either zero or one. In characteristic two its rank is \(t(n-s)+(m-t)s=sm+tn-2st\); in other characteristics one projection is zero and its rank is \(sm\) or \(tn\). There are \({b\brack s}_q q^{s(b-s)}\) choices of \(S\), by choosing the image and a complementary kernel, followed by \(q^s\) choices of \(v_0\); the choices for \(T,u_0\) are analogous. This yields the formulas without double counting the zero map.

For the reduced locus, a fixed-rank projection variety is equivalently the open subset of the product of two Grassmannians where the subspaces are complementary. It is smooth and irreducible, of dimension \(2s(b-s)\) for \(S\) and \(2t(c-t)\) for \(T\). The allowed vectors form the sum of the tautological image bundles. For a family of idempotents, the rank is locally constant: the inequalities for ranks of the idempotent and its complement give opposite semicontinuities. Hence the rank strata are open and closed. Their vector bundle descriptions show they are the irreducible components and give the dimension and counts.

## Verification
The original accompanying Python checker specifies direct product/Leibniz and idempotence checks on small algebras with \((m,n,p)=(2,2,2),(2,2,3),(2,2,5),(2,3,2),(3,2,2)\), and an exhaustive direct test of the \(2^{16}\) linear maps of the binary \(2\)-by-\(2\) algebra. The latter count is 16 derivations and 9 composition-idempotent derivations, including zero. The choice-relative clarification does not change any of the test identities or rank counts. The all-field and geometric results are proved above independently of finite tests.

## Relationship to prior work and limitations
Drozd–Plakosh, *Representations of Munn algebras and related semigroups*, arXiv:2202.06103, Definition 1.1 and Proposition 1.3, give the sandwich construction and its normalization. Yu–Luo–Li, *Zero product and zero Jordan product determined Munn algebras*, arXiv:2407.00892, Definition 1.2 and Theorem 2.2, study that construction and generation by idempotent algebra elements, not composition-idempotent derivations. Commutator-rank censuses and commutator-fiber counts for rectangular-band algebras measure pairs of algebra elements rather than derivation operators. Results on projection derivations of free two-step, truncated local polynomial, and upper triangular algebras are related but concern other multiplication laws. The present classification concerns the rank-one rectangular-band sandwich class, not higher sandwich rank. No assertion of global priority or of nonreduced scheme structure is made.
