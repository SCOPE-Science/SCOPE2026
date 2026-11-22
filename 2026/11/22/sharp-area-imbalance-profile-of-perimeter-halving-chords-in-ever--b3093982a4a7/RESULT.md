# Sharp area-imbalance profile of perimeter-halving chords in every triangle

## Finding
Let \(T\) be a nondegenerate Euclidean triangle and write its sorted side lengths as \(0<a\le b\le c\) and its semiperimeter as \(s=(a+b+c)/2\). A **perimeter-halving chord** joins two boundary points at arclength separation \(s\). Its line partitions \(T\) into two pieces. Let
\[
M(T)=\max_{\ell}\frac{\max\{\operatorname{Area}(T\cap H^+_\ell),\operatorname{Area}(T\cap H^-_\ell)\}}{\operatorname{Area}(T)},
\]
where \(\ell\) ranges over all such chords and \(H^\pm_\ell\) are its two closed halfplanes. Then the exact two-regime formula is
\[
\boxed{M(T)=\begin{cases}\frac{s^2}{4ab},&a\ge s/2,\\[2pt]\frac{s-a}{b},&a\le s/2.\end{cases}}
\]
At the common boundary both expressions agree. The **complete range** of normalized areas cut off by a perimeter-halving line, allowing either side of the line, is \([1-M(T),M(T)]\). Moreover,
\[
\boxed{\frac9{16}\le M(T)<1.}
\]
Equality on the left holds exactly for equilateral triangles. The right endpoint is a sharp but unattained limit when the shortest side tends to zero relative to the semiperimeter. Thus every triangle has a perimeter-halving line whose area discrepancy from half is at least \(1/16\) of the total area; among triangles, the equilateral triangle uniquely minimizes this maximum discrepancy.

## Assumptions and scope
All triangles are strictly nondegenerate (positive area and strict triangle inequalities). Arclength is Euclidean boundary length and area is ordinary planar area. Both orientations of each unoriented cut are allowed in the area-fraction interval. No convex-body generalization, curved cut, or algorithmic approximation is asserted. Ties between side lengths yield symmetry-related equality chords.

## Proof
**1. Cap parameterization.** Consider a chord whose endpoints lie on the two sides of lengths \(u,v\) meeting at one vertex, at distances \(x,y\) from that vertex. Since the two perimeter arcs have equal length \(s\), the arc passing through that vertex has length \(x+y=s\). Because every triangle side is strictly less than \(s\), every perimeter-halving chord is of this form for some vertex (including one endpoint at a vertex). The cut-off triangular cap has normalized area
\[
F_{u,v}(x)=\frac{x(s-x)}{uv},\quad \max(0,s-v)\le x\le\min(u,s).
\]
Every listed interval is nonempty by the strict triangle inequalities. Their union over the three unordered adjacent-side pairs describes every chord.

**2. Maximum triangular cap.** The quadratic \(x(s-x)\) increases up to \(x=s/2\) and decreases afterward. If \(a\ge s/2\), each side is at least \(s/2\); the global cap maximum occurs on the pair \((a,b)\) with \(x=s/2\), giving \(F_{\max}=s^2/(4ab)\). If \(a<s/2\), necessarily \(b,c>s/2\). For the pairs \((a,b)\) and \((a,c)\), the maximum occurs at \(x=a\), giving \((s-a)/b\) and \((s-a)/c\). The remaining pair \((b,c)\) has maximum \(s^2/(4bc)\), which is strictly less than \((s-a)/b\), because \(4c(s-a)>s^2\). Thus \(F_{\max}=(s-a)/b\). This also identifies optimal chords: a centered vertex cap on the two shortest sides in the first strict regime, and a vertex-passing splitter in the second.

