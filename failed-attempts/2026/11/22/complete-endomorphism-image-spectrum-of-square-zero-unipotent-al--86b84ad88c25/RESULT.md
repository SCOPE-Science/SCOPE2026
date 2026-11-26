# Complete endomorphism image spectrum of square-zero unipotent Alexander quandles

## Finding
Let \(p\) be any prime, let \(d\ge1\), and let \(V=\mathbb F_p^d\) with \(N=p^d\) elements. Define the finite Alexander quandle \(Q=V\times V\) by
\[
(a,b)\triangleright(c,e)=(a+b-e,b).
\]
It is defined by the unipotent automorphism \(T(a,b)=(a+b,b)\), whose nonzero nilpotent part has square zero. **All set-theoretic quandle endomorphisms**, with no additivity assumed, have the unique form
\[
\boxed{F_{L,s,t}(a,b)=(La+t(b),\,Lb+s),\quad L\in\operatorname{End}_{\mathbb F_p}(V),\quad s\in V,\quad t:V\to V\text{ arbitrary}.}
\]
Thus there are exactly \(p^{d^2+d+dN}\) endomorphisms.

For \(0\le r\le d\), write \(q_r=p^r\), \(m_r=p^{d-r}\), and let
\[
B_{d,r}(p)={d\brack r}_p\prod_{i=0}^{r-1}(p^d-p^i),\qquad {d\brack r}_p=\prod_{i=0}^{r-1}\frac{p^{d-i}-1}{p^{r-i}-1}.
\]
These are respectively the number of \(d\times d\) matrices of rank \(r\) and a Gaussian binomial coefficient. If \({m\brace j}\) denotes a Stirling number of the second kind and \((m)_j=m(m-1)\cdots(m-j+1)\), then the **complete endomorphism image-cardinality polynomial** is
\[
\boxed{\mathcal P_{p,d}(z)=\sum_{F\in\operatorname{End}(Q)}z^{|F(Q)|}
=N\sum_{r=0}^d B_{d,r}(p)
\left[q_r^{m_r}\sum_{j=1}^{m_r}(m_r)_j{m_r\brace j}z^{q_rj}\right]^{q_r}.}
\]
The expression specifies the exact multiplicity of every achievable image size for every \(p,d\).

A sharp gap follows: every nonbijective endomorphism has image size at most \(N^2/p\), and this bound is attained. Consequently no image size strictly between \(N^2/p\) and \(N^2\) occurs. Exactly
\[
\boxed{N B_{d,d-1}(p)\left[p^{(d-1)p}p!\right]^{p^{d-1}}}
\]
endomorphisms attain the largest proper image size. (The automorphism count \(N|\operatorname{GL}_d(\mathbb F_p)|N^N\) is given for completeness, not claimed as a new automorphism theorem.)

## Assumptions and scope
An endomorphism is **any function on the underlying \(N^2\)-element set** preserving \(\triangleright\); it is not presumed additive, affine or linear. Image size is set cardinality. The field is the prime field \(\mathbb F_p\); all integers \(d\ge1\) and all primes are included. For \(r=0\), empty products are one, and the Gaussian coefficient convention is standard. The operation has \(N\) right-translation orbits, indexed by \(b\in V\). The order of the convention \(T\) in the Alexander operation is explicit and equivalent to the opposite operation convention often used in the literature.

## Proof
**1. Orbit partition.** A right translation by \((c,e)\) sends \((a,b)\) to \((a+b-e,b)\). As \(e\) ranges over \(V\), every element in the fiber \(V\times\{b\}\) is reachable. Because a homomorphism intertwines right translations, it carries each such orbit into a single target fiber. Therefore any endomorphism can be written \(F(a,b)=(f_b(a),\sigma(b))\) with arbitrary functions \(f_b:V\to V\), \(\sigma:V\to V\) at this point.

