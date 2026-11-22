# Exact nonidentity-morphism complexity of three-object sphere-bouquet models

## Finding
For each integer \(s\ge1\), define \(\mu_3(s)\) to be the least total number of **nonidentity** arrows in a finite acyclic category with **exactly three objects** whose classifying space is homotopy equivalent to \(\bigvee^s S^2\). Then
\[
\boxed{\mu_3(s)=3+\min_{u,v\ge1,\ uv\ge s}(u+v+uv-s)}.
\]
The minimization is over positive integers. Equivalently,
\[
\mu_3(s)=3+\min_{1\le u\le s}\left(u+\left\lceil\frac{s}{u}\right\rceil+u\left\lceil\frac{s}{u}\right\rceil-s\right).
\]
Every pair \(u,v\) with \(uv\ge s\) supports a simply connected three-object example with exactly \(u+v+uv-s+3\) nonidentity arrows and exactly \(s\) independent integral two-sphere classes.

## Assumptions and scope
An *acyclic category* is a small category whose endomorphisms and isomorphisms are all identities. Its classifying space is the realization of its nerve. The count includes *all* nonidentity morphisms, including composites, but excludes the three identity arrows. We assume \(s\) is an arbitrary fixed positive integer and no restriction on individual hom-set multiplicities. All homotopy equivalences are ordinary, nonequivariant homotopy equivalences. The minimum concerns three objects, not any number of objects.

## Proof
**Step 1: every admissible category is a three-object chain.** A category with \(B\mathcal C\simeq\bigvee^s S^2\), \(s\ge1\), must have a nonzero two-dimensional nerve chain group: otherwise its classifying space is a graph and has zero second homology. A nondegenerate two-simplex requires a chain of distinct objects \(0\to1\to2\). Acyclicity makes this a linear order on all three objects; there are no other directions or nontrivial endomorphisms.

Write \(a=|\operatorname{Hom}(0,1)|\), \(b=|\operatorname{Hom}(1,2)|\), and \(c=|\operatorname{Hom}(0,2)|\), all positive, and \(T:\{0,\ldots,a-1\}\times\{0,\ldots,b-1\}\to\{0,\ldots,c-1\}\) for the composition table. The nerve has exactly three nondegenerate zero-simplices, \(a+b+c\) one-simplices and \(ab\) two-simplices, and none in higher dimensions. Hence
\[
\chi(B\mathcal C)=3-(a+b+c)+ab=1+(a-1)(b-1)-(c-1).
\]
The target has Euler characteristic \(1+s\). Thus, with \(u=a-1\), \(v=b-1\), necessarily
\[
 c=uv-s+1,\qquad uv\ge s.
\]
In particular \(u,v\ge1\), and the arrow count is \(a+b+c=u+v+uv-s+3\). This proves the proposed lower bound without any assumption on the composition table beyond categorical associativity.

**Step 2: realize every permissible pair.** Fix \(u,v\ge1\), \(uv\ge s\), and put \(c=uv-s+1\). Take three objects \(0,1,2\), morphisms \(f_i:0\to1\) for \(0\le i\le u\), \(g_j:1\to2\) for \(0\le j\le v\), and \(h_k:0\to2\) for \(0\le k<c\). Define
\[
 g_j\circ f_i=h_{T(i,j)},\quad T(i,0)=T(0,j)=0.
\]
Give \(c-1=uv-s\) distinct interior cells \((i,j)\) with \(i,j\ge1\) the distinct labels \(1,\ldots,c-1\), and give every remaining interior cell label zero. There are precisely \(uv\) interior cells, so this is possible. Since there are no composable triples of nonidentity morphisms, these prescriptions satisfy associativity and determine a finite acyclic category.