**3. Minimum triangular cap and both sides.** A concave quadratic attains its minimum at an endpoint. For a pair \((u,v)\), endpoint cap ratios are \((s-v)/u\) and \((s-u)/v\). For sorted lengths, their global minimum is
\[
F_{\min}=\frac{s-c}{b}=1-\frac{s-a}{b}.
\]
Indeed \(b,c>s/2\), so the map \(z\mapsto z(s-z)\) decreases between \(b\) and \(c\), proving \((s-c)/b\le(s-b)/c\); the remaining four candidate ratios are at least \((s-c)/b\) by side ordering. Consequently \(1-F_{\min}=(s-a)/b\le F_{\max}\), where the inequality is equality in the second regime and in the first follows from \(s^2-4a(s-a)=(s-2a)^2\ge0\). Hence maximizing over both sides produces exactly \(M=F_{\max}\), not a spurious extra complement branch.

The endpoints of a perimeter-halving chord can be described by a boundary starting parameter \(t\) and its antipodal parameter \(t+s\) modulo \(2s\); the resulting area on a chosen oriented side varies continuously with \(t\). Interchanging the endpoints replaces the area fraction \(f\) by \(1-f\). The full interval of area fractions is therefore \([1-M,M]\), with no gaps.

**4. Sharp triangle inequality.** If \(a\ge s/2\), then \(a\le2s/3\), and \(b\le (2s-a)/2\) because \(b\le c\). Therefore
\[
ab\le\frac{a(2s-a)}2\le\frac{4s^2}9,
\]
and \(M=s^2/(4ab)\ge9/16\). Equality throughout forces \(a=b=c=2s/3\). If \(a<s/2\), then \(b\le s-a/2\), whence
\[
M=\frac{s-a}{b}\ge\frac{s-a}{s-a/2}>\frac23>\frac9{16}.
\]
All cap fractions are strictly below one because the cut is nondegenerate and leaves positive area on both sides; thus \(M<1\). In isosceles triangles with \(a\to0^+\) and \(b=c\), the second formula tends to one. This proves sharpness and rigidity.

## Verification
The accompanying `checker.py` independently enumerates all three exact rational cap quadratics for thousands of rational side triples and compares the exact maximum to the two-branch formula. It also samples Euclidean coordinates and computes polygon areas for antipodal boundary-point chords, using a separate shoelace implementation. Both tests passed on the package copy. Finite computations are regression checks, not the proof of the universal statement. The algebraic arguments above cover all admissible triples, including the transition \(a=s/2\).

## Relationship to prior work
Amadtohed, Chaidee, Racha-in and Theerakarn (2022) classify envelopes of fixed-perimeter-ratio chords in triangles; their geometry motivates the cap parameterization but does not give this all-triangle extremal **area-fraction** law or its rigid \(9/16\) bound. Berele and Catoiu (2023) classify extremal **chord lengths** under area or perimeter bisection, a different objective. Kodokostas (2010) counts and locates simultaneous area-and-perimeter equalizers, not worst area discrepancy over all perimeter-halving chords. Classical splitter/cleaver terminology and equalizer existence are not claimed as new. This result is a sharp quantitative complement to those questions, rather than a claim to a new envelope or new equalizer existence theorem.

## Limitations
Priority is provisional: historical triangle-divider literature is extensive, and accessible previews of the 2018 perimeter-bisecting work and 2023 extremal-length paper do not give complete page-by-page coverage. The present theorem is elementary and specific to triangles; the significance claimed is an exact natural full-family invariant with a sharp extremal classification, not a large general convex-geometric breakthrough.

## References
1. N. Amadtohed, T. Chaidee, P. Racha-in, T. Theerakarn, *Dividing the Perimeter of a Triangle into Unequal Proportions*, International Journal of Mathematics and Mathematical Sciences (2022), first posted 2022-06-09, DOI: https://doi.org/10.1155/2022/2751666.
2. A. Berele, S. Catoiu, *Extreme area and perimeter bisectors in a triangle*, Aequationes Mathematicae 98 (2024), first online 2023-10-17, DOI: https://doi.org/10.1007/s00010-023-01001-9.
3. D. Kodokostas, *Triangle Equalizers*, Mathematics Magazine 83 (2010), DOI: https://doi.org/10.4169/002557010X482916.
4. A. Berele, S. Catoiu, *Bisecting the Perimeter of a Triangle*, Mathematics Magazine 91 (2018), DOI: https://doi.org/10.1080/0025570X.2017.1418589.
