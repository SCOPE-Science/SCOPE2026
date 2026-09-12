# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Derived classification of generic Sklyanin planes by elliptic data
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1410
- **Disposition:** AUDIT_2_REJECT
- **Domain:** noncommutative projective geometry
- **Method:** tilting / Beilinson algebra and derived invariants

## Problem

Let k be an algebraically closed field of characteristic zero and let S = S(a,b,c) and S' = S(a',b',c') be generic 3-dimensional Sklyanin algebras (quadratic 3-dimensional Artin-Schelter regular algebras of Type A with smooth elliptic point scheme E and infinite-order translation automorphism sigma, respectively E' and sigma'). Determine whether D^b(qgr S) is triangulated-equivalent to D^b(qgr S') if and only if the pairs (E, sigma) and (E', sigma') are isomorphic up to automorphism of the elliptic curve and inversion sigma -> sigma^{+-1}. A complete answer is either a proof of this if-and-only-if with an explicit tilting object realizing each equivalence, or a rigorous disproof via an explicit pair of non-isomorphic geometric data with equivalent derived tails categories or an explicit pair of isomorphic data whose tails categories are proved inequivalent.

## Attempted claim

Let k be an algebraically closed field of characteristic zero and let S = S(a,b,c) and S' = S(a',b',c') be generic 3-dimensional Sklyanin algebras (quadratic 3-dimensional Artin-Schelter regular algebras of Type A with smooth elliptic point scheme E and infinite-order translation automorphism sigma, respectively E' and sigma'). Determine whether D^b(qgr S) is triangulated-equivalent to D^b(qgr S') if and only if the pairs (E, sigma) and (E', sigma') are isomorphic up to automorphism of the elliptic curve and inversion sigma -> sigma^{+-1}. A complete answer is either a proof of this if-and-only-if with an explicit tilting object realizing each equivalence, or a rigorous disproof via an explicit pair of non-isomorphic geometric data with equivalent derived tails categories or an explicit pair of isomorphic data whose tails categories are proved inequivalent.

## Research outcome

Proved the iff derived-classification of generic Sklyanin planes by elliptic data, with explicit Beilinson tilting object and categorical reconstruction via preprojective invariance.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: TARGET route (research_report.claim_route=TARGET). Forward (<=) direction and tilting numerology are essentially standard: T=O+O(1)+O(2) tilting via Minamoto-Mori Prop 4.4 / AS-regular cohomology and Serre duality, dim B=15, L-adjustment via Pic^3-transitivity and inversion via iota are correct, and numerics in check_beilinson.py were re-executed (ALL CHECKS PASSED) but only verify Hilbert/dimension/toy conjugacy, not categorical recovery. The converse (=>) proof in DRAFT section 4 Steps 2(iii)-(iv) is invalid: from Keller quasi-isomorphism Pi_3^dg(B)~=Pi_3^dg(B') it asserts a graded H0 iso preserving Adams/Veronese degree, intertwining of Nakayama data via Serre commutation, and untwisting by nu along sigma^3 to a triple isomorphism, claiming 'the twist does not create new triples'. No proof is given that the Rickard tilting complex (generally with cohomology in several degrees) induces an Adams-graded quasi-isomorphism, nor that nu-twisted iso of quasi-Veronese S^[3] forces ATV triple isomorphism. This directly contradicts the cited prior literature Itaba-Matsuno arXiv:1806.04940 Thm 4.20 vs Thm 4.16: for Type EC with i=j=0, graded-Morita equivalence holds iff q=tau^l(p)+r with r in E[3], while graded isomorphism holds iff q=tau^l(p) (F_0={o}). Taking same elliptic E (j!=0,1728), p of infinite order generic, r!=o 3-torsion, q=p+r (infinite order, p,q not in E[3]), A(E,sigma_p) and A(E,sigma_q) are generic Sklyanin-type geometric algebras, graded-Morita equivalent hence QGr-equivalent hence D^b(qgr)-equivalent, but (E,t_p) is not isomorphic to (E,t_q) up to curve automorphism and sigma->sigma^{+-1} (conjugacy gives t_{u(p)}, u=+-1, so q=+-p would be required). Thus an explicit prior counterexample refutes the headline iff. The DRAFT's claim that 'no counterexample pairs exist' is false. originality: Fused retrieval (SerpBase/OpenAlex/Crossref/OpenAIRE, no partial failure) plus full-text fetch of the decisive primary source Itaba-Matsuno arXiv:1806.04940 (Math. J. Okayama Univ. 63 (2021)) shows the headline adds nothing new and is already covered/refuted by stronger prior work. Forward direction is a mechanical corollary of Artin-Tate-Van den Bergh triple correspondence (graded iso iff triple iso) plus Zhang twists / Artin-Zhang ampleness. The exact Type EC classification up to isomorphism (Thm 4.16: q=tau^l(p)+r, r in F_i) and up to graded Morita equivalence (Thm 4.20: q=tau^l(p)+r, r in E[3], with torsion condition p-tau^{j-i}(p) in E[3]) already contains the Sklyanin translation case and its E[3]-ambiguity. Minamoto-Mori Adv. Math. 226 (2011) Beilinson/2-RI/preprojective recovery and Keller arXiv:0908.3499 CY-completion invariance are the cited tools, not new results. A prior source need not state the iff verbatim: Itaba-Matsuno substantively implies the negation of the iff by exhibiting graded-Morita-equivalent (hence derived-equivalent) pairs with non-isomorphic (E,sigma). Hence originality FAILS. value: Under the shared STANDA…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The converse relies on cited structural theorems (ATV90 triple correspondence; Minamoto-Mori Thm 4.12/4.14 preprojective recovery with explicit nu-twist nu(S^[3])~=Pi_3(nabla S); Keller Prop. 4.2/Thm 4.6/4.8 CY-completion derived invariance; HIO14 2-RI; Rickard standardness; generic Sklyanin facts of Mori-Ueyama/Smith-Tate) applied in stated scope but not re-proved here; the graded identification passes through the recorded Nakayama twist (untwisted Pi_3(B)~=S on the nose is not claimed). Compu…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
