# The exact constructible image of the minimal nonclosed two-block rank-one pattern map

## Finding

Let \(k\) be **any field**. Denote by \(\operatorname{Mat}_2(k)\) the vector space of \(2\times2\) matrices, and let \(\mathcal R_k=\{M\in\operatorname{Mat}_2(k):\operatorname{rank}M\le1\}\). Define the polynomial parametrization

\[\Phi_k:\mathcal R_k^3\longrightarrow\operatorname{Mat}_2(k)^2,\qquad(A,B,C)\longmapsto(A+C,B+C).\]

It is the formal two-pattern map of a shallow architecture with two inputs, three hidden neurons, two outputs, and one neuron active exclusively in each pattern plus one neuron active in both (block sizes \((a,b,c)=(1,1,1)\)). The **exact pointwise image**, not merely its Zariski closure, is

\[\boxed{\operatorname{im}\Phi_k=\operatorname{Mat}_2(k)^2\setminus\{(X,\lambda X):X\in\operatorname{GL}_2(k),\ \lambda\in k\setminus\{0,1\}\}.}\tag{1}\]

For algebraically closed \(k\), the exceptional, nonattainable constructible locus \(E\) is isomorphic to \(\operatorname{GL}_2\times(\mathbb A^1\setminus\{0,1\})\), hence is smooth of dimension \(5\) and codimension \(3\) in \(\mathbb A^8\). Its Zariski closure \(Z\) is the irreducible rank-at-most-one determinantal variety

\[Z=\left\{(X,Y):\operatorname{rank}\begin{pmatrix}\operatorname{vec}X&\operatorname{vec}Y\end{pmatrix}\le1\right\}.\tag{2}\]

Thus \(Z\) has six quadratic defining minors, \(\mathbb P(Z)=\operatorname{Seg}(\mathbb P^3\times\mathbb P^1)\subset\mathbb P^7\) is degree \(4\), and the affine cone \(Z\) is singular only at its vertex. The image of \(\Phi_k\) is Zariski dense in \(\mathbb A^8\) over any infinite field (and geometrically dense after any base-field extension).

For every prime power \(q\),

