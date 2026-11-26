# Two-eigenspace subalgebra permutability and its finite-field limits

## Finding and scope

For any prime power \(q\) and fixed integers \(a,b\ge2\), let \(L=\mathbb F_q h\oplus E\oplus F\) with \(\dim E=a\), \(\dim F=b\), and sole nonzero brackets \([h,e]=e\) for \(e\in E\) and their alternating counterparts. Write \(V=E\oplus F\) and \(n=a+b\). Two subalgebras permute when their vector-space sum is a subalgebra, equivalently when their mutual brackets belong to that sum. Count all subalgebras and all ordered pairs (including repetitions, zero, and the whole algebra). The counts \(T_{a,b}(q)\) of subalgebras and \(P_{a,b}(q)\) of permuting pairs are given below. With \(a,b\) fixed,
\[
\lim_{q\to\infty}\frac{P_{a,b}(q)}{T_{a,b}(q)^2}=
\begin{cases}2/5,&a=b=2,\\7/16,&\{a,b\}=\{2,3\},\\1,&\text{otherwise}.\end{cases}
\]
The limit is over prime powers, and the census includes characteristic two. For \(a=b=2\), the finite counts simplify to
\[
T_{2,2}(q)=5q^4+7q^3+9q^2+5q+6,\qquad
T_{2,2}(q)^2-P_{2,2}(q)=q^2(q^2-1)(15q^4+24q^3+18q^2+6q+1).
\]

## Exact census

Let \(G_q(d,j)\) count \(j\)-subspaces of \(\mathbb F_q^d\), equal to zero outside \(0\le j\le d\). Set
\[
H_n(q)=\sum_{j=0}^n G_q(n,j),\quad
B_{a,b}(q)=\sum_{p=0}^a\sum_{z=0}^b G_q(a,p)G_q(b,z)q^{n-p-z},\quad
R_q(w,d)=\sum_{j=0}^w G_q(w,j)q^{d(w-j)}.
\]
The subtotal with a prescribed order of one inside and one outside subalgebra is
\[
M_{a,b}(q)=\sum_{p=0}^a\sum_{z=0}^b G_q(a,p)G_q(b,z)q^{n-p-z}
\sum_{i=0}^{a-p}\sum_{j=0}^{b-z}G_q(a-p,i)G_q(b-z,j)R_q(p+z,i+j).
\]
For \(C_q(d;u,v,t)=G_q(d,u)G_q(u,t)G_q(d-u,v-t)q^{(u-t)(v-t)}\), set
\[
\begin{aligned}
Q_{a,b}(q)&=\sum_{p,p'=0}^a\sum_{z,z'=0}^b\sum_{t,s\ {\rm admissible}}
C_q(a;p,p',t)C_q(b;z,z',s)\\
&\qquad\cdot q^{n-p-z-p'-z'+k}\left(q^{a-k_E}+q^{b-k_F}-1\right),
\end{aligned}
\]
where \(\max(0,p+p'-a)\le t\le\min(p,p')\), \(\max(0,z+z'-b)\le s\le\min(z,z')\), \(k_E=p+p'-t\), \(k_F=z+z'-s\), and \(k=k_E+k_F\). Then
\[
T_{a,b}=H_n+B_{a,b},\qquad P_{a,b}=H_n^2+2M_{a,b}+Q_{a,b}.
\]

## Proof of the census

Let \(D=\operatorname{ad}(h)|_V\), the projection onto \(E\) with kernel \(F\). Every subspace of \(V\) is a subalgebra. Each subalgebra not contained in \(V\) has a unique form \(\mathbb F_q(h+v)\oplus W\) with \(W=P\oplus Z\), \(P\le E, Z\le F\), and parameter \(v+W\in V/W\). In fact closure is precisely \(DW\subseteq W\), and such a space splits since \(D\) and \(I-D\) are its complementary projections. Choosing \(P,Z\) and the coset gives \(B_{a,b}\). Pairs inside \(V\) contribute \(H_n^2\).

For a mixed pair with inside subspace \(U\), the sum is a subalgebra precisely when \(Y=U+W\) is invariant. Invariant superspaces \(Y\) are chosen by extending \(P,Z\) by dimensions \(i,j\), respectively. For fixed \(Y\) with \(d=\dim Y/W\), put \(w=\dim W\). After choosing a \(\ell\)-space \(K=U\cap W\), choose the graph of a map \(Y/W\to W/K\), using any fixed splitting of \(Y/K\). This gives \(q^{d(w-\ell)}\) choices and yields \(M_{a,b}\) in each orientation.