**2. Derive a common additive linear map.** Preservation of \(\triangleright\) is equivalent to
\[
f_b(a+b-e)=f_b(a)+\sigma(b)-\sigma(e)
\]
for every \(a,b,e\in V\). With \(h=b-e\), put \(L_b(h)=\sigma(b)-\sigma(b-h)\). The displayed identity says that \(f_b(a+h)-f_b(a)=L_b(h)\), independent of \(a\), so \(L_b\) is additive in \(h\). But telescoping differences of \(\sigma\) give
\[
L_b(h+k)=L_b(h)+L_{b-h}(k).
\]
Additivity of \(L_b\) in its argument then implies \(L_{b-h}(k)=L_b(k)\) for all \(b,h,k\). Hence \(L_b=L\) is independent of \(b\), and this common map is additive. Therefore \(L\) is \(\mathbb F_p\)-linear, \(\sigma(b)=Lb+s\) with \(s=\sigma(0)\), and \(f_b(a)=La+t(b)\) where \(t(b)=f_b(0)\). This proves necessity and uniqueness of the displayed normal form. Substitution into the original homomorphism identity proves sufficiency, for every arbitrary \(t\).

**3. Count endomorphisms.** There are \(p^{d^2}\) linear operators \(L\), \(N\) vectors \(s\), and \(N^N=p^{dN}\) functions \(t:V\to V\). Multiplying gives \(p^{d^2+d+dN}\). For a specified linear rank \(r\), the number of \(L\) is \(B_{d,r}(p)\) by choosing its image (Gaussian coefficient) and a surjection onto that image (the product in the definition).

**4. Determine image sizes with occupancy.** Fix a rank-\(r\) map \(L\), set \(W=L(V)\), and put \(q_r=|W|\) and \(m_r=|\ker L|\). In the output of \(F_{L,s,t}\), there are exactly \(q_r\) distinct second coordinates \(Lb+s\). Each such coordinate has exactly \(m_r\) input component labels \(b\). For each of these labels the entire image of the corresponding first-coordinate fiber is \(W+t(b)\), a coset of \(W\) in \(V\). There are \(m_r=|V/W|\) possible cosets, each with \(q_r\) choices of representative \(t(b)\). If precisely \(j\) distinct cosets are used among the \(m_r\) independently labeled inputs, the output has \(q_rj\) points over that second coordinate. The number of assignments with exactly \(j\) occupied cosets is
\[
q_r^{m_r}\binom{m_r}{j}j!\,{m_r\brace j}=q_r^{m_r}(m_r)_j{m_r\brace j}.
\]
Different second-coordinate fibers use disjoint input labels and contribute independent, additive image cardinalities. Therefore their ordinary size generating polynomials multiply and yield the \(q_r\)-th power of the bracketed expression. Multiplying by the \(N\) choices of translation \(s\) and the \(B_{d,r}(p)\) choices of \(L\), then summing over ranks, proves the exact polynomial.

**5. Sharp forbidden interval and endpoint count.** If \(\operatorname{rank}L=d\), then \(L\) is bijective, so the second coordinate \(Lb+s\) identifies \(b\) uniquely, and each first-coordinate map \(a\mapsto La+t(b)\) is bijective. Thus \(F\) is bijective. If \(r<d\), there are at most \(p^r\) output component labels, each holding at most \(N\) points: hence \(|F(Q)|\le p^rN\le N^2/p\). For rank \(d-1\), every component can fill its entire \(N\)-point first-coordinate fiber provided the \(p\) coset classes contributed by its \(p\) input labels are all distinct. This is possible and gives equality. Per output component label there are \(p!\) bijections from input labels to cosets and \((p^{d-1})^p\) choices of coset representatives; there are \(p^{d-1}\) output component labels. Hence the endpoint multiplicity is exactly the boxed expression. Lower linear ranks cannot attain equality. This proves the gap and the sharp endpoint count.

