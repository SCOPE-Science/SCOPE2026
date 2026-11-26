# Independent mathematical audit

## correctness

PASS

Expanding gives F'(x)=x²(x+1)²−1/30 and the centered odd polynomial z⁵/5−z³/6+7z/240 for z=x+1/2. The seven residue and derivative values check directly. The four regular branches are isometries onto the stated balls: the divided difference is a unit, so the scaled maps induce bijections at every finite precision. For x=−1/2+7t the quotient F(x)/49 has unit linear term and higher coefficients divisible by 7, giving exactly the additional seven indices modulo 7^k on 49Z_7, not additional image points. The other singular classes are Hensel simple roots of F', with F''(1)=12 a unit and the negative branch obtained by F(−1−x)=−F(x). Taylor at c and at 1 gives the square-branch factor 1+7tH(t), u≡6 mod 7, and A≡1 mod 49. The Hensel square root h(t)≡1 has (h(t)−h(s))/7=(tH(t)−sH(s))/(h(t)+h(s)); the denominator is a unit, so t↦th(t) is an isometry, bijective also modulo every 7-power. Input precision k−1 and normalized output precision k−2 give the factor seven even at k=2. The unit-square count is 3·7^(m−2j−1) at each valuation 2j<m; adding zero yields Q, and the square measure 7/16 gives 3/7+2·(7/16)/49=25/56. Continuous image of the compact domain is the closure of the values on dense nonnegative integers. A period must be divisible by seven because the value 1 modulo seven has a unique index class, and for 7|h the valuation of F(h) is that of h by the unit constant term of F(x)/x. Thus the least period is 7^k. A bounded independent direct-polynomial run compared each of 137,256 targets through k=6, confirmed all six image sizes and critical residues, and checked the ninefold fibers: /workspace/branches/5ce1f7b5-0a1e-403d-83d4-cf65227aff66/bounded_histogram.py. The uploaded checker.py was inspected and not executed; the finite run corroborates rather than proves the all-depth statements.

## originality

PASS

The supported distinct claim is the exact local classification of this particular consecutive fourth-power-sum polynomial, including the overlap of the central and regular fibers. No general Hensel or Morse technique is claimed as new. Accessible predecessors and their direct implications do not cover that classification; remaining access risks are explicit.

## value

PASS

The map is a classical power-sum sequence. Its natural local questions are representable residues and how many indices realize each; neither the single-prime reduction nor the measure answers the second question. At the first displayed singular prime the image contains three full balls and two sparse square branches, and one singular branch changes fibers without changing the image. The exact all-depth description and exact index period are useful for local representability and counting without enumerating 7^k indices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
