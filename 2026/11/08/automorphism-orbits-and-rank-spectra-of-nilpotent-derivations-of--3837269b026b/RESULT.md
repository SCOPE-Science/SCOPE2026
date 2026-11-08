# Automorphism orbits and rank spectra of nilpotent derivations of Kronecker path algebras

## Finding

Let \(k\) be any field of characteristic \(p>0\), let \(m\ge2\), and let \(A_m=ke\oplus kf\oplus V\), where \(\dim_k V=m\), with nonzero products \(e^2=e\), \(f^2=f\), and \(ev=v=vf\) for \(v\in V\). Thus \(A_m\) is the path algebra of the two-vertex quiver with \(m\) parallel arrows. A derivation \(D\) is called \(p\)-nilpotent when \(D^p=0\) as a \(k\)-linear endomorphism of \(A_m\).

**Theorem (one classification with orbit and rank refinements).** Every derivation is uniquely given by a pair \((T,w)\in\operatorname{End}_k(V)\times V\) through
\[
D(e)=w,\qquad D(f)=-w,\qquad D(v)=T(v).
\]
It is \(p\)-nilpotent exactly when \(T^p=0\) and \(T^{p-1}w=0\). Under conjugation by \(\operatorname{Aut}_k(A_m)\), the \(p\)-nilpotent derivations are classified, over **every** field \(k\) of characteristic \(p\), by the following data: a partition \(\lambda\vdash m\) whose parts are at most \(p\), together with either the label \(0\) or one of the distinct part sizes \(j<p\) that occur in \(\lambda\). No two such labels give the same orbit, and each label is realized.

Write \(O_{m,p}\) for the number of these conjugacy orbits. The exact generating series, with the first two formal terms removed to match the stipulated range \(m\ge2\), is
\[
\boxed{\sum_{m\ge2}O_{m,p}z^m
=\frac{1}{(1-z)^2\prod_{j=2}^{p-1}(1-z^j)}-1-2z.}
\]
The empty product is \(1\). In particular \(O_{m,2}=m+1\), independent of the size or algebraic closedness of \(k\).

