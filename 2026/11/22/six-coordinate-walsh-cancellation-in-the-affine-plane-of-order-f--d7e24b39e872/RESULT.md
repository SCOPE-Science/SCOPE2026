# Six-coordinate Walsh cancellation in the affine plane of order four

## Finding
Let \(A=\operatorname{AG}(2,4)\) be the sixteen-point affine plane over the four-element field, and let \(\mathcal B\) be its \(480\) noncollinear triples (the bases of its ordinary rank-three affine-geometry matroid). Regard every triple as an incidence vector in \(H=(\mathbb F_2)^{16}\), and define the unnormalized Walsh coefficient
\[
 W(S)=\sum_{B\in\mathcal B}(-1)^{|S\cap B|},\qquad S\subseteq A.
\]
The first vanishing coefficients have frequency support size six. There are exactly \(960\) of them, and their supports are **precisely** the sets consisting of a complete four-point affine line \(L\), together with two exterior points whose joining line meets \(L\). At every other frequency weight below six, no cancellation occurs.

More generally, there are precisely \(6{,}150\) zeros among the \(65{,}536\) frequencies. They occur only at weights six, eight and ten, with respective multiplicities \(960,4230,960\). Consequently, counting convolution by the basis-incidence indicator on \(H\) has rank \(59{,}386\), least nonzero absolute multiplier \(4\), largest multiplier magnitude \(480\), and sharp nonzero-spectrum \(\ell^2\) condition number \(120\).

The exact minimum operator norm over **all real or complex linear projections** onto this convolution range is
\[
 \min_{Q^2=Q,\ \operatorname{ran}Q=\operatorname{ran}T}\|Q\|_{\ell^1(H)\to\ell^1(H)}
 =\min_{Q^2=Q,\ \operatorname{ran}Q=\operatorname{ran}T}\|Q\|_{\ell^\infty(H)\to\ell^\infty(H)}
 =\frac{558109}{16384}.
\]

The complete **absolute** Walsh-multiplier spectrum is as follows; for each nonzero magnitude, positive and negative signs each occur in half of the indicated multiplicity.

| \(|W|\) | Frequency multiplicity |
|---:|---:|
| 0 | 6,150 |
| 4 | 10,560 |
| 8 | 6,960 |
| 12 | 10,880 |
| 16 | 10,320 |
| 20 | 9,216 |
| 24 | 8,960 |
| 28 | 960 |
| 40 | 96 |
| 48 | 40 |
| 76 | 960 |
| 84 | 160 |
| 168 | 240 |
| 300 | 32 |
| 480 | 2 |

## Assumptions and scope
Construct \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\). The sixteen points are ordered lexicographically as \((x,y)\), where \(x,y\in\{0,1,u,u+1\}\). The twenty affine lines comprise the four vertical lines \(x=b\) and the sixteen lines \(y=mx+b\), with \(b,m\in\mathbb F_4\). Each line contains four points, each point lies on five lines, and each pair of points lies on exactly one line. Every basis is a three-element point set not contained in a line. The convolution operator is \(Tf(z)=\sum_{B\in\mathcal B}f(z+\mathbf1_B)\), where addition is coordinatewise modulo two and no probability normalization is applied. The assertions concern precisely this fixed affine geometry and this vertex-incidence embedding, not all affine geometries or arbitrary matroids.

## Proof
**Basis incidences and an exact multiplier formula.** Of the \(\binom{16}{3}=560\) distinct triples, precisely \(20\binom43=80\) are collinear. Thus \(|\mathcal B|=480\). Any given point belongs to \(\binom{15}{2}-5\binom32=90\) bases, and any two distinct points belong to \(14-2=12\) bases. Write \(k=|S|\), and let
\[
 t(S)=\sum_{L\text{ affine line}}\binom{|S\cap L|}{3}.
\]
Every collinear triple lies in exactly one line, so \(\binom k3-t(S)\) is the number of bases wholly contained in \(S\). Expanding \((-1)^r=(1-2)^r\) and summing over bases gives the **identity for every one of the \(2^{16}\) frequencies**
\[
 \boxed{W(S)=480-180k+48\binom{k}{2}-8\binom{k}{3}+8t(S).}\tag{1}
\]
This formula supplies a second route to every Fourier coefficient independently of the Walsh butterfly transform.

**First zero and its geometry.** For \(0\le k\le4\), the term in (1) excluding \(8t(S)\) is respectively \(480,300,168,76,16\), all positive. At \(k=5\), it is \(-20\), which is not divisible by eight, so zero remains impossible. At \(k=6\), it is \(-40\), hence \(W(S)=0\) exactly if \(t(S)=5\).

If \(S\) contains no complete four-point line, all its collinear triples belong to distinct lines. Five such triples would use \(15\) distinct point-pairs, exhausting the \(\binom62=15\) pairs. This would make each point belong to \((6-1)/(3-1)=5/2\) triples, impossible. Thus \(t(S)\le4\) without a complete line. If \(S\) contains a complete line \(L\), that line contributes four collinear triples. With only two additional exterior points, at most one other triple is collinear; it occurs exactly when their joining line meets \(L\). Two distinct complete lines cannot both fit in six points. There are twenty choices of \(L\), and, for fixed \(L\), \(\binom{12}{2}-3\binom42=48\) eligible exterior pairs (exclude pairs on the same one of three lines parallel to \(L\)). Hence exactly \(20\cdot48=960\) six-point zeros, with the stated unique geometric form.

