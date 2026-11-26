# Independent mathematical audit

## correctness

PASS

With the Li–Tang divisibility and internal congruence quoted in RESULT.md lines 39–43, dividing the latter by 3^(m+3) is legitimate and gives a congruence modulo 9 of the normalized integers at adjacent levels. Both possible multipliers reduce to −1 modulo 3. Their cited level-zero extraction gives 144ϑξ+1728ϑξ²; after division by 9 the multipliers reduce to 1 and 0 modulo 3. In the product ϑξ, the characteristic-three rule E_r³=E_(3r) replaces E_2^9 by E_6³ and E_1^12 by E_3^4, yielding qE_6^4. Thus the same mod-3 support controls all m≥0. The Li–Tang paper identity and scope were confirmed in the arXiv PDF opening; the proof uses the precise stated inputs as cited in the frozen record, and the exact numbered external passages were not recovered. For the normalized CM eigenform, support is in n≡1 mod 6. Multiplicativity and the good-prime Hecke recursion give vanishing at odd exponents of inert primes and nonvanishing modulo 3 at even exponents. At split primes the trace ±2u with p=u²+3v² gives a nonzero repeated characteristic root mod 3, and induction gives (e+1)λ^e, zero exactly at e≡2 mod 3. This includes n=1. For the count, local factors are (1+p^(−s))/(1−p^(−3s)) and 1/(1−p^(−2s)), with 2,3 omitted. On removing ζ^(1/2)L(χ_−3)^(1/2), the residual factors are 1+O(p^(−2 Re s)) apart from explicit finite factors, giving a regular positive factor at 1. Selberg–Delange applies to this bounded multiplicative indicator with the fixed character and normally convergent correction; L(1,χ_−3)=π/(3√3), Γ(1/2)=√π, and the two removed local factors give 1/√2 in H(1). This yields the claimed constant and order. Independent bounded code /workspace/review_checks/tagged_counts.py counts directly from designation choices (rather than the frozen eta quotient), and compares with signed pentagonal coefficients: 100,33,11,3 normalized residue checks for m=0,1,2,3 with input degree ≤1200. Its Euler product through primes ≤4,000,000 is 0.3100616431, supporting the approximate size without certifying the last displayed digit. Neither check proves the uniform congruence or the asymptotic. The supplied check.py was inspected, not executed.

## originality

PASS

Pass for the uniform exact prime-factor sharpness classification on the 12·3^m n progression and its asymptotic with explicit constant, to the best of the available evidence. Credit Li–Tang for their bounds and internal congruences and the normalized residue as a derivation from them, and treat CM, Hecke and Selberg–Delange theory as background. Neither the indexed sibling records nor the available published passages establish coverage of the joint assertion.

## value

PASS

This asks a natural question left by an infinite divisibility lower bound: exactly when it is attained and how frequent that is. The answer applies at every level and for composite indices as well as primes; the exponent pattern and explicit counting constant quantify a sparse but infinite sharpness locus rather than merely exhibiting equality or improving one modulus at a chosen index. It gives no claim about higher valuations or a uniform error term.

The dated certificate retains the supplied scientific assessment, sources and limitations.