\[\boxed{\#\bigl(\operatorname{Mat}_2(\mathbb F_q)^2\setminus\operatorname{im}\Phi_{\mathbb F_q}\bigr)=(q-2)(q^2-1)(q^2-q),}\tag{3}\]

with image cardinality \(q^8-(q-2)(q^2-1)(q^2-q)\). In particular the map is surjective on \(\mathbb F_2\)-points, even though its geometric image is not closed after extending the field.

## Assumptions and scope

Matrices have entries in an arbitrary field, including characteristic two. The inequality \(\operatorname{rank}\le1\) permits zero matrices. The pairs \((X,Y)\) are ordered. The word *image* means the images of **\(k\)-rational input matrices**, not just geometric points of a scheme-theoretic image. The geometric statements refer to the reduced locally closed missing locus over an algebraically closed field. The map describes algebraic compatibility of two specified activation patterns, not whether those two patterns occur as nonempty cells of a particular real-input hyperplane arrangement.

## Proof

**Step 1: reduction to an invertible member.** Given \((X,Y)\), if both matrices are singular then \(A=X\), \(B=Y\), \(C=0\) is a valid rank-at-most-one decomposition. If \(X\) is singular and \(Y\) invertible, exchange the ordered outputs and the roles of \(A\) and \(B\). It remains to analyze the case \(X\in\operatorname{GL}_2(k)\). Put \(T=X^{-1}Y\). A decomposition \(X=A+C\), \(Y=B+C\) is equivalent, after left multiplication by \(X^{-1}\), to a rank-at-most-one matrix \(C'=X^{-1}C\) for which \(I-C'\) and \(T-C'\) are singular.

**Step 2: the matrix-determinant identity.** Seek \(C'=uv^{\mathsf T}\) with column vectors \(u,v\in k^2\). The elementary \(2\times2\) determinant identity holds over every characteristic:

\[\det(S-uv^{\mathsf T})=\det(S)-v^{\mathsf T}\operatorname{adj}(S)u.\]

For \(S=I\), the first singularity condition is \(v^{\mathsf T}u=1\). For \(S=T\), the second is \(v^{\mathsf T}\operatorname{adj}(T)u=\det T\). Because \(\operatorname{adj}(T)=(\operatorname{tr}T)I-T\), the two constraints are equivalent to

\[v^{\mathsf T}u=1,\qquad v^{\mathsf T}Tu=\operatorname{tr}(T)-\det(T).\tag{4}\]

**Step 3: every nonscalar normalized pair is attained.** If \(T\) is not scalar, there is a vector \(u\in k^2\) such that \(u\) and \(Tu\) are linearly independent: otherwise every line in \(k^2\) would be invariant, forcing \(T\) scalar (apply invariance to two basis vectors and their sum). The independent columns \((u,Tu)\) form a basis; hence there exists a unique linear form \(v^{\mathsf T}\) taking on them the two prescribed values in (4). Consequently \(C'=uv^{\mathsf T}\) and \(A=X(I-C')\), \(B=X(T-C')\), \(C=XC'\) each have rank at most one. Indeed the determinant identity gives \(\det(I-C')=\det(T-C')=0\) and \(\operatorname{rank}C'\le1\).

**Step 4: scalar normalized pairs.** Suppose \(T=\lambda I\). Every solution must have \(\operatorname{tr}C'=1\), since \(\det(I-C')=1-\operatorname{tr}C'\) for a rank-at-most-one \(2\times2\) matrix. The second constraint becomes \(\det(\lambda I-C')=\lambda^2-\lambda\), so \(\lambda(\lambda-1)=0\). Over a field this is equivalent to \(\lambda\in\{0,1\}\). Conversely for either scalar, take \(C'=\begin{pmatrix}1&0\\0&0\end{pmatrix}\); then \(I-C'\) and \(\lambda I-C'\) have rank at most one. This proves (1), including the case \(\operatorname{char}k=2\).

**Step 5: geometry of the omitted locus.** On the open locus where \(X\) is invertible, the equation \(Y=\lambda X\) identifies the missing set as \(\operatorname{GL}_2\times(\mathbb A^1\setminus\{0,1\})\). This identification is algebraic in both directions: the inverse obtains \(\lambda\) as the \((1,1)\)-entry of \(X^{-1}Y\). The closure of this locus consists of all proportional pairs \((X,Y)\); these are precisely the rank-at-most-one points of the \(4\times2\) matrix whose columns are \(\operatorname{vec}X\) and \(\operatorname{vec}Y\). To see density, note that among nonzero rank-one columns there is a dense open subset with \(X\) invertible and scalar parameter neither zero nor one. Classical row-column charts show smoothness away from the zero matrix; at the vertex the defining minors are quadratic and the Zariski tangent space is all \(\mathbb A^8\), larger than \(\dim Z=5\). Projectivizing gives \(\mathbb P^3\times\mathbb P^1\) via the Segre embedding. With hyperplane classes \(h_3,h_1\), its degree is

\[\int_{\mathbb P^3\times\mathbb P^1}(h_3+h_1)^4=\binom41=4.\]

The complement of this closed rank-one cone is a dense open subset of the image, so the whole parameter-image closure is \(\mathbb A^8\).

**Step 6: finite fields.** For \(k=\mathbb F_q\), the map \((X,\lambda)\mapsto(X,\lambda X)\) is injective on \(\operatorname{GL}_2(k)\times(k\setminus\{0,1\})\). Since \(\#\operatorname{GL}_2(\mathbb F_q)=(q^2-1)(q^2-q)\), (3) follows. Every rank-at-most-one matrix is an outer product, so a triple of such matrices corresponds to the three hidden-neuron contributions in the stated formal pattern-map model.

## Verification

The standalone accompanying `finite_field_check.py` enumerates all rank-at-most-one triples over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), constructing actual pairs and comparing the entire missing set with (1). All three equalities were checked by exact finite-field arithmetic:

| Field | Attainable ordered pairs | Nonattainable ordered pairs |
|---|---:|---:|
| \(\mathbb F_2\) | 256 | 0 |
| \(\mathbb F_3\) | 6513 | 48 |
| \(\mathbb F_4\) | 65176 | 360 |

Run `python3 finite_field_check.py` using the Python standard library. These tests check only finite cases and are **not** used to infer the universal theorem; Steps 1–6 provide the proof for all fields.

## Relationship to prior work

Alexandr, Grillo, Holleben, Montúfar and Yu [1], Theorem 1, determine the defining ideals of the **Zariski closures** of two-block shallow ReLU pattern images. For the \((2,3,2)\) architecture and \((1,1,1)\) block sizes, all their determinantal equations are vacuous, so that closure is the whole space. Their Example 3 exhibits the particular nonattainable limit \((I_2,2I_2)\) over the complex numbers, and Proposition 4 determines when a general pattern-map image is closed. They explicitly distinguish closure from exact attainment and leave a general exact representability criterion for later work. Formula (1) completely classifies attained and omitted pairs for their minimal nonclosed example, rather than giving another isolated obstruction. Alexandr–Montúfar [2] introduce the surrounding pattern-variety approach; Finkel–Fu–Wu [3] study canonical activation patterns and pattern equivalence, rather than this exact pointwise decomposition. The determinantal geometry used in Step 5 is classical and is not claimed as a new construction independent of (1).

## Limitations

No claim is made about exact images of larger architectures or about the realization of the selected activation patterns as actual nonempty real regions for a prescribed input configuration. The degree-four Segre cone is a standard determinantal variety; the new content is its identification as the closure of **all and only** the missing points of this formal minimal pattern map. Search-based novelty comparison is not proof of absolute publication priority. This is a self-reviewed mathematical finding, not independently audited or externally certified.

## References

[1] Y. Alexandr, M. Grillo, T. Holleben, G. Montúfar, and T. Yu, *Defining equations for two-block shallow ReLU pattern varieties*, arXiv:2611.23846v1 (first public 18 November 2026). https://arxiv.org/html/2611.23846v1.

[2] Y. Alexandr and G. Montúfar, *Constraining the outputs of ReLU neural networks*, arXiv:2508.03867v2. https://arxiv.org/html/2508.03867v2.

[3] B. Finkel, Y. Fu, and C. Wu, *Canonical activation patterns and ReLU pattern varieties*, arXiv:2611.20346v1. https://arxiv.org/html/2611.20346v1.