When \(k=\mathbb F_q\), with \(q\) a power of \(p\), the theorem also gives the **number of individual derivations at every linear-map rank** and the size of every automorphism orbit. Define \(c_j(\lambda)\) as the multiplicity of part size \(j\) in \(\lambda\), \(b_j(\lambda)=\sum_{i=1}^j c_i(\lambda)\), \(b_0=0\), and \(r(\lambda)=m-\sum_{j=1}^p c_j(\lambda)\). Put
\[
C_\lambda(q)=q^{\sum_{i=1}^p (\lambda_i')^2}
\prod_{j=1}^p\prod_{h=1}^{c_j(\lambda)}(1-q^{-h}),\qquad
B_\lambda(q)=\frac{|\operatorname{GL}_m(\mathbb F_q)|}{C_\lambda(q)}.
\]
Here \(\lambda'\) is the conjugate partition, and \(C_\lambda(q)\) is the order of the invertible centralizer of a nilpotent matrix of type \(\lambda\). The orbit with label \(0\) has size \(B_\lambda(q)q^{r(\lambda)}\) and consists of rank-\(r(\lambda)\) derivations. For any occurring label \(j<p\), its orbit has size
\[
\boxed{B_\lambda(q)q^{r(\lambda)}
\bigl(q^{b_j(\lambda)}-q^{b_{j-1}(\lambda)}\bigr),}
\]
and every derivation in it has rank \(r(\lambda)+1\). Accordingly the exact rank-enumerator is
\[
\boxed{F_{m,q}(z)=\sum_{\substack{\lambda\vdash m\\\lambda_1\le p}}
B_\lambda(q)\left[q^{r(\lambda)}z^{r(\lambda)}+
\bigl(q^{m-c_p(\lambda)}-q^{r(\lambda)}\bigr)z^{r(\lambda)+1}\right].}
\]
The coefficient of \(z^s\) is the number of \(p\)-nilpotent derivations of rank \(s\) on the \((m+2)\)-dimensional algebra \(A_m\), including the zero derivation.

## Assumptions and scope

The ground field has characteristic \(p>0\), where \(p\) is prime. For the orbit classification it need not be finite, perfect, or algebraically closed. The quiver has exactly two vertices, all \(m\) arrows point in the same direction, and \(m\ge2\). The rank is the rank of the endomorphism \(D:A_m\to A_m\), not the rank of the linear part \(T:V\to V\). Automorphism orbits mean conjugation by **all unital algebra automorphisms**, not merely arrow-basis changes or conjugacy of the \(T\) matrices. The phrase \(p\)-nilpotent uses the ordinary \(p\)-fold composition, not nilpotence of the adjoint representation.

## Proof

**Step 1 (all derivations and all automorphisms).** Differentiate the idempotent identities \(e^2=e\), \(f^2=f\), the relation \(e+f=1\), and the bimodule identities \(ev=v=vf\), \(ve=fv=0\). The idempotent derivatives have no vertex components, and \(D(f)=-D(e)\). As \(V\) is the unique radical, the bimodule identities force \(D(V)\subseteq V\). Conversely, any displayed \((T,w)\) satisfies the Leibniz rule on the basis, including the zero products. Hence the parametrization is exact.

The two primitive-idempotent classes cannot be interchanged: \(eA_m f=V\) has dimension \(m\), whereas \(fA_m e=0\). Every automorphism is consequently of the form
\[
\phi_{G,u}(e)=e+u,\quad\phi_{G,u}(f)=f-u,\quad
\phi_{G,u}(v)=Gv,\qquad G\in\operatorname{GL}(V),\ u\in V.
\]
One checks the defining multiplication directly. Its conjugation action on pairs has the same orbit structure as
\[
(T,w)\longmapsto (GTG^{-1},\; Gw+GTG^{-1}u),
\]
because \(G\) and \(u\) run through all their allowed values.

**Step 2 (restricted nilpotence).** For every integer \(a\ge1\), \(D^a(v)=T^a v\), \(D^a(e)=T^{a-1}w\), and \(D^a(f)=-T^{a-1}w\). Therefore \(D^p=0\) if and only if \(T^p=0\) and \(T^{p-1}w=0\). In characteristic \(p\), composition \(D^p\) is again a derivation, as expected from the restricted Lie algebra structure, but this general fact is not needed for the equivalence.

**Step 3 (translation quotient).** Fix the similarity class of \(T\). The vector translations by \(u\) identify \(w\) modulo \(TV\). Since \(T^p=0\), the subspace \(TV\) is contained in \(\ker T^{p-1}\). Hence the remaining classification is the action of the invertible centralizer \(Z_{\operatorname{GL}(V)}(T)\) on
\[
W_T=\ker T^{p-1}/TV.
\]
For a nilpotent Jordan type \(\lambda\) with all parts at most \(p\), regard \(V\) as the \(k[t]\)-module \(\bigoplus_{j=1}^{p}(k[t]/t^j)^{c_j(\lambda)}\), where \(t\) acts as \(T\). Each summand of size \(p\) contributes nothing to \(W_T\), and each smaller block contributes one class of its cyclic generator. Thus
\[
W_T\cong\bigoplus_{j=1}^{p-1}k^{c_j(\lambda)}.
\]
A \(k[t]\)-linear map from a length-\(a\) cyclic block to a length-\(b\) block can have a nonzero constant coefficient on the quotient by \(t\) exactly when \(b\le a\). Consequently the invertible centralizer induces the complete block-triangular group (relative to increasing block lengths) on \(W_T\): arbitrary invertible diagonal blocks and arbitrary maps from longer-block tops to shorter-block tops. Every permitted elementary block map lifts to an invertible \(k[t]\)-module map (use identity plus a one-way off-diagonal map), establishing surjectivity onto this triangular group.

It follows that the zero vector is one orbit, while any nonzero vector is equivalent to a basis vector in its **largest** nonzero block-length component. This largest length \(j<p\) is invariant because the sum of components of lengths \(\le j\) is stable. Hence there is exactly one further orbit for each occurring part size \(j<p\), and the partition-plus-label classification is both exhaustive and disjoint. Nilpotent Jordan form and the required centralizer operations work over every field because the only elementary divisor is \(t\).

**Step 4 (orbit generating function).** For a fixed partition \(\lambda\), the number of orbits is \(1+\#\{j<p:c_j(\lambda)>0\}\). Summing the indicator of each occurring part size across partitions of \(m\) with parts at most \(p\) yields
\[
\sum_{m\ge0}O_{m,p}z^m
=\frac{1+\sum_{j=1}^{p-1}z^j}{\prod_{j=1}^p(1-z^j)}
=\frac{1}{(1-z)^2\prod_{j=2}^{p-1}(1-z^j)}.
\]
The two coefficients \(O_{0,p}=1\) and \(O_{1,p}=2\) here are combinatorial boundary conventions and also follow from the same derivation calculation; subtracting them gives the asserted series for \(m\ge2\).

**Step 5 (finite-field sizes and rank).** The number of matrices \(T\) of Jordan type \(\lambda\) is \(B_\lambda(q)\), the standard general-linear similarity-class formula. For each such \(T\), \(\dim TV=r(\lambda)\). The fibre of the quotient \(\ker T^{p-1}\twoheadrightarrow W_T\) has \(q^{r(\lambda)}\) elements. The triangular-group orbit of the zero vector in \(W_T\) is a singleton, and the orbit whose greatest occupied length is \(j\) has \(q^{b_j}-q^{b_{j-1}}\) vectors. Multiplication gives both formulae for automorphism-orbit sizes. Finally the image of \(D\) is \(TV+kw\), whence \(\operatorname{rank}D=r(\lambda)\) for \(w\in TV\) and \(r(\lambda)+1\) otherwise. Because \(\dim\ker T^{p-1}=m-c_p(\lambda)\), there are \(q^{m-c_p(\lambda)}\) allowed \(w\), of which \(q^{r(\lambda)}\) lie in \(TV\). These quantities prove the rank polynomial.

## Verification

Run `python3 artifacts/check_p_derivations.py` with Python 3 and no additional packages. The checker enumerates every \(T\), every admissible \(w\), and tests the **original Leibniz identity** on every pair of basis elements and the \(p\)-fold iterate on the original algebra. It independently compares rank counts with the partition/centralizer formula and, for four configurations, builds the orbits from explicit invertible arrow changes and translations. Field \(\mathbb F_4\) is implemented using \(\mathbb F_2[u]/(u^2+u+1)\), not integer arithmetic modulo four. The embedded record `artifacts/check_output.txt` contains the observed output.

The complete observed rank distributions (rank: number) are: \(\mathbb F_2,m=2\): \(0:1,1:9\); \(\mathbb F_2,m=3\): \(0:1,1:49,2:42\); \(\mathbb F_2,m=4\): \(0:1,1:225,2:1470\); \(\mathbb F_3,m=2\): \(0:1,1:32,2:48\); \(\mathbb F_4,m=2\): \(0:1,1:75\). All comparison checks passed. The code also tests the orbit generating function for \(p\in\{2,3,5\}\) and \(0\le m\le16\).

## Relationship to prior work

Guo and Li [1], Theorems 2.3 and 3.4 and the structural analysis in Section 3, give a basis and structural description of derivation Lie algebras of path algebras; the present derivation parametrization is consistent with that foundation and **is not claimed as a new general characterization of path-algebra derivations**. Achar and Henderson [2], Proposition 2.3, classify the finer \(\operatorname{GL}(V)\)-orbits of vector-plus-nilpotent-matrix pairs by bipartitions. Sun [3] provides finite-field orbit-size formulae for that enhanced nilpotent cone. Neither statement by itself describes the different conjugation action of the complete algebra automorphism group, which additionally translates \(w\) by \(TV\), nor selects \(D^p=0\) and derives the resulting partition-plus-length orbit law and its rank enumerator. These are the asserted contributions. The close enhanced-cone analogy is a material priority risk: a broader affine-adjoint orbit theorem or a published specialization not located in the inspected literature could subsume parts of the result.

## Limitations

The result concerns finite-dimensional derivations of exactly this two-vertex quiver algebra, ordinary \(p\)-fold nilpotence, and conjugation by its unital algebra automorphisms. It does not classify arbitrary nilpotent derivations of unbounded exponent, actions of general finite group schemes, orbit-closure singularities, or derivations on more general quivers. The finite-field examples do not prove the arbitrary-field theorem; the module/centralizer argument supplies that proof. Historical priority and independent mathematical validation remain unconfirmed.

## References

[1] Li Guo and Fang Li, *Structure of Hochschild cohomology of path algebras and differential formulation of Euler's polyhedron formula*, arXiv:1010.1980, first posted 2010-10-11, https://arxiv.org/abs/1010.1980, particularly Theorems 2.3 and 3.4.

[2] Pramod N. Achar and Anthony Henderson, *Orbit closures in the enhanced nilpotent cone*, arXiv:0712.1079, first posted 2007-12-07, https://arxiv.org/abs/0712.1079, particularly Proposition 2.3. The author's corrigendum arXiv:1008.1117 concerns a different assertion; no disputed affine-paving theorem is used here.

[3] Michael Yuan Sun, *Point stabilisers for the enhanced and exotic nilpotent cones*, arXiv:0909.0356, first posted 2009-09-02, https://arxiv.org/abs/0909.0356, especially Theorem 2.10 and Corollaries 2.12–2.13.
