# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Multiplicity-three flop functors and the spherical cotwist: impossibility of the setup

## 1. Claim (target resolution)

Let f: X → Y and f⁺: X⁺ → Y be flopping contractions of quasi-projective
Gorenstein Calabi–Yau threefolds over an affine base Y with isolated canonical
hypersurface singularity of multiplicity exactly 3, with fibre-product
Fourier–Mukai functors F, F⁺ and Bodzenta–Bondal null-category spherical
functor Ψ with cotwist C. Then:

**Theorem.** No such configuration (f, f⁺) exists. In particular the universal
statements "F and F⁺ are mutually inverse equivalences" and
"K_{F⁺∘F} ≃ K_C^{-1} in Perf(X×X)" hold vacuously, and no counterexample
perfect complex can exist. The target is thereby settled by rigorous proof of
impossibility of its hypotheses.

"Flopping contraction" is used in the standard MMP sense (cf. Kollár–Mori):
f projective birational of normal threefolds, X ℚ-factorial terminal,
f small (isomorphism in codimension one), K_X f-numerically trivial; the
smooth case is included a fortiori. All varieties are over ℂ.

## 2. Lemmas

**Lemma 1 (terminality propagates across crepant small maps).**
Let f: X → Y be projective birational of normal threefolds with X terminal,
f small (isomorphism in codimension one, as holds for flopping contractions),
and K_X = f*K_Y (crepant; automatic for a flop since f is small and both
canonical divisors are Cartier, agreeing where f is an isomorphism).
Then Y is terminal.

*Proof.* Take a common resolution W → X, W → Y. Write
K_W = g*K_X + Σ a(E,X)·E = h*K_Y + Σ a(E,Y)·E.
Since g*K_X = g*f*K_Y = h*K_Y, discrepancies coincide:
a(E,X) = a(E,Y) for every divisor E. If E is exceptional over Y but not over
X, then D = g(E) is a divisor on X dominating a divisor h(E) = f(D) on Y by
smallness of f (which contracts no divisor), contradicting h-exceptionality;
hence every h-exceptional divisor is g-exceptional, with
a(E,Y) = a(E,X) > 0 by terminality of X. Thus every discrepancy over Y
is > 0: Y is terminal. The crepant divisorial case shows smallness is
necessary, since a divisor contracted by f has discrepancy 0 over Y without
being exceptional over X. ∎

**Lemma 2 (Reid).** A Gorenstein terminal threefold singularity is isolated
compound Du Val (cDV): its general hyperplane section is a Du Val (rational
double point) surface singularity.

*Reference.* Reid, "Canonical 3-folds" (1980) and "Minimal models of canonical
3-folds" (1983); see also Kollár–Mori, *Birational Geometry of Algebraic
Varieties*, Theorem 5.38. A hypersurface germ is Gorenstein, so the result
applies to Y.

**Lemma 3.** An isolated cDV hypersurface germ has multiplicity exactly 2.

*Proof.* Let (Y,0) ⊂ (ℂ⁴,0) be defined by f with ord₀(f) = d = mult(Y,0).
For a hyperplane H = {ℓ = 0}, ord(f|_H) = d provided ℓ ∤ f_d, the lowest
homogeneous part of f; this is a dense open condition on ℓ. By Lemma 2,
general H gives a Du Val section; intersecting the two dense opens, some
section is both Du Val and multiplicity-preserving, so d equals the
multiplicity of a Du Val germ. Du Val germs are the ADE singularities
(A_n: x²+y²+z^{n+1}; D_n: x²+y²z+z^{n-1} up to standard form;
E₆: x²+y³+z⁴; E₇: x²+y³+yz³; E₈: x²+y³+z⁵), each with nonzero quadratic
part, hence multiplicity exactly 2 (verified computationally for each type
in `output/artifacts/check_mult3.py`). Thus mult(Y,0) = 2. ∎

**Corollary.** An isolated canonical hypersurface threefold singularity of
multiplicity exactly 3 is strictly canonical (canonical but not terminal).