Two subalgebras not contained in \(V\), with parameters \(v+W\) and \(v'+W'\), sum to \(\mathbb F_q(h+v)\oplus (W+W'+\mathbb F_q(v'-v))\). Their sum is closed if and only if the image of \(v'-v\) in \(V/(W+W')\) is zero or spans an invariant line. In the quotient the eigenspace dimensions are \(a-k_E\) and \(b-k_F\); their union contains exactly \(q^{a-k_E}+q^{b-k_F}-1\) allowed vectors. The map from pairs of cosets to that quotient difference is onto, with each fiber of size \(q^{n-\dim W-\dim W'+k}\). For the ordered pairs of subspaces of dimensions \(u,v\) with intersection dimension \(t\) in a \(d\)-space, first choose the \(u\)-space, then the \(t\)-space in it, then the projected \((v-t)\)-space in the quotient. After quotienting by the intersection, lifts are graphs with \(q^{(u-t)(v-t)}\) choices. This proves the factor \(C_q\) and the formula for \(Q_{a,b}\).

For the special case the Gaussian coefficients give
\[
H_4=q^4+3q^3+4q^2+3q+5,\qquad B_{2,2}=(2q^2+q+1)^2.
\]
The same substitution into \(2(H_4B_{2,2}-M_{2,2})+(B_{2,2}^2-Q_{2,2})\) gives the displayed defect polynomial.

## Proof of the limits

A Gaussian coefficient has degree \(j(d-j)\) and leading coefficient one. The degrees of \(H_n\) and \(B_{a,b}\) are \(\lfloor n^2/4\rfloor\) and \(n+\lfloor(a-1)^2/4\rfloor+\lfloor(b-1)^2/4\rfloor\), respectively. With \(A=a-1, B=b-1\), their difference is \(\lfloor(A+B)^2/4\rfloor-\lfloor A^2/4\rfloor-\lfloor B^2/4\rfloor-1\). For at least one of \(A,B\) even this equals \(\lfloor AB/2\rfloor-1\); when both are odd it equals \((AB-1)/2\). Thus the difference vanishes only at \((a,b)=(2,2),(2,3),(3,2)\), and is positive otherwise. In the positive range, two uniform independent subalgebras are both in the abelian ideal with probability tending to one.

For the exceptional cases, only degree-maximizing types contribute to the limiting probability. For a fixed outside component \(W\), a uniform inside subspace of dimension \(m\) has image in \(V/W\) of the generic dimension \(\min(m,n-\dim W)\) with probability tending to one, by the intersection count \(C_q\) (the minimum intersection term alone reaches the full degree). The image is uniform among subspaces of that dimension by invariance under the stabilizer of \(W\). If the quotient has two positive eigen-dimensions \(e,f\), a proper nonzero subspace of dimension \(d\) is invariant with probability tending to zero: a split type \((i,j)\), \(i+j=d\), loses \(i(f-j)+j(e-i)>0\) degrees relative to the full Grassmannian. For two outside components, the two eigenspace sums generically have maximal dimension, again by the intersection count; given these components the quotient difference is uniform. It is allowed with limiting probability one if a quotient eigenspace is zero, and otherwise with limiting probability zero (fraction \(q^{-e}+q^{-f}-q^{-e-f}\)).

At \((2,2)\) the leading types, each with coefficient one, are the inside dimension two and the four outside types \((p,z)\in\{0,1\}^2\). The limiting allowed type pairs consist of the inside–inside pair, the two oriented mixed pairs with outside type \((1,1)\), and seven ordered outside pairs (four generically fill \(E\), four fill \(F\), and one does both). This gives \(10/25\). At \((2,3)\) the leading types are inside dimensions two and three, and outside types \((0,1),(1,1)\). There are four inside–inside pairs, two oriented mixed pairs (dimension three with \((1,1)\)), and one outside–outside pair (both of type \((1,1)\), filling \(E\)). This gives \(7/16\).

Interchanging \(E,F\) replaces \(D\) by \(I-D\). For \(x=\alpha h+v\), \(y=\beta h+w\) the **sum** of the two bracket values \([x,y]_D+[x,y]_{I-D}\) equals \(\alpha y-\beta x\). For every subspace containing \(x,y\), either both bracket values belong to the subspace or neither does. This preserves subalgebras and permutability, giving the result also at \((3,2)\).

## Verification and context

The original standard-library `artifacts/verify.py` tests the formulas against direct ordered-pair bracket containment for several small prime-field cases, including \((a,b,q)=(2,2,2),(2,2,3)\) with \((T,P)=(188,29140),(696,337248)\). See `artifacts/verification_output.txt`. These are finite checks; the proofs above are field-independent.

[Muhie–Otera–Russo](https://arxiv.org/abs/2609.19086v1) define the degree and study selected families. [Rank-one central stabilizations](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-parity-phase-transition-for-subalgebra-permutability-in-centrall--409c328075cb), [three-dimensional plane counts](https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-plane-counts-control-subalgebra-commutativity-dimension-three--0c4c7f02cc9c), and [scalar-shift invariance in the Jordan-chain setting](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-subalgebra-permutability-and-a-rank-threshold-for-jordan-c--2ca07ad52f23) are separate known results. The new census and limit classify the higher-rank split case: they quantify exactly when the abelian ideal does and does not dominate the pair distribution. They do not treat arbitrary nonsplit actions or simultaneous variation of \(q,a,b\). Historical priority beyond the compared statements is not certified.