**Step 3: fundamental group and higher homology.** The underlying one-skeleton is connected. Choose the edges \(f_0,g_0\) as a maximal tree. In the cellular presentation of \(\pi_1(B\mathcal C)\), each two-simplex imposes \(f_i g_j=h_{T(i,j)}\) (up to the harmless order convention). The \((0,0)\) relation kills \(h_0\). The zeroth-column relations kill all \(f_i\), and the zeroth-row relations kill all \(g_j\). Finally every \(h_k\) occurs as a composite, so all \(h_k\) are killed. Thus \(\pi_1(B\mathcal C)=1\), and \(H_1=0\).

The nerve is two-dimensional, so \(H_2=\ker\partial_2\) is a free abelian group. Its rank follows from the already computed Euler characteristic: \(\operatorname{rank}H_2=\chi-1=s\). By the Hurewicz theorem choose spherical representatives of an integral basis of \(H_2\). Their wedge gives a homology equivalence \(\bigvee^s S^2\to B\mathcal C\). Both spaces are simply connected CW complexes, so the homological Whitehead theorem makes this a homotopy equivalence. Therefore the lower bound is achieved at every allowed \(u,v\).

**Step 4: finite optimization, scale, and nonmonotonicity.** For fixed \(u\), the objective is strictly increasing in \(v\), so the minimizing \(v\) is \(\lceil s/u\rceil\). Values \(u>s\) cannot improve \(u=s,v=1\), proving the finite one-variable formula. The arithmetic-geometric mean inequality gives \(u+v\ge2\sqrt s\) and \(uv-s\ge0\), so \(\mu_3(s)\ge2\sqrt s+3\). Conversely choose \(u=\lfloor\sqrt s\rfloor\), \(v=\lceil s/u\rceil\). Then \(v\le u+2\) and \(0\le uv-s\le u-1\), giving \(\mu_3(s)\le3u+4\le3\sqrt s+4\). Direct minimization gives \(\mu_3(7)=10\) and \(\mu_3(8)=9\). At \(s=100\), \(u=v=10\) gives \(11+11+1=23\) nonidentity arrows, compared with \(104\) in the cited one-thin-factor family.

## Verification
The included `verify.py` constructs the exact tables, forms all integer nerve boundary columns, verifies \(\partial_1\partial_2=0\), and checks maximal boundary ranks over three finite fields. It passed 150 optimal constructions, 250 independently chosen permissible nonoptimal parameter triples, and 100 exhaustive small-instance optimization comparisons. Finite calculations check instances; the proof above covers all positive integers \(s\).

Run in an environment with Python 3: `python3 verify.py`. No external packages or internet access are needed.

## Relationship to prior work
Carcacía-Campos (arXiv:2611.09718v1, Sections 2.3 and 4.2–4.4) introduced three-object composition tables for categorical models and proved the minimum *object* number for bouquets of spheres; its explicit family \(\mathcal S_{s+1}\) has \(s+4\) nonidentity arrows. The present exact minimization of **arrow count at fixed object-minimum three** is a different invariant and shows square-root rather than linear growth. The new result uses the known nerve cell description and an anchor-row composition table, but neither the exact minimum nor the optimizing arithmetic law is stated in that primary source. Tanaka's work concerns strong homotopy and beat-object reductions, rather than this morphism-count extremum.

## Limitations
The result does not minimize the number of morphisms over categories with four or more objects, nor the number of generating arrows before closure under composition. It does not classify all minimizing composition tables or their strong homotopy types. Similar unindexed optimizations could exist. The proof is mathematical, not independently validated; the finite checker is not a proof of the universal statement.

## References
- Isaac Carcacía-Campos, *How many points does it take to see the homotopy of a space? Minimal acyclic categorical models*, arXiv:2611.09718v1 (public 2026-11-06), https://arxiv.org/abs/2611.09718 . Read Sections 1, 2.3, 4.2–4.4.
- Kohei Tanaka, *Strong homotopy types of acyclic categories and \(\Delta\)-complexes*, arXiv:1707.01179 (2017), https://arxiv.org/abs/1707.01179 . Background on strong homotopy.
- Allen Hatcher, *Algebraic Topology* (2002), https://pi.math.cornell.edu/~hatcher/AT/AT.pdf . Standard CW, Hurewicz, and Whitehead results.