**Complete finite spectrum and nullity.** The accompanying standalone `verify.py` constructs all twenty lines in two different ways, lists the 480 bases, and computes the complete \(2^{16}\)-entry integer Walsh-Hadamard transform. Separately, it evaluates (1) using line intersections for every frequency and checks equality entry by entry. The resulting absolute histogram is the table above. In particular zeros occur only at support weights six, eight, and ten; at weight eight they have three distinct intersection profiles \((N_0,N_1,N_2,N_3,N_4)\), with multiplicities
\[
 (1,4,10,4,1):4080,\qquad(0,8,4,8,0):120,\qquad(2,0,16,0,2):30,
\]
where \(N_j\) counts lines meeting \(S\) in exactly \(j\) points. The transform verifies no other zeros. Because every basis has cardinality three, \(W(A\setminus S)=-W(S)\), accounting for the matching ten-point cancellation count and the equal positive/negative multiplicities. The convolution is diagonal in the Walsh basis, so its rank is \(65536-6150=59386\); its largest absolute eigenvalue is \(480\) and its least nonzero absolute eigenvalue is \(4\).

**Unrestricted optimal projection.** Let \(R=\operatorname{ran}T\). Its unique translation-invariant linear projection is the Fourier multiplier \(\mathbf1_{\{W\ne0\}}\), whose convolution kernel is
\[
 p(x)=2^{-16}\sum_{S:W(S)\ne0}(-1)^{|S\cap x|}.
\]
For an arbitrary projection \(Q\) onto \(R\), average \(\tau_gQ\tau_{-g}\) over all translations \(g\in H\). This remains a projection onto \(R\) (every summand fixes \(R\) and maps into \(R\)) and has norm at most \(\|Q\|\) in either endpoint space. Translation invariance makes the averaged operator exactly convolution by \(p\). The norm of that operator in both \(\ell^1\) and \(\ell^\infty\) equals \(\sum_x|p(x)|\). A second integer Walsh transform of the support indicator computes
\[
 \sum_{x\in H}\left|\sum_{S:W(S)\ne0}(-1)^{|S\cap x|}\right|=2{,}232{,}436,
\]
so both sharp endpoint projection constants equal \(2{,}232{,}436/65{,}536=558109/16384\).

## Verification
Run `python verify.py` using the Python standard library, without third-party packages or external data. It asserts both constructions of the affine lines, uniqueness of pair-incidence, base count and single/pair frequencies, all 65,536 identities (1), the complete spectrum, support-weight and geometric cancellation counts, the minimum nonzero multiplier, the rank, and the projection-kernel norm. A successful run prints `PASS` and the exact certified counts. The source code and all computations operate on fixed finite integer arrays; the finite census is exhaustive because it loops over **every** sixteen-bit frequency. The analytic first-zero classification and unrestricted projection optimality were also proved above independently of computational extrapolation.

## Relationship to prior work
Affine geometry and its independent-point matroids are standard; the 2016 public preprint *Designs and codes in affine geometry* gives a matroid framework and affine incidence identities. A 2016 study of matroid visualization depicts \(\operatorname{AG}(2,4)\) but studies drawing and incident-line representations, not Walsh recovery. Related published results for rank-three Steiner triple systems concern **three-point lines**, unlike the four-point lines here; results for binary projective geometries concern a different underlying matroid and do not imply this signed spectrum. These sources supply the geometric framework and context, not the 960 first-cancellation supports, 6,150 total null frequencies, or the unrestricted endpoint projection constant.

## Limitations
This is a complete and reproducible finite theorem about \(\operatorname{AG}(2,4)\), not a theorem for all prime powers. The full spectral histogram and projection numerator depend on exhaustive integer computation, supported by the independent algebraic identity (1); no claim that enumeration alone proves a general infinite theorem is made. Unindexed equivalent computations may exist. The result has received self-review but no independent mathematical audit.

## References
1. Jens Zumbrägel, *Designs and codes in affine geometry*, arXiv:1605.03789, first publicly submitted 2016-05-12. https://arxiv.org/abs/1605.03789
2. R. L. Schepens, *Matroid visualization: avoiding false line incidents in geometric visualization methods for matroids of rank 3*, Eindhoven University of Technology thesis, August 2016; figure 35 treats \(\operatorname{AG}(2,4)\). https://pure.tue.nl/ws/files/69852125/Schepens_2016.pdf
3. *Uniform dyadic nonvanishing for the Walsh transform of Steiner matroid bases*, related published mathematical result (2026); concerns Steiner triple systems whose line size is three.
4. *Sharp dyadic Fourier divisibility and the first singular rank of binary projective matroid bases*, related published mathematical result (2026); concerns binary projective geometries.
