# Independent mathematical audit

## correctness

PASS

Scale to w=1 and set α=π/n, β=α/2. Curvature in the normal angle is the alternating 0/1 wave (each arc has length α in angle, each intervening vertex cone also has length α by the antipodal constant-width relation). Its odd-harmonic amplitudes are 2(−1)^((ℓ−1)/2)/(πℓ). Dividing each by 1−n²ℓ² for the support function and using area=(1/2)∫(h²−h'²) yields the two-copy deficit f(t)=π^−1 Σ_{ℓ odd}(1+cos(nℓt))/(ℓ²(n²ℓ²−1)). To obtain its closed form, integrate the cosine coefficients of g(x)=sin(β−x/n) by parts twice: their unnormalized integral is [g'(π)(−1)^ℓ−g'(0)]/(ℓ²−1/n²). Matching f'' and using f'(0)=0 and f(α)=0 gives f(t)=−π/4+(n/4)[t+(sinβ+sin(β−t))/cosβ] on [0,α]. The three-copy deficit by polarization is (4/9)Σ f(gap)−f(0)/3. If a positive gap is at least α, its derivative is nonnegative while smaller positive gaps have negative derivative, excluding a stationary minimum. For all gaps in (0,α), equal derivatives imply equal gaps or a complementary pair summing to α; a complementary pair would force the third gap to be α, so the only interior minimum candidate has gaps 2α/3. If a gap is zero, even periodicity and nonnegativity give Σ f≥f(0). Independently, the closed form and the triple-angle identity give f(0)−3f(2α/3)=n sin³(β/3)/cosβ>0, ensuring strict improvement over the boundary. At equal gaps the three curvature waves have alternating upward and downward jumps at intervals α/3 and their average has values 1/3 and 2/3, the curvature of (2/3)B_1+(1/3)R_{3n}(1). The support functions can differ only by a first harmonic, excluded by the common center and n-fold invariance. The disk deficit is quadratic in the centered nonconstant part of the support function, hence one ninth of the regular 3n-gon deficit. Substituting the regular Reuleaux area (also obtained from f(0)) gives the exact stated area and the tan expansion gives π³w²/(3888n²). Strict monotonicity follows from d[s tan(c/s)]/ds=tan u−u sec²u<0 for u=c/s>0 in this range.

## originality

FAIL

An indexed distinct finding gives the same sharp maximum and its equality phases on exactly the same optimization domain, with the same positive deficit and its asymptotic. Its different trigonometric expression is identically equal. The maximizer's body identity, not found verbatim in the inspected finding, follows directly from the covered equality phases and the same record's square-wave curvature formula. This is equivalent or implied scientific coverage, not a finding about historical priority.

## value

FAIL

The odd-copy obstruction and strict optimizing phases are a natural geometric question. As a distinct contribution, however, the frozen result leaves only the description of a known maximizer as a disk–Reuleaux mixture and consequences of the existing deficit formula. The mixture follows immediately by averaging the three supplied curvature functions and adds no separate unknown extremal or structural fact to the checked coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
