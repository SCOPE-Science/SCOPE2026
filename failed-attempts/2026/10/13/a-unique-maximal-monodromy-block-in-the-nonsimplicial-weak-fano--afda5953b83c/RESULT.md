# A unique maximal monodromy block in the nonsimplicial weak-Fano Laurent setting
## Finding
Let \(N\) be a lattice of rank \(d\ge1\), let
\[
P\subset N_{\mathbb R}
\]
be a full-dimensional lattice polytope with \(0\in\operatorname{int}(P)\), and let \(f\in\mathbb C[N]\) be nondegenerate at infinity with \(P_{f,\infty}=P\). For sufficiently large \(|t|\), put
\[
V_{\mathbb C}=H^d\!\left((\mathbb C^*)^d,f^{-1}(t);\mathbb C\right),
\]
let \(T_\infty\) be the monodromy at infinity on this relative cohomology, and define the normalized nilpotent logarithm
\[
N_\infty=(2\pi i)^{-1}\log T_{\infty,u}.
\]
Then every Jordan block of \(N_\infty\) has size at most \(d+1\), and there is exactly one block of size \(d+1\). Moreover, that unique maximal block belongs to the semisimple eigenvalue-\(1\) summand. In particular,
\[
N_\infty^d\ne0,
\qquad
N_\infty^{d+1}=0,
\]
and the top Jordan layer is one-dimensional.

The statement applies throughout the full-dimensional weak-Fano Laurent class treated by Wang's 2026 monodromy formula, including nonsimplicial radial fans and Laurent polynomials not restricted to the earlier vertex-supported family.

## Assumptions and scope
The ground field is \(\mathbb C\). The polynomial is nondegenerate at infinity in the sense used in the cited Newton--Hodge formula, and \(P_{f,\infty}=P\) is full-dimensional with the origin in its interior. These are precisely the hypotheses under which the source identifies the unique nonzero relative cohomology at infinity and gives its eigenvalue-graded Jordan multiplicities.

For a cone \(c\) of the radial fan, write
\[
m_c=d-\dim c.
\]
The source expands the local weighted polynomial as
\[
l^*_{\psi_c}(c;t)=\sum_{a\in\mathbb Q}n_{c,a}t^a
\]
and writes \(b_{c,j}\) for the primitive intersection-cohomology multiplicity indexed by \(j\ge0\).

## Proof
Wang's monodromy multiplicity formula states that the number \(J_{k,\lambda}\) of size-\(k\) Jordan blocks on the semisimple \(\lambda\)-eigenspace is
\[
J_{k,\lambda}
=
\sum_{\substack{a\in\mathbb Q\\ e^{-2\pi i a}=\lambda}}
\ \sum_{\substack{c,j\\m_c-2j+1=k}}
 n_{c,a}b_{c,j}.
\]
Because \(m_c=d-\dim c\le d\) and \(j\ge0\), every summand satisfies
\[
m_c-2j+1\le d+1.
\]
Hence no Jordan block can have size greater than \(d+1\).

Suppose now that \(k=d+1\). The equality
\[
m_c-2j+1=d+1
\]
forces simultaneously \(\dim c=0\) and \(j=0\). The radial fan has a unique zero cone \(c=0\). For that cone the source states that the local weighted polynomial is exactly \(1\), so
\[
n_{0,0}=1
\]
and \(n_{0,a}=0\) for \(a\ne0\). The degree-zero primitive intersection cohomology of the complete quotient fan is one-dimensional, hence
\[
b_{0,0}=1.
\]
Therefore
\[
J_{d+1,1}=1,
\qquad
J_{d+1,\lambda}=0\quad(\lambda\ne1).
\]
This proves both uniqueness and the eigenvalue statement. A nilpotent Jordan block of size \(d+1\) has nonzero \(d\)-th power but zero \((d+1)\)-st power, while all other blocks are no larger, so
\[
N_\infty^d\ne0,
\qquad
N_\infty^{d+1}=0.
\]

## Verification
The proof was replayed directly from the source's full eigenvalue-graded block formula rather than inferred from examples or finite experiments. The two boundary inputs were separately checked in the source: \(m_c=d-\dim c\), and the zero-cone local weighted polynomial is \(1\). The maximal-size equation then has the unique solution \((c,j)=(0,0)\), and its age is \(0\), giving semisimple eigenvalue \(e^{-2\pi i\cdot0}=1\).

The argument is independent of a choice of simplicial subdivision because the source's primitive multiplicity formulation is subdivision-independent. No computation about lower Jordan blocks is needed, and no claim is made about their multiplicities.

## Relationship to prior work
Wang's 2026 paper proves the general eigenvalue-graded Jordan multiplicity formula and the age--monodromy comparison in the full-dimensional weak-Fano setting. It explicitly notes that the simplicial, vertex-supported case specializes to Wang's 2024 sectorwise comparison, while the new pure-sheaf formulation extends to nonsimplicial weak-Fano data. The unique maximal block above is an unstated extremal consequence of the 2026 formula: the maximal block can only come from the zero cone, whose local contribution is exactly one.

The 2024 paper therefore already supplies enough structure to obtain the same conclusion in its narrower simplicial, vertex-supported family; no originality is claimed for that special case. The new scope is the 2026 nonsimplicial and non-vertex-supported weak-Fano Laurent setting.

Stapledon's 2017 monodromy formulas, and the earlier work of Matsui--Takeuchi, give combinatorial Jordan-block formulas for monodromy at infinity of convenient polynomial maps on affine space. Those hypotheses and cohomology groups are different from the arbitrary Laurent-torus relative-cohomology setting used here, so those results do not by themselves imply the stated nonsimplicial weak-Fano Laurent theorem.

## Limitations
The theorem identifies only the extremal Jordan layer. It does not determine the lower block multiplicities, the rational polarized limit mixed Hodge structure, extension data, or a canonical comparison with the compact mirror side.

The originality comparison is literature-based. Older formulas cover important special polynomial-map settings, and the 2024 paper covers the simplicial vertex-supported Laurent special case. The accepted claim is restricted to the additional generality furnished by the 2026 formula.

## References
1. Haoxu Wang, *Motivic Vanishing Cycles at Infinity and Toric Landau--Ginzburg Mirror Symmetry*, arXiv:2610.00289v1, 25 September 2026, especially Corollary 6.5 and Corollary 7.4.
2. Haoxu Wang, *Newton Polyhedrons and Hodge Numbers of Non-degenerate Laurent Polynomials*, arXiv:2403.02105, 2024, especially Corollary 4.5.
3. Alan Stapledon, *Formulas for monodromy*, Research in the Mathematical Sciences 4 (2017), article 8, DOI 10.1186/s40687-017-0097-x, especially Corollary 6.14.
4. Yutaka Matsui and Kiyoshi Takeuchi, *Monodromy at infinity of polynomial maps and Newton polyhedra*, arXiv:0912.5144.