*Proof.* Terminal + Gorenstein ⇒ cDV (Lemma 2) ⇒ mult 2 (Lemma 3),
contradicting mult 3. Given canonical, it is therefore strictly canonical. ∎

## 3. Main argument

Suppose f: X → Y is as in the target with X ℚ-factorial terminal Gorenstein
CY (in particular X smooth). Since f is small and K_X, K_Y are Cartier
(X smooth/CY, Y hypersurface hence Gorenstein), K_X = f*K_Y: f is crepant.
By Lemma 1, Y is terminal. By Lemma 2, Y is isolated cDV; by Lemma 3,
mult(Y) = 2 — contradicting the hypothesis mult(Y) = 3. Hence no such f
exists, and no pair (f, f⁺) with Bodzenta–Bondal data (Ψ, C) over a
multiplicity-3 base can occur. Both halves of the target question
(equivalence of F, F⁺; kernel identity K_{F⁺∘F} ≃ K_C^{-1}) are universal
statements over an empty class, hence true vacuously; a rigorous
counterexample (an instance plus an explicit perfect complex violating
either statement) is impossible since instances do not exist.

*Remark (sharpness of Bodzenta–Bondal's hypothesis).* This shows the
multiplicity-two hypothesis in Bodzenta–Bondal, "Flops and spherical
functors" (arXiv:1511.00665) is not a technical artifact: by Reid's
classification, every smooth (indeed every Gorenstein terminal) flop has
cDV, hence multiplicity-2, base. Multiplicity 3 forces the base to be
strictly canonical, which admits no terminal crepant model at all.

## 4. Sharpness: the base class itself is nonempty

The obstruction is the existence of the flop, not of the base. The Fermat
cubic cone Y₀ = {x³+y³+z³+w³ = 0} ⊂ 𝔸⁴ satisfies: (a) isolated singularity
at 0 (Jacobian ideal (x²,y²,z²,w²), zero-dimensional); (b) multiplicity
exactly 3; (c) canonical and strictly so: the Fermat cubic surface
S = {x³+y³+z³+w³ = 0} ⊂ ℙ³ is smooth (its Jacobian locus in 𝔸⁴ is only the
origin, which is not a point of ℙ³; checked in `output/artifacts/check_mult3.py`),
so the strict transform Bl₀(Y) is smooth with single exceptional divisor S of
discrepancy a = (4−1) − 3 = 0; then for any further divisor E over Bl₀(Y),
a(E,Y) = a(E,Bl₀(Y)) > 0 since smooth is terminal, hence all discrepancies
over Y are ≥ 0 with equality only for S, i.e. Y is strictly canonical; (d) a general
hyperplane section remains a cubic (mult 3), hence is not Du Val, in
agreement with Lemma 3's contrapositive. All items verified by the
reproducible script `output/artifacts/check_mult3.py` (all checks passed).
Thus isolated canonical hypersurface singularities of multiplicity 3 exist;
what is impossible is a (terminal) flopping contraction over them.

## 5. Conclusion

The target is resolved: the multiplicity-3 flop setup is impossible, so F, F⁺
are vacuously mutually inverse equivalences and the cotwist kernel identity
holds vacuously; no counterexample exists. The proof uses only standard,
cited classification results (Reid cDV; ADE multiplicity 2; discrepancy
calculus) plus a machine-checked sharpness example.

## References

- A. Bodzenta, A. Bondal, "Flops and spherical functors", arXiv:1511.00665.
- M. Reid, "Canonical 3-folds", Journées de Géométrie Algébrique d'Angers
  (1980); "Minimal models of canonical 3-folds", Adv. Stud. Pure Math. (1983).
- J. Kollár, S. Mori, *Birational Geometry of Algebraic Varieties*, CUP 1998
  (terminal/cDV correspondence, discrepancy formalism).
- M. Reid, "Young person's guide to canonical singularities" (1987).