## Verification
The standalone `checker.py` computes the rank generating polynomial using its own finite Stirling recursion and Gaussian counts; separately it enumerates every normal-form map in parameter cases \((p,d)=(2,1),(3,1),(2,2)\) and checks the quandle preservation relation directly on all input pairs. It additionally brute-forces **every** set map of the four-element quandle to verify no other endomorphisms exist in that particular case. The enumerations reproduce, respectively,
\[
\mathcal P_{2,1}(z)=4z+4z^2+8z^4,
\]
\[
\mathcal P_{3,1}(z)=9z+54z^2+18z^3+162z^9,
\]
\[
\mathcal P_{2,2}(z)=16z+336z^2+576z^3+2400z^4+4608z^6+2304z^8+6144z^{16}.
\]
Additional exact polynomial consistency tests for \((p,d)=(3,2),(2,3)\) check total endomorphisms, the automorphism coefficient, and the proper-rank boundary; they do not enumerate all maps in those cases. Run `python3 checker.py`. The captured output is in `checker_output.txt`. The mathematical proof above—not finite experiments—establishes the theorem for arbitrary dimension.

## Relationship to prior work
Jedlička, Pilitowska, Stanovský and Zamojska-Dzienio develop general structural representations of medial and Alexander quandles, including orbit decompositions, in *The structure of medial quandles* (arXiv:1409.8396, first posted 2014-09-30). Such decomposition is a foundational ingredient but does not directly give the displayed set-endomorphism image-cardinality polynomial. Hou's work on *Automorphism groups of Alexander quandles* (2011) addresses bijective maps; the automorphism count above is not advanced as new.

Two closely relevant previously published results were also compared: *Semisimple Alexander-quandle retractions: a transformation–affine factorization and exact image ranks* treats **semisimple** defining operators, hence excludes the nonsplit unipotent operator here; *Complete subquandle size distribution for rank-one unipotent Alexander quandles* treats **the same quandle** but counts embedded subquandles by their sizes, not endomorphisms with prescribed image cardinalities (which additionally requires surjective-map multiplicities for each image). The original claim assessed here is the complete endomorphism image **multiplicity** law and its sharp proper-image gap for the nonsemisimple family. No novelty is asserted for the quandle operation, its orbit decomposition, Stirling occupancy numbers or the previously known separate subquandle enumeration.

## Limitations
The theorem concerns one square-zero Jordan-block family on \(V\oplus V\) over prime fields, not all Alexander quandles or higher nilpotent Jordan types. It does not count endomorphisms onto any **specified** subquandle or classify endomorphisms up to conjugation. The source for Hou's 2011 paper could not be materially inspected in full; the accessible abstract concerns automorphisms and therefore does not establish the nonbijective image-distribution claim, but unknown equivalent older results remain a historical-priority risk. The source comparisons are not an exhaustive proof of novelty. Computational tests are finite, with no inference to all dimensions independent of the proof.

## References
1. P. Jedlička, A. Pilitowska, D. Stanovský, A. Zamojska-Dzienio, *The structure of medial quandles*, arXiv:1409.8396v1 (2014-09-30), https://arxiv.org/abs/1409.8396 ; HTML full text https://arxiv.org/html/1409.8396v2 .
2. X.-D. Hou, *Automorphism groups of Alexander quandles*, J. Algebra 344 (2011), https://doi.org/10.1016/j.jalgebra.2011.06.027 .
3. *Semisimple Alexander-quandle retractions: a transformation–affine factorization and exact image ranks* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-semisimple-alexander-quandle-retractions-a-transformation-affine--117335b68a3e .
4. *Complete subquandle size distribution for rank-one unipotent Alexander quandles* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-subquandle-size-distribution-for-rank-one-unipotent-ale--288df6733df1 .
5. S. Nelson, *Classification of finite Alexander quandles*, arXiv:math/0202281 (2002), https://arxiv.org/abs/math/0202281 .
